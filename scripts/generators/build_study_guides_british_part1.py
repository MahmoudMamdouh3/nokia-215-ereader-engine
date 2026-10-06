"""
Generates master-level study guides for British & Irish Literature (Part 1):
- 28_Ulysses
- 30_Animal_Farm
- 31_Pride_And_Prejudice
- 32_Wuthering_Heights
- 33_Jane_Eyre
- 34_Great_Expectations
- 35_David_Copperfield
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 28 Ulysses
    {
        "id": "28_Ulysses",
        "content_en": """# Comprehensive Study Guide: Ulysses
**Author:** James Joyce  
**Year:** 1922  
**Genre:** Modernist Epic / Stream of Consciousness  

---

## 1. Homeric Parallel & Literary Revolution
Set entirely across a single day—Thursday, June 16, 1904 ("Bloomsday")—in Dublin, Ireland, *Ulysses* parallels Homer's *Odyssey*. Joyce maps the ordinary, mundane experiences of modern city dwellers onto ancient mythological archetypes:
- **Leopold Bloom** = Odysseus (The Wandering Hero)
- **Stephen Dedalus** = Telemachus (The Searching Son)
- **Molly Bloom** = Penelope (The Faithful/Fleshly Wife)

---

## 2. In-Depth Episode-by-Episode Breakdown (The 18 Episodes)

### The Telemachia (Episodes 1–3)
- **1. Telemachus (8:00 AM)**: At the Sandycove Martello tower, Stephen Dedalus, an introspective young artist in mourning for his mother, is mocked by medical student Buck Mulligan and an English guest, Haines. Stephen feels evicted from his own home.
- **2. Nestor (10:00 AM)**: Stephen teaches a history lesson at a Dalkey school and debates history and Irish nationalism with the unionist headmaster Mr. Deasy: *"History is a nightmare from which I am trying to awake."*
- **3. Proteus (11:00 AM)**: Walking alone along Sandymount Strand, Stephen contemplates philosophical perception (*"ineluctable modality of the visible"*), time, and linguistic creation.

### The Odyssey (Episodes 4–15)
- **4. Calypso (8:00 AM)**: Leopold Bloom prepares breakfast and pork kidneys for his wife Molly at 7 Eccles Street. He brings her breakfast in bed, including a letter from her concert manager and lover, Blazes Boylan.
- **5. Lotus Eaters (10:00 AM)**: Bloom wanders Dublin, collects a clandestine letter under the pseudonym "Henry Flower," visits All Hallows church, and bathes.
- **6. Hades (11:00 AM)**: Bloom attends the funeral of Paddy Dignam at Glasnevin Cemetery with Stephen's father Simon Dedalus. Bloom contemplates death, decay, and his deceased infant son Rudy.
- **7. Aeolus (12:00 PM)**: At the *Freeman's Journal* newspaper office, Bloom tries to place an advertisement amidst journalistic wind and rhetoric.
- **8. Lestrygonians (1:00 PM)**: Bloom seeks lunch, repulsed by the animalistic gluttony at the Burton Restaurant, settling on a gorgonzola sandwich and burgundy at Davy Byrne's pub.
- **9. Scylla and Charybdis (2:00 PM)**: At the National Library, Stephen expounds his biographical theory of Shakespeare's *Hamlet* to literary scholars. Bloom passes between them.
- **10. Wandering Rocks (3:00 PM)**: Nineteen short vignettes capturing simultaneous cross-sections of Dublin city life.
- **11. Sirens (4:00 PM)**: At the Ormond Hotel, two barmaids flirt while Bloom listens to singing, his thoughts overwhelmed by knowing Boylan is arriving at Molly's bed.
- **12. Cyclops (5:00 PM)**: In Barney Kiernan's pub, a xenophobic Irish nationalist ("The Citizen") attacks Bloom's Jewish heritage. Bloom defends universal love and human dignity before escaping a hurled biscuit tin.
- **13. Nausicaa (8:00 PM)**: At Sandymount Strand, Bloom watches young Gerty MacDowell, their shared voyeuristic gaze set against fireworks.
- **14. Oxen of the Sun (10:00 PM)**: At the National Maternity Hospital, Mina Purefoy endures a grueling 3-day labor. Joyce writes the episode in 32 historical prose styles evolving from Anglo-Saxon to modern slang. Stephen and Bloom finally meet and drink together.
- **15. Circe (Midnight)**: In Dublin's red-light district ("Nighttown"), written as an expressionist theatrical script. Stephen and Bloom confront their deepest subconscious hallucinations, guilts, and phobias. Bloom protects Stephen from British soldiers.

### The Nostos (Episodes 16–18)
- **16. Eumaeus (1:00 AM)**: Bloom guides the exhausted Stephen to a cabman's shelter for coffee and stale buns.
- **17. Ithaca (2:00 AM)**: Written in clinical, scientific catechism (question-and-answer). Bloom brings Stephen home to 7 Eccles Street, where they drink cocoa in the kitchen and urinate together under the stars. Stephen departs into the night.
- **18. Penelope (Molly's Soliloquy)**: Molly lies awake in bed, delivering an eight-sentence, unpunctuated stream-of-consciousness monologue spanning over 40 pages, closing with her ecstatic affirmation of love and life: *"and yes I said yes I will Yes."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: عوليس (Ulysses)
**المؤلف:** جيمس جويس (James Joyce)  
**سنة النشر:** 1922  
**التصنيف الأدبي:** قمة الأدب الحداثي العالمي / تيار الوعي / الملحمة الرمزية  

---

## 1. التناص مع ملحمة هوميروس والثورة الجويسية
تدور أحداث الرواية بالكامل في يوم واحد فقط: الخميس 16 يونيو 1904 في دبلن بأيرلندا (وهو اليوم المعروف عالمياً بـ "يوم بلوم Bloomsday"). يعيد جويس صياغة أوديسة هوميروس الإغريقية داخل تفاصيل الحياة اليومية العادية:
- **ليوبولد بلوم** = أوديسيوس (البطل التائه المتسامح)
- **ستيفن ديدالوس** = تليماك (الابن الباحث عن أب روحي)
- **مولي بلوم** = بينيلوبي (الزوجة والجسد الإنساني الحي)

---

## 2. التحليل التفصيلي للحلقات الثماني عشرة (Episodes 1–18)

### التليماكيا (الفصول 1–3)
- **1. تليماك (8:00 صباحاً)**: في برج مارتيلو على البحر، يعيش ستيفن الشاب الفنان المثقف المعذب بموت أمه، وسط سخرية رفيقه الطبيب باكل موليجان والضيف الإنجليزي هينز.
- **2. نستور (10:00 صباحاً)**: يدرس ستيفن التاريخ لتلاميذ المدرسة ويحاور المدير مستر ديسي حول القومية والتاريخ قائلاً: *"التاريخ كابوس أحاول الاستيقاظ منه"*.
- **3. بروتيوس (11:00 صباحاً)**: يمشي ستيفن وحيداً على شاطئ البحر سابحاً في تيار الوعي الفلسفي حول الإدراك الحسي واللغة والوجود.

### الأوديسة (الفصول 4–15)
- **4. كاليبسو (8:00 صباحاً)**: يظهر ليوبولد بلوم في منزله يجهز إفطار الكلى المقلية لزوجته مولي، ويصعد لها الإفطار ورسالة من مدير حفلاتها وعشيقها بويبلان.
- **5. آكلو اللوتس (10:00 صباحاً)**: يتجول بلوم في المدينة، ويستلم رسالة غرامية سرية تحت اسم مستعار، ويزور الكنيسة.
- **6. هاديس (عالم الأموات - 11:00 صباحاً)**: يركب بلوم عربة الجنازة لحضور دفن صديقه دغنام في المقبرة، متأملاً الموت ومسترجعاً وفاة رضيعه رودي في مهده.
- **7. إيولوس (إله الرياح - 12:00 ظهراً)**: في دار جريدة فريمانز، يحاول بلوم نشر إعلان تجاري وسط رياح الخطب الصحفية والسياسية الصاخبة.
- **8. اللستريغونيون (1:00 ظهراً)**: يبحث بلوم عن وجبة غداء، ويشمئز من شراهة الزبائن الحيوانية في المطعم، فيكتفي بساندويتش جبن وكأس نبيذ في حانة دافي بايرنز.
- **9. سيلا وخاريبديس (2:00 ظهراً)**: في المكتبة الوطنية، يلقي ستيفن محاضرته الأدبية الشهيرة مفسراً مسرحية هاملت لشكسبير. يمر بلوم بين الحاضرين كطيف عابر.
- **10. الصخور المتلاطمة (3:00 عصراً)**: 19 مشهداً بانورامياً متزامناً تلتقط نبض شوارع دبلن وشخصياتها المتنوعة.
- **11. السيرينات (4:00 عصراً)**: في فندق أورموند، تتمايل نادلتان على أنغام البيانو بينما يستمع بلوم للموسيقى وهو يعتصر ألماً لعلمه بوصول العشيق لفراش زوجته في هذه اللحظة.
- **12. السيكلوب (5:00 مساءً)**: في الحانة، يهاجم القومي الأيرلندي المتعصب "المواطن" أصول بلوم اليهودية. يدافع بلوم بنبل عن المحبة الإنسانية والعدالة قبل أن يفر من علبة البسكويت التي قذفها المتعصب نحوه.
- **13. ناوسيكا (8:00 مساءً)**: على الشاطئ، يتأمل بلوم الفتاة الشابة جيرتي ماكدويل تحت أضواء الألعاب النارية.
- **14. ثيران الشمس (10:00 مساءً)**: في مستشفى الولادة، تلد السيدة بيورفوي طفلها بعد مخاض عسير لثلاثة أيام. كتب جويس الفصل بـ 32 أسلوباً لغوياً يواكب تطور النثر الإنجليزي من العصور الوسطى حتى العصر الحديث. يلتقي بلوم بستيفن أخيراً ويشربان معاً.
- **15. سيرسي (منتصف الليل)**: في حي البغاء الليلي، مكتوب كمسرحية تعبيرية تكشف كوابيس بلوم وستيفن وهلوساتهما الدفينة. ينقذ بلوم ستيفن من اعتداء جنود إنجليز.

### العودة والنوستوس (الفصول 16–18)
- **16. إيمايوس (1:00 صباحاً)**: يقود بلوم ستيفن المنهك لمقهى سائقي العربات لتناول القهوة وحمايته كأب بديل.
- **17. إيثاكا (2:00 صباحاً)**: حوار علمي صارم على طريقة السؤال والجواب الرياضي الجاف؛ يدخل بلوم ستيفن لمنزله ويشربان الكاكاو في المطبخ ويخرجان للنظر إلى النجوم، ثم يودعه ستيفن في الليل.
- **18. بينيلوبي (مناجاة مولي الخاتمة)**: تستلقي مولي في الفراش، لتطلق أطول مونولوج داخلي غير منقط في تاريخ الأدب؛ يتألف من 8 جمل ضخمة عبر أكثر من 40 صفحة، يتدفق فيها تيار الوعي بكل رغباتها وذكرياتها، وتختمه بإعلانها الأسطوري للحب والحياة: *"ونعم قلت نعم سأوافق نعم"*.
"""
    },

    # 30 Animal Farm
    {
        "id": "30_Animal_Farm",
        "content_en": """# Comprehensive Study Guide: Animal Farm
**Author:** George Orwell  
**Year:** 1945  
**Genre:** Political Satire / Dystopian Fable / Allegory  

---

## 1. Historical Context & Allegorical Key
Written during WWII and published in 1945, Orwell crafted a devastating allegorical fairy story tracking the degeneration of the 1917 Russian Revolution into Stalinist totalitarianism.
- **Mr. Jones**: Czar Nicholas II
- **Old Major**: Karl Marx and Vladimir Lenin
- **Snowball**: Leon Trotsky
- **Napoleon**: Joseph Stalin
- **Squealer**: Soviet state propaganda (Pravda / Molotov)
- **Boxer**: The betrayed working proletariat
- **The Dogs**: The NKVD / Secret Police

---

## 2. In-Depth Chapter Breakdown
- **Chapter 1: Old Major's Dream**: At Manor Farm, the prize boar Old Major gathers the abused animals. He teaches them the revolutionary anthem *"Beasts of England"* and proclaims that all humans are parasites: *"All animals are equal."*
- **Chapter 2: The Rebellion**: Old Major dies. Led by pigs Snowball and Napoleon, the animals drive out the drunken farmer Mr. Jones. They rename the property **Animal Farm** and paint the **Seven Commandments of Animalism** on the barn wall.
- **Chapter 3–4: Early Utopia and the Battle of the Cowshed**: The harvest is a triumph. Snowball organizes literacy classes. Jones returns with armed farmers to retake the farm, but Snowball brilliantly coordinates defense at the **Battle of the Cowshed**, routing the humans.
- **Chapter 5: The Expulsion of Snowball**: Snowball drafts plans to build an electrical windmill to reduce animal labor. Napoleon opposes it. At the final vote, Napoleon unleashes nine ferocious attack dogs he raised in secret, running Snowball off the farm. Napoleon seizes sole dictatorial power, cancelling all debates.
- **Chapter 6–7: Windmill Agony and The Purges**: The windmill collapses in a storm; Napoleon blames "Snowball's sabotage." Rations are slashed. Starving hens protest egg confiscations and are starved into submission. In a horrific public spectacle, animals confess to invented treason and are torn apart by Napoleon's hounds, leaving a pool of blood. *"Beasts of England"* is banned.
- **Chapter 8–9: Boxer's Betrayal**: The commandments are secretly altered at night by Squealer (e.g., *"No animal shall drink alcohol"* becomes *"No animal shall drink alcohol TO EXCESS"*). When the faithful cart-horse Boxer collapses from exhaustion rebuilding the windmill, Napoleon sells him to the horse slaughterer (knacker) to buy whisky, while Squealer lies that Boxer died peacefully in a luxury hospital.
- **Chapter 10: The Ultimate Betrayal**: Years pass. The Seven Commandments are erased and replaced by a single law:  
  **"ALL ANIMALS ARE EQUAL, BUT SOME ANIMALS ARE MORE EQUAL THAN OTHERS."**  
  The pigs walk upright on two legs, wear human clothes, and carry whips. In the final scene, the common animals look through the farmhouse window from pig to man, and from man to pig, and realize it is impossible to tell them apart.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: مزرعة الحيوان (Animal Farm)
**المؤلف:** جورج أورويل (George Orwell)  
**سنة النشر:** 1945  
**التصنيف الأدبي:** هجاء سياسي / رواية رمزية وأسطورة ديستوبية  

---

## 1. السياق التاريخي ومفتاح الرموز
كتب أورويل هذه التحفة في أواخر الحرب العالمية الثانية ليقدم نقداً رمزياً صاعقاً للثورة البلشفية الروسية عام 1917 وانحرافها إلى ديكتاتورية ستالينية باطشة.
- **السيد جونز**: القيصر الروسي نيقولا الثاني
- **الخنزير ميجور العجوز**: كارل ماركس ولينين
- **سنوبول (كرة الثلج)**: ليون تروتسكي (المخطط الثوري المنفي)
- **نابليون**: جوزيف ستالين (الديكتاتور المستبد)
- **سكويلر**: آلة البروباغندا والإعلام السوفيتي (جريدة برافدا)
- **الحصان بوكسر**: الطبقة العاملة المخلصة والمخدوعة
- **الكلاب الشرسة**: الشرطة السرية وأجهزة القمع

---

## 2. التسلسل التفصيلي لفصول الرواية
- **الفصل 1 (حلم الثورة)**: في مزرعة القصر، يجمع الخنزير الحكيم ميجور الحيوانات المقهورة، ويلقي خطبته التاريخية ويعلمهم نشيد الثورة *"وحوش إنجلترا"* مؤكداً أن الإنسان هو الطفيلي الوحيد الذي يسرق عرق الحيوانات: *"جميع الحيوانات متساوية"*.
- **الفصل 2 (اندلاع الثورة)**: يموت ميجور، ويثور الحيوانات ويطردون المزارع السكير جونز. يغيرون اسم المزرعة إلى **مزرعة الحيوان** ويكتبون **الوصايا السبع** على جدار الحظيرة.
- **الفصول 3–4 (معركة زريبة البقر)**: ينجح موسم الحصاد بإخلاص الحيوانات. يقود سنوبول الدفاع العبقري عن المزرعة في **معركة زريبة البقر** ويهزم جونز وأعوانه شر هزيمة.
- **الفصل 5 (طرد سنوبول وانقلاب نابليون)**: يخطط سنوبول لبناء طاحونة هواء لتوفير الكهرباء وتقليل ساعات العمل. يعارضه نابليون، وفي يوم التصويت، يطلق نابليون تسعة كلاب متوحشة ربّاها سراً لتطارد سنوبول وتطرده من المزرعة للأبد، ليعلن نابليون إلغاء الاجتماعات واحتكار السلطة.
- **الفصول 6–7 (حملات التطهير الدموية)**: تنهار الطاحونة بفعل عاصفة، فيدعي نابليون أن سنوبول هو المخرب الخائن. تنخفض الحصص الغذائية، ويجبر الدجاج على التنازل عن البيض. وفي مشهد مروع، يقيم نابليون محاكمة علنية تعترف فيها الحيوانات بجرائم وهمية وتُمزق حناجرها بالكلاب الشرسة. ويُلغى نشيد الثورة.
- **الفصلان 8–9 (خيانة الحصان بوكسر)**: يعدل سكويلر الوصايا ليلاً خلسة (مثلاً: *"لا يقتل حيوان حيواناً آخر... دون سبب"*). وعندما يسقط الحصان الوفي بوكسر مغشياً عليه من فرط العمل، يبيعه نابليون لجزار الخيول ليشتري بثمنه ويسكي للخنازير، بينما يكذب سكويلر مدعياً وفاته في مشفى فاخر!
- **الفصل 10 (التحول التام للخنزير إلى إنسان)**: تُمحى الوصايا السبع بالكامل وتستبدل بقاعدة واحدة مرعبة:  
  **"جميع الحيوانات متساوية، لكن بعض الحيوانات أكثر مساواة من غيرها."**  
  تمشي الخنازير على قائمتين، وترتدي ثياب البشر، وتحمل السياط. وفي المشهد الختامي، تنظر الحيوانات البائسة عبر نافذة القصر من وجه الخنزير إلى وجه الإنسان، ومن الإنسان إلى الخنزير، فيستحيل عليها التمييز بينهما!
"""
    },

    # 31 Pride and Prejudice
    {
        "id": "31_Pride_And_Prejudice",
        "content_en": """# Comprehensive Study Guide: Pride and Prejudice
**Author:** Jane Austen  
**Year:** 1813  
**Genre:** Regency Romance / Comedy of Manners / Social Realism  

---

## 1. Context & Famous Opening
*"It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."*  
Set in Regency England, Austen critiques the economic vulnerability of 19th-century women who could not inherit property due to entailment laws and were forced to secure financial survival through marriage.

---

## 2. In-Depth Chapter Breakdown
- **Arrival of Netherfield**: The wealthy, amiable Charles Bingley leases Netherfield Park, delighting Mrs. Bennet, who has five unmarried daughters (Jane, Elizabeth, Mary, Kitty, Lydia). At the Meryton ball, Bingley falls for gentle Jane, but his arrogant, aristocratic friend Fitzwilliam Darcy refuses to dance with Elizabeth Bennet: *"She is tolerable, but not handsome enough to tempt me."* Elizabeth forms an immediate prejudice against Darcy's pride.
- **Wickham and Collins**: Mr. Collins, a pompous, sycophantic clergyman who will inherit the Bennet estate, arrives proposing to Elizabeth; she flatly rejects him. Meanwhile, charming militia officer George Wickham captivates Elizabeth, lying that Darcy unjustly disinherited him.
- **The Netherfield Separation & Collins's Marriage**: The Bingleys suddenly depart for London, devastating Jane. Collins promptly marries Elizabeth's pragmatic best friend, Charlotte Lucas.
- **The First Proposal at Rosings**: Visiting Charlotte, Elizabeth encounters Darcy visiting his aunt, Lady Catherine de Bourgh. Overwhelmed by passion, Darcy proposes to Elizabeth, but emphasizes how degrading her family connections are to him. Furious, Elizabeth rejects him: *"You could not have made me the offer of your hand in any possible way that would have tempted me to accept it."* She accuses him of destroying Jane's happiness with Bingley and ruining Wickham.
- **Darcy's Expository Letter**: Darcy gives Elizabeth a letter revealing the truth: Wickham was a profligate gambler who attempted to seduce and elope with Darcy's 15-year-old sister Georgiana for her fortune; and Darcy separated Bingley and Jane believing Jane did not truly love him. Elizabeth realizes her terrible blindness and prejudice.
- **Pemberley & The Crisis**: Touring Darcy's majestic estate at Pemberley, Elizabeth is awed by his generosity and hears his housekeeper describe him as the kindest master. Darcy appears, treating Elizabeth and her working-class relatives with utmost respect. The blooming romance is shattered by news that youngest sister Lydia has eloped with Wickham, threatening total family ruin.
- **Redemption and Resolution**: Darcy secretly locates Wickham in London slums, pays off his massive debts, purchases him an army commission, and forces him to marry Lydia, saving the Bennets from social destruction. Bingley returns and proposes to Jane. Darcy proposes again to Elizabeth; this time, humbled of his pride and her prejudice vanished, she accepts with deep joy.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: كبرياء وتحامل (Pride and Prejudice)
**المؤلف:** جين أوستن (Jane Austen)  
**سنة النشر:** 1813  
**التصنيف الأدبي:** الأدب الكلاسيكي الإنجليزي / كوميديا الأخلاق / الرواية الاجتماعية  

---

## 1. السياق والمفتتح الخالد
تبدأ الرواية بإحدى أشهر الجمل الافتتاحية في تاريخ الأدب: *"إنها لحقيقة مسلم بها في كل مكان، أن الرجل الأعزب الذي يملك ثروة طائلة لا بد أن يكون في حاجة إلى زوجة"*. تكشف أوستن ببراعة القيود الاقتصادية الصارمة المفروضة على نساء العصر الجورجي، حيث كان حرمان البنات من وراثة أملاك العائلة يجبرهن على البحث عن الزواج كوسيلة بقاء واستقرار مالي.

---

## 2. التسلسل التفصيلي لمجريات الرواية
- **وصول أصحاب الثروة لنيذرفيلد**: يستأجر الشاب الثري الطيب تشارلز بينغلي قصراً في الحي، مما يسعد السيدة بينيت الساعية لتزويج بناتها الخمس (جين، إليزابيث، ماري، كيتي، ليديا). يقع بينغلي في حب جين، بينما يرفض صديقه الأرستقراطي المتكبر فيتزويليام دارسي الرقص مع إليزابيث قائلاً بازدراء: *"إنها مقبولة، لكنها ليست حسناء بما يكفي لإغرائي"*. تشتعل نيران الكراهية والتحامل في قلب إليزابيث الذكية ضد كبرياء دارسي.
- **القس كولينز والضابط ويكهام**: يتقدم القس السخيف كولينز لخطبة إليزابيث فترفضه بحزم. وفي الوقت نفسه، تلتقي بالضابط الوسيم اللبق جورج ويكهام الذي يروي لها قصة ملفقة تدعي أن دارسي ظلمه وحرمه من ميراث والده، فتزداد كراهيتها لدارسي.
- **رحيل بينغلي وزواج كولينز**: يغادر بينغلي فجأة إلى لندن كاسراً قلب جين. ويسارع القس كولينز للزواج من شارلوت صديقة إليزابيث التي تزوجته طمعاً في الأمان المالي.
- **طلب الزواج الأول في روزينجز**: أثناء زيارة إليزابيث لصديقتها، تلتقي بدارسي. يفاجئها دارسي بطلب يدها، لكنه يركز في عرضه على الفارق الطبقي المخزي لعائلتها! تنفجر إليزابيث غضباً وترفضه قائلة: *"لو كنت آخر رجل في العالم لما وافقت على الزواج منك!"*، متهمة إياه بتدمير سعادة أختها وظلم ويكهام.
- **رسالة دارسي وانكشاف الحقيقة**: يسلمها دارسي رسالة سرية تكشف الحقائق: ويكهام مقامر فاسق حاول خطف شقيقة دارسي الصغيرة ذات الـ 15 عاماً طمعاً في ثروتها، وتدخله بين جين وبينغلي كان لظنه أن جين لا تبادله المشاعر. تدرك إليزابيث عمى بصيرتها وتحاملها المتسرع.
- **قصر بيمبرلي والمأساة**: تزور إليزابيث قصر دارسي العظيم بيمبرلي وتسمع من مدبرة القصر شهادات نبله وكرمه، ويلتقي بها دارسي معاملاً إياها وأقاربها بغاية اللطف والاحترام. وفجأة تقع الكارثة: تهرب أختها المراهقة ليديا مع ويكهام، مما يهدد العائلة بالعار الاجتماعي الأبدي.
- **الخلاص والنهاية السعيدة**: يبحث دارسي عن ويكهام في أحياء لندن سرا، ويسدد كل ديونه ويشتري له رتبة عسكرية ويجبره على الزواج من ليديا لإنقاذ سمعة عائلة إليزابيث. يعود بينغلي ويخطب جين، ويجدد دارسي طلبه للزواج من إليزابيث بعد أن زال كبرياؤه وسقط تحاملها، فتقبل بسعادة غامرة.
"""
    },

    # 32 Wuthering Heights
    {
        "id": "32_Wuthering_Heights",
        "content_en": """# Comprehensive Study Guide: Wuthering Heights
**Author:** Emily Brontë  
**Year:** 1847  
**Genre:** Gothic Romance / Revenge Tragedy / Romanticism  

---

## 1. Context & Savage Nature
Emily Brontë's only novel broke Victorian moral conventions. Set on the wild, desolate Yorkshire moors, the story rejects sanitized polite romance in favor of demonic obsession, generational trauma, and elemental forces.

---

## 2. In-Depth Chapter Breakdown
- **Heathcliff's Arrival**: Mr. Earnshaw brings an orphaned, dark-skinned child from Liverpool to Wuthering Heights, naming him Heathcliff. Catherine Earnshaw forms an intense, primal bond with him, while her brother Hindley brutally abuses and degrades him as a servant after their father dies.
- **The Betrayal**: Catherine is injured and stays at Thrushcross Grange with the refined, civilized Linton family. She falls for the wealthy Edgar Linton. Catherine confesses to the housekeeper Nelly Dean: *"Whatever our souls are made of, his and mine are the same; and Linton's is as different as a moonbeam from lightning, or frost from fire."* But she resolves to marry Edgar because marrying Heathcliff would degrade her. Overhearing only that it would degrade her, Heathcliff vanishes into the stormy night.
- **Heathcliff's Revenge**: Three years later, Heathcliff returns wealthy, refined, and consumed by vengeful hatred. He marries Edgar's naive sister Isabella solely to torture her.
- **Catherine's Death**: Catherine falls mortally ill, torn between Edgar and Heathcliff. Following a savage final embrace with Heathcliff, she dies giving birth to young Cathy. Heathcliff weeps violently, slamming his head against a tree and praying: *"Catherine Earnshaw, may you not rest as long as I am living! You said I killed you—haunt me then!... Be with me always—take any form—drive me mad! only do not leave me in this abyss, where I cannot find you!"*
- **Second Generation & Redemption**: Heathcliff acquires both estates (Wuthering Heights and Thrushcross Grange), enslaving Hindley's son Hareton and forcing young Cathy to marry his dying, sickly son Linton. Yet when Hareton and young Cathy fall in love, Heathcliff loses his appetite for vengeance. Haunted by visions of Catherine's ghost, he starves himself to death. The novel closes with Heathcliff and Catherine buried side by side on the quiet moors.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: مرتفعات وذرنغ (Wuthering Heights)
**المؤلف:** إميلي برونتي (Emily Brontë)  
**سنة النشر:** 1847  
**التصنيف الأدبي:** الرومانسية القوطية / تراجيديا الانتقام والجنون العاطفي  

---

## 1. الطبيعة الوحشية والتمرد الأدبي
كسرت إميلي برونتي بروايتها الوحيدة كل تقاليد الأدب الفيكتوري المهذب؛ حيث تدور الأحداث في مروج يوركشاير العاصفة الموحشة، مجسدة عاطفة بدائية مدمرة تتجاوز حدود العقل والأخلاق وتتحول إلى هوس شيطاني وانتقام أجيال.

---

## 2. المسار الدرامي للعاصفة والأجيال
- **وصول هيثكليف**: يجلب الأب إيرنشو طفلاً غجرياً يتيماً أسمر البشرة من ليفربول إلى مزرعة "مرتفعات وذرنغ" ويسميه هيثكليف. يقع في حبه الطفلة كاثرين إيرنشو بحميمية روحية بدائية، بينما يذيقه شقيقها هندلي ألوان الإهانة والضرب بعد وفاة الأب.
- **الخيانة والرحيل**: تقيم كاثرين في قصر "ثراشكروس غرانج" عند عائلة لينتون الأرستقراطية المتحضرة وتنبهر بأناقة إدغار لينتون. تعترف للمدبرة نيلي دين بمشاعرها قائلة: *"أياً كانت المادة التي صُنعت منها أرواحنا، فإن روحي وروحه واحدة، بينما روح لينتون تختلف عنهما كما يختلف شعاع القمر عن البرق، أو الصقيع عن النار!"*، لكنها تقرر الزواج من إدغار لأن الزواج بهيثكليف سيحط من شأنها. يسمع هيثكليف جملتها الأخيرة فقط، فيهرب في ليلة عاصفة مكسور الفؤاد.
- **عودة المنتقم القاسي**: يعود هيثكليف بعد ثلاث سنوات ثرياً وغامضاً وعازماً على تدمير كل من أهانوه. يتزوج من إيزابيلا شقيقة إدغار نكاية بهما ويعاملها بقسوة بالغة.
- **موت كاثرين واللعنة الأبدية**: تصاب كاثرين بحمى قاتلة ممزقة بين إدغار وهيثكليف. وبعد عناق أخير ملتهب مع هيثكليف، تموت وهي تضع طفلتها كاثي الصغيرة. يضرب هيثكليف رأسه في جذع شجرة باكياً بمرارة: *"كاثرين، لا ترقدي في سلام طالما حييت! طارديني، كوني شبحاً، ادفعيني للجنون، لكن لا تتركيني في هذه الهاوية التي لا أراكِ فيها!"*.
- **انتقام الجيل الثاني والخلاص**: يسيطر هيثكليف على العقارين ويذل هيرتون ابن هندلي، ويجبر كاثي الصغيرة على الزواج من ابنه الضعيف. لكن عندما يرى الحب ينشأ بين كاثي وهيرتون، يفقد رغبته في الانتقام بعد أن أنهكه الشوق لشبح كاثرين. يمتنع عن الطعام حتى يموت، ويُدفن بجوار كاثرين في مروج الريف الهادئة.
"""
    },

    # 33 Jane Eyre
    {
        "id": "33_Jane_Eyre",
        "content_en": """# Comprehensive Study Guide: Jane Eyre
**Author:** Charlotte Brontë  
**Year:** 1847  
**Genre:** Gothic Romance / Bildungsroman / Victorian Feminism  

---

## 1. Context & Groundbreaking Female Agency
Published under the male pseudonym "Currer Bell," Charlotte Brontë revolutionized Victorian fiction by creating an orphan heroine who is plain, poor, and powerless, yet possesses unyielding moral integrity, passion, and fierce independence.

---

## 2. In-Depth Chapter Breakdown
- **Gateshead Hall**: Orphaned Jane Eyre is tormented by her cruel aunt Mrs. Reed and pampered cousin John. Locked in the terrifying "Red-Room" where her uncle died, Jane suffers a nervous breakdown, then bravely denounces Mrs. Reed's cruelty.
- **Lowood School**: Jane is sent to Lowood, an austere charity institution run by the hypocritical, sadistic Mr. Brocklehurst. Jane endures starvation and typhus, sustained by her saintly friend Helen Burns, who dies peacefully in Jane's arms teaching her Christian forgiveness.
- **Thornfield Hall & Mr. Rochester**: Jane becomes governess to Adèle Varens at Thornfield Hall. She meets the brooding, cynical, yet passionate master Edward Rochester. They fall deeply in love, Jane declaring: *"Do you think, because I am poor, obscure, plain, and little, I am soulless and heartless? You think wrong!—I have as much soul as you—and full as much heart!"* Rochester proposes marriage.
- **The Madwoman in the Attic**: At the altar, the wedding is stopped by a lawyer revealing that Rochester is already married. His wife, Bertha Mason, is a violently insane Creole woman kept locked in the attic third-floor tower, guarded by Grace Poole. Rochester begs Jane to live with him abroad as his mistress; Jane refuses to compromise her self-respect and flees into the night penniless.
- **Moor House & St. John Rivers**: Collapsing on the moors, Jane is rescued by the Rivers siblings. St. John Rivers, an austere clergyman, offers Jane marriage on condition that she join him as a missionary in India. Jane refuses loveless spiritual martyrdom. Suddenly, she hears a telepathic voice calling her name: *"Jane! Jane! Jane!"*
- **Reunion at Ferndean**: Jane returns to Thornfield, finding it a blackened ruin. Bertha set the mansion on fire, jumping to her death from the roof; Rochester was blinded and lost a hand rescuing servants. Jane travels to secluded Ferndean and embraces the humbled, blind Rochester: *"Reader, I married him."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: جين إير (Jane Eyre)
**المؤلف:** شارلوت برونتي (Charlotte Brontë)  
**سنة النشر:** 1847  
**التصنيف الأدبي:** الرومانسية القوطية / رواية التكوين والتمكين الأنثوي  

---

## 1. السياق والتمرد النسوي المبكر
نُشرت الرواية تحت اسم مستعار مذكر؛ وأحدثت ثورة في الأدب الفيكتوري بتقديم بطلة يتيمة، فقيرة، عادية الملامح، لكنها تتمتع بكرامة فولاذية، واستقلال روحي، ونزاهة أخلاقية ترفض الخضوع لإملاءات المجتمع الطبقي.

---

## 2. المسار الدرامي لمحطات حياة جين إير
- **قصر غيتسهيد وعذاب الطفولة**: تعيش اليتيمة جين مع خالتها القاسية السيدة ريد وأبنائها المتنمرين. تُحبس في "الغرفة الحمراء" المرعبة التي مات فيها خالها، فتصاب بانهيار عصبي وتواجه خالتها بجرأة تفضح ظلمها.
- **مدرسة لووود الخيرية**: تُرسل لمدرسة خيرية قاسية يديرها القس المتزمت بروكلهيرست. تعاني جين من الجوع والمرض، لكنها تصادق التلميذة التقية هيلين بيرنز التي تموت بين يديها معلمة إياها التسامح والصبر.
- **قصر ثورنفيلد ومستر روتشستر**: تعمل جين معلمة خاصة للطفلة أديل في قصر ثورنفيلد الغامض. تقع في حب سيد القصر إدوارد روتشستر الغامض الجريء. تصارحه بمشاعرها قائلة جملتها الخالدة: *"أتظن أنني لمجرد كوني فقيرة، وبسيطة الملامح، وصغيرة الشأن، أنني بلا قلب ولا روح؟ إنك مخطئ! فروحي تماثل روحك وقلبي يماثل قلبك تماماً!"*. يطلب روتشستر يدها للزواج.
- **المجنونة في العلية**: عند المذبح أثناء مراسم الزواج، يتدخل محامٍ ويفجر المفاجأة: روتشستر متزوج بالفعل من بيرثا ميسون، وهي امرأة مجنونة عنيفة يحبسها في علية القصر تحت حراسة مشددة. يترجاها روتشستر لتعيش معه كعشيقة في باريس، لكن جين ترفض خيانة مبادئها وتهرب ليلاً دون أي مال.
- **ملجأ سينت جون ريفرز**: توشك جين على الموت جوعاً في المروج، فينقدها القس سينت جون ريفرز وأخواته. يطلب القس المتزمت الزواج منها لترافقه في بعثة تبشيرية شاقة في الهند، لكنها ترفض الزواج الخالي من الحب. وفجأة تسمع صوتاً أثيرياً غامضاً يناديها: *"جين! جين! جين!"*.
- **اللقاء الخالد في فيرندين**: تعود جين لقصر ثورنفيلد لتجده ركاماً محترقاً؛ أحرقت الزوجة المجنونة القصر وألقت بنفسها من السطح وماتت، بينما فقد روتشستر بصره وإحدى يديه وهو ينقذ الخدم. تسافر جين لكوخه المنعزل وتحتضن روتشستر الأعمى الكسير وتتزوجه: *"أيها القارئ.. لقد تزوجته"*.
"""
    },

    # 34 Great Expectations
    {
        "id": "34_Great_Expectations",
        "content_en": """# Comprehensive Study Guide: Great Expectations
**Author:** Charles Dickens  
**Year:** 1861  
**Genre:** Victorian Realism / Bildungsroman / Social Satire  

---

## 1. Context & The Illusion of Class
Dickens's late masterpiece is a profound psychological critique of class snobbery, the corrupting influence of unearned wealth, and the true meaning of gentility.

---

## 2. In-Depth Chapter Breakdown
- **The Graveyard Convict**: Young orphan Pip lives on the Kent marshes with his abusive sister and her saintly blacksmith husband, Joe Gargery. In a foggy churchyard, an escaped convict, Abel Magwitch, terrifies Pip into stealing food and a file for him.
- **Satis House & Miss Havisham**: Pip is invited to play at Satis House, the rotting mansion of Miss Havisham—an eccentric recluse who was abandoned at the altar decades earlier, wearing her yellowed bridal dress amidst her rotting wedding cake. Pip falls hopelessly in love with her adopted daughter, the cold, beautiful Estella, who is raised specifically to break men's hearts. Pip begins to feel ashamed of his blacksmith home.
- **The Great Expectations**: A London lawyer, Mr. Jaggers, announces that an anonymous benefactor has bestowed "great expectations" of wealth on Pip to be educated as a gentleman. Assuming Miss Havisham is his sponsor, Pip moves to London, becoming an arrogant snob who neglects Joe Gargery.
- **The Terrible Truth**: On his 23rd birthday, Magwitch suddenly appears in Pip's London chambers. Pip learns with horror that his fortune did not come from aristocratic Miss Havisham, but from the transported criminal Magwitch, who dedicated his grueling labor in Australia to make Pip a gentleman. Pip is initially sickened by Magwitch, but as police close in, Pip recognizes Magwitch's immense paternal love and risks his life trying to smuggle him out of England.
- **Climax and Redemption**: Magwitch is mortally injured during the escape and dies peacefully in prison with Pip by his side. Pip falls ill, and Joe Gargery nurses him back to health and pays his debts without reproach. Humbled, Pip works as a hard-working clerk. In the ruined garden of Satis House, Pip meets a softened, widowed Estella, seeing *"no shadow of another parting from her."*
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: آمال عريضة (Great Expectations)
**المؤلف:** تشارلز ديكنز (Charles Dickens)  
**سنة النشر:** 1861  
**التصنيف الأدبي:** الواقعية الفيكتورية / رواية التكوين / النقد الطبقي والأخلاقي  

---

## 1. السياق ووهم الطبقية الاجتماعية
تعد هذه الرواية قمة نضج تشارلز ديكنز الأدبي؛ حيث يقدم تحليلاً نفسياً عميقاً لوهم الصعود الطبقي، وكيف يفسد المال السهل النفوس، مؤكداً أن النبل الحقيقي ينبع من نقاء القلب لا من الثروة والألقاب.

---

## 2. المسار الدرامي لتحولات "بيب"
- **سجين المقبرة الموحشة**: يعيش اليتيم بيب في مستنقعات كينت مع أخته القاسية وزوجها الحداد الطيب النبيل جو غارجري. في مقبرة ضبابية، يفاجئه سجين هارب مروع مقيد بالسلاسل يدعى آبل ماغويتش ويجبره على سرقة مبرد وطعام له.
- **قصر مس هافيشام وإستيلا**: يُدعى بيب لقصر مس هافيشام، وهي امرأة غريبة الأطوار تركها خطيبها يوم زفافها قبل عقود، فارتدت فستان زفافها الأصفر المهترئ وتركت كعكة العرس تتعفن. يقع بيب في حب ربيبتها الحسناء القاسية إستيلا، التي ربتها مس هافيشام لتكسر قلوب الرجال. يبدأ بيب في الشعور بالخجل من فقر منزله ومهنة الحدادة.
- **الآمال العريضة المجهولة**: يخبره المحامي جاغرز أن متبرعاً مجهولاً وهبه ثروة طائلة ليصبح "جنتلمان" راقياً في لندن. يظن بيب أن مس هافيشام هي المتبرعة، وينتقل للندن ويتحول لشاب متكبر يبدد أمواله ويخجل من زيارة الحداد الوفي جو.
- **الصدمة المدوية**: في عيد ميلاده الثالث والعشرين، يقتحم السجين ماغويتش شقة بيب في لندن، ليكتشف بيب في رعب أن ثروته لم تأتِ من سيدة القصر الأرستقراطية، بل من السجين المحكوم بالأشغال الشاقة الذي أفنى عمره في أستراليا ليجعل من بيب سيداً محترماً!
- **التضحية والتطهر الأخلاقي**: يشمئز بيب في البداية، لكنه يدرك نبل مشاعر السجين وأبوته الصادقة، فيخاطر بحياته لتهريبه عبر النهر من بطش الشرطة. يُصاب ماغويتش ويموت بسلام في السجن ممسكاً بيد بيب. يمرض بيب فيأتي جو غارجري لتمريضه وسداد ديونه برضا تام. يتطهر بيب من غروره ويعمل موظفاً مكافحاً، ويلتقي بإستيلا بعد سنوات في حديقة القصر المهدم ليجدا السكينة معاً.
"""
    },

    # 35 David Copperfield
    {
        "id": "35_David_Copperfield",
        "content_en": """# Comprehensive Study Guide: David Copperfield
**Author:** Charles Dickens  
**Year:** 1850  
**Genre:** Autobiographical Fiction / Victorian Bildungsroman  

---

## 1. Autobiographical Soul
Dickens's most personal work, which he famously declared his *"favorite child."* The novel reflects Dickens's own traumatized childhood working in a blacking factory, his journalistic rise, and his growth as a literary master.

---

## 2. In-Depth Chapter Breakdown
- **Childhood Torment**: David is raised by his sweet mother Clara and faithful servant Peggotty. His life is shattered when Clara marries the cruel, sadistic Edward Murdstone. Murdstone beats David and sends him to Salem House, where brutal headmaster Creakle terrorizes boys.
- **The Blacking Factory & Micawber**: Following his mother's death, David is sent at age ten to work in Murdstone's filthy wine-bottling factory. He lodges with the eccentric, perpetually indebted Mr. Micawber, who cheerfully awaits for *"something to turn up."*
- **Aunt Betsey Trotwood**: Desperate, David walks miles to Dover to seek refuge with his eccentric, fiercely loyal aunt Betsey Trotwood and her simple-minded friend Mr. Dick. She adopts David, drives Murdstone away, and finances his education.
- **Steerforth's Betrayal & Uriah Heep**: David befriends the charming aristocrat James Steerforth, who betrays David's trust by seducing and eloping with little Em'ly, ruining the Peggotty family. Meanwhile, the insidious, scheming clerk Uriah Heep pretends false humility (*"'umble"*) while attempting to ruin David's benefactor Mr. Wickfield. Micawber heroically exposes Heep's fraud.
- **Dora and Agnes**: David marries his "child-wife" Dora Spenlow, but realizes her intellectual vanity. Dora dies young of illness. Over time, David realizes that true, enduring love was always right beside him: Agnes Wickfield, his moral guardian angel and lifelong soulmate.
""",
        "content_ar": """# الدليل الدراسي والتحليلي الشامل: ديفيد كوبرفيلد (David Copperfield)
**المؤلف:** تشارلز ديكنز (Charles Dickens)  
**سنة النشر:** 1850  
**التصنيف الأدبي:** سيرة روائية شبه ذاتية / أدب العصر الفيكتوري  

---

## 1. البعد الذاتي في أدب ديكنز
الرواية الأقرب لقلب تشارلز ديكنز؛ والتي وصفها دوماً بأنها *"طفله المفضل"*. تعكس الرواية طفولة ديكنز المعذبة عندما سُجن والده بسبب الديون واضطر للعمل طفلاً في مصنع تلميع الأحذية، وكفاحه للوصول إلى قمة المجد الأدبي.

---

## 2. المحطات الكبرى في مسيرة ديفيد كوبرفيلد
- **عذاب الطفولة وقسوة ميردستين**: يولد ديفيد يتيماً لأم رقيقة وخادمة وفية تدعى بيغوتي. تتزوج أمه من رجل شرير قاسٍ يدعى ميردستين يضربه ويعذبه، ثم يرسله لمدرسة "سالم هاوس" البائسة حيث يعاقب المدير التلاميذ بوحشية.
- **مصنع القوارير وعائلة ميكاوبر**: بعد وفاة أمه، يرسله زوج أمه في سن العاشرة للعمل الشاق في مصنع قوارير النبيذ القذرة بلندن. يسكن عند عائلة السيد ميكاوبر الغريب الأطوار، الغارق دوماً في الديون والمبتسم أملاً في أن *"يحدث شيء إيجابي قريباً"*.
- **الخلاص عند العمة بيتسي تروتوود**: يهرب ديفيد مشياً على الأقدام إلى دوفر باحثاً عن عمته غريبة الأطوار بيتسي تروتوود، التي تتبناه بحنان وتهزم زوج أمه القاسي وتتكفل بتعليمه ليصبح رجلاً مستقيماً.
- **خيانة ستيرفورث ونفاق أوريا هيب**: يصادق ديفيد الشاب الأرستقراطي الساحر ستيرفورث، الذي يخون ثقته ويغوي إميلي الصغيرة ويدمر عائلة بيغوتي. وفي الوقت نفسه، يظهر الكاتب الخبيث أوريا هيب، الذي يدعي التواضع والمسكنة نفاقاً بينما يبتز مستر ويكفيلد ويسرق أمواله، حتى يفضحه مستر ميكاوبر بشجاعة.
- **دورا وأغنيس**: يتزوج ديفيد من "دورته الطفلة" الحسناء الساذجة دورا، التي تموت مبكراً بالمرض. وفي النهاية، يكتشف ديفيد أن الحب الحقيقي الذي رافقه طوال حياته كان ملاكه الحارس "أغنيس ويكفيلد"، فيتزوجها ويجد السعادة والخلود الأدبي.
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
