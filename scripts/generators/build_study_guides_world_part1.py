"""
Generates master-level study guides for World Classics & Sci-Fi (Part 1):
- 51_Brave_New_World
- 52_Dune
- 54_Don_Quixote
- 55_One_Hundred_Years_Of_Solitude
- 56_Love_In_The_Time_Of_Cholera
- 57_The_Trial
- 58_The_Metamorphosis
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 51 Brave New World
    {
        "id": "51_Brave_New_World",
        "content_en": """# Comprehensive Study Guide: Brave New World
**Author:** Aldous Huxley  
**Year:** 1932  
**Genre:** Dystopian Science Fiction / Satire  

---

## 1. Context & Contrast with Orwell's 1984
Unlike Orwell’s vision of totalitarianism maintained by violent fear, pain, and police terror, Aldous Huxley foresaw a far more insidious tyranny: control through pleasure, genetic engineering, ubiquitous consumerism, and chemical contentment (*soma*). Humanity surrenders its freedom willingly in exchange for trivial amusements and painless conditioning.

---

## 2. In-Depth Chapter Breakdown
- **The World State & The Bokanovsky Process (Chapters 1–3)**: In the year AF 632 (After Ford), the Central London Hatchery and Conditioning Centre mass-produces test-tube babies categorized into a rigid biological caste system: Alpha, Beta, Gamma, Delta, and Epsilon. Through hypnopaedia (sleep-teaching), citizens are conditioned to consume, enjoy their predetermined caste role, and repeat state slogans: *"Community, Identity, Stability"* and *"Ending is better than mending."* Monogamy, family, and childbirth are considered revolting taboos; sexual promiscuity is mandatory.
- **Bernard Marx & Helmholtz Watson (Chapters 4–6)**: Bernard Marx, an Alpha-Plus psychologist whose physical stature was stunted by rumored alcohol in his fetal blood-surrogate, feels alienated and insecure. His friend, Helmholtz Watson, an intellectual lecturer, feels his talents are wasted producing meaningless state rhymes. Bernard visits the Savage Reservation in New Mexico with Lenina Crowne.
- **The Savage Reservation (Chapters 7–9)**: Bernard and Lenina witness natural human life: aging, disease, marriage, and religious rituals. They encounter John "the Savage," the son of Linda (a World State woman stranded years earlier) and the Director of Hatcheries. John was educated on the complete works of Shakespeare. Bernard brings John and Linda back to London as celebrity spectacles.
- **John in Civilization (Chapters 10–15)**: Bernard becomes famous, while the Director is humiliated and resigns. Linda drowns herself in continuous soma holidays until she dies in a hospital, horrifying John. When nurses hand soma rations to Delta workers, John hurls the soma out the window, shouting: *"I'll make you free!"* A riot ensues.
- **The Debate with Mustapha Mond (Chapters 16–17)**: John, Bernard, and Helmholtz are brought before Resident World Controller Mustapha Mond. In one of the greatest philosophical debates in literature, Mond defends the World State: art, truth, beauty, God, and science have been sacrificed to achieve universal comfort and social stability. John passionately demands the right to suffer: *"I want God, I want poetry, I want real danger, I want freedom, I want goodness. I want sin... I claim them all."*
- **The Tragic Climax (Chapter 18)**: Banished to a secluded lighthouse in Surrey, John attempts spiritual purification through self-flagellation and hermitage. Crowds of sightseers and reporters surround him like an animal in a zoo. Overcome by a soma-fueled frenzy, John succumbs. The next morning, horrified by his degradation, John hangs himself in the lighthouse stairway.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: عالم جديد شجاع (Brave New World)
**المؤلف:** ألدوس هكسلي (Aldous Huxley)  
**سنة النشر:** 1932  
**التصنيف الأدبي:** الخيال العلمي الديستوبي / الهجاء الفلسفي للمستقبل  

---

## 1. السياق والمقارنة مع رواية 1984
على نقيض أورويل الذي رأى أن الاستبداد يفرض بالخوف والألم والشرطة السرية، تنبأ هكسلي بنوع أشد فتكاً وخبثاً من العبودية: السيطرة عبر الإغراق في اللذات، والهندسة الوراثية، والاستهلاك المفرط، وعقار السعادة الاصطناعي "السوما". يتنازل البشر في هذا العالم عن حريتهم طواعية مقابل الراحة والمتعة الساذجة.

---

## 2. المسار الدرامي لأحداث الرواية
- **دولة العالم وتفريخ البشر (الفصول 1–3)**: في عام 632 بعد هنري فورد، يُلغى التكاثر الطبيعي تماماً ويُفرخ البشر في أنابيب اختبار ويُبرمجون وراثياً إلى 5 طبقات اجتماعية: ألفا وبيتا للقيادة، وغاما ودلتا وإبسيلون للأعمال الشاقة والوضيعة. يُلقن الأطفال عبر النوم أفكار الاستهلاك والشعار الرسمي: *"الجماعة، الهوية، الاستقرار"*. ويصبح الزواج والأسرة عاراً قبيحاً، بينما الإباحية الجنسية إلزامية للجميع.
- **تمرد برنارد ماركس (الفصول 4–6)**: برنارد ماركس، أخصائي نفسي من طبقة ألفا، يشعر بالنقص والعزلة لأن حجم جسده ضئيل بسبب خطأ في أنبوب التغذية الجنينية. يسافر مع لينينا في رحلة سياحية إلى "محمية المتوحشين" في نيومكسيكو حيث لا يزال البشر يتكاثرون طبيعياً.
- **جون "المتوحش" وشكسبير (الفصول 7–9)**: يلتقي برنارد بالشاب جون، ابن امرأة من العالم المتحضر ضلت في المحمية وأنجبته. نشأ جون وهو يقرأ مسرحيات شكسبير الكاملة. يصطحبه برنارد إلى لندن كظاهرة مثيرة للفرجة.
- **صدمة المدنية وموت ليندا (الفصول 10–15)**: يصدم جون بتفاهة العالم المتحضر وخلوه من المشاعر. تموت والدته ليندا بإدمان السوما، وحين يرى العمال يصطفون لتناول حصص المخدر، يلقي جون بالسوما من النافذة صارخاً: *"سأجعلكم أحراراً!"*، فتندلع الفوضى ويُعتقل.
- **المناظرة الفلسفية مع مصطفى موند (الفصلان 16–17)**: يواجه جون حاكم العالم مصطفى موند في مناظرة فكرية كبرى؛ يدافع موند عن نظامه مؤكداً أنهم ضحوا بالفن، والدين، والجمال، والعلم الحقيقي لشراء الاستقرار والراحة العامة. فيصرخ جون في وجهه مطالباً بالحق في الشقاء: *"أنا أطالب بحقي في الله، والشعر، والخطر الحقيقي، والحرية، والفضيلة، وأطالب بحقي في الخطيئة والألم!"*.
- **النهاية المفجعة (الفصل 18)**: يعتزل جون في منارة مهجورة ليتطهر بالصلاة وجلد الذات. تحاصره طائرات الفضوليين والمصورين كحيوان في حديقة، ويستسلم لحفلة ماجنة تحت تأثير السوما. وفي الصباح التالي، يصحو ليرى هول ما انحدر إليه، فيشنق نفسه في درج المنارة.
"""
    },

    # 52 Dune
    {
        "id": "52_Dune",
        "content_en": """# Comprehensive Study Guide: Dune
**Author:** Frank Herbert  
**Year:** 1965  
**Genre:** Epic Science Fiction / Ecological Space Opera / Political Religion  

---

## 1. Context & Masterpiece of Ecology & Realpolitik
Frank Herbert’s *Dune* is universally recognized as the *Lord of the Rings* of science fiction. Set 20,000 years in the future across a feudal galactic empire, Herbert crafts a profound exploration of planetary ecology, resource scarcity, religious manipulation, and the lethal dangers of charismatic leaders.

---

## 2. In-Depth Chapter Breakdown
- **The Trap of Arrakis**: Duke Leto of House Atreides is commanded by Padishah Emperor Shaddam IV to assume control of the desert planet **Arrakis (Dune)**—the sole source in the universe of the spice *melange*, which prolongs life and enables interstellar navigation. Leto knows it is an imperial trap orchestrated with their bitter blood rivals, House Harkonnen.
- **The Betrayal and Fall of House Atreides**: Lady Jessica, Leto's concubine and a Bene Gesserit initiate, defied her sisterhood by bearing Leto a son, **Paul Atreides**, suspected of being the messianic *Kwisatz Haderach*. Suk doctor Wellington Yueh betrays the Atreides shields to save his captured wife. Baron Vladimir Harkonnen’s forces and imperial Sardaukar butcher the Atreides; Leto dies in a failed suicide attempt to poison the Baron.
- **Sanctuary Among the Fremen**: Paul and the pregnant Jessica escape into the deep desert. They are taken in by the Fremen, the desert warriors led by Stilgar. The Fremen venerate Paul as *Muad'Dib* and *Lisan al-Gaib* (the Voice from the Outer World), an ancient prophecy planted centuries earlier by the Bene Gesserit's *Missionaria Protectiva*.
- **Riding the Sandworms & The Water of Life**: Paul masters desert survival, rides the colossal 400-meter sandworms (*Shai-Hulud*), and falls in love with the Fremen warrior Chani. By drinking the toxic Water of Life, Paul awakens total prescient awareness, perceiving all past and future timelines.
- **The Holy War (Jihad)**: Paul leads the Fremen in a planetary rebellion, destroying the Harkonnen spice harvesting with atomic weapons and riding sandworms into the capital Arrakeen. Paul slays Feyd-Rautha Harkonnen in single combat, deposes the Emperor, and forces a dynastic marriage to Princess Irulan. Yet Paul is terrified by the prescient vision of the bloody, unstoppable galactic jihad unleashed in his holy name across a billion worlds.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: كثيب (Dune)
**المؤلف:** فرانك هربرت (Frank Herbert)  
**سنة النشر:** 1965  
**التصنيف الأدبي:** الخيال العلمي الملحمي / أوبرا الفضاء الإيكولوجية / أسطورة السلطة والدين  

---

## 1. السياق وأعظم ملحمة فضاء في التاريخ
تعد رواية *كثيب* بمثابة "سيد الخواتم" في أدب الخيال العلمي. تدور أحداثها بعد 20 ألف عام في إمبراطورية مجرية إقطاعية؛ حيث يقدم هربرت دراسة عبقرية للتوازن البيئي، وصراع الموارد، واستخدام الدين كأداة للهيمنة السياسية، والتحذير من الخطر الكارثي للزعماء الملهمين.

---

## 2. المسار الدرامي لأحداث الملحمة
- **فخ كوكب أراكيس**: يأمر الإمبراطور شادام الرابع الدوق النبيل ليتو آتريديز بتولي حكم كوكب **أراكيس (كثيب)**؛ وهو كوكب صحراوي قاحل يمثل المصدر الوحيد في الكون لمادة "التوابل" (الميلانج) التي تطيل العمر وتمكن ملاحي الفضاء من طي أبعاد الكون. يعلم الدوق ليتو أن الانتقال فخ مدبر بالتحالف مع أعدائهم اللدودين آل هاركونين.
- **خيانة الطبيب وسقوط عائلة آتريديز**: أنجبت السيدة جيسيكا التابعة لمنظمة "بيني جيزيريت" ابنها **بول آتريديز**، الذي يحمل صفات المخلص الأسطوري المنتظر. يخون الطبيب يويه دفاعات القلعة لإنقاذ زوجته، وتهجم قوات البارون هاركونين الوحشية مع جنود الإمبراطور لتبيد آل آتريديز. يموت الدوق ليتو مسموماً ويهرب بول وجيسيكا في الصحراء.
- **الملاذ عند الفريمن (سكان الصحراء)**: يلجأ بول ووالدته الحامل إلى قبائل "الفريمن" الشرسة بقيادة ستيلغار. يرى الفريمن في بول "لسان الغيب" والمهدي المنتظر، وهي نبوءة زرعتها منظمة بيني جيزيريت في عقولهم قبل قرون للسيطرة عليهم.
- **ركوب ديدان الرمال وماء الحياة**: يتعلم بول أسرار الصحراء، ويروض ديدان الرمال العملاقة (شاي هولود) التي يبلغ طولها مئات الأمتار، ويقع في حب المقاتلة شاني. يشرب بول "ماء الحياة" السام فينجو من الموت وتنفتح بصيرته على رؤية كل خطوط الماضي والمستقبل بدقة خارقة.
- **الجهاد المقدس والعرش الإمبراطوري**: يقود بول جيش الفريمن في ثورة كبرى تشل إنتاج التوابل، ويقتحم العاصمة راكباً ديدان الرمال. يقتل بول الشرير فيد-روثا في مبارزة حاسمة، ويجبر الإمبراطور على التنازل عن العرش والزواج من ابنته إيرولان. لكن بول يرتعد رعباً من رؤيته المستقبلية لحرب مقدسة كونية دموية ستندلع باسمه عبر مليارات العوالم ولن يستطيع أحد إيقافها.
"""
    },

    # 54 Don Quixote
    {
        "id": "54_Don_Quixote",
        "content_en": """# Comprehensive Study Guide: Don Quixote (El ingenioso hidalgo Don Quijote de la Mancha)
**Author:** Miguel de Cervantes  
**Publication:** Part I (1605), Part II (1615)  
**Genre:** Satirical Chivalric Epic / The First Modern Novel / Metafiction  

---

## 1. Context & The Birth of the Modern Novel
Published in Spain's Golden Age, Cervantes set out to parody popular chivalric romances, accidentally creating the foundational masterpiece of Western fiction. Don Quixote explores the eternal human tension between noble, poetic idealism and earthy, pragmatic reality.

---

## 2. In-Depth Chapter Breakdown

### Part I (1605): The Quixotic Quests
- **The Madness of Alonso Quijano**: An impoverished 50-year-old country nobleman in La Mancha reads so many chivalric romances that his brain dries up and he loses his wits. He dons rusty ancestral armor, mounts his scrawny nag **Rocinante**, rechristens himself **Don Quixote de la Mancha**, and dedicates his deeds to an idealized peasant girl whom he names **Dulcinea del Toboso**.
- **Sancho Panza**: Quixote enlists a simple, pragmatic peasant, **Sancho Panza**, as his squire, promising him governorship of an island (*ínsula*). Sancho rides his donkey Dapple, supplying a stream of folk proverbs and grounded realism.
- **The Windmills & Illusions**: Quixote mistakes 30 windmills for ferocious giants, charging them with his lance and being violently thrown when the blades shatter his weapon. He blames the enchanter Fréstón for turning giants into windmills. He attacks flocks of sheep believing they are warring armies, frees chained galley slaves who immediately stone him, and turns a brass barber's basin into the mythical "Helmet of Mambrino."
- **The Caged Return**: Friends from his village (the Priest and the Barber) lure Quixote into an enchanted wooden cage on an ox-cart, bringing him home to recover.

### Part II (1615): The Metafictional Masterpiece
- **Awareness of Fame**: In a revolutionary meta-literary twist, Quixote and Sancho learn that Part I of their adventures has been published as a worldwide bestseller.
- **The Duke and Duchess**: An aristocratic Duke and Duchess invite Quixote and Sancho to their castle, staging elaborate, cruel pranks for their own amusement, including granting Sancho governorship of Barataria (where Sancho surprisingly rules with Solomonic wisdom before renouncing power).
- **The Knight of the White Moon & Death**: In Barcelona, his neighbor Sansón Carrasco, disguised as the "Knight of the White Moon," defeats Quixote in combat, commanding him to lay down his arms for a year. Brokenhearted, Quixote returns to La Mancha, falls ill, and regains his sanity as Alonso Quijano the Good, denouncing all chivalric books before dying peacefully surrounded by weeping friends.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: دون كيخوت (Don Quixote)
**المؤلف:** ميغيل دي ثيربانتس (Miguel de Cervantes)  
**سنة النشر:** الجزء الأول (1605)، الجزء الثاني (1615)  
**التصنيف الأدبي:** الرواية الحديثة الأولى في التاريخ / سخرية الفروسية / الصراع بين المثالية والواقع  

---

## 1. السياق وميلاد الرواية العالمية الأولى
أبدع ثيربانتس في العصر الذهبي الإسباني عملاً أراد به السخرية من كتب الفروسية المبتذلة، فصنع أعظم رواية في تاريخ الأدب الإنساني. يجسد دون كيخوت الصراع الأزلي بين المثالية الشعرية الحالمة (دون كيخوت)، وبين الواقعية الشعبية النفعية (سانشو بانثا).

---

## 2. المسار الدرامي لأحداث الجزأين

### الجزء الأول (1605): مغامرات الفارس المغوار
- **جنون ألونسو كيخانو**: نبيل ريفي فقير في الخمسين من عمره في إقليم لامانشا، يفرط في قراءة روايات الفرسان الجوالين حتى يجف دماغه ويفقد عقله. يرتدي دروع أجداده الصدئة، ويمتطي حصانه الهزيل "روثينانتي"، ويسمي نفسه **دون كيخوت دي لا مانشا**، متخذاً من فتاة ريفية ساذجة ملهمة وأميرة لأحلامه يسميها **دولسينيا دي توبوسو**.
- **سانشو بانثا ورفقة الدرب**: يقنع فلاحاً بسيطاً ساذجاً يدعى "سانشو بانثا" بالعمل تابعاً له وحاملاً لدرعه مقابل وعد بتعيينه حاكماً على جزيرة. يركب سانشو حماره موازناً جنون سيده بأمثال شعبية وواقعية ملموسة.
- **طواحين الهواء والأوهام**: يهاجم دون كيخوت 30 طاحونة هواء ظناً منه أنها عمالقة متوحشون، فتقذفه أشرعتها أرضاً وتحطم رمحه؛ فيدعي أن الساحر فريستون حول العمالقة لطواحين لحرمانه من المجد! يهاجم قطيع خراف ظناً أنه جيش جرار، ويحرر مجرمين محكومين بالأشغال الشاقة فيرجمونه بالحجارة، ويعتبر طشت الحلاق النحاسي خوذة الساحر مامبرينو الذهبية!
- **العودة في القفص**: يدبر قسيس البلدة والحلاق حيلة لإعادته مقيداً داخل قفص خشبي على عربة تجرها الثيران لعلاجه في منزله.

### الجزء الثاني (1615): الرواية الماورائية واليقظة
- **شهرة الأبطال**: في حبكة حداثية سابقة لعصرها بقرون، يكتشف دون كيخوت وسانشو أن الجزء الأول من مغامراتهما قد طُبع وأصبح الكتاب الأكثر مبيعاً وشهرة في إسبانيا وأوروبا!
- **مكائد الدوق والدوقة**: يستضيفهما دوق أرستقراطي في قصره لا كرامة لهما، بل لتدبير مقالب هزلية قاسية للتسلية، ومنها تنصيب سانشو حاكماً على جزيرة باراتاريا، حيث يفاجئ سانشو الجميع بإصدار أحكام قضائية شديدة الحكمة والعدل قبل أن يزهد في الحكم ويعود لسيده.
- **فارس القمر الأبيض والموت الحزين**: في برشلونة، يتنكر جاره الشاب في شخصية "فارس القمر الأبيض" ويهزم دون كيخوت في مبارزة، مجبراً إياه على ترك سلاحه والعودة لقريته لعام كامل. يعود دون كيخوت منكسر الفؤاد، ويصيبه مرض شديد، فيسترد عقله فجأة ويتبرأ من كتب الفروسية الخيالية، ويموت بسلام باسم "ألونسو كيخانو الصالح" وسط بكاء صديقه الوفي سانشو.
"""
    },

    # 55 One Hundred Years of Solitude
    {
        "id": "55_One_Hundred_Years_Of_Solitude",
        "content_en": """# Comprehensive Study Guide: One Hundred Years of Solitude (Cien años de soledad)
**Author:** Gabriel García Márquez  
**Year:** 1967  
**Genre:** Magical Realism / Epic Multi-Generational Saga  

---

## 1. Context & The Epoch of Magical Realism
Winner of the Nobel Prize in Literature, García Márquez’s masterpiece tracks seven generations of the Buendía family in the mythical Colombian town of **Macondo**. The novel blends the impossible and the everyday—flying carpets, insomnia plagues, yellow butterfly swarms, and ghost visitations—as a searing allegory for Latin American history, colonial exploitation, and the inescapable curse of human solitude.

---

## 2. In-Depth Chapter Breakdown
- **The Founding of Macondo**: Patriarch **José Arcadio Buendía** and his pragmatic cousin-wife **Úrsula Iguarán** flee their homeland haunted by the ghost of Prudencio Aguilar. They found Macondo, a forgotten Eden by a river of clear water and prehistorical stones. Gypsies led by the alchemist **Melquíades** bring wonders: magnets, telescopes, and ice.
- **The Thirty-Two Civil Wars**: Their son, **Colonel Aureliano Buendía**, organizes thirty-two armed uprisings against the Conservative regime, surviving multiple firing squads and assassination attempts. Disillusioned by the corruption of power, he signs a peace treaty and retreats to his workshop, endlessly fashioning little gold fish.
- **The Banana Massacre**: Macondo modernizes with the arrival of the American banana company. When thousands of workers strike for humane conditions, the national army massacres over 3,000 workers at the railway station, dumping their corpses into the sea. The government erases the massacre from official history, declaring that *"nothing has happened in Macondo."*
- **The Deluge & Decline**: A torrential rain falls upon Macondo for four years, eleven months, and two days, washing away the banana plantations. The matriarch Úrsula dies at well over a hundred years old. Macondo decays into neglect and red dust.
- **The Parchments and the Hurricane**: The final Aureliano (Aureliano Babilonia) and his aunt Amaranta Úrsula commit incestuous love, giving birth to a baby with a pig's tail, who is devoured by red ants. Aureliano deciphers Melquíades's Sanskrit parchments, realizing they are the complete prophetic history of the Buendía family written a century before. As he reads the final lines, a biblical biblical hurricane sweeps Macondo off the face of the earth: *"Because races condemned to one hundred years of solitude did not have a second opportunity on earth."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: مئة عام من العزلة (One Hundred Years of Solitude)
**المؤلف:** غابرييل غارسيا ماركيز (Gabriel García Márquez)  
**سنة النشر:** 1967  
**التصنيف الأدبي:** الواقعية السحرية / ملحمة الأجيال / التاريخ الرمزي لأمريكا اللاتينية  

---

## 1. السياق وثورة الواقعية السحرية
تعد تحفة ماركيز الحائزة على جائزة نوبل الرواية الأبرز في تاريخ أدب أمريكا اللاتينية؛ تروي قصة سبعة أجيال من عائلة بوينديا في قرية **ماكوندو** الخيالية المعزولة. تدمج الرواية الخوارق السحرية بالأحداث اليومية (سجاد طائر، وباء الأرق، مطر يدوم 5 سنوات، فراشات صفراء) كرمز ملحمي لتاريخ كولومبيا واستغلال الشركات الأجنبية ولعنة العزلة الإنسانية.

---

## 2. المسار الدرامي لأجيال ماكوندو السبعة
- **تأسيس ماكوندو وعالم الغجر**: يهرب المؤسس خوسيه أركاديو بوينديا وزوجته الصبورة أورسولا إيغواران بعد قتله لبرودينسيو أغيلار ومطاردة شبحه لهما. يؤسسان بلدة ماكوندو البدائية المنعزلة. يزورهم الغجر بقيادة الساحر الغامض **ميلكياديس** جالباً اختراعات مذهلة كالمغناطيس والتليسكوب والثلج.
- **حروب الكولونيل أوريليانو الـ 32**: يشعل ابنهما الكولونيل أوريليانو بوينديا 32 ثورة مسلحة ضد النظام المحافظ، وينجو من فرق الإعدام المتكررة والسم والكمائن. وبعد عقود من إراقة الدماء، يكتشف خواء الحرب والسياسة فيوقع معاهدة سلام ويعتزل في ورشته يصنع أسماكاً ذهبية صغيرة ويصهرها ليعيد صنعها بلا توقف.
- **مجزرة عمال الموز ومحو الذاكرة**: تدخل سكة الحديد وتصل شركة الموز الأمريكية الاستعمارية. يضرب آلاف العمال للمطالبة بحقوقهم الإنسانية، فيحاصرهم الجيش في محطة القطار ويفتح النار عليهم مبيداً أكثر من 3,000 عامل، ويحمل جثثهم في قطارات سرية ليلقيها في المحيط. تمحو الحكومة المجزرة من التاريخ الرسمي وتنكر حدوث أي شيء في ماكوندو!
- **طوفان السنوات الخمس وزوال البلدة**: ينهمر مطر طوفاني مستمر على ماكوندو لأربع سنوات وأحد عشر شهراً ويومين، فيغسل مزارع الموز ويدمر الحياة. تموت الجدة الكبرى أورسولا بعد أن تجاوزت المئة عام، وتغرق البلدة في الخراب والنمل والنسيان.
- **مخطوطات ميلكياديس والإعصار الخاتم**: يقع أوريليانو بابيلونيا في حب خالته أمارانتا أورسولا، لينجبا طفلاً بذيل خنزير يلتهمه النمل الأحمر. يفك أوريليانو شفرة رقوق الساحر ميلكياديس السنسكريتية؛ فيكتشف أنها لم تكن سوى نبوءة دقيقة لتاريخ عائلة بوينديا كُتبت قبل مئة عام! ومع قراءته للسطر الأخير، يجتاح إعصار توراتي هائل قرية ماكوندو ويمسحها من الوجود إلى الأبد؛ *"لأن السلالات المحكوم عليها بمئة عام من العزلة لا تملك فرصة ثانية على وجه الأرض"*.
"""
    },

    # 56 Love in the Time of Cholera
    {
        "id": "56_Love_In_The_Time_Of_Cholera",
        "content_en": """# Comprehensive Study Guide: Love in the Time of Cholera (El amor en los tiempos del cólera)
**Author:** Gabriel García Márquez  
**Year:** 1985  
**Genre:** Romantic Realism / Psychological Drama / Ode to Enduring Passion  

---

## 1. Context & The Sickness of Love
García Márquez explores love not as a youthful romance, but as a biological affliction mirroring cholera—marked by fever, agony, and lifelong obsession.

---

## 2. In-Depth Chapter Breakdown
- **Youthful Infatuation**: In a Caribbean port city, telegraph clerk and poet **Florentino Ariza** falls obsessively in love with young schoolgirl **Fermina Daza**. They exchange hundreds of passionate letters. But when Fermina’s ambitious father discovers the affair, he takes her on a long inland journey. Upon her return, seeing Florentino at the market, Fermina realizes her feeling was an illusion and dismisses him: *"Forget it: it was only a dream."*
- **Fermina and Dr. Urbino**: Fermina marries **Dr. Juvenal Urbino**, a prestigious, aristocratic physician dedicated to eradicating cholera. Their marriage spans over fifty years of comfortable bourgeois companionship, domestic friction, and quiet stability.
- **Florentino's 622 Affairs & Secret Loyalty**: Devastated, Florentino vows to wait for Fermina until Urbino dies. He becomes president of the River Steamship Company. Over 51 years, 9 months, and 4 days, Florentino participates in 622 clandestine affairs with women, yet maintains that in his soul, he has remained faithfully devoted to Fermina alone.
- **The Reconnection**: Dr. Urbino dies at age 81 falling from a ladder trying to catch a pet parrot. Florentino appears at the wake and reiterates his eternal love to the shocked widow. After initial fury, Fermina allows Florentino to visit her. They take a river voyage up the Magdalena River on a steamboat.
- **The Yellow Flag of Cholera**: Realizing they cannot bear to return to societal gossip on land, Florentino orders the captain to raise the yellow quarantine flag of cholera. Barred from all ports, the boat sails forever along the river. When asked how long they can keep going, Florentino replies with immortal certainty: *"Forever."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الحب في زمن الكوليرا (Love in the Time of Cholera)
**المؤلف:** غابرييل غارسيا ماركيز (Gabriel García Márquez)  
**سنة النشر:** 1985  
**التصنيف الأدبي:** الواقعية الرومانسية / دراما العشق الخالد / أدب الشيخوخة  

---

## 1. المفهوم الجوهري: الحب كوباء الكوليرا
يقدم ماركيز الحب كمرض عضوي وعاطفي يشبه وباء الكوليرا في أعراضه؛ بحمى تسحق الجسد، وهذيان، وألم يستمر طوال العمر. الرواية أنشودة ملحمية لانتصار الصبر الإنساني والعشق المتحدي للشيخوخة والزمن.

---

## 2. المسار الدرامي لأحداث الرواية
- **غرام الشباب والرسائل السرية**: في مدينة كولومبية ساحلية على البحر الكاريبي، يقع موظف التلغراف الشاعر الشاب **فلورنتينو أريثا** في حب التلميذة الجميلة **فيرمينا داثا**. يتبادلان مئات الرسائل العاطفية الملتهبة. يكتشف والدها الأمر ويسافر بها بعيداً لقطع العلاقة. وحين تعود وتلتقي بفلورنتينو في السوق، تراه بعين الواقع وتكتشف أن حبها كان وهماً طفولياً فتقول له ببرود: *"انسَ الأمر.. لم يكن سوى وهم"*.
- **زواج فيرمينا من الدكتور أوربينو**: تتزوج فيرمينا من الطبيب الأرستقراطي المرموق **د. خوفينال أوربينو**؛ بطل مكافحة الكوليرا. يعيشان معاً زواجاً برجوازياً مستقراً يمتد لأكثر من نصف قرن، مبنياً على العادات والهدوء لا الشغف الجارف.
- **وفاء أريثا وعلاقاته الـ 622**: يقسم فلورنتينو على انتظار فيرمينا حتى يموت زوجها. يرتقي في العمل ليصبح رئيساً لشركة الملاحة النهرية. وعلى مدار 51 عاماً و9 أشهر و4 أيام، يخوض 622 علاقة سرية مع نساء مختلفات، لكنه يظل مقتنعاً بأن روحه ظلت عذراء مخلصة لفيرمينا وحدها.
- **موت الزوج وتجدد العهد**: يموت الدكتور أوربينو في سن الـ 81 بعد سقوطه من شلم وهو يحاول الإمساك بببغائه الأليف. في نفس ليلة الجنازة، يقف فلورنتينو أمام الأرملة المكلومة ويجدد عهد حبه الأبدي لها! تطرده فيرمينا في البداية، لكنهما يستعيدان التواصل تدريجياً ويبحران معاً في رحلة نهرية على متن باخرة في نهر ماغدالينا.
- **علم الكوليرا الأصفر والأبدية**: يكتشفان في خريف العمر حباً حقيقياً طاهراً. ولتجنب الفضائح والعودة للواقع الأرضي، يأمر فلورنتينو القبطان برفع علم الكوليرا الأصفر الذي يفرض الحجر الصحي، مانعاً أي ركاب من الصعود ومحرماً على السفينة الرسو في أي ميناء. وعندما يسأله القبطان في دهشة: وإلى متى سنظل نبحر هكذا؟ يجيب فلورنتينو بثقة تخرق حدود الزمن: *"إلى الأبد!"*.
"""
    },

    # 57 The Trial
    {
        "id": "57_The_Trial",
        "content_en": """# Comprehensive Study Guide: The Trial (Der Process)
**Author:** Franz Kafka  
**Written:** 1914–1915 (Published 1925)  
**Genre:** Absurdist Fiction / Bureaucratic Nightmare / Existential Horror  

---

## 1. Context & The Kafkaesque Predicament
Written on the eve of WWI and published posthumously by Max Brod, *The Trial* is the definitive portrait of the modern individual crushed by an invisible, impenetrable, and irrational judicial bureaucracy.

---

## 2. In-Depth Chapter Breakdown
- **The Arrest (Chapter 1)**: *"Someone must have slandered Josef K., for one morning, without having done anything wrong, he was arrested."* On his 30th birthday, bank chief financial clerk Josef K. is arrested in his boarding house by two low-ranking warders (Franz and Willem). They refuse to tell him what he is charged with or what court has jurisdiction. He remains free to go to work.
- **The Interrogation in the Attic (Chapter 2)**: Summoned to his initial inquiry, K. climbs to a suffocating tenement attic in a squalid suburb. Facing an indifferent, bizarre court of old men, K. delivers an impassioned speech exposing bureaucratic corruption, which only isolates him further.
- **The Lawyers and the Court Painter (Chapters 4–8)**: K.'s uncle introduces him to Lawyer Huld, a bedridden, pompous advocate who does nothing but stall. K. consults the court painter Titorelli, who explains the three possible judicial outcomes: *Actual Acquittal* (a myth that has never happened), *Apparent Acquittal* (temporary freedom followed by rearrest), and *Protraction* (endless procedural delay).
- **In the Cathedral (The Parable of the Law - Chapter 9)**: Assigned to guide an Italian client through a dark cathedral, K. meets the prison chaplain, who calls him by name and tells him the parable **"Before the Law"**: A man from the country seeks admittance to the Law. The gatekeeper refuses entry, telling him to wait. The man waits his entire life until blindness and death overtake him. At his dying breath, the gatekeeper tells him: *"No one else could ever be admitted here, since this gate was made only for you. I am now going to shut it."*
- **The Execution (Chapter 10)**: On the eve of his 31st birthday, two executioners in top hats escort K. to a deserted stone quarry outside the city. They pin him to a slab. As a butcher's knife is passed above him, K. sees a window open in the distance, wondering if help is coming. One executioner holds his throat while the other plunges the knife into his heart and twists it twice: *"‘Like a dog!’ he said; it was as if the shame of it should outlive him."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: المحاكمة (The Trial)
**المؤلف:** فرانتس كافكا (Franz Kafka)  
**سنة التأليف:** 1914–1915 (نُشرت 1925)  
**التصنيف الأدبي:** أدب الكابوس الكافكاوي / العبث البيروقراطي / الرعب الوجودي  

---

## 1. السياق والمأزق الكافكاوي
كُتبت الرواية عشية الحرب العالمية الأولى ونشرها ماكس برود بعد وفاة كافكا؛ وتعد الصياغة الكاملة للمصطلح الأدبي "كافكاوي" (Kafkaesque)؛ حيث يُسحق الفرد الأعزل تحت وطأة منظومة بيروقراطية وقضائية غامضة، لا وجه لها ولا منطق يحكمها.

---

## 2. التسلسل التفصيلي لفصول الرواية
- **الاعتقال المباغت (الفصل 1)**: تفتتح الرواية بالجملة الأيقونية: *"لا بد أن شخصاً ما قد افترى على جوزيف ك.، لأنه اعتُقل ذات صباح دون أن يفعل أي سوء"*. في عيد ميلاده الثلاثين، يفاجأ مصرفي البنك الناجح جوزيف ك. بحارسين يدخلان غرفته ويعلنان اعتقاله، رافضين إخباره بطبيعة التهمة أو الجهة القضائية التي تحاكمه، مع السماح له بالذهاب لعمله كالمعتاد!
- **التحقيق في العلية السكنية (الفصل 2)**: يُستدعى للتحقيق الأول فيجد المحكمة منعقدة في علية مظلمة قذرة بمبنى سكني بائس. يلقي ك. خطبة نارية يفضح فيها فساد وسخافة المحكمة، مما يزيد من تضييق الخناق عليه.
- **المحامي ورسام المحكمة تيتوريللي (الفصول 4–8)**: يوكل ك. المحامي المقعد هولد الذي يغرق في الثرثرة وتأجيل الإجراءات. يلجأ ك. لرسام المحكمة "تيتوريللي" الذي يشرح له المآلات القضائية الثلاثة الممكنة: *البراءة الفعلية* (وهي أسطورة لم تحدث قط في تاريخ المحكمة)، أو *البراءة الظاهرية* (إفراج مؤقت يتبعه اعتقال جديد)، أو *المماطلة الأبدية* (تأجيل الإجراءات حتى الموت).
- **في الكاتدرائية وأمثولة "أمام القانون" (الفصل 9)**: في كاتدرائية مظلمة، يلتقي ك. بواعظ السجن الذي يناديه باسمه ويروي له أمثولة كافكا الخالدة **"أمام القانون"**: رجل قروي يأتي طالباً الدخول إلى القانون، فيمنعه البواب ويخبره بالانتظار. يقضي الرجل عمره كله جالساً أمام الباب حتى يدركه الموت، وقبل أن يلفظ أنفاسه يخبره البواب: *"لم يكن لأحد غيرك أن يدخل من هذا الباب، لأن هذا الباب كان مخصصاً لك وحدك، والآن سأغلقه للأبد!"*.
- **الإعدام المروع في المقالع (الفصل 10)**: في الليلة التي تسبق عيد ميلاده الحادي والثلاثين، يقتاده جلاوزان يرتديان قبعات سوداء لمقلع حجارة مهجور خارج المدينة. يسندانه لصخرة، وتمر سكين جزار فوق رأسه. ينظر ك. لنافذة بعيدة يرى فيها شخصاً يمد يديه متسائلاً إن كان هناك أمل أو نجاة. يطعنه الجلاد بسكين في قلبه ويديرها مرتين، فيلفظ ك. كلمته الأخيرة قبل أن يخمد: *"كالكلب!"، وكأن الخزي والمهانة كُتب لهما أن يعيشا أطول منه!
"""
    },

    # 58 The Metamorphosis
    {
        "id": "58_The_Metamorphosis",
        "content_en": """# Comprehensive Study Guide: The Metamorphosis (Die Verwandlung)
**Author:** Franz Kafka  
**Year:** 1915  
**Genre:** Absurdist Novella / Existentialism / Psychological Allegory  

---

## 1. Context & The Anatomy of Alienation
*"One morning, upon awakening from agitated dreams, Gregor Samsa found himself, in his bed, transformed into a monstrous vermin"* (*ungeheuren Ungeziefer*). Kafka literalizes the emotional dehumanization of the modern worker under capitalist economic dependency.

---

## 2. In-Depth Chapter Breakdown
- **Chapter 1: The Transformation & Panic**: Gregor Samsa, an exhausted traveling salesman working to pay off his parents' bankruptcy debts, wakes up as a giant armored beetle with helpless spindly legs. His primary concern is not his horrific body, but missing the 5:00 AM train to work. When his office manager arrives demanding explanations, Gregor opens the door; the manager flees in terror, his mother collapses, and his father violently drives Gregor back into his room with a cane and a newspaper, injuring his leg.
- **Chapter 2: Confinement and the Apple Wound**: Consoled only by his younger sister Grete, Gregor hides beneath a sofa. Grete brings him rotting food scraps, which he now relishes. As the family is forced to work to replace Gregor's income, their sympathy curdles into resentment. When his mother faints seeing him, his father furiously pelts Gregor with apples from a fruit bowl; one apple embeds itself deeply into Gregor's soft back, rotting and causing a festering, permanent wound.
- **Chapter 3: Neglect, The Violin, and Death**: Gregor's room becomes a dusty storage dumping ground. The family rents rooms to three arrogant lodgers. One evening, drawn by the beautiful sound of Grete's violin playing in the parlor, Gregor creeps out, yearning for human connection. The lodgers are disgusted and threaten legal action. Grete tearfully turns on Gregor: *"We must try to get rid of it... it's killing you both, I see it coming."* Broken in spirit and body, Gregor crawls back into his dark room, thinks of his family with tender love, and dies at dawn. The charwoman sweeps his dry corpse away. The relieved Samsa family takes a celebratory tram ride into the countryside, noting how Grete has blossomed into a beautiful young woman ready for marriage.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: المسخ (التحول - The Metamorphosis)
**المؤلف:** فرانتس كافكا (Franz Kafka)  
**سنة النشر:** 1915  
**التصنيف الأدبي:** أدب العبث والوجودية / التحول الرمزي / تشريح الاغتراب الإنساني  

---

## 1. المفتتح الخالد ومأساة الاغتراب
تبدأ النوفيلا بإحدى أشهر الافتتاحيات في تاريخ الرواية: *"استيقظ غريغور سامسا ذات صباح من أحلام مضطربة، ليجد نفسه قد تحول في سريره إلى حشرة عملاقة مفزعة"*. يجسد كافكا بعبقرية كيف يتحول الإنسان المعاصر إلى مجرد أداة إنتاج اقتصادية، وحين يعجز عن الكد والعمل، تسقط عنه إنسانيته ويتحول لعبء ثقيل في عيون أقرب الناس إليه.

---

## 2. التسلسل التفصيلي لفصول الرواية الثلاثة
- **الفصل 1 (التحول والذعر)**: غريغور موظف مبيعات متجول منهك، يعمل بضراوة لسداد ديون والده المفلس. عند استيقاظه وتحوله إلى حشرة بدرع صلب وأرجل دقيقة عاجزة، لا يشغل باله شكل جسده المخيف، بل يرتعب من فوات قطار الخامسة صباحاً وغضب رئيسه في العمل! يصل مدير الشركة للمنزل مستنكراً تأخره؛ وحين يفتح غريغور الباب، يهرب المدير في ذعر، وتنهار أمه مغشياً عليها، بينما يهاجمه والده بعصا وجريدة ويدفعه بعنف داخل غرفته جريحاً ومدمى.
- **الفصل 2 (العزلة وتفاحة الأب القاتلة)**: تعتني به شقيقته الصغرى غريتا بحذر، وتضع له بقايا الطعام الفاسد التي أصبحت تستهويه. تضطر الأسرة للعمل لتعويض دخل غريغور المفقود، فتتحول الشفقة تدريجياً إلى تذمر وحقد. وعندما تحاول الأم وغريتا إخلاء غرفته من الأثاث، يخرج غريغور لحماية لوحة سيدة الفراء، فيفاجئه الأب برجمه بالتفاح بقسوة؛ فتستقر تفاحة في ظهره اللين وتتعفن داخل جرحه محدثة التهاباً مزمناً يقعده عن الحركة.
- **الفصل 3 (كمان الأخت، الموت، والراحة)**: تتحول غرفة غريغور إلى مخزن للمهملات والغبار بعد إهماله التام. تؤجر العائلة غرفاً لثلاثة مستأجرين متغطرسين. وفي إحدى الأمسيات، تعزف غريتا على الكمان، فيخرج غريغور من غرفته منجذباً لسحر الموسيقى باحثاً عن لمسة دفء إنساني. يكتشفه المستأجرون فيشمئزون ويهددون بالرحيل دون دفع. تنفجر غريتا باكية وتعلن ببرود: *"يجب أن نتخلص من هذا الشيء.. إنه يدمر حياتنا!"*. يزحف غريغور المكلوم لغرفته المظلمة، ويفكر في عائلته بمحبة ورقة، ويلفظ أنفاسه الأخيرة مع طلوع الفجر. تكنس الخادمة جثته الجافة مع القمامة، وتخرج العائلة المشرقة في نزهة بالترام في الريف متأملين نضارة ابنتهم غريتا وتأهبها للزواج.
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
