"""
Universal Feature Phone Book Summaries Generator
Creates high-density, literary-grade executive summaries for the top books in both English and Arabic.
Structured for readability on small screens or text readers.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

SUMMARIES_DIR = r"E:\nokia\summaries"
EN_DIR = os.path.join(SUMMARIES_DIR, "english")
AR_DIR = os.path.join(SUMMARIES_DIR, "arabic")

os.makedirs(EN_DIR, exist_ok=True)
os.makedirs(AR_DIR, exist_ok=True)

SUMMARIES = [
    {
        "id": "01_Atomic_Habits",
        "title_en": "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones",
        "author": "James Clear (2018)",
        "title_ar": "العادات الذرية: طريقة سهلة ومثبتة لبناء عادات جيدة والتخلص من السيئة",
        "content_en": """# Atomic Habits by James Clear

## Core Thesis
Small, incremental changes of 1% every day compound into massive transformations over time. Habits are the compound interest of self-improvement. Focus not on setting goals, but on designing systems and identity-based habits.

## The Four Laws of Behavior Change

### How to Create a Good Habit
1. **Make it Obvious (Cue)**: Design your environment. Use implementation intentions ("I will [BEHAVIOR] at [TIME] in [LOCATION]") and habit stacking ("After [CURRENT HABIT], I will [NEW HABIT]").
2. **Make it Attractive (Craving)**: Pair an action you want to do with an action you need to do (Temptation Bundling). Join a culture where your desired behavior is normal.
3. **Make it Easy (Response)**: Reduce friction. Use the 2-Minute Rule: scale any new habit down to two minutes or less when starting.
4. **Make it Satisfying (Reward)**: Immediate rewards reinforce behavior. Track habits visibly (never break the chain twice).

### How to Break a Bad Habit (The Inversion)
1. **Make it Invisible**: Remove environmental cues.
2. **Make it Unattractive**: Reframe your mindset to highlight the negatives.
3. **Make it Difficult**: Increase friction; create commitment devices.
4. **Make it Unsatisfying**: Introduce an accountability partner or contract.

## Key Takeaway
You do not rise to the level of your goals; you fall to the level of your systems. True behavior change is identity change.
""",
        "content_ar": """# ملخص كتاب العادات الذرية - جيمس كلير

## الفكرة الجوهرية
التغييرات الصغيرة المتراكمة بنسبة 1% يومياً تحقق نتائج جذرية على المدى الطويل. العادات هي الفائدة المركبة لتطوير الذات. لا تركز على تحديد الأهداف، بل ركز على بناء الأنظمة وتغيير الهوية الذاتية.

## القوانين الأربعة لتغيير السلوك

### كيفية اكتساب عادة حسنة
1. **اجعلها واضحة (المحفز)**: هيئ بيئتك المحيطة. استخدم خطة التنفيذ: "سأفعل [السلوك] في [الوقت] في [المكان]". واعتمد تكديس العادات: "بعد [عادتي الحالية]، سأفعل [العادة الجديدة]".
2. **اجعلها جذابة (الرغبة)**: ادمج ما ترغب في فعله بما يجب عليك فعله (حزم الإغراء). أحط نفسك ببيئة يكون فيها السلوك المرغوب هو الطبيعي.
3. **اجعلها سهلة (الاستجابة)**: قلل العوائق. طبق قاعدة الدقيقتين: ابدأ أي عادة جديدة في صورة تستغرق دقيقتين أو أقل فقط.
4. **اجعلها مجزية (المكافأة)**: المكافآت الفورية ترسخ السلوك. استخدم سجل تتبع العادات (إياك أن تنقطع مرتين متتاليتين).

### كيفية التخلص من عادة سيئة (معكوس القوانين)
1. **اجعلها غير مرئية**: أبعد المحفزات من بيئتك.
2. **اجعلها غير جذابة**: ركز على التبعات السلبية وتكاليف العادة السيئة.
3. **اجعلها صعبة**: زد من العقبات والحواجز التي تفصلك عن ممارستها.
4. **اجعلها غير مرضية**: استخدم شريكاً للمساءلة أو عقداً يفرض عليك كلفة فورية.

## الخلاصة العملية
أنت لا ترتقي إلى مستوى أهدافك، بل تهبط إلى مستوى أنظمتك. التغيير الحقيقي للسلوك هو تغيير لهويتك وإيمانك بنفسك.
"""
    },
    {
        "id": "02_The_Psychology_Of_Money",
        "title_en": "The Psychology of Money: Timeless Lessons on Wealth, Greed, and Happiness",
        "author": "Morgan Housel (2020)",
        "title_ar": "سيكولوجية المال: دروس خالدة في الثروة والجشع والسعادة",
        "content_en": """# The Psychology of Money by Morgan Housel

## Core Thesis
Financial success is not about intellect, math, or complex algorithms; it is about behavior. How you behave is far more important than how smart you are.

## Essential Insights & Principles

1. **No One's Crazy**: People make financial decisions based on their unique life experiences, childhood, and era. What seems irrational to you makes perfect sense to them.
2. **Compounding & Time**: Over 99% of Warren Buffett's wealth was accumulated after his 50th birthday. The secret isn't genius returns; it is endurance and longevity over decades.
3. **Getting Wealthy vs. Staying Wealthy**: Getting wealthy requires taking risks, optimism, and hustle. Staying wealthy requires the opposite: paranoia, humility, and frugality.
4. **Tails Drive Everything**: In business and investing, a tiny percentage of events (outliers) account for almost all long-term returns. It's okay to be wrong half the time as long as your winners pay off massively.
5. **Freedom (The True Dividend of Wealth)**: The highest form of wealth is the ability to wake up every morning and say: "I can do whatever I want today."
6. **Room for Error**: Plan for things not going according to plan. Having cash margin of safety prevents you from being forced to sell during crashes.

## Key Takeaway
Wealth is what you do not see: the cars not purchased, the watches not worn, the first-class tickets declined. Wealth is financial options and freedom.
""",
        "content_ar": """# ملخص كتاب سيكولوجية المال - مورغان هاوسل

## الفكرة الجوهرية
النجاح المالي ليس علماً حسابياً معقداً أو ذكاءً أكاديمياً، بل هو علم سلوكي ونفسي. طريقة تصرفك وعاداتك اليومية أكثر أهمية بكثير من مقدار ذكائك.

## أبرز المبادئ والقوانين الخالدة

1. **لا أحد مجنون**: كل شخص يتخذ قراراته المالية بناءً على تجاربه الشخصية، طفولته، والظروف الاقتصادية التي نشأ فيها. ما يبدو لك مخاطرة غير مبررة، يبدو منطقياً تماماً لشخص آخر.
2. **سحر الفائدة المركبة والزمن**: أكثر من 99% من ثروة وارن بافيت تحققت بعد تجاوزه سن الخمسين. السر ليس عوائد خارقة كل شهر، بل الاستمرار على مدى عقود طويلة دون توقف.
3. **صنع الثروة مقابل الحفاظ عليها**: بناء الثروة يتطلب التفاؤل والإقدام والمخاطرة؛ بينما الحفاظ عليها يتطلب النقيض: الحذر، والتواضع، وإدراك أن الحظ قد يتغير.
4. **الأحداث النادرة تقود النتائج (قانون الذيل)**: في الاستثمار والأعمال، نسبة ضئيلة جداً من القرارات الناجحة تصنع الغالبية العظمى من الأرباح الإجمالية. يمكنك أن تخطئ في نصف قراراتك وتظل ثرياً.
5. **الحرية هي القيمة الحقيقية للمال**: أعلى درجات الثروة هي أن تستيقظ كل صباح وتقول: "أستطيع أن أفعل ما أريد، مع من أريد، في الوقت الذي أريد".
6. **هامش الأمان والخطأ**: خطط دائماً لاحتمال ألا تسير الأمور وفق الخطة. الادخار يمنحك حصانة ضد الصدمات غير المتوقعة ويحميك من البيع الإجباري أثناء الأزمات.

## الخلاصة العملية
الثروة الحقيقية هي ما لا يراه الناس: السيارات التي لم تُشترَ، والساعات الفاخرة التي لم تُرتدَ. الثروة هي راحة البال وحرية الاختيار.
"""
    },
    {
        "id": "03_The_48_Laws_Of_Power",
        "title_en": "The 48 Laws of Power",
        "author": "Robert Greene (1998)",
        "title_ar": "قواعد السطوة الـ48 - روبرت جرين",
        "content_en": """# The 48 Laws of Power by Robert Greene

## Core Thesis
Power is a timeless, amoral game governed by strategic acumen, emotional self-control, and psychological perception. Master power dynamics, or be mastered by those who do.

## Key Foundational Laws

1. **Law 1: Never Outshine the Master**: Always make those above you feel comfortably superior. Disguise your brilliance so they do not feel insecure.
2. **Law 3: Conceal Your Intentions**: Keep people off-balance and in the dark by never revealing the purpose behind your actions.
3. **Law 4: Always Say Less than Necessary**: The more you speak, the more common you appear, and the higher the risk of saying something foolish.
4. **Law 9: Win Through Your Actions, Never Through Argument**: Demonstration, not debate, changes minds without stirring resentment.
5. **Law 15: Crush Your Enemy Totally**: If one ember is left alight, a fire will eventually break out. Extinguish threats completely.
6. **Law 28: Enter Action with Boldness**: Hesitation is fatal. Timidity creates obstacles; boldness eliminates them.
7. **Law 33: Discover Each Man's Thumbscrew**: Everyone has a weakness—an insecurity, an uncontrollable desire, or a secret vanity. Find it and command it.
8. **Law 48: Assume Formlessness**: By having no visible shape or predictable plan, you become impossible to attack or counter.

## Philosophical Framework
Power requires mastering your emotions. Anger, vanity, and impatience are strategic weaknesses that enemies exploit.
""",
        "content_ar": """# ملخص كتاب قواعد السطوة الـ48 - روبرت جرين

## الفكرة الجوهرية
السطوة لعبة أزلية تحكم العلاقات البشرية، تعتمد على الذكاء الاستراتيجي، والتحكم المطلق في العواطف، ودراسة سيكولوجيا الآخرين. إما أن تفهم قواعد القوة وتتقنها، أو تقع فريسة لمن يجيدونها.

## أبرز القواعد المحورية

1. **القاعدة 1: لا تشرق أبداً أكثر من سيدك**: اجعل من هم فوقك يشعرون دائماً بتفوقهم وراحتهم. احرص على ألا تثير غيرتهم أو قلقهم بمواهبك.
2. **القاعدة 3: اكتم نواياك**: لا تكشف عن الهدف الحقيقي وراء أفعالك، واجعل الآخرين في حيرة دائمة حتى يفوت أوان التدخل.
3. **القاعدة 4: قل دائماً أقل مما يلزم**: كلما زاد كلامك، بدوت عادياً وأكثر عرضة للوقوع في الأخطاء والزلات.
4. **القاعدة 9: انتصر بأفعالك لا بالمجادلة**: البرهان العملي يغير القناعات دون أن يترك ضغينة أو مشاعر انتقام كما تفعل المجادلة الكلامية.
5. **القاعدة 15: اسحق عدوك سحقاً تاماً**: ترك جمرة واحدة متقدة قد يشعل حريقاً مدمراً لاحقاً. يجب حسم النزاعات جذرياً.
6. **القاعدة 28: ادخل الميدان بجرأة**: التردد يولد العقبات ويكشف الضعف، بينما الجرأة تفرض الهيبة وتفتح الأبواب.
7. **القاعدة 33: اكتشف نقطة ضعف كل إنسان**: لكل شخص مفتاح خفي: إما رغبة ملحة، أو عقدة نقص، أو غرور شخصي؛ معرفتها تمنحك السيطرة.
8. **القاعدة 48: كن بلا شكل محدد**: لا تجعل خططك وتحركاتك متوقعة؛ المرونة المطلقة تجعل استهدافك مستحيلاً.

## الخلاصة الفلسفية
السطوة تتطلب ضبطاً فولاذياً للنفس؛ الغضب والتسرع والغرور هي ثغراتك التي يستغلها الخصوم ضدك.
"""
    },
    {
        "id": "04_The_Pragmatic_Programmer",
        "title_en": "The Pragmatic Programmer: Your Journey to Mastery (20th Anniversary Edition)",
        "author": "David Thomas & Andrew Hunt (2019)",
        "title_ar": "المبرمج البراغماتي: رحلتك نحو الإتقان - النسخة العشرينية",
        "content_en": """# The Pragmatic Programmer by David Thomas & Andrew Hunt

## Core Philosophy
Pragmatism is about taking responsibility for your craft, continuously learning, writing adaptable and maintainable code, and solving real human and business problems rather than dogmatically worshipping tools.

## Core Tenets & Best Practices

1. **Care About Your Craft**: There is no point in writing software unless you care about doing it well.
2. **Think! (About Your Work)**: Never code on autopilot. Constantly critique and evaluate what you are doing.
3. **Don't Live with Broken Windows**: Fix bad designs, wrong decisions, and poor code immediately. Technical debt creates negligence and decays systems.
4. **DRY (Don't Repeat Yourself)**: Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
5. **Orthogonality**: Design components that are independent and self-contained. Changes in one area should not cause ripples elsewhere.
6. **Tracer Bullets & Prototypes**: Build thin, end-to-end working slices to validate architecture and get rapid feedback before scaling.
7. **Crash Early & Assertive Programming**: Write code that fails fast and loud when invariants are violated, preventing silent corruption.
8. **Refactoring as a Habit**: Refactor constantly as you learn more about the problem domain—treat code like a living garden that requires continuous weeding.

## Career Rule
Invest regularly in your knowledge portfolio. Learn at least one new programming language every year, read technical books, and remain insatiably curious.
""",
        "content_ar": """# ملخص كتاب المبرمج البراغماتي - ديفيد توماس وأندرو هانت

## الفلسفة الجوهرية
البراغماتية تعني تحمّل المسؤولية الكاملة عن عملك، والتعلم المستمر، وكتابة كود مرن وقابل للصيانة، والتركيز على حل المشكلات الحقيقية بدلاً من التعصب الأعمى للتقنيات والأدوات.

## أبرز المبادئ والقواعد الهندسية

1. **اهتم بصنعتك (Care About Your Craft)**: لا جدوى من كتابة البرمجيات إذا لم تكن شغوفاً ومخلصاً لجودتها ودقتها.
2. **فكر باستمرار (Think About Your Work)**: لا تكتب الكود بوضع الطيار الآلي؛ راجع كل قرار تصميمي واسأل نفسك عن جدواه.
3. **لا تترك نوافذ مكسورة (No Broken Windows)**: أصلح الأخطاء والتصاميم الرديئة فور اكتشافها؛ فالإهمال البسيط يقود لانهيار جودة النظام بالكامل.
4. **مبدأ DRY (لا تكرر نفسك)**: يجب أن يمتلك كل مفهوم أو قاعدة بيانات أو سلوك تمثيلاً واحداً موثوقاً وغير مكرر داخل الشيفرة.
5. **التعامدية والاستقلالية (Orthogonality)**: صمم وحدات برمجية مستقلة تماماً بحيث لا تؤدي التغييرات في وحدة ما إلى أعطال جانبية في وحدات أخرى.
6. **الرصاصات التتبعية (Tracer Bullets)**: ابنِ نماذج أولية متصلة من البداية إلى النهاية للتحقق من سلامة البنية المعمارية وتلقي الملاحظات مبكراً.
7. **الانهيار المبكر (Crash Early)**: اجعل الكود يفشل بوضوح وسرعة عند حدوث خلل، لتجنب استمرار النظام في حالة مشوهة وتلويث البيانات.
8. **إعادة الهيكلة المستمرة (Refactoring)**: الكود مثل الحديقة؛ يحتاج إلى تقليم مستمر وإعادة تنظيم مع تطور فهمك للمشكلة البرمجية.

## نصيحة المسار المهني
استثمر بانتظام في محفظتك المعرفية: تعلم لغة برمجة جديدة كل عام، واقرأ كتباً تقنية عميقة، وحافظ على شغفك بالاستكشاف.
"""
    },
    {
        "id": "05_1984_George_Orwell",
        "title_en": "Nineteen Eighty-Four",
        "author": "George Orwell (1949)",
        "title_ar": "١٩٨٤ - جورج أورويل",
        "content_en": """# 1984 by George Orwell

## Core Premise & World-Building
Set in the superstate of Oceania, a dystopian society dominated by the omnipresent Party and its mythical leader, Big Brother. The Party exercises total surveillance, rewrites history, controls language, and eradicates individual identity.

## Critical Concepts
- **Newspeak**: A manufactured language designed to eliminate the capacity for rebellious or independent thought by reducing vocabulary.
- **Doublethink**: The psychological ability to hold two contradictory beliefs in one's mind simultaneously, and accept both of them.
- **Thoughtcrime**: Having unorthodox thoughts or questioning Party orthodoxy, investigated by the Thought Police.
- **Memory Hole**: Disposal chutes where inconvenient historical records are incinerated and rewritten.

## The Tragic Arc of Winston Smith
Winston Smith, a minor bureaucrat at the Ministry of Truth, rebels by buying an illicit diary, falling in love with Julia, and seeking the underground Brotherhood. He is betrayed, imprisoned in the Ministry of Love, and subjected to psychological and physical torture in Room 101. Ultimately, his spirit is broken: he betrays Julia, abandons independent thought, and finally "loves Big Brother."

## Ultimate Warning
Totalitarianism does not merely seek obedience; it demands complete surrender of truth, memory, and love.
""",
        "content_ar": """# ملخص رواية ١٩٨٤ - جورج أورويل

## الإطار العام وعالم الرواية
تدور الرواية في دولة أوشينيا الشمولية، الخاضعة للهيمنة المطلقة للحزب ولشخصية الأخ الأكبر الرمزية. يمارس الحزب رقابة كلية على المواطنين، ويعيد كتابة التاريخ، ويتحكم في اللغة، ويمحو أي أثر للفردية والحرية.

## أهم المفاهيم الفلسفية والسياسية
- **اللغة الجديدة (Newspeak)**: لغة مبتكرة تهدف إلى تقليص المفردات للقضاء على إمكانية صياغة أفكار معارضة أو حرة.
- **التفكير المزدوج (Doublethink)**: القدرة النفسية على تصديق فكرتين متناقضتين في الوقت ذاته والقبول التام بهما.
- **جريمة الفكر (Thoughtcrime)**: الشك في قرارات الحزب أو التفكير المستقل، وهي الجريمة الأخطر التي تطاردها شرطة الفكر.
- **ثقب الذاكرة (Memory Hole)**: فتحات حرق الوثائق التاريخية لتعديل الماضي وفق مصالح الحاضر.

## المسار الدرامي لوينستون سميث
وينستون، موظف في وزارة الحقيقة، يبدأ تمرده بكتابة مذكرات سرية، والارتباط عاطفياً بجوليا، ومحاولة الانضمام إلى المقاومة. يتعرض للخيانة ويُعتقل في وزارة الحب، حيث يخضع للتعذيب الممنهج في الغرفة 101. تنتهي الرواية بكسر إرادته وتجريده من إنسانيته؛ حتى يعترف بخيانته لجوليا ويعلن استسلامه التام وحبه للأخ الأكبر.

## الرسالة التحذيرية
الأنظمة الاستبدادية لا تكتفي بفرض الطاعة الخارجية، بل تسعى إلى السيطرة على الوعي الباطني والحقيقة ذاتها وتدمير المشاعر الإنسانية.
"""
    },
    {
        "id": "06_Crime_And_Punishment",
        "title_en": "Crime and Punishment",
        "author": "Fyodor Dostoevsky (1866)",
        "title_ar": "الجريمة والعقاب - فيودور دوستويفسكي",
        "content_en": """# Crime and Punishment by Fyodor Dostoevsky

## Core Thesis
Intellectual rationalization of evil leads to psychological disintegration. Morality is not a theoretical construct that superior minds can bypass; true redemption comes through suffering, humility, and love.

## The Theory of the Extraordinary Man
Rodion Raskolnikov, an impoverished former student in Saint Petersburg, believes humanity is divided into the "ordinary" (who submit to laws) and the "extraordinary" (Napoleons who have the moral right to overstep laws for a greater good). To test his theory and resolve his poverty, he murders an unscrupulous pawnbroker and her sister.

## The Internal Inferno & Resolution
Immediately following the crime, Raskolnikov is gripped not by triumph, but by paranoia, fever, and profound alienation from humanity. The narrative is a psychological duel between Raskolnikov and Porfiry Petrovich, the shrewd magistrate. 

His moral salvation begins through Sonya Marmeladova, a saintly young woman forced into prostitution to feed her starving family. Guided by Sonya's Christian humility and faith, Raskolnikov confesses, is exiled to Siberia, and embarks on a painful path toward spiritual resurrection.

## Master Theme
Human nature cannot tolerate separation from the moral universe. Rationalist nihilism collapses before the reality of the human soul.
""",
        "content_ar": """# ملخص رواية الجريمة والعقاب - فيودور دوستويفسكي

## الفكرة الجوهرية
محاولة تبرير الشر فكرياً تقود إلى الانهيار النفسي والعزلة التامة. الأخلاق ليست نظرية رياضية يمكن للعباقرة تجاوزها؛ والخلاص الروحي الحقيقي لا يتحقق إلا بالاعتراف والندم وتحمل المعاناة.

## نظرية الإنسان الخارق
يعيش روديون راسكولنيكوف، الطالب الجامعي المعدم في سانت بطرسبرغ، صراعاً فكرياً يقسم فيه البشر إلى صنفين: عاديين خاضعين للقوانين، واستثنائيين (مثل نابليون) يملكون الحق الأخلاقي في تجاوز القوانين لصالح الإنسانية. ولاختبار نظريته، يقتل عجوزاً مرابية وشقيقتها البريئة.

## العذاب النفسي والصراع الداخلي
عقب الجريمة مباشرة، لا يشعر راسكولنيكوف بالعظمة، بل يجتاحه الرعب والحمى والانفصال التام عن المجتمع. تتحول الرواية إلى مواجهة نفسية عبقرية بينه وبين المحقق الذكي بورفيري بيتروفيتش.

يبدأ خلاصه الروحي عبر علاقته بسونيا مارميلادوفا، الفتاة التقية التي دفعتها الحاجة للعمل لإنقاذ أسرتها الجائعة. بإلهام من إيمانها وتواضعها، يعترف راسكولنيكوف بجريمته، ويُحكم عليه بالأشغال الشاقة في سيبيريا حيث تبدأ ولادته الروحية الجديدة.

## الدرس الوجودي
الروح الإنسانية ترفض الانفصال عن الضمير الجمعي، والفلسفات المادية العدمية تعجز أمام عمق الفطرة والوجدان البشري.
"""
    },
    {
        "id": "07_The_Brothers_Karamazov",
        "title_en": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky (1880)",
        "title_ar": "الإخوة كارامازوف - فيودور دوستويفسكي",
        "content_en": """# The Brothers Karamazov by Fyodor Dostoevsky

## Core Premise
A profound philosophical exploration of faith, doubt, morality, free will, and guilt centered on the dysfunctional Karamazov family in 19th-century Russia, culminating in the patricide of Fyodor Pavlovich Karamazov.

## The Four Brothers as Psychological Archetypes
1. **Dmitri (Passion)**: Sensual, impulsive, and torn between debauchery and spiritual honor.
2. **Ivan (Intellect & Doubt)**: The rationalist intellectual who grapples with the problem of evil and suffering (author of the famous parable *The Grand Inquisitor*).
3. **Alyosha (Faith & Compassion)**: The gentle novice monk who represents unconditional Christian love and moral purity.
4. **Smerdyakov (Resentment & Nihilism)**: The illegitimate son and servant who puts Ivan's philosophical premise ("If God does not exist, everything is permitted") into literal murderous action.

## Key Parable: The Grand Inquisitor
Ivan's philosophical poem imagines Christ returning during the Spanish Inquisition. The Grand Inquisitor arrests Christ, arguing that freedom of conscience is too agonizing a burden for frail humanity; humans prefer bread, mystery, and submission to freedom. Christ answers only with a silent kiss of compassion.

## Resolution & Message
Everyone is responsible to all men for all things. Redemption comes through active love and mutual responsibility, not cold intellectual logic.
""",
        "content_ar": """# ملخص رواية الإخوة كارامازوف - فيودور دوستويفسكي

## الإطار العام
قمة أدب دوستويفسكي وملحمة فلسفية تستكشف الإيمان والشك والحرية والمسؤولية الأخلاقية، من خلال مأساة أسرة كارامازوف التي تتوج بجريمة قتل الأب الفاسد فيودور بافلوفيتش.

## الإخوة الأربعة ونماذج النفس البشرية
1. **ديمتري (العاطفة والجسد)**: مندفع وحيوي، يتأرجح بين الرغبات الحسية والسمو الأخلاقي.
2. **إيفان (العقل والشك)**: المفكر العقلاني المتألم من وجود الشر وعذاب الأبرياء في العالم، وصاحب أسطورة "المفتش الأكبر".
3. **أليوشا (الإيمان والروح)**: الراهب الشاب الوديع الذي يمثل المحبة الصادقة والتسامح والنقاء القلبي.
4. **سميردياكوف (العدمية والحقد)**: الابن غير الشرعي الذي يترجم فكرة إيفان الفلسفية ("إذا لم يكن الإله موجوداً فكل شيء مباح") إلى جريمة قتل فعلية.

## قصة المفتش الأكبر
قصيدة رمزية يرويها إيفان عن عودة المسيح أثناء محاكم التفتيش الإسبانية؛ يعتقله المفتش الأكبر ويخبره بأن البشر يعجزون عن تحمل عبء الحرية، ويفضلون الخبز والتبعية على حرية الضمير. يجيب المسيح بتقبيل المفتش بصمت في تعبير عن الحب الإلهي الخالص.

## الرسالة المركزية
كل إنسان مسؤول عن كل إنسان وعن كل خطيئة في هذا العالم؛ والمحبة العملية هي الملاذ الوحيد لشفاء الروح الإنسانية.
"""
    },
    {
        "id": "08_The_Trial",
        "title_en": "The Trial",
        "author": "Franz Kafka (1925)",
        "title_ar": "المحاكمة - فرانز كافكا",
        "content_en": """# The Trial by Franz Kafka

## Core Premise
Josef K., a respectable bank officer, is arrested one morning by an obscure, impenetrable authority for a crime that is never specified. He is left free to conduct his life, but becomes increasingly consumed by a nightmarish, labyrinthine bureaucratic judicial system.

## The Absurdist Labyrinth
- **The Invisible Authority**: The judges, upper courts, and actual laws remain entirely unseen and unreachable.
- **The Parable 'Before the Law'**: A man from the country spends his entire life waiting outside an open doorway to the Law, guarded by an impassive doorkeeper, only to learn on his deathbed that the door was meant only for him, and is now being shut.
- **Psychological Paralysis**: K. attempts to mount a rational defense, consult lawyers, and enlist painters and priests, but all efforts merely trap him further in the absurdity.

## The Climax
On the eve of his thirty-first birthday, two executioners lead Josef K. to a quarry outside town. He is stabbed in the heart, dying with his final whispered words: "Like a dog!"

## Philosophical Meaning
A terrifying allegory of alienation, existential guilt, and the helplessness of modern individuals facing dehumanizing, inaccessible institutional power.
""",
        "content_ar": """# ملخص رواية المحاكمة - فرانز كافكا

## الإطار العام
يستيقظ جوزيف ك.، الموظف المصرفي الناجح، ذات صباح ليجد نفسه رهن الاعتقال من قبل سلطة غامضة وغير مرئية بتهمة لا تُعلن له أبداً. يُترك حراً لممارسة عمله، لكنه يغرق تدريجياً في دهاليز نظام قضائي بيروقراطي كابوسي لا مخرج منه.

## المتاهة الكافكاوية
- **السلطة الغائبة**: القضاة والمحاكم العليا والقوانين الفعلية تظل محجوبة وخفية تماماً عن الإدراك.
- **حكاية أمام القانون (Before the Law)**: يقضي رجل ريفي عمره بأكمله منتظراً أمام باب القانون الذي يحرسه حارس مهيب، ليعلم عند احتضاره أن هذا الباب كان مخصصاً له وحده، وأنه سيُغلق الآن إلى الأبد.
- **العجز والانهيار**: يحاول جوزيف ك. عبثاً الاستعانة بالمحامين والرسامين ورجال الدين للدفاع عن نفسه، لكن كل خطوة منطقية تزيد من إحكام الشباك حوله.

## النهاية والرسالة
في ليلة عيد ميلاده الحادي والثلاثين، يقتاده جلادان مجهولان إلى محجر مهجور خارج المدينة ويطعنانه في قلبه، ليلفظ أنفاسه الأخيرة قائلاً: "كالكلب!".

## المغزى الوجودي
مرثية بليغة لعصر الحداثة والبيروقراطية الخانقة، وتجسيد للشعور بالاغتراب والذنب الوجودي أمام قوى مجهولة تسلب الإنسان كرامته وإرادته.
"""
    },
    {
        "id": "09_One_Hundred_Years_Of_Solitude",
        "title_en": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez (1967)",
        "title_ar": "مئة عام من العزلة - غابرييل غارسيا ماركيز",
        "content_en": """# One Hundred Years of Solitude by Gabriel García Márquez

## Core Premise
The multi-generational saga of the Buendía family across seven generations in the mythical Colombian town of Macondo, charting their rise, wars, modernization, decadence, and ultimate apocalyptic oblivion.

## Magical Realism as Truth
Márquez treats the miraculous as mundane (flying carpets, yellow butterfly swarms, ascension into heaven) and the mundane as miraculous (ice, magnets, magnifying glasses). This technique mirrors the historical reality and emotional psyche of Latin America.

## Key Themes & The Curse of Solitude
- **Cyclical Time**: Names, personalities, passions, and mistakes repeat relentlessly from generation to generation (the adventurous José Arcadios and the contemplative Aurelianos).
- **The Curse of Incest & Solitude**: The fear of bearing a child with a pig's tail haunts the family from its founding to its final descendant.
- **The Banana Massacre**: A harrowing depiction of imperialist exploitation, where the state massacres thousands of striking banana workers and erases the memory from official history.
- **Melquíades' Parchments**: The gypsy Melquíades records the family's entire destiny in advance. As the final Buendía deciphers the manuscripts, a biblical hurricane sweeps Macondo from the face of the earth.

## Famous Opening Line
"Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that distant afternoon when his father took him to discover ice."
""",
        "content_ar": """# ملخص رواية مئة عام من العزلة - غابرييل غارسيا ماركيز

## الإطار العام
ملحمة أسطورية تمتد عبر سبعة أجيال لعائلة بوينديا في بلدة ماكوندو الخيالية في كولومبيا؛ ترصد نشأة البلدة وازدهارها، ثم دخولها في الحروب الأهلية والتحولات الاستعمارية، وانتهاءً بزوالها التام في إعصار مهيب.

## الواقعية السحرية
يمزج ماركيز بين المعجزات والخوارق كأمور عادية يومية (سجاد طائر، أسراب الفراشات الصفراء، الصعود إلى السماء)، وبين المخترعات البسيطة كمعجزات مدهشة (الثلج والمغناطيس والعدسات). تعكس هذه التقنية التاريخ الحقيقي والوجدان الجمعي لأمريكا اللاتينية.

## المحاور الكبرى ولعنة العزلة
- **الزمن الدائري**: تتكرر الأسماء والطباع والأخطاء جيلاً بعد جيل دون أن يتعلم الأبناء من مآسي الآباء (عاطفة خوسيه أركاديو وعزلة أوريليانو).
- **مجزرة عمال الموز**: تصوير عبقري للاستغلال الرأسمالي والاستبداد السياسي، حيث يُباد آلاف العمال المضربين وتُمحى الحادثة تماماً من الذاكرة الرسمية.
- **مخطوطات ملكياديس**: كتب الغجري ملكياديس مصير العائلة مشفراً قبل مئة عام؛ ومع قراءة آخر سليل لآخر سطر، تجتاح عاصفة هوجاء بلدة ماكوندو وتمحوها إلى الأبد من ذاكرة البشر.

## الافتتاحية الخالدة
"بعد سنوات طويلة، وأمام فصيل الإعدام، كان العقيد أوريليانو بوينديا سيتذكر تلك الأمسية البعيدة التي أخذه فيها والده للتعرف على الثلج."
"""
    },
    {
        "id": "10_The_Lord_Of_The_Rings",
        "title_en": "The Lord of the Rings",
        "author": "J.R.R. Tolkien (1954-1955)",
        "title_ar": "سيد الخواتم - ج. ر. ر. تولكين",
        "content_en": """# The Lord of the Rings by J.R.R. Tolkien

## Epic Structure
Divided into three volumes: *The Fellowship of the Ring*, *The Two Towers*, and *The Return of the King*. The narrative follows the hobbit Frodo Baggins on a desperate quest across Middle-earth to destroy the corrupting One Ring in the fires of Mount Doom, where it was forged by the Dark Lord Sauron.

## Core Themes
1. **The Corrupting Nature of Absolute Power**: The Ring cannot be wielded for good; it inevitably bends every possessor to malice and tyranny.
2. **The Triumph of the Humble**: Salvation is not delivered by mighty warriors or ancient wizards, but by hobbits—the smallest, simplest, and most unassuming creatures.
3. **Pity and Mercy**: Bilbo and Frodo's refusal to kill Gollum out of pity ultimately enables the destruction of the Ring when all mortal willpower fails.
4. **Fellowship and Loyalty**: Self-sacrificing friendship (exemplified by Samwise Gamgee) sustains light in the darkest corners of despair.

## Lasting Cultural Impact
Tolkien established the foundational grammar, linguistic depth, and mythic standard of modern epic fantasy literature.
""",
        "content_ar": """# ملخص ملحمة سيد الخواتم - ج. ر. ر. تولكين

## البنية الملحمية
تتكون الملحمة من ثلاثة أجزاء: *رفقة الخاتم*، *البرجان*، و*عودة الملك*. تروي رحلة الهوبيت فرودو باجنز عبر أصقاع الأرض الوسطى لتدمير الخاتم الأوحد في نيران جبل الهلاك، حيث صنعه سيد الظلام ساورون.

## المحاور الفلسفية والإنسانية
1. **طبيعة السلطة المطلقة ومفسدتها**: الخاتم لا يمكن استخدامه للخير؛ فكل من يرتديه ينتهي به المطاف عبداً للشر والاستبداد.
2. **انتصار الضعفاء والمتواضعين**: الخلاص لا يتحقق ببطولات الجيوش الجرارة أو حكمة السحرة العظام، بل على أيدي الهوبيت؛ المخلوقات الأبسط والأكثر براءة في الأرض.
3. **قيمة الرحمة والشفقة**: قرار بيلبو وفرودو بالعفو عن غولوم وعدم قتله هو ما سمح في النهاية بتدمير الخاتم حين انهارت الإرادة البشرية في اللحظة الحاسمة.
4. **الإخلاص والصداقة**: الوفاء المطلق والاستعداد للتضحية (الذي جسده ساموايز غامجي) هو الشعلة التي بددت ظلمات اليأس.

## الأثر الأدبي
رسم تولكين المعايير الكلاسيكية لأدب الفانتازيا الملحمية وصاغ لغات وأساطير متكاملة ألهمت الأدب العالمي عبر العصور.
"""
    }
]

def main():
    print("==================================================")
    print("      BUILDING EXECUTIVE BOOK SUMMARIES LIBRARY   ")
    print("==================================================")
    
    count = 0
    for s in SUMMARIES:
        # Write English Summary
        en_path = os.path.join(EN_DIR, f"{s['id']}.md")
        with open(en_path, 'w', encoding='utf-8') as f:
            f.write(s['content_en'].strip() + "\n")
            
        # Write Arabic Summary
        ar_path = os.path.join(AR_DIR, f"{s['id']}_Arabic.md")
        with open(ar_path, 'w', encoding='utf-8') as f:
            f.write(s['content_ar'].strip() + "\n")
            
        print(f"  [✓] Generated: {s['id']} (EN & AR)")
        count += 1
        
    print(f"\n[✓] Generated {count} comprehensive bilingual book summaries in:")
    print(f"    - {EN_DIR}")
    print(f"    - {AR_DIR}")

if __name__ == "__main__":
    main()
