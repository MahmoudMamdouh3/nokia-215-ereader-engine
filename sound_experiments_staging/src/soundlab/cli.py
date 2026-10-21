"""
Command Line Interface for Sound Experiments (soundlab).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn
from rich.table import Table

from soundlab.catalog import CatalogDB
from soundlab.config import config
from soundlab.dedup import DeduplicationEngine
from soundlab.ingestion import IngestionEngine
from soundlab.storage import get_free_space_gb

app = typer.Typer(help="Sound Experiments: High-performance audio engineering and dataset toolkit.")
console = Console()


@app.command()
def status():
    """Display system status, disk budgets, and dataset statistics."""
    catalog = CatalogDB()
    stats = catalog.get_stats()

    free_e = get_free_space_gb(config.raw_dir)
    free_d = get_free_space_gb(config.derived_dir)

    table = Table(title="Sound Experiments - System & Dataset Status", show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="dim")
    table.add_column("Value", style="bold green")

    table.add_row("Primary Storage (E:)", f"{free_e:.1f} GB free")
    table.add_row("Overflow Storage (D:)", f"{free_d:.1f} GB free")
    table.add_row("Catalog DB", str(config.catalog_path))
    table.add_row("Total Ingested Sources", str(stats["total_sources"]))
    table.add_row("Active Clean Audio Files", str(stats["active_files_count"]))
    table.add_row("Active Data Size", f"{stats['active_files_bytes'] / (1024.0**2):.1f} MB")
    table.add_row("Quarantined Duplicates", str(stats["duplicates_detected"]))
    table.add_row("Kobe Speech Segments", str(stats["kobe_segments_count"]))
    table.add_row("Total Kobe Speech Time", f"{stats['kobe_total_hours']:.2f} hours")

    console.print(table)


@app.command()
def progress(
    target: int = typer.Option(500, "--target", "-t", help="Target number of clean audio recordings for the master campaign"),
    watch: bool = typer.Option(False, "--watch", "-w", help="Keep running and refresh live in place"),
    interval: float = typer.Option(2.0, "--interval", "-i", help="Seconds between refresh in watch mode"),
):
    """Display real-time visual progress bars for raw harvesting, GPU transcription, and storage quotas."""
    import time
    from rich.live import Live
    from rich.panel import Panel
    from rich.console import Group

    def fetch_stats():
        catalog = CatalogDB()
        with catalog.get_connection() as conn:
            active_count = conn.execute("SELECT COUNT(*) FROM raw_files WHERE status = 'active';").fetchone()[0]
            transcribed_count = conn.execute("SELECT COUNT(*) FROM sources WHERE metadata_json LIKE '%transcript%';").fetchone()[0]
            dup_count = conn.execute("SELECT COUNT(*) FROM duplicates;").fetchone()[0]
            total_bytes = conn.execute("SELECT COALESCE(SUM(file_size_bytes), 0) FROM raw_files WHERE status = 'active';").fetchone()[0]

        size_mb = total_bytes / (1024.0 ** 2)
        size_gb = size_mb / 1024.0
        rem = max(0, target - active_count)
        return active_count, transcribed_count, dup_count, size_gb, size_mb, rem

    if not watch:
        active_count, transcribed_count, dup_count, size_gb, size_mb, rem = fetch_stats()
        console.print("\n[bold cyan]Sound Experiments — Kobe Bryant Master Dataset Progress[/bold cyan]")
        with Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=40),
            TaskProgressColumn(),
            TextColumn("[dim]({task.completed}/{task.total})[/dim]"),
            console=console,
        ) as p:
            p.add_task("[green]Raw Harvest Campaign", total=target, completed=active_count)
            p.add_task("[magenta]GPU AI Transcription", total=max(1, active_count), completed=transcribed_count)

        console.print(
            f"[dim]Archive Size:[/dim] [bold green]{size_gb:.2f} GB[/bold green] ({size_mb:.1f} MB)  |  "
            f"[dim]Duplicates Blocked:[/dim] [bold red]{dup_count}[/bold red]  |  "
            f"[dim]Remaining to Target:[/dim] [bold yellow]{rem} recordings[/bold yellow]\n"
        )
    else:
        console.print("[bold cyan]Starting Live Progress Watch (Press Ctrl+C to stop)...[/bold cyan]\n")
        try:
            with Live(console=console, refresh_per_second=2) as live:
                while True:
                    active_count, transcribed_count, dup_count, size_gb, size_mb, rem = fetch_stats()
                    p = Progress(
                        TextColumn("[bold blue]{task.description}"),
                        BarColumn(bar_width=35),
                        TaskProgressColumn(),
                        TextColumn("[dim]({task.completed}/{task.total})[/dim]"),
                    )
                    p.add_task("[green]Raw Harvest Campaign", total=target, completed=active_count)
                    p.add_task("[magenta]GPU AI Transcription", total=max(1, active_count), completed=transcribed_count)

                    info_table = Table.grid(padding=(0, 2))
                    info_table.add_row(
                        f"[dim]Archive Size:[/dim] [bold green]{size_gb:.2f} GB[/bold green] ({size_mb:.1f} MB)",
                        f"[dim]Duplicates Quarantined:[/dim] [bold red]{dup_count}[/bold red]",
                        f"[dim]Remaining to Target:[/dim] [bold yellow]{rem} recordings[/bold yellow]",
                    )

                    group = Group(
                        "[bold cyan]Sound Experiments — Kobe Bryant Master Dataset (LIVE)[/bold cyan]",
                        p,
                        info_table,
                    )
                    live.update(Panel(group, border_style="cyan"))
                    time.sleep(interval)
        except KeyboardInterrupt:
            console.print("\n[dim]Live watch stopped.[/dim]")


@app.command()
def ingest_url(url: str = typer.Argument(..., help="Direct URL or platform link to download and process")):
    """Download and ingest audio from a web URL."""
    console.print(f"[bold cyan]Ingesting from URL:[/bold cyan] {url}")
    engine = IngestionEngine()
    result = engine.download_url(url)
    if result:
        console.print(f"[bold green]Successfully ingested:[/bold green] {result}")
    else:
        console.print("[bold yellow]Ingestion finished (or duplicate quarantined).[/bold yellow]")


@app.command()
def harvest(
    query: Optional[str] = typer.Option(None, "--query", "-q", help="Specific search query to harvest"),
    limit: int = typer.Option(15, "--limit", "-l", help="Number of recordings per query"),
    workers: int = typer.Option(4, "--workers", "-w", help="Number of concurrent parallel download workers"),
):
    """Automatically search and harvest recordings using parallel worker threads."""
    from soundlab.harvester import AutoHarvester
    harvester = AutoHarvester(max_workers=workers)
    if query:
        console.print(f"[bold cyan]Starting parallel harvest for query:[/bold cyan] {query} (limit {limit}, {workers} threads)")
        count = harvester.harvest_query(query, max_results=limit, max_workers=workers)
    else:
        console.print(f"[bold cyan]Starting comprehensive parallel harvest across all seed queries ({workers} threads)...[/bold cyan]")
        count = harvester.harvest_all_seed_queries(max_per_query=limit, max_workers=workers)
    console.print(f"[bold green]Harvest batch finished! Ingested {count} unique clean recordings.[/bold green]")




@app.command()
def ingest_inbox():
    """Scan and ingest all media dropped in the raw inbox/ folder."""
    console.print(f"[bold cyan]Scanning inbox:[/bold cyan] {config.inbox_dir}")
    engine = IngestionEngine()
    results = engine.process_inbox()
    console.print(f"[bold green]Processed {len(results)} new files from inbox.[/bold green]")


@app.command()
def verify_dedup():
    """Run cryptographic & acoustic verification to prove zero duplicates exist."""
    console.print("[bold cyan]Running zero-duplicate audit across active archive...[/bold cyan]")
    engine = DeduplicationEngine()
    report = engine.verify_database_no_duplicates()

    is_pass = report["status"] == "PASS"
    color = "bold green" if is_pass else "bold red"

    table = Table(title="Deduplication Audit Verification", show_header=True)
    table.add_column("Test Property")
    table.add_column("Result", style=color)

    table.add_row("Active Recordings Audited", str(report["active_records_audited"]))
    table.add_row("Duplicates Detected", str(report["duplicates_detected"]))
    table.add_row("Zero Duplicates Proven", "YES (100% Unique)" if is_pass else "NO (Duplicates Found)")

    console.print(table)

    report_path = config.manifests_dir / "latest_dedup_audit.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    console.print(f"Audit report saved to: [dim]{report_path}[/dim]")


@app.command()
def transcribe_all():
    """Run GPU Whisper ASR transcription and speech-level similarity matching across all audio."""
    from soundlab.speech_pipeline import SpeechPipeline
    console.print("[bold cyan]Starting GPU Whisper transcription across active archive...[/bold cyan]")
    pipeline = SpeechPipeline()
    res = pipeline.process_all_transcripts()
    console.print(f"[bold green]Transcription complete! Processed {res['processed_count']} recordings.[/bold green]")
    if res["duplicate_speeches_found"] > 0:
        console.print(f"[bold yellow]Found {res['duplicate_speeches_found']} matching speeches with different audio/music edits.[/bold yellow]")


@app.command()
def separate_vocals(
    audio_path: str = typer.Argument(..., help="Path to audio file to extract vocals from using UVR5")
):
    """Run UVR5 vocal separation on an audio track to strip background music."""
    from soundlab.speech_pipeline import SpeechPipeline
    console.print(f"[bold cyan]Running UVR5 vocal extraction on:[/bold cyan] {audio_path}")
    pipeline = SpeechPipeline()
    vocal_out = pipeline.separate_vocals_uvr5(Path(audio_path))
    if vocal_out:
        console.print(f"[bold green]Isolated vocals saved to:[/bold green] {vocal_out}")
    else:
        console.print("[bold red]Vocal separation failed or produced no output.[/bold red]")


@app.command()
def run_worker(
    poll_interval: float = typer.Option(3.0, "--poll", "-p", help="Seconds to wait between polling for new audio"),
):
    """Run continuous GPU deep learning worker (ASR + UVR5) in parallel with harvester."""
    from soundlab.worker_pipeline import ContinuousAIWorker
    console.print("[bold cyan]Starting continuous GPU deep learning audio worker...[/bold cyan]")
    worker = ContinuousAIWorker()
    worker.run_loop(poll_interval=poll_interval)




@app.command()
def ui(
    host: str = "127.0.0.1",
    port: int = 7860,
    share: bool = False,
):
    """Launch the Gradio Web Control Center."""
    from soundlab.ui import launch_ui
    console.print(f"[bold green]Starting Sound Experiments Web UI on http://{host}:{port}[/bold green]")
    launch_ui(host=host, port=port, share=share)


if __name__ == "__main__":
    app()
