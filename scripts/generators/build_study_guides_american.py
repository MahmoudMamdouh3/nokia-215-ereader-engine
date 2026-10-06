"""
Generates master-level study guides for American Literature masterpieces:
- 43_Moby_Dick
- 44_The_Catcher_In_The_Rye
- 45_To_Kill_A_Mockingbird
- 46_Adventures_Of_Huckleberry_Finn
- 47_The_Grapes_Of_Wrath
- 48_The_Sound_And_The_Fury
- 49_Lolita
- 50_Beloved
- 53_The_Old_Man_And_The_Sea
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 43 Moby Dick
    {
        "id": "43_Moby_Dick",
        "content_en": """# Comprehensive Study Guide: Moby-Dick (The Whale)
**Author:** Herman Melville  
**Year:** 1851  
**Genre:** Epic American Novel / Allegory / Philosophical Tragedy  

---

## 1. Context & Cosmic Symbolism
*"Call me Ishmael."*  
Herman Melville crafts an American epic that transforms a 19th-century Nantucket whaling voyage into a metaphysical duel with the divine. Captain Ahab's obsessive pursuit of the albino sperm whale Moby Dick is a rebellion against cosmic order, existential vulnerability, and God Himself.

---

## 2. In-Depth Chapter Breakdown
- **Nantucket & Queequeg**: Ishmael, seeking spiritual renewal at sea, boards at the Spouter-Inn in New Bedford, sharing a bed with Queequeg, a heavily tattooed Polynesian harpooner. Overcoming racial prejudice, they form a profound fraternal bond and sign aboard the *Pequod*, a weather-beaten whaling ship.
- **Captain Ahab's Vow**: At sea, Captain Ahab emerges with his ivory leg (fashioned from a whale's jaw). He nails a gold Spanish doubloon to the masthead, demanding the crew pledge their souls to hunt down Moby Dick, the ferocious white whale who severed his leg: *"I'd strike the sun if it insulted me!"* First Mate Starbuck is the lone voice of Christian reason and moral protest.
- **The Whaling Odyssey**: The novel balances thrilling oceanic chases with encyclopedic treatises on cetology, ambergris, and harpoons. The *Pequod* encounters nine ships ("gams"), each providing symbolic portents of doom. Queequeg falls ill and commissions a wooden coffin, which later becomes a lifebuoy.
- **The Three-Day Chase**: Ahab finally spots the white whale. Over three consecutive days of violent pursuit, Moby Dick destroys whaleboats, bites Ahab's boat in two, and tangles Fedallah in the harpoon lines.
- **The Annihilation**: On the third day, Moby Dick rams the *Pequod*'s bow, breaching its hull. As the ship sinks, Ahab hurls his final harpoon: *"From hell's heart I stab at thee; for hate's sake I spit my last breath at thee."* The harpoon line catches Ahab around the neck, snapping him into the sea's abyss. The ship sinks in a swirling vortex. Only Ishmael survives, floating on Queequeg's wooden coffin until rescued by the *Rachel*.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: موبي ديك (Moby-Dick)
**المؤلف:** هيرمان ميلفيل (Herman Melville)  
**سنة النشر:** 1851  
**التصنيف الأدبي:** ملحمة أدبية كبرى / التراجيديا الفلسفية / الصراع الوجودي والرمزي  

---

## 1. السياق والمفتتح الأسطوري
تبدأ الرواية بإحدى أشهر العبارات في تاريخ الأدب: *"نادوني إسماعيل"*. يحول هيرمان ميلفيل رحلة صيد حيتان من جزيرة نانتوكت في القرن التاسع عشر إلى ملحمة ميتافيزيقية كبرى؛ حيث يجسد مطاردة القبطان "أهاب" للحوت الأبيض الضخم تمرداً أعمى ضد الأقدار والقوى الإلهية والعدمية الكونية.

---

## 2. المسار الدرامي لأحداث الملحمة
- **إسماعيل وكويكويغ**: يبحث إسماعيل عن تجديد روحه بالبحر، فينزل في نزل بنيوبيدفورد ويضطر للنوم في فراش واحد مع "كويكويغ"، الرامي البولينيزي ذي الوشوم الكثيفة. تسقط الحواجز العرقية وتنشأ بينهما أخوة إنسانية نقية، وينضمان لطاقم سفينة صيد الحيتان "بيكود".
- **ظهور القبطان أهاب والعملة الذهبية**: يظهر القبطان الغامض أهاب بساقه العاجية المنحوتة من فك حوت. يسمر عملة ذهبية في صاري السفينة ويقسم الطاقم على مطاردة "موبي ديك"؛ الحوت الأبيض الشرس الذي قطع ساقه، معلناً تحديه لقوى الكون: *"سأضرب الشمس لو أنها أهانتني!"*. ويظل المساعد الأول "ستاربك" الصوت العقلاني الوحيد الذي يرفض هذا الهوس المدمر.
- **رحلة السفينة بيكود**: تتقاطع مطاردات صيد الحيتان مع تأملات موسوعية في عالم البحار. تلتقي بيكود بتسع سفن، تحمل كل منها نبوءات بخراب السفينة. يمرض كويكويغ ويصنع لنفسه تابوتاً خشبياً، يتحول لاحقاً إلى طوق نجاة معلق في مؤخرة السفينة.
- **أيام المطاردة الثلاثة المهلكة**: يلمح أهاب الحوت الأبيض؛ وعلى مدار ثلاثة أيام من الصراع الدامي في المحيط، يحطم موبي ديك زوارق الصيد، ويقتل الرماة ويسحق المعدات.
- **الفناء والناجي الوحيد**: في اليوم الثالث، ينطح الحوت الأبيض مقدمة السفينة بيكود ويغرقها. يرمي أهاب رمحه الأخير بحقد أعمى: *"من قلب الجحيم أطعنك.. وبدافع الكراهية أبصق في وجهك أنفاسي الأخيرة!"*. يلتف حبل الرمح حول عنق أهاب فيجره الحوت لأعماق المحيط. تغرق السفينة برمتها في دوامة بحرية هائلة، ولا ينجو سوى "إسماعيل" الذي يطفو فوق تابوت صديقه كويكويغ حتى تنقذه السفينة ريتشيل.
"""
    },

    # 44 The Catcher in the Rye
    {
        "id": "44_The_Catcher_In_The_Rye",
        "content_en": """# Comprehensive Study Guide: The Catcher in the Rye
**Author:** J.D. Salinger  
**Year:** 1951  
**Genre:** Coming-of-Age (Bildungsroman) / Post-War Alienation  

---

## 1. Cultural Phenomenon & Holden's Voice
J.D. Salinger created the defining voice of adolescent alienation. Tormented by the death of his younger brother Allie, 16-year-old Holden Caulfield rebels against the pervasive hypocrisy, superficiality, and commercialism of adult society, which he famously dismisses as "phoniness."

---

## 2. In-Depth Narrative Breakdown
- **Expulsion from Pencey Prep**: Kicked out of his fourth boarding school for failing grades, Holden visits his history teacher Mr. Spencer, gets into a bloody fistfight with his handsome, shallow roommate Stradlater over a girl Holden cares for (Jane Gallagher), and packs his bags in the dead of night, shouting: *"Sleep tight, ya morons!"*
- **The New York Odyssey (48 Hours of Disillusionment)**: Holden checks into the sleazy Edmont Hotel in Manhattan. He dances with tourists, is swindled and punched in the stomach by the elevator pimp Maurice and teen prostitute Sunny, visits museums, and takes his superficial friend Sally Hayes to a Broadway show, proposing they run away to live in a Vermont cabin.
- **The Central Metaphor**: Holden sneaks into his parents' apartment to visit his beloved 10-year-old sister Phoebe. Phoebe challenges his cynicism, demanding to know what he wants to do with his life. Holden reveals his fantasy: based on a misheard Robert Burns song, he pictures thousands of children playing in a rye field on the edge of a cliff, and his only role would be to stand there and catch them before they fall off: *"I'd just be the catcher in the rye and all."*
- **The Epiphany at the Carousel**: Planning to hitchhike West, Holden meets Phoebe, who arrives with a suitcase determined to come with him. Holden refuses to let her ruin her life. He takes her to the Central Park carousel. Sitting in the pouring rain, watching Phoebe reach for the brass ring on the wooden horse, Holden experiences immense, unadulterated joy: *"I was damn near bawling, I felt so damn happy."*
- **Conclusion**: Speaking from a psychiatric sanitarium, Holden regrets telling his story because: *"Don't ever tell anybody anything. If you do, you start missing everybody."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الحارس في حقل الشوفان (The Catcher in the Rye)
**المؤلف:** ج. د. سالينجر (J.D. Salinger)  
**سنة النشر:** 1951  
**التصنيف الأدبي:** أدب الاغتراب والتمرد الشبابي / رواية التكوين المعاصرة  

---

## 1. الظاهرة الأدبية وصوت هولدن كولفيلد
ابتكر سالينجر الصوت الأبرز لاغتراب المراهقين في القرن العشرين. يعيش هولدن كولفيلد (16 عاماً) صدمة نفسية عميقة بعد وفاة شقيقه الأصغر آلي بسرطان الدم، فيثور ضد نفاق وتصنع وزيف العالم البالغ، واصفاً إياهم بـ "المزيفين" (Phonies).

---

## 2. التسلسل التفصيلي لمغامرة الـ 48 ساعة
- **الطرد من مدرسة بنسي**: يُطرد هولدن من مدرسته الداخلية للمرة الرابعة بسبب رسوبه. يتشاجر بالأيدي مع زميله المتغطرس سترادلتر دفاعاً عن كرامة صديقته جين غالاغر، ويحزم حقائبه ليلاً هارباً إلى نيويورك صارخاً في الممر: *"نوماً هنيئاً يا معشر الأغبياء!"*.
- **التيه في شوارع نيويورك**: يقيم في فندق رخيص، ويسهر في الحانات، ويقع ضحية لابتزاز قوّاد المصعد وفتاة الليل ساني ويتعرض للضرب. يلتقي بصديقته السطحية سالي ويقترح عليها الهروب معاً للعيش في كوخ بغابات فيرمونت لكنها تسخر من خياله.
- **رمزية العنوان واللقاء مع فيبي**: يتسلل هولدن لشقة والديه ليلاً للقاء شقيقته الصغيرة الذكية فيبي ذات العشر سنوات. تواجهه فيبي بمرارته وسلبيته وتسأله عما يحب في هذه الحياة. يروي لها هولدن حلمه الرمزي: يتخيل آلاف الأطفال الصغار يلعبون في حقل شوفان كبير بجوار هاوية سحيقة، ومهمته الوحيدة أن يقف عند الحافة ليمسك بكل طفل قبل أن يسقط في الهاوية؛ ليكون "الحارس في حقل الشوفان".
- **مشهد لعبة الدوامة والمطر**: يقرر هولدن الهرب للغرب الأمريكي، فتفاجئه فيبي بحقيبتها مصرة على مرافقته. يرفض هولدن تدمير براءتها، ويأخذها لحديقة الحيوان لتركب لعبة الأحصنة الدوارة. وبينما يجلس في المطر المنهمر يراقب شقيقته تضحك وتحاول الإمساك بالحلقة الذهبية، تنفجر في صدره سعادة طاهرة طال انتظارها ويبكي فرحاً.
- **الخاتمة**: يتحدث هولدن من مصحة نفسية ليتعافى، نادماً على رواية قصته قائلاً جملته الوداعية: *"إياك أن تخبر أحداً بأي شيء في حياتك؛ فإن فعلت فستبدأ في الاشتياق للجميع"*.
"""
    },

    # 45 To Kill a Mockingbird
    {
        "id": "45_To_Kill_A_Mockingbird",
        "content_en": """# Comprehensive Study Guide: To Kill a Mockingbird
**Author:** Harper Lee  
**Year:** 1960  
**Genre:** Southern Gothic / Courtroom Drama / Social Justice  

---

## 1. Context & Moral Courage
Published on the cusp of the American Civil Rights Movement in 1960, Harper Lee's Pulitzer Prize-winning novel explores racial injustice, moral courage, and childhood innocence in 1930s Maycomb, Alabama.

---

## 2. In-Depth Chapter Breakdown
- **Growing Up in Maycomb**: Six-year-old Jean Louise "Scout" Finch, her older brother Jem, and summer friend Dill navigate childhood superstitions, fascinated by the neighborhood recluse **Boo Radley**, who leaves small treasures for them in a tree knot.
- **Atticus Finch's Moral Code**: Their widowed father, attorney Atticus Finch, teaches them profound empathy: *"You never really understand a person until you consider things from his point of view... until you climb into his skin and walk around in it."* When Atticus gives them air rifles, he tells them: *"Shoot all the bluejays you want, if you can hit 'em, but remember it's a sin to kill a mockingbird."* (Mockingbirds do nothing but sing their hearts out for humans; they harm no one).
- **The Trial of Tom Robinson**: Atticus is appointed to defend Tom Robinson, a gentle Black man falsely accused of raping a poor white woman, Mayella Ewell. Despite Atticus exposing in open court that Mayella's abusive, drunken father Bob Ewell beat her when he caught her trying to kiss Tom, the all-white jury convicts Tom due to ingrained racial prejudice. Tom is later shot and killed trying to escape prison.
- **The Attack and Boo's Intervention**: Humiliated by the trial, Bob Ewell vows vengeance. On Halloween night, Ewell ambushes Scout and Jem in the dark woods, breaking Jem's arm. Suddenly, a mysterious figure intervenes, wrestling Ewell and killing him with a kitchen knife. The savior carries Jem home—it is Boo Radley. Sheriff Heck Tate decides to protect the gentle Boo from publicity, insisting Ewell fell on his own knife. Scout walks Boo back to his porch, viewing the world from his perspective for the first time.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: لا تقتل عصفوراً ساخراً (To Kill a Mockingbird)
**المؤلف:** هاربر لي (Harper Lee)  
**سنة النشر:** 1960  
**التصنيف الأدبي:** الأدب الجنوبي الأمريكي / دراما المحاكم / العدالة الاجتماعية والعنصرية  

---

## 1. السياق التاريخي ورمزية العصفور الساخر
صدرت الرواية في ذروة حركة الحقوق المدنية في أمريكا لتنال جائزة بوليتزر؛ مصورة التمييز العنصري الصارم في بلدة ميكوم بولاية ألاباما في ثلاثينيات القرن العشرين. يرمز "طائر المحاكي" (العصفور الساخر) إلى الكائنات البريئة الوديعة التي لا تؤذي أحداً بل تغرد لتسعد الناس، وقتلها إثم عظيم.

---

## 2. التسلسل التفصيلي لمجريات الرواية
- **طفولة سكاوت وأسطورة بو رادلي**: تعيش الطفلة الذكية سكاوت (6 سنوات) مع شقيقها جيم ووالدها المحامي النبيل أتيكوس فينش. يفتن الأطفال بشخصية الجار الغامض المنعزل "بو رادلي"، الذي لا يغادر منزله أبداً ويضع لهم هدايا صغيرة في تجويف شجرة قديمة.
- **مبادئ أتيكوس فينش الأخلاقية**: يعلم أتيكوس طفليه جوهر الإنسانية: *"لن تفهم شخصاً بحق حتى تضع نفسك في مكانه، وترتدي جلده وتسير به"*، ويحذرهما عند الصيد: *"اقتلا ما شئتما من الطيور، لكن تذكرا دوماً أن قتل طائر المحاكي خطيئة كبرى؛ فهو لا يفسد الحقول بل يغني من قلبه للبشر"*.
- **محاكمة توم روبنسون**: يُعين أتيكوس للدفاع عن توم روبنسون، الشاب الأسود الطيب الذي لُفقت له تهمة اغتصاب الفتاة البيضاء ماييلا إيويل. يثبت أتيكوس في المحكمة بالدليل القاطع أن والد الفتاة السكير بوب إيويل هو من ضربها حين رآها تحاول تقبيل توم. ولكن بدافع التعصب العرقي الأعمى، تدين هيئة المحلفين البيضاء الشاب البريء. ويُقتل توم لاحقاً بالرصاص أثناء محاولته الهرب من السجن.
- **انتقام بوب إيويل وتضحية بو رادلي**: يشعر بوب إيويل بالخزي، فيقرر الانتقام من أتيكوس بقتل طفليه. وفي ليلة الهالوين، يهاجم الطفلين في الغابة المظلمة ويكسر ذراع جيم. وفجأة يتدخل رجل غامض ويصارع المعتدي ويطعنه بسكين دفاعاً عن الأطفال، ويحمل جيم الجريح إلى منزله؛ وكان هذا المنقذ هو "بو رادلي" نفسه! يقرر قائد الشرطة التستر على بو لحمايته من أضواء الشهرة القاسية، وتقود سكاوت بو إلى شرفة منزله متأملة العالم من نافذته لأول مرة في حياتها.
"""
    },

    # 46 Adventures of Huckleberry Finn
    {
        "id": "46_Adventures_Of_Huckleberry_Finn",
        "content_en": """# Comprehensive Study Guide: Adventures of Huckleberry Finn
**Author:** Mark Twain (Samuel Langhorne Clemens)  
**Year:** 1884  
**Genre:** Picaresque / Satire / Great American Novel  

---

## 1. Hemingway's Acclaim & Moral Conflict
Ernest Hemingway famously wrote: *"All modern American literature comes from one book by Mark Twain called Huckleberry Finn."* Twain stages a profound conflict between Huck’s "sound heart" (innate human empathy) and his "deformed conscience" (societal conditioning that claimed slavery was God-ordained).

---

## 2. In-Depth Chapter Breakdown
- **Flight from Pap**: Escaping the abusive, drunken clutches of his racist father Pap, young Huck Finn fakes his own murder and flees to Jackson's Island on the Mississippi River. There, he discovers Jim, Miss Watson's runaway slave, fleeing sale down the river.
- **The Raft on the Mississippi**: Building a wooden raft, Huck and Jim journey down the Mississippi River toward Cairo to reach free states. The river represents pastoral freedom and authentic brotherhood, contrasted with the violent, hypocritical towns on shore.
- **The Grangersons and the Scoundrels**: Huck witnesses the absurd, bloody family feud between the Grangerfords and Shepherdsons, where devout churchgoers slaughter one another. Later, two con men—"The Duke" and "The King"—take over the raft, running fraudulent Shakespeare shows and attempting to swindle orphaned girls out of their inheritance (The Wilks family).
- **The Climax of the Moral Soul**: When the King betrays Jim and sells him for forty dollars, Huck writes a letter to Miss Watson to turn Jim in, believing his Sunday-school training that helping a runaway slave leads to hell. Huck pauses, recalls Jim's immense kindness, tears up the letter, and declares: *"All right, then, I'll go to hell!"*
- **Resolution**: Arriving at the Phelps farm, Tom Sawyer appears and constructs an overly elaborate, dangerous mock-escape plan for Jim. In the end, it is revealed Miss Watson died and freed Jim in her will. Huck resolves to head out to the Western territory ahead of the rest, refusing to let Aunt Sally "sivilize" him.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: مغامرات هكلبيري فن (Adventures of Huckleberry Finn)
**المؤلف:** مارك توين (Mark Twain)  
**سنة النشر:** 1884  
**التصنيف الأدبي:** الأدب الكلاسيكي الأمريكي / الهجاء الاجتماعي / الرواية الصعلوكية  

---

## 1. شهادة هيمنغواي والصراع الأخلاقي
قال إرنست هيمنغواي مقولته الشهيرة: *"كل الأدب الأمريكي الحديث ينبع من كتاب واحد لمارك توين اسمه هكلبيري فن"*. يقدم توين صراعاً فكرياً عبقرياً بين "فطرة القلب السليمة" لدى هك، وبين "الضمير المجتمعي المشوه" الذي ربته الكنيسة والمجتمع الجنوبي على أن مساعدة العبيد إثم يستوجب دخول النار.

---

## 2. المسار الدرامي لرحلة النهر
- **الهروب من الأب السكير**: يهرب الصبي المشرد هكلبيري فن من والده العنيف السكير بعد أن يزيف مقتله، ويلجأ لجزيرة جاكسون في نهر الميسيسيبي. يلتقي هناك بالعبد الهارب "جيم" الذي فر بعد أن علم بنية مالكته بيعه في أسواق الجنوب.
- **الطوف ونهر الميسيسيبي**: يبني هك وجيم طوفاً خشبياً ويبحران عبر النهر طلباً للحرية في الولايات الشمالية. يمثل النهر رمز البراءة والأخوة الإنسانية النقية في مواجهة فساد ونفاق المدن الشاطئية.
- **المعارك العائلية والمحتالان**: يشهد هك النزاع الدموي العبثي بين عائلتي غرانجرفورد وشيباردسون؛ حيث يذهب أفراد العائلتين للكنيسة ببنادقهم ثم يقتلون بعضهم في الشوارع. ثم يقتحم الطوف محتالان يدعيان أنهما "الدوق والملك"، ويقومان بالنصب والاحتيال في البلدات ومحاولة سرقة ميراث فتيات يتيمات.
- **الذروة الأخلاقية الخالدة (سأذهب إلى الجحيم!)**: يبيع المحتالان جيم مقابل 40 دولاراً. يكتب هك رسالة لمالكة جيم ليبلغها بمكانه ظناً منه أن مساعدة عبد هارب معصية دينية. يتوقف هك، ويتذكر محبة جيم وحنانه عليه طوال الرحلة، فيمزق الرسالة بحزم معلناً: *"حسناً إذن.. سأذهب إلى الجحيم!"*، مفضلاً لعنة المجتمع على خيانة صديقه.
- **الخاتمة**: يصل هك لمزرعة فيلبس ويلتقي بصديقه توم سوير، وينقذان جيم ليكتشفوا أن مالكته توفيت وأعتقت جيم في وصيتها. ويقرر هك الرحيل نحو الغرب الأمريكي رافضاً كل محاولات المجتمع "لتمدينه" وتدجينه.
"""
    },

    # 47 The Grapes of Wrath
    {
        "id": "47_The_Grapes_Of_Wrath",
        "content_en": """# Comprehensive Study Guide: The Grapes of Wrath
**Author:** John Steinbeck  
**Year:** 1939  
**Genre:** Social Realism / Dust Bowl Epic / Great Depression Literature  

---

## 1. Historical Crucible & The Biblical Exodus
Winner of the Pulitzer Prize and National Book Award, Steinbeck tracks the displacement of thousands of tenant farming families ("Okies") during the 1930s Dust Bowl and Great Depression. The novel serves as a modern American Exodus, moving from environmental disaster across Route 66 toward the promised land of California, which reveals itself as an exploitative corporate trap.

---

## 2. In-Depth Chapter Breakdown
- **Tom Joad & Jim Casy**: Released from McAlester prison on parole for manslaughter, Tom Joad returns to Oklahoma to find his family's farm seized by banks and bulldozers. He reunites with ex-preacher Jim Casy, who abandoned dogma to follow a humanist belief that all mankind shares one vast, collective oversoul.
- **The Route 66 Exodus**: The Joad family (Grampa, Granma, Pa, Ma, pregnant Rose of Sharon, and siblings) pile into a decrepit Hudson truck along Route 66. Grampa and Granma perish along the harsh desert route and are buried by the roadside. Ma Joad emerges as the unshakeable rock holding the disintegrating family together.
- **The California Illusion & Hoovervilles**: Arriving in California, the Joads find hundreds of thousands of starving migrants competing for starvation wages. Corporate agribusiness landowners control the police, violently suppressing migrant organizing and branding desperate workers "Reds."
- **Casy's Martyrdom & Tom's Vow**: At a peach orchard strike, Jim Casy organizes workers. Strike-breakers corner Casy and crush his skull with a pickax handle. Tom Joad strikes back, killing Casy's murderer and fleeing into hiding. Hiding in a cave, Tom bids farewell to Ma Joad, delivering his immortal promise to carry forward Casy's spirit: *"Wherever they's a fight so hungry people can eat, I'll be there. Wherever they's a cop beatin' up a guy, I'll be there... I'll be in the way guys yell when they're mad an'—I'll be in the way kids laugh when they're hungry n' know supper's ready."*
- **The Transcendent Ending**: Trapped by torrential floods, Rose of Sharon gives birth to a stillborn baby. Taking shelter in a barn, they find a starving boy and his dying elderly father. In the novel's breathtaking final act, Rose of Sharon offers her breast to the starving stranger, feeding him with her milk, gazing across the barn with a mysterious, transcendent smile.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: عناقيد الغضب (The Grapes of Wrath)
**المؤلف:** جون شتاينبك (John Steinbeck)  
**سنة النشر:** 1939  
**التصنيف الأدبي:** الواقعية الاجتماعية الملحمية / أدب الكساد الكبير وعاصفة الغبار  

---

## 1. السياق التاريخي ورحلة الخروج الأمريكية
توجت هذه الرواية بجائزة بوليتزر ونوبل؛ وتوثق مأساة طرد آلاف المزارعين من أراضيهم في أوكلاهوما خلال الكساد الكبير وجفاف "قصعة الغبار" في ثلاثينيات القرن العشرين. تشبه الرواية رحلة خروج توراتية عبر الطريق 66 نحو "أرض الميعاد" المزعومة في كاليفورنيا، التي تتبدى كمصيدة رأسمالية شرسة تطحن كرامة العمال.

---

## 2. المسار الدرامي لعائلة جود
- **توم جود وجيم كيسي**: يخرج توم جود من السجن بعفو مشروط ليعود لمزرعة عائلته فيجدها مهجورة جرفتها الجرافات لصالح البنوك. يلتقي بالقس السابق جيم كيسي الذي ترك الكنيسة مؤمناً بأن البشرية كلها روح واحدة مشتركة.
- **رحلة الشقاء عبر الطريق 66**: تحزم عائلة جود (الجد، الجدة، الأب، الأم، والابنة الحامل روز أوف شارون وبقية الأبناء) أمتعتها في شاحنة متهالكة نحو الغرب. يموت الجد والجدة في الطريق الصحراوي القاسي ويُدفنان على قارعة الطريق، وتبرز "الأم جود" كعمود خيمة صلب يحافظ على بقاء وتماسك الأسرة.
- **وهم كاليفورنيا ومخيمات الجوع**: يصل المهاجرون لكاليفورنيا ليجدوا مئات الآلاف من الجياع يتنافسون على أجور بخسة لا تكفي لشراء الخبز، بينما تسيطر كبرى الشركات الزراعية على الشرطة وتقمع أي مطالبة بحقوق العمال متهمة إياهم بالشيوعية.
- **استشهاد كيسي وعهد توم الخالد**: ينظم جيم كيسي إضراباً للعمال في مزارع الخوخ، فيهجم عليه حراس المزارع ويهشمون رأسه بفأس. يثور توم جود ويقتل قاتل كيسي ويهرب مطارداً. وفي مخبئه المظلم، يودع والدته ويلقي عهده الخالد لحمل راية كيسي والدفاع عن المظلومين: *"أينما كان هناك صراع ليأكل الجياع، سأكون هناك. أينما ضرب شرطي رجلاً فقيراً، سأكون هناك... سأكون في صرخة المظلومين حين يغضبون، وفي ضحكة الأطفال الجائعين حين يعلمون أن العشاء جاهز"*.
- **المشهد الختامي الأسطوري**: تحاصر الفيضانات العائلة، وتضع روز أوف شارون جنيناً ميتاً. يلجأون لحظيرة مهجورة ليجدوا طفلاً يبكي بجوار والده الشيخ الذي يوشك على الموت جوعاً. وفي مشهد إنساني مهيب يخلد الرواية، تحتضن روز أوف شارون الشيخ العجوز الجائع وترضعه من حليب ثديها، ناظرة في الأفق بابتسامة خلاص وسلام روحي يتحدى الموت.
"""
    },

    # 48 The Sound and the Fury
    {
        "id": "48_The_Sound_And_The_Fury",
        "content_en": """# Comprehensive Study Guide: The Sound and the Fury
**Author:** William Faulkner  
**Year:** 1929  
**Genre:** Modernist Masterpiece / Southern Gothic / Stream of Consciousness  

---

## 1. Title Origin & Modernist Revolution
Taking its title from Shakespeare's *Macbeth* (*"Life's but a walking shadow... It is a tale told by an idiot, full of sound and fury, signifying nothing"*), Faulkner chronicles the tragic decline of the aristocratic Compson family of Jefferson, Mississippi across four distinct consciousnesses.

---

## 2. The Four Perspectives Breakdown
- **April 7, 1928 (Benjy's Section)**: Narrated through the non-linear, fragmented consciousness of 33-year-old Benjy Compson, who has severe intellectual disabilities. Lacking any concept of time, Benjy experiences past and present simultaneously through sensory triggers (smells, sounds, the pasture sold to send Quentin to Harvard). His anchor is his beloved sister Caddy, who smelled like trees.
- **June 2, 1910 (Quentin's Section)**: Narrated on the day of his suicide at Harvard. Quentin is an agonizingly neurotic, romantic intellectual obsessed with southern aristocratic honor and the virginity of his sister Caddy. Unable to accept Caddy's pregnancy and wedding to a fraud, Quentin breaks the hands off his grandfather's watch, wanders Boston with a little Italian girl, and drowns himself in the Charles River weighted down by flatirons.
- **April 6, 1928 (Jason's Section)**: Narrated by Jason IV, the bitter, cynical, venomously racist and materialistic brother who manages a farm-supply store. Jason relentlessly steals the support money Caddy sends for her illegitimate daughter, Miss Quentin, keeping it locked in his desk.
- **April 8, 1928 (Easter Sunday - Dilsey's Section)**: Written in objective third-person, focusing on Dilsey, the faithful Black family cook who holds the shattered remnants of the household together. Dilsey attends an Easter church service with Benjy, moved to tears: *"I've seed de first en de last."* Miss Quentin climbs down a pear tree with a carnival worker, stealing back all the money Jason robbed from her, leaving Jason humiliated and furious.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: الصخب والعنف (The Sound and the Fury)
**المؤلف:** وليام فوكنر (William Faulkner)  
**سنة النشر:** 1929  
**التصنيف الأدبي:** قمة الحداثة الأدبية / تيار الوعي المركب / الأدب الجنوبي الأمريكي  

---

## 1. دلالة العنوان والثورة الفوكنرية
استلهم فوكنر عنوان روايته من مسرحية شكسبير *ماكبث* (*"الحياة ظل عابر... حكاية يرويها معتوه، ملؤها الصخب والعنف، ولا تعني أي شيء"*). يسجل فوكنر الانهيار المروع لعائلة كومبسون الأرستقراطية العريقة في مسيسيبي عبر أربعة أصوات وتيارات وعي متباينة.

---

## 2. الأصوات الأربعة الكبرى للرواية
- **7 أبريل 1928 (فصل بنجي المعاق)**: يُروى عبر تيار الوعي المعقد للشاب بنجي (33 عاماً) المصاب بإعاقة ذهنية كاملة. لا يملك بنجي أي إدراك زمني؛ فالماضي والحاضر يندمجان في حواسه عبر الروائح والأصوات. محوره العاطفي الوحيد هو شقيقته كادي التي *"كانت رائحتها كرائحة الأشجار"*.
- **2 يونيو 1910 (فصل كوينتين والانتحار)**: يُروى في اليوم الأخير من حياة كوينتين قبل انتحاره في جامعة هارفارد. طالب جامعي معذب بفكرة الشرف الجنوبي وعذرية أخته كادي. يعجز عن تقبل سقوط شقيقته وخطيئتها وزواجها؛ فيحطم عقارب ساعته ويتجول في شوارع بوسطن ثم يغرق نفسه في النهر محملاً بالمكاوي الثقيلة.
- **6 أبريل 1928 (فصل جيسون الحاقد)**: يُروى بلسان جيسون الرابع؛ الأخ المادي القاسي الأناني المشحون بالحقد، الذي يعمل موظفاً في متجر زراعي. يسرق جيسون طوال سنوات الأموال التي ترسلها كادي سراً لتربية ابنتها غير الشرعية "ميس كوينتين".
- **8 أبريل 1928 (أحد الفصح - فصل ديلسي الخاتم)**: سرد موضوعي يركز على "ديلسي"، الطاهية الإفريقية العجوز الصبورة التي تتحمل حماقات العائلة المنهارة. تأخذ بنجي لكنيسة الزنوج في أحد الفصح وتبكي تأثراً قائلة: *"لقد رأيت البداية والنهاية"*. وفي تلك الليلة، تهرب الفتاة كوينتين مع رجل السيرك متسلقة الشجرة، وسارقة كل أموالها التي اختلسها جيسون، تاركة إياه يغلي في خيبته وهزيمته.
"""
    },

    # 49 Lolita
    {
        "id": "49_Lolita",
        "content_en": """# Comprehensive Study Guide: Lolita
**Author:** Vladimir Nabokov  
**Year:** 1955  
**Genre:** Modernist Masterpiece / Unreliable Narrator / Tragedy & Satire  

---

## 1. Context & The Ultimate Unreliable Narrator
Nabokov crafts a tour-de-force of glittering English prose narrated by Humbert Humbert, an erudite European literature scholar and predatory pedophile. The novel is not an erotic romance, but an agonizing dissection of monstrous obsession, exploitation, and the tragic destruction of a child's stolen life.

---

## 2. In-Depth Narrative Breakdown
- **The Obsession with Nymphets**: Humbert Humbert, traumatized by the childhood death of his first love Annabel Leigh, rationalizes his predatory fixation on girls aged 9 to 14, whom he terms "nymphets." Renting a room in Ramsdale, New Hampshire, he meets 12-year-old Dolores "Lolita" Haze and is instantly ensnared.
- **The Marriage to Charlotte**: Humbert marries Lolita’s widowed, pretentious mother Charlotte strictly to remain near the child. Charlotte discovers Humbert’s diary detailing his lust for Lolita; running into the street in shock, she is struck and killed by a car.
- **The Cross-Country Motel Captivity**: Humbert collects Lolita from summer camp, seduces her at the Enchanted Hunters motel, and drags her on a claustrophobic one-year road trip across American motels and tourist traps, manipulating and emotionally imprisoning her while she weeps secretly in pillows every night.
- **The Doppelgänger (Clare Quilty)**: Lolita is secretly abducted by Clare Quilty, a depraved playwright who stalked them. Humbert spends years obsessively searching for them.
- **The Final Reckoning**: Three years later, Humbert receives a letter from a married, impoverished, pregnant 17-year-old Dolores. Visiting her, Humbert sees the woman she became, stripped of all nymph fantasy, and realizes for the first time his genuine love and the monstrous horror of the childhood he stole from her. Humbert tracks down Quilty to his mansion and shoots him in a surreal, grotesque murder. Humbert dies of coronary thrombosis in prison awaiting trial.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: لوليتا (Lolita)
**المؤلف:** فلاديمير نابوكوف (Vladimir Nabokov)  
**سنة النشر:** 1955  
**التصنيف الأدبي:** قمة النثر الحداثي / الراوي غير الموثوق / تراجيديا الهوس والاستغلال  

---

## 1. السياق وأسلوب الراوي المخادع
أبدع نابوكوف تحفة لغوية وبلاغية فائقة بلسان "همبرت همبرت"؛ الأكاديمي الأوروبي المثقف والمتحرش الشرير. لا تعد الرواية عملاً رومانسياً ولا إباحياً، بل هي تشريح نفسي مرعب لوحشية الهوس، وكيف يغلف المجرم جرائمه ببلاغة زائفة بينما يدمر طفولة بريئة ويسرق حياتها.

---

## 2. المسار الدرامي لمحطات الرواية
- **هوس الحوريات**: يبرر همبرت انحرافه النفسي بصدمة موت حبيبته الأولى في الطفولة، مطوراً هوساً بالفتيات الصغيرات اللاتي يسميهن "الحوريات". يستأجر غرفة في نيو هامبشاير ويلتقي بالطفلة دولوريس هيز (لوليتا) ذات الـ 12 عاماً.
- **الزواج من شارلوت**: يتزوج همبرت من والدة لوليتا الأرملة المتصنعة فقط ليبقى قريباً من الطفلة. تكتشف الأم مذكراته الفاضحة وتهرع للشارع في صدمة فتصدمها سيارة وتموت فوراً.
- **رحلة الاختطاف عبر الموتيلات**: يأخذ همبرت لوليتا من المخيم الصيفي ويتحرش بها في فندق "الصيادين المسحورين"، ويجبرها على رحلة استمرت عاماً كاملاً عبر فنادق أمريكا ومخيماتها، حابساً إياها في سجن عاطفي خانق بينما تبكي الطفلة ليلاً في وسادتها سراً.
- **القرين الشرير (كلير كويلتي)**: تختطف لوليتا سراً على يد الكاتب المسرحي الفاسق كلير كويلتي الذي كان يطاردهما في الخفاء. يقضي همبرت سنوات في مطاردة أثرهما.
- **المواجهة الأخيرة والاعتراف**: بعد سنوات يتلقى همبرت رسالة من دولوريس؛ أصبحت الآن شابة في السابعة عشرة، متزوجة من عامل بسيط وحاملاً في فقر مدقع. يزورها همبرت ليرى المرأة الحقيقية بعد أن زال كل وهم "الحورية"، ويدرك لأول مرة فداحة الجريمة التي ارتكبها بحق طفولتها. يطارد كويلتي ويقتله بالرصاص في قصره، ويموت همبرت بنوبة قلبية في السجن قبل محاكمته.
"""
    },

    # 50 Beloved
    {
        "id": "50_Beloved",
        "content_en": """# Comprehensive Study Guide: Beloved
**Author:** Toni Morrison  
**Year:** 1987  
**Genre:** Magical Realism / Historical Trauma / Masterpiece of African American Literature  

---

## 1. Historical Basis & The Trauma of Slavery
Winner of the Pulitzer Prize, Toni Morrison based *Beloved* on the historical case of Margaret Garner, an escaped slave who killed her own infant daughter rather than allow her to be returned to the horrors of chattel slavery. Morrison interrogates "rememory"—how unresolved collective trauma haunts individuals and communities.

---

## 2. In-Depth Chapter Breakdown
- **124 Bluestone Road**: Set in 1873 Cincinnati, Ohio. House 124 is spiteful, haunted by the vengeful ghost of Sethe’s unnamed baby daughter whose tombstone bears only the single word: **Beloved**. Sethe lives in ostracization with her teenage daughter Denver.
- **Paul D's Arrival**: Paul D, a fellow survivor from the Sweet Home plantation in Kentucky, arrives and drives the poltergeist out of the house, beginning a relationship with Sethe.
- **The Physical Manifestation**: A mysterious young woman with flawless skin, dressed in black, emerges from the water and appears on the porch, calling herself "Beloved." She has no memory except a desperate hunger for Sethe.
- **The Terrible Truth (The Shed)**: Schoolteacher (the sadistic master of Sweet Home) tracked Sethe to Ohio. Cornered in a woodshed, Sethe slit her two-year-old daughter's throat with a handsaw and attempted to kill her other children to save them from slavery. Paul D learns the truth and departs in horror.
- **The Exorcism**: Beloved becomes a parasitic, consuming tyrant, swelling as Sethe wastes away in guilt. Denver bravely reaches out to the Black community of Cincinnati for help. Led by Ella, thirty neighborhood women gather outside 124, singing and praying. In a collective ritual of spiritual redemption, they banish Beloved's ghost forever. Paul D returns, taking Sethe’s hand and declaring: *"You your best thing, Sethe. You are."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: المحبوبة (Beloved)
**المؤلف:** توني موريسون (Toni Morrison)  
**سنة النشر:** 1987  
**التصنيف الأدبي:** الواقعية السحرية / أدب الصدمة التاريخية / درة الأدب الإفريقي الأمريكي  

---

## 1. الأساس التاريخي ومأساة الاستعباد
نالت توني موريسون عن هذه الرواية جائزتي بوليتزر ونوبل. استندت موريسون إلى القصة الحقيقية لمارغريت غارنر؛ وهي أم مستعبدة هربت من مزارع الجنوب وقتلت طفلتها الرضيعة بيدها لتنقذها من العودة إلى جحيم الاستعباد. تستكشف الرواية مفهوم "استعادة الذاكرة" (Rememory) وكيف تظل صدمات التاريخ تطارد الأرواح.

---

## 2. المسار الدرامي لأحداث الرواية
- **المنزل رقم 124 في سينسيناتي**: يبدأ السرد عام 1873؛ المنزل مسكون بروح شريرة غاضبة لشظايا طفلة مقتولة حُفرت على شاهد قبرها كلمة واحدة: **المحبوبة (Beloved)**. تعيش الأم سيث في عزلة تامة ونبذ اجتماعي مع ابنتها المراهقة دنفر.
- **وصول بول دي**: يصل بول دي، رفيق سيث القديم والناجي من ويلات مزرعة "سويت هوم"، ويطرد الروح الشريرة من المنزل، محاولاً بناء حياة جديدة مع سيث.
- **تجسد المحبوبة**: تخرج من النهر فتاة شابة غامضة ترتدي ثياباً سوداء وتسمي نفسها "المحبوبة". تسكن معهما في المنزل وتبدي تعلقاً مرضياً جارفاً بسيث.
- **حقيقة الحظيرة المروعة**: عندما طارد النخاسون سيث وأطفالها للقبض عليهم وإعادتهم للاستعباد، حبست نفسها في الحظيرة وذبحت طفلتها الرضيعة ذات السنتين بمنشار لإنقاذها من الاستعباد وحاولت قتل بقية أطفالها. يصدم بول دي بالحقيقة ويهرب من المنزل.
- **التطهير والخلاص الجمعي**: تتحول المحبوبة إلى كائن طفيلي يمتص طاقة سيث التي تذبل تحت وطأة الشعور بالذنب. تخرج الابنة دنفر لطلب العون من نساء المجتمع الإفريقي في البلدة. تجتمع 30 امرأة أمام المنزل في صلاة وغناء جماعي مهيب يطرد شبح المحبوبة للأبد. يعود بول دي ويمسك بيد سيث المنهكة قائلاً كلمته الخالدة: *"أنتِ أثمن ما تملكين يا سيث، أنتِ كنزكِ الحقيقي"*.
"""
    },

    # 53 The Old Man and the Sea
    {
        "id": "53_The_Old_Man_And_The_Sea",
        "content_en": """# Comprehensive Study Guide: The Old Man and the Sea
**Author:** Ernest Hemingway  
**Year:** 1952  
**Genre:** Philosophical Novella / Parable / Heroic Realism  

---

## 1. Context & The Iceberg Theory
Hemingway's Pulitzer Prize-winning masterpiece and catalyst for his 1954 Nobel Prize. Employing his famous "Iceberg Theory" of prose, Hemingway strips away ornament to tell a universal parable of human endurance, dignity, and indomitable courage.

---

## 2. In-Depth Chapter Breakdown
- **84 Days Without a Fish**: Santiago, an aged, weathered Cuban fisherman in the Gulf Stream, has gone eighty-four days without taking a fish (*salao*—the worst form of unlucky). His devoted young apprentice, Manolin, is forbidden by his parents to sail with him, but still loves and feeds him. Santiago dreams only of the lions playing on the white beaches of Africa.
- **The Hooking of the Marlin**: On the eighty-fifth day, Santiago ventures far out into the deep waters of the Gulf Stream alone. At noon, an eighteen-foot giant blue marlin takes his bait. The colossal fish pulls Santiago's small skiff northward for two days and nights. Santiago endures cut hands, extreme cramping, exhaustion, and hunger, treating the noble fish with immense brotherly respect: *"I love you and respect you very much. But I will kill you dead before this day ends."*
- **The Victory**: On the third day, the exhausted marlin circles. Santiago summons his last reserve of strength and drives his harpoon through its heart. He lashes the magnificent giant to the side of his skiff and sets sail for Havana.
- **The Sharks & The Battle**: An hour later, the scent of blood draws a Mako shark (*Dentuso*). Santiago kills it with his harpoon, losing the weapon. Packs of shovel-nosed sharks attack the carcass throughout the night. Santiago fights with a knife lashed to an oar, then a club, then the tiller, uttering his immortal maxim:  
  **"Man is not made for defeat. A man can be destroyed but not defeated."**  
  The sharks strip every ounce of flesh from the fish.
- **Return and Legacy**: Santiago stumbles ashore in the darkness, carrying his heavy mast up to his shack like Christ carrying the cross, collapsing into sleep. In the morning, fishermen and tourists marvel at the giant 18-foot skeleton lashed to the boat. Manolin sits crying beside the sleeping old man, promising they will fish together again. Santiago dreams of the lions.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: العجوز والبحر (The Old Man and the Sea)
**المؤلف:** إرنست هيمنغواي (Ernest Hemingway)  
**سنة النشر:** 1952  
**التصنيف الأدبي:** نوفيلا فلسفية / أدب الصمود والبطولة الإنسانية / رمزية الكفاح  

---

## 1. السياق ونظرية جبل الجليد
الرواية التي منحت هيمنغواي جائزتي بوليتزر ونوبل للآداب. يطبق فيها "نظرية جبل الجليد" حيث يختزل النثر إلى أقصى درجات البساطة والدقة، ليقدم أسطورة ملحمية خالدة عن كرامة الإنسان وصموده الخارق أمام قوى الطبيعة والشيخوخة.

---

## 2. التسلسل الدرامي لأحداث الملحمة البحرية
- **84 يوماً بلا سمكة**: سانتياغو صياد كوبي عجوز في خليج المكسيك، عانده الحظ ولم يصطد سمكة واحدة طوال 84 يوماً. يمنعه والدا الصبي الوفي "مانولين" من مرافقته، لكن الصبي يظل مخلصاً للعجوز، يطعمه ويساعده. ينام العجوز ليحلم بالأسود وهي تلعب على شواطئ إفريقيا البيضاء.
- **صيد سمكة المارلين العملاقة**: في اليوم الخامس والثمانين، يبحر سانتياغو بمفرده بعيداً في المياه العميقة. في الظهيرة، تعلق بالصنارة سمكة مارلين زرقاء هائلة يبلغ طولها 18 قدماً. تجر السمكة القارب الصغير ليومين وليلتين نحو الشمال. يعاني العجوز من نزيف يديه، وتقلص عضلاته، والجوع والإرهاق، معاملاً السمكة بنبل وإخاء: *"أنا أحبك وأحترمك جداً، لكني سأقتلك حتماً قبل أن ينتهي هذا اليوم"*.
- **الظفر والانتصار الملحمي**: في اليوم الثالث، تدور السمكة حول القارب منهكة. يجمع العجوز كل ما تبقى في جسده العجوز من قوة، ويغرس رمحه في قلب السمكة. يربط السمكة الهائلة بجانب زورقه ويبحر نحو هافانا في نشوة انتصار.
- **هجوم القروش والصراع حتى الرمق الأخير**: تجذب رائحة الدماء قرش الماكو، فيقتله العجوز برمحه الذي يضيع في البحر. تهاجم أسراب قروش الشوفيل الجثة في الليل. يقاتل سانتياغو بسكين مربوط بمجداف، ثم بهراوة، ثم بذراع الدفة، مطلقاً مقولته الخالدة التي تلخص وجود الإنسان:  
  **"الإنسان لم يُخلق للهزيمة.. يمكن تدمير الإنسان، لكن لا يمكن هزيمته!"**  
  تلتهم القروش كل لحم السمكة، ولا تترك سوى هيكلها العظمي الأبيض.
- **العودة وحلم الأسود**: يدخل العجوز الميناء في الظلام، ويحمل صاري قاربه الثقيل على كتفه كالمسيح حاملاً صليبه، ويسقط في نوم عميق في كوخه. في الصباح، يتجمع الصيادون في ذهول حول الهيكل العظمي العملاق (18 قدماً)، ويبكي الصبي مانولين عند فراش العجوز معاهداً إياه على الصيد معاً مجدداً. وينام العجوز، وهو يحلم بالأسود.
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
