# Examiners' Report Insights (OCR H446)

## What this is — and why it's worth your time

After every exam series, OCR publishes an **examiners' report** for each paper. Senior examiners describe — across thousands of scripts — *exactly* where candidates lost marks, which misconceptions kept recurring, and what a full-mark answer looked like. The same warnings come back **year after year**, because students keep making the same mistakes.

This makes the reports some of the highest-value revision material there is: they are, in effect, a list of the marks you can win simply by *not* repeating last year's cohort's errors. Most of these are **technique and precision** errors, not gaps in knowledge — which makes them the cheapest marks to recover.

This page distils the recurring themes by spec area. **You should still read the real reports** (free on the OCR website under "Computer Science H446 → Assessment → Examiner reports"). Read the report for a paper *after* you've attempted that past paper — it tells you not just the right answer but *why* most people got it wrong.

> The reports won't quote you exact grade boundaries or statistics here on purpose — those change every year. Treat the advice below as durable patterns, then confirm against the live reports.

---

## How to read a real examiners' report (5 minutes)

1. Do the past paper **first**, under timed conditions.
2. Mark it with the mark scheme.
3. Open the examiners' report and read **only the questions you dropped marks on**.
4. For each, note the *category* of mistake (e.g. "described instead of compared") — categories repeat across topics.
5. Add the misconception to your own error log so you pre-empt it next time.

---

## Component 01 — Computer Systems

### 1.1 Characteristics of contemporary processors, input, output and storage devices

| Common error / what examiners say | What to do instead |
|---|---|
| **Confusing MAR and MDR.** The single most common 1.1 slip: candidates swap their roles. | MAR holds the **address** of the location to access; MDR holds the **data/instruction** being transferred. Say it as "MAR = where, MDR = what". |
| Describing the **fetch–decode–execute cycle** vaguely ("it fetches and runs instructions"). | Name the **register transfers** at each step (PC → MAR, memory → MDR → CIR, PC incremented, decode in CU, execute in ALU). |
| Claiming **"more cores = always faster"** with no caveat. | State that the gain depends on whether the **task can be parallelised** and the **software supports** multiple cores; some tasks are inherently sequential. |
| Treating **clock speed, cache and cores** as interchangeable performance boosters. | Explain the distinct mechanism for each: clock = cycles/sec; cache = fewer slow main-memory accesses (note L1 fastest/smallest); cores = genuine parallel execution. |
| Mixing up **Von Neumann vs Harvard** architectures. | Von Neumann = shared memory/bus for data and instructions; Harvard = separate. Link Harvard to embedded/DSP use. |
| **RISC vs CISC**: listing features without consequences. | Connect features to effects (RISC: simpler instructions → easier pipelining → lower power, good for mobile). |
| Confusing the three **addressing modes** or just naming them. | Distinguish immediate (operand *is* the value), direct (operand is the address), indirect (operand points to the address), indexed (base + index register). |
| Storage answers that ignore the **scenario's needs**. | Match medium to requirement: portability, capacity, speed, durability, cost — and *justify* against the named use case. |

### 1.2 Software and software development

| Common error / what examiners say | What to do instead |
|---|---|
| **Compiler vs interpreter** muddled. | Compiler translates the **whole** program once into object/executable code (errors reported at the end); interpreter translates and executes **line by line** (stops at first error). Mention an assembler for assembly code. |
| Reciting the **stages of compilation** in the wrong order or omitting one. | Order: **lexical analysis → syntax analysis → code generation → optimisation**. Know what each does (e.g. lexical removes whitespace/comments and builds tokens + symbol table). |
| Describing a **development methodology generically** instead of justifying it for the scenario. | Tie the choice to the context: Agile/iterative for **changing/unclear requirements**; Waterfall for **fixed, well-understood** requirements; Extreme Programming for high-quality, fast-changing code. |
| Confusing **procedure vs function**. | A **function returns a value**; a procedure performs an action and need not. |
| Vague on **types of programming** (procedural, OOP, declarative, assembly). | Give a defining characteristic and a use case for each. |
| Mixing up **utility software and applications**, or OS roles. | OS manages hardware/resources (memory management, scheduling, interrupts); utilities maintain the system (defrag, backup, compression). |

### 1.3 Exchanging data

| Common error / what examiners say | What to do instead |
|---|---|
| **Lossy vs lossless** confused. | Lossy **permanently discards** data to shrink size (irreversible); lossless preserves all data and is exactly reversible (e.g. RLE, dictionary coding). |
| **Symmetric vs asymmetric** encryption swapped. | Symmetric = **one shared key** (fast, key-distribution problem); asymmetric = **public/private key pair** (encrypt with public, decrypt with private; underpins digital signatures). |
| **Normalisation**: not knowing the rule for each form, or stopping early. | 1NF: atomic values, no repeating groups. 2NF: 1NF + no **partial** dependencies. 3NF: 2NF + no **transitive** dependencies. Quote the rule, then apply it to the given table. |
| **SQL**: forgetting the **WHERE** clause on UPDATE/DELETE (would change every row), or wrong JOIN logic. | Always check whether the query needs a WHERE. State the JOIN condition explicitly (`ON a.id = b.id`). |
| **Database concepts** mixed (primary/foreign key, referential integrity, indexing). | Primary key = unique identifier; foreign key = primary key of another table used to link; referential integrity stops orphaned foreign keys. |
| **TCP/IP layers** listed without function. | Application, Transport, Network/Internet, Link — give one job each (e.g. Transport splits into packets/handles ports). |
| Confusing **circuit vs packet switching**, or LAN vs WAN. | Packet switching: data split into packets routed independently and reassembled; no dedicated path. |
| **ACID** transactions vaguely defined. | Atomicity, Consistency, Isolation, Durability — define each in one phrase. |

### 1.4 Data types, data structures and Boolean algebra

| Common error / what examiners say | What to do instead |
|---|---|
| **Floating point**: not **normalising** the result, or sign-handling errors with two's complement mantissas. | Normalise so the mantissa starts `0.1…` (positive) or `1.0…` (negative). Show the exponent adjustment. Practise both directions: normalise *and* denormalise. |
| **Two's complement** subtraction/overflow mistakes. | Subtract by adding the two's complement; check for overflow (carry into vs out of the sign bit). |
| Confusing **binary, hex and BCD** conversions. | Group binary in 4s for hex; remember BCD encodes each decimal digit separately (used where exact decimal matters, e.g. displays). |
| **Data structures**: describing a stack/queue/list but not the **operations or use case**. | Give the behaviour (LIFO/FIFO), the core operations (push/pop, enqueue/dequeue, with overflow/underflow checks), and a realistic use (call stack, print queue). |
| **Graphs vs trees** confused; missing traversal detail. | A tree is a connected acyclic graph with a root. Know pre/in/post-order and breadth/depth-first, and what each produces. |
| **Boolean algebra**: not simplifying fully, or misapplying De Morgan's. | Quote the law you're using (De Morgan's, distribution, absorption). Simplify step by step; don't jump. |
| Drawing **logic gates / Karnaugh maps** carelessly. | Label inputs/outputs; group K-map cells in powers of two, largest groups first, wrapping allowed. |

### 1.5 Legal, moral, ethical and cultural issues

| Common error / what examiners say | What to do instead |
|---|---|
| **One-sided ethics essays** — arguing only the harms (or only the benefits). | Give a **balanced** argument: stakeholders on **both sides**, then a justified conclusion. Examiners reward a reasoned judgement, not a rant. |
| Naming a law incorrectly or describing the **wrong** Act. | Know the headline Acts: Data Protection / GDPR, Computer Misuse Act, Copyright Designs and Patents Act, Regulation of Investigatory Powers Act. Match the Act to the scenario. |
| Confusing **legal vs moral vs ethical vs cultural** dimensions (the question asks for a specific one). | Legal = what the law says; moral/ethical = right vs wrong; cultural = effect on groups/society. Answer the dimension asked. |
| Generic answers that **ignore the named scenario**. | Anchor every point in the context (who is affected here, and how). Use the stakeholders the question gives you. |
| Vague impacts ("it's bad for society"). | Be specific: privacy, employment, digital divide, environmental cost, automated decision-making — and explain the mechanism. |

---

## Component 02 — Algorithms and Programming

### 2.1 Elements of computational thinking

| Common error / what examiners say | What to do instead |
|---|---|
| **Defining** the computational-thinking terms instead of **applying** them to the scenario. | Don't write "abstraction means removing detail." *Show* it: state which details you'd remove **from this problem** and why. The same goes for decomposition, pattern recognition, caching, concurrency. |
| Treating **abstraction and decomposition** as the same thing. | Decomposition = breaking a problem into smaller sub-problems; abstraction = removing/hiding unnecessary detail. Use both correctly in context. |
| Vague on **thinking ahead / caching / preconditions**. | Identify the inputs/outputs and reusable results in *this* problem; explain what caching saves *here*. |
| Ignoring **concurrency trade-offs**. | Note benefits (throughput) and costs (synchronisation, race conditions, not all tasks parallelise). |

### 2.2 Problem solving and programming

| Common error / what examiners say | What to do instead |
|---|---|
| **Recursion with no (or wrong) base case** — code that never terminates. | Always state the **base case** (stopping condition) *and* the recursive case that moves toward it. In a trace, show the stack building and unwinding. |
| **Pseudocode that won't run** — undeclared variables, off-by-one loops, no return. | Follow OCR's reference language conventions; declare/initialise variables; check loop bounds; return where required. Re-read your own code as if executing it. |
| **Trace tables** filled in carelessly (skipping iterations, wrong column updates). | One **row per change**; update every affected column each pass; track the loop counter and condition explicitly. |
| Confusing **parameters/arguments, by value vs by reference**, or **local vs global scope**. | Be precise: passing by reference lets the subroutine change the caller's variable; local variables exist only inside their subroutine. |
| **IDE / debugging** answers that just list features. | Link the feature to the task (breakpoints to inspect state, stepping to find the failing line, watch to track a variable). |
| Mixing up **procedure vs function** again (carries over from 1.2). | Function returns a value; procedure performs an action. |

### 2.3 Algorithms

| Common error / what examiners say | What to do instead |
|---|---|
| **Quoting Big O without justification** — stating "it's O(n log n)" with no reasoning. | Explain *why*: relate the complexity to the number of operations as input grows (e.g. each merge level is O(n), there are log n levels). State **best/average/worst** where they differ. |
| **Describing instead of comparing** when asked to compare two algorithms. | Use comparative language ("X is faster than Y *because*…"), pick comparison axes (time complexity, space, stability, suitability for sorted/unsorted data), and reach a judgement. |
| Confusing **searching algorithms** — using binary search on **unsorted** data. | Binary search requires the data to be **sorted**; linear search does not. State the precondition. |
| Muddling the **sorts** (bubble, insertion, merge, quick) — their mechanism and complexity. | Know each one's method and complexity: bubble/insertion O(n²) (insertion good on nearly-sorted), merge O(n log n) stable but needs extra space, quick O(n log n) average / O(n²) worst. |
| **Dijkstra / graph traversals**: not showing working, or wrong queue/visited handling. | Show the table of distances/visited nodes step by step; explain the priority choice each step. State what BFS vs DFS is used for. |
| Stating an algorithm is "more efficient" with no metric. | Specify the metric — time **or** space — and the input size regime; the answer can differ for small vs large *n*. |

---

## The Top 10 marks students throw away

1. **Answering the wrong command word** — *describing* when the question says *evaluate*, *justify* or *compare*. Match your answer to the verb.
2. **Describing instead of comparing.** "Compare" needs comparative language and a judgement, not two separate descriptions.
3. **Quoting Big O / "more efficient" with no justification.** Always say *why*, and give best/worst case where they differ.
4. **One-sided ethics essays.** Argue both sides, then conclude. No conclusion = lost marks on every "discuss/evaluate" question.
5. **Defining computational-thinking terms instead of applying them** to the actual scenario.
6. **Recursion with no base case** (or pseudocode that wouldn't run).
7. **Not normalising floating-point results** — and two's complement sign slips.
8. **Forgetting WHERE on SQL UPDATE/DELETE**, and wrong JOIN logic.
9. **Swapping MAR/MDR, lossy/lossless, symmetric/asymmetric** — the classic confusable pairs. Drill them.
10. **Ignoring the scenario.** If the question names a context, name it back and anchor every point to it — generic answers cap your marks.

> Print the Top 10, and tick off in each mock that you avoided all of them. These are pure technique marks — they cost nothing to win back.
