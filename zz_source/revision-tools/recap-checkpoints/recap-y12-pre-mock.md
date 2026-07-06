# Year 12 Pre-Mock Recap — cumulative 1.1–1.4 + 2.1 + 2.2.1

Name: ______________________   Date: __________   Mark: ______ / 60

**Time allowed: 75 minutes. Closed book.**

*OCR H446 cumulative pre-mock recap. Section A covers Component 1 (36 marks); Section B covers Component 2 (24 marks). Show all working.*

## Questions

### Section A — Component 1 (36 marks)

**Q1.** Describe the role of the **address bus**, the **data bus** and the **control bus** when the CPU fetches an instruction from main memory. **[3]** *(AO1)* — *1.1.1*

**Q2.** A desktop computer contains both **RAM** and **ROM**.
(a) State **two** differences between RAM and ROM. **[2]** *(AO1)*
(b) Give **one** reason the computer needs ROM. **[1]** *(AO1)*
**[3 total]** — *1.1.3*

**Q3.** An operating system is managing three processes.
(a) Describe how **round robin** scheduling shares the processor between the processes. **[2]** *(AO1)*
(b) Explain how a long job could be treated unfairly under **shortest job first** scheduling. **[1]** *(AO2)*
(c) State the name of the memory-management technique that divides memory into **fixed-size** blocks. **[1]** *(AO1)*
**[4 total]** — *1.2.1*

**Q4.** A developer writing firmware for a microcontroller programs in **assembly language**.
(a) State the name of the translator that converts assembly language into machine code. **[1]** *(AO1)*
(b) Give **one** reason assembly language is appropriate for this task. **[1]** *(AO2)*
(c) Within a machine-code instruction, state what is meant by the **opcode** and the **operand**. **[1]** *(AO1)*
**[3 total]** — *1.2.4*

**Q5.** A student types `www.revisionhub.co.uk` into a web browser.
(a) Describe how **DNS** is used to obtain the IP address of the web server, including what happens when the local resolver does **not** already know the address. **[3]** *(AO1)*
(b) State what is meant by a **protocol**, and give **one** reason standard protocols are essential on the internet. **[2]** *(AO1)*
**[5 total]** — *1.3.3*

**Q6.** Show all working.
(a) Convert the denary number **154** into 8-bit binary. **[1]** *(AO2)*
(b) Convert **154** into hexadecimal. **[1]** *(AO2)*
(c) Using **8-bit two's complement**, calculate **47 − 61**: show 47 and 61 in 8-bit binary, form the two's complement of 61, then perform the addition and state the final **denary** result. **[3]** *(AO2)*
**[5 total]** — *1.4.1*

**Q7.** Show each step.
(a) Use **De Morgan's law** to rewrite **¬(B ∨ ¬C)** so that NOT is no longer applied to a bracket. **[2]** *(AO2)*
(b) Simplify **A∧B ∨ A∧B∧C**, naming the law used. **[2]** *(AO2)*
**[4 total]** — *1.4.3*

**Q8.** A sorted collection of values is stored in a **linked list**: `14 → 26 → 33`.
(a) Describe how a linked list stores its items, referring to **nodes** and **pointers**. **[2]** *(AO1)*
(b) Describe the steps needed to insert the value **29** into its correct position, and state why no existing data has to be moved. **[2]** *(AO2)*
**[4 total]** — *1.4.2*

**Q9.** A music festival issues electronic wristbands. Battery-powered scanners at each gate currently check every wristband against a **central database** over the site's Wi-Fi; the organisers are considering instead giving each scanner its **own local copy** of the ticket data. Evaluate the two approaches, referring to **data consistency**, **reliability of the network link**, and the **security of transmitted data**. **[5]** *(AO3)* — *synoptic 1.3.1 / 1.3.2 / 1.3.3*

### Section B — Component 2 (24 marks)

**Q10.** A city introduces a bike-hire scheme: riders unlock a bike at a docking station using an app, ride it, and return it to any station. The app shows a map of stations with the number of bikes available at each.
(a) Identify **one** example of **abstraction** in the app's map. **[1]** *(AO2)*
(b) The developers **decompose** the overall problem. Identify **two** sub-problems of "hire a bike". **[2]** *(AO2)*
(c) Identify **one** part of the system that is well suited to **concurrent** processing. **[1]** *(AO2)*
**[4 total]** — *2.1.1 / 2.1.3 / 2.1.5*

**Q11.** A toll-bridge barrier rises only when payment has been accepted **and** the vehicle's height, held in the variable `height`, does not exceed **2.4** metres. The Boolean variable `paymentOK` is available.
(a) *Thinking logically:* write the **Boolean condition** the program should test before raising the barrier. **[2]** *(AO2)*
(b) *Thinking ahead:* the toll charge looked up for each regular number plate could be **cached** after its first lookup. State **one benefit** and **one risk** of this caching. **[2]** *(AO2)*
**[4 total]** — *2.1.4 / 2.1.2*

**Q12.** The following program is written in OCR Exam Reference Language.

```
n = 305
rev = 0
while n > 0
    rev = rev * 10 + (n MOD 10)
    n = n DIV 10
endwhile
print(rev)
```

(a) Complete the trace table, showing the values of `n` and `rev` at the **end of each iteration** of the loop. **[3]** *(AO3)*

| Iteration | n | rev |
|---|---|---|
| start | 305 | 0 |
| 1 |   |   |
| 2 |   |   |
| 3 |   |   |

@@SPACE:0@@

(b) State the value output by the program. **[1]** *(AO3)*
(c) State the purpose of the program. **[1]** *(AO2)*
**[5 total]** — *2.2.1*

**Q13.** A swimming coach records a swimmer's lap times, in seconds (real numbers), in the array `laps`. Write a function `countFaster(laps, target)` in **OCR Exam Reference Language** that:
- returns **−1** if `laps` is empty;
- otherwise returns the **number of laps** swum in **strictly less than** `target` seconds.
Use `laps.length` to find the number of items in the array. **[6]** *(AO3)* — *2.2.1*

**Q14.** A programmer is improving a menu-driven program.
(a) State **two** features of an **IDE** that help the programmer find the cause of a logic error, describing how each helps. **[2]** *(AO1)*
(b) Give **one** reason for using a **named constant** rather than repeating a literal value through the code. **[1]** *(AO1)*
(c) The menu must be displayed **at least once**, and redisplayed until the user enters a valid choice. Name the most suitable **iteration structure** in OCR Exam Reference Language and justify your choice over `while ... endwhile`. **[2]** *(AO2)*
**[5 total]** — *2.2.1*

---

## Mark scheme

*Total = 60 marks (Section A = 36, Section B = 24). Award marks for valid alternatives in line with OCR positive-marking. All calculations and code checked below.*

**Q1 — [3] (AO1)** — *1.1.1*
- The **address bus** carries the **address** of the memory location to be fetched (sent from the MAR); it is one-directional, CPU → memory (1).
- The **data bus** carries the **instruction/data** itself back from memory to the CPU (into the MDR); it is bi-directional (1).
- The **control bus** carries **control signals** (e.g. memory read, clock) that coordinate/time the transfer (1).

**Q2 — [3] (AO1)** — *1.1.3*
(a) Any two (1 each): RAM is **volatile**, ROM is **non-volatile**; RAM is **read/write**, ROM is **read-only** (contents fixed/written at manufacture); RAM holds the **programs and data currently in use**, ROM holds **fixed startup instructions**.
(b) ROM holds the **bootstrap loader / BIOS / firmware** needed to start the computer before anything is loaded into RAM (1).

**Q3 — [4]** — *1.2.1*
(a) Each process is given a fixed **time slice (quantum)** of processor time in turn (1); when its slice expires it is moved to the **back of the queue** and the next process runs, cycling round until processes complete (1). *(AO1)*
(b) Shortest job first always selects the **shortest** waiting job, so a long job can be repeatedly leapfrogged by newly arriving shorter jobs and may wait indefinitely (**starvation**) (1). *(AO2)*
(c) **Paging** (fixed-size blocks/pages; segmentation uses variable-size logical blocks) (1). *(AO1)*

**Q4 — [3]** — *1.2.4*
(a) An **assembler** (1). *(AO1)*
(b) Any one (1): direct **control of the hardware/registers**; produces **fast / memory-efficient** code suited to the microcontroller's limited resources; no OS/translator available on the device. *(AO2)*
(c) The **opcode** is the operation to be carried out; the **operand** is the value/address it operates on (both needed for the mark) (1). *(AO1)*

**Q5 — [5] (AO1)** — *1.3.3*
(a) Up to 3:
- The browser asks the **local/ISP DNS resolver** for the IP address matching the domain name (1).
- If the resolver does not hold it (not in its **cache**), it queries the **DNS hierarchy** — root server, then `.uk`/`.co.uk` TLD server, then the **authoritative** name server for the domain (1).
- The IP address is **returned to the browser and cached** for future requests; the browser then contacts the web server using that IP address (1).
(b) A protocol is an **agreed set of rules** for transmitting/formatting data between devices (1). Standard protocols mean devices from **different manufacturers/networks can interoperate** (1).

**Q6 — [5] (AO2)** — *1.4.1*
(a) 154 = 128 + 16 + 8 + 2 → **`1001 1010`** (1).
(b) Nibbles `1001` = 9, `1010` = A → **9A** (1). *Check: 9 × 16 + 10 = 144 + 10 = 154 ✓.*
(c) 47 = `0010 1111`, 61 = `0011 1101` (1). −61: invert `0011 1101` → `1100 0010`, add 1 → **`1100 0011`** (1). Add `0010 1111 + 1100 0011` = `1111 0010`; MSB = 1 → negative; magnitude = invert + 1 = `0000 1101 + 1` = `0000 1110` = 14, so the answer is **−14** (1).
*Check: 47 − 61 = −14 ✓.*

**Q7 — [4] (AO2)** — *1.4.3*
(a) De Morgan: break the bar and swap OR → AND: ¬(B ∨ ¬C) = ¬B ∧ ¬(¬C) (1); double negation gives **¬B ∧ C** (1). *(Truth-table check: B=0, C=1 gives LHS ¬(0∨0)=1, RHS 1∧1=1 ✓.)*
(b) A∧B ∨ A∧B∧C = **A∧B** (1); **absorption** law (X ∨ X∧Y = X, with X = A∧B) — also accept distributive + identity: A∧B∧(1 ∨ C) = A∧B∧1 = A∧B (1).

**Q8 — [4]** — *1.4.2*
(a) Each **node** stores the **data item plus a pointer to the next node** (1); nodes need not be contiguous in memory — the list starts at a **head pointer** and the final node's pointer is **null** (1). *(AO1)*
(b) Create a new node holding 29; set the **pointer of node 26 to the new node** and the **new node's pointer to node 33** (1). Only pointers change — the existing nodes stay where they are, so nothing is shuffled along as it would be in an array (1). *(AO2)*

**Q9 — [5] (AO3)** — *synoptic 1.3.1 / 1.3.2 / 1.3.3*
Mark holistically; up to 5 from a reasoned evaluation covering all three strands:
- **Consistency:** a central database holds a **single, consistent copy** — a wristband already scanned in (or cancelled) at one gate is immediately rejected at every other gate (1); with local copies the data can become **stale/inconsistent** between syncs, so a cloned/cancelled wristband might be accepted twice (1).
- **Reliability:** the central approach depends entirely on the **Wi-Fi link** — congestion or failure on a crowded festival site stops all scanning (single point of failure) (1); local copies keep gates working **offline** with fast lookups (1).
- **Security:** wristband checks/updates crossing Wi-Fi can be **intercepted**, so transmitted data must be **encrypted**; a local copy on each handheld device instead risks exposing the whole ticket list if a scanner is lost/stolen (1).
- Reasoned judgement, e.g. a **hybrid** — cache ticket data locally, sync updates whenever the link is available (1).
*(Max 5.)*

**Q10 — [4] (AO2)** — *2.1.1 / 2.1.3 / 2.1.5*
(a) The map **hides unnecessary detail** — it shows only station locations and bike counts, not streets' full detail, individual bikes' colours/serial numbers, etc. (1).
(b) Any two (1 each): authenticate the user / app login; locate and display nearby stations; unlock the chosen bike; time the ride and calculate the charge; take payment; detect the bike being re-docked; update availability counts.
(c) Handling **many users' app requests (availability lookups / unlock requests) at the same time** — the requests are largely independent, so they can be processed concurrently (1).

**Q11 — [4] (AO2)** — *2.1.4 / 2.1.2*
(a) Condition combines **both** requirements with AND (1): **`paymentOK == true AND height <= 2.4`** (accept `paymentOK AND NOT (height > 2.4)`) — correct comparisons on both variables (1).
(b) Benefit (1): a regular vehicle's toll is looked up **once** and then served from the cache — faster processing at the barrier / less load on the database. Risk (1): the cached charge can become **stale** — if the tariff (or the vehicle's classification) changes, the old cached value is applied until the cache is refreshed.

**Q12 — [5]** — *2.2.1*
(a) Completed trace (1 mark per correct row; allow follow-through): *(AO3)*

| Iteration | n | rev |
|---|---|---|
| start | 305 | 0 |
| 1 | 30 | 5 |
| 2 | 3 | 50 |
| 3 | 0 | 503 |

*Working: 305 MOD 10 = 5, 305 DIV 10 = 30; 30 MOD 10 = 0 → rev = 50, 30 DIV 10 = 3; 3 MOD 10 = 3 → rev = 503, 3 DIV 10 = 0 → loop ends.*
(b) Output: **503** (1). *(AO3)*
(c) The program **reverses the digits** of the number held in `n` (1). *(AO2)*

**Q13 — [6] (AO3)** — *2.2.1*
Model answer (verified):

```
function countFaster(laps, target)
    if laps.length == 0 then
        return -1
    endif
    count = 0
    for i = 0 to laps.length - 1
        if laps[i] < target then
            count = count + 1
        endif
    next i
    return count
endfunction
```

Award 1 mark each:
- `function` header with **two parameters** and matching `endfunction` (1).
- Empty-array check using `laps.length == 0` that **returns −1** (1).
- Counter **initialised to 0** before the loop (1).
- Loop visiting **every index**, e.g. `for i = 0 to laps.length - 1 ... next i` (or an equivalent `while`) (1).
- Correct comparison — **strictly less than**: `if laps[i] < target then` count incremented (1).
- `return count` **after the loop** (1).
*(Accept any language/dialect with correct logic; reject `<=` for the comparison mark. Check: for laps = 31.2, 29.8, 33.0, 28.4, 30.0 and target = 30.0 the function returns 2 ✓; for an empty array it returns −1 ✓.)*

**Q14 — [5]** — *2.2.1*
(a) Any two IDE features, each with how it helps (1 each): **breakpoints** — pause execution at a chosen line to inspect the program's state; **single-stepping** — execute one line at a time to follow the flow; **variable watch/inspection window** — see values change to spot where they become wrong; **error/stack trace or debugging output** — locate where execution diverges. *(AO1)*
(b) Any one (1): a change is made **in one place** and applies everywhere; prevents accidental modification; makes code more **readable/maintainable**. *(AO1)*
(c) **`do ... until`** (post-condition loop) (1) — the condition is tested **at the end**, so the body always runs **at least once** (the menu is always shown), whereas `while ... endwhile` tests first and could skip the menu entirely (1). *(AO2)*
