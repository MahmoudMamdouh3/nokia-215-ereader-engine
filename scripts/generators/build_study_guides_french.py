"""
Generates master-level study guides for French Literature masterpieces:
- 22_In_Search_Of_Lost_Time_Swanns_Way
- 23_Les_Miserables
- 24_Madame_Bovary
- 25_The_Stranger
- 26_The_Little_Prince
- 27_The_Red_And_The_Black
- 66_Journey_To_The_End_Of_The_Night
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 22 Swann's Way
    {
        "id": "22_In_Search_Of_Lost_Time_Swanns_Way",
        "content_en": """# Comprehensive Study Guide: In Search of Lost Time: Swann's Way (Du côté de chez Swann)
**Author:** Marcel Proust  
**Year:** 1913  
**Genre:** Modernist Epic / Involuntary Memory / Psychological Fiction  

---

## 1. Context & Literary Revolution
The monumental opening volume of Proust's seven-part masterpiece *À la recherche du temps perdu*. Proust fundamentally revolutionized modern literature by shifting focus from external plot events to internal consciousness, time perception, and involuntary memory (*mémoire involontaire*).

---

## 2. In-Depth Structural Analysis

### Part I: Combray (The Architecture of Memory)
- **The Bedtime Drama**: The neurotic, sensitive young narrator recalls childhood evenings at the family estate in Combray. His mother's bedtime kiss is the emotional center of his world. One evening, wealthy family friend Charles Swann visits for dinner, depriving the boy of his mother's kiss and throwing him into emotional agony.
- **The Episode of the Madeleine**: Decades later as an adult, the narrator dips a petite madeleine pastry into a spoonful of lime-blossom tea. The sensory taste instantly unlocks a forgotten flood of vivid childhood memories—the entire village of Combray, its church spire, gardens, and streets resurrected like Japanese paper flowers expanding in water.
- **The Two "Ways"**:
  - *Méséglise Way (Swann's Way)*: Symbolizing nature, passion, sensuality, and bourgeois intellect.
  - *Guermantes Way*: Symbolizing aristocratic power, social climbing, and unattainable elegance.

### Part II: Swann in Love (Un amour de Swann)
A devastating psychological novella recounting Charles Swann's obsessive passion for Odette de Crécy years before the narrator was born. Initially unimpressed by Odette, Swann becomes ensnared by jealousy, paranoia, and social vanity, especially through Vinteuil's musical sonata. Swann realizes in despair: *"To think that I've wasted years of my life, that I've longed to die, for a woman who didn't please me, who wasn't in my style!"*

### Part III: Place-Names: The Name
The narrator explores his childhood daydreams of exotic travel destinations (Venice, Florence, Balbec) and his early romantic infatuation with Gilberte Swann in the gardens of the Champs-Élysées.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: طرف منزل سوان (البحث عن الزمن المفقود)
**المؤلف:** مارسيل بروست (Marcel Proust)  
**سنة النشر:** 1913  
**التصنيف الأدبي:** الأدب الحداثي العالمي / تيار الوعي / فلسفة الذاكرة والزمن  

---

## 1. السياق والثورة الأدبية لبروست
يمثل هذا المجلد الافتتاحية الكبرى لملحمة بروست السباعية *البحث عن الزمن المفقود*. أحدث بروست ثورة في الرواية الحديثة؛ محولاً مركز الثقل من تتابع الأحداث الخارجية إلى سراديب الوعي الإنساني، وإدراك الزمن النفسي، وفلسفة "الذاكرة اللاإرادية".

---

## 2. التحليل التفصيلي للأجزاء الثلاثة

### الجزء الأول: كومبريه وهندسة الذاكرة
- **دراما قبلة النوم**: يسترجع الراوي الحساس ذكريات طفولته في بلدة كومبريه؛ حيث كانت قبلة أمه قبل النوم محور أمانه العاطفي. في إحدى الأمسيات يزورهم الصديق الثري شارل سوان لتناول العشاء، فيُحرم الطفل من قبلة أمه ويغرق في لوعة نفسية عاصفة.
- **لحظة كعكة المادلين الأسطورية**: بعد عقود، يغمس الراوي البالغ قطعة كعك "مادلين" في فنجان شاي زهر الليمون؛ فتعيد تلك النكهة فجأة وبلا سابق إنذار كل ذكريات الطفولة المنسية، وتنبثق بلدة كومبريه وكنيستها وحدائقها حية كأزهار ورقية يابانية تتفتح في الماء.
- **طريقا كومبريه**:
  - *طريق سوان*: يرمز للطبيعة، والشغف، والبرجوازية المثقفة.
  - *طريق غيرمانت*: يرمز للأرستقراطية القديمة، والجاه، والطبقات المخملية.

### الجزء الثاني: حب سوان
رواية نفسية عبقرية داخل الرواية؛ تروي قصة هوس شارل سوان بسيدة المجتمع أوديت دي كريسي قبل مولد الراوي. لم تكن أوديت تعجب سوان في البداية، لكن الغيرة والشكوك العاصفة حولتا إعجابه إلى جحيم نفسي خانق، خصوصاً عندما يسمع مقطوعة فانتوي الموسيقية. ويصرخ سوان في النهاية بمرارة: *"يا إلهي، لقد ضيعت سنوات من عمري وكدت أموت حزناً من أجل امرأة لم تكن حتى من ذوقي!"*.

### الجزء الثالث: أسماء الأماكن: الاسم
تأملات الراوي في سحر الأسماء والمدن التي يحلم بزيارتها (البندقية، فلورنسا)، وبدايات حبه الطفولي لجيلبرت سوان في حدائق الشانزلزيه.
"""
    },

    # 23 Les Miserables
    {
        "id": "23_Les_Miserables",
        "content_en": """# Comprehensive Study Guide: Les Misérables
**Author:** Victor Hugo  
**Year:** 1862  
**Genre:** Epic Historical Realism / Romantic Humanitarianism  

---

## 1. Social Context & Epic Purpose
Written over two decades, Victor Hugo's epic is a passionate indictment of poverty, social inequality, and the penal system in 19th-century post-Napoleonic France. Hugo declared: *"So long as there shall exist, by reason of law and custom, a social condemnation creating artificial hells on earth... books like this cannot be useless."*

---

## 2. In-Depth Character Arcs & Plot
- **Jean Valjean's Redemption**: Valjean, imprisoned for 19 years in the galleys for stealing a loaf of bread to feed his starving sister's family, is released hardened by hatred. When kindly Bishop Myriel feeds him, Valjean steals the bishop's silver plates. Captured by police, the Bishop saves Valjean by telling them the silver was a gift and presents him with two silver candlesticks, saying: *"Jean Valjean, my brother, you belong no longer to evil, but to good. It is your soul that I am buying for you."* Valjean vows to become an honest man.
- **Fantine and Cosette**: Valjean reinvents himself as Monsieur Madeleine, a wealthy industrialist and mayor of Montreuil-sur-Mer. He rescues Fantine, an impoverished mother forced into prostitution by poverty, and promises to care for her abused daughter Cosette, enslaved by the villainous Thénardiers.
- **The Nemesis (Inspector Javert)**: Javert, the relentless embodiment of cold, inflexible legal justice, pursues Valjean across decades.
- **The Barricades of 1832**: During the Paris June Rebellion of 1832, Marius Pontmercy falls in love with the grown Cosette. Valjean goes to the bloody student barricades to protect Marius, spares Javert's life when students capture him as a spy, and carries the mortally wounded Marius to safety through the labyrinthine sewers of Paris.
- **Javert's Suicide**: Unable to reconcile his black-and-white legalism with the moral debt he owes to a convicted felon who showed him mercy, Javert drowns himself in the River Seine. Valjean dies peacefully surrounded by Marius and Cosette beneath the light of the bishop's silver candlesticks.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: البؤساء (Les Misérables)
**المؤلف:** فيكتور هوغو (Victor Hugo)  
**سنة النشر:** 1862  
**التصنيف الأدبي:** الواقعية الملحمية / الأدب الإنساني والاجتماعي  

---

## 1. السياق الاجتماعي والرسالة الإنسانية
تعد رواية *البؤساء* صرخة فيكتور هوغو الكبرى في وجه الفقر والظلم الاجتماعي وقسوة القوانين الطبقية في فرنسا ما بعد نابليون. يلخص هوغو رسالته قائلاً: *"طالما وُجد في الأرض جهل وفقر ينشئان جحيماً مصطنعاً على الأرض... فإن كتباً كهذا الكتاب لن تكون بلا جدوى"*.

---

## 2. المسار الدرامي وتحولات الشخصيات
- **خلاص جان فالجان**: يقضي جان فالجان 19 عاماً في الأشغال الشاقة لسرقته رغيف خبز لإطعام أطفال أخته الجائعين. يخرج بقلب أسود يملؤه الحقد؛ لكن الأسقف النبيل ميريل يطعمه ويأويه. يسرق فالجان فضيات الأسقف، وحين يقبض عليه الحرس، ينقذه الأسقف قائلاً إنه وهبه الفضيات ويزيده شمعدانين فضيين: *"يا أخي جان فالجان، لقد اشتريت روحك من الشر ووهبتها لله وللخير"*.
- **مأساة فانتين وكوزيت**: يغير فالجان هويته ويصبح مصلحاً وصناعياً ثرياً وعمدة محبوباً. ينقذ فانتين، الأم المطحونة التي باعت شعرها وأسنانها لتطعم ابنتها كوزيت عند عائلة تيناردييه الجشعة، ويعاهدها على حماية طفلتها.
- **المحقق جافير (تجسيد القانون الأعمى)**: يلاحق جافير فالجان لعقود بعناد قاطع، مؤمناً بأن المجرم يظل مجرماً ولا خلاص له.
- **متاريس ثورة 1832 ومجاري باريس**: في خضم تمرد الطلاب بباريس، يقع الشاب ماريوس في حب كوزيت. يذهب فالجان للمتاريس لحماية ماريوس، ويعفو عن جافير حين يقع في الأسر، وينقذ ماريوس الجريح بحمله عبر شبكة مجاري باريس المظلمة.
- **انتحار جافير ووفاة فالجان**: يصاب جافير بانهيار فكري حاد؛ إذ يعجز عقله القانوني الصارم عن استيعاب نبل هذا المحكوم السابق الذي عفا عنه، فيلقي بنفسه في نهر السين منتحراً. يموت جان فالجان بسلام في أحضان كوزيت وماريوس على ضوء الشمعدانين الفضيين.
"""
    },

    # 24 Madame Bovary
    {
        "id": "24_Madame_Bovary",
        "content_en": """# Comprehensive Study Guide: Madame Bovary
**Author:** Gustave Flaubert  
**Year:** 1857  
**Genre:** Realist Fiction / Critique of Romanticism  

---

## 1. Context & Le Mot Juste
Gustave Flaubert spent five agonizing years crafting *Madame Bovary*, pursuing *le mot juste* (the exact word) and impassive artistic objectivity. When published, Flaubert was prosecuted for obscenity by the French government. The novel introduced "Bovarysme"—the psychological delusion of projecting romantic escapist fantasies onto mediocre reality.

---

## 2. In-Depth Chapter Breakdown
- **Emma's Romantic Conditioning**: Emma Rouault, educated in a convent reading sentimental romance novels, dreams of aristocratic passion, luxury, and whirlwind romance. She marries Charles Bovary, a devoted but dull and unimaginative country doctor.
- **The Ball at La Vaubyessard**: An invitation to an aristocratic ball gives Emma a brief taste of high society, plunging her into deep depression when she returns to boring provincial Yonville.
- **The Affairs**:
  - *Léon Dupuis*: A young law clerk who shares her romantic daydreams, though their initial encounter remains unconsummated when he leaves for Paris.
  - *Rodolphe Boulanger*: A wealthy, cynical local aristocrat who easily seduces Emma. When Emma begs him to elope with her, Rodolphe deserts her with a cowardly farewell letter.
  - *Reunion with Léon*: Emma encounters Léon in Rouen and starts a reckless, expensive affair in hotel rooms, neglecting her daughter Berthe.
- **Financial Ruin and Arsenic**: Manipulated by the predatory merchant Lheureux, Emma accumulates massive debts to buy luxury gifts. Faced with financial bankruptcy, public seizure of Charles's property, and abandonment by both lovers, Emma swallows white arsenic from Homais's pharmacy, suffering an agonizing, grotesque death.
- **Aftermath**: Charles discovers her love letters, forgives her in grief, and dies of a broken heart, leaving their young daughter destitute in a cotton mill.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: مدام بوفاري (Madame Bovary)
**المؤلف:** غوستاف فلوبير (Gustave Flaubert)  
**سنة النشر:** 1857  
**التصنيف الأدبي:** الواقعية النقدية / هجاء الرومانسية الزائفة  

---

## 1. السياق وفلسفة فلوبير (الكلمة الدقيقة)
قضى فلوبير خمس سنوات مضنية في كتابة *مدام بوفاري* باحثاً عن "الكلمة الدقيقة" (Le mot juste) والحياد الفني الصارم. حوكم فلوبير بتهمة خدش الحياء العام، وابتكرت الرواية مصطلح "البوفارية" (Bovarysme)؛ وهو الوهم النفسي المتمثل في الهروب من الواقع إلى خيالات رومانسية مستحيلة.

---

## 2. التحليل التفصيلي لمسار المأساة
- **أوهام إيما الرومانسية**: نشأت إيما في دير تقرأ الروايات العاطفية الساذجة، وتحلم بالفرسان والقصور والحب الملتهب. تتزوج من شارل بوفاري، الطبيب الريفي الطيب المخلص لكنه بليد وخالٍ تماماً من الطموح والشاعرية.
- **حفلة قصر فوبيسار**: دعوة واحدة لحفلة راقصة في قصر أرستقراطي تذيق إيما طعم الثراء، فتعود لبيتها الريفي في إيونفيل لتغرق في اكتئاب حاد وازدراء لزوجها المسكين.
- **العلاقات المحرمة**:
  - *ليون ديبوي*: كاتب قانوني شاب يشاركها شغف الأدب، تفترق عنه ثم تلتقي به لاحقاً في روان لتبدأ معه علاقة عاطفية مكلفة.
  - *رودولف بولانجييه*: أرستقراطي ثري ولعوب، يغويها بسهولة. وعندما تطالبه بالهرب معها بعيداً، يهرب بمفرده تاركاً لها رسالة وداع جبانة تودي بها إلى المرض.
- **الخراب المالي والزرنيخ**: تقع إيما في شباك التاجر المرابي لورو، وتغرق في ديون طائلة لشراء هدايا وأثاث فاخر. وعند صدور حكم الحجز القضائي على منزل زوجها، وتخلي عشاقها عنها، تبتلع الزرنيخ الأبيض من صيدلية أوميه لتموت ميتة شنيعة تتلوى فيها ألماً.
- **النهاية**: يكتشف شارل رسائل خيانتها، لكنه يسامحها بحزن ويموت كمداً، لتنتهي طفلتهما الصغيرة بالعمل الشاق في مصنع غزل للقطن.
"""
    },

    # 25 The Stranger
    {
        "id": "25_The_Stranger",
        "content_en": """# Comprehensive Study Guide: The Stranger (L'Étranger)
**Author:** Albert Camus  
**Year:** 1942  
**Genre:** Existentialism / Absurdism / Philosophical Novella  

---

## 1. Philosophical Framework: The Philosophy of the Absurd
Written in occupied France in 1942, *The Stranger* embodies Camus's philosophy of the **Absurd**—the inevitable collision between the human desire for meaning and the cold, silent, indifferent universe.

---

## 2. In-Depth Chapter Breakdown

### Part I: The Sensory Existence & The Sun
- **The Mother's Death**: The novel begins with the iconic line: *"Aujourd'hui, maman est morte. Ou peut-être hier, je ne sais pas"* (*"Mother died today. Or maybe yesterday; I can't be sure."*). Meursault, a French Algerian shipping clerk, attends his mother's funeral at an old folks' home in Marengo. He displays no grief, drinks coffee, smokes, and doesn't weep.
- **Marie and Raymond**: The day after the funeral, he goes swimming, starts a sexual liaison with former coworker Marie Cardona, and watches a comedy film. He befriends his neighbor Raymond Sintès, a pimp, and agrees to write a letter to punish Raymond's unfaithful Arab mistress.
- **The Shooting on the Beach**: Spending a weekend at a beach cottage, Meursault, Raymond, and their friend are confronted by two Arab men. Later, Meursault walks alone onto the blinding, scorching beach. Tormented by the intolerable heat and the sun glinting off an Arab's drawn knife, Meursault fires a revolver once, then shoots four more times into the inert body—*"knocking four times on the door of unhappiness."*

### Part II: The Trial and Condemnation
- **The Trial of the Soul**: In prison, the magistrate waves a crucifix at Meursault, appalled by his lack of remorse. At the trial, the prosecution focuses not on the murder of the Arab, but on Meursault's lack of tears at his mother's funeral. He is condemned to the guillotine not for murder, but for refusing to play society's hypocritical emotional games.
- **The Chaplain's Rage & Liberation**: In his cell awaiting execution, Meursault violently rejects the prison chaplain's religious platitudes. In an explosive epiphany, he accepts the *"benign indifference of the universe"* and wishes for a large crowd of spectators at his execution to greet him with cries of hate.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الغريب (L'Étranger)
**المؤلف:** ألبير كامو (Albert Camus)  
**سنة النشر:** 1942  
**التصنيف الأدبي:** الفلسفة الوجودية / أدب العبث / الرواية الفلسفية  

---

## 1. الإطار الفلسفي: فلسفة العبث
صدرت رواية *الغريب* في عام 1942 في فرنسا المحتلة، لتجسد فلسفة كامو في **العبث**؛ وهو الصدام الحتمي بين رغبة الإنسان الفطرية في البحث عن معنى، وبين صمت الكون وبرودته ولا مبالاته التامة.

---

## 2. التحليل التفصيلي لمجريات الرواية

### الجزء الأول: العالم الحسي وشمس الجزائر الحارقة
- **وفاة الأم**: تفتتح الرواية بالجملة الشهيرة: *"اليوم ماتت أمي. أو ربما أمس، لست أدري"*. ميرسو، موظف فرنسي بسيط في الجزائر العاصمة، يسافر لحضور جنازة أمه في دار المسنين. لا يبكي، ولا يظهر أي حزن مصطنع، ويدخن السجائر ويشرب القهوة بحياد تام.
- **ماري وريمون**: في اليوم التالي للجنازة مباشرة، يذهب للسباحة ويبدأ علاقة مع ماري ويشاهد فيلماً كوميدياً. يصادق جاره ريمون المشبوه ويكتب له رسالة لتأديب عشيقته العربية.
- **الجريمة على الشاطئ**: على شاطئ البحر الملتهب، تقع مشاجرة مع شقيق الفتاة ورفيقه. يمشي ميرسو بمفرده تحت وطأة شمس حارقة تكاد تفتت رأسه، فيواجه العربي الذي يسحب سكيناً يلمع في عينيه. في لحظة هذيان حسّي وضغط شمس ساحق، يطلق ميرسو رصاصة، ثم يتبعها بأربع رصاصات أخرى في الجسد الساكن كأنه *"يدق أربع دقات على باب الشقاء"*.

### الجزء الثاني: المحاكمة والمشنقة والتحرر
- **محاكمة الروح لا الجريمة**: في السجن، يحاول قاضي التحقيق إجباره على التوبة ملوحاً بالصليب في وجهه دون جدوى. في قاعة المحكمة، يتجاهل الادعاء واقعة القتل، ويركز تماماً على برود ميرسو في جنازة أمه! يُحكم عليه بقطع الرأس بالمقصلة ليس لأنه قاتل، بل لأنه رفض النفاق ومجاملة المجتمع بأكاذيب مشاعر مصطنعة.
- **مواجهة القسيس والانفجار الوجودي**: يرفض ميرسو لقاء قس السجن، وحين يصر القس على تلقينه الغفران، ينفجر ميرسو في وجهه بغضب عارم مؤكداً أن الجميع محكوم عليهم بالموت، وأن الحياة عبثية لا معنى لها. وبعد رحيل القس، يستشعر ميرسو السلام التام ويتصالح مع "اللامبالاة العذبة لهذا الكون"، متمنياً حضور حشد غفير عند إعدامه يستقبله بصرخات الكراهية.
"""
    },

    # 26 The Little Prince
    {
        "id": "26_The_Little_Prince",
        "content_en": """# Comprehensive Study Guide: The Little Prince (Le Petit Prince)
**Author:** Antoine de Saint-Exupéry  
**Year:** 1943  
**Genre:** Philosophical Fable / Children's Literature for Adults  

---

## 1. Context & Allegorical Depth
Written in exile in New York during WWII, Saint-Exupéry's poetic fable is an adult meditation disguised as a children's story, lamenting how the rigid utilitarianism of the adult world blinds humanity to true spiritual beauty, love, and friendship.

---

## 2. In-Depth Chapter Breakdown
- **The Sahara Crash**: An aviator stranded in the Sahara Desert after an engine breakdown meets a mysterious little boy with golden hair who asks: *"Please... draw me a sheep!"*
- **Asteroid B-612**: The Prince comes from Asteroid B-612, a planet scarcely bigger than a house, with three miniature volcanoes and threatening baobab trees that must be uprooted daily.
- **The Rose**: The Prince loves a proud, delicate, vain rose that blossomed on his asteroid. Tormented by her demands and insecurities, he leaves his planet to explore the universe.
- **The Adult Planets (Allegories of Grown-Up Folly)**:
  1. *The King*: Demands absolute obedience, claiming authority over everything while ruling an empty realm.
  2. *The Conceited Man*: Wants only praise and applause.
  3. *The Tippler*: Drinks to forget that he is ashamed of drinking.
  4. *The Businessman*: Obsessively counts and owns the stars, mistaking possession for purpose.
  5. *The Lamplighter*: Blindly follows an absurd order without questioning why.
  6. *The Geographer*: Writes massive books about worlds he has never seen because he relies only on explorers.
- **Earth and The Fox**: On Earth, the Prince discovers a garden of 5,000 identical roses, crying that his rose was not unique. But the Fox teaches him the secret of life: **To Tame** (*créer des liens*). By taming one another, they become unique in all the world. The Fox reveals the immortal truth: *"It is only with the heart that one can see rightly; what is essential is invisible to the eye."*
- **The Snake and Departure**: To return to his beloved rose, the Prince allows a venomous yellow desert snake to bite him, leaving his heavy body behind to travel back to his star.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الأمير الصغير (The Little Prince)
**المؤلف:** أنطوان دو سانت إكزوبيري  
**سنة النشر:** 1943  
**التصنيف الأدبي:** أسطورة فلسفية / أدب الرمز والإنسانية  

---

## 1. السياق والبعد الرمزي
كُتبت هذه التحفة في نيويورك أثناء الحرب العالمية الثانية؛ وهي حكاية شعرية فلسفية موجهة للبالغين في ثوب قصة أطفال. تنتقد الرواية المادية الجافة للبالغين الذين يفقدون دهشة الطفولة ويعجزون عن رؤية الجمال الحقيقي والمحبة النقية.

---

## 2. التحليل التفصيلي لمجريات الرحلة الرمزية
- **السقوط في صحراء ساهارا**: طيار يتعطل محرك طائرته في الصحراء، فيفاجأ بطفل ذهبي الشعر يطلب منه فجأة: *"أرجوك.. ارسم لي خروفاً!"*.
- **الكويكب B-612**: موطن الأمير الصغير كويكب متناهي الصغر يحتوي على ثلاثة براكين صغيرة وأشجار باوباب ضخمة يجب اقتلاع جذورها يومياً حتى لا تدمر الكوكب.
- **الوردة الفريدة**: يقع الأمير في حب وردة مغرورة وحساسة تفتحت في كوكبه، لكن كبرياءها وشكوكها تجعله يغادر كوكبه باحثاً عن المعرفة.
- **كواكب البالغين (رموز الحماقة الإنسانية)**:
  1. *الملك*: يتوهم السلطة المطلقة ويحكم كوكباً خالياً.
  2. *المغرور*: لا يسمع إلا عبارات المديح والتصفيق.
  3. *السكير*: يشرب لينسى خجله من الشرب!
  4. *رجل الأعمال*: يعد النجوم ويجمعها ليمتلكها دون فائدة.
  5. *مشعل القناديل*: عبد للأوامر القديمة ينفذها بآلية عمياء.
  6. *الجغرافي*: يدون الأماكن في كتب ضخمة دون أن يراها بنفسه.
- **الأرض وسر الثعلب**: على كوكب الأرض، يرى الأمير بستاناً يضم 5000 وردة تشبه وردته، فيبكي ظناً منه أن وردته كانت عادية. لكن الثعلب الحكيم يعلمه معنى "الترويض" وصنع الروابط العاطفية؛ فالوقت الذي قضيته مع وردتك هو ما جعلها فريدة في الكون. ويكشف له السر الخالد: *"لا يرى المرء جيداً إلا بقلبه؛ فالجوهر الحقيقي تعجز العين المجردة عن رؤيته"*.
- **لدغة الأفعى والعودة**: ليعود لوردته الحبيبة، يسمح الأمير لأفعى صفراء سامة بلدغه ليتخلص من ثقل جسده المادي ويطير بروحه إلى كوكبه الصغير.
"""
    },

    # 27 The Red and the Black
    {
        "id": "27_The_Red_And_The_Black",
        "content_en": """# Comprehensive Study Guide: The Red and the Black (Le Rouge et le Noir)
**Author:** Stendhal (Henri Beyle)  
**Year:** 1830  
**Genre:** Psychological Realism / Social Satire / Bildungsroman  

---

## 1. Political Context & Symbolism of the Title
Set during the Bourbon Restoration (1820s), Stendhal examines the stifling class barriers of French society:
- **The Red**: Represents the military career under Napoleon (glory, republican meritocracy).
- **The Black**: Represents the Catholic clergy (hypocrisy, jesuitical climbing, the only path to advancement for poor, ambitious men under the Restoration).

---

## 2. In-Depth Chapter Breakdown
- **Julien Sorel's Ambition**: The brilliant, impoverished son of a carpenter in Verrières, Julien worships Napoleon in secret while preparing for the priesthood.
- **Madame de Rênal**: Employed as tutor to the children of the pompous mayor Monsieur de Rênal, Julien seduces the pious, gentle Madame de Rênal—partly out of pride and partly out of genuine affection. Discovered, Julien flees to the Seminary of Besançon, where he endures the grim intrigues of envious clerical students.
- **Mathilde de La Mole**: Julien becomes secretary to the aristocratic Marquis de La Mole in Paris. He catches the eye of the Marquis's proud, romantic daughter, Mathilde. Julien calculates his courtship with Machiavellian precision, and Mathilde becomes pregnant. The Marquis is on the verge of granting Julien a noble title and military commission.
- **The Letter and the Crime**: Madame de Rênal, coerced by her priest, writes a devastating letter to the Marquis exposing Julien as an opportunistic fortune hunter. His future shattered, Julien rushes to Verrières, enters the church during mass, and shoots Madame de Rênal twice.
- **The Trial and Guillotine**: Madame de Rênal survives. Imprisoned, Julien sheds all ambition and realizes that Madame de Rênal was the only true love of his life. Defiantly condemning the aristocratic class jury in court, Julien refuses to plead for mercy and is guillotined with calm dignity. Madame de Rênal dies three days later embracing her children.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الأحمر والأسود (The Red and the Black)
**المؤلف:** ستندال (Stendhal)  
**سنة النشر:** 1830  
**التصنيف الأدبي:** الواقعية النفسية / الهجاء السياسي والطبقي  

---

## 1. السياق السياسي ودلالة العنوان
تدور أحداث الرواية في فرنسا خلال حقبة عودة الملكية (عقد 1820). يعبر العنوان عن مساري الصعود الاجتماعي:
- **الأحمر**: يرمز للعسكرية والجيش في عصر نابليون (عصر الشرف والمجد والترقي بالكفاءة).
- **الأسود**: يرمز للكهنوت وسلك الكنيسة (عصر النفاق والارتقاء بالتملق والوصولية في ظل حكم البوربون الرجعي).

---

## 2. التحليل التفصيلي لمأساة جوليان سوريل
- **طموح جوليان سوريل**: شاب عبقري، ابن نجار فقير في بلدة ريفية، يعشق نابليون سراً ويدرس اللاهوت علناً كوسيلة وحيدة للهروب من الفقر والمهانة الطبقية.
- **مدام دي رينال**: يعمل معلماً لأبناء عمدة البلدة، ويقرر إغواء زوجة العمدة النقية "مدام دي رينال" بدافع الانتقام الطبقي وإثبات تفوقه، لكنه يقع في حبها الحقيقي. يفتضح أمره فيهرب لمعهد اللاهوت في بيزانصون ليصطدم بنفاق الكهنة.
- **ماتيلد دي لا مول**: ينتقل لباريس سكرتيراً للماركيز دي لا مول، ويوقع ابنة الماركيز الأرستقراطية المتكبرة "ماتيلد" في حبه بدهاء بارد. تحمل ماتيلد منه، ويوشك الماركيز على منحه لقباً نبيلاً ورتبة عسكرية ليتم الزواج.
- **رسالة الخراب والرصاصتان**: تجبر الكنيسة مدام دي رينال على كتابة رسالة للماركيز تفضح فيها جوليان وتصفه بأنه وصولي يتسلق على ظهور النساء. ينهار طموح جوليان؛ فيسافر كالمجنون لبلدته ويدخل الكنيسة أثناء القداس ويطلق رصاصتين على مدام دي رينال.
- **المحاكمة والمقصلة**: تنجو مدام دي رينال من الموت. في السجن، تسقط عن جوليان كل أوهام الطموح ويكتشف أن مدام دي رينال هي حبه الوحيد الصادق. يرفض استجداء العفو ويفضح نفاق هيئة المحلفين الطبقية، ويُعدم بالمقصلة برأس مرفوع، لتموت حبيبته بعده بثلاثة أيام حسرة عليه.
"""
    },

    # 66 Journey to the End of the Night
    {
        "id": "66_Journey_To_The_End_Of_The_Night",
        "content_en": """# Comprehensive Study Guide: Journey to the End of the Night (Voyage au bout de la nuit)
**Author:** Louis-Ferdinand Céline  
**Year:** 1932  
**Genre:** Picaresque / Dark Satire / Existential Nihilism  

---

## 1. Context & Linguistic Shock
Céline shattered French literary style with his 1932 debut, substituting classical prose with raw, colloquial, spoken street French (*argot*) and visceral punctuation. The novel is an uncompromising, pitch-black journey through the horrors of the 20th century: the trenches of WWI, brutal African colonial exploitation, Detroit Fordist assembly lines, and Parisian slum medicine.

---

## 2. Major Plot Breakdown
- **The Meat Grinder of WWI**: The cynical narrator Ferdinand Bardamu enlists on an impulse, only to find himself trapped in the butchery of World War I. He concludes that the only sane response to war is cowardice and survival. He meets Léon Robinson, a fellow survivor who becomes his haunting, shadowy double throughout his life.
- **Colonial Africa**: Discharged as mentally unfit, Bardamu travels to a French colony in West Africa. He witnesses horrifying colonial greed, malaria, and cruelty before fleeing through the jungle.
- **Fordist America**: Arriving in New York and Detroit, Bardamu works on the Ford assembly line, experiencing the crushing dehumanization of industrial capitalism and prostitution.
- **The Parisian Slums & Robinson's Death**: Returning to France, Bardamu earns a medical degree and opens a practice in a squalid Paris suburb (La Garenne-Rancy), treating impoverished patients for free while observing domestic cruelty, murder schemes, and despair. Robinson becomes entangled in murder and is eventually shot by his furious fiancée Madelon. Bardamu watches him die, sailing down the Seine at night into the pitch-black void.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: سفر إلى آخر الليل (Journey to the End of the Night)
**المؤلف:** لويس فرديناند سيلين (Louis-Ferdinand Céline)  
**سنة النشر:** 1932  
**التصنيف الأدبي:** الواقعية السوداء / الأدب الصعلوكي / العدمية الوجودية  

---

## 1. الصدمة اللغوية والأدبية لسيلين
أحدثت رواية سيلين زلزالاً في الأدب الفرنسي؛ حيث حطم الأسلوب الكلاسيكي واستبدله باللغة المحكية العامية الفظة (Argot) وإيقاع الشارع الصاخب. الرواية رحلة ملحمية شديدة السواد في قلب ويلات القرن العشرين: خنادق الحرب العالمية الأولى، وبشاعة الاستعمار في إفريقيا، ومصانع فورد في ديترويت، وفقر ضواحي باريس.

---

## 2. المسار الدرامي لمحطات الرحلة
- **مفرمة الحرب العالمية الأولى**: يتطوع البطل الساخر "فرديناند باردامو" في الجيش بحماقة عابرة، ليجد نفسه وسط مجزرة الخنادق المروعة. يكتشف أن الجبن والهرب هما الفضيلة العقلانية الوحيدة في مواجهة جنون الحرب. يلتقي هناك بـ "ليون روبنسون" الذي يصبح ظله وقرينه الملازم له طوال حياته.
- **جحيم المستعمرات الإفريقية**: يفر إلى مستعمرة فرنسية في إفريقيا، فيشهد بشاعة الاستغلال الاستعماري والمرض والفساد الأخلاقي في الغابات.
- **أمريكا والرأسمالية الآلية**: يصل لنيويورك ثم ديترويت ليعمل في خطوط تجميع سيارات فورد، كاشفاً كيف تسحق الآلات كرامة الإنسان وتحوله إلى ترس ميكانيكي بلا روح.
- **طبيب الفقراء في باريس ونهاية روبنسون**: يعود لفرنسا ويتخرج طبيباً ليفتح عيادة في ضاحية باريسية بائسة، معالجاً الفقراء ومراقباً جرائمهم ومؤامراتهم المنزلية القاتلة. يتورط روبنسون في مؤامرة قتل وتنتهي حياته برصاصة من خطيبته المنتقمة. يراقب باردامو موت صديقه ويبحر في قارب بنهر السين نحو ظلمة الليل السرمدية التي لا تنتهي.
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
