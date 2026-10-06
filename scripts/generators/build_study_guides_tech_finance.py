"""
Generates master-level analytical study guides for:
- 01_The_Pragmatic_Programmer
- 02_Programming_Principles_And_Practice_Using_CPP
- 03_Atomic_Habits
- 04_The_Psychology_Of_Money
- 05_How_To_Win_Friends_And_Influence_People
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EN_DIR = r"E:\nokia\summaries\english"
AR_DIR = r"E:\nokia\summaries\arabic"

GUIDES = [
    # 01 The Pragmatic Programmer
    {
        "id": "01_The_Pragmatic_Programmer",
        "content_en": """# Comprehensive Master Guide: The Pragmatic Programmer (20th Anniversary Edition)
**Authors:** David Thomas & Andrew Hunt  
**Edition:** 20th Anniversary Edition (2019/2020)  
**Field:** Software Craftsmanship / Software Engineering Architecture  

---

## 1. Core Philosophy: The Pragmatic Mindset
The Pragmatic Programmer is not bound to a specific language, framework, or corporate methodology. A pragmatic programmer approaches software as a craft requiring continuous discipline, critical thinking, personal responsibility, and adaptability.

### The Foundation Principles:
- **Care About Your Craft (Tip #1)**: Why spend your life developing software unless you care about doing it well?
- **Think! About Your Work (Tip #2)**: Turn off the autopilot. Continuously critique, question, and appraise your technical choices.
- **You Have Agency (Tip #3)**: Take ownership of your career, codebase, and team culture. If your environment is toxic or stagnant, change it or move.
- **Provide Options, Don’t Make Lame Excuses (Tip #4)**: When something fails, do not deliver excuses; deliver solutions, alternatives, and risk mitigation paths.
- **Don’t Live with Broken Windows (Tip #5)**: Software rot (technical debt) spreads exponentially. A single unaddressed bug, messy function, or broken test encourages developers to lower their standards. Fix bad designs immediately.
- **Remember the Big Picture (Tip #7)**: Never get so lost in minutiae that you lose sight of the real business context and system goals.

---

## 2. In-Depth Architectural & Engineering Topics

### Chapter 2: A Pragmatic Approach
- **DRY (Don’t Repeat Yourself - Tip #15)**: Every piece of knowledge within a system must have a single, unambiguous, authoritative representation. DRY applies to architecture, documentation, database schemas, and business logic—not just copying lines of code.
- **Orthogonality (Tip #17)**: Eliminate effects between unrelated components. Design modular systems where changing a database engine, network layer, or UI has zero side-effects on business rules.
- **Reversibility (Tip #18)**: There are no final decisions. Code and architecture must be flexible enough to swap out vendors, databases, or frameworks when conditions change.
- **Tracer Bullets (Tip #20)**: Instead of building layers in isolation, build an end-to-end thin slice from database to UI to verify system architecture in real conditions early.
- **Prototypes to Learn (Tip #21)**: Write throwaway prototypes to explore unknown algorithms or APIs. Never put prototype code into production.

### Chapter 3: The Basic Tools
- **Plain Text as Truth (Tip #25)**: Keep data and configurations in human-readable plain text to ensure durability and prevent proprietary vendor lock-in.
- **Shell Fluency (Tip #26)**: Master command-line shells to automate repetitive workflows.
- **Achieve Editor Fluency (Tip #27)**: Know your editor intimately; minimize friction between thought and code.
- **Always Use Version Control (Tip #28)**: Version control is a project time machine and a foundational collaboration hub.

### Chapter 4: Pragmatic Paranoia
- **Design by Contract (DbC - Tip #37)**: Define preconditions, postconditions, and class invariants. If a caller violates a precondition, fail fast.
- **Dead Programs Tell No Lies (Tip #38)**: Crash early when an impossible error occurs. Do not allow a corrupted system to continue executing.
- **Assertive Programming (Tip #39)**: Use assertions to guard against the impossible. If it can't happen, use an assertion to ensure it doesn't.
- **Finish What You Start (Tip #41)**: Allocate and deallocate resources (memory, file handles, sockets, database transactions) in the same scope or balanced abstraction.

### Chapter 5: Bend or Break (Decoupling)
- **Decoupled Code (Tip #44)**: Don't chain method calls (`person.getDepartment().getManager().getAddress()`). Obey the Law of Demeter.
- **Transforming Programming (Tip #49)**: View programs as pipelines that transform input data streams into output data streams, rather than state machines manipulating hidden internal state.
- **Event-Driven Architectures**: Decouple components in time and space using publishers/subscribers and event queues.

### Chapter 6: Concurrency & Real World
- **Break Shared State**: Shared mutable state is the root of all concurrency bugs (race conditions, deadlocks). Use actors, channels, or immutability.
- **Blackboard Systems**: Use shared message boards to allow independent autonomous agents to collaborate asynchronously.

### Chapter 7: While You Are Coding
- **Programming by Coincidence (Tip #58)**: Don't code by superstition. Know exactly why your code works and why it fails.
- **Algorithm Speed (Big-O)**: Estimate computational complexity before writing critical routines.
- **Refactoring (Tip #61)**: Refactor early, refactor often. Refactoring is continuous maintenance, not an isolated project phase.
- **Test-Driven Thinking**: Tests are not just quality assurance; they are the primary clients of your APIs that drive clean design.

---

## 3. The Official Author Takeaways
1. Invest regularly in your knowledge portfolio (learn at least one new language every year).
2. Code that is easy to change is good code (ETC: Easy To Change).
3. Software craftsmanship is an active, daily ethical commitment to excellence.
""",
        "content_ar": """# الدليل الدراسي والهندسي الشامل: المبرمج البراغماتي (طبعة الذكرى العشرين)
**المؤلفون:** ديفيد توماس وأندرو هانت  
**الطبعة:** طبعة الذكرى العشرين (20th Anniversary Edition - 2019/2020)  
**المجال:** هندسة البرمجيات الاحترافية / البراغماتية البرمجية  

---

## 1. الفلسفة الجوهرية: العقلية البراغماتية
المبرمج البراغماتي لا يتقيد بلغة برمجة واحدة أو إطار عمل محدد أو مدرسة إدارية جامدة. البرمجة في نظره حرفة سامية تتطلب انضباطاً ذاتياً، وتفكيراً نقدياً، ومسؤولية كاملة عن جودة المنتج، وقدرة مستمرة على التكيف مع الواقع العملي.

### المبادئ التأسيسية:
- **اهتم بحرفتك (النصيحة #1)**: ما الفائدة من قضاء حياتك في كتابة البرمجيات إن لم تكن مهتماً بصناعتها على أكمل وجه؟
- **فكر في عملك! (النصيحة #2)**: أوقف وضع الطيار الآلي. قيّم قراراتك البرمجية والمعمارية باستمرار وبنظرة نقدية.
- **أنت صاحب القرار (النصيحة #3)**: حياتك المهنية وبيئة عملك بيدك؛ إذا كانت بيئة العمل متخلفة أو سامة، اعمل على تغييرها أو غادرها.
- **قدّم حلولاً وبدائل، لا أعذاراً واهية (النصيحة #4)**: عند وقوع مشكلة، لا تأتِ للمدير أو العميل بالأعذار؛ بل وضّح المخاطر واطرح الخيارات العملية الممكنة.
- **لا تتعايش مع النوافذ المكسورة (النصيحة #5)**: عطب البرمجيات (الدين التقني) يبدأ بثغرة واحدة مهملة أو تصميم سيئ أو كود فوضوي يُترك دون إصلاح. النوافذ المكسورة تشجع على مزيد من الإهمال؛ أصلح المشاكل فور اكتشافها.
- **تذكر الصورة الكلية (النصيحة #7)**: لا تغرق في تفاصيل الكود لدرجة تنسى فيها الهدف التجاري والواقعي للمنظومة.

---

## 2. المحاور المعمارية والتقنية الكبرى

### الفصل الثاني: المنهجية البراغماتية
- **مبدأ عدم التكرار DRY (Don't Repeat Yourself)**: كل معلومة أو منطق عمل في النظام يجب أن يكون له تمثيل واحد وحيد وقاطع. التكرار ليس مجرد نسخ أسطر الكود، بل تكرار التوثيق وهيكلية قواعد البيانات والمنطق التجاري.
- **التعامدية (Orthogonality)**: صمم مكوناتك بحيث تكون مستقلة تماماً ومغلقة على وظيفتها؛ تغيير قاعدة البيانات أو واجهة المستخدم يجب ألا يترك أي أثر جانبي على قواعد العمل الأساسية.
- **القابلية للتراجع (Reversibility)**: لا يوجد قرار تقني أبدي. ابنِ كودك بحيث يسهل استبدال قواعد البيانات والمكتبات الخارجية عندما تتغير الظروف.
- **الرصاصات المضيئة (Tracer Bullets)**: بدلاً من بناء الطبقات بمعزل عن بعضها، ابنِ مساراً كاملاً رفيعاً يربط واجهة المستخدم بقاعدة البيانات مبكراً للتأكد من سلامة المعمارية عملياً.
- **النماذج الأولية الاستكشافية (Prototypes)**: ابنِ نماذج سريعة لتعلم وفهم التقنيات المجهولة، ثم تخلص منها ولا تضعها في بيئة الإنتاج.

### الفصل الثالث: الأدوات الأساسية
- **النص المجرد (Plain Text)**: احفظ البيانات والإعدادات في نصوص مجردة، فهي لا تصدأ ولا تصبح ملغاة وتضمن استقلالية البيانات.
- **إتقان الطرفية (Shell)**: تعلم سطر الأوامر وأتمتة المهام اليومية المتكررة.
- **إتقان المحرر (Editor Fluency)**: اعرف محرر الأكواد الخاص بك كظهر يدك لتكتب أفكارك البرمجية دون احتكاك ذهني.
- **أنظمة التحكم بالإصدار (Git)**: إدارة الإصدارات هي آلة زمنية لمشروعك ومركز للتعاون الآمن.

### الفصل الرابع: الحذر البراغماتي (Pragmatic Paranoia)
- **التصميم بالتعاقد (Design by Contract)**: حدد شروط المدخلات والمخرجات لكل دالة. إذا خالف المستدعي الشروط، أوقف التنفيذ فوراً.
- **البرامج الميتة لا تكذب (Crash Early)**: عندما يقع خطأ مستحيل الحدوث، دع البرنامج ينهار فوراً بدلاً من الاستمرار في تشغيل نظام فاسد البيانات.
- **البرمجة التوكيدية (Assertions)**: استخدم التوكيدات للتأكد من استحالة حدوث السيناريوهات الكارثية.
- **أنهِ ما بدأت (Resource Management)**: كل مورد تحجزه (ملف، ذاكرة، اتصال شبكي) يجب تحريره في نفس النطاق المنطقي.

### الفصل الخامس: المرونة وفك الارتباط
- **فك الارتباط وقانون ديميتر**: لا تستدعِ سلاسل طويلة من الكائنات المتداخلة، بل اجعل كل كائن يتعامل فقط مع جيرانه المباشرين.
- **البرمجة التحويلية (Pipelines)**: تعامل مع البرنامج كمسار أنابيب يحول تدفقات البيانات من حالة إلى أخرى، بدلاً من كتل معقدة تعدل حالات داخلية مخفية.

### الفصل السادس والسابع: التزامن وجودة الكود
- **كسر الحالة المشتركة (Shared State)**: المتغيرات المشتركة القابلة للتعديل هي أم المشاكل في التزامن. استخدم مبدأ عدم القابلية للتغيير أو تمرير الرسائل.
- **تجنب البرمجة بالصدفة**: اعرف تماماً لماذا يعمل كودك ولماذا يفشل، ولا تبرمج بناءً على تخمينات عشوائية.
- **إعادة الهيكلة المستمرة (Refactoring)**: إعادة التصميم وتحسين الكود ليست مرحلة معزولة، بل نشاط يومي ملازم للكتابة.

---

## 3. الدروس البراغماتية الخالدة
1. استثمر في محفظتك المعرفية يومياً (تعلم لغة برمجة جديدة كل عام).
2. الكود الجيد هو الكود السهل التغيير (ETC: Easy To Change).
3. الجودة والاحتراف التزام أخلاقي يومي يبدأ من أصغر سطر كود.
"""
    },

    # 02 Programming Principles And Practice Using CPP
    {
        "id": "02_Programming_Principles_And_Practice_Using_CPP",
        "content_en": """# Comprehensive Master Guide: Programming: Principles and Practice Using C++ (3rd Edition, 2024)
**Author:** Bjarne Stroustrup (Creator of C++)  
**Edition:** 3rd Edition (May 2024 - C++20 / C++23)  
**Field:** Computer Science Fundamentals / Systems Programming / C++ Engineering  

---

## 1. Stroustrup's Pedagogical Vision
*Programming: Principles and Practice Using C++* is Bjarne Stroustrup’s definitive foundational textbook. It does not treat programming merely as language syntax, but as the art of expressing ideas precisely in code. The 3rd Edition (2024) completely modernizes the material for **C++20 and C++23**, introducing:
- **C++20 Modules**: Replacing legacy `#include` headers with scalable module imports.
- **Concepts**: Formal compile-time constraints on template arguments, providing human-readable error messages.
- **Ranges**: Composable pipelines of algorithms and views (`ranges::filter`, `ranges::transform`).
- **`std::format` & `std::print`**: Type-safe, high-performance formatted output replacing clunky `iostreams` and unsafe `printf`.

---

## 2. Structural Breakdown & Core Engineering Concepts

### Part I: The Basics
- **Computation, Expressions & Statements**: Developing algorithmic thinking, flow control, functions, and loop invariants.
- **Errors, Exceptions & Debugging**: Stroustrup teaches defensive programming from day one. Run-time errors, range checking, contract checks, and structured exception handling (`try-catch`).
- **Writing a Real Program (The Calculator)**: Designing a recursive-descent parser and lexical scanner from scratch to demonstrate grammar parsing, tokenization, and symbol tables.

### Part II: Input & Output and Modularity
- **Modern I/O**: Type-safe formatting with `std::print` and `std::format`, robust file stream handling, and string views.
- **C++20 Modules**: Structuring large codebases into compiled binary interfaces, eliminating header guard macros, macro leakage, and quadratic compilation times.

### Part III: Data Structures and Memory Management (The Core of Systems Programming)
- **Vector and Free Store (Heap Memory)**: Building `std::vector` from raw pointers to explain how computers manage physical memory.
- **RAII (Resource Acquisition Is Initialization)**: The golden rule of C++. Every resource (memory, files, sockets, mutexes) is tied to the lifetime of an object. Constructors acquire; destructors automatically release.
- **The Rule of 0, 3, and 5**: Copy constructors, copy assignment, move constructors, move assignment, and destructors. Move semantics eliminate costly deep copies when transferring ownership.
- **Arrays, Pointers, and References**: Understanding direct hardware addresses, pointer arithmetic, memory layouts, and avoiding dangling references.

### Part IV: Abstraction, OOP & Generic Programming
- **Class Design & Invariants**: Designing classes that maintain valid internal states at all times. If an invariant cannot be established, throw in the constructor.
- **Object-Oriented Programming**: Virtual functions, polymorphism, abstract interfaces, runtime dispatch, and inheritance hierarchies.
- **Generic Programming with Templates & Concepts**: Writing flexible, zero-overhead algorithms. Using C++20 Concepts (`template<std::integral T>`) to constrain types and verify preconditions at compile-time.
- **Standard Template Library (STL)**: Containers (`vector`, `map`, `unordered_set`), iterators, and modern Ranges algorithms.

---

## 3. Stroustrup's Core Principles & Maxims
1. **Direct Representation of Ideas**: Express concepts directly in code (e.g., use a `Matrix` class or a `Date` type, not raw integers and arrays).
2. **Zero-Overhead Principle**: What you don't use, you don't pay for. What you do use, you couldn't hand-code any better.
3. **Type Safety & Resource Safety**: Make code type-safe and resource-safe by construction through RAII, smart pointers (`std::unique_ptr`, `std::shared_ptr`), and modern containers. Never manage raw memory manually in business logic.
""",
        "content_ar": """# الدليل الدراسي والهندسي الشامل: البرمجة: المبادئ والممارسة بلغة ++C (الطبعة الثالثة 2024)
**المؤلف:** بيارن ستروستروب (Bjarne Stroustrup - مبتكر لغة ++C)  
**الطبعة:** الطبعة الثالثة (مايو 2024 - متوافقة تماماً مع معايير C++20 و C++23)  
**المجال:** أسس علوم الحاسوب / برمجة الأنظمة وهندسة البرمجيات  

---

## 1. الرؤية التعليمية لبيارن ستروستروب
يعد هذا الكتاب المرجع التأسيسي الأضخم لبيارن ستروستروب لتعليم البرمجة الحقيقية. لا يتعامل الكتاب مع البرمجة كحفظ لقواعد لغة معينة، بل كفن التعبير الدقيق والفعال عن الأفكار الحسابية. وقد خضعت الطبعة الثالثة (2024) لعملية تحديث جذرية لتعتمد على أحدث معايير **C++20 و C++23**، وأبرزها:
- **الموديولات (C++20 Modules)**: استبدال ملفات الترويسات القديمة (`#include`) بموديولات مجمعة تحمي الكود من تداخل الماكرو وتسرع عملية البناء.
- **المفاهيم والقيود (Concepts)**: فرض قيود شكلية على القوالب في وقت الترجمة للحصول على رسائل خطأ بشرية واضحة بدلاً من صفحات الأخطاء المشفرة.
- **المجالات والخطوط الأنبوبية (Ranges)**: صياغة الخوارزميات كسلاسل ترشيح وتحويل مركبة وأنيقة.
- **الطباعة الحديثة (`std::print` و `std::format`)**: إخراج نصوص منسقة آمنة الأنواع وفائقة السرعة.

---

## 2. المحاور الهندسية والبرمجية الكبرى

### الجزء الأول: التأسيس البرمجي
- **العمليات الحسابية والعبارات**: بناء التفكير الخوارزمي، والتحكم في التدفق، وتصميم الدوال وحلقات التكرار الآمنة.
- **الأخطاء والاستثناءات**: يرسخ ستروستروب البرمجة الدفاعية ومعالجة أخطاء وقت التشغيل وفحص الحدود عبر الاستثناءات المهيكلة (`try-catch`).
- **بناء برنامج حقيقي (الآلة الحاسبة)**: بناء محلل نحوي ومصنف رموز من الصفر، لتعليم الطلاب كيفية تحليل القواعد اللغوية وجداول الرموز.

### الجزء الثاني: النمطية والمدخلات/المخرجات
- **المدخلات والمخرجات الحديثة**: التعامل الآمن مع الملفات والسلاسل النصية وتدفقات البيانات.
- **معمارية الموديولات**: تقسيم الأنظمة البرمجية الضخمة إلى واجهات ثنائية نقية وفعالة.

### الجزء الثالث: هياكل البيانات وإدارة الذاكرة (جوهر برمجة الأنظمة)
- **المصفوفات الديناميكية وذاكرة الكومة (Heap)**: إعادة بناء حاوية `std::vector` خطوة بخطوة لفهم كيفية تعامل العتاد مع الذاكرة الفيزيائية.
- **مبدأ RAII (حيازة الموارد تعني التهيئة)**: المبدأ الذهبي في ++C؛ كل مورد (ذاكرة، ملف، مقبس شبكي، قفل تزامن) ترتبط حياته بكائن. الباني يحجز المورد، والهادم يحرره تلقائياً فور خروجه من النطاق.
- **قواعد الإدارة (Rule of 0, 3, 5)**: بواني النسخ والنقل والتدمير، وميكانيكا النقل (Move Semantics) التي تمنع عمليات النسخ البطيئة عند نقل ملكية البيانات.
- **المؤشرات والمراجع**: التعامل مع العناوين الفيزيائية، وتجنب المؤشرات التائهة (Dangling Pointers) وتسريب الذاكرة.

### الجزء الرابع: التجريد والبرمجة الكائنية والعمومية
- **تصميم الأصناف والثوابت الهيكلية (Invariants)**: بناء أصناف تضمن سلامة حالتها الداخلية طوال الوقت؛ وإذا تعذر تحقيق الحالة السليمة، يرمي الباني استثناءً فوراً.
- **البرمجة الكائنية (OOP)**: الدوال الافتراضية، وتعدد الأشكال (Polymorphism)، والواجهات المجردة، والوراثة المنضبطة.
- **البرمجة العمومية بالقوالب والمفاهيم**: كتابة خوارزميات عامة بدون تكلفة تشغيلية (Zero-Overhead)، وضبطها عبر Concepts للتأكد من ملاءمة الأنواع في وقت الترجمة.
- **مكتبة القوالب القياسية (STL)**: الحاويات، والمكررات (Iterators)، وخوارزميات المعالجة الحديثة.

---

## 3. مبادئ ستروستروب الهندسية الراسخة
1. **التمثيل المباشر للأفكار**: عبّر عن المفاهيم مباشرة في الكود (استخدم صنف `Date` أو `Matrix` بدلاً من مصفوفات بدائية وأرقام مجهولة).
2. **مبدأ التكلفة الصفرية (Zero-Overhead Principle)**: ما لا تستخدمه لا تدفع ثمنه؛ وما تستخدمه لا يمكنك كتابته يدوياً بكفاءة أعلى.
3. **أمان الأنواع وسلامة الموارد**: اجعل كودك آمناً بطبيعته عبر المؤشرات الذكية (`std::unique_ptr`) وحاويات الـ STL، ولا تُدر الذاكرة الخام يدوياً في منطق الأعمال أبداً.
"""
    },

    # 03 Atomic Habits
    {
        "id": "03_Atomic_Habits",
        "content_en": """# Comprehensive Master Guide: Atomic Habits
**Author:** James Clear  
**Year:** 2018  
**Field:** Behavioral Psychology / Habit Formation / Personal Mastery  

---

## 1. The Core Philosophy: The Power of 1% Compounding
Changes that seem small and unimportant at first will compound into remarkable results if you are willing to stick with them for years. 
- **The Aggregation of Marginal Gains**: If you get 1% better each day for one year, you’ll end up **37 times better** by the time you’re done ($1.01^{365} \\approx 37.78$). Conversely, if you get 1% worse each day, you decline nearly to zero ($0.99^{365} \\approx 0.03$).
- **Forget About Goals, Focus on Systems**: Goals are about the results you want to achieve. Systems are about the processes that lead to those results. You do not rise to the level of your goals; you fall to the level of your systems.
- **The Plateau of Latent Potential**: Habits often appear to make no difference until you cross a critical threshold. Complaints about lack of success despite hard work are like complaining that an ice cube won't melt when heated from 25 to 31 degrees; the transformation occurs at 32 degrees.

---

## 2. Identity-Based Habits: The Three Layers of Behavior Change
Behavior change exists on three concentric levels:
1. **Outcomes**: What you get (losing 10 kg, publishing a book).
2. **Processes**: What you do (implementing a workout routine, writing daily).
3. **Identity**: What you believe (your worldview, your self-image).
- Most people focus on *outcome-based habits*. Lasting change must be *identity-based habits*. 
- The ultimate goal is not to read a book; it is to **become a reader**. The goal is not to run a marathon; it is to **become a runner**.
- Every action you take is a vote for the type of person you wish to become.

---

## 3. The Habit Loop and the Four Laws of Behavior Change

Every habit is governed by a 4-step neurological feedback loop: **Cue $\\rightarrow$ Craving $\\rightarrow$ Response $\\rightarrow$ Reward**.

| Phase | How to Create a Good Habit | How to Break a Bad Habit (Inversion) |
| :--- | :--- | :--- |
| **1. Cue** | **Make it Obvious** | **Make it Invisible** |
| **2. Craving** | **Make it Attractive** | **Make it Unattractive** |
| **3. Response** | **Make it Easy** | **Make it Difficult** |
| **4. Reward** | **Make it Satisfying** | **Make it Unsatisfying** |

### The 1st Law: Make It Obvious (The Cue)
- **Habit Scorecard**: List your daily habits and rate them (+, -, =) to build awareness.
- **Implementation Intentions**: Specify exact trigger and location: *"I will [BEHAVIOR] at [TIME] in [LOCATION]."*
- **Habit Stacking**: Pair a new habit with a current habit: *"After [CURRENT HABIT], I will [NEW HABIT]."*
- **Environment Design**: Visual cues trigger habits. Place healthy food on the counter, put your guitar in the center of the living room, remove junk food from view.

### The 2nd Law: Make It Attractive (The Craving)
- **Temptation Bundling**: Pair an action you *want* to do with an action you *need* to do.
- **Social Norms**: Join a culture where your desired behavior is the normal behavior.
- **Reframing Mindset**: Shift from *"I have to"* to *"I get to"*.

### The 3rd Law: Make It Easy (The Response)
- **Law of Least Effort**: Reduce the friction associated with good habits; increase friction for bad habits.
- **The 2-Minute Rule**: When you start a new habit, it should take less than two minutes to do (*"Read one page"*, *"Tie my running shoes"*). Standardize before you optimize.
- **Prime the Environment**: Prepare your workspace the night before so starting takes zero effort.

### The 4th Law: Make It Satisfying (The Reward)
- **The Cardinal Rule of Behavior Change**: What is immediately rewarded is repeated. What is immediately punished is avoided.
- **Habit Trackers & The "Don't Break the Chain" Rule**: Visual measurement of progress provides immediate satisfaction.
- **The Rule of Never Missing Twice**: If you miss one day due to circumstances, get back on track immediately the next day. Missing once is an accident; missing twice is the start of a new bad habit.

---

## 4. Advanced Tactics: From Good to Truly Great
- **The Goldilocks Rule**: Humans experience peak motivation when working on tasks that are right on the edge of their current abilities (not too hard, not too easy).
- **The Downside of Habits**: Habits create automaticity, which can lead to complacency. **Habits + Deliberate Practice = Mastery**.
""",
        "content_ar": """# الدليل الدراسي والتطبيقي الشامل: العادات الذرية (Atomic Habits)
**المؤلف:** جيمس كلير (James Clear)  
**سنة النشر:** 2018  
**المجال:** علم النفس السلوكي / بناء العادات / هندسة الإنتاجية والنمو الشخصي  

---

## 1. الفلسفة الجوهرية: قوة التراكم بنسبة 1%
التغييرات الصغيرة التي تبدو غير ملحوظة في البداية تتراكم لتحدث نتائج هائلة ومدهشة بمرور السنوات:
- **تراكم المكاسب الهامشية**: إذا تحسنت بنسبة 1% يومياً لمدة عام كامل، فستكون في نهاية العام أفضل بـ **37 ضعفاً** ($1.01^{365} \\approx 37.78$). بينما إذا تراجعت بنسبة 1% يومياً، فستنحدر نحو الصفر تقريباً.
- **انسَ الأهداف وركّز على الأنظمة**: الأهداف تتعلق بالنتائج التي تريد تحقيقها، بينما الأنظمة تتعلق بالعمليات اليومية التي تقود لتلك النتائج. أنت لا ترتقي إلى مستوى أهدافك، بل تسقط إلى مستوى أنظمتك.
- **هضبة الإمكانات الكامنة (The Plateau of Latent Potential)**: العادات لا تظهر نتائجها فوراً بل تمر بفترة تبدو فيها بلا أثر؛ مثل تسخين مكعب الثلج من درجة 25 إلى 31 دون أن يذوب، حتى إذا وصل إلى 32 درجة ذاب فجأة. النجاح انفجار تراكمي لا يحدث بين ليلة وضحاها.

---

## 2. العادات المبنية على الهوية (Identity-Based Habits)
يحدث التغيير السلوكي على ثلاث طبقات متحدة المركز:
1. **النتائج**: ما تحصل عليه (خسارة 10 كجم، تأليف كتاب).
2. **العمليات**: ما تفعله يومياً (نظام التمرين، الكتابة لساعة يومياً).
3. **الهوية**: ما تؤمن به عن نفسك ومعتقداتك الذاتية.
- معظم الناس يركزون على تغيير النتائج ويفشلون. التغيير الدائم يبدأ من **الهوية**.
- الهدف ليس قراءة كتاب، بل أن **تصبح قارئاً**. الهدف ليس الجري في سباق، بل أن **تصبح رياضياً**.
- كل عمل تقوم به هو بمثابة "صوت انتخابي" تدلي به لصالح الشخصية التي تريد أن تصبحها.

---

## 3. حلقة العادة والقوانين الأربعة للتغيير السلوكي

تخضع كل عادة لحلقة عصبية من 4 خطوات: **الإشارة $\\rightarrow$ الرغبة $\\rightarrow$ الاستجابة $\\rightarrow$ المكافأة**.

| المرحلة | كيف تبني عادة إيجابية | كيف تتخلص من عادة سلبية (المعكوس) |
| :--- | :--- | :--- |
| **1. الإشارة (Cue)** | **اجعلها واضحة (Make it Obvious)** | **اجعلها خفية (Make it Invisible)** |
| **2. الرغبة (Craving)** | **اجعلها جذابة (Make it Attractive)** | **اجعلها غير جذابة (Make it Unattractive)** |
| **3. الاستجابة (Response)** | **اجعلها سهلة (Make it Easy)** | **اجعلها صعبة وشاقة (Make it Difficult)** |
| **4. المكافأة (Reward)** | **اجعلها مشبعة (Make it Satisfying)** | **اجعلها غير مشبعة (Make it Unsatisfying)** |

### القانون الأول: اجعلها واضحة (الإشارة)
- **بطاقة تقييم العادات**: اكتب عاداتك اليومية وصنفها (+، -، =) لزيادة الوعي السلوكي.
- **نية التنفيذ**: حدد الوقت والمكان بدقة: *"سأقوم بـ [السلوك] في [الوقت] في [المكان]"*.
- **تراكم العادات (Habit Stacking)**: اربط العادة الجديدة بعادة قديمة راسخة: *"بعد [العادة الحالية]، سأقوم بـ [العادة الجديدة]"*.
- **تصميم البيئة**: صمم بيئتك بحيث تكون الإشارات الإيجابية ظاهرة أمامك، وأخفِ مشتتاتك (ضع الكتب والفاكهة أمام عينيك، وأخفِ الهاتف أو ألعاب الفيديو).

### القانون الثاني: اجعلها جذابة (الرغبة)
- **حزم المغريات (Temptation Bundling)**: اربط عملاً *تحتاج* للقيام به بعمل *ترغب* في القيام به.
- **الانتماء للبيئة الاجتماعية**: انضم إلى مجتمع وسياق يكون فيه السلوك المرغوب هو السلوك الطبيعي المعتاد.
- **إعادة التأطير الذهني**: حوّل التفكير من *"يجب عليّ فعل ذلك"* إلى *"تتاح لي فرصة فعل ذلك"*.

### القانون الثالث: اجعلها سهلة (الاستجابة)
- **قانون الجهد الأقل**: قلل الاحتكاك والعوائق أمام العادات الجيدة، وزد العوائق أمام العادات السيئة.
- **قاعدة الدقيقتين**: عندما تبدأ عادة جديدة، اجعلها تستغرق أقل من دقيقتين (*"اقرأ صفحة واحدة"*, *"البس حذاء الركض"*). اجعل العادة قياسية وسهلة التكرار قبل أن تبحث عن تحسينها.
- **تهيئة البيئة مسبقاً**: جهز مكتبك أو ملابسك الرياضية في الليلة السابقة لتنطلق دون تردد.

### القانون الرابع: اجعلها مشبعة (المكافأة)
- **القاعدة الذهبية لتغيير السلوك**: ما يُكافأ عليه فوراً يتكرر، وما يُعاقب عليه فوراً يُتجنب.
- **مُتتبّع العادات (Habit Tracker)**: علامة الإنجاز في التقويم اليومي تمنح الدماغ دفعة فورية من الرضا.
- **قاعدة عدم الانقطاع مرتين**: إذا اضطرتك الظروف لتفويت يوم، عد فوراً في اليوم التالي. التفويت لمرة واحدة حادث عارض؛ التفويت لمرتين هو بداية عادة سيئة جديدة.

---

## 4. استراتيجيات متقدمة
- **قاعدة جولديلوكس (Goldilocks Rule)**: يصل الإنسان لأعلى درجات الشغف والتركيز عندما يعمل على مهام تقع بالضبط على حافة قدراته الحالية (ليست شديدة السهولة فيمل، ولا شديدة الصعوبة فيحبط).
- **العادات + الممارسة المركزة = الإتقان**: العادات تمنحك الأوتوماتيكية، ولكن المراجعة والنقد المستمر هما اللذان يقودانك إلى الاحتراف والتميز.
"""
    },

    # 04 The Psychology of Money
    {
        "id": "04_The_Psychology_Of_Money",
        "content_en": """# Comprehensive Master Guide: The Psychology of Money
**Author:** Morgan Housel  
**Year:** 2020  
**Field:** Behavioral Finance / Personal Economics / Wealth Psychology  

---

## 1. Core Thesis: Financial Success is Soft Skill, Not Hard Science
Doing well with money has a little to do with how smart you are and a lot to do with how you behave. Genius without behavioral discipline is a financial disaster, while ordinary people with disciplined emotional control can accumulate staggering wealth.

---

## 2. The 20 Pivotal Lessons & Chapters

1. **No One’s Crazy**: Everyone’s financial decisions are shaped by the specific economic era they grew up in (e.g., growing up during hyperinflation vs. a 30-year bull market). Nobody makes decisions solely based on spreadsheets; they make them based on personal lived experience.
2. **Luck & Risk**: Luck and risk are siblings. Every outcome in life and business is guided by forces outside individual effort. Be careful when judging your own success or others' failures; neither is as good or as bad as it looks.
3. **Never Enough**: The hardest financial skill is getting the goalpost to stop moving. Comparing yourself to richer peers is a game you cannot win. Knowing what is "enough" prevents catastrophic gambles.
4. **Confounding Compounding**: More than 99% of Warren Buffett's wealth was accumulated after his 50th birthday. His secret is not astonishing returns, but **time**. Compounding rewards patience over brilliant stock picking.
5. **Getting Wealthy vs. Staying Wealthy**: Getting wealthy requires taking risks, optimism, and putting yourself out there. Staying wealthy requires the opposite: humility, paranoia, frugality, and the acceptance that at least some of what you made was due to luck.
6. **Tails, You Win**: A small number of extreme events (tail events) account for the majority of outcomes. In venture capital, index funds, or art collecting, you can be wrong half the time and still make an immense fortune because the top 1% carries the entire portfolio.
7. **Freedom**: The highest dividend money pays is the ability to control your time. Having the autonomy to wake up every morning and say, *"I can do whatever I want today,"* is the ultimate lifestyle luxury.
8. **Man in the Car Paradox**: When you see someone driving a Ferrari, you don't think, *"The driver is cool."* You think, *"If I had that car, people would think I am cool."* Humility gains you more true respect than flashy possessions.
9. **Wealth is What You Don’t See**: Wealth is the cars not purchased, the diamonds not bought, the first-class tickets declined. Wealth is financial options not yet spent. Spending money to show people how much money you have is the fastest way to have less money.
10. **Save Money**: You don't need a specific reason to save. Saving is simply the gap between your ego and your income. Cash in the bank gives you options, resilience, and flexibility during crises.
11. **Reasonable > Rational**: Aiming to be strictly rational on paper often fails because humans have emotions. Strive to be *reasonable* and comfortable enough with your strategy that you can sleep soundly at night.
12. **Surprise!**: History is the study of change, ironically used as a map of the future. The most important economic events are always unprecedented outliers that nobody predicted.
13. **Room for Error**: The most critical part of every financial plan is planning on your plan not going according to plan. A margin of safety ensures you survive market downturns without being forced to sell at the bottom.
14. **You’ll Change**: Long-term financial planning is hard because human desires, values, and goals change drastically over decades (the "End of History" illusion).
15. **Nothing’s Free**: Successful investing demands an admission price. That price is not paid in dollars, but in volatility, fear, doubt, and regret. Treat volatility as an admission fee, not a fine.
16. **You & Me**: Beware taking financial cues from people playing a different game than you (e.g., day traders vs. 30-year index fund holders).
17. **The Seduction of Pessimism**: Pessimism sounds smarter, more urgent, and more intellectual than optimism. Yet historically, human progress and economic compounding reward patient optimism.
18. **When You’ll Believe Anything**: In times of desperation or greed, people believe comforting fictions. The more you want something to be true, the more likely you are to believe a story that overestimates the odds of it being true.
19. **All Together Now**: The summary checklist: live below your means, prioritize independence, respect the role of luck, embrace room for error.
20. **Confessions**: Morgan Housel's personal philosophy: high savings rate, paid-off mortgage, index funds, maximizing peace of mind over raw financial yield.
""",
        "content_ar": """# الدليل الدراسي والمالي الشامل: سيكولوجية المال (The Psychology of Money)
**المؤلف:** مورغان هاوسل (Morgan Housel)  
**سنة النشر:** 2020  
**المجال:** السلوك المالي / الاقتصاد النفسي / فلسفة الثروة والادخار  

---

## 1. الفكرة الجوهرية: النجاح المالي مهارة سلوكية وليس معادلة رياضية
تحقيق النجاح المالي لا يرتبط بمدى ذكائك أو تفوقك في الرياضيات بقدر ما يرتبط بـ **سلوكك النفسي والعاطفي**. العبقري الذي يفقد السيطرة على مشاعره يواجه كارثة مالية محققة، بينما يستطيع الإنسان البسيط المنضبط عاطفياً أن يبني ثروة طائلة مستدامة.

---

## 2. الدروس والقوانين العشرون الكبرى

1. **لا يوجد إنسان مجنون**: كل قرار مالي يتخذه شخص يبدو منطقياً في ضوء التجربة الحياتية والظروف الاقتصادية التي نشأ فيها. من عاش أزمة التضخم يختلف جذرياً عمن نشأ في عصر ازدهار الأسهم.
2. **الحظ والمخاطرة**: الحظ والمخاطرة توأمان ملتصقان. كل نتيجة في الأعمال والاستثمار تحكمها عوامل خارج نطاق الجهد الفردي؛ لذا لا تغتر بنجاحك ولا تفرط في لوم نفسك عند التعثر.
3. **لا تكفي أبداً (Never Enough)**: أصعب مهارة مالية هي إيقاف تحريك خط النهاية. مقارنة نفسك بالأثرياء لعبة خاسرة دوماً؛ ومعرفة متى يكون لديك "ما يكفي" تحميك من مغامرات كارثية قد تطيح بكل ما تملك.
4. **سحر التراكم (Compounding)**: أكثر من 99% من ثروة وارن بافيت تحققت بعد عيد ميلاده الخمسين. سره ليس ضربات الحظ الاستثنائية، بل **الاستمرار لعقود طويلة**. التراكم يكافئ الصبر الزمني قبل أي شيء.
5. **صناعة الثروة مقابل الحفاظ عليها**: صناعة الثروة تتطلب الجرأة والمخاطرة والتفاؤل. أما الحفاظ عليها فيتطلب نقيض ذلك تماماً: التواضع، والحذر، والتقشف، والاعتراف بأن جزءاً من المكسب كان بفضل الحظ.
6. **الأحداث النادرة هي الفائزة (Tails, You Win)**: قلة ضئيلة من القرارات أو الأحداث النادرة تصنع الأغلبية الساحقة من العوائد. في صناديق الاستثمار والشركات الناشئة، يمكنك أن تخطئ في نصف قراراتك وتظل ثرياً لأن أفضل 1% يعوض كل شيء.
7. **الحرية هي الجائزة الكبرى**: أعظم عائد يمكن أن يشتريه المال هو **السيطرة على وقتك**. الاستيقاظ كل صباح والقدرة على قول: *"أستطيع أن أفعل ما أريد اليوم"* هو المعنى الحقيقي والنهائي للثراء.
8. **مفارقة الرجل داخل السيارة الفارهة**: حين ترى شخصاً يقود سيارة فيراري، نادراً ما تفكر في شخص السائق؛ بل تفكر: *"لو كنت أملك هذه السيارة لظن الناس أنني رائع"*. التواضع يمنحك احتراماً حقيقياً لا تشتريه المظاهر.
9. **الثروة هي ما لا تراه**: الثروة الحقيقية هي السيارات التي لم تُشترَ، والمجوهرات التي لم تُقتنَ، والخيارات المالية التي لم تُنفق. إنفاق المال لإظهار ثرائك هو أسرع طريق لخسارة المال.
10. **ادخر دون سبب محدد**: لا تحتاج لهدف محدد لتدخر؛ الادخار هو ببساطة الفارق بين غرورك ودخلك. السيولة في البنك تمنحك مرونة وخيارات نجاة في الأزمات.
11. **كن عقلانياً بشكل مريح (Reasonable > Rational)**: السعي وراء المنطق الرياضي الصارم يفشل لأننا بشر لدينا مشاعر. اختر استراتيجية مالية مريحة نفسياً تتيح لك النوم بهدوء ليلاً.
12. **المفاجأة**: التاريخ هو دراسة للتغيرات غير المتوقعة، والخطأ يكمن في استخدامه كخريطة للمستقبل؛ أعظم الأحداث الاقتصادية لم يتوقعها أحد قط.
13. **هامش الأمان (Room for Error)**: أهم جزء في أي خطة مالية هو التخطيط لاحتمال فشل الخطة! هامش الأمان يحميك من البيع في قاع الأزمات.
14. **أنت تتغير باستمرار**: التخطيط المالي لعقود طويلة صعب لأن رغبات الإنسان وأولوياته وقيمه تتغير جذرياً عبر مراحل العمر.
15. **لا شيء مجاني**: الاستثمار الناجح يتطلب ثمناً؛ وثمنه ليس بالدولار بل بالقلق والتقلبات والشك والندم. اعتبر تقلب الأسواق تذكرة دخول للعبة وليست غرامة مفروضة عليك.
16. **أنا وأنت نلعب ألعاباً مختلفة**: احذر من تقليد قرارات مستثمرين يلعبون لعبة زمنية تختلف عن لعبتك (كالمضاربين اليوميين مقابل المستثمر طويل الأجل).
17. **جاذبية التشاؤم**: التشاؤم يبدو دائماً أذكى وأكثر جاذبية وإلحاحاً من التفاؤل؛ لكن التاريخ يثبت أن التراكم والتطور يكافئان التفاؤل الهادئ.
18. **تصديق الأوهام في الأزمات**: كلما اشتدت حاجتك لأمر ما، زادت قابليتك لتصديق قصص خيالية تعدك بتحقيقه دون جهد.
19. **الخلاصة العملية**: عش بأقل من دخلك، أعطِ الأولوية للاستقلال المالي والتحكم بالوقت، وقدّر دور الحظ، وامنح نفسك هامشاً للأمان.
20. **اعترافات الكاتب**: الفلسفة الشخصية لمورغان هاوسل: نسبة ادخار مرتفعة، سداد الرهن العقاري، وصناديق المؤشرات منخفضة التكلفة، لراحة البال التامة.
"""
    },

    # 05 How To Win Friends And Influence People
    {
        "id": "05_How_To_Win_Friends_And_Influence_People",
        "content_en": """# Comprehensive Master Guide: How to Win Friends and Influence People
**Author:** Dale Carnegie  
**Year:** 1936  
**Field:** Interpersonal Communication / Social Psychology / Leadership  

---

## 1. Context and Foundational Philosophy
Published during the Great Depression in 1936, Dale Carnegie’s masterpiece remains the bedrock text of interpersonal communication and professional leadership. Carnegie understood that human beings are not primarily creatures of logic, but creatures of emotion, bristling with prejudices and motivated by pride and vanity. Dealing with people successfully requires empathy, genuine interest, and the restraint to elevate others rather than criticize them.

---

## 2. The Four Pillars and Complete Principles

### Part One: Fundamental Techniques in Handling People
1. **Don't criticize, condemn, or complain**: Criticism puts a person on the defensive and usually makes them strive to justify themselves. It wounds their precious pride and arouses resentment. As Carnegie noted, even Al Capone saw himself as a public benefactor who was misunderstood.
2. **Give honest and sincere appreciation**: The deepest urge in human nature is the *"desire to be important"* (John Dewey) and the *"craving to be appreciated"* (William James). Sincere praise nourishes the soul; flattery is shallow and manipulative.
3. **Arouse in the other person an eager want**: The only way on earth to influence other people is to talk about what *they* want and show them how to get it. When you go fishing, you don't bait the hook with strawberries; you bait it with worms.

### Part Two: Six Ways to Make People Like You
1. **Become genuinely interested in other people**: You can make more friends in two months by becoming interested in other people than you can in two years by trying to get other people interested in you.
2. **Smile**: An action speaks louder than words, and a smile says: *"I like you. You make me happy. I am glad to see you."*
3. **Remember that a person's name is to that person the sweetest and most important sound in any language**: Remembering and using a person's name pays a subtle and very effective compliment.
4. **Be a good listener; encourage others to talk about themselves**: Many people fail to make a favorable impression simply because they don't listen attentively.
5. **Talk in terms of the other person's interests**: Speak on subjects that matter to the listener to establish an instant rapport.
6. **Make the other person feel important—and do it sincerely**: Always follow the Golden Rule: treat others as you would have them treat you.

### Part Three: How to Win People to Your Way of Thinking
1. **The only way to get the best of an argument is to avoid it**: Nine times out of ten, an argument ends with each contestant more firmly convinced than ever that he is absolutely right. You can't win an argument: if you lose it, you lose it; and if you win it, you make the other person feel inferior and resentful.
2. **Show respect for the other person's opinions; never say, "You're wrong"**: Saying someone is wrong directly strikes at their intelligence, judgment, and self-respect.
3. **If you are wrong, admit it quickly and emphatically**: Admitting fault disarms opponents and invites forgiveness.
4. **Begin in a friendly way**: A drop of honey catches more flies than a gallon of gall.
5. **Get the other person saying "yes, yes" immediately**: Start on points of agreement using the Socratic method to prevent psychological walls from rising.
6. **Let the other person do a great deal of the talking**: Let people express their problems and pride fully before presenting your perspective.
7. **Let the other person feel that the idea is theirs**: People have far more faith in ideas that they discover themselves than in ideas handed to them on a platter.
8. **Try honestly to see things from the other person's point of view**: Ask yourself: *"Why would he want to do this?"*
9. **Be sympathetic with the other person's ideas and desires**: The magic phrase that stops arguments: *"I don't blame you one bit for feeling as you do. If I were you, I would undoubtedly feel just the same."*
10. **Appeal to the nobler motives**: Assume people are honest and upright; they will often rise to the high standard you hold them to.
11. **Dramatize your ideas**: Make your ideas vivid, visual, and compelling.
12. **Throw down a challenge**: When all else fails, stimulate friendly competition and the desire to excel.

### Part Four: Be a Leader—How to Change People Without Giving Offense
1. Begin with praise and honest appreciation.
2. Call attention to people's mistakes indirectly.
3. Talk about your own mistakes before criticizing the other person.
4. Ask questions instead of giving direct orders.
5. Let the other person save face.
6. Praise the slightest improvement and praise every improvement.
7. Give the other person a fine reputation to live up to.
8. Use encouragement; make the fault seem easy to correct.
9. Make the other person happy about doing the thing you suggest.
""",
        "content_ar": """# الدليل الدراسي والتواصلي الشامل: كيف تكسب الأصدقاء وتؤثر في الناس
**المؤلف:** ديل كارنيجي (Dale Carnegie)  
**سنة النشر:** 1936  
**المجال:** علم التواصل الإنساني / الذكاء الاجتماعي / القيادة والتأثير  

---

## 1. السياق والفلسفة التأسيسية
صدر كتاب ديل كارنيجي خلال فترة الكساد الكبير عام 1936، وظل حتى اليوم المرجع الأول في فن التعامل الإنساني وبناء العلاقات الإيجابية. أدرك كارنيجي بعمق أن البشر ليسوا كائنات منطقية بحتة، بل كائنات عاطفية تحركها المشاعر، والكبرياء، والاعتزاز بالذات. النجاح في قيادة الناس وكسب ثقتهم لا يتحقق بالجدال ولا بالتسلط، بل بالتعاطف الصادق وتقدير مشاعرهم ورفع مكانتهم.

---

## 2. المحاور والمبادئ الكبرى (الأبواب الأربعة)

### الباب الأول: القواعد الأساسية في معاملة الناس
1. **لا تنتقد، ولا تدن، ولا تشتكِ**: النقد يضع الشخص في موقف دفاعي ويجعله يبحث عن تبرير موقفه، ويجرح كبرياءه ويثير حقده الدفين. حتى عتاة المجرمين كـ "آل كابوني" كانوا يرون أنفسهم فاعلي خير أساء المجتمع فهمهم!
2. **قدّم التقدير الصادق والمخلص**: أعمق دافع في الطبيعة البشرية هو "الرغبة في الشعور بالأهمية" و"التعطش للتقدير". التقدير الصادق غذاء الروح، بينما النفاق رخيص ومكشوف.
3. **أيقظ في الشخص الآخر رغبة عارمة في التعاون**: الطريقة الوحيدة للتأثير في الآخرين هي التحدث عما *يريدونه هم* وإرشادهم لكيفية تحقيقه. عندما تذهب لصيد السمك، لا تضع في الصنارة فراولة لأنك تحبها، بل ضع دودة لأن السمك يشتهيها!

### الباب الثاني: ست طرق لجعل الناس يحبونك
1. **اهتم بالآخرين اهتماماً صادقاً**: يمكنك كسب أصدقاء في شهرين عبر الاهتمام بالآخرين أكثر مما تكسبه في عامين بمحاولة جعل الناس يهتمون بك.
2. **ابتسم**: الأفعال أبلغ من الكلمات، والابتسامة تقول للطرف الآخر: *"أنا معجب بك، ورؤيتك تسعدني"*.
3. **تذكر أن اسم الشخص هو أحلى وأهم صوت يسمعه في أي لغة**: تذكر الأسماء ومناداتها احترام راقٍ للشخصية.
4. **كن مستمعاً جيداً، وشجع الآخرين على الحديث عن أنفسهم**: كثير من الناس يفشلون في كسب القلوب لأنهم يستعجلون الحديث ولا يستمعون باهتمام.
5. **تحدث بما يتفق مع اهتمامات الشخص الآخر**: ادخل لعالمه من الباب الذي يحبه هو.
6. **اجعل الشخص الآخر يشعر بأهميته بصدق وإخلاص**: طبق القاعدة الذهبية: عامل الناس بما تحب أن يعاملوك به.

### الباب الثالث: كيف تكسب الناس إلى طريقة تفكيرك
1. **الطريقة الوحيدة لكسب الجدال هي تجنبه**: تسع مرات من أصل عشر، ينتهي الجدال بتمسك كل طرف برأيه أكثر من ذي قبل. إذا خسرت الجدال خسرت، وإذا كسبته أهنت كبرياء خصمك وخسرت وده.
2. **احترم آراء الآخرين ولا تقل لأحد قط: "أنت مخطئ"**: مصارحة شخص بخطئه تهين ذكاءه وكرامته.
3. **إذا كنت مخطئاً، فاعترف بخطئك سريعاً وبصراحة**: الاعتراف بالخطأ يجرد الخصم من أسلحته ويستجلب المسامحة.
4. **ابدأ دائماً بطريقة ودية**: قطرة عسل تصيد ذباباً أكثر من برميل علقم.
5. **اجعل الطرف الآخر يجيب بـ "نعم" فوراً**: استخدم أسلوب سقراط بالتركيز على نقاط الاتفاق أولاً لمنع بناء جدران نفسية رافضة.
6. **اترك للشخص الآخر فرصة الحديث بحرية**: دعه يفرغ مشاعره وأفكاره حتى يهدأ.
7. **اجعل الطرف الآخر يشعر أن الفكرة فكرته هو**: يثق الناس بأفكارهم التي اكتشفوها بأنفسهم أكثر من أفكار تُملى عليهم.
8. **حاول مخلصاً أن ترى الأمور من وجهة نظر الطرف الآخر**: اسأل نفسك دوماً: *"لماذا يتصرف بهذه الطريقة؟"*.
9. **أظهر التعاطف التام مع أفكار ورغبات الآخرين**: العبارة السحرية لتهدئة أي غضب: *"لا ألومك مطلقاً على شعورك هذا، فلو كنت في مكانك لشعرت بالشيء نفسه تماماً"*.
10. **خاطب الدوافع النبيلة في النفوس**: افترض في الناس النبل والصدق، وسيسعون لإثبات حسن ظنك بهم.
11. **اعرض أفكارك بطريقة درامية ومشوقة**: اجعل أفكارك حية وجذابة بالصور والقصص.
12. **اطرح تحدياً**: التنافس الشريف والرغبة في التفوق يحفزان الهمم العالية.

### الباب الرابع: كيف تكون قائداً وتغير الناس دون إثارة غضبهم
1. ابدأ بالثناء والتقدير الصادق قبل أي توجيه.
2. لفت الأنظار إلى الأخطاء بطريقة غير مباشرة وذكية.
3. تحدث عن أخطائك الشخصية أولاً قبل نقد الآخرين.
4. اطرح أسئلة واقتراحات بدلاً من إصدار أوامر مباشرة جافة.
5. احفظ للطرف الآخر ماء وجهه.
6. امتدح أقل بادرة تحسن، وامتدح كل تقدم.
7. امنح الشخص سمعة طيبة ومكانة يسعى جاهداً للمحافظة عليها.
8. شجع الآخرين واجعل إصلاح الخطأ يبدو سهلاً وممكناً.
9. اجعل الشخص سعيداً ومتحمساً لتنفيذ ما تقترحه عليه.
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
