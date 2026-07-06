# Recap Checkpoint 6 — Full Year 12 Cumulative (Pre-Mock): 1.1–1.4 + 2.1 + 2.2.1

Name: ______________________   Date: __________   Mark: ______ / 46

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
(a) State why floating-point numbers are **normalised**. **[1]**
(b) Simplify **A ∨ A∧B** and name the law used. **[2]**

**Q5 [4] (AO1).** *(1.3 — Networks)* 
(a) Explain the difference between **circuit switching** and **packet switching**. **[2]**
(b) State **two** items of data added to a packet's **header**. **[2]**

**Q6 [3] (AO1).** *(1.2 — Operating systems)*
(a) State what is meant by **scheduling** and name **one** scheduling algorithm. **[2]**
(b) State the purpose of a **device driver**. **[1]**

**Q7 [4] (AO2).** *(2.1 / 2.2.1 — Computational thinking + programming)*
(a) State the difference between a **procedure** and a **function**. **[1]**
(b) Explain the difference between **passing a parameter by value** and **by reference**. **[2]**
(c) State **one** advantage of using **local** variables over **global** variables. **[1]**

**Q8 [5] (AO2).** *(1.4 — Data structures trace)* A **stack** is initially empty. The following operations are carried out in order: `push(7)`, `push(2)`, `push(9)`, `pop()`, `push(4)`, `pop()`, `pop()`.
(a) State the value returned by **each** of the three `pop()` calls, in order. **[2]**
(b) State the contents of the stack after all seven operations. **[1]**
(c) The same seven operations are repeated using a **queue** (`enqueue` in place of `push`, `dequeue` in place of `pop`). State the values returned by the three `dequeue()` calls, and name the access order each structure demonstrates. **[2]**

**Q9 [4] (AO1/AO2).** *(2.1 — Computational thinking)*
(a) State what is meant by **abstraction** and give **one** example of its use in software. **[2]**
(b) **Caching** is often described as an example of *thinking ahead*. State what caching is and give **one** benefit it provides. **[2]**

**Q10 [6] (AO1/AO2).** *(1.4 — Boolean logic: adders)*
(a) Complete the **Sum** and **Carry** columns of the truth table for a **half adder**. **[2]**

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 |     |       |
| 0 | 1 |     |       |
| 1 | 0 |     |       |
| 1 | 1 |     |       |

@@SPACE:0@@

(b) Name the **logic gate** that produces the Sum output and the logic gate that produces the Carry output. **[2]**
(c) State **one** way a **full adder** differs from a half adder, and explain why this difference allows full adders to be chained together to add multi-bit binary numbers. **[2]**

**Q11 [6] (AO3).** *(Synoptic extended response)* A hospital is replacing a paper appointment system with networked software that stores patient data, lets staff search records, and sends automated reminders.
In an extended response, discuss the design considering: **(i)** how **abstraction and decomposition** help manage the build, **(ii)** an appropriate **data structure** for fast record lookup (justify your choice), and **(iii)** **one security** consideration for transmitting and storing patient data. **[6]**

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
- (b) A ∨ A∧B = A∧(1 ∨ B) = A∧1 = **A** (1 for answer A); law: **Absorption** (accept Distributive + identity) (1).

*Examiner tip: absorption law A ∨ A∧B = A — the B term is redundant.*

---

**Q5 [4] (AO1).**
- (a) **Circuit switching** sets up a **dedicated end-to-end path** held for the whole communication; **packet switching** splits data into **packets routed independently**, sharing the network, reassembled at the destination (1 each, up to 2).
- (b) Any two (1 each): **destination IP/address**, **source IP/address**, **packet/sequence number**, **TTL/hop count**, **protocol**.

*Examiner tip: sequence number is needed because packets can arrive out of order and must be reassembled.*

---

**Q6 [3] (AO1).**
- (a) Scheduling: the OS **decides which process is given CPU time** / manages the order in which processes run, to make best use of the processor and keep all jobs progressing (1). Algorithm — any one (1): **round robin**, **first come first served**, **shortest job first**, **shortest remaining time**, **multilevel feedback queues**.
- (b) A device driver is software that **allows the OS to communicate with and control a specific piece of hardware** (translates generic OS commands into device-specific instructions) (1).

*Examiner tip: scheduling answers must mention the processor/CPU time — "organises programs" alone is too vague.*

---

**Q7 [4] (AO2).**
- (a) A **function returns a value**; a **procedure performs actions and need not return a value** (1).
- (b) **By value**: a **copy** of the data is passed, so changes inside the subprogram **do not affect** the original (1). **By reference**: the **address/reference** is passed, so changes **do affect** the original variable (1).
- (c) Local variables (1): avoid unintended side effects / name clashes; memory is **freed when the subprogram ends**; improves modularity and maintainability (any one).

*Examiner tip: by value = copy (safe, isolated); by reference = original can be changed.*

---

**Q8 [5] (AO2).** Stack trace: push(7) → `7`; push(2) → `7, 2`; push(9) → `7, 2, 9`; pop() returns **9**; push(4) → `7, 2, 4`; pop() returns **4**; pop() returns **2**.
- (a) Pops return **9, 4, 2** in that order (all three correct = 2; two correct = 1).
- (b) Final stack contents: **7** only (1).
- (c) Queue trace: enqueue 7, 2, 9 → `7, 2, 9`; dequeue returns **7**; enqueue 4 → `2, 9, 4`; dequeue returns **2**; dequeue returns **9** — returns **7, 2, 9** (1). Stack is **LIFO** (last in, first out); queue is **FIFO** (first in, first out) (1).

*Examiner tip: a pop always takes the most recently pushed item still present; a dequeue takes the oldest.*

---

**Q9 [4] (AO1/AO2).**
- (a) Abstraction: **removing/hiding unnecessary detail** to focus on what matters for the problem (1). Example (1): the London Underground map; a file/folder icon hiding how data is stored; a variable or class representing a real-world entity; a subroutine hiding its implementation behind its name/interface.
- (b) Caching: data that has been used (or is expected to be needed) is **stored in faster-to-access memory/storage after first use** so it does not have to be recomputed/refetched (1). Benefit (1): faster subsequent access / reduced load on the slower source (e.g. web pages, database query results, CPU cache).

*Examiner tip: caching is "thinking ahead" because you anticipate that the data will be needed again.*

---

**Q10 [6] (AO1/AO2).**
- (a) Completed half-adder truth table (Sum column fully correct = 1; Carry column fully correct = 1):

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

- (b) Sum is produced by an **XOR** gate (1); Carry is produced by an **AND** gate (1).
- (c) A full adder has a **third input — the carry in** (from the previous, less significant column) (1); because each full adder accepts a carry in and produces a carry out, the carry can **ripple from one bit position to the next**, so a chain of full adders can add multi-bit binary numbers column by column (1).

*Examiner tip: half adder = XOR (sum) + AND (carry); the full adder's carry-in is exactly what makes chaining possible.*

---

**Q11 [6] (AO3).** Levelled extended response (up to 6). Indicative content across the three strands:
- **(i) Abstraction & decomposition**: decompose into modules — record storage, search, reminders, networking/security — built and tested separately; abstraction hides detail (e.g. model an appointment as date/time/patient ID, ignore irrelevant detail) so complexity is manageable (up to 2).
- **(ii) Data structure**: justify a **hash table** (a hashed key such as the patient ID gives near-direct access to a record without examining every entry) or a **sorted array/indexed structure** (allows the search to repeatedly discard half the records rather than checking each one), contrasted with an unsorted list where every record may need checking — far too slow for many records (up to 2).
- **(iii) Security**: patient data is sensitive, so it should be **encrypted** in storage and in transit (e.g. so intercepted packets are unreadable), with **access control/authentication** limiting which staff can view records (up to 2).
- Mark holistically: a strong answer addresses all three strands with applied, justified reasoning; weaker answers describe one strand only.

*Examiner tip: this is a synoptic question — tie the computational-thinking choices to the scenario AND justify the data-structure choice by how it avoids checking every record.*

---

**Total: 46 marks.**
