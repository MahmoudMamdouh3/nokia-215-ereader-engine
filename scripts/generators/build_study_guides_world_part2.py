"""
Generates master-level study guides for World Classics & Epics (Part 2):
- 59_The_Castle
- 60_The_Odyssey
- 61_The_Iliad
- 62_The_Divine_Comedy
- 63_The_Magic_Mountain
- 64_One_Thousand_And_One_Nights
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 59 The Castle
    {
        "id": "59_The_Castle",
        "content_en": """# Comprehensive Study Guide: The Castle (Das Schloss)
**Author:** Franz Kafka  
**Written:** 1922 (Published 1926)  
**Genre:** Absurdist Allegory / Existential Parable  

---

## 1. Context & The Inaccessible Authority
Kafka’s final, unfinished masterwork depicts an individual’s desperate quest for legitimate recognition and belonging against an aloof, invisible, and incomprehensible bureaucratic hierarchy.

---

## 2. In-Depth Chapter Breakdown
- **Arrival in the Snow**: Late on a snowy evening, the protagonist, known only as **K.**, arrives in a desolate, freezing village. He claims to have been summoned by the Castle authorities as a Land Surveyor (*Landvermesser*). Village officials at the inn treat him with intense suspicion, demanding papers.
- **The Inaccessible Castle & The Assistants**: The Castle looms above the village, obscured by mist and snow, appearing neither like a fortress nor a palace, but a rambling cluster of decaying cottages. K. attempts to walk up to the Castle, but the road continuously circles away. Two bizarre, infantile assistants (Arthur and Jeremias) are assigned to him, acting as constant, meddlesome spies.
- **The Letter from Klamm & Frieda**: K. receives an ambiguous letter from Castle official **Klamm**, welcoming him. K. seeks access to Klamm through Frieda, a barmaid at the Herrenhof inn and Klamm’s mistress. K. seduces Frieda, taking her away from Klamm and proposing marriage, viewing her primarily as a conduit to penetrate Castle authority.
- **The Barnabas Family**: K. befriends the messenger Barnabas, learning that his family was cast into complete social pariahdom simply because his sister Amalia tore up an obscene letter from Castle official Sortini, refusing to submit to his degradation. The village ostracized them without any formal order from the Castle.
- **Exhaustion & Kafka's Intended Ending**: Frieda abandons K., exhausted by his relentless, calculating obsession with Klamm. K. continues to wander between innkeepers, secretaries (Bürgel), and coachmen, worn down by endless bureaucratic paradoxes. Max Brod noted that Kafka intended the novel to end with K. dying of physical exhaustion; only on his deathbed does a messenger arrive from the Castle declaring that K. had no legal claim to reside in the village, but in view of certain auxiliary circumstances, he is permitted to live and work there.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: القلعة (The Castle)
**المؤلف:** فرانتس كافكا (Franz Kafka)  
**سنة التأليف:** 1922 (نُشرت 1926)  
**التصنيف الأدبي:** أدب العبث والرمزية الوجودية / السلطة الغائبة والمنفى الإنساني  

---

## 1. السياق وفلسفة السلطة المتعالية
رواية كافكا الأخيرة غير المكتملة؛ تمثل قمة التعبير الرمزي عن سعي الإنسان المستميت للحصول على اعتراف وشرعية وانتماء في مواجهة سلطة غامضة، متعالية، مستحيلة المنال، لا يمكن التواصل معها أو فهم قراراتها.

---

## 2. المسار الدرامي لأحداث الرواية
- **الوصول في الثلج**: يصل البطل المعروف فقط بحرف **ك.** (K.) في ليلة شتوية مثلجة إلى قرية كئيبة تابعة للقلعة. يدعي أنه مسّاح أراضٍ استدعته سلطات القلعة للعمل. يستقبله أهل القرية في الحانة بارتياب شديد ويطالبونه بتصريح إقامة رسمي.
- **القلعة المنيعة والمساعدان العبثيان**: تلوح القلعة فوق التل يلفها الضباب والجليد، كأنها مسخ معماري هجين. يحاول ك. المشي نحو القلعة، فتلتف به الطرق وتبعده دوماً عن الهدف. يُعين له مساعدان ساذجان متطفلان (آرثر وجيريمياس) يتصرفان كأطفال ومخبرين يراقبون كل حركاته.
- **رسالة كلام وفريضا**: يتلقى ك. رسالة غامضة من رئيس مكتب القلعة "كلام" ترحب به. يحاول ك. الوصول لكلام عبر عشيقته "فريضا" ساقية الحانة، فيغويها ويخطبها كوسيلة وحيدة لاختراق جدار القلعة والوصول للمسؤول الغامض.
- **مأساة عائلة بارناباس**: يتعرف ك. على رسول القلعة بارناباس، ويكتشف أن عائلته منبوذة تماماً في القرية لمجرد أن شقيقته أماليا مزقت رسالة غير لائقة أرسلها مسؤول القلعة سورتيني ورفضت الخضوع له؛ حيث نبذهم أهل القرية تطوعاً دون أي أمر رسمي صادر من القلعة!
- **الإنهاك والنهاية المقدرة**: تهجره فريضا بعد أن أرهقها هوسه الأعمى بالوصول للقلعة. يظل ك. يتخبط بين البيروقراطيين والسكرتارية في دوامة من التفسيرات والتعقيدات التي لا تنتهي. ذكر ماكس برود أن كافكا كان ينوي إنهاء الرواية بموت ك. من فرط الإعياء والإنهاك التام؛ وفي لحظة احتضاره فقط، يصل رسول القلعة حاملاً قراراً بأنه ليس له حق قانوني في البقاء بالقرية، ولكن نظراً لظروف معينة، يُسمح له بالعيش والعمل هنا!
"""
    },

    # 60 The Odyssey
    {
        "id": "60_The_Odyssey",
        "content_en": """# Comprehensive Study Guide: The Odyssey
**Author:** Homer (Ancient Greece)  
**Period:** c. 8th Century BCE  
**Genre:** Ancient Epic Poetry / Mythological Hero's Journey  

---

## 1. Epic Scale & The Hero's Return (Nostos)
Composed of **24 Books** in dactylic hexameter, *The Odyssey* is the foundational epic of Western literature. It celebrates *metis* (cunning, intellectual resourcefulness, and adaptability) embodied by Odysseus, King of Ithaca, during his ten-year voyage home following the Trojan War.

---

## 2. In-Depth Structural Breakdown

### Books 1–4: The Telemachy
In Ithaca, Odysseus has been missing for twenty years. Over a hundred arrogant suitors overrun his palace, devouring his livestock and pressuring his faithful wife, **Penelope**, who stalls them by weaving and secretly unweaving a burial shroud for Lord Laertes each night. Guided by the goddess Athena, his son **Telemachus** travels to Pylos and Sparta seeking news of his father.

### Books 5–8: Calypso and the Phaeacians
Odysseus is trapped on the paradise island of Ogygia by the nymph **Calypso**, who offers him immortality if he stays as her lover. Longing for his mortal home and wife, Odysseus weeps on the shore. Hermes commands Calypso to release him. Building a raft, Odysseus is shipwrecked by Poseidon's wrath, washing ashore on the island of Scheria, where the Phaeacian princess Nausicaa rescues him.

### Books 9–12: Odysseus’s Great Wanderings (The Apologue)
At King Alcinous's court, Odysseus recounts his legendary trials:
1. *The Cicones & The Lotus-Eaters*: Men lose their desire to return home after eating the intoxicating lotus fruit.
2. *The Cyclops Polyphemus*: Odysseus and his men are trapped in the cave of the one-eyed giant Polyphemus. Odysseus blinds the monster with a burning stake, telling him his name is "Nobody" (*Outis*). As they escape beneath rams, Odysseus’s hubris takes over: he shouts his real name, prompting Polyphemus to invoke his father **Poseidon** to curse the voyage.
3. *Aeolus & The Laestrygonians*: The wind king Aeolus gifts a bag of winds, which foolish sailors open near Ithaca, blowing them back. Giant cannibals (Laestrygonians) sink eleven ships.
4. *Circe & The Underworld*: The sorceress Circe turns his men into swine. Protected by the herb moly, Odysseus compels her to restore them. Circe sends him to the **Underworld (Nekuia)**, where the blind prophet Tiresias warns him of trials, and Odysseus weeps seeing his deceased mother and fallen Trojan comrades (Agamemnon, Achilles).
5. *Sirens, Scylla and Charybdis, and Cattle of the Sun*: Odysseus lashes himself to the mast to hear the Sirens' enchanting song; navigates between the six-headed monster Scylla and the whirlpool Charybdis. On Thrinacia, his starving men slaughter the sacred cattle of Helios, leading Zeus to destroy their last ship with a thunderbolt. Only Odysseus survives.

### Books 13–24: The Homecoming and The Slaughter of the Suitors
- **The Beggar’s Disguise**: Athena transforms Odysseus into an elderly beggar. He stays with his loyal swineherd Eumaeus and reveals his identity to Telemachus. Entering his palace, his faithful old hound Argos recognizes his master's voice and dies in peace.
- **The Contest of the Bow**: Penelope announces she will marry whoever can string Odysseus’s great hunting bow and shoot an arrow through twelve axe-heads. Every suitor fails. The old beggar steps forward, strings the bow effortlessly like a harpist, and shoots clean through the twelve axes.
- **The Slaughter (Mnesterophonia)**: Shedding his rags, Odysseus, Telemachus, and two loyal herdsmen bar the doors. Odysseus shoots the arrogant lead suitor Antinous through the throat, executing all 108 suitors.
- **The Bed of Olive Wood & Peace**: Penelope tests Odysseus by ordering their bridal bed moved. Odysseus objects, revealing the secret: he built the bed into the living stump of an ancient olive tree. Weeping with joy, Penelope embraces him. Athena intervenes to halt a blood feud with the suitors' families, restoring eternal peace to Ithaca.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الأوديسة (The Odyssey)
**المؤلف:** هوميروس (اليونان القديمة)  
**تاريخ التأليف:** القرن الثامن قبل الميلاد تقريباً  
**التصنيف الأدبي:** ملحمة شعرية إغريقية كبرى / أدب العودة والبطولة والذكاء  

---

## 1. البناء الملحمي وفلسفة الدهاء (Metis)
تتألف الأوديسة من **24 نشيداً ملحمياً** وتعد حجر الزاوية في تراث الأدب الإنساني. تمجد الملحمة ذكاء ودهاء وصبر البطل "أوديسيوس" ملك إيثاكا خلال رحلة عودته الشاقة التي دامت 10 سنوات عقب انتهاء حرب طروادة.

---

## 2. المسار الدرامي لأناشيد الملحمة الـ 24

### الأناشيد 1–4: التليماكيا (رحلة الابن)
تفتتح الملحمة في إيثاكا؛ غاب أوديسيوس 20 عاماً وظن الجميع أنه مات. يحتل قصره أكثر من مئة خاطب وقح، ينحرون مواشيه ويهدرون أمواله ويضغطون على زوجته الوفية **بينيلوبي** للزواج. تماطلهم بينيلوبي بحيلة حياكة كفن والد زوجها لايرتيس، حيث تحيكه نهاراً وتنقضه خلسة ليلاً. يسافر ابنه **تليماك** بتوجيه من الإلهة أثينا إلى بيلوس وإسبرطة للبحث عن أخبار والده.

### الأناشيد 5–8: حورية البحر كاليبسو وشعب الفياكيين
يقبع أوديسيوس أسيراً في جزيرة أوغيغيا عند الحورية **كاليبسو** التي تعرض عليه الخلود والشباب الدائم إذا بقي حبيبها. يرفض أوديسيوس ويبكي يومياً على صخرة الشاطئ شوقاً لوطنه وزوجته الفانية. يأمر زيوس بإطلاق سراحه، فيبني طوفاً خشبياً، لكن إله البحر بوزيدون يدمر طوفه بعاصفة هوجاء، فينجو سباحة لجزيرة الفياكيين حيث تنقذه الأميرة ناوسيكا.

### الأناشيد 9–12: أهوال الرحلة البحرية (اعترافات أوديسيوس)
يروي أوديسيوس لملك الفياكيين الأهوال الأسطورية التي لاقاها:
1. *آكلو اللوتس*: ثمرة تفقد البحارة ذاكرتهم ورغبتهم في العودة.
2. *العملاق بوليفيموس*: يحبسهم العملاق ذو العين الواحدة في كهفه ويلتهم رفاقه. يسقيه أوديسيوس الخمر ويفقأ عينه بوتد مشتعل، ويخبره بمكر أن اسمه "لا أحد"! وعندما يصرخ العملاق لإخوته: "لا أحد يقتلني!" يتجاهلونه. لكن عند هروب أوديسيوس بالبحر يصرخ باسمه الحقيقي بغرور، فيدعو عليه العملاق والده إله البحر بوزيدون بلعنة الموت والتيه.
3. *ساحرة الخنازير سيرسي وعالم الأموات*: تحول الساحرة رفاقه لخنازير، لكنه يرغمها على إعادتهم ببذرة العشب السحرية. تنصحه بزيارة **عالم الموتى (هاديس)**؛ حيث يقابل روح النبي الأعمى تيريسياس، ويبكي لرؤية والدته الراحلة ورفاق حرب طروادة (أغاممنون، وأخيل).
4. *السيرينات ووحشا سكيلا وخاريبديس*: يربط أوديسيوس نفسه بصاري السفينة لسماع غناء السيرينات الساحر دون أن يلقي بنفسه في البحر، ويعبر بين وحش الصخور ذي الرؤوس الستة ودوامة البحر المميتة.
5. *ثيران إله الشمس والهلاك*: يذبح بحارته الجياع ثيران الشمس المقدسة، فينزل زيوس صاعقة تدمر سفينتهم بالكامل ويهلك الجميع، ولا ينجو سوى أوديسيوس متشبثاً بقطعة خشب.

### الأناشيد 13–24: العودة والانتقام واسترداد العرش
- **التنكر في زي الشحاذ**: تعيده سفينة الفياكيين لإيثاكا. تحوله أثينا لعجوز شحاذ رث الثياب، فيلجأ لكوخ خادمه الوفي إيومايوس ويكشف هويته لابنه تليماك. وعند دخوله القصر، يتعرف عليه كلبه العجوز المخلص "أرغوس" بصوته ويهز ذيله ويموت فرحاً.
- **مبارزة القوس والخواتم**: تعلن بينيلوبي مسابقة: من يستطيع وتر قوس أوديسيوس الضخم ورمي سهم عبر فتحات 12 فأساً حديدية ستتزوجه. يعجز جميع الخطباء المتغطرسين. يتقدم الشحاذ العجوز ويوتر القوس بسهولة عازف قيثارة ويطلق السهم عبر الفؤوس الاثنتي عشرة!
- **مجزرة الخطاب والتطهر**: يلقي أوديسيوس أسماله، ويغلق تليماك الأبواب. يرمي أوديسيوس زعيم الخطاب أنتينيوس بسهم في حنجرته، ويبيد هو وابنه وخادماه جميع الخطاب الـ 108.
- **سر شجرة الزيتون والسلام الأبدي**: تختبر بينيلوبي زوجها وتأمر بنقل سريرهما، فيغضب أوديسيوس كاشفاً السر: إنه نحت السرير بيده في جذع شجرة زيتون حية في قلب المنزل لا يمكن تحريكها! تنهار بينيلوبي باكية وتحتضنه بحرارة بعد 20 عاماً من الانتظار. تتدخل أثينا لمنع الثأر وتفرض السلام الخالد على أرض إيثاكا.
"""
    },

    # 61 The Iliad
    {
        "id": "61_The_Iliad",
        "content_en": """# Comprehensive Study Guide: The Iliad
**Author:** Homer (Ancient Greece)  
**Period:** c. 8th Century BCE  
**Genre:** Heroic Epic Poetry / The Tragedy of War  

---

## 1. Core Theme: The Wrath of Achilles (Menin)
*"Sing, O goddess, the anger of Achilles son of Peleus, that destructive anger which brought ten thousand sorrows upon the Achaeans..."*  
The opening word of the *Iliad* is **Mēnin (Wrath)**. Set during the tenth and final year of the siege of Troy, Homer crafts an unflinching exploration of martial honor (*timē*), glory (*kleos*), mortality, and the devastating cost of war.

---

## 2. In-Depth Structural Breakdown

### Books 1–8: The Quarrel and the Achaean Crisis
- **The Insult**: King Agamemnon offends the god Apollo by refusing to ransom the priest's daughter Chryseis. Apollo strikes the Greek camp with plague. Agamemnon surrenders her, but forcibly seizes **Briseis**, the war-prize of Greece's greatest champion, **Achilles**. Enraged by this dishonor, Achilles withdraws from the war and begs his mother, the sea-nymph Thetis, to convince Zeus to grant victory to the Trojans until the Greeks beg for his return.
- **The Duel of Paris and Menelaus**: Trojan prince Paris duels Menelaus to end the war, but Aphrodite spirits the cowardly Paris away into Helen's bedchamber.
- **The Trojan Onslaught**: Led by the noble prince **Hector**, the Trojans push the Greeks back to their beached ships, breaching the defensive wall.

### Books 9–16: The Embassy and the Death of Patroclus
- **The Failed Embassy (Book 9)**: Agamemnon sends Odysseus, Ajax, and Phoenix with immense gifts and the return of Briseis, pleading for Achilles’s help. Achilles adamantly refuses, questioning the entire ethos of heroic sacrifice: *"Fate is the same for the man who holds back, the same if he fights his bravest."*
- **Hector at the Ships**: Hector sets fire to the Greek fleet. Seeing disaster, Achilles’s beloved companion **Patroclus** begs to wear Achilles's armor to terrify the Trojans. Achilles relents, commanding Patroclus only to drive them from the ships and not assault Troy.
- **The Fall of Patroclus (Book 16)**: Swept away by battle fury, Patroclus attacks the walls of Troy. Apollo stuns him, Euphorbus wounds him, and Hector strikes the fatal blow, stripping Achilles's armor.

### Books 17–24: Fury, Vengeance, and Reconciliation
- **The Grief of Achilles**: Learning of Patroclus's death, Achilles weeps in agony, smearing black ash on his face. His grief transforms into apocalyptic rage. Hephaestus forges divine new armor and a monumental shield depicting the entire cosmos and human civilization.
- **The Return to Slaughter**: Achilles rejoins battle, choking the river Scamander with Trojan corpses. He battles the river god himself until gods intervene.
- **The Slaying of Hector (Book 22)**: Outside the walls of Troy, Hector stands alone. Seeing Achilles blazing like a star, Hector panics and flees three times around the walls of Troy. Athena tricks Hector into turning to fight. Achilles pierces Hector’s neck with a spear. Dying, Hector begs for his body to be ransomed to his parents; Achilles snarls that he wishes he had the stomach to eat Hector raw. Achilles lashes Hector's ankles to his chariot and drags the corpse in the dust around Troy before his weeping parents, Priam and Hecuba.
- **The Ransom of Hector (Book 24)**: King Priam sneaks into the Greek camp at night and enters Achilles's tent. The aged king falls to his knees, kisses the hands that slaughtered his sons, and speaks: *"Think of your own father, Achilles, and have pity on me."* Achilles breaks down weeping for his own aging father Peleus and for Patroclus. His ferocious wrath dissolves into universal human empathy. Achilles returns Hector’s body and grants an eleven-day truce. The epic concludes not with the fall of Troy, but with Hector’s solemn funeral rites: *"Such was their burial of Hector, breaker of horses."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الإلياذة (The Iliad)
**المؤلف:** هوميروس (اليونان القديمة)  
**تاريخ التأليف:** القرن الثامن قبل الميلاد تقريباً  
**التصنيف الأدبي:** أم الملاحم الإغريقية / تراجيديا الحرب والغضب والكرامة  

---

## 1. الفكرة الجوهرية: غضب أخيل (Menin)
تفتتح الملحمة بأولى وأشهر الكلمات في تاريخ الأدب: *"غنّي يا ربة الشعر غضب أخيل بن بيليوس، ذلك الغضب المشؤوم الذي جلب آلاف الويلات على الإغريق..."*. تدور أحداث الإلياذة في السنة العاشرة والأخيرة من حصار طروادة؛ مقدمة تشريحاً فلسفياً صارماً لمعنى الشرف والمجد العسكري وفناء الإنسان وبشاعة الحروب.

---

## 2. المسار الدرامي لأناشيد الملحمة الـ 24

### الأناشيد 1–8: الخلاف واعتزال أخيل
- **إهانة أغاممنون**: يرفض القائد الإغريقي الأعلى أغاممنون إعادة ابنة كاهن أبولو، فينزل الإله وباء الطاعون في المعسكر. يضطر أغاممنون لإعادتها، لكنه يعوض كبرياءه بانتزاع الفتاة الأسيرة **بريسيس** من خيمة بطل الإغريق الأول **أخيل**. يشعر أخيل بإهانة شرفه العسكري، فيعتزل القتال ويسحب جيشه، راجياً أمه حورية البحر ثيتيس أن تطلب من زيوس نصرة الطرواديين حتى يتوسل الإغريق لعودته.
- **مبارزة باريس ومينلاوس**: يتبارز باريس مع زوج هيلين لاستردادها، لكن أفروديت تنقذ باريس وتخفيه في غرفة هيلين.
- **الهجوم الطروادي الكاسح**: يقود أمير طروادة النبيل **هيكتور** هجوماً ساحقاً، محطماً السور الدفاعي للإغريق ومحاصراً سفنهم.

### الأناشيد 9–16: الوفد الفاشل وموت باتروكلس
- **وفد المصالحة الفاشل (النشيد 9)**: يرسل أغاممنون أوديسيوس وأياكس مع هدايا خيالية متوسلين عودة أخيل، لكن أخيل يرفض بغطرسة مشككاً في جدوى الموت من أجل المجد: *"الموت مصير متساوٍ لمن يقاتل بضراوة ولمن يجلس خامل الذكر"*.
- **حريق السفن وفداء باتروكلس**: يشعل هيكتور النار في أولى سفن الإغريق. يهرع الصديق الروحي لأخيل **باتروكلس** متوسلاً السماح له بارتداء درع أخيل لإرهاب الطرواديين. يوافق أخيل محذراً إياه من الاكتفاء بطردهم من السفن وعدم مهاجمة أسوار طروادة.
- **مقتل باتروكلس (النشيد 16)**: يندفع باتروكلس في نشوة المعركة نحو أسوار طروادة، فيصيبه أبولو ويطعنه يوفوربوس، ويجهز عليه هيكتور برمحه وينزع درع أخيل عن جثته.

### الأناشيد 17–24: الانتقام الدموي والتصالح الإنساني
- **حزن أخيل وجنون الغضب**: يلطخ أخيل وجهه بالرماد الأسود باكياً رفيقه بنواح يفطر القلوب، ويتحول حزنه إلى بركان غضب مدمر. يصنع له الإله هيفايستوس درعاً إلهياً جديداً مرسوماً عليه الكون والإنسانية برمتها.
- **مجزرة النهر ومصرع هيكتور**: يعود أخيل للمعركة كإعصار جارف؛ يسد مجرى نهر سكاندر بجثث الطرواديين. يقف هيكتور وحيداً خارج الأسوار؛ وحين يرى أخيل يلمع كشهاب ساقط، يصيبه الرعب ويهرب حول أسوار طروادة لثلاث دورات كاملة قبل أن تخدعه أثينا للوقوف والقتال. يطعن أخيل هيكتور في رقبته؛ وقبل أن يلفظ أنفاسه يرجوه هيكتور إعادة جثته لأبويه، فيرد أخيل بوحشية: *"ليتني أستطيع تمزيق لحمك وأكله نيئاً!"*. يربط جثة هيكتور في عربته ويجرها في التراب حول طروادة أمام عيني والده الملك بريام وأمه هكوبا.
- **فداء الجثة واللقاء الخالد (النشيد 24)**: يتسلل الملك الشيخ بريام ليلاً لمعسكر الإغريق ويدخل خيمة أخيل بمفرده. يركع الملك العجوز ويقبل يدي أخيل القاتلتين اللتين أبادتا أبناءه، قائلاً: *"تذكر أباك العجوز يا أخيل وارحمني!"*. ينفجر أخيل بالبكاء تذكراً لوالده وباتروكلس، وتذوب وحشية الغضب في لحظة رحمة إنسانية خالدة. يعيد أخيل جثة هيكتور ويمنح الطرواديين هدنة 11 يوماً للدفن. وتنتهي الملحمة بجنازة هيكتور المهيبة: *"وهكذا كانت مراسم دفن هيكتور مروض الخيول"*.
"""
    },

    # 62 The Divine Comedy
    {
        "id": "62_The_Divine_Comedy",
        "content_en": """# Comprehensive Study Guide: The Divine Comedy (La Divina Commedia)
**Author:** Dante Alighieri  
**Written:** 1308–1320  
**Genre:** Epic Theological Poetry / Allegory / Masterpiece of World Literature  

---

## 1. Scale & Triadic Architecture
Written in Italian *terza rima* across 14,233 lines and **100 Cantos** (1 introductory + 33 for each realm), Dante’s journey represents the soul’s ascent from the darkness of sin to divine vision.
- **Virgil** = Human Reason and Classical Philosophy
- **Beatrice** = Divine Grace and Christian Revelation
- **St. Bernard of Clairvaux** = Mystical Contemplation

---

## 2. The Three Realms Breakdown

### 1. Inferno (Hell)
- **The Dark Wood & The Gate**: Lost in a dark wood on Good Friday 1300, Dante is blocked by three beasts (Leopard of Fraud, Lion of Pride, She-Wolf of Greed). Roman poet Virgil arrives to guide him through the gate of Hell: *"Abandon all hope, ye who enter here"* (*Lasciate ogne speranza, voi ch'intrate*).
- **The Nine Circles of Contrapasso (The Punishment Fits the Crime)**:
  1. *Limbo*: Virtuous pagans (Homer, Plato, Aristotle).
  2. *Lust*: Paolo and Francesca blown forever by relentless whirlwinds.
  3. *Gluttony*: Mired in vile icy slush under Cerberus.
  4. *Greed*: Hoarders and spendthrifts rolling colossal boulders against each other.
  5. *Anger & Sullenness*: Submerged in the muddy River Styx.
  6. *Heresy*: Trapped in flaming iron tombs.
  7. *Violence*: Murderers boiled in river of blood (Phlegethon); suicides turned into bleeding trees devoured by Harpies; blasphemers under burning sand.
  8. *Fraud (Malebolge)*: Ten stony ditches punishing pimps, flatterers, simoniacs, false prophets, corrupt politicians, hypocrites, thieves, and sowers of discord.
  9. *Treachery (Cocytus)*: A frozen lake of ice. Traitors frozen to their necks. At the very center, the colossal, three-headed winged **Lucifer** is trapped waist-deep in ice, chewing the three ultimate traitors in human history: **Judas Iscariot** (who betrayed Jesus), and **Brutus and Cassius** (who betrayed Julius Caesar). Virgil and Dante climb down Satan’s shaggy fur to emerge on the other side of the world: *"And then we emerged to see the stars once more."*

### 2. Purgatorio (Purgatory)
An island mountain in the Southern Hemisphere with seven cornices purging the Seven Deadly Sins (Pride, Envy, Wrath, Sloth, Greed, Gluttony, Lust). Souls willingly suffer with joy because they are assured of salvation. At the summit in the Earthly Paradise (Eden), Virgil must depart, and Beatrice appears in radiant glory to guide Dante.

### 3. Paradiso (Paradise)
Dante ascends through the nine celestial spheres of the Ptolemaic cosmos (Moon, Mercury, Venus, Sun, Mars, Jupiter, Saturn, Fixed Stars, Primum Mobile), meeting saints, theologians, and martyrs. Ascending to the Empyrean beyond space and time, St. Bernard prays to the Virgin Mary on Dante’s behalf. Dante gazes into the Beatific Vision—the Triune God depicted as three equal circles of light. The poem ends in total mystical communion:  
**"The Love that moves the sun and the other stars."** (*L'amor che move il sole e l'altre stelle*).
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الكوميديا الإلهية (The Divine Comedy)
**المؤلف:** دانتي أليغييري (Dante Alighieri)  
**سنوات التأليف:** 1308–1320  
**التصنيف الأدبي:** الملحمة اللاهوتية الشعرية الكبرى / الأدب الإيطالي الخالد / الرحلة الصوفية  

---

## 1. الهيكل الثلاثي والرمزية الكبرى
تتألف الملحمة من 14,233 بيتاً و **100 أنشودة** مقسمة بالتساوي على العوالم الثلاثة؛ تجسد رحلة النفس الإنسانية من ظلمات الخطيئة إلى التطهير ثم النعيم الإلهي المطلق:
- **فرجيل** (الشاعر الروماني) = العقل البشري والفلسفة الأرضية.
- **بياتريتشه** (ملهمة دانتي) = النعمة الإلهية والإيمان الخالص.
- **القديس برنارد** = التأمل الروحي والشهود الصوفي.

---

## 2. المسار الملحمي للعوالم الثلاثة

### أولاً: الجحيم (Inferno - 9 دوائر)
- **الغابة المظلمة وبوابة الجحيم**: يضل دانتي طريقه في غابة مظلمة محاطاً بوحوش الشهوة والغرور والجشع. يظهر فرجيل لإنقاذه ويدخلان بوابة الجحيم الشهيرة المكتوب فوقها: *"اتركوا كل أمل، يا من تدخلون هنا"*.
- **دوائر الجحيم وقانون القصاص العادل (Contrapasso)**:
  1. *الليمبو*: الفضلاء من غير المسيحيين (هوميروس، أفلاطون، أرسطو).
  2. *الشهوة*: باولو وفرانشيسكا تعصف بهما رياح أبدية لا تهدأ.
  3. *الشره*: غارقون في طين جليدي كريه تنهشهم كلاب الجحيم.
  4. *الجشع والتبذير*: يدفعون صخوراً عملاقة تتصادم إلى الأبد.
  5. *الغضب*: مغمورون في مستنقع نهر ستيكس الموحل.
  6. *الهرطقة*: محبوسون في قبور حديدية مشتعلة.
  7. *العنف*: القتلة في نهر من الدماء المغلية؛ والمنتحرون تحولوا لأشجار دامية تنهشها الوحوش.
  8. *المخادعون (مالبولجي)*: عشرة خنادق للمنافقين والمرتشين ولصوص المال العام ومثيري الفتن.
  9. *الخيانة (بحيرة الجليد كوكيتوس)*: بحيرة متجمدة محبوس فيها الخونة حتى أعناقهم. وفي مركز الكون يقبع **لوسيفر (إبليس)** الضخم ذو الأجنحة العملاقة مجمداً في الجليد بثلاثة رؤوس، يمضغ في أفواهه الخونة الثلاثة الكبار في التاريخ: **يهوذا الإسخريوطي** (خائن المسيح)، و**بروتوس وكاسيوس** (خائنا يوليوس قيصر). يتسلق دانتي وفرجيل فراء الشيطان ليعبرا للجانب الآخر من الأرض: *"وهكذا خرجنا لنرى النجوم مجدداً"*.

### ثانياً: المطهر (Purgatorio - 7 طبقات)
جبل شاهق في النصف الجنوبي من الأرض؛ يتسلقه التائبون لتطهير نفوسهم من خطايا الكبرياء والحسد والغضب والكسل والشهوة، وهم يرتلون في صبر وأمل لمعرفتهم بحتمية خلاصهم ودخولهم الجنة. وفي قمة الجبل في الفردوس الأرضي، يودع فرجيل دانتي وتظهر بياتريتشه بنور ملائكي لتقوده إلى السماء.

### ثالثاً: الفردوس (Paradiso - 9 أفلاك)
يرتقي دانتي عبر الأفلاك السماوية (القمر، عطارد، الزهرة، الشمس، المريخ، المشتري، زحل، النجوم الثوابت)، ملتقياً بالشهداء والمفكرين والقديسين. وعند وصوله لأعلى عليين، يصلي القديس برنارد للعذراء مريم لتمكين دانتي من الشهود الأعظم. ينظر دانتي في نور الألوهية الأقدس المتمثل في ثلاثة أطياف ضوئية متداخلة، ليذوب قلبه في المحبة الكونية الشاملة، ويختم الملحمة بالبيت الخالد:  
**"المحبة التي تحرك الشمس وسائر النجوم"**.
"""
    },

    # 63 The Magic Mountain
    {
        "id": "63_The_Magic_Mountain",
        "content_en": """# Comprehensive Study Guide: The Magic Mountain (Der Zauberberg)
**Author:** Thomas Mann  
**Year:** 1924  
**Genre:** Philosophical Novel / Modernist Masterpiece / Intellectual Bildungsroman  

---

## 1. Context & The Pre-WWI European Crisis
Published in 1924 after twelve years of composition, Thomas Mann dissects the diseased, decadent psychology of pre-WWI bourgeois Europe. Set in an isolated tuberculosis sanatorium in Davos, Switzerland, the mountain functions as a sealed ideological petri dish.

---

## 2. In-Depth Chapter Breakdown
- **Arrival in Davos**: Hans Castorp, an ordinary, complacent young engineering graduate from Hamburg, travels to the Berghof sanatorium in the Swiss Alps to visit his tubercular cousin Joachim Ziemssen for a planned three-week stay.
- **The Magic Atmosphere & The Illness**: Up on the mountain, time loses its linear urgency, dissolving into a dreamlike haze. Dr. Behrens discovers a moist spot in Castorp’s lung; Castorp tests positive for a low-grade fever and stays—not for three weeks, but for seven years.
- **The Battle for Castorp's Soul**: Castorp becomes the intellectual prize in a monumental dialectical duel between two mentors:
  - **Lodovico Settembrini**: An Italian humanist, rationalist, Freemason, and democrat who champions Enlightenment progress, science, and classical liberty.
  - **Leo Naphta**: A radical Jesuit convert, nihilist, and totalitarian who advocates terror, spiritual absolutism, and medieval mysticism.
- **Clawdia Chauchat & Peeperkorn**: Castorp falls in love with Madame Clawdia Chauchat, an elusive, alluring Russian patient with feline eyes, confessing his passion in French during Carnival. Later, she returns accompanied by Mynheer Peeperkorn, a titanic Dutch coffee planter whose vitalistic personality overshadows all intellectual arguments before his tragic suicide.
- **The "Snow" Chapter**: Skiing alone into a blizzard, Castorp loses his way in the mountains and experiences an existential hallucination of golden sunlight and human harmony, formulating the book's core moral epiphany: *"For the sake of goodness and love, man must let death have no sovereignty over his thoughts."*
- **The Thunderbolt (WWI) & Descent**: The tension between Naphta and Settembrini ends in a duel; Naphta shoots himself in the head. In August 1914, the "Thunderbolt" of World War I erupts, shattering the hermetic isolation of the Magic Mountain. Castorp descends to the muddy flatlands as a soldier. The novel closes with Castorp charging through the artillery mud of Flanders, singing Schubert's *"The Linden Tree"*, fading into the smoke of war.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الجبل السحري (The Magic Mountain)
**المؤلف:** توماس مان (Thomas Mann)  
**سنة النشر:** 1924  
**التصنيف الأدبي:** درة الرواية الفلسفية الألمانية / أدب الأفكار / تشريح الحضارة الأوروبية  

---

## 1. السياق وأزمة الحضارة الأوروبية
عكف توماس مان على كتابة هذه التحفة لـ 12 عاماً؛ ليقدم تشريحاً فكرياً ونفسياً مذهلاً لانحطاط وبرود المجتمع البرجوازي الأوروبي قبيل اندلاع الحرب العالمية الأولى. تدور الأحداث في مصحة دافوس لمرضى السل في جبال الألب السويسرية؛ حيث يتحول الجبل إلى مختبر رمزي لعقل القارة العجوز المريضة.

---

## 2. المسار الدرامي لأحداث الرواية
- **الوصول إلى دافوس**: يسافر الشاب المهندس هانز كاستورب من هامبورغ لزيارة ابن عمه يواخيم في مصحة بيرغهوف لعلاج السل بجبال سويسرا في زيارة كان مقرراً لها أن تدوم 3 أسابيع فقط.
- **سحر الجبل وتلاشي الزمن**: في هواء الجبل البارد، يفقد الزمن خطيته وتذوب الأيام والشهور في رتابة ساحرة. يكتشف الطبيب بقعة في رئة كاستورب وارتفاعاً طفيفاً في حرارته، فيقرر البقاء مريضاً؛ ولا تدوم إقامته 3 أسابيع، بل تمتد لـ **سبع سنوات كاملة**!
- **الصراع الفكري على عقل كاستورب**: يتحول كاستورب الساذج إلى تلميذ يتنازع عقله قطبان فكريان جباران:
  - **سيتembrini (سيتيمبريني)**: إيطالي إنساني عقلاني، يدافع عن التنوير والحرية والديمقراطية والعلم.
  - **نافتا (Naphta)**: يسوعي راديكالي متطرف وماركسي النزعة، يدافع عن الإرهاب والمطلقات الروحية والشمولية القروسطية.
- **عشق كلوديا والعملاق بيبركورن**: يقع كاستورب في حب المريضة الروسية الفاتنة كلوديا شوشا، ويعترف لها بحبه بالفرنسية في ليلة الكرنفال. تعود لاحقاً بصحبة الهولندي الثري بيبركورن ذي الحضور الطاغي الذي ينتحر لاحقاً بالسم.
- **فصل الثلج والومضة الخالدة**: يضل كاستورب طريقه في عاصفة ثلجية وهو يتزلج وحيداً، ويشرف على التجمد، فيرى في نومه رؤيا صوفية لمدينة شمسية فاضلة، ويستخلص الحكمة المركزية للرواية: *"من أجل الخير والمحبة، يجب ألا يدع الإنسان الموت يفرض سيادته على أفكاره"*.
- **صاعقة الحرب والنزول إلى الخنادق**: يشتعل الصدام بين نافتا وسيتيمبريني ويصل لمبارزة بالرصاص، فيطلق نافتا النار على رأسه منتحراً. وفي أغسطس 1914، تنفجر صاعقة الحرب العالمية الأولى لتهدم برج العزلة السحري للجبل. ينزل كاستورب للأرض المنبسطة جندياً في الجيش، وتختتم الرواية بمشهده وهو يركض بين قذائف المدفعية في وحل معارك فلاندرز مغنياً قصيدة شوبيرت، متبدداً في دخان الحرب المجهول.
"""
    },

    # 64 One Thousand and One Nights
    {
        "id": "64_One_Thousand_And_One_Nights",
        "content_en": """# Comprehensive Study Guide: One Thousand and One Nights (Arabian Nights)
**Origin:** Middle Eastern, Persian, Indian & Arab Oral Tradition  
**Compilation:** 8th–14th Centuries (Golden Age of Islam)  
**Genre:** Frame Tale / Folk Epic / Fantasy & Adventure  

---

## 1. Cultural Impact & The Frame Narrative
*One Thousand and One Nights* is one of the most influential narrative tapestries in global literature. The framing narrative establishes storytelling as an existential weapon: **Scheherazade** uses suspense, moral psychology, and imagination to heal a despotic king and save an entire kingdom of women from execution.

---

## 2. In-Depth Structural Breakdown
- **The Frame (King Shahryar and Scheherazade)**: King Shahryar discovers his wife's infidelity with slaves. Traumatized and bitter, he resolves to marry a new virgin each evening and behead her the following morning to guarantee fidelity. When all eligible women have fled or died, **Scheherazade**, the brilliant, well-read daughter of the Grand Vizier, volunteers to marry the tyrant. On their wedding night, she begins an enchanting tale, stopping at dawn at the most gripping cliffhanger. Desperate to hear the ending, Shahryar spares her life for one more day—a cycle that continues for 1,001 nights.
- **The Master Tales**:
  - *The Fisherman and the Jinni*: A poor fisherman draws a brass jar from the sea containing an imprisoned, vengeful Jinni; the fisherman outwits the spirit using cunning reason.
  - *The Three Apples & The Hunchback's Tale*: Early detective mystery and comedy of errors set in Abbasid Baghdad under Caliph Harun al-Rashid.
  - *The Seven Voyages of Sinbad the Sailor*: Sinbad leaves Baghdad for maritime trade, surviving giant Roc birds, cyclopean monsters, diamond valleys, and cannibal tribes through resilience and resourcefulness.
  - *Aladdin and the Wonderful Lamp*: A poor Chinese-Arab street urchin is deceived by an African sorcerer, claims a magical oil lamp containing a genie, and wins Princess Badroulbadour through wisdom and loyalty.
  - *Ali Baba and the Forty Thieves*: A poor woodcutter discovers the magic passphrase *"Open Sesame"* to a cavern of stolen treasure; his clever slave-girl **Morgiana** thwarts forty murderous thieves, killing them in oil jars to save her master's household.
- **Resolution**: After 1,001 nights and three sons born to them, Scheherazade presents her children to Shahryar, asking for her life. Shahryar weeps, declaring that he had already forgiven her long ago, transformed by her wisdom, patience, and morality into a just, loving sovereign.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: ألف ليلة وليلة (One Thousand and One Nights)
**الأصل:** التراث الشعبي العربي والشرقي (العصر العباسي)  
**التصنيف الأدبي:** الحكاية الإطارية / الملحمة الفلكلورية العالمية / أدب الفانتازيا والحكمة  

---

## 1. الأثر العالمي والحكاية الإطارية
تعد *ألف ليلة وليلة* من أعظم الكنوز السردية في التراث الإنساني؛ ترجمت لكل لغات الأرض وألهمت كبار أدباء العالم من بورخيس إلى ماركيز. تجسد الحكاية الإطارية قوة السرد كأداة للنجاة من الموت وعلاج الروح؛ حيث تستخدم **شهرزاد** الحكمة والخيال لترويض الملك المستبد ووقف نزيف دماء بنات جنسها.

---

## 2. المسار الدرامي لأشهر الحكايات

### الحكاية الإطارية (شهريار وشهرزاد)
يصدم الملك شهريار بخيانة زوجته، فيتحول إلى طاغية دموي يقسم على الزواج من عذراء كل ليلة وقطع رأسها في الصباح الباكر لقطع دابر الخيانة. وعندما تفنى نساء المملكة، تتطوع **شهرزاد** الذكية المثقفة، ابنة الوزير، بالزواج منه. وفي ليلة العرس، تبدأ في سرد حكاية ساحرة وتقطعها عند بزوغ الفجر في أكثر لحظاتها تشويقاً؛ فيؤجل الملك إعدامها ليلة تلو أخرى لسماع بقية القصة، لتمتد الرحلة عبر 1001 ليلة.

### أبرز الليالي والقصص الخالدة:
- **حكاية الصياد والعفريت**: صياد فقير يخرج من البحر قمقماً نحاسياً محبوساً فيه مارد شرير يقسم على قتله؛ فيتحايل عليه الصياد بذكائه ويعيده داخل القمقم، متحدثاً عن عاقبة الغدر وعفو الملوك.
- **رحلات السندباد البحري السبع**: يبحر السندباد من بغداد والبصرة بحثاً عن التجارة، ويواجه أهوال الجزر المتحركة، وطائر الرخ العملاق، ووادي الألماس، والعمالقة، متغلباً على الأهوال بالصبر والشجاعة.
- **علاء الدين والمصباح السحري**: فتى فقير يخدعه ساحر مغربي ويحبسه في مغارة الكنوز، فيظفر بالمصباح السحري ومارد الخاتم، وينتصر على مكائد الساحر ليتزوج ابنة السلطان.
- **علي بابا والأربعون حرامياً**: حطاب فقير يكتشف كلمة السر السحرية *"افتح يا سمسم"* لكهف عصابة اللصوص. وتبرز الجارية الذكية **مرجانة** كبطلة حقيقية تكتشف اللصوص وتصب الزيت المغلي في جرارهم لإنقاذ سيدها.
- **النهاية وشفاء الملك**: بعد انقضاء الألف ليلة وليلة، تنجب شهرزاد ثلاثة أطفال وتقدمهم لشهريار ملتمسة العفو عن حياتها. يبكي شهريار ويعلن أنه عفا عنها منذ زمن بعيد، بعد أن طهرت الحكايات قلبه من الحقد والشك، وأعادته ملكاً عادلاً رحيماً.
"""
    }
]

def main():
    for g in GUIDES:
        file_id = g['id']
        en_path = os.path.join(EN_DIR, f"{file_id}.md")
        ar_path = os.path.join(AR_DIR, f"{file_id}_Arabic.md")
        with open(en_path, 'w', encoding='utf-8') as f:
            f.write(g['content_en'].strip() + "\n")
        with open(ar_path, 'w', encoding='utf-8') as f:
            f.write(g['content_ar'].strip() + "\n")
        print(f"  [✓] Successfully upgraded master study guide: {file_id}")

if __name__ == "__main__":
    main()
