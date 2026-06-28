# Top Exam Mistakes (and How to Avoid Them)

These are the recurring, grade-costing errors across H446. Most are *technique*, not knowledge — which means they're the **cheapest marks to win back**. Read this the week of each exam.

---

## Universal (both papers)

| Mistake | Fix |
|---------|-----|
| Answering the wrong **command word** (describing when asked to evaluate). | Circle the command word first; match your answer to it. |
| Ignoring the **scenario** on AO2 questions. | If the question names a context, *name it back* in your answer. |
| **One-word answers** to "explain/describe". | Add the "because…/which means…". One developed point per mark. |
| **No working** shown on calculations/traces. | Always show method — method marks survive a wrong final answer. |
| **Repeating one idea** in different words. | Examiners count *distinct* points; make each one new. |
| **Over-writing low-tariff questions**, then running out of time. | ~1 minute per mark; move on and return. |
| Vague terminology ("it's faster/better"). | Be precise: *why* — cache hit, fewer cycles, lower complexity, etc. |
| Listing pros/cons but **no conclusion** on "evaluate/justify". | Always end with a judgement: "Overall, X because…". |

---

## Component 01 — content-specific traps

### 1.1 Processors
- Confusing **MAR/MDR** roles (MAR holds the *address*, MDR holds the *data/instruction*).
- Saying "more cores = always faster" — note **not all tasks parallelise**; software must support it.
- Forgetting **cache** in performance answers, or mixing up cache *level* (L1 fastest/smallest).
- Vague FDE answers — name the **register transfers** at each step.

### 1.2 Software
- Mixing up **compiler vs interpreter** (compiler translates *all at once* producing an executable; interpreter translates+runs *line by line*).
- Confusing the **stages of compilation** order (lexical → syntax → code generation → optimisation).
- Describing a methodology generically instead of **justifying it for the scenario** (e.g. Agile for changing requirements).
- Confusing **procedure vs function** (a function returns a value).

### 1.3 Exchanging data
- Muddling **lossy vs lossless** (lossy *permanently discards* data).
- **Symmetric vs asymmetric** encryption mixed up — asymmetric uses a *public/private key pair*.
- Normalisation: not knowing the **rule for each normal form**; forgetting to remove **partial/transitive dependencies**.
- SQL: forgetting the **WHERE** clause on UPDATE/DELETE, or wrong **JOIN** logic.
- TCP/IP: confusing the **four layers** and which protocol sits where.

### 1.4 Data / Boolean
- **Two's complement**: forgetting the leftmost bit is *negative*; sign errors on subtraction.
- **Floating point**: not normalising correctly; confusing mantissa vs exponent; wrong handling of negatives.
- **Binary shifts**: forgetting a left shift can **overflow**; mixing up logical vs arithmetic shift.
- **Boolean**: misapplying **De Morgan's** (the bar breaks *and the operator flips*); sloppy truth tables.
- Confusing **stack (LIFO)** vs **queue (FIFO)**; forgetting pointer updates (top/front/rear).

### 1.5 Legal/ethical
- Naming the **wrong Act** for a scenario (learn the four and one example breach of each).
- Writing a **one-sided** essay — top band needs balance *and* multiple stakeholders.
- No **justified conclusion** on the 9–12 markers.

---

## Component 02 — content-specific traps

### 2.1 Computational thinking
- **Defining** the terms instead of **applying** them to the scenario given.
- Confusing **abstraction** (removing detail) with **decomposition** (breaking into parts).

### 2.2 Programming
- **Recursion**: missing/incorrect **base case** → infinite recursion; not knowing it uses the **call stack**.
- **By value vs by reference** mixed up (by reference can change the original).
- **Scope**: assuming a local variable is visible globally.
- OOP: confusing **class vs object**, or **encapsulation vs inheritance vs polymorphism**.

### 2.3 Algorithms
- Quoting **Big O** wrong (binary search is **O(log n)**; merge sort **O(n log n)**; bubble/insertion worst **O(n²)**).
- Tracing sorts inaccurately — **do a trace table**, one pass at a time.
- **Dijkstra**: not updating tentative distances / not picking the lowest-cost unvisited node.
- Confusing **DFS vs BFS**, or the tree-traversal orders (pre/in/post-order).
- Recommending an algorithm without **justifying by time/space** for the given dataset.

---

## Your personal error log

The most powerful version of this page is the one **you** write. Every time you lose a mark in practice, add a line:

```
Topic | What I got wrong | The correct point | One-line fix
```

Re-read your own log before each paper. Fixing *your* repeat mistakes is the fastest route from a pass to an A\*.
