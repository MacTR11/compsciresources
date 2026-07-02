# A* Stretch Pack — 03: Synoptic Stretch Questions

> **OCR A Level Computer Science (H446)**
> These questions deliberately cross component and topic boundaries. A* candidates are distinguished not by recalling isolated facts but by *joining ideas together* — linking representation to compression, hardware to complexity, data structures to algorithms, and theory to real systems.
>
> **How to use:** Attempt under timed conditions first. Write in continuous prose for the higher-mark "discuss/evaluate" parts (AO3 reward joined-up reasoning, not bullet lists). Then self-mark against the model answers, awarding yourself the band — not just the ticks.
>
> **AO reminder:** AO1 = knowledge/understanding · AO2 = apply knowledge to a context · AO3 = analyse, evaluate, make/justify decisions and program solutions.

---

## Question 1 — Compression, encryption and transmission across a network
**[12 marks — AO1 (3), AO2 (4), AO3 (5)]**

A messaging application sends a large image file from one user to another over the internet.
Explain how the data could be **compressed**, **encrypted** and **transmitted** across the network, and **evaluate** the trade-offs involved in the choices made.

<details><summary>Model answer / mark points</summary>

**Compression (link representation ↔ storage ↔ bandwidth):**
- The image is stored as binary data; its size determines transmission time and bandwidth use.
- **Lossy** compression (e.g. JPEG) discards data the human eye is less sensitive to, achieving high compression ratios but irreversibly losing detail — acceptable for photos.
- **Lossless** compression (e.g. PNG, run-length encoding, dictionary coding) allows perfect reconstruction; lower ratio but no quality loss — needed where exact data matters (e.g. medical imaging, text).
- Trade-off: smaller file = faster transfer / less bandwidth, but lossy reduces fidelity and lossless gives weaker compression. Compression itself costs CPU time at both ends.

**Encryption (link security ↔ keys ↔ performance):**
- To keep the data confidential in transit it is encrypted. **Symmetric** encryption (e.g. AES) uses one shared key — fast and suitable for the bulk image data.
- The problem is key distribution; this is solved using **asymmetric** encryption (public/private key pairs) to securely exchange the symmetric session key — i.e. a hybrid scheme as used in TLS/HTTPS.
- A **hash/digital signature** can verify integrity and authenticate the sender (non-repudiation).
- Trade-off: asymmetric is computationally expensive so it is used only to exchange the key, not the payload; stronger keys = more security but more processing.

**Transmission (link networks ↔ protocols ↔ layering):**
- Data is split into **packets**, each with header (source/destination IP, sequence number) and payload.
- The **TCP/IP stack** is used: application layer (e.g. HTTPS), transport layer (TCP provides reliable, ordered delivery via acknowledgements and retransmission), network layer (IP routing across networks), link layer.
- **Packet switching** routes packets independently; they may take different routes and are reassembled in sequence order at the destination; lost packets are retransmitted.
- Trade-off: TCP guarantees delivery but has overhead (acknowledgements, retransmission, ordering) vs UDP which is faster but unreliable — TCP is correct here since image integrity matters.

**Synoptic evaluation (top band):** A strong answer ties the three together as a pipeline — compress to reduce what must be encrypted and transmitted; encrypt the (now smaller) data; packetise and send reliably — and recognises competing pressures: CPU cost of compression/encryption vs bandwidth saved, security strength vs speed, reliability (TCP) vs latency (UDP). The candidate justifies a coherent overall design (e.g. lossless if quality critical + hybrid AES/RSA + TCP) rather than listing options.

**Band 3 (10–12):** Detailed, accurate coverage of all three areas, explicitly linked, with justified trade-offs.
**Band 2 (5–9):** Covers areas with some linkage; trade-offs partial.
**Band 1 (1–4):** Fragmented description of one or two areas, little linkage.
</details>

---

## Question 2 — Stacks in recursion vs expression evaluation
**[10 marks — AO1 (3), AO2 (4), AO3 (3)]**

Compare how a **stack** is used during **recursion** and during the **evaluation of an expression in Reverse Polish Notation (RPN)**. Use examples in your answer.

<details><summary>Model answer / mark points</summary>

**The stack in recursion (link data structures ↔ algorithms ↔ memory):**
- Each recursive call creates a **stack frame** pushed onto the **call stack**, storing the return address, parameters and local variables.
- Frames are popped (LIFO) as calls return, so execution "unwinds" back through the chain.
- Example: factorial(3) pushes frames for n=3, n=2, n=1; the base case (n=1) returns, then frames pop multiplying back up: 1 → 2 → 6.
- Too-deep recursion exhausts the stack → **stack overflow**. This is why recursion can be less memory-efficient than iteration.

**The stack in RPN evaluation (link data structures ↔ algorithms ↔ compilers):**
- RPN (postfix) is evaluated by scanning left to right: **push operands**; on reaching an **operator, pop the required operands, apply it, push the result**.
- Example: `5 3 + 2 *` → push 5, push 3, see `+` pop 3 and 5 push 8, push 2, see `*` pop 2 and 8 push 16. Final stack top = 16.
- RPN needs no brackets or precedence rules — operator order in the string encodes evaluation order — which is why compilers/interpreters convert infix to postfix and evaluate with a stack.

**Comparison (top band):**
- *Similarity:* both rely on **LIFO** behaviour; the most recently stored item is the next needed — partial computations (frames / operands) are held until ready to combine.
- *Difference in what is stored:* recursion stores whole **execution contexts** (frames); RPN stores **data values** (operands/intermediate results).
- *Difference in control:* in recursion the stack is managed **implicitly by the runtime**; in RPN it is **explicitly managed by the algorithm**.
- *Link:* both demonstrate why the stack is the natural structure when work must be deferred and resumed in reverse order — recursion *is* an implicit stack-based process, which is why any recursive algorithm can be rewritten iteratively using an explicit stack.

**Mark guidance:** AO1 for correct stack/LIFO and frame definitions; AO2 for correct worked examples in both contexts; AO3 for the comparison drawing out the implicit/explicit and context/value distinctions and the unifying insight.
</details>

---

## Question 3 — Database query performance: complexity and indexing
**[12 marks — AO1 (3), AO2 (4), AO3 (5)]**

A database table `Customer` holds 10 million records. The query
`SELECT * FROM Customer WHERE Surname = 'Patel';`
runs slowly.
**Discuss** the performance of this query in terms of **algorithmic complexity** and **indexing**, and recommend improvements.

<details><summary>Model answer / mark points</summary>

**The problem (link databases ↔ algorithms ↔ Big O):**
- Without an index the DBMS performs a **full table scan**: it checks every record's `Surname`. This is a **linear search**, **O(n)** — for 10 million rows, up to 10 million comparisons.
- As `n` grows, query time grows proportionally, so the design does not **scale**.

**Indexing as the fix (link data structures ↔ search algorithms):**
- An **index** on `Surname` is a separate structure (a balanced, sorted index structure) mapping values to record locations, kept sorted.
- Searching a balanced tree index is **O(log n)** — roughly 24 comparisons for 10 million rows vs up to 10 million. This is the same speed-up as **binary search over linear search**, because the index keeps data ordered so half the remaining records are eliminated each step.
- The index lets the DBMS jump near-directly to matching records instead of scanning all of them.

**Trade-offs (top band, AO3):**
- Indexes **cost storage** and must be **updated on every INSERT/UPDATE/DELETE**, slowing writes — so index columns frequently *searched/joined*, not everything.
- `SELECT *` returns all columns; selecting only needed columns reduces data transferred and can allow a **covering index** (query answered from the index alone).
- A **primary key** is automatically indexed; searching by it is already fast — the issue here is searching by a **non-key** field.
- **Normalisation** keeps data consistent and reduces redundancy but adds **joins**, which themselves benefit from indexes on the joined/foreign-key columns; over-normalisation can hurt read performance (a denormalisation trade-off).

**Recommendation:** Create an index on `Surname` (turning O(n) → O(log n)), select only required columns, and index foreign keys used in joins — while accepting slower writes and extra storage as the cost. A complete answer explicitly maps the SQL behaviour to search-algorithm complexity and justifies *when* indexing is worthwhile.

**Band 3 (10–12):** Links full-scan→O(n), index→O(log n) with the binary-search analogy, and evaluates write/storage trade-offs.
**Band 2 (5–9):** Identifies indexing helps; complexity link partial.
**Band 1 (1–4):** Vague "add an index" with no complexity reasoning.
</details>

---

## Question 4 — Trace, justify Big O, and improve an algorithm
**[12 marks — AO1 (2), AO2 (5), AO3 (5)]**

Consider this pseudocode that checks whether an array contains any duplicate values:

```
function hasDuplicate(arr)
  for i = 0 to length(arr) - 1
    for j = 0 to length(arr) - 1
      if i != j AND arr[i] == arr[j] then
        return true
  next j
  next i
  return false
endfunction
```

(a) **Trace** the algorithm for `arr = [4, 7, 4]` and state the result.
(b) **Justify** its Big O time complexity.
(c) **Suggest and justify a more efficient alternative.**

<details><summary>Model answer / mark points</summary>

**(a) Trace (AO2):**
- i=0 (arr[i]=4): j=0 skip (i==j); j=1 (7) 4≠7; j=2 (4) i≠j and 4==4 → **return true**.
- Result: **true** (the two 4s are detected). Award marks for showing the i/j comparisons and the early return on first match.

**(b) Big O justification (link algorithms ↔ complexity):**
- Two nested loops each run up to `n` times → up to `n²` comparisons → **O(n²)** (quadratic) in the worst case (no duplicate, e.g. all-distinct array runs all n² iterations).
- Best case is O(1) if an early duplicate is found, but Big O describes the **worst case**, so O(n²).
- Memory use is **O(1)** — no extra structures.

**(c) More efficient alternative (top band, AO3):**

*Option 1 — sort then scan adjacents:*
- Sort the array: **O(n log n)** (e.g. merge sort), then a single pass comparing each element to its neighbour: O(n).
- Overall **O(n log n)** — dominated by the sort — beating O(n²). Trade-off: mutates/needs ordering and uses sort's memory.

*Option 2 — hash set (usually best):*
- Insert each element into a **hash table / set**; before inserting, check if already present → duplicate found.
- Average **O(n)** time (O(1) average insert/lookup), at the cost of **O(n) extra memory** for the set.

**Justified recommendation:** The hash-set approach gives the best average time (O(n)) and is preferred when memory is available; sort-and-scan (O(n log n)) is better when extra memory is constrained or data already sorted. Both are asymptotically superior to the original O(n²), which only wins on memory (O(1)). A top answer states the **time–space trade-off** explicitly rather than just naming a faster method.

**Mark guidance:** (a) correct trace + result; (b) O(n²) with worst-case justification (not just "two loops"); (c) at least one valid faster algorithm with its complexity *and* the time/space trade-off.
</details>

---

## Question 5 — Floating point, binary representation and rounding errors
**[10 marks — AO1 (3), AO2 (4), AO3 (3)]**

A program summing many small floating-point currency values produces a slightly incorrect total.
Explain, with reference to how numbers are **represented in binary**, why this happens, and **evaluate** how a developer could avoid it.

<details><summary>Model answer / mark points</summary>

**Representation cause (link binary ↔ floating point ↔ data representation):**
- Floating-point numbers are stored as **mantissa × 2^exponent** in a fixed number of bits.
- Many decimal fractions (e.g. 0.1, 0.2) have **no exact finite binary representation** — they recur in binary, just as ⅓ recurs in decimal — so they are stored as the nearest representable value: a **rounding/representation error**.
- The mantissa has **finite precision**; bits beyond it are lost. Summing many such approximations lets small errors **accumulate**, so the total drifts from the true value.

**Why it matters here:** Currency needs exact arithmetic; tiny per-value errors compound across many additions, producing a visible discrepancy.

**Evaluation of fixes (top band, AO3):**
- **Use integers** (store amounts in pence/cents as whole numbers) — exact, no fractional binary error; recommended for currency. Trade-off: must scale on input/output.
- **Fixed-point / decimal types** — represent decimals exactly within range; slower than native floats.
- **Increase precision** (e.g. double rather than single) — reduces but does **not eliminate** error; only delays the problem.
- **Round only at the end / for display** — avoids propagating intermediate rounding.

**Trade-off summary:** more bits = greater range/precision but more storage and slower; the real fix for currency is to avoid floating point's inexactness entirely by using integers or decimal types. A top answer links *why* (no exact binary fraction + finite mantissa + accumulation) to *what to do* and weighs the options rather than just saying "use more decimal places".

**Mark guidance:** AO1 mantissa/exponent + finite precision; AO2 the recurring-binary-fraction explanation applied to 0.1-style values and accumulation; AO3 evaluated, justified fix (integers/decimal preferred).
</details>

---

## Question 6 — CPU performance: FDE cycle, architecture and limiting factors
**[12 marks — AO1 (4), AO2 (4), AO3 (4)]**

**Discuss** the factors that affect the performance of a CPU, with reference to the **fetch–decode–execute cycle**, **CPU architecture**, and the **memory hierarchy**.

<details><summary>Model answer / mark points</summary>

**The FDE cycle as the baseline (link CPU ↔ FDE ↔ registers):**
- Each instruction is fetched (PC → MAR → address bus; data → MDR via data bus; PC incremented), decoded by the CU, and executed (possibly using the ALU and accumulator).
- More cycles per second = more instructions processed.

**Performance factors (link hardware ↔ performance):**
- **Clock speed** (Hz): more cycles/second → more FDE cycles → faster — but limited by heat/power.
- **Number of cores**: multiple cores run instructions **in parallel**; benefits **multi-threaded** workloads, but gains are limited by tasks that can't be parallelised (sequential dependencies cap the speed-up).
- **Cache** (link to memory hierarchy): small, fast SRAM near the CPU holds frequently used data/instructions; **L1/L2/L3** levels. More/larger cache → fewer slow main-memory fetches → less stalling. Cache misses force slow RAM access.
- **Word length / bus width**: wider data/address buses move more bits per cycle and address more memory.
- **Pipelining**: overlapping fetch/decode/execute of successive instructions raises throughput; **branches** can stall the pipeline (must flush on misprediction).

**Architecture (link to assembly/instruction sets):**
- **Von Neumann**: shared memory/bus for data and instructions — simpler but a **bus bottleneck** (the von Neumann bottleneck).
- **Harvard**: separate instruction/data memories and buses — fetch instruction and data simultaneously, useful in embedded/DSP.
- **RISC vs CISC**: RISC's simple, uniform instructions pipeline efficiently; CISC does more per instruction but is harder to pipeline.

**Synoptic evaluation (top band):**
- Factors **interact**: a high clock speed is wasted if the CPU stalls waiting on memory (so cache matters), and extra cores help only parallelisable code. The "best" CPU depends on the **workload** — single-thread-bound work favours clock speed and IPC; parallel work favours cores; memory-bound work favours cache/bus width.
- A top answer treats performance as a **system** (cycle × architecture × memory hierarchy) and explains *why* simply increasing one factor hits diminishing returns, rather than listing factors in isolation.

**Band 3 (10–12):** Multiple factors, correctly linked to FDE/architecture/memory, with interaction/diminishing-returns reasoning.
**Band 2 (5–9):** Several factors, some explanation, limited linkage.
**Band 1 (1–4):** Lists factors without explanation.
</details>

---

## Question 7 — Hashing: data structures, databases and security
**[10 marks — AO1 (3), AO2 (4), AO3 (3)]**

The term "hashing" appears in **hash tables**, in **database indexing/storage**, and in **password security**.
Compare how hashing is used in these contexts and explain why a property that is desirable in one may be undesirable in another.

<details><summary>Model answer / mark points</summary>

**Common idea (link data representation ↔ algorithms):**
- A **hash function** maps an input (key) to a fixed-size value (hash) used as an address or fingerprint. Same input → same output (deterministic).

**Hash tables (link data structures):**
- The hash of a key gives an **index/bucket** for storing/retrieving the item, giving **average O(1)** insertion and lookup.
- **Collisions** (two keys → same index) are resolved by **chaining** or **open addressing**. A *good* table hash spreads keys **evenly** and is **fast** to compute.

**Database storage/indexing (link databases):**
- Hashing can place records into buckets for fast direct access, or hash indexes support equality lookups in O(1) average. Same goals: even distribution, speed, few collisions.

**Password security (link security/encryption):**
- Passwords are stored as **hashes**, not plaintext; on login the entered password is hashed and compared. Because hashing is **one-way**, a stolen database doesn't reveal passwords.
- Here good properties are the **opposite** of table hashes: a cryptographic hash should be **slow/computationally expensive** (to resist brute force) and **collision-resistant in an adversarial sense**, and **salting** is added so identical passwords hash differently and rainbow tables fail.

**The key synoptic point (top band):**
- **Speed is desirable for hash tables but undesirable for password hashing**: a fast hash that spreads data well is ideal for lookups, but a *fast* hash is dangerous for passwords because it lets attackers try billions of guesses cheaply — hence deliberately slow, salted cryptographic hashes.
- Likewise, **collisions** are merely a performance nuisance in a hash table (handled by chaining) but a **security failure** in cryptographic hashing.

**Mark guidance:** AO1 define hash function/collision; AO2 correct use in each context; AO3 the inversion of "good" properties (fast & cheap vs slow & salted; collisions tolerated vs catastrophic) — the discriminating A* point.
</details>

---

## Question 8 — Recursion, data structures and real-world problem solving
**[12 marks — AO1 (3), AO2 (5), AO3 (4)]**

A file system stores folders that can contain files and other folders.
Explain how a **recursive algorithm** operating on a suitable **data structure** could calculate the total size of all files within a folder, and **evaluate** recursion versus iteration for this problem.

<details><summary>Model answer / mark points</summary>

**Suitable data structure (link data structures ↔ trees):**
- A file system is naturally a **tree**: each folder is a node whose children are its files (leaves) and subfolders (subtrees). This hierarchical structure is what makes recursion natural.

**Recursive algorithm (link recursion ↔ algorithms):**
```
function folderSize(folder)
  total = 0
  for each item in folder
    if item is a file then
      total = total + item.size
    else                        // item is a folder
      total = total + folderSize(item)   // recursive call
  next item
  return total
endfunction
```
- **Base case:** a folder with no subfolders (or empty) returns the sum of its files (recursion stops — no further calls).
- **General/recursive case:** for each subfolder, call `folderSize` and add the result — the problem is broken into the same problem on smaller subtrees.
- This is essentially a **depth-first traversal** of the tree.

**Why recursion fits (link to call stack):**
- The tree's arbitrary, unknown depth maps cleanly to recursion; each call handles one node and delegates subtrees. The **call stack** implicitly tracks where to resume in each folder.

**Evaluation: recursion vs iteration (top band, AO3):**
- *Recursion:* concise, mirrors the tree structure, easy to reason about. **But** each level adds a stack frame — very deep nesting risks **stack overflow**, and call overhead can be slower.
- *Iteration:* can do the same traversal using an **explicit stack** (or queue) — avoids recursion-depth limits and call overhead, and any recursive solution *can* be rewritten this way. **But** the code is longer and less readable because you manage the stack manually.
- **Justified conclusion:** recursion is preferable for clarity given the hierarchical data, *provided* nesting depth is bounded; for untrusted or potentially very deep structures, an iterative version with an explicit stack is safer. This shows the link that **recursion and an explicit-stack iteration are equivalent** — recursion just uses the call stack implicitly.

**Mark guidance:** AO1 tree + base/general case; AO2 a correct recursive algorithm with both cases and the size accumulation; AO3 a balanced, justified recursion-vs-iteration evaluation referencing the stack.
</details>

---

## Question 9 — From web request to database: a full synoptic trace
**[12 marks — AO1 (3), AO2 (4), AO3 (5)]**

A user submits a search form on a website. Describe and analyse the journey of this request from the browser to a back-end **database** and back, drawing together **networks**, **client–server**, **SQL** and **security**.

<details><summary>Model answer / mark points</summary>

**Client side (link web ↔ HTML/JS ↔ client-server):**
- The browser (client) collects form input; client-side **JavaScript** may validate it before sending, reducing invalid round-trips.
- The request is sent over **HTTPS** to the web server — a **client–server** interaction.

**Network transmission (link networks ↔ protocols):**
- DNS resolves the domain to an **IP address**; the request is split into **TCP/IP packets** and routed via packet switching across the internet to the server.
- **HTTPS/TLS** encrypts the request so search terms and any credentials are confidential in transit (hybrid symmetric/asymmetric encryption).

**Server and database (link client-server ↔ SQL ↔ databases):**
- The web server passes the request to server-side code, which builds an **SQL query**, e.g. `SELECT * FROM Product WHERE Name LIKE '%term%';`.
- The DBMS executes it — performance depends on **indexing** and query complexity (link to Q3): an index on the searched column turns an O(n) scan into ~O(log n).
- Results are returned to the server, formatted into HTML, and sent back to the client.

**Security analysis (top band, AO3 — link to defensive design):**
- **SQL injection:** if user input is concatenated directly into the query, an attacker could inject SQL (e.g. `'; DROP TABLE Product; --`). Mitigate with **parameterised queries/prepared statements** and **input validation/sanitisation**.
- **Encryption in transit** (HTTPS) protects confidentiality; **access control** limits what the query/account can do (least privilege).
- Validate **server-side** too — client-side validation can be bypassed.

**Synoptic evaluation (top band):**
- A top answer presents this as an end-to-end **pipeline** and analyses trade-offs at each stage: client vs server validation (UX vs trust), encryption (security vs CPU cost), indexing (read speed vs write/storage cost), and security (parameterisation as the correct defence vs naive concatenation). It explicitly connects networking, the client–server model, SQL/database performance and security rather than describing them separately.

**Band 3 (10–12):** Coherent end-to-end journey linking all four areas with security analysis (esp. SQL injection + parameterisation) and trade-offs.
**Band 2 (5–9):** Describes the journey, some areas linked, security partial.
**Band 1 (1–4):** Fragmented description of one or two stages.
</details>

---

## Question 10 — Boolean logic, hardware and abstraction
**[10 marks — AO1 (4), AO2 (3), AO3 (3)]**

Explain how the **Boolean logic** taught in theory connects to **physical hardware** and to the **abstraction** that lets programmers ignore that hardware. Use an adder as an example.

<details><summary>Model answer / mark points</summary>

**Boolean logic → gates (link logic ↔ hardware):**
- Boolean operations (AND, OR, NOT, XOR) are implemented physically as **logic gates** built from transistors acting as switches; voltages represent **1 and 0**.
- Truth tables specify behaviour; **Boolean algebra** (e.g. De Morgan's laws) lets designers **simplify** expressions to use fewer gates — cheaper, faster, less power.

**Example — the adder (link logic ↔ arithmetic ↔ representation):**
- A **half adder**: Sum = A XOR B, Carry = A AND B. It adds two bits but can't take a carry-in.
- A **full adder** adds A, B and a carry-in using two half adders plus an OR; chaining full adders builds an **n-bit adder** that performs binary addition in the **ALU**.
- This directly links to **binary representation**: the same circuitry, with two's complement, performs subtraction (add the negative), connecting logic gates to the number representations studied separately.

**Abstraction (link hardware ↔ software ↔ layers, top band):**
- Programmers write `a + b` in a high-level language without knowing about gates. Each layer **hides** the one below: high-level language → machine code → microarchitecture/ALU → logic gates → transistors.
- This **abstraction** lets developers reason about programs without electronics, while hardware engineers improve gates without breaking software — the layers have stable interfaces.

**Synoptic point (top band, AO3):**
- A strong answer shows the **unbroken chain**: a `+` in code ultimately triggers XOR/AND gates flipping transistor voltages, and explains *why* abstraction is valuable — it manages complexity and decouples concerns. It connects three areas usually taught apart (Boolean logic, data representation, and the hardware/software stack).

**Mark guidance:** AO1 gates + adder logic (XOR sum / AND carry); AO2 correct half/full adder and link to binary addition; AO3 the abstraction-layers argument explaining why hiding the hardware is beneficial.
</details>

---

## Question 11 — Sorting algorithms: complexity, data structures and suitability
**[12 marks — AO1 (3), AO2 (4), AO3 (5)]**

Compare **merge sort**, **bubble sort** and **insertion sort** in terms of **time complexity**, **space**, and **suitability**, and justify which you would choose to sort a very large dataset that does not fit in memory.

<details><summary>Model answer / mark points</summary>

**Complexity comparison (link algorithms ↔ Big O):**
- **Bubble sort:** O(n²) average/worst; O(n) best (already sorted, with a swap-flag optimisation). In-place, O(1) extra space. Simple but slow on large n.
- **Insertion sort:** O(n²) average/worst; **O(n) best** when nearly sorted. In-place, O(1) space. Efficient for **small or nearly-sorted** data; stable.
- **Merge sort:** **O(n log n)** in all cases (predictable) — repeatedly **divides** (link to recursion / divide-and-conquer) and **merges**. **But** needs **O(n) extra memory** for merging and is typically recursive (stack frames).

**Why O(n log n) beats O(n²) (link to scalability):**
- For large n the gap is enormous (e.g. n=1,000,000: n² ≈ 10¹² vs n log n ≈ 2×10⁷). Quadratic sorts don't scale; merge sort does.

**Data-structure / property links:**
- Merge sort is naturally **divide-and-conquer**, mirroring recursion and trees; it is **stable** and works well on **linked lists** (no random access needed).
- Bubble/insertion work in place on arrays with minimal extra memory.

**The large-dataset-not-in-memory decision (top band, AO3):**
- This is an **external sorting** problem. **Merge sort** is the right choice because its merge step processes data **sequentially** and can merge **sorted chunks streamed from disk**: split the data into memory-sized runs, sort each, write to disk, then **k-way merge** them. Bubble/insertion sort assume random in-memory access and are O(n²) — unusable at this scale.
- **Trade-off acknowledged:** merge sort's O(n) extra space is acceptable here because the merge reads/writes sequentially (disk-friendly), and its guaranteed O(n log n) matters when n is huge. The cost is extra disk space for the runs and I/O overhead.

**Justified conclusion:** choose **merge sort** for the large external dataset (predictable O(n log n) + sequential, mergeable runs); insertion sort would only be sensible for the small in-memory sub-runs if nearly sorted. A top answer connects the **algorithmic complexity**, the **memory/space constraint**, and the **physical I/O** characteristics into one justified decision.

**Band 3 (10–12):** Accurate complexities, space and stability, with a fully justified external-sort decision linking complexity to the memory/disk constraint.
**Band 2 (5–9):** Compares algorithms; decision partially justified.
**Band 1 (1–4):** Lists complexities with little comparison or justification.
</details>

---

## Question 12 — Programming paradigms, abstraction and maintainability
**[10 marks — AO1 (3), AO2 (3), AO3 (4)]**

A large program is being rewritten. **Discuss** how choosing an **object-oriented** approach (vs procedural) relates to **abstraction**, **data structures**, and the long-term **maintainability** of the software.

<details><summary>Model answer / mark points</summary>

**Paradigms recap (link paradigms ↔ programming):**
- **Procedural:** program as a sequence of procedures/functions operating on shared data.
- **Object-oriented (OOP):** program as **objects** bundling **data (attributes)** and **behaviour (methods)**; built from **classes**.

**OOP and abstraction (link OOP ↔ abstraction):**
- **Encapsulation** hides internal state behind methods (a public interface), so other code depends on *what* an object does, not *how* — a form of abstraction that limits ripple effects when internals change.
- **Inheritance** lets subclasses reuse/extend a base class; **polymorphism** lets different objects respond to the same method call appropriately — reducing duplication.

**OOP and data structures (link OOP ↔ data structures):**
- Objects model real-world entities and complex data structures cleanly (e.g. a `Tree` class with `Node` objects, a `Stack` class exposing push/pop while hiding the array/list inside).
- This packages a data structure **with** its valid operations, enforcing correct use (you can't bypass `push`/`pop` to corrupt the stack) — encapsulation protecting invariants.

**Maintainability (top band, AO3):**
- **Modularity:** classes are self-contained units, so changes are **localised** — easier to test, debug and extend; teams can work on separate classes.
- **Reuse:** inheritance/composition reduce duplicated code, so a fix in one place propagates.
- **Trade-offs:** OOP adds **design overhead and complexity**, can be **slower / more memory-heavy** (object overhead), and poor design (deep inheritance, tight coupling) can *harm* maintainability — procedural may be simpler and faster for small or performance-critical programs.

**Synoptic evaluation:** A top answer connects **abstraction (encapsulation)** → **safe data-structure handling** → **maintainability (localised change, reuse)**, and gives a **justified** position: OOP suits large, evolving codebases where maintainability dominates, while procedural can be preferable for small or low-level/performance-critical code — i.e. the choice is context-dependent, not absolute.

**Mark guidance:** AO1 define paradigms + encapsulation/inheritance/polymorphism; AO2 apply to data structures and a concrete example; AO3 a balanced, justified maintainability discussion with trade-offs.
</details>

---

### Self-assessment guidance (A/A* boundary)

| Trait of an A* response | Trait of a borderline response |
|---|---|
| **Links** topics explicitly ("…which is the same idea as…") | Treats each topic separately |
| States and **justifies trade-offs** | Lists options without choosing |
| Uses correct **technical vocabulary** in every area touched | Vocabulary strong in one area, vague in others |
| Reaches a **justified conclusion/decision** | Describes without evaluating |
| Connects **theory to a real system/context** | Stays abstract or stays concrete, never both |

> **Examiner tip:** Synoptic marks (AO3) are won in the *connections*. When you finish a paragraph, ask: "Which *other* H446 topic does this touch, and have I said so?"
