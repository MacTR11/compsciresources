# Recap Checkpoint 1 — after 1.1 (Processors, Input/Output & Storage) + 1.2 (Software)

Name: ______________________   Date: __________   Mark: ______ / 30

*OCR H446 cumulative recap — mixes every topic taught so far. Show all working.*

## Questions

**Q1.** State the function of the **Program Counter (PC)** and the **Current Instruction Register (CIR)** during the Fetch–Decode–Execute cycle. **[2]** *(AO1)* — *1.1.1*

**Q2.** A processor uses **pipelining**.
(a) Explain what is meant by pipelining. **[2]** *(AO1)*
(b) State **one** situation in which the pipeline may have to be flushed. **[1]** *(AO1)*
**[3 total]** — *1.1.2*

**Q3.** A games studio is choosing hardware to render graphics that apply the **same calculation across millions of pixels in parallel**. Explain why a **GPU** is better suited to this than a general-purpose CPU. **[3]** *(AO2)* — *1.1.2*

**Q4.** A digital camera stores photographs onto a removable memory card.
(a) Name the **type of secondary storage** used by a typical memory card. **[1]** *(AO1)*
(b) Justify why this storage type is more suitable for a camera than a magnetic hard disk drive, referring to **two** distinct properties. **[2]** *(AO2)*
**[3 total]** — *1.1.3*

**Q5.** Explain how an **interrupt** is handled by the operating system, referring to the role of the **interrupt service routine (ISR)** and the **stack**. **[4]** *(AO1)* — *1.2.1*

**Q6.** An operating system uses a **paging** approach to memory management together with **virtual memory**.
(a) Explain what is meant by virtual memory. **[2]** *(AO1)*
(b) Describe **one** drawback of relying heavily on virtual memory. **[1]** *(AO2)*
**[3 total]** — *1.2.1*

**Q7.** A developer writes a program in a high-level language.
(a) State **one** difference between a **compiler** and an **interpreter**. **[2]** *(AO1)*
(b) Place the four stages of compilation in the correct order: *code generation, lexical analysis, syntax analysis, optimisation*. **[2]** *(AO1)*
**[4 total]** — *1.2.2*

**Q8.** A software team is choosing between the **Waterfall** and **Agile (e.g. extreme programming)** methodologies for a project whose requirements are expected to change frequently. Recommend a methodology and justify your choice, referring to **two** characteristics of the chosen methodology. **[4]** *(AO2)* — *1.2.3*

**Q9.** Object-oriented programming uses **encapsulation** and **inheritance**.
(a) Explain what is meant by **encapsulation**. **[2]** *(AO1)*
(b) Give **one** benefit of **inheritance** to a programming team. **[1]** *(AO2)*
**[3 total]** — *1.2.4*

**Q10.** A retailer is replacing its ageing tills. The new tills must run reliably for long shifts, recover quickly from power loss, and let staff carry out card payments and stock look-ups simultaneously. The IT manager must decide on the **type of processor architecture (CISC vs RISC)** and the **type of operating system** (real-time, multi-tasking, distributed). Evaluate suitable choices for **both** decisions, justifying each against the retailer's requirements. **[5]** *(AO3)* — *synoptic 1.1 + 1.2*

---

## Mark scheme

*Total = 30 marks. Award marks for valid alternatives in line with OCR positive-marking.*

**Q1 — [2] (AO1)** — *1.1.1*
- PC holds the **address of the next instruction** to be fetched (1).
- CIR holds the **current instruction** being decoded/executed (1).

**Q2 — [3] (AO1)** — *1.1.2*
(a) Pipelining **fetches, decodes and executes different instructions at the same time** (1) so that while one instruction is executing, the next is decoded and a third is fetched — increasing throughput/instructions completed per unit time (1).
(b) Any one (1): a **branch/jump** (conditional jump) means the pre-fetched instructions are wrong / a branch misprediction / an interrupt occurs.
*Examiner tip: pipelining improves throughput, not the time for a single instruction.*

**Q3 — [3] (AO2)** — *1.1.2*
- A GPU has **many (hundreds/thousands of) cores** (1)…
- …suited to **SIMD / massively parallel** processing of the same operation on many data items (1)…
- …so each pixel's identical calculation runs in parallel, whereas a CPU has few cores optimised for sequential/varied tasks, making it slower for this workload (1).

**Q4 — [3]** — *1.1.3*
(a) **Flash (solid-state)** storage (1). *(AO1)*
(b) Any two (1 + 1) *(AO2)*: **no moving parts** so it is more shock/drop resistant in a portable device; **lower power consumption** (battery life); **smaller/lighter/more compact**; **faster access** times; silent. *(Reject "more storage" — HDDs offer more capacity per £.)*

**Q5 — [4] (AO1)** — *1.2.1*
Award up to 4 from:
- The CPU **checks for interrupts at the end of each FDE cycle** (1).
- The current **contents of registers / state are saved onto the stack** (1).
- The appropriate **ISR is loaded/run** to service the interrupt (1).
- Interrupts are **prioritised** — only a higher-priority interrupt suspends the current ISR (1).
- When the ISR finishes, the **saved state is restored (popped) from the stack** and the original program resumes (1).

**Q6 — [3]** — *1.2.1*
(a) Virtual memory uses a **portion of secondary storage as if it were RAM** (1), so programs **larger than physical RAM can run** / more programs can be held than fit in RAM (1). *(AO1)*
(b) Heavy use causes **disk thrashing** — constant paging in/out of pages slows the system because secondary storage is far slower than RAM (1). *(AO2)*

**Q7 — [4] (AO1)** — *1.2.2*
(a) Any one difference for 2 marks (1 for each side, or 1+1 for a developed point):
- A compiler **translates the whole program at once** producing an executable; an interpreter **translates and executes line by line** (1).
- Compiled code **runs faster / no translator needed at run time**; interpreted code is **easier to debug / portable** (1).
(b) Correct order (2 marks; 1 mark if one pair transposed): **lexical analysis → syntax analysis → code generation → optimisation**.
*Examiner tip: lexical (tokenise) before syntax (parse); optimisation refines the generated code.*

**Q8 — [4] (AO2)** — *1.2.3*
- Recommend **Agile / extreme programming** (1)…
- …because requirements are **expected to change**, and Agile is **iterative**, delivering working increments and welcoming change late in development (1).
- Second characteristic (1): **frequent customer/stakeholder involvement** ensures the product matches evolving needs / **frequent small releases**, **pair programming**, or **continuous testing** improves quality.
- Justified link back to the requirement of changing needs (1).
*(Accept a justified Waterfall answer only if it engages with — and overcomes — the "changing requirements" point; otherwise no credit for choosing Waterfall here.)*

**Q9 — [3]** — *1.2.4*
(a) Encapsulation **bundles data (attributes) and the methods that act on them within an object** (1) and **restricts direct access to the data (private attributes accessed via methods)** — information hiding (1). *(AO1)*
(b) Inheritance lets a subclass **reuse code from a superclass** (1) — less duplication / easier maintenance / models an "is-a" relationship. *(AO2)*

**Q10 — [5] (AO3)** — *synoptic 1.1 + 1.2*
Mark holistically; up to 5 from a reasoned evaluation covering **both** decisions:
- **Processor:** recommend **RISC** (1) — simpler, fixed-length instructions, lower power and predictable execution suit long reliable shifts / embedded-style tills, with complexity handled in software; *(or a justified CISC choice citing fewer instructions per task)* (1 for justification).
- **Operating system:** recommend a **multi-tasking** OS (1) so staff can run **card payments and stock look-ups concurrently** via time-slicing; a **real-time** OS could be argued for guaranteed response, distributed rejected as a single till (1 for justified link).
- **Evaluation/trade-off** that weighs the choices against reliability, fast recovery and concurrency (1).
*Indicative full-mark answer: RISC for low-power predictable operation + multi-tasking OS for concurrent transactions, with a trade-off noting RTOS could guarantee responsiveness but adds complexity.*
