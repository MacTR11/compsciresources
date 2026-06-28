# Recap Checkpoint 6 — Full Year 12 Cumulative (Pre-Mock): 1.1–1.5 + 2.1–2.3

Name: ______________________   Date: __________   Mark: ______ / 40

*OCR H446 cumulative recap — mixes every topic taught so far. Show all working.*

## Questions

**Q1 [3] (AO1).** *(1.1 — Processors)* State **three** factors that affect the **performance** of a processor, and for each give a brief explanation of its effect.

**Q2 [4] (AO2).** *(1.4 — Number bases)* Show all working.
(a) Convert denary **181** to **8-bit binary**. **[1]**
(b) Convert **181** to **hexadecimal**. **[2]**
(c) Convert binary **`1010 0110`** to denary. **[1]**

**Q3 [4] (AO2).** *(1.4 — Two's complement)* Using **8-bit two's complement**, calculate **−40 + 25**.
(a) Show 40 and 25 in 8-bit binary. **[1]**
(b) Form the two's complement representation of −40. **[1]**
(c) Perform the addition and give the final **denary** result. **[2]**

**Q4 [3] (AO2).** *(1.4 — Boolean algebra / floating point)*
(a) State the result of the floating-point benefit of **normalisation** (why numbers are normalised). **[1]**
(b) Simplify **A + A·B** and name the law used. **[2]**

**Q5 [4] (AO1).** *(1.3 — Networks)* 
(a) Explain the difference between **circuit switching** and **packet switching**. **[2]**
(b) State **two** items of data added to a packet's **header**. **[2]**

**Q6 [3] (AO1/AO3).** *(1.5 — Legal/ethical)* Self-driving cars must sometimes "decide" how to act in an unavoidable collision.
Discuss **one ethical** issue this raises and identify **who** might be held **legally responsible** in a crash. **[3]**

**Q7 [4] (AO2).** *(2.1 / 2.2 — Computational thinking + programming)*
(a) State the difference between a **procedure** and a **function**. **[1]**
(b) Explain the difference between **passing a parameter by value** and **by reference**. **[2]**
(c) State **one** advantage of using **local** variables over **global** variables. **[1]**

**Q8 [5] (AO2).** *(2.3 — Algorithm trace)* A list contains `[7, 2, 9, 4, 1]`. Carry out a **bubble sort**, showing the list after **each complete pass**. State how many passes are needed before the list is sorted, and give the **worst-case** time complexity of bubble sort.

**Q9 [4] (AO1/AO2).** *(2.3 — Big O reasoning)*
(a) State the worst-case Big O of: insertion sort, merge sort, and a binary search. **[3]**
(b) Explain why merge sort is preferable to insertion sort for very large datasets, referencing growth rates. **[1]**

**Q10 [6] (AO3).** *(2.3 — Graphs, applied)* Using **Dijkstra's algorithm**, find the shortest **distance** and shortest **path** from **A** to **E** in the weighted, undirected graph below. Show a table of tentative distances and the order in which nodes are visited.

```
Edges (undirected, weighted):
A-B = 2,  A-C = 5,  B-C = 1,  B-D = 7,  C-D = 3,  C-E = 8,  D-E = 2
```

**Q11 [4 + (rest)] (AO3).** *(Synoptic extended response)* A hospital is replacing a paper appointment system with networked software that stores patient data, lets staff search records, and sends automated reminders.
In an extended response, discuss the design considering: **(i)** how **abstraction and decomposition** help manage the build, **(ii)** an appropriate **data structure or search algorithm** for fast record lookup (justify with time complexity), and **(iii)** **one legal** consideration for storing patient data. **[6]**

---

## Mark scheme

**Q1 [3] (AO1).** Any three (1 each, factor + effect):
- **Clock speed** — more cycles per second → more instructions executed per second.
- **Number of cores** — more cores allow more instructions/tasks to run in **parallel**.
- **Cache size/amount** — larger/faster cache reduces fetches from slower main memory, speeding access.
- (Also accept word/bus width, pipelining.)

*Examiner tip: each mark needs a named factor AND its effect — a bare list of words scores less.*

---

**Q2 [4] (AO2).**
- (a) 181 = `1011 0101` (1). *(128+32+16+4+1 = 181)*
- (b) 181 ÷ 16 = 11 remainder 5 → high nibble 11 = B, low nibble 5 = 5 → **B5** (1 method, 1 answer). *(Check: `1011`=B, `0101`=5.)*
- (c) `1010 0110` = 128+32+4+2 = **166** (1).

*Examiner tip: nibble-check binary↔hex: 181 = `1011 0101` = B5 — the two must agree.*

---

**Q3 [4] (AO2).** −40 + 25 in 8-bit two's complement:
- (a) 40 = `0010 1000`, 25 = `0001 1001` (1 for both).
- (b) −40: invert `0010 1000` → `1101 0111`, add 1 → **`1101 1000`** (1).
- (c) `1101 1000` + `0001 1001` = `1111 0001` (1). Leading 1 → negative; magnitude = invert+1 of `1111 0001` = `0000 1111` = 15, so result = **−15** (1).

*Examiner tip: −40 + 25 = −15. The sum `1111 0001` is negative — decode to confirm −15.*

---

**Q4 [3] (AO2).**
- (a) Normalisation gives the **greatest possible precision/accuracy** for a given number of mantissa bits (and a unique representation) (1).
- (b) A + A·B = A·(1 + B) = A·1 = **A** (1 for answer A); law: **Absorption** (accept Distributive + identity) (1).

*Examiner tip: absorption law A + A·B = A — the B term is redundant.*

---

**Q5 [4] (AO1).**
- (a) **Circuit switching** sets up a **dedicated end-to-end path** held for the whole communication; **packet switching** splits data into **packets routed independently**, sharing the network, reassembled at the destination (1 each, up to 2).
- (b) Any two (1 each): **destination IP/address**, **source IP/address**, **packet/sequence number**, **TTL/hop count**, **protocol**.

*Examiner tip: sequence number is needed because packets can arrive out of order and must be reassembled.*

---

**Q6 [3] (AO1/AO3).**
- Ethical issue (1–2): e.g. how the car should **prioritise lives** (passengers vs pedestrians), fairness of programmed decisions, transparency/accountability of the algorithm.
- Legal responsibility (1): could be the **manufacturer/software developer**, the **owner/driver**, or shared — credit a reasoned choice (e.g. manufacturer if the autonomous system was in control).
- Up to 3 total with reasoning.

*Examiner tip: examiners want a reasoned position on responsibility, not just "it's complicated".*

---

**Q7 [4] (AO2).**
- (a) A **function returns a value**; a **procedure performs actions and need not return a value** (1).
- (b) **By value**: a **copy** of the data is passed, so changes inside the subprogram **do not affect** the original (1). **By reference**: the **address/reference** is passed, so changes **do affect** the original variable (1).
- (c) Local variables (1): avoid unintended side effects / name clashes; memory is **freed when the subprogram ends**; improves modularity and maintainability (any one).

*Examiner tip: by value = copy (safe, isolated); by reference = original can be changed.*

---

**Q8 [5] (AO2).** Bubble sort on `[7, 2, 9, 4, 1]`:

| Pass | Result after pass |
|------|-------------------|
| 1 | `[2, 7, 4, 1, 9]` |
| 2 | `[2, 4, 1, 7, 9]` |
| 3 | `[2, 1, 4, 7, 9]` |
| 4 | `[1, 2, 4, 7, 9]` ✓ |

- Correct list after pass 1 → `[2, 7, 4, 1, 9]` (1).
- Correct list after pass 2 → `[2, 4, 1, 7, 9]` (1).
- Correct lists after passes 3 and 4 → sorted `[1, 2, 4, 7, 9]` (1).
- **4 passes** needed before the list is sorted (1).
- Worst-case time complexity **O(n²)** (1).

*Examiner tip: one pass = comparing/swapping adjacent pairs left to right once. The largest value "bubbles" to the end each pass.*

---

**Q9 [4] (AO1/AO2).**
- (a) Insertion sort **O(n²)** (1); merge sort **O(n log n)** (1); binary search **O(log n)** (1).
- (b) For large n, **n log n grows much more slowly than n²**, so merge sort scales far better / does far fewer operations (1).

*Examiner tip: O(n log n) beats O(n²) as n grows — the gap widens rapidly for large datasets.*

---

**Q10 [6] (AO3).** Dijkstra's algorithm, A → E. Tentative distances from A ("—" = settled):

| Step | Current | A | B | C | D | E | Visited |
|------|---------|---|---|---|---|---|---------|
| Init | – | 0 | ∞ | ∞ | ∞ | ∞ | {} |
| 1 | **A** (0) | — | **2** | 5 | ∞ | ∞ | {A} |
| 2 | **B** (2) | — | — | min(5, 2+1)=**3** | min(∞, 2+7)=9 | ∞ | {A,B} |
| 3 | **C** (3) | — | — | — | min(9, 3+3)=**6** | min(∞, 3+8)=11 | {A,B,C} |
| 4 | **D** (6) | — | — | — | — | min(11, 6+2)=**8** | {A,B,C,D} |
| 5 | **E** (8) | — | — | — | — | — | {A,B,C,D,E} |

- Correct initialisation: A = 0, others ∞ (1).
- B relaxed to 2, then C relaxed to 3 via B (1).
- Visits nodes in correct distance order **A, B, C, D, E** (1).
- Correct relaxation of D to 6 via C, and E updated to 8 via D (1).
- Shortest distance **A → E = 8** (1).
- Shortest path **A → B → C → D → E** (2 + 1 + 3 + 2 = 8), by tracing predecessors E ← D ← C ← B ← A (1).

*Examiner tip: always settle the smallest unvisited tentative distance next. Note A→C direct (5) is beaten by A→B→C (3) — relax carefully. State both distance (8) and path.*

---

**Q11 [6] (AO3).** Levelled extended response (up to 6). Indicative content across the three strands:
- **(i) Abstraction & decomposition**: decompose into modules — record storage, search, reminders, networking/security — built and tested separately; abstraction hides detail (e.g. model an appointment as date/time/patient ID, ignore irrelevant detail) so complexity is manageable (up to 2).
- **(ii) Data structure / search**: justify a **sorted structure + binary search O(log n)** or a **hash table O(1) average** for fast lookup, contrasted with linear search O(n) which is too slow for many records; reference time complexity explicitly (up to 2).
- **(iii) Legal**: patient data is **sensitive personal data** under data protection law (GDPR / Data Protection Act) — needs a lawful basis, **secure storage/encryption**, access control, and retention limits (up to 1–2).
- Mark holistically: a strong answer addresses all three strands with applied, justified reasoning; weaker answers describe one strand only.

*Examiner tip: this is a synoptic question — explicitly tie computational-thinking choices to a complexity justification AND name the relevant legislation for full credit.*

---

**Total: 40 marks.**
