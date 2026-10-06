"""
Generates master-level study guides for Russian Literature masterpieces:
- 17_The_Brothers_Karamazov
- 18_White_Nights
- 19_War_And_Peace
- 20_Anna_Karenina
- 21_The_Master_And_Margarita
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 17 The Brothers Karamazov
    {
        "id": "17_The_Brothers_Karamazov",
        "content_en": """# Comprehensive Study Guide: The Brothers Karamazov
**Author:** Fyodor Dostoevsky  
**Year:** 1880  
**Genre:** Philosophical Novel / Psychological Drama / Theological Realism  

---

## 1. Historical & Philosophical Background
Published in 1880 just months before Dostoevsky's death, *The Brothers Karamazov* represents the pinnacle of his literary and philosophical genius. Set in 19th-century provincial Russia (Skotoprigonyevsk), the novel addresses the deepest existential dilemmas of mankind: faith versus doubt, the problem of innocent suffering (theodicy), moral responsibility, and free will.

---

## 2. In-Depth Chapter & Book Breakdown

### Books 1–3: The Karamazov Family Dynamic
- **Fyodor Pavlovich Karamazov**: A vulgar, cynical, sensualist landowner who neglected all his sons.
- **The Three Brothers**:
  - **Dmitri (Mitya)**: The eldest; sensual, passionate, honorable yet reckless. He and his father are locked in a bitter dispute over inheritance and both passionately lust after the bewitching Grushenka.
  - **Ivan**: The middle brother; a brilliant, rationalist intellectual tormented by metaphysical doubt and nihilism.
  - **Alexei (Alyosha)**: The youngest; gentle, compassionate, a novice monk at the local monastery under the spiritual tutelage of the revered Elder Zosima.
- **Pavel Smerdyakov**: The sullen, epileptic servant, widely believed to be Fyodor's illegitimate son by the mute village woman "Stinking Lizaveta."

### Books 4–6: Faith and Theodicy
- **Rebellion**: Ivan and Alyosha meet in a tavern. Ivan declares that he does not reject God, but rejects God's world because of the unmerited suffering of innocent children. He presents Alyosha with his legendary prose poem, *The Grand Inquisitor*.
- **The Grand Inquisitor**: Set during the Spanish Inquisition in Seville, Jesus returns and is arrested by the ninety-year-old Cardinal Inquisitor. The Inquisitor interrogates Christ in his cell, arguing that Christ doomed humanity by giving them freedom of choice instead of bread, miracles, and authority. Humans cannot bear freedom. In response, Christ says nothing, but silently kisses the old man's bloodless lips.
- **The Russian Monk (Elder Zosima)**: In contrast to Ivan's cold rebellion, Elder Zosima delivers his spiritual testament before dying: love all God's creation, practice active love, and realize that *"everyone is responsible to all men for all men and for everything."*

### Books 7–9: The Murder and the Arrest
- **The Odor of Corruption**: After Zosima dies, his body begins to decompose rapidly, scandalizing superstitious monks who expected a miracle. Alyosha's faith is shaken, but restored when he experiences a vision of the Wedding at Cana.
- **The Fatal Night**: Driven by frantic jealousy, Dmitri rushes to his father's house searching for Grushenka. He strikes the servant Grigory and flees covered in blood. Smerdyakov murders Fyodor Pavlovich, steals 3,000 rubles, and frames Dmitri. Dmitri is arrested at Mokroye during a wild feast with Grushenka.

### Books 10–12: The Trial and Madness
- **Ivan's Breakdown & The Devil**: In private meetings, Smerdyakov reveals to Ivan that Smerdyakov was the actual killer, but insists Ivan is the true intellectual instigator because of Ivan's philosophical doctrine: *"If there is no God, everything is permitted."* Horrified by his moral guilt, Ivan hallucinates a shabby, cynical devil visiting his room. Smerdyakov hangs himself.
- **The Trial**: Despite passionate defenses and Dmitri's protests of innocence, the provincial jury convicts Dmitri of parricide, sentencing him to Siberian exile.
- **Epilogue**: Dmitri plans an escape to America. The novel closes with Alyosha addressing a group of schoolboys at the funeral of young Ilyusha, proclaiming the resurrection of the dead and eternal love.

---

## 3. Major Characters & Themes
- **Dmitri**: The broad Russian soul, suspended between the ideal of the Madonna and the ideal of Sodom.
- **Ivan**: The tragedy of pure intellect severed from love; self-destroying pride.
- **Alyosha**: Active, practical Christ-like love in the world.
- **Universal Guilt**: We are all complicit in each other's sins, and we can only be redeemed through collective love and forgiveness.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الإخوة كارامازوف (The Brothers Karamazov)
**المؤلف:** فيودور دوستويفسكي  
**سنة النشر:** 1880  
**التصنيف الأدبي:** درة الأدب الروسي الفلسفي / دراما نفسية ولاهوتية وجودية  

---

## 1. السياق التاريخي والفلسفي
صدرت رواية *الإخوة كارامازوف* في أواخر عام 1880 قبل أشهر قليلة من وفاة دوستويفسكي، وتعد قمة نتاجه الفكري والأدبي. تدور أحداثها في بلدة روسية ريفية حول صراع عائلة كارامازوف، وتطرح أعمق الأسئلة الوجودية: الإيمان في مواجهة الشك، معضلة الألم وعذاب الأطفال الأبرياء، وحرية الإرادة والمسؤولية الأخلاقية للبشر.

---

## 2. التحليل التفصيلي لمجريات الرواية (كتاباً بكتاب)

### الكتب 1–3: طبيعة آل كارامازوف
- **فيودور بافلوفيتش كارامازوف**: الأب الماجن، البخيل، الفاسق الذي تخلى عن أبنائه الثلاثة ويعيش في انحلال تام.
- **الإخوة الثلاثة**:
  - **ديمتري (ميتيا)**: الابن الأكبر، جندي سابق تحركه العواطف الجياشة والشهوات، لكنه يملك ضميراً نبيلاً. يشتعل بينه وبين والده صراع على الميراث وعلى حب امرأة فاتنة تدعى غروشينكا.
  - **إيفان**: الابن الأوسط، مثقف عبقري، عقلاني ملحد يعذبه الشك الميتافيزيقي والتمرد الفلسفي.
  - **أليوشا**: الابن الأصغر، راهب مبتدئ نقي السريرة، تلميذ القديس الروحي الشيخ زوسيما، يمثل المحبة والصفاء.
- **بافيل سميردياكوف**: الخادم المصاب بالصرع، ويُعتقد أنه الابن غير الشرعي للأب من امرأة متخلفة عقلياً.

### الكتب 4–6: التمرد والمفتش العام
- **حوار الحانة والتمرد**: يلتقي إيفان بأليوشا في حانة، ويعلن إيفان أنه لا ينكر وجود الله، بل يرفض "العالم الذي خلقه الله" بسبب عذاب الأطفال الأبرياء الذي لا يمكن لأي جنة أن تعوضه.
- **قصيدة المفتش العام (The Grand Inquisitor)**: تحفة إيفان الفلسفية؛ يتخيل عودة المسيح في إشبيلية إبان محاكم التفتيش. يعتقله المفتش العجوز ذو التسعين عاماً، ويواجهه في زنزانته قائلاً: إنك منحت البشر حرية الاختيار، والبشر ضعفاء لا يطيقون الحرية ويفضلون الخبز والمعجزات والسلطة. لا يرد المسيح بكلمة، بل يقبل شفتي العجوز في صمت.
- **تعاليم الشيخ زوسيما**: يقدم الراهب زوسيما البديل الإيماني: محبة الخلق أجمعين، وممارسة المحبة الفعالة، وأن *"كل إنسان مسؤول عن كل إنسان وعن كل خطيئة في الأرض"*.

### الكتب 7–9: مقتل الأب والاعتقال
- **رائحة الفساد**: بعد وفاة زوسيما، يتعفن جسده سريعاً بدلاً من حدوث معجزة، فيهتز إيمان أليوشا مؤقتاً قبل أن يستعيده برؤيا عرس قانا الجليل.
- **ليلة الجريمة المروعة**: بدافع الغيرة الجنونية، يذهب ديمتري لبيت والده باحثاً عن غروشينكا، ويضرب الخادم غريغوري ويهرب ملطخاً بالدماء. يغتنم سميردياكوف الفرصة ويقتل الأب ويسرق 3000 روبل ويلفق التهمة لديمتري. يُعتقل ديمتري أثناء احتفاله مع غروشينكا في موكرويه.

### الكتب 10–12: المحاكمة، الجنون، والنهاية
- **اعتراف سميردياكوف وجنون إيفان**: يعترف سميردياكوف لإيفان سراً بأنه القاتل الفعلي، لكنه يرمي بالمسؤولية الأخلاقية على إيفان لأن إيفان روج لمقولة: *"إذا لم يكن هناك إله، فكل شيء مباح"*. يصاب إيفان بالحمى والجنون ويهلوس بشيطان يزوره في غرفته، وينتحر سميردياكوف شنقاً.
- **المحاكمة**: رغم مرافعة المحامي البارعة، تدين هيئة المحلفين ديمتري بقتل والده ويُحكم عليه بالأشغال الشاقة في سيبيريا.
- **الخاتمة**: يخطط ديمتري للهرب، وتنتهي الرواية بخطاب أليوشا المؤثر للأطفال عند قبر الطفل إليوشا مؤكداً حقيقة البعث والمحبة الخالدة.

---

## 3. الرموز والدروس الكبرى
- **مقولة إيفان**: سقوط الرادع الإلهي يفتح الباب للفوضى والعدمية والقتل.
- **صراع ديمتري**: الإنسان كائن معقد يتسع صدره لمثال العذراء ومثال سدوم في آن واحد.
- **المسؤولية الأخلاقية الشاملة**: كلنا شركاء في خطايا العالم، وخلاص البشرية يبدأ بالتوبة والمحبة الفعالة.
"""
    },

    # 18 White Nights
    {
        "id": "18_White_Nights",
        "content_en": """# Comprehensive Study Guide: White Nights
**Author:** Fyodor Dostoevsky  
**Year:** 1848  
**Genre:** Sentimental Fiction / Romantic Melancholy  

---

## 1. Context & Premise
Written during Dostoevsky's early period before his Siberian imprisonment, *White Nights* is set against the luminous, twilight "white nights" of St. Petersburg in June. It is a lyrical meditation on loneliness, romantic daydreaming, and the fleeting nature of happiness.

---

## 2. In-Depth Night-by-Night Breakdown
- **First Night (The Meeting)**: The 26-year-old unnamed narrator wanders the canals of St. Petersburg at midnight. A chronic loner and hopeless daydreamer, he meets Nastenka, a young woman weeping by the canal railing, and protects her from an aggressive drunk. They agree to meet the next evening on condition that he does not fall in love with her.
- **Second Night (The Dreamer's Confession & Nastenka's Story)**: The narrator explains his existence as a "dreamer," living entirely in vivid interior fantasies because reality is too cold. Nastenka shares her story: raised by her strict, half-blind grandmother who pins her dress to hers, she fell in love with a lodger who promised to return for her exactly one year later. That year has passed, and she is desperately awaiting his arrival.
- **Third Night (Doubt and Agony)**: The lodger fails to appear or write. Nastenka weeps, comforted by the narrator who suppresses his deep, consuming love for her to preserve her emotional peace.
- **Fourth Night (The Resolution)**: Giving up hope, Nastenka accepts the narrator's love, promising to spend her life with him. Just as they walk home, the lodger suddenly reappears. Nastenka rushes into the lodger's arms, kisses the narrator on the lips in bittersweet farewell, and leaves with her true love.
- **The Morning**: The narrator receives a tender letter from Nastenka apologizing and praying for his happiness. Looking at his dingy room, he utters the immortal closing reflection: *"A whole minute of bliss! Is that not enough, even for an entire human life?"*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الليالي البيضاء (White Nights)
**المؤلف:** فيودور دوستويفسكي  
**سنة النشر:** 1848  
**التصنيف الأدبي:** أدب عاطفي / نوستالجيا رومانسية حزينة  

---

## 1. السياق والموضوع الجوهري
كتب دوستويفسكي هذه التحفة القصيرة في مرحلة شبابه المبكرة قبل نفيه لسيبيريا. تدور أحداثها في ليالي بطرسبرغ الصيفية البيضاء حيث لا يغيب الشفق ليلاً. الرواية مرثية رقيقة لعزلة الإنسان المعاصر وهروبه إلى أحلام اليقظة، وبحثه المستميت عن لحظة صدق ودفء إنساني.

---

## 2. التسلسل التفصيلي للأحداث (ليلة بليلة)
- **الليلة الأولى (اللقاء)**: يتجول الراوي الشاب (26 عاماً) وحيداً عند قنوات بطرسبرغ في منتصف الليل. يلتقي بفتاة حسناء تدعى "ناستينكا" تبكي عند حافة الجسر، وينقذها من متحرش مخمور. يتفقان على اللقاء في الليلة التالية بشرط ألا يقع في حبها.
- **الليلة الثانية (قصة الحالم وقصة ناستينكا)**: يعترف الراوي بأنه "حالم" يعيش في عالم خيالي صنعه بنفسه ليعوض وحشة الواقع. وتروي ناستينكا مأساتها: تعيش مع جدتها العمياء الصارمة التي تثبت فستانها بدبوس مع ثوبها، وقد أحبت مستأجراً شاباً وعدها بالعودة للزواج منها بعد عام كامل، وقد انقضى العام ولم يظهر.
- **الليلة الثالثة (لوعة الانتظار)**: لا يحضر الحبيب، وتغرق ناستينكا في البكاء، بينما يكتم الراوي حبه العارم ليواسيها بأخوة مخلصة.
- **الليلة الرابعة (الذروة والفراق)**: بعد أن تفقد ناستينكا الأمل، تعترف للراوي بأنها مستعدة لمنحه قلبها والزواج منه. وبينما يسيران في نشوة، يظهر الحبيب الغائب فجأة. تطير ناستينكا إلى ذراعيه، وتقبل الراوي قبلة وداع ممتنة وتغادر مع حبيبها.
- **الصباح الخاتم**: يتلقى الراوي رسالة رقيقة من ناستينكا تطلب منه مسامحتها وتتمنى له السعادة. ينظر إلى غرفته الكئيبة ويختم بتأمله الخالد: *"دقيقة كاملة من النعيم! ألا تكفي هذه الدقيقة حياة إنسان كاملة؟"*.
"""
    },

    # 19 War and Peace
    {
        "id": "19_War_And_Peace",
        "content_en": """# Comprehensive Study Guide: War and Peace
**Author:** Leo Tolstoy  
**Year:** 1869  
**Genre:** Epic Historical Fiction / Philosophy of History  

---

## 1. Context & Scale
Leo Tolstoy's magnum opus depicts Russian society through the Napoleonic invasion of 1812. Encompassing hundreds of historical and fictional characters across five aristocratic families (Bezukhov, Bolkonsky, Rostov, Kuragin, Drubetskoy), the novel is both an intimate human chronicle and a monumental philosophy of history: Tolstoy argues that history is not driven by "great men" (like Napoleon), but by the aggregate, unconscious actions of millions of ordinary people.

---

## 2. In-Depth Narrative Breakdown
- **Peace (1805–1811)**: Pierre Bezukhov, the illegitimate, socially awkward son of a wealthy count, inherits an immense fortune. He makes a disastrous marriage to the beautiful, shallow Helene Kuragina. Prince Andrei Bolkonsky, seeking military glory, fights at Austerlitz, where he is wounded gazing up at the infinite blue sky, realizing the vanity of Napoleon's ambitions. Andrei falls in love with the vibrant young Natasha Rostova, but their engagement is fractured when the rake Anatole Kuragin attempts to abduct her.
- **War (1812: The French Invasion)**: Napoleon marches the Grande Armee into Russia. Andrei rejoins the army and is mortally wounded at the bloody Battle of Borodino. Natasha nurses him tenderly until his peaceful death.
- **The Burning of Moscow & Spiritual Transformation**: Pierre remains in occupied Moscow intending to assassinate Napoleon, but is arrested. In prison, he meets Platon Karataev, a simple peasant whose unshakeable faith and organic harmony with life transform Pierre's soul.
- **Resolution**: The harsh Russian winter and Kutuzov's patient guerrilla strategy destroy the retreating French army. Pierre marries Natasha, finding serene domestic fulfillment.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الحرب والسلام (War and Peace)
**المؤلف:** ليو تولستوي  
**سنة النشر:** 1869  
**التصنيف الأدبي:** ملحمة تاريخية وأدبية كبرى / فلسفة حركة التاريخ  

---

## 1. السياق والمفهوم الملحمي
تعد رواية *الحرب والسلام* أعظم ملحمة روائية كُتبت في التاريخ البشري؛ تصور المجتمع الروسي إبان الغزو النابليوني عام 1812 عبر تتبع مصائر عائلات أرستقراطية كبرى (بيزوخوف، بولكونسكي، روستوف). لا يكتفي تولستوي بالسرد القصصي، بل يطرح فلسفة تاريخية عميقة تثبت أن التاريخ لا يصنعه "الزعماء العظام" كنابليون، بل هو حركة حتمية تنبع من التراكم العفوي لإرادات ملايين البشر البسطاء.

---

## 2. التسلسل الدرامي لمجريات الملحمة
- **عالم السلام (1805–1811)**: بيير بيزوخوف، الشاب الضخم المتردد، يرث ثروة والده الطائلة فجأة ويتزوج من الفاتنة الخائنة هيلين كوراجينا. الأمير أندريه بولكونسكي يذهب للحرب طمعاً في المجد العسكري، فيصاب في معركة أوسترليتز وينظر لسماء الخلود مدركاً تفاهة طموح نابليون. يقع أندريه في حب ناتاشا روستوفا المفعمة بالحياة، لكن خطبتهما تنهار بمكيدة من الفاسق أناتول.
- **عالم الحرب (غزو 1812)**: يقتحم نابليون الأراضي الروسية بجيشه الجرار. يُصاب الأمير أندريه إصابة مميتة في معركة بورودينو، وتتولى ناتاشا تمريضه بندم وحب حتى يفيض روحه في سلام روحي.
- **حريق موسكو والتحول الروحي**: يقرر بيير البقاء في موسكو المحتلة لاغتيال نابليون، فيُقبض عليه ويُساق أسيراً. يلتقي في الأسر بالفلاح البسيط بلاتون كاراتاييف، الذي يتعلم منه التناغم الطبيعي مع الحياة والإيمان الفطري الخالص.
- **الخاتمة**: يهلك الشتاء الروسي القارس جيش نابليون المنسحب، وينتصر الصبر الروسي بقيادة كوتوزوف. يتزوج بيير من ناتاشا ويجدان السكينة الحقيقية في العائلة والاستقامة الروحية.
"""
    },

    # 20 Anna Karenina
    {
        "id": "20_Anna_Karenina",
        "content_en": """# Comprehensive Study Guide: Anna Karenina
**Author:** Leo Tolstoy  
**Year:** 1877  
**Genre:** Realist Fiction / Tragedy / Social Critique  

---

## 1. Core Thesis & Contrasting Plots
*"All happy families are alike; each unhappy family is unhappy in its own way."*  
Tolstoy constructs a dual-narrative masterpiece contrasting two emotional trajectories:
1. **Anna Karenina and Count Vronsky**: An adulterous, all-consuming, destructive passion rooted in societal vanity and physical desire.
2. **Konstantin Levin and Kitty Shcherbatskaya**: A slow, patient, grounded love culminating in marriage, agrarian labor, and spiritual redemption.

---

## 2. Major Plot Arcs & Tragedy
- **The Affair**: Anna Karenina, charming and high-society, is married to Alexei Karenin, a cold, pious, high-ranking bureaucrat. Visiting Moscow to reconcile her brother Stiva and his wife Dolly, Anna meets Count Alexei Vronsky, a dashing cavalry officer. A scandalous romance ensues.
- **The Social Ostracization**: Anna becomes pregnant with Vronsky's child, confesses her infidelity to her husband, and leaves her beloved son Seryozha to live with Vronsky abroad. While high society tolerates Vronsky's transgressions, Anna is ruthlessly cast out and humiliated by Petersburg society.
- **The Spiral and Suicide**: Isolated in the countryside, Anna's mental state deteriorates into jealous paranoia and morphia addiction. Convinced Vronsky has fallen out of love with her, she travels to the Nizhny Novgorod railway station and throws herself beneath the wheels of an oncoming freight train.
- **Levin's Spiritual Epiphany**: Alongside Anna's tragedy runs Levin's search for meaning. Working the land alongside Russian peasants, Levin experiences a profound spiritual revelation: life's purpose is not intellectual pride, but living for the soul and for God.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: آنا كارينينا (Anna Karenina)
**المؤلف:** ليو تولستوي  
**سنة النشر:** 1877  
**التصنيف الأدبي:** الواقعية الروسية / تراجيديا اجتماعية ونفسية  

---

## 1. الفلسفة ومفارقة الخطين الدراميين
تبدأ الرواية بالجملة الخالدة: *"كل العائلات السعيدة تتشابه، أما العائلات التعيسة فلكل منها تعاستها الخاصة"*. يبني تولستوي روايته على خطين متوازيين متناقضين:
1. **خط آنا كارينينا وفيرونسكي**: عشق عاصف غير شرعي، محكوم بالشهوة والمظاهر الاجتماعية، ينتهي بالتدمير الذاتي والانتحار.
2. **خط قسطنطين ليفين وكيتي**: حب هادئ متزن، ينضج بالصبر وينتهي بزواج مستقر وعمل زراعي والارتقاء الروحي نحو الإيمان.

---

## 2. المسار الدرامي والتراجيديا
- **بداية العاصفة**: آنا كارينينا سيدة مجتمع ساحرة متزوجة من أليكسي كارينين، رجل الدولة الصارم البارد. تسافر لموسكو للإصلاح بين أخيها وزوجته، فتلتقي بالضابط الشاب الوسيم فرونسكي وتشتعل بينهما عاطفة جارفة تفضحها أمام المجتمع المخملي.
- **النبذ الاجتماعي والانهيار**: تترك آنا زوجها وابنها الحبيب سيريوجا وتعيش مع فرونسكي. يعاقب المجتمع الطبقي المنافق آنا بالنبذ التام بينما يسامح فرونسكي كرجل.
- **النهاية المأساوية**: تغرق آنا في نوبات الشك والغيرة وإدمان المورفين، وتظن أن فرونسكي سئم منها؛ فترمي بنفسها تحت عجلات القطار في محطة السكة الحديد.
- **خلاص ليفين**: بالتوازي، يكتشف ليفين (المعبر عن روح تولستوي) معنى الوجود من خلال العمل في الأرض مع الفلاحين والإيمان بالبساطة والخير الإلهي.
"""
    },

    # 21 The Master and Margarita
    {
        "id": "21_The_Master_And_Margarita",
        "content_en": """# Comprehensive Study Guide: The Master and Margarita
**Author:** Mikhail Bulgakov  
**Written:** 1928–1940 (Published 1967)  
**Genre:** Magical Realism / Political Satire / Philosophical Fantasy  

---

## 1. Historical & Political Context
Written secretly in Stalinist Moscow during the Great Purges, Mikhail Bulgakov hid the manuscript until his death, knowing it meant execution. Published decades later in 1967, it remains one of the greatest satires of state censorship, bureaucratic cowardice, and militant atheism ever written.

---

## 2. The Three Interwoven Narrative Strands

1. **Woland's Chaos in Moscow**: Satan (disguised as the foreign professor Woland) arrives in 1930s Moscow with his bizarre demonic retinue: Behemoth (a giant, talking, gun-toting black cat), Koroviev (the checkered choirmaster), Azazello, and Hella. They wreak hilarious and terrifying havoc on corrupt Soviet bureaucrats, theatrical elites, and the state-controlled writers' union (MASSOLIT).
2. **The Story of Pontius Pilate**: The Master’s rejected historical novel details the psychological torment of Roman procurator Pontius Pilate, who condemns Yeshua Ha-Nozri (Jesus) to death despite knowing he is innocent, paralyzed by political cowardice.
3. **The Master and Margarita**: The Master, a broken novelist whose book on Pilate was banned by Soviet censors, languishes in an insane asylum. His devoted lover, Margarita, strikes a pact with Woland to save him. She transforms into a witch, flies over Moscow on a broomstick, serves as Queen at Satan's Grand Midnight Ball, and frees the Master. Woland utters the immortal phrase: *"Manuscripts don't burn!"* (*Rukopisi ne goryat!*).
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: المعلم ومارغريتا (The Master and Margarita)
**المؤلف:** ميخائيل بولغاكوف  
**سنة التأليف:** 1928–1940 (نُشرت 1967)  
**التصنيف الأدبي:** الواقعية السحرية / السخرية السياسية / الفانتازيا الفلسفية  

---

## 1. السياق التاريخي والسياسي
كُتبت هذه التحفة سراً في موسكو الستالينية في ذروة حملات القمع والتطهير الكبرى. كان بولغاكوف يدرك أن اكتشاف المخطوطة يعني إعدامه فوراً، فظلت حبيسة الأدراج حتى نُشرت عام 1967. تعد الرواية أعظم نقد ساخر للبيروقراطية السوفيتية، والرقابة الفكرية، والإلحاد القسري للدولة.

---

## 2. الخيوط الدرامية الثلاثة المتشابكة

1. **فوضى فولاند في موسكو**: يصل الشيطان متنكراً في شخصية البروفيسور "فولاند" بصحبة حاشيته الشيطانية العجيبة: القط الضخم الناطق "بيهيموث" الذي يحمل مسدساً ويشرب الفودكا، والمهرج كوروفييف، وأزازيلو. ينزلون بموسكو ليقلبوا حياة كبار البيروقراطيين والانتهازيين في اتحاد الكتاب السوفيتي رأساً على عقب في مشاهد هزلية مرعبة.
2. **رواية بيلاطس البنطي**: وهي الرواية التي ألفها "المعلم"؛ تتناول العذاب النفسي للحاكم الروماني بيلاطس البنطي الذي يحكم على "يشوع الغمري" (المسيح) بالإعدام رغم يقينه ببراءته، بسبب الجبن السياسي والخوف على منصبه.
3. **عشق مارغريتا والتحرر**: يودع "المعلم" مستشفى المجانين بعد منع روايته، فتعقد حبيبته المخلصة مارغريتا صفقة مع الشيطان لإنقاذه. تتحول إلى ساحرة، وتطير فوق موسكو، وتترأس حفل الشيطان السنوي الأسطوري، ليعيد لها فولاند حبيبها ومخطوطته المنقذة، قائلاً جملته الخالدة: *"المخطوطات لا تحترق!"*.
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
