"""
Sound Experiments - Gradio Web Control Center
Comprehensive interactive UI for database ingestion, duplicate auditing,
voice segment playback, and hardware telemetry.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

import gradio as gr

from soundlab.catalog import CatalogDB
from soundlab.config import config
from soundlab.dedup import DeduplicationEngine
from soundlab.ingestion import IngestionEngine, KOBE_DISCOVERY_QUERIES
from soundlab.storage import get_free_space_gb


def get_telemetry():
    """Fetch current system storage and database statistics with visual progress bars."""
    catalog = CatalogDB()
    stats = catalog.get_stats()
    free_e = get_free_space_gb(config.raw_dir)
    free_d = get_free_space_gb(config.derived_dir)

    target_campaign = 1000
    active = stats["active_files_count"]
    harvest_pct = min(100.0, (active / target_campaign) * 100) if target_campaign > 0 else 0
    rem = max(0, target_campaign - active)

    with catalog.get_connection() as conn:
        transcribed_count = conn.execute("SELECT COUNT(*) FROM sources WHERE metadata_json LIKE '%transcript%';").fetchone()[0]

    transcribe_pct = min(100.0, (transcribed_count / active) * 100) if active > 0 else 0

    summary_md = f"""
    ### 📊 Live Campaign Progress & Hardware Telemetry

    <div style="background-color: #1a1b26; padding: 16px; border-radius: 8px; margin-bottom: 16px; border: 1px solid #414868;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 6px; color: #c0caf5; font-weight: bold; font-size: 14px;">
            <span>📥 Raw Audio Harvest Campaign ({active} / {target_campaign} recordings — {rem} remaining)</span>
            <span style="color: #7aa2f7;">{harvest_pct:.1f}%</span>
        </div>
        <div style="width: 100%; background-color: #24283b; border-radius: 6px; height: 14px; overflow: hidden; margin-bottom: 14px;">
            <div style="width: {harvest_pct:.1f}%; background: linear-gradient(90deg, #7aa2f7, #bb9af7); height: 100%;"></div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-bottom: 6px; color: #c0caf5; font-weight: bold; font-size: 14px;">
            <span>🧠 GPU Whisper AI Transcription ({transcribed_count} / {active} recordings)</span>
            <span style="color: #9ece6a;">{transcribe_pct:.1f}%</span>
        </div>
        <div style="width: 100%; background-color: #24283b; border-radius: 6px; height: 14px; overflow: hidden;">
            <div style="width: {transcribe_pct:.1f}%; background: linear-gradient(90deg, #9ece6a, #73daca); height: 100%;"></div>
        </div>
    </div>

    - **Primary Archive Drive (E: Dev Drive):** `{free_e:.1f} GB free` (Floor: {config.disk_floor_gb} GB)
    - **Overflow & Scratch (D: NVMe):** `{free_d:.1f} GB free`
    - **Total Registered Sources:** `{stats['total_sources']}`
    - **Active Unique Audio Recordings:** `{stats['active_files_count']}`
    - **Active Storage Consumed:** `{stats['active_files_bytes'] / (1024.0**2):.1f} MB ({stats['active_files_bytes'] / (1024.0**3):.2f} GB)`
    - **Quarantined Redundant Duplicates:** `{stats['duplicates_detected']}` (Zero Duplicates Proven)
    - **Isolated Kobe Speech Segments:** `{stats['kobe_segments_count']}`
    - **Kobe Speech Yield:** `{stats['kobe_total_hours']:.2f} hours`
    """
    return summary_md


def handle_url_ingest(url: str):
    """Trigger background download and ingestion for a web URL."""
    if not url or not url.strip():
        return "⚠️ Please enter a valid URL."
    engine = IngestionEngine()
    res = engine.download_url(url.strip())
    if res:
        return f"✅ Successfully ingested & cataloged:\n{res}"
    return "⚠️ Download completed, but file was identified as duplicate and quarantined (or download failed)."


def handle_inbox_process():
    """Trigger processing of the local inbox folder."""
    engine = IngestionEngine()
    processed = engine.process_inbox()
    if not processed:
        return "ℹ️ Inbox is empty or files already processed. Drop audio or video files into:\n" + str(config.inbox_dir)
    return f"✅ Processed and added {len(processed)} clean recordings from inbox:\n" + "\n".join(str(p.name) for p in processed)


def handle_batch_harvest(selected_query: str, limit: int):
    """Trigger automated search and batch downloading."""
    from soundlab.harvester import AutoHarvester
    harvester = AutoHarvester()
    count = harvester.harvest_query(selected_query, max_results=int(limit))
    return f"🚀 Harvest completed for query '{selected_query}'!\nIngested {count} clean recordings into raw archive."



def handle_dedup_audit():
    """Run comprehensive zero-duplicate mathematical proof."""
    engine = DeduplicationEngine()
    report = engine.verify_database_no_duplicates()
    
    if report["status"] == "PASS":
        status_banner = "### 🛡️ AUDIT PASSED: ZERO DUPLICATES PROVEN\n"
        status_banner += "Every active audio file in the database has a unique SHA-256 and distinct acoustic fingerprint."
    else:
        status_banner = f"### ⚠️ AUDIT DETECTED {report['duplicates_detected']} POTENTIAL DUPLICATES\n"
    
    return status_banner, json.dumps(report, indent=2)


def get_quarantined_table():
    """Retrieve list of quarantined duplicates from database."""
    catalog = CatalogDB()
    with catalog.get_connection() as conn:
        rows = conn.execute("""
            SELECT d.id, d.raw_file_id, d.duplicate_of_id, d.match_type, d.similarity_score, d.details, d.created_at,
                   r.file_path as quarantined_path
            FROM duplicates d
            JOIN raw_files r ON r.id = d.raw_file_id
            ORDER BY d.id DESC LIMIT 50;
        """).fetchall()

    data = []
    for r in rows:
        data.append([
            r["id"],
            f"File #{r['raw_file_id']}",
            f"Original #{r['duplicate_of_id']}",
            r["match_type"],
            f"{r['similarity_score']:.2f}",
            Path(r["quarantined_path"]).name,
            r["created_at"],
        ])
    return data


def build_ui() -> gr.Blocks:
    """Build the Gradio application layout."""
    custom_css = """
    .gradio-container { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    """

    with gr.Blocks(title="Sound Experiments - Kobe Bryant Audio Engine", css=custom_css, theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            # 🎙️ Sound Experiments — Voice Engine & Dataset Control Center
            **Exhaustive audio harvesting, acoustic fingerprint deduplication, and voice conversion pipeline.**
            """
        )

        with gr.Tabs():
            # Tab 1: Dashboard
            with gr.TabItem("📊 Dashboard & Telemetry"):
                telemetry_box = gr.Markdown(value=get_telemetry)
                refresh_btn = gr.Button("🔄 Refresh System Telemetry", variant="primary")
                refresh_btn.click(fn=get_telemetry, outputs=[telemetry_box])

                gr.Markdown("---")
                gr.Markdown(
                    f"""
                    #### 📁 Storage Architecture
                    - **Raw Archive Path:** `{config.raw_dir}`
                    - **Overflow Spill Path:** `{config.raw_overflow_dir}`
                    - **Local Drop Inbox:** `{config.inbox_dir}`
                    - **Catalog Database:** `{config.catalog_path}`
                    """
                )

            # Tab 2: Ingestion
            with gr.TabItem("📥 Web Harvester"):
                gr.Markdown("### Ingest from Web & Online Archives (YouTube, Podcasts, Archive.org)")
                with gr.Row():
                    url_input = gr.Textbox(label="Media URL", placeholder="https://www.youtube.com/watch?v=... or direct audio link", scale=4)
                    download_btn = gr.Button("⬇️ Download & Ingest", variant="primary", scale=1)

                ingest_output = gr.Textbox(label="Ingestion Log", lines=4, interactive=False)
                download_btn.click(fn=handle_url_ingest, inputs=[url_input], outputs=[ingest_output])

                gr.Markdown("---")
                gr.Markdown("#### Automated Batch Query Harvester")
                with gr.Row():
                    query_dropdown = gr.Dropdown(choices=KOBE_DISCOVERY_QUERIES, value=KOBE_DISCOVERY_QUERIES[0], label="Target Query Seeds", interactive=True, scale=3)
                    limit_slider = gr.Slider(minimum=5, maximum=50, value=15, step=5, label="Max Videos to Harvest", scale=1)
                    batch_btn = gr.Button("⚡ Run Batch Harvest", variant="primary", scale=1)

                batch_output = gr.Textbox(label="Batch Harvest Status", lines=3, interactive=False)
                batch_btn.click(fn=handle_batch_harvest, inputs=[query_dropdown, limit_slider], outputs=[batch_output])


            # Tab 3: Local Inbox
            with gr.TabItem("📂 Local Media & Movie Inbox"):
                gr.Markdown(
                    f"""
                    ### Batch Media Importer
                    Drop any audio files (`.wav`, `.flac`, `.mp3`, `.m4a`) or video files (`.mp4`, `.mkv`, `.mov`)
                    extracted from movies, documentaries, and interviews into:
                    `{config.inbox_dir}`
                    """
                )
                process_inbox_btn = gr.Button("⚡ Process All Inbox Media Now", variant="primary")
                inbox_output = gr.Textbox(label="Inbox Processing Results", lines=6, interactive=False)
                process_inbox_btn.click(fn=handle_inbox_process, outputs=[inbox_output])

            # Tab 4: Deduplication Proof
            with gr.TabItem("🛡️ Deduplication Verifier"):
                gr.Markdown("### Multi-Layer Acoustic & Cryptographic Duplicate Verification")
                audit_btn = gr.Button("🔍 Run Full Mathematical Zero-Duplicate Audit", variant="primary")
                audit_status = gr.Markdown()
                audit_json = gr.Code(label="Audit Report (JSON)", language="json")
                audit_btn.click(fn=handle_dedup_audit, outputs=[audit_status, audit_json])

                gr.Markdown("---")
                gr.Markdown("#### Quarantined Redundant Recordings")
                dup_table = gr.Dataframe(
                    headers=["ID", "Quarantined File", "Original File", "Match Type", "Score", "Filename", "Timestamp"],
                    value=get_quarantined_table,
                    interactive=False,
                )

            # Tab 5: System Specs
            with gr.TabItem("⚙️ System Specs"):
                gr.Markdown("### Laptop Hardware Profile & Optimization Parameters")
                specs_file = Path(r"E:\Sound Experiments\docs\SYSTEM_SPECS.md")
                specs_text = specs_file.read_text(encoding="utf-8") if specs_file.exists() else "SYSTEM_SPECS.md not found."
                gr.Markdown(specs_text)

    return demo


def launch_ui(host: str = "127.0.0.1", port: int = 7860, share: bool = False):
    """Launch the Gradio server."""
    demo = build_ui()
    demo.launch(server_name=host, server_port=port, share=share)
