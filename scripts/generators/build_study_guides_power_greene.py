"""
Generates master-level analytical study guides for the complete Robert Greene collection:
- 06_The_48_Laws_Of_Power
- 07_The_33_Strategies_Of_War
- 08_Mastery
- 09_The_Laws_Of_Human_Nature
- 10_The_Art_Of_Seduction
- 11_The_50th_Law
- 12_The_Daily_Laws
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 06 The 48 Laws of Power
    {
        "id": "06_The_48_Laws_Of_Power",
        "content_en": """# Comprehensive Master Guide: The 48 Laws of Power
**Author:** Robert Greene  
**Year:** 1998  
**Field:** Political Philosophy / Power Dynamics / Realpolitik  

---

## 1. Historical Context & Core Philosophy
Synthesizing three thousand years of history—from Machiavelli and Sun Tzu to Talleyrand, Bismarck, and Catherine the Great—Robert Greene argues that power is an amoral game played continuously by all human beings. Denying the existence of power games is merely the most cunning game of all. Power is about mastery of emotions, strategic patience, deep observation of others, and disciplined self-restraint.

---

## 2. Structural Analysis of Key Laws

### Pillars of Power Strategy:
- **Law 1: Never Outshine the Master**: Always make those above you feel comfortably superior. Do not display all your talents openly, or you will inspire fear and insecurity. Make your masters appear more brilliant than they are.
- **Law 2: Never Put Too Much Trust in Friends; Learn How to Use Enemies**: Friends will betray you faster because they are easily aroused to envy; an old enemy whom you hire has more to prove and will be more loyal.
- **Law 3: Conceal Your Intentions**: Keep people off-balance and in the dark by never revealing the purpose behind your actions. Lead them down a false path.
- **Law 4: Always Say Less Than Necessary**: The more you speak, the more common you appear, and the more likely you are to say something foolish. Powerful people impress and intimidate by saying little.
- **Law 5: So Much Depends on Reputation—Guard It with Your Life**: Reputation is the cornerstone of power. Through reputation alone you can intimidate and win. Once slipped, you become vulnerable to attacks on every side.
- **Law 6: Court Attention at All Costs**: Everything is judged by its appearance; what is unseen counts for nothing. Stand out from the crowd; be mysterious and larger than life.
- **Law 7: Get Others to Do the Work for You, but Always Take the Credit**: Use the wisdom, knowledge, and legwork of other people to further your own cause. In the end, only the coordinator is remembered.
- **Law 9: Win Through Your Actions, Never Through Argument**: You can never truly convince anyone through heated debate. Demonstrate your point through concrete actions without saying a word.
- **Law 15: Crush Your Enemy Totally**: If one ember is left burning, a fire will eventually break out. Extinguish your adversaries completely so they cannot regroup to strike back.
- **Law 28: Enter Action with Boldness**: If you are unsure of a course of action, do not attempt it. Timidity is dangerous; boldness strikes fear and commands respect.
- **Law 33: Discover Each Man's Thumbscrew**: Everyone has a weakness, a secret insecurity, or an uncontrollable need. Once you uncover it, you hold the key to their behavior.
- **Law 48: Assume Formlessness**: By taking a shape, by having a visible plan, you open yourself to attack. Stay adaptable, fluid, and unpredictable like water.

---

## 3. The Psychology of the Courtier & Transgressions
Greene emphasizes that power requires detachment from personal ego. The fatal error of the amateur is emotional reactivity—anger, impatience, and vanity. The master courtier operates with cold, polite elegance, never showing pain or wounded pride in public.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: 48 قانوناً للقوة (The 48 Laws of Power)
**المؤلف:** روبرت غرين (Robert Greene)  
**سنة النشر:** 1998  
**المجال:** الفلسفة السياسية الواقعية / ديناميكيات النفوذ والسلطة / الميكيافيلية التاريخية  

---

## 1. السياق التاريخي والفلسفة الجوهرية
يستخلص روبرت غرين خلاصة ثلاثة آلاف عام من الصراعات الإنسانية والتاريخية؛ مستلهماً من مكيافيللي، وسون تزو، وبسمارك، وتاليران، ونابليون. يرى غرين أن القوة لعبة لا أخلاقية يمارسها البشر جميعاً في كل مجالات الحياة. الادعاء بالطهرانية أو الترفع عن مناورات القوة هو في حد ذاته حيلة من حيل اللعبة. القوة تتطلب السيطرة المطلقة على المشاعر، والصبر الاستراتيجي، والملاحظة العميقة لسلوك الآخرين.

---

## 2. التحليل الهيكلي لأبرز قوانين القوة الكبرى

- **القانون 1: إياك أن تتفوق على سيدك**: اجعل من هم فوقك يشعرون دوماً بتفوقهم وأمانهم؛ لا تستعرض مواهبك بالكامل أمامهم حتى لا تثير مخاوفهم وحقدهم.
- **القانون 2: لا تضع ثقة مفرطة في الأصدقاء، وتعلم كيف تستخدم الأعداء**: الأصدقاء أسرع خيانة بدافع الغيرة؛ بينما العدو الذي تستعين به لديه ما يثبته وسيكون أشد ولاءً وإخلاصاً.
- **القانون 3: اكتم نواياك الحقيقية**: حافظ على ارتباك خصومك بعدم كشف أهدافك الحقيقية، واجعلهم يسيرون في مسارات خادعة.
- **القانون 4: قل دائماً أقل مما هو ضروري**: كلما زاد كلامك، بدوت عادياً وأقل شأناً، وزاد احتمال زلتك؛ أصحاب النفوذ يثيرون الرهبة بالإيجاز والغموض.
- **القانون 5: الكثير يعتمد على السمعة فاحمِها بحياتك**: السمعة هي حجر الزاوية للقوة؛ بالسمعة وحدها ترهب خصومك وتنتصر، وإذا تلطخت أصبحت عرضة للسهام من كل جانب.
- **القانون 6: الفت الانتباه بأي ثمن**: كل شيء يُحكم عليه بالمظهر؛ ما لا يُرى لا قيمة له. تميز عن الحشود واصنع لنفسك هالة غامضة.
- **القانون 7: اجعل الآخرين يقومون بالعمل لكن احصد التقدير لنفسك**: استعن بجهود وخبرات الآخرين لدعم مشروعك، فالتاريخ لا يذكر سوى القائد الذي نسق العمل.
- **القانون 9: اكسب بأفعالك لا بالجدال**: لا يمكنك إقناع شخص في جدال كلامي محتدم دون إثارة حنقه؛ أثبت وجهة نظرك بالأفعال الملموسة دون كلام.
- **القانون 15: اسحق عدوك تماماً**: إذا تركت جمرة مشتعلة، ستندلع النار مجدداً. اقضِ على خصمك بالكامل ولا تترك له فرصة للنهوض والانتقام.
- **القانون 28: ادخل الميدان بجرأة وشجاعة**: التردد يولد الأخطاء ويعرضك للهلاك؛ والجرأة تفرض الاحترام وتزرع الهيبة.
- **القانون 33: اكتشف نقطة الضعف في كل إنسان**: لكل شخص ثغرة خفية أو رغبة جامحة أو خوف مكبوت؛ متى عرفت نقطة ضعفه ملكت زمام أمره.
- **القانون 48: لا تتخذ شكلاً ثابتاً (كن كالسائل)**: بالثبات والوضوح المكشوف تصبح هدفاً سهلاً لضربات الخصوم؛ كن كالسائل مرناً متكيفاً غير متوقع.

---

## 3. نفسية رجل الحاشية والأخطاء القاتلة
يؤكد غرين أن القوة الحقيقية تبدأ بضبط النفس وإلغاء الأنا المتضخمة. الخطأ القاتل الذي يقع فيه المبتدئون هو الانفعال اللحظي (الغضب، التسرع، الغرور). خبير القوة يتسم بالبرود الأنيق، والمجاملة الدبلوماسية، والقدرة على الانتظار حتى تحين اللحظة المناسبة.
"""
    },

    # 07 The 33 Strategies of War
    {
        "id": "07_The_33_Strategies_Of_War",
        "content_en": """# Comprehensive Master Guide: The 33 Strategies of War
**Author:** Robert Greene  
**Year:** 2006  
**Field:** Military Strategy / Psychological Warfare / Strategic Leadership  

---

## 1. Core Premise: Life as Endless Strategic Conflict
Daily social and professional life is a subtle form of warfare. Without a strategic framework, human beings react emotionally to conflict, suffering defeat through panic or passive aggression. Greene adapts millennia of military theory (Sun Tzu, Clausewitz, Alexander the Great, Napoleon, Patton) to master the battlefield of life.

---

## 2. The Five Strategic Parts

### Part I: Self-Directed Warfare (Mastering Your Own Mind)
1. **The Polarity Strategy**: Declare war on your enemies. Know who you are fighting; clarity of opposition sharpens focus.
2. **The Guerrilla-War-of-the-Mind Strategy**: Do not fight the last war. Adapt your mind to the changing reality; shed dogmas and outdated playbooks.
3. **The Counterbalance Strategy**: Amidst the turmoil of events, maintain your inner presence of mind. Detach yourself from fear and emotional panic.
4. **The Death-Ground Strategy**: Create a sense of urgency and desperation. When soldiers have no retreat behind them, they fight with superhuman courage. Burn your ships.

### Part II: Organizational Warfare (Team Leadership & Cohesion)
5. **The Command-and-Control Strategy**: Avoid micromanagement; install mission command where field officers understand the broad intent and execute fluidly.
6. **The Controlled-Chaos Strategy**: Fragment your forces and hit from multiple angles to paralyze enemy command structures.
7. **Morale Strategies**: Transform your team into a crusade; bind them with a higher ideological purpose.

### Part III: Defensive Warfare
8. **The Perfect-Economy Strategy**: Pick your battles carefully. Conserve resources; fight only when victory brings disproportionate gain.
9. **The Counterattack Strategy**: Turn the tables. Lure the enemy into overextending their position, then strike their exposed flanks.
10. **Deterrence Strategies**: Create a threatening reputation so potential adversaries calculate that attacking you is far too costly.

### Part IV: Offensive Warfare
11. **The Trade-Off Strategy**: Gain territory by sacrificing short-term assets.
12. **The Center-of-Gravity Strategy**: Strike at the linchpin that holds the opponent's entire organization together.
13. **Divide and Conquer**: Separate allies; break up coordinated coalitions into isolated, weak factions.
14. **The Turning Strategy**: Encircle the enemy by striking their exposed rear while engaging their attention from the front.

### Part V: Unconventional (Dirty) Warfare
15. **The Foreseen-Fallacy Strategy**: Plant false information to lead the enemy into misjudging reality.
16. **The Alliance Strategy**: Form convenient partnerships, but always remember that allies are temporary and self-interested.
17. **The Void Strategy**: Offer no target for enemy aggression; wear them down through empty space and psychological attrition.
""",
        "content_ar": """# الدليل الدراسي والاستراتيجي الشامل: 33 استراتيجية للحرب (The 33 Strategies of War)
**المؤلف:** روبرت غرين (Robert Greene)  
**سنة النشر:** 2006  
**المجال:** الاستراتيجية العسكرية / الحرب النفسية / فن القيادة والمناورة  

---

## 1. الفلسفة الجوهرية: الحياة كحلبة صراع استراتيجي دائم
يرى روبرت غرين أن الصراعات الاجتماعية والمهنية اليومية ما هي إلا شكل متطور من أشكال الحرب. ودون امتلاك عقلية استراتيجية واعية، يستسلم الإنسان للانفعالات العاطفية ويخسر معاركه في الحياة نتيجة الذعر أو السلبية. يستلهم الكتاب مبادئ كبار القادة العسكريين عبر التاريخ (سون تزو، كلاوزفيتز، الإسكندر الأكبر، نابليون).

---

## 2. الأقسام الاستراتيجية الخمسة الكبرى

### القسم الأول: الحرب الموجهة للذات (السيطرة على عقلك أولاً)
1. **استراتيجية القطبية**: أعلن الحرب على أعدائك؛ وضوح جبهة الخصم يمنحك تركيزاً فائقاً ويوحد صفوفك.
2. **حرب العصابات الذهنية**: لا تخض معركة اليوم بأسلحة وتكتيكات الأمس؛ حرر عقلك من القوالب الجامدة وتكيف مع الوقائع الجديدة.
3. **استراتيجية التوازن النفسي**: حافظ على هدوئك وحضورك الذهني في قلب الفوضى والأزمات، ولا تستسلم للذعر.
4. **استراتيجية أرض الموت (احرق سفنك)**: اخلق لنفسك ولرجالك حالة من الإلحاح والاضطرار؛ المقاتل الذي لا يملك خياراً للانسحاب يقاتل بشراسة أسطورية.

### القسم الثاني: الحرب التنظيمية (قيادة الفريق والتماسك)
5. **استراتيجية القيادة والتحكم**: تجنب الإدارة التفصيلية الخانقة؛ امنح رجالك حرية الحركة مع توضيح الهدف الاستراتيجي العام.
6. **استراتيجية الفوضى المنضبطة**: جزئ قواتك وهاجم من زوايا متعددة لشل قدرة الخصم على التنبؤ.
7. **استراتيجية الروح المعنوية**: حول عمل فريقك إلى قضية سامية ورسالة كبرى لتوحيد طاقاتهم.

### القسم الثالث: الحرب الدفاعية
8. **استراتيجية الاقتصاد المثالي**: اختر معاركك بحكمة؛ لا تستنزف مواردك في معارك جانبية لا طائل منها.
9. **استراتيجية الهجوم المعاكس**: استدرج الخصم ليتمدد خارج خطوطه الدفاعية، ثم اضرب أجنحته المكشوفة بضربة قاصمة.
10. **استراتيجية الردع**: ابنِ لنفسك سمعة تجعل أي خصم يفكر ألف مرة قبل مهاجمتك لعلمه بفداحة الثمن.

### القسم الرابع: الحرب الهجومية
11. **استراتيجية التضحية**: اضغط على الخصم بالتنازل عن مكاسب ثانوية للظفر بالهدف الاستراتيجي الأكبر.
12. **استراتيجية مركز الثقل**: اضرب الركيزة المحورية التي يعتمد عليها كيان الخصم بالكامل لتنهار كل بنيته.
13. **فرق تسد**: فكك تحالفات خصومك واضرب كل طرف على حدة وهو في أضعف حالاته.

### القسم الخامس: الحرب غير التقليدية (الذكاء النفسي)
14. **استراتيجية الفراغ**: لا تمنح الخصم هدفاً ثابتاً يفرغ فيه ضرباته؛ دعه يصارع الفراغ حتى ينهكه التعب والإحباط النفسي.
15. **استراتيجية كسر الوهم**: واجه الحقيقة المجردة دوماً؛ فالعدو الأخطر هو وهمك الشخصي وتمنياتك الخادعة.
"""
    },

    # 08 Mastery
    {
        "id": "08_Mastery",
        "content_en": """# Comprehensive Master Guide: Mastery
**Author:** Robert Greene  
**Year:** 2012  
**Field:** Cognitive Psychology / Creative Genius / Human Excellence  

---

## 1. The Core Thesis: Mastery is Accessible to All
Genius is not a mystical innate gift bestowed upon a lucky few; it is the natural byproduct of intense, prolonged, and focused engagement with a specific craft. Greene analyzes masters such as Leonardo da Vinci, Charles Darwin, Wolfgang Amadeus Mozart, Albert Einstein, and contemporary masters to map out the psychological journey from novice to master.

---

## 2. The Three Phases of Mastery

### Phase 1: Discover Your Life's Task (The Primal Inclination)
- Every human being possesses a unique genetic and psychological makeup that inclines them toward certain activities in childhood.
- To achieve mastery, you must reconnect with this **Life's Task** and clear away the expectations of parents, society, and peer pressure.

### Phase 2: The Ideal Apprenticeship (The Crucible)
The Apprenticeship phase lasts roughly 5 to 10 years (or 10,000 hours). It is not about earning money or gaining immediate status; it is about pure skill acquisition.
1. **Deep Observation (The Passive Mode)**: When entering a new field, mute your ego. Observe the rules, hierarchy, and unspoken cultural codes.
2. **Skills Acquisition (The Practice Mode)**: Engage in intense, repetitive deliberate practice. The brain rewires neural pathways through repetition.
3. **Experimentation (The Active Mode)**: Gradually take risks, push boundaries, and test your own variations.
4. **Mentorship**: Seek out a master who can accelerate your learning by decades. Absorb their knowledge, then ruthlessly outgrow and leave them behind.

### Phase 3: The Creative-Active & Mastery
- Once technical skills become second nature, the mind opens to the **Dimensional Mind**—the capacity to combine disparate concepts into radical innovations.
- True Mastery is intuitive intelligence: the master perceives patterns and solutions instantly because their mind is completely fused with the medium.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الإتقان (Mastery)
**المؤلف:** روبرت غرين (Robert Greene)  
**سنة النشر:** 2012  
**المجال:** علم النفس المعرفي / الإبداع والعبقرية / تطوير المهارات العليا  

---

## 1. الفكرة الجوهرية: الإتقان حق مكتسب بالانضباط
يرفض روبرت غرين أسطورة أن "العبقرية موهبة فطرية غامضة" يولد بها قلة من المحظوظين. العبقرية هي النتيجة الطبيعية والحتمية للتركيز العميق والانضباط الطويل في مجال معين. يحلل غرين مسيرة عظماء التاريخ (ليوناردو دافنشي، تشارلز داروين، موزارت، آينشتاين) ليرسم خارطة طريق واضحة لكل من يسعى للوصول إلى قمة مجاله.

---

## 2. المراحل الثلاث الكبرى للوصول إلى الإتقان

### المرحلة الأولى: اكتشاف نداء الحياة ومهمة العمر (Life's Task)
- يمتلك كل إنسان ميولاً فطرية وشغفاً حقيقياً يظهر بوضوح في مرحلة الطفولة المبكرة.
- الوصول للإتقان يبدأ بالتصالح مع هذا الميول الداخلي والتخلص من ضغوط الآباء والمجتمع التي تدفعك نحو مسارات تقليدية لا تشبهك.

### المرحلة الثانية: التلمذة المثالية (سنوات الصقل والمعاناة)
تستمر هذه المرحلة من 5 إلى 10 سنوات (أو ما يقارب 10,000 ساعة من الممارسة المركزة). هدفها ليس جمع المال أو الشهرة السريعة، بل اكتساب المهارات الخام:
1. **الملاحظة العميقة الصامتة**: عند دخول مجال جديد، اخفض صوت الأنا وراقب القواعد وآليات العمل بصمت.
2. **اكتساب المهارات بالممارسة الشاقة**: كرر الأساسيات حتى تصبح جزءاً من ذاكرتك العضلية والعصبية.
3. **التجريب النشط**: ابدأ في اختبار أفكارك الخاصة تدريجياً وتحمل أخطاء التجربة.
4. **التتلمذ على يد مرشد عبقري (Mentorship)**: ابحث عن أستاذ عظيم يختصر عليك عقوداً من التعلم، وامتص خبرته، ثم تجاوزه بشجاعة.

### المرحلة الثالثة: الإبداع النشط والوصول للذكاء الحدسي
- عندما تصبح المهارات التقنية طبيعة ثانية، ينفتح العقل على "العقل ذي الأبعاد"، حيث يربط بين مجالات متباعدة لابتكار حلول عبقرية.
- الإتقان الحقيقي هو ذكاء حدسي فوري؛ يرى فيه الخبير الحلول والأنماط بلمحة بصر لأن عقله اندمج تماماً في صلب صنعته.
"""
    },

    # 09 The Laws of Human Nature
    {
        "id": "09_The_Laws_Of_Human_Nature",
        "content_en": """# Comprehensive Master Guide: The Laws of Human Nature
**Author:** Robert Greene  
**Year:** 2018  
**Field:** Evolutionary Psychology / Behavioral Analysis / Self-Awareness  

---

## 1. Core Premise: Decoding the Primal Drivers of Mankind
Human beings are governed by ancient evolutionary instincts that evolved over hundreds of thousands of years. We imagine ourselves to be modern, conscious, and rational, yet we are constantly driven by unconscious drives: narcissism, envy, grandiosity, irrationality, and tribal aggression. Understanding these primal forces frees you from being their blind victim.

---

## 2. Structural Analysis of the Major Laws

1. **The Law of Irrationality**: Master your emotional self. Realize that emotions constantly cloud your reasoning. Recognize your cognitive biases (confirmation bias, conviction bias, appearance bias).
2. **The Law of Narcissism**: Transform self-love into empathy. Everyone is born a narcissist; channel your focus outward into deep, active empathy for others.
3. **The Law of Role-Playing**: See behind people's masks. People wear polite masks in public; observe their micro-expressions, body language, and slips of the tongue.
4. **The Law of Compulsive Behavior**: Character is destiny. Do not judge people by their words or promises; judge them strictly by their repetitive patterns of behavior over time.
5. **The Law of Covetousness**: Become an elusive object of desire. People desire what they cannot have; create mystery and distance to maintain value.
6. **The Law of Shortsightedness**: Elevate your perspective. Resist immediate gratification and short-term panic; focus on long-term trajectories.
7. **The Law of Defensiveness**: Soften people's resistance by confirming their self-opinion. Never attack someone's core identity directly.
8. **The Law of Self-Sabotage**: Change your circumstances by changing your attitude. Your inner attitude acts as a self-fulfilling prophecy.
9. **The Law of Repression (The Shadow)**: Confront your dark side. Accept and integrate the repressed aspects of your personality before they erupt destructively.
10. **The Law of Envy**: Beware the fragile ego. Envy disguises itself as criticism or passive-aggressive behavior; deflect it with humility.
11. **The Law of Grandiosity**: Know your limits. Success causes delusional grandiosity; stay grounded in realistic humility.
12. **The Law of Mortality**: Meditate on your common mortality (*Memento Mori*). Remembering death purifies petty concerns and infuses daily life with supreme urgency.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: قوانين الطبيعة البشرية (The Laws of Human Nature)
**المؤلف:** روبرت غرين (Robert Greene)  
**سنة النشر:** 2018  
**المجال:** علم النفس التطوري / تحليل الشخصيات / الوعي الذاتي والسلوك البشري  

---

## 1. الفلسفة الجوهرية: فك شفرة الغرائز البشرية الدفينة
يرى روبرت غرين أن البشر تحكمهم دوافع تطورية غائرة تشكلت عبر مئات آلاف السنين. نتوهم أننا كائنات عقلانية ومتحضرة، لكننا في الحقيقة نقع أسرى لدوافع لا واعية: النرجسية، والحسد، والغرور، والعصبية القبلية. فهم هذه القوانين يحررك من الوقوع ضحية لمكائد الآخرين ولأوهام نفسك الشخصية.

---

## 2. التحليل الهيكلي لأبرز القوانين

1. **قانون اللاعقلانية**: سيطر على عواطفك؛ العاطفة تعمي البصيرة وتشوه التفكير المنطقي. اعترف بانحيازاتك المعرفية المسبقة.
2. **قانون النرجسية**: حوّل حب الذات إلى تعاطف نشط مع الآخرين بدلاً من الانغلاق داخل فقاعة الأنا.
3. **قانون تقمص الأدوار**: انظر خلف الأقنعة؛ البشر يرتدون أقنعة اجتماعية مهذبة، راقب لغة أجسادهم وزلات ألسنتهم وردود أفعالهم العفوية.
4. **قانون السلوك القهري (الشخصية هي القدر)**: لا تحكم على الناس بوعودهم وكلامهم المعسول، بل احكم عليهم بسلسلة تصرفاتهم المتكررة عبر الزمن.
5. **قانون الاشتهاء والتمنّع**: كن عصياً على الامتلاك؛ البشر يشتهون ما لا يستطيعون الحصول عليه، واصنع هالة من الغموض حول نفسك.
6. **قانون قصر النظر**: ارفع أفق نظرك؛ لا تنغمس في انفعالات اليوم وأزمات اللحظة، بل انظر للصورة الاستراتيجية البعيدة.
7. **قانون الدفاعية**: لا تهاجم كبرياء الآخرين مباشرة، بل هدئ مقاومتهم بتأكيد احترامك لذواتهم.
8. **قانون تدمير الذات**: غير واقعك بتغيير نظرتك الذهنية؛ فموقفك الداخلي نبوءة تحقق ذاتها في الواقع.
9. **قانون كبت الجانب المظلم (الظل)**: واجه عيوبك ونقاط ضعفك الدفينة واعترف بها حتى لا تنفجر في سلوكيات مدمرة دون وعي منك.
10. **قانون الحسد**: احذر من الكبرياء الهش؛ الحسد يتنكر في صورة نقد لاذع أو سلبية مبطنة، واحمِ نفسك بإظهار التواضع.
11. **قانون تذكر الفناء (Memento Mori)**: استشعر دنو الموت دوماً؛ تذكر الموت ينقي النفس من الصغائر ويمنح كل يوم في حياتك طاقة وتركيزاً استثنائياً.
"""
    },

    # 10 The Art of Seduction
    {
        "id": "10_The_Art_Of_Seduction",
        "content_en": """# Comprehensive Master Guide: The Art of Seduction
**Author:** Robert Greene  
**Year:** 2001  
**Field:** Social Dynamics / Charisma / Psychological Influence  

---

## 1. Core Concept: Seduction as Psychological Persuasion
Seduction is not merely sexual romance; it is the ultimate form of soft power and subtle persuasion. While brute force and argumentation create friction and resentment, seduction creates willing surrender. The seducer pulls others in by understanding their hidden voids, fantasies, and psychological needs.

---

## 2. The Nine Seducer Profiles & The 24-Step Process

### The Seducer Archetypes:
1. **The Siren**: Epitomizes intense sexual fantasy and theatrical danger.
2. **The Rake**: Driven by insatiable passion; appeals to women's desire to be fiercely desired.
3. **The Ideal Lover**: Creates an idealized fantasy world that compensates for the mundanity of everyday life.
4. **The Dandy**: Blurs gender norms and social conventions; enigmatic and non-conformist.
5. **The Natural**: Radiates playful, childlike innocence and uninhibited charm.
6. **The Coquette**: Masters the dance of hot and cold, drawing people in through unpredictable emotional delays.
7. **The Charmer**: Flatters, uplifts, and makes everyone feel immensely appreciated without demanding anything in return.
8. **The Charismatic**: Projects an intense inner conviction and purpose that commands discipleship.
9. **The Star**: Enigmatic, glamorous, and larger than life; offers an escape from reality.

### The 24-Step Seduction Process:
- **Phase 1: Arouse Interest & Desire**: Choose the right victim; create a false sense of security; approach obliquely; send mixed signals.
- **Phase 2: Lead Astray**: Create surprises; stir the senses; enter their spirit; create a need or anxiety.
- **Phase 3: The Precipice**: Deepen the emotional hook; master the art of the bold move; isolate the target.
- **Phase 4: Moving In for the Kill**: Arouse both transgressive thrills and emotional surrender.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: فن الإغواء (The Art of Seduction)
**المؤلف:** روبرت غرين (Robert Greene)  
**سنة النشر:** 2001  
**المجال:** القوة الناعمة / الكاريزما والتأثير النفسي / علم الجاذبية الاجتماعية  

---

## 1. المفهوم الجوهري: الإغواء كأعلى مراتب القوة الناعمة
لا يقتصر الإغواء على الجانب العاطفي أو الجنسي، بل هو في جوهره فن التأثير النفسي والإقناع غير المباشر. في حين أن القوة الغاشمة تولد الرفض والمقاومة، فإن الإغواء يقود الآخرين للاستسلام الطوعي برغبة وحماس. الغاوي المحترف لا يستعرض ذاته، بل يدرس الفراغ النفسي والاحتياج غير المشبع لدى الطرف الآخر ويملؤه ببراعة.

---

## 2. الأنماط التسعة للشخصيات الجذابة ومراحل العملية الإغوائية

### أبرز أنماط الجاذبية:
1. **الحورية (The Siren)**: تجسد الفتنة والخطر الأسطوري والتحرر من القيود.
2. **الفاسق المغامر (The Rake)**: يفيض شغفاً واندفاعاً لا يقاوم يمنح الطرف الآخر شعوراً بأنه مرغوب بشدة.
3. **العاشق المثالي (The Ideal Lover)**: يخلق عالماً رومانسياً بديلاً يعوض به الشريك عن رتابة الواقع.
4. **الغندور (The Dandy)**: يكسر القوالب التقليدية بالغموض والتمرد والأناقة المتفردة.
5. **الفطري (The Natural)**: يشع براءة وعفوية طفولية تسقط دفاعات الجميع.
6. **المتدللة المتقلبة (The Coquette)**: تتقن لعبة الشد والجذب، تمنح الأمل ثم تتمنع لتشعل الرغبة.
7. **الساحر (The Charmer)**: يركز بالكامل على مدح الآخر وإشعاره بأهميته دون أن يطلب شيئاً لنفسه.
8. **ذو الكاريزما (The Charismatic)**: يشع يقيناً وثقة مطلقة برسالته تجعل الآخرين يتبعونه كمريدين.
9. **النجم (The Star)**: محاط بهالة من السحر والغموض يعيش في سماء بعيدة عن البشر.

### مراحل التأثير والإغواء:
- **المرحلة الأولى**: إثارة الاهتمام والفضول عبر الإشارات المتباينة وكسر التوقع.
- **المرحلة الثانية**: إشعال الحيرة والارتباك بالدخول إلى عالم الطرف الآخر وإشاعة الترقب.
- **المرحلة الثالثة**: التعميق العاطفي وعزل الطرف الآخر عن المؤثرات الخارجية وصنع التبعية النفسية.
"""
    },

    # 11 The 50th Law
    {
        "id": "11_The_50th_Law",
        "content_en": """# Comprehensive Master Guide: The 50th Law
**Authors:** 50 Cent (Curtis Jackson) & Robert Greene  
**Year:** 2009  
**Field:** Fearlessness / Pragmatism / Street Strategy & Corporate Power  

---

## 1. Core Thesis: Fear is the Ultimate Limiting Factor
The 50th Law states: **Fear Nothing**. While the previous 48 laws govern tactics and court strategy, fearlessness is the psychological bedrock upon which all power rests. Analyzing Curtis Jackson’s (50 Cent) rise from South Jamaica, Queens crack dealer to multi-platinum artist and corporate mogul alongside historical icons (Frederick Douglass, Abraham Lincoln, Napoleon), Greene demonstrates that fear distorts reality and paralyzes decisive action.

---

## 2. The Ten Principles of Fearlessness

1. **See Things for What They Are (Intense Realism)**: Strip away emotional sugarcoating. Face harsh reality without sentimentality.
2. **Make Everything Your Own (Self-Reliance)**: Never depend completely on corporations, gatekeepers, or patrons. Ownership is true power.
3. **Turn Shit into Sugar (Opportunism)**: View every setback, betrayal, or crisis as an opportunity for reinvention.
4. **Keep Moving (Calculated Momentum)**: Do not stagnate in comfortable routines. Constantly disrupt yourself.
5. **Know When to Be Bad (Aggression)**: Stand up to bullies firmly and decisively; passivity invites predators.
6. **Lead from the Front (Authority)**: True leaders earn moral authority by taking the greatest risks themselves.
7. **Know Your Environment from the Inside Out (Connection)**: Keep your ear to the ground; never become an ivory-tower executive.
8. **Respect the Process (Mastery)**: Learn to love the grind and slow, deliberate practice.
9. **Push Beyond Your Limits (Self-Belief)**: Your self-confidence determines how far others will allow you to go.
10. **Confront Your Mortality (Sublime Perspective)**: Accepting death dissolves trivial anxieties and unleashes immense fearlessness.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: القانون الخمسون (The 50th Law)
**المؤلفون:** 50 سنت (كيرتس جاكسون) وروبرت غرين  
**سنة النشر:** 2009  
**المجال:** قهر الخوف / الواقعية الشرسة / استراتيجيات البقاء والريادة  

---

## 1. الفكرة الجوهرية: الخوف هو القيد الأكبر للإنسان
القانون الخمسون ينص على مبدأ واحد حاسم: **لا تخَف من شيء**. إذا كانت قوانين القوة الـ 48 تشرح تكتيكات المناورة، فإن التحرر من الخوف هو القاعدة النفسية الصلبة التي تقوم عليها كل سلطة. يدمج الكتاب بين قصة كيرتس جاكسون (50 Cent) وكيف تحول من حي كوينز الفقير وتجار المخدرات إلى إمبراطورية تجارية وموسيقية كبرى، وبين تجارب قادة تاريخيين واجهوا الموت بشجاعة.

---

## 2. القواعد العشر لقهر الخوف وصناعة النفوذ

1. **انظر للأمور كما هي تماماً (الواقعية الشرسة)**: انزع النظارات الوردية وواجه الواقع بقسوته دون تزييف أو تمنيات ساذجة.
2. **امتلك كل شيء يخصك (الاعتماد على الذات)**: لا تعتمد كلياً على وسطاء أو شركات أو رعاة؛ الاستقلال والملكية هما القوة الحقيقية.
3. **حوّل الأزمات إلى فرص (الانتهازية الإيجابية)**: كل طعنة أو انتكاسة هي مادة خام تصنع منها انتصارك القادم.
4. **واصل الحركة والتدفق**: الركود في منطقة الأمان هو بداية الموت؛ جدد نفسك باستمرار واكسر التكرار.
5. **اعرف متى تكون حازماً وشديداً**: الضعف والوداعة الزائدة في عالم الصراع استدعاء للحيوانات المفترسة؛ واجه المتنمرين بحسم قاطع.
6. **قُد من خط المواجهة الأول**: القائد الحقيقي يكسب هيبته وولاء رجاله بخوضه أكبر المخاطر بنفسه.
7. **افهم بيئتك حتى نخاعها**: لا تعزل نفسك في برج عاجي؛ ابقَ على اتصال مباشر بالشارع والواقع الميداني.
8. **احترم مسار التعلم والجهد الصامت**: لا تبحث عن القفزات السريعة، بل اعشق التعب والانضباط اليومي.
9. **اكسر حدودك بالإيمان المطلق بقدراتك**: ثقتك بذاتك هي السقف الذي يسمح لك العالم بالوصول إليه.
10. **واجه فكرة فنائك بشجاعة**: استحضار الموت يحررك من المخاوف التافهة ويمنحك جرأة مطلقة لصناعة المجد.
"""
    },

    # 12 The Daily Laws
    {
        "id": "12_The_Daily_Laws",
        "content_en": """# Comprehensive Master Guide: The Daily Laws
**Author:** Robert Greene  
**Year:** 2021  
**Field:** Daily Meditations / Philosophy of Life / Practical Mastery  

---

## 1. Structure & Purpose: A 366-Day Field Guide for Life
*The Daily Laws* serves as a distillation of Robert Greene’s entire life's work across 25 years. Structured as daily reflections across all twelve months, the book guides the reader through a disciplined journey of personal evolution:

- **January–March: Mastery & Life's Task**: Reconnecting with childhood inclinations, submitting to apprenticeship, and building creative intelligence.
- **April–June: Political Savvy & Power Dynamics**: Navigating court politics, reading hidden intentions, concealing plans, and neutralizing toxic adversaries.
- **July–September: Persuasion & Seduction**: Charisma, soft power, mastering emotions, and overcoming resistance.
- **October–December: Human Nature & The Sublime**: Confronting irrationality, envy, grandiosity, and meditating on mortality (*The Sublime*).

---

## 2. Core Takeaways
Consistent daily contemplation of power, strategy, and human nature prevents regression into emotional reactivity. The master is a lifelong student of reality.
""",
        "content_ar": """# الدليل الدراسي والفكري الشامل: القوانين اليومية (The Daily Laws)
**المؤلف:** روبرت غرين (Robert Greene)  
**سنة النشر:** 2021  
**المجال:** التأملات اليومية / الحكمة العملية / ممارسة الإتقان والقوة  

---

## 1. الهيكل والهدف: مرشد عملي لـ 366 يوماً
يختزل هذا الكتاب عصارة 25 عاماً من أبحاث روبرت غرين ومؤلفاته الكبرى في شكل تأملات وتطبيقات يومية مقسمة على مدار شهور السنة:

- **يناير إلى مارس (الإتقان ومهمة العمر)**: العودة لنداء الطفولة، والصبر في سنوات التلمذة، وتطوير التفكير الإبداعي.
- **أبريل إلى يونيو (الدهاء السياسي وألاعيب القوة)**: فهم صراعات النفوذ، وقراءة ما بين السطور، والحذر من الخصوم المؤذيين.
- **يوليو إلى سبتمبر (الإقناع والإغواء والكاريزما)**: التأثير النفسي الناعم، وإدارة العواطف، وتليين مقاومة الآخرين.
- **أكتوبر إلى ديسمبر (الطبيعة البشرية والسمو الروحي)**: قهر النرجسية واللاعقلانية والحسد، والارتقاء بالتأمل في فناء الحياة.

---

## 2. الخلاصة العملية
الانضباط الذهني اليومي والتأمل المستمر في ديناميكيات الحياة هما الحصن المنيع ضد الانفعال والزلل؛ الحكيم تلميذ دائم للواقع العملي.
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
