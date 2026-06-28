# Recap Checkpoint 3 — after 1.4 (Data Types, Data Structures & Boolean Algebra) — cumulative 1.1–1.4

Name: ______________________   Date: __________   Mark: ______ / 35

*OCR H446 cumulative recap — mixes every topic taught so far. Show all working.*

## Questions

**Q1.** State **one** difference between **CISC** and **RISC** processors, referring to the instruction set. **[2]** *(AO1)* — *1.1.2*

**Q2.** Explain what is meant by **virtual memory** and give **one** drawback of relying on it heavily. **[3]** *(AO1/AO2)* — *1.2.1*

**Q3.** Place the four stages of compilation in the correct order, and name the stage that **removes redundant instructions to make the object code more efficient**: *code generation, lexical analysis, optimisation, syntax analysis*. **[3]** *(AO1)* — *1.2.2*

**Q4.** A company hashes stored passwords but **encrypts** the customer data it transmits. Explain, referring to the **key difference between hashing and encryption**, why each technique is appropriate for its purpose. **[3]** *(AO2)* — *1.3.1*

**Q5.** Convert the denary number **89** into:
(a) 8-bit binary **[1]** *(AO2)*
(b) hexadecimal **[2]** *(AO2)*
Show your working. **[3 total]** — *1.4.1*

**Q6.** Using **8-bit two's complement**, calculate **39 − 52**. You must:
(a) show 39 and 52 in 8-bit binary **[1]** *(AO2)*
(b) form the two's complement of 52 **[1]** *(AO2)*
(c) perform the addition and state the final **denary** result **[2]** *(AO2)*
**[4 total]** — *1.4.1*

**Q7.** A floating point value is shown as **`0.0001101 × 2⁴`** (mantissa with the point after the sign bit, exponent in denary).
(a) Normalise the mantissa and state the new exponent. **[2]** *(AO2)*
(b) Explain **why** numbers are normalised. **[1]** *(AO1)*
**[3 total]** — *1.4.1*

**Q8.** Simplify the Boolean expression **A·(Ā + B)** using Boolean identities. Show each step and name the identities used. **[3]** *(AO2)* — *1.4.3*

**Q9.** Complete the truth table for **F = (A + B)·¬(A·B)** and state which single logic gate it is equivalent to. **[4]** *(AO2)* — *1.4.3*

| A | B | F |
|---|---|---|
| 0 | 0 |   |
| 0 | 1 |   |
| 1 | 0 |   |
| 1 | 1 |   |

**Q10.** A **stack** (implemented in an array) is initially empty. The following operations are applied in order:
`push 8, push 3, push 5, pop, push 9, pop`.
(a) State the value returned by **each** `pop` operation. **[2]** *(AO3)*
(b) State the contents of the stack (bottom → top) after all operations, and explain why a stack is described as **LIFO**. **[2]** *(AO3)*
**[4 total]** — *1.4.2*

**Q11.** The values **60, 40, 80, 30, 50, 70** are inserted, in that order, into an initially empty **binary search tree**.
(a) Draw or describe the resulting tree. **[2]** *(AO3)*
(b) State the order of values produced by an **in-order** traversal and what this demonstrates about a BST. **[2]** *(AO3)*
**[4 total]** — *1.4.2*

**Q12.** An embedded controller for a heart-rate monitor must store readings, process them in real time, and use as little power as possible. The design team must justify, **synoptically**, three decisions: the **processor architecture (RISC vs CISC)**, an appropriate **data structure** to buffer the most recent readings, and whether to use a **lossy or lossless** compression scheme before transmitting stored readings to a doctor. Evaluate suitable choices for **all three**, justifying each against the device's requirements. **[6]** *(AO3)* — *synoptic 1.1 + 1.4 + 1.3*

---

## Mark scheme

*Total = 35 marks. Award marks for valid alternatives in line with OCR positive-marking. All calculations checked below.*

**Q1 — [2] (AO1)** — *1.1.2*
- **CISC** has a **large/complex instruction set** with variable-length, multi-cycle instructions (complexity in hardware) (1).
- **RISC** has a **small/simple instruction set** of fixed-length, single-cycle instructions (complexity in software/compiler) (1).

**Q2 — [3]** — *1.2.1*
- Virtual memory uses **secondary storage as if it were RAM** (1)…
- …so programs **larger than physical RAM, or more programs than fit in RAM, can run** (1). *(AO1)*
- Drawback (1): **disk thrashing** — heavy paging in/out slows the system because secondary storage is much slower than RAM. *(AO2)*

**Q3 — [3] (AO1)** — *1.2.2*
- Correct order (2; 1 mark if one pair transposed): **lexical analysis → syntax analysis → code generation → optimisation**.
- The stage that removes redundant instructions / improves efficiency is **optimisation** (1).

**Q4 — [3] (AO2)** — *1.3.1*
- Key difference (1): **hashing is one-way / irreversible**; **encryption is two-way / reversible** with a key.
- Passwords are **hashed** because they **never need to be recovered** — login only compares hashes, so a stolen database does not reveal plaintext (1).
- Transmitted data is **encrypted** because the **recipient must recover (decrypt) the original data**, which requires a reversible process (1).

**Q5 — [3]** — *1.4.1*
(a) 89 = 64 + 16 + 8 + 1 → **`0101 1001`** (1). *(AO2)*
(b) Nibbles `0101` = 5, `1001` = 9 → **0x59** (1 for nibble split, 1 for answer = 2). *(AO2)*
*Check: 5 × 16 + 9 = 80 + 9 = 89 ✓.*

**Q6 — [4] (AO2)** — *1.4.1*
(a) 39 = `0010 0111`; 52 = `0011 0100` (1).
(b) −52: invert `0011 0100` → `1100 1011`, add 1 → **`1100 1100`** (1).
(c) Add `0010 0111 + 1100 1100`:
```
  0 0 1 0 0 1 1 1   (39)
+ 1 1 0 0 1 1 0 0   (-52)
-----------------
  1 1 1 1 0 0 1 1
```
Result `1111 0011` has MSB = 1 → negative; magnitude = invert + 1 = `0000 1100 + 1` = `0000 1101` = 13, so the answer is **−13** (1 for the addition, 1 for converting back to denary).
*Check: 39 − 52 = −13 ✓.*

**Q7 — [3]** — *1.4.1*
(a) Mantissa must start `0.1…`; `0.0001101` so shift the point **right by 3** places → `0.1101` (1). Moving the point right by 3 **reduces the exponent by 3**: 4 − 3 = **1**, giving **`0.1101 × 2¹`** (1). *(AO2)*
(b) Normalising removes wasted leading zeros so the mantissa holds the **maximum significant figures / greatest precision** for the available bits (1). *(AO1)*
*Examiner tip: moving the point right DECREASES the exponent; the value is unchanged.*

**Q8 — [3] (AO2)** — *1.4.3*
- Distribute (distributive law): A·(Ā + B) = (A·Ā) + (A·B) (1).
- A·Ā = **0** (complement / annihilation law) (1).
- 0 + (A·B) = **A·B** (identity law) (1).
Final answer: **A·B**.

**Q9 — [4] (AO2)** — *1.4.3*

| A | B | F |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

(Working: `A+B` is 0,1,1,1; `¬(A·B)` is 1,1,1,0; AND them → 0,1,1,0.) *(1 mark per correct pair of rows = up to 2; allow follow-through.)*
F is 1 only when the inputs **differ**, so it is equivalent to an **XOR** gate (2 marks: 1 for the column completed correctly, 1 for identifying XOR).

**Q10 — [4] (AO3)** — *1.4.2*
(a) First `pop` returns **5**; second `pop` returns **9** (1 + 1).
Trace: push 8 → [8]; push 3 → [8,3]; push 5 → [8,3,5]; **pop → 5** → [8,3]; push 9 → [8,3,9]; **pop → 9** → [8,3].
(b) Stack contents bottom → top: **8, 3** (1). A stack is **LIFO (Last In, First Out)** — the **most recently pushed item is the first popped**, as both pops returned the most recent pushes (1).

**Q11 — [4] (AO3)** — *1.4.2*
(a) BST from inserting 60, 40, 80, 30, 50, 70:
```
        60
       /  \
     40    80
    /  \   /
  30   50 70
```
*(1 for 60 root with 40 left / 80 right; 1 for 30 & 50 under 40 and 70 as left child of 80.)*
(b) In-order (left, root, right): **30, 40, 50, 60, 70, 80** (1). This is **ascending sorted order**, demonstrating the BST ordering property (left subtree < node < right subtree) (1).

**Q12 — [6] (AO3)** — *synoptic 1.1 + 1.4 + 1.3*
Mark holistically; up to 6 from a reasoned evaluation covering **all three** decisions:
- **Processor:** recommend **RISC** (1) — fixed-length, single-cycle instructions give **low power consumption and predictable, fast real-time response** suited to a battery embedded device; *(reject CISC unless its fewer-instructions benefit is justified against the low-power need)* (1 for justification).
- **Data structure:** recommend a **(circular) queue** (1) to buffer the **most recent readings in time order (FIFO)** with fixed memory and O(1) enqueue/dequeue; *(accept a justified stack/array only with sound reasoning)* (1 for justification).
- **Compression:** recommend **lossless** (1) because **medical readings must not lose accuracy/data**, so lossy (which discards data) is unsuitable despite smaller files (1 for justification linking to clinical accuracy).
*Indicative full-mark answer weaves RISC (power/real-time) + circular queue (recent readings, FIFO, fixed memory) + lossless (data integrity), each justified against the heart-rate monitor's requirements.*
