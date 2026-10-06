"""
Generates master-level study guides for British & Irish Literature (Part 2):
- 36_Frankenstein
- 37_The_Picture_Of_Dorian_Gray
- 38_Heart_Of_Darkness
- 39_To_The_Lighthouse
- 40_Mrs_Dalloway
- 41_The_Lord_Of_The_Rings
- 65_Middlemarch
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 36 Frankenstein
    {
        "id": "36_Frankenstein",
        "content_en": """# Comprehensive Study Guide: Frankenstein (The Modern Prometheus)
**Author:** Mary Shelley  
**Year:** 1818  
**Genre:** Gothic Horror / Science Fiction / Romantic Tragedy  

---

## 1. Context & The Promethean Myth
Conceived during the "Year Without a Summer" (1816) by 18-year-old Mary Shelley at Lake Geneva, *Frankenstein* is the foundational text of science fiction. Shelley critiques scientific hubris, the neglect of moral responsibility, and Rousseau's concept of the noble savage corrupted by societal cruelty.

---

## 2. In-Depth Chapter Breakdown
- **Walton's Frame Narrative**: Captain Robert Walton, sailing an expedition to the North Pole, rescues Victor Frankenstein from floating Arctic ice. Victor agrees to tell his cautionary tale.
- **Victor's Obsession & Creation**: Born in Geneva, Victor studies natural philosophy and chemistry at Ingolstadt. Obsessed with discovering the secret of life, he animates an eight-foot creature assembled from charnel-house corpses. When the creature opens its dull yellow eye, Victor is seized with horror and flees in disgust, abandoning his newborn creation.
- **The Monster's Education & Rejection**: The nameless creature wanders into the wilderness. He learns language, emotions, and culture by secretly observing the impoverished De Lacey family in their cottage. He reads Milton's *Paradise Lost*, Plutarch's *Lives*, and Goethe's *Sorrows of Young Werther*. But when he reveals himself to the blind patriarch, the sighted family returns and violently beats him. Heartbroken, the creature burns their cottage and declares war on humanity.
- **The Murders & The Ultimatum**: The creature murders Victor's young brother William, framing the innocent servant Justine Moritz, who is executed. Confronting Victor on the Mer de Glace glacier in Chamonix, the creature demands Victor create a female companion: *"I am malicious because I am miserable... If any being felt emotions of benevolence towards me, I would return them a hundredfold."*
- **The Broken Promise & Vengeance**: Victor begins assembling a female mate in the remote Orkney Islands, but destroys it in panic, fearing a race of monsters. The creature vows: *"I will be with you on your wedding night."* On Victor's wedding night, the creature strangles Victor's bride, Elizabeth Lavenza.
- **Arctic Pursuit and Death**: Victor pursues the creature to the Arctic wastes, dying on Walton's ship. The creature appears over Victor's corpse, weeping for his dead creator, and vanishes onto the ice floes to burn himself on a funeral pyre.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: فرانكنشتاين (بروميثيوس المعاصر)
**المؤلف:** ماري شيلي (Mary Shelley)  
**سنة النشر:** 1818  
**التصنيف الأدبي:** الرعب القوطي / الخيال العلمي التأسيسي / التراجيديا الرومانسية  

---

## 1. السياق وأسطورة بروميثيوس المعاصر
أبدعت ماري شيلي هذه الرواية وهي في الثامنة عشرة من عمرها عند بحيرة جنيف؛ لتؤسس أول عمل في تاريخ الخيال العلمي. تقدم الرواية تحذيراً صاعقاً من الغرور العلمي للإنسان عندما يتجرد من المسؤولية الأخلاقية، وتثبت كيف تحول قسوة المجتمع ونبذه الكائنات البريئة إلى وحوش مدمرة.

---

## 2. المسار الدرامي لمحطات الرواية
- **إطار الكابتن والتون**: يبحر الكابتن والتون في بعثة قطبية نحو القطب الشمالي، فينقذ العالم فيكتور فرانكنشتاين من بين الكتل الجليدية، فيروي له فيكتور قصته المأساوية كتحذير.
- **الهوس العلمي وميلاد المسخ**: يدرس فيكتور الكيمياء في جامعة إنغولشتات، ويسيطر عليه هوس كشف سر الحياة. يجمع أجزاء جثث من المقابر ويبعث فيها الحياة بشرارة كهربائية. وعندما يفتح الكائن الضخم عينيه الصفراوين، يصاب فيكتور بذعر واشمئزاز ويهرب تاركاً مخلوقه الوليد لمصيره بلا رعاية.
- **تعليم المسخ وقسوة البشر**: يهيم المخلوق المشوه في الغابات، ويتعلم اللغة والمشاعر الإنسانية بمراقبة عائلة دي لاسي الفقيرة خلسة. يقرأ *الفردوس المفقود* لميلتون؛ وحين يظهر لهم مستجدياً الرحمة والمحبة، تضربه العائلة بوحشية وتطرده. ينفطر قلبه ويحرق كوخهم معلناً الحرب على البشرية.
- **الجرائم والمواجهة فوق الجبل**: يقتل المسخ وليام، الشقيق الأصغر لفيكتور، ويلفق التهمة للخادمة البريئة جوستين فتُعدم ظلماً. يواجه المسخ خالقه فوق قمم الجليد مطالباً بأن يصنع له رفيقة أنثى تشبهه: *"أنا شرير لأنني بائس ومنبوذ... لو منحني أحد ذرة من الحنان لعوضته مئة ضعف"*.
- **نكث العهد والانتقام المروع**: يبدأ فيكتور في صنع الأنثى، ثم يمزقها في ذعر خشية تكاثر المسوخ. يتوعده المسخ بجملته الخالدة: *"سأكون معك في ليلة زفافك!"*. وفي ليلة الزفاف، يخنق المسخ عروس فيكتور "إليزابيث".
- **المطاردة القطبية والنهاية**: يطارد فيكتور المسخ حتى صقيع القطب الشمالي ليموت مريضاً على سفينة والتون. يظهر المسخ باكياً فوق جثة صانعه بنواح حارق، ثم يغادر فوق ألواح الجليد ليحرق نفسه في محرقة أخيرة تنهي عذابه.
"""
    },

    # 37 The Picture of Dorian Gray
    {
        "id": "37_The_Picture_Of_Dorian_Gray",
        "content_en": """# Comprehensive Study Guide: The Picture of Dorian Gray
**Author:** Oscar Wilde  
**Year:** 1890  
**Genre:** Decadent Gothic Fiction / Aestheticism / Philosophical Allegory  

---

## 1. Aestheticism & The Faustean Pact
Oscar Wilde's only novel is a provocative exploration of the Aesthetic Movement ("Art for Art's sake"). Wilde creates a modern Faustian myth interrogating the deadly consequences of hedonism devoid of moral responsibility.

---

## 2. In-Depth Chapter Breakdown
- **The Portrait**: Artist Basil Hallward paints a full-length portrait of the breathtakingly handsome young aristocrat Dorian Gray. In Basil's studio, Dorian meets Lord Henry Wotton, a charismatic, cynical aristocrat who preaches the doctrine of the "New Hedonism"—urging Dorian to pursue every sensual pleasure before his youth fades. Awed by the portrait, Dorian utters his fateful wish: *"If it were I who was to be always young, and the picture that was to grow old! For that—I would give my soul!"*
- **Sibyl Vane's Tragedy**: Dorian falls in love with young actress Sibyl Vane. When Sibyl performs poorly because her real love has superseded stage illusions, Dorian cruelly rejects and humiliates her. Returning home, Dorian notices the painted portrait has changed: a sneer of cruelty touches the mouth. Sibyl commits suicide by drinking prussic acid that night; seduced by Lord Henry's cynical rationalizations, Dorian views her death as a gorgeous theatrical tragedy.
- **The Decadent Descent**: Dorian hides the portrait in his locked old childhood schoolroom. For eighteen years, Dorian indulges in drug dens, secret vices, and scandalous sins, remaining miraculously youthful, while the hidden painting ages grotesquely, reflecting the decaying, pustulant rot of his soul.
- **Basil's Murder**: Basil visits Dorian, pleading with him to repent. Dorian unveils the grotesque, rotting portrait to Basil, then flies into an uncontrollable rage and stabs Basil to death. He blackmails a chemist into dissolving Basil's body in acid.
- **The Climax & Death**: Consumed by guilt and paranoia, Dorian decides to destroy the painting—the only physical evidence of his crimes. He stabs the canvas with the knife that killed Basil. Servants hear a terrible scream; breaking in, they find a splendid portrait of their master in his youthful beauty, and an unrecognizable, withered, loathsome old man lying on the floor with a knife plunged into his heart.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: صورة دوريان غراي (The Picture of Dorian Gray)
**المؤلف:** أوسكار وايلد (Oscar Wilde)  
**سنة النشر:** 1890  
**التصنيف الأدبي:** الأدب القوطي الجمالي / الفلسفة الأخلاقية / التراجيديا الفاوستية  

---

## 1. الحركة الجمالية وميثاق فاوست الجديد
رواية أوسكار وايلد الوحيدة والشهيرة؛ وتعد درة الحركة الجمالية (الفن للفن). يعيد وايلد صياغة أسطورة "فاوست" في العصر الفيكتوري كاشفاً المصير المرعب للانغماس في اللذة الحسية والمظاهر الخارجية مع موت الضمير الأخلاقي.

---

## 2. التسلسل التفصيلي لمجريات المأساة
- **اللوحة والفتنة**: يرسم الفنان النبيل باسل هالوارد لوحة فنية ساحرة للشاب الأرستقراطي فائق الجمال دوريان غراي. يلتقي دوريان في المرسم باللورد هنري ووتون، الأرستقراطي الساخر الذي يلقنه مبادئ "المتعة الجديدة" محذراً إياه من زوال شبابه. ينظر دوريان للوحة ويطلق أمنيته الشيطانية: *"لو كنت أنا من يبقى شاباً إلى الأبد، وتشيخ اللوحة مكاني! سأهب روحي من أجل ذلك!"*.
- **مأساة سيبيل فين**: يقع دوريان في حب الممثلة الشابة سيبيل فين؛ لكن عندما تؤدي دوراً مسرحياً ضعيفاً لانشغال قلبها بحبه الحقيقي، يجرحها دوريان بقسوة مروعة ويتركها باكية. يعود لغرفته ليفاجأ بتغير ملامح اللوحة: ابتسامة قسوة خبيثة ارتسمت على شفتي صورته! تنتحر سيبيل بالسم في تلك الليلة، ويقنعه اللورد هنري بأن يعتبر موتها مشهداً تراجيدياً جميلاً.
- **الانحدار الأخلاقي في الظلام**: يحبس دوريان اللوحة في عليته القديمة المغلقة. وعلى مدار 18 عاماً، ينغمس دوريان في أوكار الأفيون والملذات المشبوهة، محتفظاً بنضارة شبابه الخالد، بينما تتحول اللوحة المخفية إلى مسخ قبيح تتجعد فيه الملامح ويتعفن بفساد روحه وذنوبه.
- **مقتل الفنان باسل هالوارد**: يزور باسل دوريان راجياً إياه أن يتوب ويصلح سيرته. يكشف دوريان لباسل عن اللوحة المشوهة المرعبة، ثم يثور في نوبة غضب جنونية ويطعن باسل بالسكين حتى الموت، ويجبر كيميائياً على إذابة الجثة بالحمض.
- **الطعنة الأخيرة والموت**: يطارده الرعب وعذاب الضمير، فيقرر تمزيق اللوحة للتخلص من الشاهد الوحيد على جرائمه. يطعن اللوحة بنفس السكين التي قتل بها باسل؛ فيسمع الخدم صرخة احتضار مروعة، ليجدوا لوحة سيدهم معلقة بجمالها وشبابها الأخاذ، وعلى الأرض جثة رجل عجوز بشع مشوه وميت بسكين مغروس في قلبه!
"""
    },

    # 38 Heart of Darkness
    {
        "id": "38_Heart_Of_Darkness",
        "content_en": """# Comprehensive Study Guide: Heart of Darkness
**Author:** Joseph Conrad  
**Year:** 1899  
**Genre:** Modernist Psychological Novella / Critique of Imperialism  

---

## 1. Historical Context: The Congo Free State
Conrad drew upon his own 1890 voyage commanding a steamship in King Leopold II’s Congo Free State, where millions perished in forced rubber harvesting. The novella exposes European imperialism not as a civilizing crusade, but as savage, rapacious pillage, while probing the dark depths of human psychology.

---

## 2. In-Depth Chapter Breakdown
- **Frame Narrative on the Thames**: At sunset on the River Thames, sailor Charles Marlow narrates his African voyage to comrades aboard the *Nellie*, observing: *"And this also has been one of the dark places of the earth."*
- **The Outer and Central Stations**: Employed by a Belgian trading company, Marlow journeys to the Congo. At the Outer Station, he sees the "Grove of Death," where starved African chain-gang laborers crawl away to die. At the Central Station, Marlow discovers his steamship has been sunk, suspecting deliberate sabotage by envious company managers. Everyone whispers of **Kurtz**, the Company's most brilliant, successful ivory agent deep upriver.
- **The Journey Upriver**: Marlow repairs the steamer and journeys hundreds of miles up the primeval river into the brooding, suffocating jungle—a journey backwards in time to humanity's prehistoric dawn. The ship is attacked by native arrows in the fog; the African helmsman is killed.
- **Kurtz's Inner Station**: Marlow reaches Kurtz's outpost, surrounded by severed human heads impaled on fence posts facing inward. Kurtz, once an idealistic philosopher, orator, and artist, has succumbed to megalomania, worshipped as a demigod by local tribes and presiding over unspeakable midnight rituals. Marlow reads Kurtz's eloquent treatise on civilizing the natives, culminating in a scrawled postscript: *"Exterminate all the brutes!"*
- **The Death of Kurtz**: Mortally ill, Kurtz is carried aboard the steamer. As his life ebbs away, Kurtz experiences a terrifying flash of supreme moral clarity, whispering his dying words: *"The horror! The horror!"*
- **The Lie to the Intended**: Returning to Brussels ("the sepulchral city"), Marlow visits Kurtz's grieving fiancée. When she tearfully asks for Kurtz's last words, Marlow cannot bear to shatter her illusions with the truth, lying that Kurtz's final word was her name.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: قلب الظلام (Heart of Darkness)
**المؤلف:** جوزيف كونراد (Joseph Conrad)  
**سنة النشر:** 1899  
**التصنيف الأدبي:** الأدب الحداثي النفسي / نقد الاستعمار الأوروبي / الرحلة الرمزية  

---

## 1. السياق التاريخي: جحيم الكونغو البلجيكي
استلهم كونراد روايته من رحلته الحقيقية قبطاناً لباخرة نيلية في الكونغو عام 1890 إبان حكم الملك ليوبولد الثاني؛ حيث أبيد ملايين البشر في جمع المطاط والعاج. تكشف الرواية زيف الادعاءات الأوروبية بـ "تمدين الشعوب"، معرية الوجه الاستعماري الوحشي، وغائصة في أعماق النفس البشرية حين تسقط عنها ضوابط الحضارة.

---

## 2. المسار الدرامي لمحطات الرحلة
- **إطار نهر التيمز**: على متن قارب عند مصب نهر التيمز في لندن، يروي البحار مارلو لرفاقه رحلته الإفريقية متأملاً: *"وهذا المكان أيضاً كان يوماً ما إحدى بقاع الأرض المظلمة"*.
- **المحطة الساحلية والمحطة الوسطى**: يسافر مارلو للكونغو للعمل لدى شركة تجارية بلجيكية. يرى في المحطة الأولى "بستان الموت" حيث يزحف العمال الأفارقة المكبلون بالسلاسل ليموتوا جوعاً وإرهاقاً تحت الأشجار. وفي المحطة الوسطى، يجد باخرته غارقة وسط مؤامرات البيروقراطيين، ويسمع الجميع يهمسون باسم الأسطورة **كورتز**؛ أنجح وكلاء الشركة وأكثرهم جمعاً للعاج في أقصى الأدغال.
- **الرحلة نحو منبع النهر**: يصلح مارلو الباخرة ويبحر عبر النهر الاستوائي في قلب غابة صامتة خانقة تشبه العودة إلى فجر التاريخ البشري البدائي. يتعرض القارب لهجوم بالسهام في الضباب الكثيف ويُقتل ربان السفينة الإفريقي.
- **محطة كورتز الداخلية والوحشية**: يصل مارلو لمحطة كورتز ليصدم برؤوس بشرية مقطوعة مثبتة على أوتاد السور تحيط بالمنزل! كورتز، الذي جاء كفيلسوف ومبشر بالمدنية، استسلم للتوحش والجنون وأعلن نفسه إلهاً معبوداً للقبائل يقود طقوساً دموية ليحصل على أطنان العاج. يقرأ مارلو تقرير كورتز الأدبي البليغ عن رعاية البدائيين، والذي ذيّله بخط يده بهامش مروع: *"أبيدوا كل هؤلاء الوحوش!"*.
- **موت كورتز**: يُحمل كورتز المريض المشرف على الموت إلى الباخرة. وفي لحظات احتضاره، تنقشع الغشاوة عن بصيرته ليرى قبح ما اقترفه، ويهمس بكلماته الأخيرة الخالدة: *"الرعب! الرعب!"*.
- **الكذبة لخطيبة كورتز**: يعود مارلو إلى بروكسل ("المدينة التي تشبه قبراً مبيضاً") ويزور خطيبة كورتز المخلصة. وعندما تسأله باكية عن آخر كلمة نطق بها كورتز قبل موته، يعجز مارلو عن تحطيم قلبها بالحقيقة، ويكذب قائلاً إن آخر كلمة نطق بها كانت اسمها!
"""
    },

    # 39 To The Lighthouse
    {
        "id": "39_To_The_Lighthouse",
        "content_en": """# Comprehensive Study Guide: To the Lighthouse
**Author:** Virginia Woolf  
**Year:** 1927  
**Genre:** Modernist Masterpiece / Stream of Consciousness / Elegy  

---

## 1. Context & Modernist Time
Virginia Woolf captures the fluid passage of time and the subjective nature of human perception. Set on the Isle of Skye in the Hebrides, the novel functions as an elegy for Woolf's parents and a philosophical exploration of art, grief, and domesticity.

---

## 2. Structural Breakdown (The Three Parts)

### 1. The Window
Takes place over a single summer day before WWI. Mrs. Ramsay, a nurturing, radiant matriarch, creates social harmony and emotional warmth among her family and bohemian guests. Her six-year-old son James longs to sail to the distant lighthouse, but Mr. Ramsay, an emotionally needy, rationalist philosopher, bluntly declares the weather will not permit it. Artist Lily Briscoe struggles to paint Mrs. Ramsay, fearing she cannot capture her essence.

### 2. Time Passes
A breathtaking, experimental interlude compressing ten years into a few haunting pages. The summer house is abandoned to decay, wind, and shadows. WWI erupts. In brief, bracketed sentences, Woolf reveals devastating tragedies: Mrs. Ramsay dies suddenly in the night; daughter Prue dies in childbirth; son Andrew is killed by an exploding shell in France.

### 3. The Lighthouse
Ten years later, the surviving Ramsays and Lily return to the decayed house. Mr. Ramsay, now an old man, finally sails with the grown James and Cam to the Lighthouse. After years of resentment, James earns his father's praise. Simultaneously on the lawn, Lily Briscoe experiences a transcendent moment of creative clarity, painting a single line down the center of her canvas and declaring: *"I have had my vision."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: إلى الفنار (To the Lighthouse)
**المؤلف:** فرجينيا وولف (Virginia Woolf)  
**سنة النشر:** 1927  
**التصنيف الأدبي:** تيار الوعي الحداثي / الرواية الشعرية الفلسفية / مرثية الزمن  

---

## 1. السياق وفلسفة الزمن الحداثي
تعد هذه الرواية قمة إبداع فرجينيا وولف في رصد سيولة الزمن، وعلاقة الفن بالحياة. تدور الأحداث في جزيرة سكاي الاسكتلندية؛ حيث تحول وولف ذكريات طفولتها وعائلتها إلى مرثية تأملية تسبر أغوار الفقدان والخلود الفني.

---

## 2. الهيكل التفصيلي للأقسام الثلاثة

### القسم الأول: النافذة (The Window)
تدور أحداثه في يوم صيفي واحد قبل الحرب العالمية الأولى؛ تقود السيدة رامزي، الأم الحنون المشرقة، الحياة الأسرية بحنان تصنع به التوافق بين أبنائها والضيوف. يرجو طفلها جيمس الذهاب في رحلة بالزورق إلى الفنار البحري، لكن الأب الفيلسوف الصارم مستر رامزي يحطم أمله بجفاء مؤكداً أن الطقس لن يسمح بذلك. وتحاول الرسامة الشابة ليلي بريسكو رسم لوحة للسيدة رامزي باحثة عن التعبير عن جوهرها.

### القسم الثاني: مرور الزمن (Time Passes)
فصل تجريبي عبقري يختزل عشر سنوات في صفحات معدودة؛ يُهجر المنزل للرياح والغبار والظلام. تندلع الحرب العالمية الأولى، وتسجل وولف الفواجع الإنسانية بين أقواس مقتضبة: تموت السيدة رامزي فجأة في الليل، وتموت الابنة برو أثناء الولادة، ويُقتل الابن أندرو بقذيفة في الحرب.

### القسم الثالث: الفنار (The Lighthouse)
بعد مرور عشر سنوات، يعود من بقي حياً من العائلة للمنزل القديم. يقود الأب العجوز ابنيه جيمس وكام في رحلة الزورق التي طال انتظارها نحو الفنار. يتصالح جيمس مع والده، وبالتوازي في تلك اللحظة على حديقة المنزل، تلمع ومضة الإلهام في عقل الرسامة ليلي بريسكو، وترسم خطاً فاصلاً في مركز اللوحة معلنة في سلام روحي: *"لقد تحققت رؤيتي الفنية"*.
"""
    },

    # 40 Mrs Dalloway
    {
        "id": "40_Mrs_Dalloway",
        "content_en": """# Comprehensive Study Guide: Mrs Dalloway
**Author:** Virginia Woolf  
**Year:** 1925  
**Genre:** Modernist Stream of Consciousness / Post-WWI Trauma  

---

## 1. Setting & The Tunneling Process
Set across a single Wednesday in mid-June 1923 in London, Woolf employs her revolutionary "tunneling process," excavating characters' deep memories and interior psychological realities in rhythm with the hourly chimes of Big Ben (*"leaden circles dissolved in the air"*).

---

## 2. The Twin Destinies
- **Clarissa Dalloway**: A 51-year-old upper-class society hostess preparing to host an evening party: *"Mrs. Dalloway said she would buy the flowers herself."* Walking through London, she reflects on her youth at Bourton, her rejection of passionate Peter Walsh, and her choice of stable politician Richard Dalloway.
- **Septimus Warren Smith**: A shell-shocked WWI veteran suffering from severe PTSD and hallucinations of his dead officer Evans. Accompanied by his distressed Italian wife Lucrezia, Septimus is tormented by pompous physicians (Dr. Holmes and Sir William Bradshaw) who fail to comprehend his mental trauma, demanding rest cure and institutionalization. Rather than surrender his soul to Bradshaw's coercion, Septimus leaps from a window onto rusty area railings, impaling himself to death.
- **The Party & Epiphany**: At Clarissa's glittering party, Sir William Bradshaw arrives late, mentioning the suicide of a young veteran. Clarissa slips into a dark room alone, deeply affected. She understands that Septimus’s suicide was an act of defiance to preserve his soul’s integrity. Purified by his sacrifice, Clarissa returns to her guests, where Peter Walsh gazes upon her in awe: *"What is this terror? what is this ecstasy?... It is Clarissa."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: السيدة دالواي (Mrs Dalloway)
**المؤلف:** فرجينيا وولف (Virginia Woolf)  
**سنة النشر:** 1925  
**التصنيف الأدبي:** تيار الوعي الحداثي / صدمة ما بعد الحرب / فلسفة اللحظة  

---

## 1. مسرح الأحداث ودقات بيغ بن
تدور أحداث الرواية في يوم أربعاء واحد من منتصف يونيو 1923 في لندن. تستخدم وولف أسلوب "الحفر النفسي"، غائصة في ذكريات الشخصيات وأعماق وعيها الداخلي على إيقاع دقات ساعة بيغ بن التي تذوب دوائرها الرصاصية في الهواء.

---

## 2. المساران المتوازيان والمصير المشترك
- **كلاريسا دالواي**: سيدة مجتمع مخملية في الحادية والخمسين من عمرها، تستعد لإقامة حفل ساهر في المساء: *"قالت السيدة دالواي إنها ستشتري الزهور بنفسها"*. تتجول في شوارع لندن وتستعيد ذكريات شبابها، ورفضها لحبيبها القديم بيتر والش، وزواجها الهادئ من السياسي ريتشارد دالواي.
- **سبتيموس وارن سميث**: جندي عائد من الحرب العالمية الأولى يعاني من صدمة حرب حادة (PTSD) وهلوسات برؤية رفيقه الميت إيفانز. يقع ضحية لأطباء نفسيين متغطرسين يهددونه بالإيداع في مصحة عقلية قسراً. ولحماية نقاء روحه من بطش الأطباء، يقفز سبتيموس من النافذة ليموت مصلوباً على الأسياخ الحديدية في الشارع.
- **الحفل والومضة الوجودية**: في ذروة حفل كلاريسا الأنيق، يحضر الطبيب متأخراً ويتحدث عن انتحار الجندي الشاب. تنعزل كلاريسا في غرفة مظلمة، وتتأمل المشهد بعمق؛ فتدرك أن انتحار سبتيموس لم يكن هزيمة، بل كان عملاً شجاعاً للحفاظ على كرامة روحه. تتطهر نفس كلاريسا، وتعود لحفلها تشع ألقاً، ليتأملها بيتر والش في انبهار: *"ما هذا الرعب؟ ما هذه النشوة؟... إنها كلاريسا"*.
"""
    },

    # 41 The Lord of the Rings
    {
        "id": "41_The_Lord_Of_The_Rings",
        "content_en": """# Comprehensive Study Guide: The Lord of the Rings
**Author:** J.R.R. Tolkien  
**Publication:** 1954–1955  
**Genre:** Epic High Fantasy / Mythopoeia  

---

## 1. Mythopoeic Scope & The Corrupting Nature of Power
J.R.R. Tolkien, an Oxford philologist, created an entire secondary world (Middle-earth) with constructed languages, mythologies, and histories. The One Ring of Sauron serves as the ultimate metaphor for absolute power: it cannot be used for good, for any attempt to wield it corrupts the user into tyranny.

---

## 2. The Three Volumes Breakdown

### The Fellowship of the Ring
- **The Shire & The Shadow**: Frodo Baggins inherits the One Ring from Bilbo. Wizard Gandalf the Grey reveals its dark nature. Pursued by the terrifying Ringwraiths (Nazgûl), Frodo and hobbit companions (Sam, Merry, Pippin) flee to Rivendell.
- **The Council of Elrond**: Representatives of the Free Peoples form the Nine Walkers (The Fellowship) to destroy the Ring in Mount Doom.
- **Moria and Amon Hen**: In the Mines of Moria, Gandalf falls battling the Balrog (*"Fly, you fools!"*). At Amon Hen, Boromir succumbs to the Ring's temptation, then redeems himself dying to save Merry and Pippin. The Fellowship breaks: Frodo and faithful Sam journey alone toward Mordor.

### The Two Towers
- **Rohan and Helm's Deep**: Aragorn, Legolas, and Gimli track the captured hobbits, reuniting with Gandalf the White. They defend Rohan at the siege of Helm's Deep, while the Ents destroy Saruman's fortress at Isengard.
- **The Journey with Gollum**: Frodo and Sam capture the corrupted creature Gollum (Sméagol), who agrees to guide them into Mordor. Gollum's split personality wars within him, culminating in his betrayal at Shelob's lair.

### The Return of the King
- **The Siege of Gondor**: Sauron unleashes his armies upon Minas Tirith. The Battle of the Pelennor Fields sees the Witch-king slain and Aragorn claiming the royal throne of Gondor.
- **Mount Doom**: Emaciated and crawling across the ash plains of Mordor, Frodo reaches the Crack of Doom. At the final brink, Frodo’s will breaks: *"I will not do this thing. The Ring is mine."* He puts on the Ring. Gollum attacks him, bites off Frodo's finger with the Ring, and dancing in ecstasy, slips over the edge into the volcanic fires. The Ring is destroyed.
- **The Scouring of the Shire & The Grey Havens**: The hobbits return to liberate the Shire from Saruman. Bearing the deep wounds of his burden, Frodo bids farewell to Sam, boarding an Elven ship into the Undying Lands.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: سيد الخواتم (The Lord of the Rings)
**المؤلف:** ج. ر. ر. تولكين (J.R.R. Tolkien)  
**سنوات النشر:** 1954–1955  
**التصنيف الأدبي:** الفانتازيا الملحمية العليا / أسطورة الصراع بين الخير والشر  

---

## 1. البناء الأسطوري وفلسفة الخاتم
أبدع أستاذ اللغويات في أكسفورد ج. ر. ر. تولكين عالماً أسطورياً متكاملاً (الأرض الوسطى) بلغاته وتاريخه وجغرافيته. يجسد "خاتم القوة الواحد" الاستعارة الكبرى لشهوة السلطة المطلقة؛ فالخاتم لا يمكن استخدامه في الخير، لأن مجرد حمله يفسد أنبل النفوس ويقودها إلى الاستبداد.

---

## 2. المسار الملحمي عبر المجلدات الثلاثة

### رفقة الخاتم (The Fellowship of the Ring)
- **ميراث المقاطعة وظلال الخطر**: يرث الهوبيت فرودو باجنز الخاتم من عمه بيلبو. يكشف له الساحر غاندالف حقيقة الخاتم الشرير وأنه يعود لسيد الظلام ساورون. يهرب فرودو بصحبة رفاقه الهوبيت (سام، بيبين، ميري) مطاردين بفرسان الظلام المروعين (النازغول) حتى يصلوا إلى ريفنديل.
- **مجلس إلروند والرفقة**: يجتمع ممثلو شعوب الأرض الوسطى وتتشكل "رفقة الخاتم" من تسعة أبطال لتدمير الخاتم في نيران جبل الهلاك في موردور.
- **مناجم موريا وانكسار الرفقة**: يسقط غاندالف في الهاوية أثناء قتاله لوحش البالروغ. يستسلم بورومير لإغواء الخاتم، ثم يستشهد دفاعاً عن الهوبيت ميري وبيبن. تنكسر الرفقة، ويمضي فرودو ورفيقه المخلص سام بمفردهما نحو موردور.

### البرجان (The Two Towers)
- **مملكة روهان وحصن هيلمز ديب**: يطارد أراغورن وليغولاس وغيملي الأورك لإنقاذ الهوبيت، ويلتقون بغاندالف الأبيض العائد من الموت. ينتصرون في حصار هيلمز ديب، بينما تدمر كائنات الإنتس شجرية الشكل قلعة الساحر الخائن سارومان.
- **رحلة فرودو مع غولوم**: يقبض فرودو وسام على المخلوق المشوه غولوم (سميغول) الذي يقودهما في مسالك موردور الوعرة. تتصارع شخصيتا غولوم بين الوفاء والطمع، حتى يغدر بهما ويقودهما لكهف العنكبوت العملاق شيلوب.

### عودة الملك (The Return of the King)
- **معركة غوندور الكبرى**: يحاصر جيش ساورون مدينة ميناس تيريث، وتدور معركة حقول بيلينور الملحمية التي يُقتل فيها ملك السحرة، ويستعيد أراغورن عرش أجداده ملكاً على غوندور.
- **جبل الهلاك والتطهير الأخير**: يصل فرودو المنهك الموشك على الهلاك إلى فوهة البركان. وفي اللحظة الأخيرة تنهار إرادته ويستسلم للخاتم قائلاً: *"الخاتم لي!"* ويضعه في إصبعه. يهاجمه غولوم ويعض إصبعه ليخطف الخاتم، وفي غمرة نشوته يترنح ويسقط في الحمم البركانية ليحترق الخاتم ويسقط ملك ساورون إلى الأبد.
- **تطهير المقاطعة والموانئ الرمادية**: يعود الهوبيت لتحرير المقاطعة من بقايا سارومان. ونظراً لعمق جراحه الروحية التي لا تندمل، يودع فرودو رفيقه سام ويبحر مع الجان في سفينة نحو الأراضي الخالدة.
"""
    },

    # 65 Middlemarch
    {
        "id": "65_Middlemarch",
        "content_en": """# Comprehensive Study Guide: Middlemarch (A Study of Provincial Life)
**Author:** George Eliot (Mary Ann Evans)  
**Year:** 1871–1872  
**Genre:** Victorian Masterpiece / Social Realism / Psychological Complexity  

---

## 1. Context & The "Web" of Society
Virginia Woolf famously called *Middlemarch* *"one of the few English novels written for grown-up people."* George Eliot weaves a dense social web in a fictional Midlands town on the cusp of the 1832 Reform Act, dissecting human idealism against social compromise.

---

## 2. The Twin Disillusionments
- **Dorothea Brooke & Casaubon**: Dorothea, an earnest, passionate young heiress with noble ideals, marries Edward Casaubon, a scholarly clergyman decades her senior, believing she will assist his great work (*The Key to All Mythologies*). The marriage becomes an intellectual and emotional tomb: Casaubon is sterile, pedantic, and insecure. Following Casaubon's death, Dorothea discovers a humiliating codicil in his will: she will lose her entire inheritance if she ever marries Casaubon's idealistic young cousin, Will Ladislaw.
- **Tertius Lydgate & Rosamond Vincy**: Dr. Lydgate, an ambitious medical reformer determined to pioneer modern clinical research and hygiene, makes an impulsive marriage to Rosamond Vincy, a shallow, narcissistic, materialistic provincial beauty. Rosamond’s relentless spending drives Lydgate into financial ruin and moral compromise, forcing him into wealthy social practice rather than groundbreaking scientific reform.
- **Resolution**: Dorothea renounces Casaubon’s wealth to marry Will Ladislaw for true love and shared reformist purpose. The novel closes with Eliot's immortal tribute to quiet, uncelebrated goodness: *"The growing good of the world is partly dependent on unhistoric acts; and that things are not so ill with you and me as they might have been, is half owing to the number who lived faithfully a hidden life, and rest in unvisited tombs."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: ميدلمارش (Middlemarch)
**المؤلف:** جورج إليوت (ماري آن إيفانز)  
**سنة النشر:** 1871–1872  
**التصنيف الأدبي:** قمة الواقعية الفيكتورية / الرواية النفسية والاجتماعية  

---

## 1. السياق وشبكة المجتمع الفيكتوري
وصفت فرجينيا وولف رواية *ميدلمارش* بأنها *"واحدة من الروايات الإنجليزية القليلة جداً التي كُتبت للبالغين حقاً"*. تنسج الكاتبة شبكة اجتماعية مذهلة لبلدة ميدلمارش الريفية قبيل قانون الإصلاح السياسي لعام 1832، مفككة الصدام بين الأحلام الإنسانية النبيلة والواقع الاجتماعي المحافظ.

---

## 2. المساران الدراميان وخيبة الأمل
- **دوروثيا بروك وكازوبون**: دوروثيا شابة نبيلة مثالية، ترفض الزواج التقليدي وتتزوج من القس الباحث إدوارد كازوبون الذي يكبرها بعقود، ظناً منها أنها ستساعده في تأليف موسوعته الفكرية الخالدة. يتحول الزواج لمقبرة نفسية؛ فالزوج عقيم الفكر بارد المشاعر يسيطر عليه الشك. بعد موته، يترك كازوبون وصية مهينة تحرم دوروثيا من الميراث بالكامل إذا تزوجت من قريبه الشاب المصلح ويل لاديسلو.
- **الدكتور ليدغيت وروزاموند**: طبيب شاب عبقري ومصلح صحي طموح يحلم بتطوير الطب في الأقاليم، يقع في حب الفتاة الحسناء المدللة روزاموند فينسي. تدمره زوجته بإنفاقها المادي الاستعراضي حتى يغرق في الديون ويضطر للتنازل عن طموحه العلمي ليعالج أثرياء العاصمة.
- **التطهر والخاتمة الخالدة**: تتنازل دوروثيا عن الثروة طواعية وتتزوج ويل لاديسلو عن حب حقيقي وتشاركه النضال الاجتماعي. وتختم الرواية بواحدة من أروع الجمل في تاريخ الأدب الإنساني: *"إن الخير المتنامي في هذا العالم يعتمد جزئياً على أفعال أناس مجهولين؛ وإن الأمور ليست بالسوء الذي يمكن أن تكون عليه معي ومعك، بفضل أولئك الذين عاشوا حياة مستقيمة صامتة، ويرقدون الآن في قبور لا يزورها أحد"*.
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
