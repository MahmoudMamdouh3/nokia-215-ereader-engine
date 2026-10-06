"""
Full Library Executive Summaries Generator (66 Books - Bilingual English & Arabic)
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

SUMMARIES_BASE = r"E:\nokia\summaries"
EN_DIR = os.path.join(SUMMARIES_BASE, "english")
AR_DIR = os.path.join(SUMMARIES_BASE, "arabic")

os.makedirs(EN_DIR, exist_ok=True)
os.makedirs(AR_DIR, exist_ok=True)

DATA = [
    # 1. Technical
    {
        "id": "01_The_Pragmatic_Programmer",
        "title_en": "The Pragmatic Programmer (20th Anniversary Edition)",
        "author": "David Thomas & Andrew Hunt",
        "title_ar": "المبرمج البراغماتي (النسخة العشرينية)",
        "thesis_en": "Pragmatic programming is about continuous professional learning, taking responsibility for your code, designing modular software, and focusing on user value rather than dogmatic methodologies.",
        "thesis_ar": "البرمجة البراغماتية تدور حول التعلم المهني المستمر، وتحمل المسؤولية عن جودة الشيفرة، وتصميم أنظمة برمجية مرنة ومستقلة، والتركيز على تقديم قيمة حقيقية للمستخدم.",
        "points_en": "- Care about your craft and think constantly about your decisions.\n- Fix broken windows immediately to prevent technical debt.\n- Apply DRY (Don't Repeat Yourself) across all system specifications.\n- Design orthogonal, decoupled modules to avoid ripple effects.\n- Practice assertive programming: fail fast and loud when invariants fail.",
        "points_ar": "- اهتم بصنعتك وفكر باستمرار في أبعاد كل قرار تقني تتخذه.\n- أصلح النوافذ المكسورة فوراً لمنع تراكم الديون التقنية وتدهور الشيفرة.\n- طبق مبدأ DRY (لا تكرر نفسك) لمنع الازدواجية وتناقض البيانات.\n- صمم وحدات برمجية متعامدة ومستقلة لتفادي الآثار الجانبية للأعطال.\n- تبنّ البرمجة الجازمة: اجعل النظام يفشل بوضوح وسرعة عند حدوث خلل.",
        "takeaways_en": "Invest constantly in your knowledge portfolio. Software is not rigid engineering; it is gardening that requires daily pruning and cultivation.",
        "takeaways_ar": "استثمر باستمرار في محفظتك المعرفية. كتابة البرمجيات ليست بناءً أسمنتياً صلباً بل رعاية حديقة تتطلب تقليماً وعناية يومية."
    },
    {
        "id": "02_Programming_Principles_And_Practice_Using_CPP",
        "title_en": "Programming: Principles and Practice Using C++ (3rd Edition, C++20/C++23)",
        "author": "Bjarne Stroustrup",
        "title_ar": "مبادئ وممارسة البرمجة باستخدام لغة C++ (الطبعة الثالثة الحديثة)",
        "thesis_en": "A comprehensive foundational guide to modern software engineering, computation, and modern C++ (C++20/C++23) by the creator of C++. Teaches clean code, type safety, object-oriented, and generic programming.",
        "thesis_ar": "المرجع التأسيسي الشامل للهندسة البرمجية الحديثة ولغة C++20/C++23 بقلم مبتكر اللغة بيارن ستروستروب؛ يركز على سلامة الأنواع والبرمجة الكائنية والمعممة.",
        "points_en": "- Type safety and memory safety through RAII (Resource Acquisition Is Initialization).\n- Abstract data types and clean interface separation.\n- Standard Library containers, algorithms, and concepts in C++20.\n- Correct error handling via exceptions and invariant preservation.",
        "points_ar": "- أمان الذاكرة والأنواع عبر مبدأ RAII لإدارة الموارد تلقائياً.\n- تصميم واجهات برمجية نظيفة وتجريد البيانات بطريقة معمارية متينة.\n- استغلال خوارزميات ومكتبات المعايير القياسية Concepts و Containers في C++20.\n- المعالجة الرصينة للأخطاء والحفاظ على سلامة الحالات الثابتة في البرامج.",
        "takeaways_en": "Write programs that clearly express intent, avoid premature optimization, and rely on the modern type system for correctness.",
        "takeaways_ar": "اكتب برامج تعبر بوضوح عن غايتها، وتجنب التحسين المبكر، واعتمد على قوة نظام الأنواع لضمان صحة البرنامج."
    },
    # 2. Personal Development & Finance
    {
        "id": "03_Atomic_Habits",
        "title_en": "Atomic Habits",
        "author": "James Clear",
        "title_ar": "العادات الذرية",
        "thesis_en": "Small 1% daily improvements compound into massive long-term transformations. Focus on systems and identity rather than arbitrary goals.",
        "thesis_ar": "التغييرات المتراكمة بنسبة 1% يومياً تصنع تحولات جذرية على المدى الطويل؛ ركز على بناء الأنظمة والهوية بدلاً من التشبث بالأهداف المجردة.",
        "points_en": "- 1st Law (Cue): Make it obvious.\n- 2nd Law (Craving): Make it attractive.\n- 3rd Law (Response): Make it easy (2-minute rule).\n- 4th Law (Reward): Make it satisfying.",
        "points_ar": "- القانون الأول: اجعل العادة واضحة وملموسة في بيئتك.\n- القانون الثاني: اجعلها جذابة ومحفزة للرغبة.\n- القانون الثالث: اجعلها سهلة التطبيق (قاعدة الدقيقتين).\n- القانون الرابع: اجعلها مجزية ومكافئة فورياً.",
        "takeaways_en": "You do not rise to the level of your goals; you fall to the level of your systems.",
        "takeaways_ar": "أنت لا ترتقي إلى مستوى أهدافك، بل تهبط إلى مستوى أنظمتك اليومية."
    },
    {
        "id": "04_The_Psychology_Of_Money",
        "title_en": "The Psychology of Money",
        "author": "Morgan Housel",
        "title_ar": "سيكولوجية المال",
        "thesis_en": "Financial success is driven primarily by behavioral discipline, humility, and patience, rather than mathematical genius or financial acumen.",
        "thesis_ar": "النجاح المالي تحركه الانضباط السلوكي والتواضع والصبر، وليس العبقرية الحسابية أو المعرفة النظرية المجردة.",
        "points_en": "- The power of compounding: endurance across decades drives exponential returns.\n- Getting wealthy requires risk-taking; staying wealthy requires frugality and humility.\n- Freedom to control your time is the highest dividend wealth provides.\n- Room for error and margin of safety protect against ruin.",
        "points_ar": "- قوة الفائدة المركبة: الاستمرار عبر العقود هو ما يصنع الثروات الضخمة.\n- بناء الثروة يتطلب الجرأة والمخاطرة؛ بينما الحفاظ عليها يتطلب التواضع والحذر.\n- حرية التصرف في وقتك هي أعلى عائد تمنحه لك الثروة.\n- هامش الأمان والادخار النقدي يحميانك من الصدمات والانهيارات غير المتوقعة.",
        "takeaways_en": "Wealth is what you do not spend. True wealth is flexibility, autonomy, and security.",
        "takeaways_ar": "الثروة هي ما لا تنفقه؛ الثروة الحقيقية هي راحة البال، والاستقلالية، والأمان المالي."
    },
    {
        "id": "05_How_To_Win_Friends_And_Influence_People",
        "title_en": "How to Win Friends and Influence People",
        "author": "Dale Carnegie",
        "title_ar": "كيف تكسب الأصدقاء وتؤثر في الناس",
        "thesis_en": "True influence is gained through sincere empathy, active listening, respecting human dignity, and making others feel genuinely valued.",
        "thesis_ar": "التأثير الحقيقي يُبنى على التعاطف الصادق، والاستماع الفعال، واحترام كرامة الإنسان، وجعل الآخرين يشعرون بقيمتهم الحقيقية.",
        "points_en": "- Fundamental Techniques: Never criticize, condemn, or complain. Give honest, sincere appreciation.\n- Make People Like You: Become genuinely interested in others. Smile. Remember names.\n- Win People to Your Way of Thinking: Avoid arguments. Respect others' opinions. Let others do the talking.\n- Be a Leader: Praise slightest improvements. Save people's face.",
        "points_ar": "- القواعد الأساسية: لا تنتقد ولا تدن ولا تشتكِ؛ وامنح تقديراً مخلصاً وصادقاً.\n- اجعل الناس يحبونك: اهتم بهم بصدق، ابتسم، وتذكر أسماءهم دائماً.\n- كيف تقنع الآخرين برأيك: تجنب الجدل، احترم آراءهم، ودعهم يتحدثون باستفاضة.\n- القيادة الحكيمة: امدح أصغر تحسن، واحرص على حفظ ماء وجه الآخرين.",
        "takeaways_en": "You can make more friends in two months by becoming interested in other people than you can in two years by trying to get other people interested in you.",
        "takeaways_ar": "يمكنك أن تكسب أصدقاء في شهرين باهتمامك بهم أكثر مما تكسبه في عامين بمحاولة جذب اهتمامهم إليك."
    },
    # 3. Robert Greene Collection
    {
        "id": "06_The_48_Laws_Of_Power",
        "title_en": "The 48 Laws of Power",
        "author": "Robert Greene",
        "title_ar": "قواعد السطوة الـ48",
        "thesis_en": "A ruthless, analytical examination of the timeless dynamics of power, strategy, deception, and psychological influence throughout human history.",
        "thesis_ar": "تحليل تاريخي واستراتيجي عميق لقواعد القوة والسطوة والنفوذ النفسي وإدارة الصراعات عبر التاريخ البشري.",
        "points_en": "- Never outshine the master.\n- Conceal your intentions.\n- Win through actions, never arguments.\n- Guard your reputation with your life.\n- Assume formlessness and adapt to any changing arena.",
        "points_ar": "- لا تشرق أبداً أكثر من سيدك.\n- اكتم نواياك واجعل تحركاتك غير متوقعة.\n- انتصر بأفعالك لا بالمجادلات الكلامية.\n- احمِ سمعتك بكل ما أوتيت فهي حصنك الأول.\n- كن بلا شكل محدد وتكيف مع أي ظرف طارئ.",
        "takeaways_en": "Emotional self-control is the supreme weapon of power; anger, impatience, and vanity lead directly to strategic destruction.",
        "takeaways_ar": "التحكم في العواطف هو سلاح السطوة الأول؛ فالغضب ونفاد الصبر والغرور تقود مباشرة إلى الهزيمة."
    },
    {
        "id": "07_The_33_Strategies_Of_War",
        "title_en": "The 33 Strategies of War",
        "author": "Robert Greene",
        "title_ar": "33 استراتيجية للحرب",
        "thesis_en": "Life is subtle psychological warfare. Military strategy applied to professional and social battlefields grants resilience, clarity, and victory.",
        "thesis_ar": "الحياة صراع استراتيجي دائم؛ وتطبيق الحكمة العسكرية على الميادين المهنية والاجتماعية يمنحك البصيرة والمرونة لتحقيق النصر.",
        "points_en": "- Declare war on your weaknesses: avoid complacency.\n- Create a sense of urgency (Death Ground Strategy).\n- Know your enemy: psychological profiling.\n- Trade space for time: counter-attack when opponents exhaust themselves.",
        "points_ar": "- أعلن الحرب على نقاط ضعفك وتخلص من التراخي والرضا الزائف.\n- اصنع حالة من الإلحاح (استراتيجية ساحة الموت: لا تراجع خلفك).\n- اعرف خصمك ونفسيته بدقة متناهية.\n- انسحب بذكاء لكسب الوقت، ثم اضرب عندما يستنزف الخصم طاقته.",
        "takeaways_en": "Strategy is a mental framework of detachment and adaptability, not a rigid set of rules.",
        "takeaways_ar": "الاستراتيجية عقلية تقوم على الهدوء والمرونة والتحليل الموضوعي، وليست مجرد قواعد جامدة."
    },
    {
        "id": "08_Mastery",
        "title_en": "Mastery",
        "author": "Robert Greene",
        "title_ar": "الإتقان",
        "thesis_en": "Mastery is not born of innate genius, but of a rigorous apprenticeship, intense focus, creative experimentation, and thousands of hours of deliberate practice.",
        "thesis_ar": "الإتقان ليس هبة فطرية أو حكراً على العباقرة، بل هو ثمرة التلمذة الصارمة، والتركيز العميق، وآلاف الساعات من الممارسة الهادفة.",
        "points_en": "- Discover your Life's Task: align with your deepest interests.\n- The Apprenticeship Phase: endure tedious foundational training without ego.\n- Absorb the master's power: mentorship.\n- The Creative-Active Phase: synthesize rules to break new ground.",
        "points_ar": "- اكتشف نداء حياتك ورسالتك الشخصية التي تشعل شغفك.\n- مرحلة التلمذة: تحمّل التدريب الشاق والتعلم الأساسي دون تكبر أو استعجال.\n- استوعب حكمة الأستاذ عبر الإرشاد والمصاحبة.\n- مرحلة الإبداع الفعال: ادمج القواعد التي تعلمتها لتبتكر أسلوبك الفريد.",
        "takeaways_en": "Time and intense focus transform ordinary diligence into intuitive mastery.",
        "takeaways_ar": "الوقت والتركيز المكثف يحولان الجهد اليومي إلى إتقان حدسي خارق."
    },
    {
        "id": "09_The_Laws_Of_Human_Nature",
        "title_en": "The Laws of Human Nature",
        "author": "Robert Greene",
        "title_ar": "قوانين الطبيعة البشرية",
        "thesis_en": "To navigate society successfully, you must pierce the masks people wear, understand their underlying psychological drives (envy, narcissism, grandiosity), and master your own shadow.",
        "thesis_ar": "للنجاح في المجتمع، يجب أن تخترق الأقنعة التي يرتديها الناس، وتفهم دوافعهم النفسية الخفية (الحسد، النرجسية، الغرور)، وتروض ضعفك الداخلي.",
        "points_en": "- Master your emotional self: irrationality is our default state.\n- Transform self-love into empathy.\n- See through people's masks: nonverbal leakage.\n- Confront your dark side and repress destructive shadow impulses.",
        "points_ar": "- تحكم في ذاتك العاطفية: فاللاعقلانية هي حالتنا الطبيعية إن لم نروضها.\n- حوّل حب الذات إلى تعاطف عميق وفهم للآخرين.\n- انظر خلف الأقنعة ولاحظ لغة الجسد والإشارات غير اللفظية.\n- واجه جانبك المظلم وتحكم في نزواتك الهدامة.",
        "takeaways_en": "Empathy and self-awareness are the ultimate antidotes to interpersonal manipulation.",
        "takeaways_ar": "الوعي الذاتي والتعاطف هما الترياق الأقوى ضد الخداع والتلاعب الاجتماعي."
    },
    {
        "id": "10_The_Art_Of_Seduction",
        "title_en": "The Art of Seduction",
        "author": "Robert Greene",
        "title_ar": "فن الإغواء",
        "thesis_en": "Seduction is not merely about romance; it is a masterform of persuasion and soft power that creates emotional dependency through psychological fascination.",
        "thesis_ar": "الإغواء ليس مجرد شأن عاطفي؛ بل هو أحد أشكال الإقناع والقوة الناعمة التي تصنع الولاء والجاذبية النفسية الفائقة.",
        "points_en": "- The Seducer Archetypes: Siren, Rake, Ideal Lover, Dandy, Natural, Coquette, Charismatic, Star.\n- Generate distance and desire: mystery creates attraction.\n- Pay attention to detail: tailor words to the target's unfulfilled psychological cravings.",
        "points_ar": "- أنماط الشخصيات الجذابة: الفاتن، الحبيب المثالي، الغامض، الكاريزمي، والنجم.\n- اصنع مسافة وافرة للغموض: فالغموض يولد الرغبة والفضول.\n- اهتم بالتفاصيل الدقيقة وخاطب الرغبات النفسية غير المشبعة لدى الطرف الآخر.",
        "takeaways_en": "Seduction requires looking outward at what others lack and becoming the mirror of their desires.",
        "takeaways_ar": "الجاذبية تتطلب النظر إلى ما يفتقده الآخرون لتكون مرآة لرغباتهم وتطلعاتهم."
    },
    {
        "id": "11_The_50th_Law",
        "title_en": "The 50th Law",
        "author": "Robert Greene & 50 Cent",
        "title_ar": "القانون الخمسون",
        "thesis_en": "Fearlessness is the supreme power. When you eliminate fear, anxiety, and timidity, you gain total clarity and command over reality.",
        "thesis_ar": "الشجاعة التامة هي أعلى درجات القوة؛ فعندما تمحو الخوف والقلق والتردد، تكتسب صفاء الذهن والسيطرة الكاملة على الواقع.",
        "points_en": "- See things as they are: intense realism over wishful thinking.\n- Make everything your own: self-reliance.\n- Turn adversity into advantage (The Alchemist).\n- Confront your mortality to live with urgency and power.",
        "points_ar": "- انظر إلى الواقع كما هو بصرامة وتجرد، وتخلص من الأوهام.\n- اعتمد على نفسك بالكامل ولا تعول على مساعدة الآخرين.\n- حوّل المحن والعقبات إلى فرص ومكاسب (كيمياء القوة).\n- تذكر فناءك وحتمية الموت لتعيش بجرأة وشغف وحزم.",
        "takeaways_en": "The greatest danger you face is the fear in your own mind, which creates paralysis and invites defeat.",
        "takeaways_ar": "الخطر الأكبر الذي يهددك ليس الظروف الخارجية، بل الخوف الداخلي الذي يشل إرادتك ويستدرج الهزيمة."
    },
    {
        "id": "12_The_Daily_Laws",
        "title_en": "The Daily Laws: 366 Meditations on Power, Seduction, Mastery, Strategy, and Human Nature",
        "author": "Robert Greene",
        "title_ar": "القوانين اليومية: 366 تأملاً في القوة والإتقان والاستراتيجية",
        "thesis_en": "Daily bite-sized wisdom distilling Robert Greene's entire life's work into actionable morning meditations on discipline, psychological perception, and personal sovereignty.",
        "thesis_ar": "خلاصة مكثفة لأعمال روبرت جرين في تأملات يومية محكمة تهدف إلى بناء الانضباط، والوعي النفسي، والسيادة على الذات.",
        "points_en": "- Mastery: daily dedication to your craft.\n- Power: awareness of hierarchy and influence.\n- Strategy: playing the long game with composure.\n- Human Nature: emotional regulation and empathy.",
        "points_ar": "- الإتقان: التفاني اليومي في تنمية المهارة.\n- السطوة: الوعي بتوازنات القوة والنفوذ.\n- الاستراتيجية: الصبر والتركيز على الأهداف البعيدة.\n- الطبيعة البشرية: ضبط الانفعالات وفهم دوافع البشر.",
        "takeaways_en": "Wisdom is not read once; it is practiced daily until it becomes instinct.",
        "takeaways_ar": "الحكمة لا تُقرأ مرة واحدة؛ بل تُمارس يومياً حتى تصبح غريزة وسلوكاً طبيعياً."
    },
    # 4. Scripture & Spiritual Foundations
    {
        "id": "13_The_Holy_Quran",
        "title_en": "The Holy Quran: The Final Revelation",
        "author": "Divine Revelation",
        "title_ar": "القرآن الكريم: كتاب الهداية والإعجاز",
        "thesis_en": "The central religious text of Islam, revealed to the Prophet Muhammad over 23 years. A comprehensive spiritual, moral, legal, and linguistic guide establishing monotheism, justice, mercy, and human purpose.",
        "thesis_ar": "الكتاب الإلهي المنزل على خاتم الأنبياء محمد ﷺ، وهو دستور الهداية والرحمة والعدالة الذي يرسخ التوحيد ويزكي النفس ويقيم موازين القسط.",
        "points_en": "- 114 Surahs categorized into Makki (theology, afterlife, ethics) and Madani (legislation, governance, community).\n- Core doctrine of Tawhid (Absolute Oneness of God).\n- Balance of divine justice, universal mercy, and individual moral accountability.",
        "points_ar": "- 114 سورة موزعة بين مكي (يرسخ العقيدة والأخلاق وتزكية الروح) ومدني (ينظم المعاملات والتشريعات والمجتمع).\n- أصل الأصول: التوحيد الخالص لله وتنزيهه عن الشريك والند.\n- التوازن المطلق بين العدل والرحمة، والمسؤولية الأخلاقية الفردية أمام الله.",
        "takeaways_en": "A transformative blueprint for purifying the heart, living with justice, and fulfilling humanity's covenant with the Creator.",
        "takeaways_ar": "منهاج شامل لنقاء القلب، واستقامة السلوك، وعمارة الأرض بالعدل والرحمة والتقوى."
    },
    {
        "id": "14_Tafsir_Al_Mukhtasar",
        "title_en": "Tafsir Al-Mukhtasar (The Concise Quranic Commentary)",
        "author": "Scholarly Council (Markaz Tafsir)",
        "title_ar": "المختصر في تفسير القرآن الكريم",
        "thesis_en": "An authoritative, contemporary scholarly commentary explaining the meanings of every verse of the Quran concisely, adhering to sound orthodox principles, linguistic clarity, and moral lessons.",
        "thesis_ar": "تفسير معاصر موثق صاغته نخبة من علماء التفسير؛ يوضح معاني الآيات بدقة واختصار دون إخلال، مع استنباط الهدايات والفوائد العملية.",
        "points_en": "- Concise verse-by-verse clarification of vocabulary and syntax.\n- Clear statement of the central theme (maqsid) of each Surah.\n- Derivation of practical faith lessons and ethical guidance for daily living.",
        "points_ar": "- شرح مفردات الآيات وتراكيبها بعبارة عذبة ميسرة.\n- بيان المقصد العام لكل سورة ومحورها الأساسي.\n- استنباط الفوائد العقدية والتربوية والأخلاقية من كل صفحة.",
        "takeaways_en": "The Quran is meant to be contemplated (Tadabbur) and enacted in life, not merely recited phonetically.",
        "takeaways_ar": "القرآن أنزل ليتدبر ويعمل به؛ والتفسير الميسر هو المفتاح لفتح مغاليق الفهم وتدبر الآيات."
    },
    {
        "id": "15_The_Holy_Bible",
        "title_en": "The Holy Bible (Old and New Testaments)",
        "author": "Biblical Authors",
        "title_ar": "الكتاب المقدس (العهدان القديم والجديد)",
        "thesis_en": "The central sacred scripture of Christianity, comprising historical narratives, prophecy, poetry, and epistles tracing humanity's creation, the moral covenant, and salvation through Christ.",
        "thesis_ar": "الكتب المقدسة في المسيحية، تضم أسفار التاريخ والنبوات والحكمة والرسائل التي تتناول الخلق، العهد الإلهي، ورسالة المسيح.",
        "points_en": "- Old Testament (Hebrew Scriptures): Pentateuch, Historical books, Wisdom literature (Psalms, Proverbs), Prophets.\n- New Testament: Four Gospels, Acts of the Apostles, Pauline Epistles, and Revelation.\n- Central themes: Covenant, redemption, divine grace, and ethical love.",
        "points_ar": "- العهد القديم: أسفار موسى، الأسفار التاريخية، كتب الحكمة والمزامير، وأسفار الأنبياء.\n- العهد الجديد: الأناجيل الأربعة، أعمال الرسل، الرسائل الجامعة، وسفر الرؤيا.\n- المحاور الكبرى: العهد، الفداء، المحبة الإلهية، والوصايا الأخلاقية.",
        "takeaways_en": "A monumental literary and spiritual foundation of Western culture, jurisprudence, and moral philosophy.",
        "takeaways_ar": "مرجع ديني وأدبي وتاريخي أسس لجوانب كبرى من الفلسفة والأدب والحضارة العالمية."
    },
    # 5. Russian Literary Masterpieces
    {
        "id": "16_Crime_And_Punishment",
        "title_en": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "title_ar": "الجريمة والعقاب",
        "thesis_en": "Rationalist utilitarianism collapses before the moral law of the human conscience. True redemption requires confessing guilt, accepting suffering, and spiritual resurrection.",
        "thesis_ar": "النزعة النفعية العقلانية تنهار أمام صوت الضمير الفطري؛ والخلاص الروحي الحقيقي لا يتحقق إلا بالاعتراف بالذنب وتحمل المعاناة.",
        "points_en": "- Raskolnikov's 'Extraordinary Man' theory leads him to murder an old pawnbroker.\n- Psychological torment and alienation replace his expected triumph.\n- The intellectual duel with magistrate Porfiry Petrovich.\n- Sonya Marmeladova's faith guides Raskolnikov to confession and Siberian exile.",
        "points_ar": "- نظرية 'الإنسان الخارق' تدفع راسكولنيكوف لقتل مرابية عجوز لاختبار قدرته على تجاوز القوانين.\n- الرعب والانهيار النفسي والعزلة يحلون محل نشوة النصر المتوقعة.\n- المبارزة العقلية الممتعة بينه وبين المحقق الذكي بورفيري بيتروفيتش.\n- إيمان سونيا الصادق يقوده إلى الاعتراف، والمنفى في سيبيريا حيث تبدأ ولادته الروحية.",
        "takeaways_en": "No intellect can outsmart the human soul's intrinsic need for moral harmony.",
        "takeaways_ar": "لا يمكن لأي ذكاء أو فلسفة أن تتجاوز حاجة الروح الفطرية للتناغم مع الضمير والأخلاق."
    },
    {
        "id": "17_The_Brothers_Karamazov",
        "title_en": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "title_ar": "الإخوة كارامازوف",
        "thesis_en": "A monumental theological and philosophical exploration of faith, doubt, morality, and family pathology, culminating in the murder of Fyodor Karamazov.",
        "thesis_ar": "قمة الأدب الروسي وملحمة فلسفية تستكشف الإيمان والشك والمسؤولية الأخلاقية الفردية عبر مأساة أسرة كارامازوف.",
        "points_en": "- Dmitri embodies sensual passion and emotional turmoil.\n- Ivan represents intellectual rationalism, rebellion against suffering, and the Grand Inquisitor parable.\n- Alyosha embodies active Christian love, humility, and faith.\n- Smerdyakov represents nihilism and carries out the literal murder.",
        "points_ar": "- ديمتري يجسد الاندفاع العاطفي والتأرجح بين الفضيلة والرذيلة.\n- إيفان يجسد العقلانية الصارمة، والتمرد على عذاب الأبرياء، وأسطورة 'المفتش الأكبر'.\n- أليوشا يجسد النقاء والمحبة العملية والتسامح المطلق.\n- سميردياكوف يمثل العدمية والحقد، ويترجم أفكار إيفان إلى جريمة قتل واقعية.",
        "takeaways_en": "Everyone is responsible for all men and all things. Active love is the only answer to existential despair.",
        "takeaways_ar": "الجميع مسؤولون عن خطايا الجميع؛ والمحبة العملية الصادقة هي الجواب الوحيد على اليأس الوجودي."
    },
    {
        "id": "18_White_Nights",
        "title_en": "White Nights",
        "author": "Fyodor Dostoevsky",
        "title_ar": "الليالي البيضاء",
        "thesis_en": "A sentimental, lyrical novella exploring romantic idealism, loneliness, and the bittersweet transience of pure connection in St. Petersburg during the summer solstice.",
        "thesis_ar": "رواية شاعرية رقيقة تستكشف العزلة والوحدة والرومانسية الحالمة، وجمال اللحظات الإنسانية العابرة في ليالي بطرسبرغ البيضاء.",
        "points_en": "- The unnamed Dreamer wanders isolated through the streets of St. Petersburg.\n- He meets Nastenka weeping on a bridge; they share their inner worlds over four nights.\n- Nastenka loves another man who returns; she departs, leaving the Dreamer with grateful memories.",
        "points_ar": "- الحالم الوحيد الذي يعيش في أوهامه وخيالاته متجولاً في شوارع بطرسبرغ.\n- يلتقي بناستينكا الباكية على الجسر، ويتشاركان خفايا أرواحهما على مدار أربع ليالٍ بيضاء.\n- يعود حبيب ناستينكا الغائب فتغادر معه، تاركة الحالم ممتناً للحظة السعادة التي أضاءت حياته.",
        "takeaways_en": "A whole moment of bliss: is that too little, even for the whole of a man's life?",
        "takeaways_ar": "لحظة واحدة كاملة من السعادة الخالصة: ألا تكفي الإنسان ليعيش عليها عمراً بأكمله؟"
    },
    {
        "id": "19_War_And_Peace",
        "title_en": "War and Peace",
        "author": "Leo Tolstoy",
        "title_ar": "الحرب والسلام",
        "thesis_en": "A panoramic epic of Russian society during the Napoleonic Wars, interwoven with deep philosophical reflections on history, free will, and the search for authentic meaning.",
        "thesis_ar": "بانوراما ملحمية للمجتمع الروسي إبان الغزو النابليوني؛ تمزج دراما الأسر الأرستقراطية بتأملات فلسفية حول مسار التاريخ والإرادة الحرة.",
        "points_en": "- The interconnected lives of the Rostovs, Bolkonskys, and Bezukhovs.\n- Pierre Bezukhov's spiritual quest for purpose.\n- Prince Andrei Bolkonsky's pursuit of military glory and ultimate transcendence.\n- Natasha Rostova's vitality, mistakes, and emotional maturity.",
        "points_ar": "- تشابك مصائر عائلات روستوف وبولكونسكي وبيزوخوف وسط لهيب الحرب.\n- رحلة بيير بيزوخوف الفلسفية والروحية بحثاً عن معنى الوجود والسكينة.\n- الأمير أندريه بولكونسكي وصراعه بين المجد العسكري الزائل والتسامي الروحي.\n- ناتاشا روستوفا وتجسيدها لبهجة الحياة، وأخطائها، ونضجها الإنساني العميق.",
        "takeaways_en": "History is not driven by 'great men' like Napoleon, but by the collective, minute decisions of millions of ordinary individuals.",
        "takeaways_ar": "التاريخ لا تصنعه إرادة 'العظماء' كنابليون، بل حركة الجماهير وإرادة ملايين البشر العاديين وتفاعل أقدارهم."
    },
    {
        "id": "20_Anna_Karenina",
        "title_en": "Anna Karenina",
        "author": "Leo Tolstoy",
        "title_ar": "آنا كارينينا",
        "thesis_en": "A tragedy of passion, societal hypocrisy, and marriage, contrasting Anna's destructive extramarital love with Levin's rural search for faith, family, and spiritual peace.",
        "thesis_ar": "مأساة العاطفة الجارفة والنفاق الاجتماعي؛ تقارن بين قصة حب آنا المدمرة خارج الزواج، وبين رحلة ليفين في الريف بحثاً عن الإيمان والأسرة وسلام الروح.",
        "points_en": "- Anna abandons her loveless marriage to Karenin for Count Vronsky, facing total social ostracization.\n- Parallel plot of Konstantin Levin finding peace through rural labor, nature, and marriage to Kitty.\n- Anna's descent into jealousy, isolation, and her climactic suicide under the train.",
        "points_ar": "- آنا تضحي بزواجها البارد من كارينين في سبيل حب الكونت فرونسكي، فتواجه نبذاً اجتماعياً قاسياً.\n- المسار الموازي لقسطنطين ليفين الذي يجد خلاصه في العمل الزراعي والاندماج مع الطبيعة وزواجه من كيتي.\n- انهيار آنا النفسي تحت وطأة الغيرة والوحدة، وصولاً إلى نهايتها المأساوية تحت عجلات القطار.",
        "takeaways_en": "All happy families are alike; each unhappy family is unhappy in its own way.",
        "takeaways_ar": "كل العائلات السعيدة تتشابه، أما كل عائلة شقية فتشقى بطريقتها الخاصة."
    },
    {
        "id": "21_The_Master_And_Margarita",
        "title_en": "The Master and Margarita",
        "author": "Mikhail Bulgakov",
        "title_ar": "المعلم ومارغريتا (الشيطان يزور موسكو)",
        "thesis_en": "A brilliant satirical fantasy attacking Soviet censorship and materialism, juxtaposing the Devil's havoc in 1930s Moscow with Pontius Pilate's agonizing trial of Yeshua in ancient Jerusalem.",
        "thesis_ar": "تحفة ساخرة تهاجم الرقابة السوفيتية والمادية الإلحادية؛ تجمع بين زيارة الشيطان (فولاند) لموسكو في الثلاثينيات، ومحاكمة بيلاطس البنطي ليسوع في القدس القديمة.",
        "points_en": "- Woland (Satan) arrives in Moscow and exposes the greed, hypocrisy, and cowardice of the Soviet elite.\n- The Master, a persecuted novelist, is committed to an asylum for writing about Pontius Pilate.\n- Margarita makes a pact with Woland to become a witch, save the Master, and achieve eternal peace.",
        "points_ar": "- وصول فولاند (الشيطان) إلى موسكو ليفضح جشع ونفاق وجبن النخبة الأدبية والبيروقراطية.\n- المعلم، كاتب مضطهد، يودع مصحة عقلية بسبب روايته المرفوضة عن بيلاطس البنطي والمسيح.\n- مارغريتا تعقد صفقة مع الشيطان وتتحول إلى ساحرة لإنقاذ حبيبها المعلم والظفر بالسلام الأبدي.",
        "takeaways_en": "Manuscripts don't burn. Truth and genuine art endure beyond political tyranny.",
        "takeaways_ar": "المخطوطات لا تحترق؛ فالحقيقة والفن الأصيل يظلان خالدين فوق كل استبداد وقمع سياسي."
    },
    # 6. French Masterpieces
    {
        "id": "22_In_Search_Of_Lost_Time_Swanns_Way",
        "title_en": "In Search of Lost Time: Swann's Way",
        "author": "Marcel Proust",
        "title_ar": "البحث عن الزمن المفقود: جانب منازل سوان",
        "thesis_en": "A monumental exploration of involuntary memory, time, desire, and art. The taste of a madeleine dipped in tea unleashes the narrator's entire vanished childhood in Combray.",
        "thesis_ar": "ملحمة الذاكرة اللاإرادية واستعادة الزمن المفقود؛ حيث تنبعث طفولة الراوي كاملة في كومبريه بمجرد تذوق قطعة كعك 'المادلين' المغمسة في الشاي.",
        "points_en": "- Involuntary memory vs. intellectual recall: sensory triggers resurrect lost time.\n- Swann in Love: Charles Swann's obsessive, agonizing jealousy over the courtesan Odette de Crécy.\n- The transformation of fleeting, decaying life into immortal art.",
        "points_ar": "- الذاكرة اللاإرادية مقابل التذكر العقلاني: المحفزات الحسية تعيد إحياء الماضي حياً متدفقاً.\n- حب سوان: الهوس العاطفي والغيرة القاتلة التي كابدها شارل سوان تجاه أوديت.\n- خلود الفن: كيف يحول الأدب اللحظات الإنسانية الفانية إلى خلود أبدي.",
        "takeaways_en": "The only real voyage of discovery consists not in seeking new landscapes, but in having new eyes.",
        "takeaways_ar": "رحلة الاستكشاف الحقيقية لا تكمن في البحث عن أراضٍ جديدة، بل في امتلاك نظرة جديدة للأشياء."
    },
    {
        "id": "23_Les_Miserables",
        "title_en": "Les Misérables",
        "author": "Victor Hugo",
        "title_ar": "البؤساء",
        "thesis_en": "An epic social manifesto advocating mercy, redemption, and human dignity against legal cruelty, poverty, and institutional callousness in 19th-century France.",
        "thesis_ar": "بيان إنساني واجتماعي خالد ينتصر للرحمة والعدالة والكرامة ضد القسوة القانونية والفقر والاستبداد في فرنسا القرن التاسع عشر.",
        "points_en": "- Jean Valjean's transformation from hardened convict to saintly benefactor through Bishop Myriel's grace.\n- Inspector Javert's relentless, unbending legalism.\n- Fantine's sacrifice and Cosette's rescue.\n- The 1832 Paris June Rebellion and Marius's idealism.",
        "points_ar": "- تحول جان فالجان من سجين حاقد إلى قديس ومحسن بفضل تسامح الأسقف ميريل.\n- المفتش جافير وتجسيده للعدالة القانونية الصارمة والعمياء الخالية من الرحمة.\n- مأساة فانتين وتضحيتها، وإنقاذ فالجان لابنتها كوزيت.\n- ثورة باريس عام 1832 وبطولات الشباب الرومانسيين من أجل الحرية والعدل.",
        "takeaways_en": "To love another person is to see the face of God. Grace is infinitely higher than mere law.",
        "takeaways_ar": "أن تحب إنساناً هو أن ترى وجه الله؛ والرحمة والمغفرة أسمى بما لا يقاس من نصوص القوانين الجافة."
    },
    {
        "id": "24_Madame_Bovary",
        "title_en": "Madame Bovary",
        "author": "Gustave Flaubert",
        "title_ar": "مدام بوفاري",
        "thesis_en": "A ruthless portrait of romantic delusion and bourgeois banality. Emma Bovary's quest for romantic passion leads to adultery, financial ruin, and catastrophic despair.",
        "thesis_ar": "تشريح أدبي دقيق لأوهام الرومانسية الزائفة وتفاهة البرجوازية؛ حيث يقود هوس إيما بوفاري بالقصص الغرامية إلى الخيانة والديون والانتحار.",
        "points_en": "- Emma's marriage to the dull, kind doctor Charles Bovary fails to satisfy her romantic fantasies.\n- Affairs with Rodolphe and Léon reveal the same emptiness she sought to escape.\n- Predatory moneylender Lheureux exploits her debt, leading to her agonizing suicide by arsenic.",
        "points_ar": "- زواج إيما من الطبيب الطيب والبسيط شارل بوفاري يخيب آمالها الرومانسية الجامحة.\n- علاقاتها غير الشرعية مع رودولف وليون تكشف عن نفس الخواء الذي حاولت الفرار منه.\n- وقوعها في فخ الديون واستغلال المرابين يقودها إلى إنهاء حياتها بالزرنيخ وسط عذاب رهيب.",
        "takeaways_en": "Romantic escapism that despises the reality of daily duty inevitably destroys both self and family.",
        "takeaways_ar": "الهروب الرومانسي الذي يحتقر الواقع والمسؤولية اليومية يقود حتماً إلى تدمير الذات والأسرة."
    },
    {
        "id": "25_The_Stranger",
        "title_en": "The Stranger (L'Étranger)",
        "author": "Albert Camus",
        "title_ar": "الغريب",
        "thesis_en": "The foundational novel of the Absurd. Meursault refuses to lie about his feelings or conform to societal pretenses, choosing total honesty even when condemned to death.",
        "thesis_ar": "رواية الفلسفة العبثية؛ يرفض بطلها ميرسو الكذب وتزييف مشاعره إرضاءً للمجتمع، ويفضل مواجهة الإعدام بصدق تام وانسجام مع عبثية الكون.",
        "points_en": "- Meursault impassively attends his mother's funeral and shoots an Arab on a blindingly hot Algiers beach.\n- Society condemns him not for the killing, but because he didn't weep at his mother's grave.\n- Confronting the prison chaplain, Meursault embraces the benign indifference of the universe.",
        "points_ar": "- حضور ميرسو جنازة والدته ببرود وقتله لرجل عربي على شاطئ الجزائر تحت وطأة الشمس الحارقة.\n- المجتمع والقضاء يدينانه لأنه لم يبكِ في جنازة أمه ورفض ارتداء قناع النفاق الاجتماعي.\n- رفضه التوبة أمام الكاهن وتصالحه مع حتمية الموت ولامبالاة الكون العذبة.",
        "takeaways_en": "A hero who dies because he refuses to play the game of societal hypocrisy.",
        "takeaways_ar": "إنسان يموت لأنه يرفض أن يلعب لعبة النفاق الاجتماعي ويفضل الصدق المطلق مع نفسه."
    },
    {
        "id": "26_The_Little_Prince",
        "title_en": "The Little Prince (Le Petit Prince)",
        "author": "Antoine de Saint-Exupéry",
        "title_ar": "الأمير الصغير",
        "thesis_en": "A poetic, philosophical fable exposing the absurdities and narrow-mindedness of the adult world through the eyes of a young prince from asteroid B-612.",
        "thesis_ar": "خرافة فلسفية وشاعرية عميقة تفضح حماقات عالم الكبار وسطحيتهم، من خلال عيون أمير صغير قادم من كويكب بعيد.",
        "points_en": "- The Prince visits planets inhabited by archetypal foolish adults (King, Conceited Man, Businessman).\n- Arriving on Earth, he tames a Fox and learns the secret of love, responsibility, and uniqueness.\n- The Fox's secret: 'It is only with the heart that one can see rightly; what is essential is invisible to the eye.'",
        "points_ar": "- زيارة الأمير لكواكب يسكنها كبار سطحيون (الملك المستبد، المغرور، ورجل الأعمال المنشغل بعد النجوم).\n- هبوطه على الأرض ومصادقته للثعلب الذي يعلمه معنى الألفة والمسؤولية تجاه وردته الوحيدة.\n- سر الثعلب الخالد: 'لا يرى المرء جيداً إلا بقلبه؛ فالجوهر لا تراه الأعين'.",
        "takeaways_en": "You become responsible, forever, for what you have tamed.",
        "takeaways_ar": "أنت مسؤول إلى الأبد عن كل ما تألفه وتمنحه حبك واهتمامك."
    },
    {
        "id": "27_The_Red_And_The_Black",
        "title_en": "The Red and the Black",
        "author": "Stendhal",
        "title_ar": "الأحمر والأسود",
        "thesis_en": "A psychological masterwork detailing Julien Sorel's ambitious ascent through French Restoration society using hypocrisy and passion, torn between the army (Red) and the church (Black).",
        "thesis_ar": "تشريح نفسي واجتماعي لطموح الشاب جوليان سوريل وسعيه للصعود الطبقي في فرنسا، متأرجحاً بين سيف الجيش (الأحمر) ورداء الكنيسة (الأسود).",
        "points_en": "- Julien's humble provincial origins and idolization of Napoleon.\n- Romantic intrigues with Madame de Rênal and Mathilde de La Mole.\n- His pride and hypocrisy culminate in shooting Madame de Rênal at church, followed by his dignified execution.",
        "points_ar": "- أصول جوليان البسيطة وانبهاره بعبقرية نابليون ورغبته في كسر القيود الطبقية.\n- مغامراته العاطفية المعقدة مع مدام دي رينال وماتيلد دي لا مول.\n- إطلاقه النار على مدام دي رينال بدافع الكبرياء المجروح، واستقباله للمقصلة برباطة جأش.",
        "takeaways_en": "Ambitious hypocrisy can elevate you socially, but true authenticity will always demand an ultimate reckoning.",
        "takeaways_ar": "النفاق الاجتماعي قد يرفعك إلى القمة، لكن ثمنه باهظ حين تصطدم الحقيقة بضميرك الداخلي."
    },
    # 7. English, Irish & Scottish Classics
    {
        "id": "28_Ulysses",
        "title_en": "Ulysses",
        "author": "James Joyce",
        "title_ar": "يوليسيس",
        "thesis_en": "The pinnacle of modernist literature, chronicling a single day (June 16, 1904) in the life of Leopold Bloom in Dublin, paralleling Homer's Odyssey through revolutionary stream-of-consciousness.",
        "thesis_ar": "ذروة الأدب الحداثي؛ ترصد يوماً واحداً (16 يونيو 1904) في حياة ليوبولد بلوم في دبلن، في محاكاة عبقرية لملحمة هوميروس عبر تيار الوعي.",
        "points_en": "- Leopold Bloom (Odysseus) traverses Dublin as an ad canvasser, gentle, observant, and cuckolded.\n- Stephen Dedalus (Telemachus) seeks intellectual independence and a spiritual father.\n- Molly Bloom's (Penelope) unpunctuated final monologue affirming life and love: 'yes I said yes I will Yes.'",
        "points_ar": "- ليوبولد بلوم (عوليس/أوديسيوس) يتجول في دبلن كبائع إعلانات مسالم ومراقب لعيوب مجتمعه.\n- ستيفن ديدالوس (تليماخوس) الشاب المثقف الباحث عن هوية وأب روحي.\n- مونولوج مولي بلوم (بينيلوبي) الختامي الشهير الخالي من علامات الترقيم، الذي يعلن قبول الحياة والحب: 'نعم قلت نعم سأفعل نعم'.",
        "takeaways_en": "The heroic epic is found not in mythical battles, but in the mundane, tender, and chaotic thoughts of ordinary daily human life.",
        "takeaways_ar": "البطولة الملحمية لا تكمن في حروب الآلهة القديمة، بل في التفاصيل اليومية البسيطة والمشاعر الإنسانية العادية."
    },
    {
        "id": "29_1984",
        "title_en": "Nineteen Eighty-Four (1984)",
        "author": "George Orwell",
        "title_ar": "١٩٨٤",
        "thesis_en": "The ultimate warning against totalitarian tyranny. The Party controls past, present, language, and truth, breaking individual humanity through surveillance and fear.",
        "thesis_ar": "التحذير الأكبر من الاستبداد الشمولي؛ حيث يتحكم الحزب في التاريخ واللغة والوعي الإنساني عبر الرقابة المطلقة والتعذيب الممنهج.",
        "points_en": "- Newspeak, Doublethink, and the Ministry of Truth rewriting facts.\n- Winston Smith's secret diary and illicit love affair with Julia.\n- Betrayal by O'Brien and torture in Room 101.\n- Total surrender: Winston betrays Julia and learns to 'love Big Brother.'",
        "points_ar": "- اللغة الجديدة (نيوسبيك)، التفكير المزدوج، وحرق الحقائق التاريخية في وزارة الحقيقة.\n- تمرد وينستون سميث السري وعلاقته العاطفية مع جوليا.\n- خيانة أوبراين له وتعذيبه الممنهج في الغرفة 101 بمواجهة مخاوفه القصوى.\n- الانهيار التام: وينستون يفرط في كرامته ويخون جوليا ليعلن خضوعه وحبه للأخ الأكبر.",
        "takeaways_en": "Freedom is the freedom to say that two plus two make four. If that is granted, all else follows.",
        "takeaways_ar": "الحرية هي أن تملك الحق في القول بأن اثنين زائد اثنين يساوي أربعة؛ وإذا سُلب هذا الحق سقط كل شيء."
    },
    {
        "id": "30_Animal_Farm",
        "title_en": "Animal Farm",
        "author": "George Orwell",
        "title_ar": "مزرعة الحيوان",
        "thesis_en": "A satirical allegorical novella exposing how revolutionary idealism is inevitably corrupted by ruthless dictators into tyrannical totalitarianism.",
        "thesis_ar": "رواية رمزية ساخرة تفضح كيف تُختطف الثورات والآمال التحررية لتتحول إلى استبداد أشد قسوة على أيدي الطغاة الجدد.",
        "points_en": "- Animals overthrow their drunken human master Mr. Jones to establish equality.\n- The pigs (Napoleon and Snowball) seize leadership; Napoleon exiles Snowball with guard dogs.\n- The Seven Commandments are gradually altered until: 'All animals are equal, but some animals are more equal than others.'\n- The pigs walk on two legs and become indistinguishable from their human oppressors.",
        "points_ar": "- تمرد الحيوانات وطرد المالك المستبد لإقامة مجتمع عادل تسوده المساواة.\n- استيلاء الخنازير (نابليون وسنوبول) على السلطة، ونفي سنوبول بالكلاب الشرسة.\n- تحريف الوصايا السبع تدريجياً حتى تختصر في: 'كل الحيوانات متساوية، لكن بعضها أكثر مساواة من غيرها'.\n- ختام الرواية: الخنازير تمشي على قدمين وتشرب مع البشر، ويعجز الناظر عن التمييز بين الخنزير والإنسان.",
        "takeaways_en": "Revolutions only result in a change of masters if citizens fail to remain eternally vigilant against power.",
        "takeaways_ar": "الثورات لا تغير سوى وجوه الحكام إذا تخلت الشعوب عن يقظتها النقدية وحمايتها للحرية."
    },
    {
        "id": "31_Pride_And_Prejudice",
        "title_en": "Pride and Prejudice",
        "author": "Jane Austen",
        "title_ar": "كبرياء وتحامل",
        "thesis_en": "A sparkling social comedy of manners and courtship examining how false first impressions, personal pride, and hasty prejudice obstruct genuine love and mutual respect.",
        "thesis_ar": "كوميديا اجتماعية متألقة ترصد كيف تعمي الأحكام المسبقة والكبرياء الزائف الإنسان عن رؤية معادن الآخرين والحب الصادق.",
        "points_en": "- Elizabeth Bennet's quick wit and prejudice against the wealthy, aloof Mr. Darcy.\n- Darcy's aristocratic pride humbled by Elizabeth's rejection.\n- Darcy secretly rescues the Bennet family from social ruin over Lydia's elopement.\n- Elizabeth overcomes her misjudgment, recognizing Darcy's true nobility.",
        "points_ar": "- ذكاء إليزابيث بينيت الحاد وتحاملها المسبق على السيد دارسي المتكبر ظاهرياً.\n- انكسار كبرياء دارسي الأرستقراطي بعد رفض إليزابيث عرضه الأول للزواج.\n- إنقاذ دارسي للأسرة سراً من العار الاجتماعي عقب هروب ليديا مع ويكهام.\n- نضج إليزابيث واكتشافها لنبل دارسي الحقيقي وتتويج علاقتهما بالزواج.",
        "takeaways_en": "True self-knowledge requires overcoming both the vanity of your own intellect and premature judgments of others.",
        "takeaways_ar": "النضج الحقيقي يتطلب التحرر من غرور العقل والتريث قبل إطلاق الأحكام المتسرعة على الناس."
    },
    {
        "id": "32_Wuthering_Heights",
        "title_en": "Wuthering Heights",
        "author": "Emily Brontë",
        "title_ar": "مرتفعات وذرنغ",
        "thesis_en": "A ferocious, gothic masterpiece of all-consuming, destructive passion and multi-generational revenge between Heathcliff and Catherine Earnshaw on the Yorkshire moors.",
        "thesis_ar": "رواية قوطية عاصفة عن العاطفة المدمرة والانتقام الجامح الممتد عبر جيلين بين هيثكليف وكاثرين في سهوب يوركشاير.",
        "points_en": "- Heathcliff's orphan adoption, abuse by Hindley, and elemental bond with Catherine.\n- Catherine marries Edgar Linton for social status, shattering Heathcliff's soul.\n- Heathcliff returns wealthy and enacts a methodical, demonic vengeance on both families.\n- Catherine's daughter and Hindley's son eventually break the cycle of hate with gentle love.",
        "points_ar": "- تبني هيثكليف كطفل يتيم، وتعرضه للاضطهاد، وارتباطه الروحي العاصف بكاثرين.\n- زواج كاثرين من إدغار لينتون بحثاً عن المكانة الاجتماعية، مما يشعل نيران الحقد في قلب هيثكليف.\n- عودة هيثكليف ثرياً وتدبيره لانتقام ممنهج يدمر العائلتين عبر جيلين.\n- كسر حلقة الكراهية في النهاية بالحب النقي بين ابنة كاثرين وابن هندلي.",
        "takeaways_en": "Obsessive love that turns into bitter revenge destroys everything in its path, including the avenger.",
        "takeaways_ar": "الحب الهوسي الذي ينقلب إلى رغبة في الانتقام يدمر كل ما حوله، ويفني المنتقم نفسه في النهاية."
    },
    {
        "id": "33_Jane_Eyre",
        "title_en": "Jane Eyre",
        "author": "Charlotte Brontë",
        "title_ar": "جين إير",
        "thesis_en": "A groundbreaking feminist bildungsroman chronicling an orphaned governess's fierce moral integrity, spiritual independence, and enduring love for the brooding Mr. Rochester.",
        "thesis_ar": "رواية رائدة ترصد نضال فتاة يتيمة تتمسك بكرامتها ونزاهتها الأخلاقية واستقلاليتها، في مواجهة قسوة المجتمع والحب المعقد للسيد روتشستر.",
        "points_en": "- Jane survives cruel abuse at Gateshead and Lowood School with unyielding inner dignity.\n- As governess at Thornfield Hall, she falls in love with Edward Rochester.\n- On their wedding day, Rochester's secret mad wife in the attic (Bertha Mason) is revealed.\n- Jane refuses to be his mistress, departs in poverty, but returns once they are moral equals.",
        "points_ar": "- صمود جين أمام سوء المعاملة في ميتم لووود متمسكة بكرامتها ونقائها الداخلي.\n- عملها كمربية في قصر ثورنفيلد ووقوعها في حب السيد إدوارد روتشستر.\n- اكتشاف سر الزوجة المجنونة الحبيسة في العلية يوم الزفاف.\n- رفض جين أن تكون عشيقة وهروبها، ثم عودتها إليه بعد توبته وحريق القصر متكافئين في الروح والحرية.",
        "takeaways_en": "Never sacrifice your moral conscience or self-respect for emotional convenience or romantic desire.",
        "takeaways_ar": "إياك أن تضحي بضميرك الأخلاقي أو احترامك لذاتك في سبيل أي رغبة عاطفية عابرة."
    },
    {
        "id": "34_Great_Expectations",
        "title_en": "Great Expectations",
        "author": "Charles Dickens",
        "title_ar": "آمال عظيمة",
        "thesis_en": "A profound moral examination of ambition, wealth, and redemption. Pip learns that true nobility is found in loyalty and kindness, not social status or money.",
        "thesis_ar": "ملحمة إنسانية تفضح بريق الثروة الزائف؛ يتعلم الصبي بيب أن النبل الحقيقي يكمن في الوفاء والمحبة الصادقة، وليس في الطبقة الاجتماعية أو المال.",
        "points_en": "- Pip aids the escaped convict Magwitch on the marshes.\n- He is summoned to Miss Havisham's decaying mansion and falls desperately in love with the cruel Estella.\n- An anonymous benefactor gifts him fortune, making Pip ashamed of his loyal blacksmith brother-in-law Joe Gargery.\n- Magwitch, not Miss Havisham, is revealed as his benefactor; Pip repents and discovers genuine humility.",
        "points_ar": "- مساعدة الصبي بيب للمحكوم الهارب ماغويتش في المستنقعات.\n- استدعاؤه لقصر الآنسة هافيشام المعتم ووقوعه في حب إستيلا المتكبرة.\n- تلقيه ثروة غامضة تجعله يتنكر لأصوله البسيطة ويخجل من صهره الطيب جو غارجيري.\n- اكتشاف أن المحكوم الهارب هو صاحب الفضل، وتوبة بيب وعودته للقيم الإنسانية الأصيلة.",
        "takeaways_en": "Social snobbery corrupts the soul; the humble kindness of ordinary people is worth more than all inherited fortunes.",
        "takeaways_ar": "الغرور الطبقي يلوث الروح؛ وطيبة البسطاء ووفاؤهم أثمن من كل كنوز العالم."
    },
    {
        "id": "35_David_Copperfield",
        "title_en": "David Copperfield",
        "author": "Charles Dickens",
        "title_ar": "ديفيد كوبرفيلد",
        "thesis_en": "Dickens's most personal, semi-autobiographical masterpiece following David's journey through childhood trauma, debtor's prisons, perseverance, and emotional maturity.",
        "thesis_ar": "الرواية الأقرب إلى قلب ديكنز وسيرته الذاتية؛ تسرد رحلة ديفيد من الطفولة المعذبة والفقر إلى المثابرة والنجاح الأدبي والنضج العاطفي.",
        "points_en": "- David endures the cruel cruelty of stepfather Mr. Murdstone and child labor in a London factory.\n- The unforgettable friendship with eccentric optimist Mr. Micawber.\n- Flight to Aunt Betsey Trotwood and his emergence as an author.\n- Loss of youthful romantic illusion (Dora) and finding mature companionship with Agnes Wickfield.",
        "points_ar": "- قسوة زوج الأم موردستون وإرسال ديفيد للعمل الشاق في مصنع لندني وهو طفل.\n- صداقته للرجل المتفائل غريب الأطوار ميكاوبر.\n- لجوؤه إلى عمته الحازمة بيتسي تروتوود وبداية مسيرته ككاتب عصامي.\n- نضجه العاطفي بعد زواجه الأول الساذج من دورا، واستقراره أخيراً مع رفيقة دربه أغنيس.",
        "takeaways_en": "Perseverance, moral earnestness, and a resilient heart can turn the darkest childhood neglect into literary and human triumph.",
        "takeaways_ar": "الإصرار والاجتهاد ونقاء السريرة كفيلة بتحويل أقسى محن الطفولة إلى نجاح إنساني وأدبي عظيم."
    },
    {
        "id": "36_Frankenstein",
        "title_en": "Frankenstein; or, The Modern Prometheus",
        "author": "Mary Shelley",
        "title_ar": "فرانكنشتاين (بروميثيوس المعاصر)",
        "thesis_en": "A cautionary masterpiece about scientific hubris, the abandonment of parental responsibility, and the tragic consequences of monstrous prejudice against the lonely and unloved.",
        "thesis_ar": "تحفة أدبية تحذر من الغرور العلمي والتجرؤ على أسرار الخلق؛ وتفضح نبذ المجتمع للقبيح والمختلف ودفع البريء نحو الجريمة بفعل القسوة.",
        "points_en": "- Victor Frankenstein animates a creature from corpse parts, then flees in disgust.\n- The abandoned creature desires kindness and education, but is violently attacked by humanity.\n- Consumed by bitter solitude, the creature demands a mate, which Victor destroys.\n- A catastrophic cycle of vengeance leads Victor and his creation across the Arctic ice to death.",
        "points_ar": "- فيكتور فرانكنشتاين يبعث الحياة في مسخ مجمع من الجثث، ثم يفزع منه ويهجره بجبن.\n- المخلوق يطلب الحنان والتعلم، لكنه يواجه بالضرب والنبذ والاشمئزاز من كل من يراه.\n- يقوده الحرمان والوحدة إلى طلب رفيقة، وحين يخلف فيكتور وعده، يبدأ المسخ انتقاماً مدمراً.\n- مطاردة متبادلة في جليد القطب الشمالي تنتهي بهلاك الصانع وندم المخلوق الحزين.",
        "takeaways_en": "Knowledge without ethical responsibility creates monsters; neglect and lack of love turn innocence into vengeful fury.",
        "takeaways_ar": "العلم المنسلخ من الأخلاق يولد كوارث؛ والإهمال والقسوة يحولان البراءة الفطرية إلى وحش كاسر."
    },
    {
        "id": "37_The_Picture_Of_Dorian_Gray",
        "title_en": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "title_ar": "صورة دوريان غراي",
        "thesis_en": "A decadent philosophical fable on aestheticism, vanity, and the moral corruption of a man whose painted portrait ages and rots while his physical body remains eternally young.",
        "thesis_ar": "رواية فلسفية تكشف مأساة الانغماس في اللذة والغرور؛ حيث تظل ملامح الشاب دوريان غراي شابة بينما تنعكس كل خطاياه وقبحه الداخلي على لوحته الشخصية.",
        "points_en": "- Lord Henry Wotton seduces Dorian into pure hedonistic aestheticism.\n- Basil Hallward paints Dorian's peerless portrait; Dorian wishes the painting age in his place.\n- Dorian engages in betrayal, murder, and vice without a single physical blemish.\n- In agony, Dorian slashes the painting, inadvertently stabbing his own withered, grotesque heart.",
        "points_ar": "- اللورد هنري يغوي دوريان بفلسفة اللذة المطلقة وتقديس الجمال الخارجي.\n- الرسام بازيل هالوارد يرسم لوحة دوريان الرائعة، فيتمنى دوريان أن تشيخ اللوحة بدلاً منه.\n- يغرق دوريان في الرذائل والجرائم وتدمير الآخرين دون أن تتأثر وسامته الخارجية.\n- في لحظة يأس يحاول تمزيق اللوحة بسكين، فيطعن قلبه هو ويتحول إلى جثة مشوهة عجوز.",
        "takeaways_en": "What does it profit a man if he gains the whole world and loses his own soul?",
        "takeaways_ar": "ماذا ينفع الإنسان لو ربح العالم كله وخسر روحه ونقاءه الداخلي؟"
    },
    {
        "id": "38_Heart_Of_Darkness",
        "title_en": "Heart of Darkness",
        "author": "Joseph Conrad",
        "title_ar": "قلب الظلام",
        "thesis_en": "A haunting descent up the Congo River uncovering the savage hypocrisy of European colonial imperialism and the terrifying psychological abyss lurking within the human soul.",
        "thesis_ar": "رحلة كابوسية في نهر الكونغو تفضح النفاق الاستعماري الأوروبي ووحشيته، وتكشف الهاوية المظلمة الكامنة في أعماق النفس البشرية عند غياب الرادع.",
        "points_en": "- Marlow journeys to Africa as a steamboat captain for an ivory trading company.\n- He witnesses the brutal exploitation and horrific treatment of native Africans.\n- He encounters Mr. Kurtz, a charismatic ivory agent worshipped as a demigod by local tribes.\n- Kurtz's dying, whispered revelation of truth: 'The horror! The horror!'",
        "points_ar": "- مارلو يقود زورقاً بخارياً في أعماق أفريقيا لصالح شركة تجارة عاج استعمارية.\n- يصطدم بالاستغلال الوحشي البشع للأفارقة تحت شعارات 'التنوير والحضارة'.\n- يلتقي بالسيد كورتز، وكيل العاج العبقري الذي استسلم لجنون السلطة المطلقة ونصب نفسه إلهاً.\n- كلمات كورتز الأخيرة وهو يحتضر ملخصاً حقيقة النفس البشرية: 'الرعب! الرعب!'.",
        "takeaways_en": "Civilization is a fragile veneer; remove societal constraints, and the primitive darkness within humanity erupts.",
        "takeaways_ar": "الحضارة قناع هش؛ فإذا سقطت القيود، انفجرت الوحشية والظلمة الكامنة في قلب الإنسان."
    },
    {
        "id": "39_To_The_Lighthouse",
        "title_en": "To the Lighthouse",
        "author": "Virginia Woolf",
        "title_ar": "إلى الفنار",
        "thesis_en": "A modernist stream-of-consciousness meditation on the passage of time, family dynamics, grief, gender roles, and the transient nature of human existence centered around the Ramsay family.",
        "thesis_ar": "عمل حداثي رائد يتأمل مرور الزمن، والفقد، والعلاقات الأسرية، وعزاء الفن، من خلال رحلة أسرة رامزي الصيفية المؤجلة إلى الفنار.",
        "points_en": "- The Window: domestic tensions and warm matriarchal presence of Mrs. Ramsay on the Isle of Skye.\n- Time Passes: ten years vanish in poetic brevity; war, decay, and death sweep through the empty house.\n- The Lighthouse: the remaining family finally sails to the lighthouse while artist Lily Briscoe completes her vision.",
        "points_ar": "- النافذة: المشاعر الأسرية ودفء السيدة رامزي في منزلهم الصيفي في اسكتلندا.\n- مرور الزمن: عقد كامل يمر في فصول سريعة تموج بالحرب والموت والخراب.\n- الفنار: العائلة المتبقية تبحر أخيراً إلى الفنار، بينما تكمل الرسامة ليلي بريسكو لوحتها الفنية ورؤيتها للعالم.",
        "takeaways_en": "Love and genuine artistic vision provide the only fleeting permanence against the unstoppable erosion of time.",
        "takeaways_ar": "المحبة والرؤية الفنية الصادقة هما الملاذ الوحيد للبقاء والخلود في مواجهة تيار الزمن الجارف."
    },
    {
        "id": "40_Mrs_Dalloway",
        "title_en": "Mrs. Dalloway",
        "author": "Virginia Woolf",
        "title_ar": "السيدة دالواي",
        "thesis_en": "A single day in post-WWI London contrasting Clarissa Dalloway's high-society party preparations with shell-shocked veteran Septimus Warren Smith's psychological collapse.",
        "thesis_ar": "يوم واحد في لندن ما بعد الحرب العالمية الأولى؛ يقارن بين استعدادات كلاريسا دالواي لحفلتها المخملية، وبين الانهيار النفسي للمحارب القديم سيبتيموس سميث.",
        "points_en": "- Stream-of-consciousness narrative moving seamlessly between minds, memory, and street sounds.\n- Clarissa reflects on choices made, lost loves (Peter Walsh), and social masks.\n- Septimus suffers from PTSD, dismissed by arrogant doctors, and jumps to his death.\n- Clarissa hears of the suicide at her party, understanding his sacrifice as an act of defiance against a stifling world.",
        "points_ar": "- تيار وعي يربط بين الذكريات وأصوات ساعة بيغ بن وشوارع لندن النابضة.\n- كلاريسا تتأمل خيارات شبابها وحبها الضائع لبيتر والش وحياتها الاجتماعية.\n- سيبتيموس يعاني من صدمة الحرب واكتئاب حاد يجهله الأطباء، فينتحر هرباً من القيد.\n- كلاريسا تبلغ بنبأ انتحاره وسط الحفلة، فتدرك عمق مأساته كصرخة تمرد في وجه زيف العالم.",
        "takeaways_en": "Life is a luminous halo; every ordinary hour contains the eternity of human joy and grief.",
        "takeaways_ar": "الحياة هالة مضيئة؛ وفي تفاصيل كل ساعة عادية تتجلى كل أفراح البشرية وأحزانها العميقة."
    },
    {
        "id": "41_The_Lord_Of_The_Rings",
        "title_en": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "title_ar": "سيد الخواتم",
        "thesis_en": "The definitive epic fantasy myth of Middle-earth. The corrupting burden of absolute power, the selfless heroism of the humble, and the enduring light of friendship against overwhelming darkness.",
        "thesis_ar": "الملحمة الكبرى للأرض الوسطى؛ تحذر من فساد السلطة المطلقة، وتنتصر لبطولة البسطاء والمستضعفين، ووفاء الصداقة في وجه ظلمات اليأس.",
        "points_en": "- Frodo Baggins undertakes the perilous quest to cast the One Ring into Mount Doom.\n- The Fellowship of the Ring fractures under war, temptation, and sacrifice.\n- Aragorn claims his ancestral kingship; Rohan and Gondor unite against Mordor.\n- Pity and mercy: Gollum's desperate treachery inadvertently completes the Ring's destruction.",
        "points_ar": "- فرودو باجنز يحمل عبء الخاتم الأوحد في رحلة مضنية لتدميره في نيران جبل الهلاك.\n- تشتت رفقة الخاتم وخوضهم معارك مصيرية لإنقاذ حرية العالم.\n- استعادة أراغورن لعرشه المفقود وتوحد الأمم ضد قوى الشر في موردور.\n- دور الشفقة والرحمة: غولوم وتشبثه بالخاتم هو ما يقود في النهاية إلى تدمير الشر إلى الأبد.",
        "takeaways_en": "Even the smallest person can alter the course of the future.",
        "takeaways_ar": "حتى أصغر إنسان وأبسطه قادر على تغيير مسار التاريخ ومصير العالم."
    },
    # 8. American Classics
    {
        "id": "42_The_Great_Gatsby",
        "title_en": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "title_ar": "غاتسبي العظيم",
        "thesis_en": "A lyrical critique of the corruption of the American Dream in the 1920s Jazz Age, exposing the hollowness of material excess and the impossibility of resurrecting the past.",
        "thesis_ar": "نقد لاذع لوهم 'الحلم الأمريكي' في عصر الجاز؛ يفضح خواء الثروة المادية واستحالة استعادة الماضي المستحيل.",
        "points_en": "- Jay Gatsby's lavish mansion and yearning for the green light on Daisy Buchanan's dock.\n- The careless, destructive entitlement of Tom and Daisy Buchanan.\n- Myrtle Wilson's tragic death and Gatsby's solitary murder in his pool.\n- The tragic emptiness of his funeral: all who partied abandon him.",
        "points_ar": "- حفلات جاي غاتسبي الباذخة وتطلعه اليومي نحو الضوء الأخضر على رصيف حبيبته ديزي.\n- قسوة ولا مبالاة الأثرياء توم وديزي بيوكانان اللذين يحطمان حياة الآخرين ويلوذان بالمال.\n- مقتل غاتسبي في حوض سباحته ظلماً بعد تحمله ذنب ديزي.\n- خلو جنازته من آلاف الضيوف الذين احتفلوا في قصره.",
        "takeaways_en": "So we beat on, boats against the current, borne back ceaselessly into the past.",
        "takeaways_ar": "وهكذا نمضي قدماً، كقوارب تصارع التيار، تُرد دون انقطاع إلى الماضي."
    },
    {
        "id": "43_Moby_Dick",
        "title_en": "Moby-Dick; or, The Whale",
        "author": "Herman Melville",
        "title_ar": "موبي ديك",
        "thesis_en": "An encyclopedic metaphysical tragedy depicting Captain Ahab's monomaniacal vengeance against the giant white whale, exploring human obsession and cosmic indifference.",
        "thesis_ar": "تراجيديا فلسفية كونية تصور هوس القبطان أهاب بالانتقام من الحوت الأبيض الضخم، مستكشفة حدود المعرفة وغطرسة الإنسان أمام قوى الطبيعة.",
        "points_en": "- Ishmael boards the doomed whaling ship Pequod with pagan harpooner Queequeg.\n- Ahab hijacks the commercial voyage into a fanatical personal vendetta.\n- The white whale shatters the ship, drowning all crew; Ishmael survives on Queequeg's coffin.",
        "points_ar": "- إسماعيل يصعد على متن سفينة صيد الحيتان المنكوبة مع صديقه صائد الحيتان كويكويغ.\n- القبطان أهاب يحول الرحلة التجارية إلى مطاردة انتحارية مسكونة بالهوس والانتقام.\n- الحوت يحطم السفينة ويغرق الطاقم بأكمله؛ وينجو إسماعيل وحده طافياً فوق تابوت صديقه.",
        "takeaways_en": "Blind obsession destroys the seeker and all who follow him.",
        "takeaways_ar": "الهوس الأعمى بالانتقام يفني صاحبه ويهلك كل من يتبعه في طريقه."
    },
    {
        "id": "44_The_Catcher_In_The_Rye",
        "title_en": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "title_ar": "الحارس في حقل الشوفان",
        "thesis_en": "A profound exploration of teenage alienation, grief, and the struggle to protect innocent childhood from the phoniness and corruption of the adult world.",
        "thesis_ar": "استكشاف عميق لاغتراب المراهقة وألم الفقد؛ وصراع الشاب هولدن كولفيلد لحماية براءة الطفولة من زيف ونفاق عالم الكبار.",
        "points_en": "- Holden Caulfield wanders New York City after being expelled from prep school.\n- He rails against societal phoniness while mourning his deceased younger brother Allie.\n- His fantasy: standing in a rye field catching children before they fall off the cliff into adulthood.\n- Solace with his sister Phoebe, realizing children must be allowed to grow and fall.",
        "points_ar": "- هولدن كولفيلد يتجول تائهاً في نيويورك بعد طرده من المدرسة الداخلية.\n- ينفر من نفاق المجتمع ويكابد حزناً دفيناً على وفاة شقيقه الصغير آلي.\n- حلمه الرمزي: أن يقف حارساً في حقل شوفان ليمسك بالأطفال قبل أن يسقطوا من هاوية النضج.\n- سكينته مع شقيقته الصغيرة فيبي وإدراكه أن الإنسان لا بد أن ينمو ويختبر الحياة بنفسه.",
        "takeaways_en": "You cannot freeze innocence in time; growing up requires confronting life's imperfections with compassion.",
        "takeaways_ar": "لا يمكنك تجميد براءة الطفولة إلى الأبد؛ والنضج يتطلب مواجهة عيوب العالم بالصبر والتعاطف."
    },
    {
        "id": "45_To_Kill_A_Mockingbird",
        "title_en": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "title_ar": "لا تقتل عصفوراً ساخراً",
        "thesis_en": "A moral masterpiece seen through Scout Finch's eyes, chronicling her lawyer father Atticus's heroic defense of a falsely accused Black man in the racially segregated American South.",
        "thesis_ar": "ملحمة أخلاقية بعيون الطفلة سكوت فينش؛ تروي دفاع والدها المحامي النبيل أتيكوس عن رجل أسود اتهم ظلماً، في الجنوب الأمريكي العنصري.",
        "points_en": "- Scout and Jem grow up learning empathy in Maycomb, Alabama.\n- Atticus defends Tom Robinson despite public hatred and threats.\n- Tom is unjustly convicted by an all-white jury, exposing entrenched systemic prejudice.\n- Reclusive neighbor Boo Radley saves the children, proving the gentleness of misunderstood souls.",
        "points_ar": "- سكوت وشقيقها جيم يتعلمان دروس الإنسانية والتسامح في بلدة ميكومب.\n- أتيكوس يتولى الدفاع عن توم روبنسون متمسكاً بضميره رغم التهديدات والعنصرية السائدة.\n- إدانة توم ظلماً من هيئة محلفين عنصرية تكشف مرارة الظلم الاجتماعي.\n- الجار المنعزل بو رادلي ينقذ الأطفال ويثبت نبل الأرواح التي يسيء المجتمع فهمها.",
        "takeaways_en": "Real courage is when you know you're licked before you begin, but you begin anyway and see it through no matter what.",
        "takeaways_ar": "الشجاعة الحقيقية هي أن تعلم أنك مهزوم مسبقاً قبل أن تبدأ، ولكنك تبدأ وتخوض المعركة حتى النهاية لأنها الحق."
    },
    {
        "id": "46_Adventures_Of_Huckleberry_Finn",
        "title_en": "Adventures of Huckleberry Finn",
        "author": "Mark Twain",
        "title_ar": "مغامرات هكلبيري فين",
        "thesis_en": "A seminal American masterpiece satirizing societal hypocrisy, racism, and religious bigotry as a runaway boy and an enslaved man travel down the Mississippi River.",
        "thesis_ar": "تحفة الأدب الأمريكي التي تسخر من النفاق الاجتماعي والعنصرية؛ تروي رحلة صبي هارب وعبد مزارع يبحث عن حريته على طوف في نهر المسيسيبي.",
        "points_en": "- Huck escapes his abusive father and rafts down the Mississippi with runaway slave Jim.\n- Huck's internal conflict between social 'morality' (which commands returning runaway slaves) and his natural conscience.\n- Huck's climactic moral decision: 'All right, then, I'll go to hell'—choosing to protect Jim.",
        "points_ar": "- هروب هك من والده السكير ولقاؤه بجيم، العبد الهارب طلباً للحرية ولم شمل أسرته.\n- الصراع الأخلاقي داخل هك بين ما لقنه المجتمع من أن مساعدة العبيد خطيئة، وبين صوت فطرته الصادق.\n- قرار هك البطولي الخالد: 'حسناً، إذن سأذهب إلى الجحيم'؛ مفضلاً إنقاذ صديقه جيم على طاعة المجتمع.",
        "takeaways_en": "A sound heart will always triumph over a deformed, prejudiced conscience.",
        "takeaways_ar": "الفطرة الإنسانية السليمة والقلب النقي يعلوان دائماً فوق القوانين الظالمة والتقاليد البالية."
    },
    {
        "id": "47_The_Grapes_Of_Wrath",
        "title_en": "The Grapes of Wrath",
        "author": "John Steinbeck",
        "title_ar": "عناقيد الغضب",
        "thesis_en": "A harrowing, compassionate epic of the Joad family driven from the Dust Bowl during the Great Depression, exploring the resilience of human solidarity against capitalist exploitation.",
        "thesis_ar": "ملحمة إنسانية مؤثرة ترصد مأساة أسرة جود المهجرة من أراضيها أثناء الكساد الكبير؛ وتنتصر للتضامن الإنساني في وجه الجشع الرأسمالي.",
        "points_en": "- The Joads journey along Route 66 to California seeking promised farm work.\n- They face exploitation, starvation, police brutality, and squalid migrant camps.\n- Tom Joad embraces preacher Jim Casy's vision of universal human brotherhood.\n- Rose of Sharon's climactic, transcendent act of nursing a starving stranger.",
        "points_ar": "- رحلة عائلة جود الشاقة على طريق 66 نحو كاليفورنيا أملاً في العمل والكرامة.\n- مواجهتهم للجشع والاستغلال وعنف السلطات في مخيمات المهاجرين البائسة.\n- تحول توم جود إلى مناضل يتبنى فكرة التضامن الإنساني الشامل والعدالة الاجتماعية.\n- المشهد الختامي المؤثر لروزا وهي ترضع رجلاً عجوزاً مشرفاً على الموت جوعاً.",
        "takeaways_en": "Wherever there's a fight so hungry people can eat, I'll be there.",
        "takeaways_ar": "أينما كان هناك نضال ليأكل الجائعون ويحيا المظلومون بكرامة، سأكون هناك."
    },
    {
        "id": "48_The_Sound_And_The_Fury",
        "title_en": "The Sound and the Fury",
        "author": "William Faulkner",
        "title_ar": "الصخب والعنف",
        "thesis_en": "A towering modernist masterpiece using four radical stream-of-consciousness perspectives to chronicle the tragic moral, financial, and mental decay of the aristocratic Southern Compson family.",
        "thesis_ar": "تحفة الأدب الحداثي الأمريكي؛ تستخدم تيار الوعي عبر أربع وجهات نظر لترصد الانهيار الأخلاقي والمادي لأسرة كومبسن الأرستقراطية في الجنوب الأمريكي.",
        "points_en": "- Section 1: Benjy, the intellectually disabled brother, perceives time and memory simultaneously.\n- Section 2: Quentin, paralyzed by obsession with Southern honor and sister Caddy's purity, commits suicide at Harvard.\n- Section 3: Jason, bitter, cynical, and ruthlessly materialistic.\n- Section 4: Dilsey, the enduring Black family servant, provides the sole anchor of faith and dignity.",
        "points_ar": "- القسم الأول: بنجي، الأخ فاقد النطق والإدراك، يرى الماضي والحاضر متداخلين بحس فطري مذهل.\n- القسم الثاني: كوينتن، الطالب المسكون بشرف الأسرة وعفة أخته كادي، يقدم على الانتحار في هارفارد.\n- القسم الثالث: جيسون، الأخ الحقود والأناني المهووس بالمال والجشع.\n- القسم الرابع: ديلسي، الخادمة الإفريقية الصابرة، التي تجسد النبل الحقيقي والصمود الإنساني في وجه الانهيار.",
        "takeaways_en": "Life is a tale told by an idiot, full of sound and fury, signifying nothing—unless redeemed by enduring human endurance.",
        "takeaways_ar": "الحياة قصة يرويها أحمق، مليئة بالصخب والعنف، ولا تعني شيئاً؛ ما لم يفتدها الصبر والنبل الإنساني."
    },
    {
        "id": "49_Lolita",
        "title_en": "Lolita",
        "author": "Vladimir Nabokov",
        "title_ar": "لوليتا",
        "thesis_en": "A controversial, stylistically dazzling novel examining aesthetic obsession, manipulation, and the tragic destruction of a child's innocence by an unreliable, solipsistic narrator.",
        "thesis_ar": "عمل أدبي فائق البراعة اللغوية؛ يشرح آليات الهوس والسيطرة النفسية وتدمير براءة الطفولة على لسان راوٍ مضلل ونرجسي يحاول تبرير أفعاله.",
        "points_en": "- Humbert Humbert's predatory obsession with young girls ('nymphets') and 12-year-old Dolores Haze.\n- His manipulation and cross-country road trip abusing Dolores.\n- Dolores's escape and Humbert's final recognition that he destroyed her genuine childhood.",
        "points_ar": "- هوس همبرت همبرت المرضي بالفتيات الصغيرات ووقوع نظره على دولوريس هيز (لوليتا).\n- تلاعبه وزواجه من والدتها ثم استغلاله للطفلة في رحلة شاقة عبر أمريكا.\n- هروب لوليتا واعتراف همبرت المتأخر بأنه سلبها طفولتها الطبيعية ودمر حياتها.",
        "takeaways_en": "Dazzling prose and aesthetic rationalizations cannot disguise moral monstrosity and the irreparable harm done to innocence.",
        "takeaways_ar": "البلاغة اللغوية والتبريرات الجمالية الزائفة تعجز عن ستر الجريمة الأخلاقية والانتهاك الفادح للبراءة."
    },
    {
        "id": "50_Beloved",
        "title_en": "Beloved",
        "author": "Toni Morrison",
        "title_ar": "محبوبة",
        "thesis_en": "A Pulitzer Prize-winning masterpiece exploring the indelible psychic trauma, generational grief, and haunting legacy of American slavery.",
        "thesis_ar": "تحفة أدبية حائزة على البوليتزر؛ تستكشف الصدمة النفسية العميقة، وألم الفقد، والأشباح التي تطارد الناجين من جحيم العبودية في أمريكا.",
        "points_en": "- Sethe, a former enslaved woman, lives haunted by the ghost of the baby daughter she killed to save from slavery.\n- A mysterious young woman named Beloved arrives, embodying physical manifested trauma and guilt.\n- The community of Black women unites to exorcise the ghost and allow Sethe to claim her own selfhood.",
        "points_ar": "- سيث، امرأة نجت من العبودية، تطاردها روح ابنتها الرضيعة التي قتلتها بيديها لحمايتها من العودة للأسر.\n- ظهور شابة غامضة تدعى 'محبوبة' تجسد الصدمة النفسية والذنب المتوارث.\n- تكاتف نساء المجتمع لمساندة سيث والتخلص من شبح الماضي لتبدأ رحلة التعافي واستعادة الكرامة.",
        "takeaways_en": "Freeing yourself was one thing; claiming ownership of that freed self was another.",
        "takeaways_ar": "التحرر من القيود الجسدية شيء، وامتلاك روحك الحرة والتصالح مع ماضيك شيء آخر تماماً."
    },
    {
        "id": "51_Brave_New_World",
        "title_en": "Brave New World",
        "author": "Aldous Huxley",
        "title_ar": "عالم جديد شجاع",
        "thesis_en": "A prophetic dystopia warning against scientific totalitarianism that enslaves humanity not through pain, but through engineered pleasure, conditioning, consumerism, and the drug Soma.",
        "thesis_ar": "نبوءة كابوسية تحذر من الاستبداد العلمي الذي يستعبد البشر ليس بالألم والقمع، بل بالإلهاء والترفيه المصطنع والمخدرات الاستهلاكية.",
        "points_en": "- Hatcheries genetically clone humans into pre-conditioned caste hierarchies (Alphas to Epsilons).\n- Hypnopaedia indoctrinates consumption; Soma eliminates all emotional sorrow.\n- John the Savage rejects synthetic comfort, demanding the right to have poetry, tragedy, and suffering.\n- Mustapha Mond argues that true happiness and stability require eliminating art, religion, and freedom.",
        "points_ar": "- مصانع الأنابيب تستنسخ البشر جينياً وتوزعهم مسبقاً على طبقات محددة.\n- التلقين أثناء النوم يرسخ الطاعة والاستهلاك، ومخدر السوما يمحق القلق والوعي.\n- جون المتوحش يرفض السعادة البلاستيكية المزيفة، ويطالب بحق الإنسان في المعاناة والشعر والحرية.\n- الحاكم المستبد يقرر أن استقرار المجتمع الصناعي يقتضي محو الفن والدين والمشاعر الحقيقية.",
        "takeaways_en": "Totalitarianism achieves its most permanent victory when people learn to love their servitude through trivial amusements.",
        "takeaways_ar": "يبلغ الاستبداد ذروته وخلوده حين يتعلم الناس حب قيودهم والرضا بالتبعية عبر الملهيات السطحية."
    },
    {
        "id": "52_Dune",
        "title_en": "Dune",
        "author": "Frank Herbert",
        "title_ar": "كثيب",
        "thesis_en": "The seminal sci-fi epic examining resource exploitation on the desert planet Arrakis, political intrigue, ecology, and the grave perils of following charismatic messiahs.",
        "thesis_ar": "ملحمة الخيال العلمي الكبرى؛ تستكشف الصراع على موارد كوكب أراكيس الصحراوي، والتوازن البيئي، والتحذير من الانقياد الأعمى للمخلصين السياسيين.",
        "points_en": "- Arrakis is the sole source of Spice Melange, essential for space navigation and longevity.\n- Duke Leto Atreides is betrayed by the Harkonnens and Emperor; his son Paul flees into the desert.\n- Paul joins the Fremen, embraces desert survival, and fulfills the prophecy of Muad'Dib.\n- Herbert warns that messianic leaders unleash unstoppable fanatical holy wars.",
        "points_ar": "- كوكب أراكيس هو المصدر الوحيد في الكون لمادة التوابل الحيوية للملاحة الفضائية وتوسيع الإدراك.\n- غدر الإمبراطور وآل هاركونين بعائلة أتريدس، وفرار الشاب بول إلى الصحراء العميقة.\n- اندماج بول مع مقاتلي الفريمن وقيادتهم كزعيم ملهم ونبي منتظر (مؤدب).\n- تحذير هربرت الصارم: حينما يسلم الناس إرادتهم لقائد ملهم، تنفلت نيران الحروب المقدسة من كل عقال.",
        "takeaways_en": "Fear is the mind-killer. Beware of charismatic leaders, for their followers inevitably surrender critical judgment.",
        "takeaways_ar": "الخوف قاتل العقل؛ واحذر من القادة الملهمين، فإن أتباعهم يفقدون قدرتهم على التفكير النقدي."
    },
    {
        "id": "53_The_Old_Man_And_The_Sea",
        "title_en": "The Old Man and the Sea",
        "author": "Ernest Hemingway",
        "title_ar": "الشيخ والبحر",
        "thesis_en": "A heroic, spare novella of human endurance and dignity. An aging Cuban fisherman battles an immense marlin in the Gulf Stream, asserting that man can be destroyed, but not defeated.",
        "thesis_ar": "ملحمة قصيرة مكثفة تمجد الصمود والكرامة الإنسانية؛ يصارع فيها صياد كوبي عجوز سمكة مارلين عملاقة، مؤكداً أن الإنسان قد يفنى لكنه لا يُهزم.",
        "points_en": "- Santiago has gone 84 days without a fish; he ventures far into the Gulf Stream alone.\n- A monumental three-day physical and spiritual duel with a giant marlin.\n- He kills the fish with reverence, only for sharks to devour the carcass on the voyage home.\n- He returns with only the skeleton, yet retains undefeated spirit and the boy Manolin's devotion.",
        "points_ar": "- سانتياغو يقضي 84 يوماً في البحر دون أن يصطاد سمكة واحدة؛ فيبحر منفرداً في مياه الخليج البعيدة.\n- صراع ملحمي بطولي يمتد لثلاثة أيام مع سمكة مارلين عملاقة يربطه بها احترام عميق.\n- ينتصر عليها ويقودها إلى الشاطئ، لكن أسماك القرش تلتهم لحمها بالكامل في طريق العودة.\n- يعود بهيكل عظمي فقط، لكنه يعود بكرامة شامخة وروح لا تعرف الانكسار وتقدير تلميذه الصغير مانولين.",
        "takeaways_en": "Man is not made for defeat. A man can be destroyed but not defeated.",
        "takeaways_ar": "الإنسان لم يُخلق للهزيمة؛ يمكن تدمير الإنسان وإفناؤه جسدياً، لكن لا يمكن هزيمة إرادته."
    },
    # 9. World Classics, Epics & Latin American Masterpieces
    {
        "id": "54_Don_Quixote",
        "title_en": "Don Quixote de la Mancha",
        "author": "Miguel de Cervantes",
        "title_ar": "دون كيشوت",
        "thesis_en": "The first modern novel: a hilarious and deeply poignant satire of chivalric romance, contrasting noble idealism with harsh realism through the knight-errant and his earthy squire.",
        "thesis_ar": "أول رواية حديثة في التاريخ؛ تجمع بين السخرية اللاذعة والتراجيديا المؤثرة، وتوازن بين المثالية الحالمة والواقعية البسيطة عبر الفارس ودرويشه سانشو.",
        "points_en": "- Alonso Quixano reads chivalric books until madness drives him to roam as Don Quixote.\n- Sancho Panza serves as his pragmatic, proverb-spouting squire.\n- Tilting at windmills believed to be giants; seeing peasant girls as noble ladies.\n- Quixote recovers his sanity on his deathbed, yet Sancho mourns the loss of noble dreaming.",
        "points_ar": "- ألونسو كيخانو يغرق في قراءة روايات الفروسية حتى يفقد عقله وينطلق كفارس جوال باسم دون كيشوت.\n- مرافقة الفلاح البسيط سانشو بانزا له كخادم واقعي يفيض بالأمثال الشعبية.\n- محاربة طواحين الهواء ظناً أنها عمالقة أشرار، ورؤية الفتاة الريفية كأميرة حسناء.\n- استعادة كيشوت لعقله على فراش الموت، وحزن سانشو على انطفاء الحلم المثالي النبيل.",
        "takeaways_en": "Madness that strives to right wrongs and protect the weak is nobler than the sane cynicism that tolerates cruelty.",
        "takeaways_ar": "الجنون الذي يسعى لنجدة المظلومين ونشر الخير أنبل بكثير من العقلانية الباردة التي ترضى بالظلم والقسوة."
    },
    {
        "id": "55_One_Hundred_Years_Of_Solitude",
        "title_en": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "title_ar": "مئة عام من العزلة",
        "thesis_en": "The crowning achievement of magical realism, chronicling the rise and apocalyptic fall of the Buendía family in Macondo across seven generations cursed by incestuous solitude.",
        "thesis_ar": "درة الواقعية السحرية؛ تسرد نشأة بلدة ماكوندو وزوالها التام، وتتبع سبعة أجيال لعائلة بوينديا المحكومة بلعنة العزلة وتكرار المآسي.",
        "points_en": "- Founding of Macondo by José Arcadio Buendía and Úrsula Iguarán.\n- Colonel Aureliano Buendía fights 32 civil wars and loses them all.\n- The Banana Company massacre: state terrorism wiped from memory.\n- Deciphering Melquíades' prophecy as a hurricane sweeps Macondo from the earth.",
        "points_ar": "- تأسيس ماكوندو على يد خوسيه أركاديو بوينديا وأورسولا إيغواران وسط عالم بكر.\n- العقيد أوريليانو بوينديا يخوض 32 حرباً أهلية خاسرة ويكتشف خواء المجد العسكري.\n- مجزرة شركة الموز: إبادة آلاف العمال ومحو الحادثة بالكامل من السجلات الرسمية.\n- فك شفرة مخطوطات ملكياديس بالتزامن مع إعصار هائل يمحو البلدة إلى الأبد.",
        "takeaways_en": "Races condemned to one hundred years of solitude did not have a second opportunity on earth.",
        "takeaways_ar": "السلالات المحكومة بمئة عام من العزلة والانفصال عن محبة الآخرين لا تحظى بفرصة ثانية على هذه الأرض."
    },
    {
        "id": "56_Love_In_The_Time_Of_Cholera",
        "title_en": "Love in the Time of Cholera",
        "author": "Gabriel García Márquez",
        "title_ar": "الحب في زمن الكوليرا",
        "thesis_en": "A lush, poetic meditation on romantic devotion, patience, and aging. Florentino Ariza waits fifty-one years, nine months, and four days to reunite with his true love, Fermina Daza.",
        "thesis_ar": "قصيدة روائية عذبة تمجد الإخلاص والصبر؛ ينتظر فيها فلورنتينو أريزا إحدى وخمسين سنة وتسعة أشهر وأربعة أيام ليعود إلى حبيبته فرمينا داثا بعد ترملها.",
        "points_en": "- Young passionate love thwarted by social class; Fermina marries the respectable Dr. Juvenal Urbino.\n- Florentino pursues hundreds of affairs while keeping his heart exclusively devoted to Fermina.\n- Following Urbino's death, elderly Florentino re-courts Fermina.\n- They sail indefinitely up the river under the yellow flag of cholera, choosing eternal love.",
        "points_ar": "- حب الشباب العذري الذي تفرقه الفوارق الطبقية، وزواج فرمينا من الطبيب المرموق خوفينال أوربينو.\n- فلورنتينو يخوض مئات العلاقات العابرة بينما يظل قلبه مكرساً بالكامل لفرمينا داثا.\n- بعد وفاة الزوج، يعود فلورنتينو العجوز لخطب ود فرمينا بحكمة وتفانٍ بالغين.\n- إبحارهما معاً في النهر رافعين راية الكوليرا الصفراء ليعيشا حبهما الخالد إلى الأبد.",
        "takeaways_en": "Age and physical decay cannot diminish the enduring vitality of passionate, committed love.",
        "takeaways_ar": "التقدم في السن والوهن الجسدي يعجزان عن إطفاء جذوة الحب الصادق والوفاء العميق."
    },
    {
        "id": "57_The_Trial",
        "title_en": "The Trial",
        "author": "Franz Kafka",
        "title_ar": "المحاكمة",
        "thesis_en": "An existential nightmare of bureaucratic totalitarianism and guilt. Josef K. is arrested by an unseen, inscrutable court for an unspecified crime, struggling helplessly in a surreal labyrinth.",
        "thesis_ar": "كابوس وجودي عن البيروقراطية الخانقة والشعور بالذنب؛ يُعتقل جوزيف ك. من سلطة غامضة بتهمة مجهولة، ويغرق في متاهة قضائية عابثة لا مخرج منها.",
        "points_en": "- Josef K. is arrested on his 30th birthday without explanation.\n- The court exists in suffocating attics, run by corrupt and inaccessible officials.\n- The parable 'Before the Law': an open door intended for K. that is shut upon his death.\n- K. is executed in a quarry, dying 'like a dog.'",
        "points_ar": "- اعتقال جوزيف ك. في صباح عيد ميلاده الثلاثين دون إبداء أي أسباب.\n- محاكم سرية ومكاتب معتمة في أقبية قذرة يديرها موظفون غامضون لا سبيل لمواجهتهم.\n- أسطورة 'أمام القانون': باب مفتوح خصيصاً له وحده يُغلق عند احتضاره.\n- اقتياده لمحجر مهجور وطعنه في قلبه ليموت 'كالكلب' وسط عجز واستسلام تام.",
        "takeaways_en": "A terrifying warning of how modern dehumanizing bureaucracies render the individual utterly powerless.",
        "takeaways_ar": "تحذير مرعب من قدرة الأنظمة البيروقراطية المجردة من الإنسانية على سحق الفرد وإلغاء كرامته."
    },
    {
        "id": "58_The_Metamorphosis",
        "title_en": "The Metamorphosis",
        "author": "Franz Kafka",
        "title_ar": "التحول (الانمساخ)",
        "thesis_en": "Gregor Samsa wakes to find himself transformed into a monstrous insect. An allegorical masterpiece exploring alienation, exploitation, and the conditional nature of familial affection.",
        "thesis_ar": "يستيقظ غريغور سامسا ليجد نفسه قد تحول إلى حشرة مقززة؛ تحفة رمزية تستكشف الاغتراب والاستغلال الاقتصادي وهشاشة العواطف الأسرية المشروطة بالمنفعة.",
        "points_en": "- Gregor, sole breadwinner for his family, awakens as a giant vermin; his immediate worry is missing work.\n- His family's gradual shift from shock to disgust, neglect, and outright hostility.\n- Gregor starves himself to death, releasing his family, who immediately celebrate their new freedom.",
        "points_ar": "- غريغور، العائل الوحيد لأسرته الكسولة، يتحول لحشرة؛ ويكون قلقه الأول هو التأخر عن وظيفته البغيضة.\n- تحول مشاعر أسرته تدريجياً من الصدمة إلى الاشمئزاز والإهمال ثم العداء السافر ورشقه بالتفاح.\n- موت غريغور حزناً وجوعاً في غرفته المعتمة، وانطلاق أسرته في نزهة مشرقة احتفالاً بالخلاص منه.",
        "takeaways_en": "When a person can no longer produce or provide economic utility, society and even family often discard them.",
        "takeaways_ar": "حين يعجز الإنسان عن الإنتاج المادي وتقديم المنفعة، يتخلى عنه المجتمع والأسرة بقسوة مروعة."
    },
    {
        "id": "59_The_Castle",
        "title_en": "The Castle",
        "author": "Franz Kafka",
        "title_ar": "القلعة",
        "thesis_en": "K. arrives at a village claiming to be a land surveyor hired by the mysterious Castle, spending his life in futile, agonizing attempts to contact the inaccessible authorities.",
        "thesis_ar": "يصل ك. إلى قرية نائية مدعياً أنه مساح أراضٍ استدعته القلعة الحاكمة، ويقضي حياته في محاولات مضنية وعقيمة للتواصل مع سلطة القلعة الغامضة.",
        "points_en": "- The Castle looms unreachable above the snow-covered, hostile village.\n- Bureaucrats like Klamm communicate through cryptic, contradictory messages.\n- K. exhausts himself trying to obtain official recognition that never comes.",
        "points_ar": "- القلعة المهيبة ترتفع فوق القرية الجليدية محاطة بالغموض والمنع المطلق.\n- البيروقراطيون يرسلون إشارات متناقضة ورسائل مبهمة تزيد من ضياع ك. وتيهه.\n- استنزاف ك. لطاقته في سبيل الحصول على اعتراف رسمي بشرعية وجوده دون جدوى.",
        "takeaways_en": "The ultimate allegory of human striving for transcendent meaning in a world where authority remains permanently silent.",
        "takeaways_ar": "تجسيد لسعي الإنسان البائس لنيل اليقين والمعنى في عالم تصمت فيه القوى العليا صمتاً أبدياً."
    },
    {
        "id": "60_The_Odyssey",
        "title_en": "The Odyssey",
        "author": "Homer",
        "title_ar": "الأوديسة",
        "thesis_en": "The foundational epic of Western literature: Odysseus's ten-year perilous voyage home to Ithaca after the Trojan War, demonstrating cunning, endurance, and the sanctity of home and family.",
        "thesis_ar": "الملحمة التأسيسية للأدب الإنساني؛ تروي رحلة عودة البطل أوديسيوس الشاقة لعشر سنوات إلى وطنه إيثاكا بعد حرب طروادة، مجسدة الدهاء والصبر والوفاء.",
        "points_en": "- Odysseus faces mythical monsters (Polyphemus the Cyclops, Circe, the Sirens, Scylla and Charybdis).\n- Penelope's steadfast fidelity weaving and unweaving her burial shroud to fend off suitors.\n- Telemachus's journey into manhood.\n- Odysseus returns in disguise, slaughters the suitors, and reclaims his kingdom and wife.",
        "points_ar": "- مواجهة أوديسيوس للأهوال والكائنات الأسطورية (السيكلوب، الساحرة سيرسي، وحوش البحر وسيرين). \n- وفاء بينيلوبي الأسطوري في انتظار زوجها وخداعها للخطاب بفك ثوب الغزل ليلاً.\n- نضج تليماخوس وبحثه عن أبيه المحارب.\n- عودة أوديسيوس متنكراً في زي متسول، وقتله للخطاب المعتدين، واستعادة مملكته وأسرته.",
        "takeaways_en": "Endurance and intellect (metis) are far greater weapons than raw physical strength.",
        "takeaways_ar": "الصبر والدهاء والحكمة أسلحة أعتى وأبقى من القوة العضلية والبطش العسكري."
    },
    {
        "id": "61_The_Iliad",
        "title_en": "The Iliad",
        "author": "Homer",
        "title_ar": "الإلياذة",
        "thesis_en": "The epic poem of the wrath of Achilles during the final weeks of the Trojan War, exploring honor, the brutality of combat, mortality, and the shared tragedy of humanity.",
        "thesis_ar": "ملحمة غضب البطل أخيل في الأسابيع الأخيرة من حصار طروادة؛ تستكشف الشرف، وأهوال الحرب، وحتمية الموت، والمأساة الإنسانية المشتركة.",
        "points_en": "- Achilles withdraws from battle following a humiliating dispute with Agamemnon.\n- Hector leads the Trojans to the brink of burning the Greek fleet.\n- The death of Patroclus re-ignites Achilles' monstrous rage; he slays Hector and desecrates his corpse.\n- King Priam begs Achilles for Hector's body; they weep together over the shared grief of mortal life.",
        "points_ar": "- اعتزال أخيل القتال غاضباً بعد إهانة أجاممنون له، مما يقود الإغريق لحافة الهزيمة.\n- هيكتور بطل طروادة يقود جيشه للانتصار دفاعاً عن وطنه وأسرته.\n- مقتل باتروكلوس صديق أخيل يشعل غضب الأخير الوحشي، فيعود وينتقم بقتل هيكتور وسحل جثته.\n- ذهاب الملك الشيخ بريام لخيمة أخيل راجياً استعادة جثمان ابنه، وبكاؤهما معاً على مأساة الفناء الإنساني.",
        "takeaways_en": "War brings only grief to victors and vanquished alike; empathy across enmity is humanity's highest glory.",
        "takeaways_ar": "الحرب لا تجلب سوى الويلات للغالب والمغلوب؛ والتعاطف مع الخصم في لحظات الألم هو قمة النبل الإنساني."
    },
    {
        "id": "62_The_Divine_Comedy",
        "title_en": "The Divine Comedy (Inferno, Purgatorio, Paradiso)",
        "author": "Dante Alighieri",
        "title_ar": "الكوميديا الإلهية (الجحيم، المطهر، الفردوس)",
        "thesis_en": "An allegorical poetic tour through Hell, Purgatory, and Heaven guided by Virgil and Beatrice, charting the soul's ascent from sin through moral purification to divine contemplation.",
        "thesis_ar": "ملحمة شعرية ورمزية تأخذ القارئ في رحلة عبر الجحيم والمطهر والفردوس بقيادة فرجيل وبياتريس؛ ترسم ارتقاء الروح من دنس الخطيئة إلى أنوار المعرفة والفيض الإلهي.",
        "points_en": "- Inferno: Dante traverses the nine circles of Hell, observing the precise poetic justice (contrapasso) of sins.\n- Purgatorio: Climbing the mountain of purification where repentant souls cleanse their vices.\n- Paradiso: Guided by Beatrice through the celestial spheres, culminating in the vision of Divine Light.",
        "points_ar": "- الجحيم (Inferno): تسعة مستويات تعاقب الخطايا بعدالة شعرية مذهلة تعكس طبيعة كل ذنب.\n- المطهر (Purgatorio): صعود جبل التطهير حيث تتخلص الأرواح النادمة من أدران الكبرياء والحسد والغضب.\n- الفردوس (Paradiso): الصعود عبر الأفلاك السماوية بصحبة بياتريس، وصولاً إلى معاينة النور الإلهي الخالص.",
        "takeaways_en": "Love moves the sun and the other stars. Moral redemption requires confronting the horror of sin and striving toward truth.",
        "takeaways_ar": "المحبة الإلهية هي التي تحرك الشمس وسائر النجوم؛ وخلاص الإنسان يبدأ بالاعتراف بضعفه والسعي نحو النور."
    },
    {
        "id": "63_The_Magic_Mountain",
        "title_en": "The Magic Mountain",
        "author": "Thomas Mann",
        "title_ar": "الجبل السحري",
        "thesis_en": "A monumental philosophical novel set in a tuberculosis sanatorium in the Swiss Alps, serving as an intellectual microcosm of European civilization on the eve of World War I.",
        "thesis_ar": "رواية فلسفية كبرى تدور في مصحة لمرضى السل في جبال الألب السويسرية؛ تجسد صراع التيارات الفكرية والسياسية في أوروبا عشية الحرب العالمية الأولى.",
        "points_en": "- Hans Castorp visits his cousin for three weeks and stays for seven years as a patient.\n- The great ideological debates: Settembrini (Humanism, Enlightenment, Democracy) vs. Naphta (Totalitarianism, Dogma, Nihilism).\n- The sensual allure of Clavdia Chauchat and the vitalism of Mynheer Peeperkorn.\n- The Thunderclap: World War I erupts, violently plunging Castorp back into the mud and slaughter of reality.",
        "points_ar": "- الشاب هانز كاستورب يزور قريبه لثلاثة أسابيع فيعلق في المصحة سبع سنوات كاملة.\n- المناظرات الفكرية العميقة بين سيتيمبريني (التنوير والديمقراطية) ونافتا (الاستبداد والعدمية والتعصب).\n- سحر الوقت وإدراك الزمن في بيئة معزولة عن العالم الخارجي.\n- الصاعقة: اندلاع الحرب العالمية الأولى التي تعصف بعالم المصحة وتلقي بكاستورب في خنادق القتال.",
        "takeaways_en": "For the sake of goodness and love, man shall let death have no sovereignty over his thoughts.",
        "takeaways_ar": "من أجل الخير والمحبة، يجب ألا يدع الإنسان للموت والعدمية سيادة على أفكاره وروحه."
    },
    {
        "id": "64_One_Thousand_And_One_Nights",
        "title_en": "One Thousand and One Nights (The Arabian Nights)",
        "author": "Traditional Middle Eastern Folklore",
        "title_ar": "ألف ليلة وليلة",
        "thesis_en": "The immortal collection of Middle Eastern, Persian, and Indian tales framed by Scheherazade weaving stories night after night to delay her execution by King Shahryar, using narrative to heal madness and tyranny.",
        "thesis_ar": "تحفة الأدب الشرقي والعالمي؛ حيث تروي شهرزاد حكاياتها ليلة بعد ليلة للملك شهريار لدرء سيف الإعدام، مستخدمة قوة السرد والحكمة لشفاء روحه من جنون الاستبداد والغدر.",
        "points_en": "- The frame story: Shahryar's murderous mistrust cured through Scheherazade's narrative intelligence.\n- Famous stories: Sinbad the Sailor, Aladdin and the Wonderful Lamp, Ali Baba and the Forty Thieves.\n- Masterclass in nested storytelling, suspense, moral consequences, and human destiny.",
        "points_ar": "- القصة الإطارية: حكمة شهرزاد وشجاعتها في ترويض بطش شهريار وتحويل انتقامه إلى حب ورحمة.\n- أشهر القصص: رحلات السندباد البحري، علاء الدين والمصباح السحري، علي بابا والأربعون حرامياً.\n- مدرسة أدبية رائدة في تقنية القص المتداخل، والتشويق، والعدالة الأخلاقية، وتقلبات الأقدار.",
        "takeaways_en": "Stories have the miraculous power to civilize violence, bridge wounds, and save human lives.",
        "takeaways_ar": "الأدب والحكاية يملكان قوة سحرية لترويض العنف، ومداواة الجراح، وحماية الإنسانية من الهلاك."
    },
    {
        "id": "65_Middlemarch",
        "title_en": "Middlemarch: A Study of Provincial Life",
        "author": "George Eliot",
        "title_ar": "ميدلمارش: دراسة للحياة الريفية",
        "thesis_en": "A panoramic Victorian masterpiece examining the complex interplay of idealistic aspirations, flawed marriages, and social reform in a provincial English town.",
        "thesis_ar": "تحفة الأدب الفيكتوري الواقعي؛ تشرح تعقيدات الزواج، والطموح الإنساني، والإصلاح الاجتماعي في بلدة إنجليزية ريفية تتغير مع فجر الحداثة.",
        "points_en": "- Dorothea Brooke's idealistic, tragic marriage to the sterile scholar Edward Casaubon.\n- Tertius Lydgate's ambitious medical career derailed by marriage to materialistic Rosamond Vincy.\n- Fred Vincy and Mary Garth's wholesome, hard-earned domestic contentment.",
        "points_ar": "- زواج دوروثيا بروك المثالي المتسرع من الباحث العقيم إدوارد كازوبون وخيبة أملها المريرة.\n- طموح الطبيب الشاب ليدغيت العلمي الذي يجهضه زواجه من روزاموند المهووسة بالمظاهر المادية.\n- قصة حب فريد فينزي وماري غارث القائمة على الكفاح والصدق والبساطة الريفية.",
        "takeaways_en": "The growing good of the world is partly dependent on unhistoric acts of ordinary people who lived faithfully a hidden life.",
        "takeaways_ar": "إن نمو الخير في هذا العالم يعتمد في جزء كبير منه على أعمال خفية لأناس بسطاء عاشوا بشرف ودُفنوا في قبور مجهولة."
    },
    {
        "id": "66_Journey_To_The_End_Of_The_Night",
        "title_en": "Journey to the End of the Night (Voyage au bout de la nuit)",
        "author": "Louis-Ferdinand Céline",
        "title_ar": "سفر إلى آخر الليل",
        "thesis_en": "A fiercely cynical, groundbreaking anti-war novel exposing the cowardice, colonialism, exploitation, and misery of human existence through the misanthropic eyes of Ferdinand Bardamu.",
        "thesis_ar": "رواية صادمة وفذة تفضح أهوال الحرب العالمية الأولى، والوحشية الاستعمارية، والفقر المدقع، عبر عيون الطبيب الساخر والعدمي فرديناند باردامو.",
        "points_en": "- WWI trenches: war revealed as organized, cowardly slaughter of ordinary men.\n- Colonial Africa: greed, sickness, and absurdity of the French empire.\n- Industrial America: soul-crushing alienation of the Ford assembly line.\n- Paris slums: Bardamu practicing medicine among the impoverished, witnessing human cruelty.",
        "points_ar": "- خنادق الحرب العالمية الأولى: الحرب كمجزرة منظمة وجبانة يساق إليها البسطاء للموت عبثاً.\n- أفريقيا الاستعمارية: جشع ومرض وتفاهة الإمبراطورية الاستعمارية الأوروبية.\n- أمريكا الصناعية: سحق الروح الإنسانية في طوابير مصانع فورد والتغريب الرأسمالي.\n- أزقة باريس الفقيرة: ممارسة الطب بين المعدمين واكتشاف القسوة والخواء النفسي البشري.",
        "takeaways_en": "An uncompromising, raw exposure of human depravity and institutional hypocrisy.",
        "takeaways_ar": "مرآة قاسية تفضح زيف الشعارات الرنانة وتكشف بؤس الإنسان حين تحكمه الأنانية والخوف."
    }
]

def main():
    print(f"==================================================")
    print(f" GENERATING COMPLETE LIBRARY SUMMARIES (66 TITLES) ")
    print(f"==================================================")
    
    count = 0
    for item in DATA:
        file_id = item['id']
        
        # English Markdown
        en_md = f"""# {item['title_en']}
**Author:** {item['author']}

## Executive Summary & Core Premise
{item['thesis_en'].strip()}

## Key Structural Breakdown & Analysis
{item['points_en'].strip()}

## Actionable Takeaways & Lessons
{item['takeaways_en'].strip()}
"""
        with open(os.path.join(EN_DIR, f"{file_id}.md"), "w", encoding="utf-8") as f:
            f.write(en_md.strip() + "\n")
            
        # Arabic Markdown
        ar_md = f"""# ملخص كتاب: {item['title_ar']}
**المؤلف:** {item['author']}

## الفكرة الجوهرية والملخص التنفيذي
{item['thesis_ar'].strip()}

## التحليل البنيوي والمحاور الرئيسية
{item['points_ar'].strip()}

## الدروس المستفادة والخلاصة العملية
{item['takeaways_ar'].strip()}
"""
        with open(os.path.join(AR_DIR, f"{file_id}_Arabic.md"), "w", encoding="utf-8") as f:
            f.write(ar_md.strip() + "\n")
            
        count += 1
        print(f"  [✓] {count:02d}/66: {file_id}")

    print(f"\n[✓] Finished generating {count} complete bilingual executive summaries!")
    print(f"    - English: {EN_DIR} ({len(os.listdir(EN_DIR))} files)")
    print(f"    - Arabic:  {AR_DIR} ({len(os.listdir(AR_DIR))} files)")

if __name__ == "__main__":
    main()
