# Mock Paper 1C — Year 12 Mock (Week 27, UNSEEN)

Time allowed: 1 hour 30 minutes · Total: 70 marks · Answer all questions.

*TEACHER ONLY until sat. This paper is unseen: do not release it, set it as homework, or file it in the student-facing library before Mock Week (Week 27). It covers exactly what Year 12 has taught by then: 1.1–1.4 complete, all of 2.1, and 2.2.1.*

Instructions: Show all working on calculations and logic questions. Aim for about 1 minute per mark and leave time to check.

AO key: **AO1** = knowledge & understanding · **AO2** = application · **AO3** = analysis/evaluation/design.

---

## Questions

### Question 1 — Processors *(7 marks)*

**1(a)** State the role of the **program counter (PC)** and the **memory address register (MAR)** during the fetch stage of the fetch–decode–execute cycle. **[2]** *(AO1)*

**1(b)** Explain **one** way that increasing the amount of **cache** can improve the performance of a processor. **[2]** *(AO1)*

**1(c)** A drone's flight controller uses a battery-powered processor with a **RISC** instruction set and a **Harvard** architecture. Explain why this combination is suitable for the drone. **[3]** *(AO2)*

*(Running total: 7)*

---

### Question 2 — Storage *(4 marks)*

**2(a)** A hospital must keep copies of old patient scans for 30 years. The scans are very large and are almost never accessed. State the **most appropriate** storage technology and justify your choice. **[2]** *(AO2)*

**2(b)** State what is meant by **virtual storage** and give **one** drawback of relying on it. **[2]** *(AO1)*

*(Running total: 11)*

---

### Question 3 — Systems software and translators *(6 marks)*

**3(a)** An operating system uses **round robin** scheduling. Describe how round robin scheduling works and state **one** advantage it has over first come first served. **[3]** *(AO1/AO2)*

**3(b)** State the **four stages of compilation** in the order they are carried out. **[2]** *(AO1)*

**3(c)** State **one** reason a developer might choose to write part of a program in **assembly language** rather than a high-level language. **[1]** *(AO1)*

*(Running total: 17)*

---

### Question 4 — Software development methodologies *(6 marks)*

A two-person independent studio is building a mobile puzzle game. The requirements will keep changing in response to player feedback, the budget is small, and the studio wants a playable version released early and updated often.

**4** Recommend a software development methodology for the studio. Justify your recommendation with reference to the scenario, and evaluate it against **at least one** alternative methodology. **[6]** *(AO3)*

*(Running total: 23)*

---

### Question 5 — Databases *(6 marks)*

A dental surgery stores data in the following tables:

```
Patient(PatientID, Surname, DateOfBirth)
Appointment(AppointmentID, PatientID, ApptDate, RoomNumber)
```

**5(a)** Identify the **primary key** and the **foreign key** of the `Appointment` table. **[2]** *(AO2)*

**5(b)** Write an SQL statement to display the `Surname` and `DateOfBirth` of every patient born after 1 January 2005, sorted into alphabetical order of surname. **[3]** *(AO3)*

**5(c)** State what is meant by **referential integrity**. **[1]** *(AO1)*

*(Running total: 29)*

---

### Question 6 — Networks and web technologies *(6 marks)*

**6(a)** When data is sent across the internet it is split into **packets**. State **two** items of information carried in a packet's header. **[2]** *(AO1)*

**6(b)** Describe the role of the **DNS** when a user types a URL into a browser. **[2]** *(AO1)*

**6(c)** A booking form is validated by **JavaScript in the browser** before it is submitted. Explain why the server must **repeat** this validation even though the client has already performed it. **[2]** *(AO2)*

*(Running total: 35)*

---

### Question 7 (starred) — Compression, encryption and hashing *(9 marks)*

*The quality of your extended response will be assessed in this question.*

*PhotoVault* is a new cloud photo-sharing service. Users upload photos from their phones over the internet, view them in a web gallery, and can pay for a "vault" that guarantees their original photos are preserved exactly. Users log in with a username and password.

**7** Discuss how PhotoVault should use **compression**, **encryption** and **hashing** in its service. In your answer you should consider the choice between lossy and lossless compression, the protection of data both in transit and at rest, and the safe storage of passwords. Reach justified recommendations. **[9]** *(AO3)*

*(Running total: 44)*

---

### Question 8 — Data types and representation *(6 marks)*

**8(a)** Convert **−90** to 8-bit two's complement binary. Show your working. **[2]** *(AO2)*

**8(b)** Convert the denary number **172** to hexadecimal. **[1]** *(AO2)*

**8(c)** A floating point number is stored with a 6-bit two's complement **mantissa** of `010110` and a 4-bit two's complement **exponent** of `0011`. Calculate its denary value. Show your working. **[2]** *(AO2)*

**8(d)** State **one** advantage of **Unicode** over ASCII. **[1]** *(AO1)*

*(Running total: 50)*

---

### Question 9 — Data structures and Boolean algebra *(7 marks)*

**9(a)** The following operations are carried out on an empty **stack**: `push(4)`, `push(7)`, `pop()`, `push(2)`, `push(5)`, `pop()`. State the value returned by **each** `pop()`, and the contents of the stack at the end, identifying the top item. **[2]** *(AO2)*

**9(b)** State why a **queue** is an appropriate data structure for managing jobs sent to a shared printer. **[1]** *(AO2)*

**9(c)** Complete the truth table for the expression `Q = (A OR B) AND NOT(A AND B)`. **[2]** *(AO2)*

| A | B | A OR B | A AND B | Q |
|---|---|--------|---------|---|
| 0 | 0 |        |         |   |
| 0 | 1 |        |         |   |
| 1 | 0 |        |         |   |
| 1 | 1 |        |         |   |

@@SPACE:0@@

**9(d)** Simplify the Boolean expression `A OR (A AND B)`, naming the law you have used. **[2]** *(AO2)*

*(Running total: 57)*

---

### Question 10 — Computational thinking *(6 marks)*

A supermarket's self-checkout terminals currently look up every scanned product's price from a central database, and each step of a sale (scanning, card payment, receipt printing) runs one after another. At busy times the terminals are slow. The developers propose (i) **caching** the day's price list on each terminal and (ii) running the steps of a sale **concurrently** where possible.

**10** Discuss the benefits and drawbacks of the two proposals, and reach a justified conclusion about whether the developers should adopt them. **[6]** *(AO3)*

*(Running total: 63)*

---

### Question 11 — Programming techniques *(7 marks)*

**11(a)** Write a function `countVowels(word)` in **pseudocode** that takes a string parameter `word` and returns the number of vowels (a, e, i, o, u) it contains. Your function must work for both upper-case and lower-case letters. **[4]** *(AO3)*

**11(b)** State the difference between a **function** and a **procedure**. **[1]** *(AO1)*

**11(c)** Explain the difference between passing a parameter **by value** and **by reference**. **[2]** *(AO1)*

*(Running total: 70)*

---

## Mark scheme

**Question 1 — 7 marks**

**1(a) [2]** 1 mark each:
- PC: holds the **address of the next instruction** to be fetched (and is incremented during the fetch stage).
- MAR: holds the **address** of the location in memory to be accessed — the PC's contents are copied into it so the instruction can be fetched.

**1(b) [2]** More instructions/data that are frequently or recently used can be held **close to the CPU in very fast memory** (1); so fewer slow accesses to main memory (RAM) are needed / the CPU stalls less waiting for data, increasing throughput (1).

**1(c) [3]** Any three applied points, 1 mark each:
- RISC has a small, simple instruction set where each instruction completes quickly (in roughly one cycle), so the hardware is simpler.
- Simpler hardware means **lower power consumption / less heat**, which suits a battery-powered drone.
- Harvard architecture stores instructions and data in **separate memories with separate buses**, so an instruction and data can be fetched simultaneously — fast, predictable timing for real-time flight control.
- The control program is fixed, so keeping it in its own (read-only) instruction memory suits an embedded device.

**Question 2 — 4 marks**

**2(a) [2]** Magnetic tape (allow magnetic hard disk) (1); justified: lowest cost per gigabyte for very large volumes, reliable for long-term archival, and slow (serial) access is acceptable because the scans are almost never read (1). The justification must match the technology chosen.

**2(b) [2]** Virtual storage: storage accessed **remotely over a network/the internet** (e.g. cloud storage) that appears to the user as local storage, with the physical media held elsewhere (1). Drawback (1): needs an internet connection / slower access; dependent on the provider's security and continued existence; ongoing cost; data protection concerns over where data is held.

**Question 3 — 6 marks**

**3(a) [3]** Each process/job is given a fixed **time slice (quantum)** of CPU time (1); when its slice ends it moves to the back of the queue and the next process runs, cycling round all processes (1). Advantage over FCFS (1): every process gets a regular share, so a long job cannot make short jobs wait indefinitely / more responsive for interactive users.

**3(b) [2]** Lexical analysis → syntax analysis → code generation → optimisation. 2 marks for all four in the correct order; 1 mark for all four stages named but misordered, or three in the correct relative order.

**3(c) [1]** Any one: complete control over the hardware / can access specific registers or memory addresses; code can be made faster or smaller for a specific processor; needed for device drivers / embedded systems where no compiler or OS support exists.

**Question 4 — 6 marks (levels of response)**

Indicative content:
- Recommendation: an **agile** methodology (accept extreme programming or RAD) — iterative development in short cycles, releasing a working (playable) version early and often.
- Fit to scenario: requirements will change with player feedback — agile welcomes changing requirements between iterations, whereas fixing them up front would waste the small budget; frequent releases match the studio's goal; a two-person team suits agile's light documentation and close collaboration (XP's pair programming literally fits two people).
- Evaluation against an alternative: **waterfall** gives clear stages and full documentation, useful when requirements are stable and the product safety-critical — but here requirements are volatile, and waterfall would deliver nothing playable until late, so feedback would come too late to act on cheaply. RAD's reliance on prototyping and user feedback also fits, though prototype code quality can suffer.
- Drawback of the recommendation acknowledged: agile is harder to cost/schedule precisely; scope can drift; light documentation could hurt if the team grows.
- A justified conclusion recommending one methodology for **this** studio.

**Levels of response:**

**Level 3 (5–6 marks):** A clear recommendation, thoroughly justified by specific features of the scenario (changing requirements, small team/budget, early frequent releases), with a genuine evaluation against at least one alternative and a justified conclusion. Accurate terminology throughout.

**Level 2 (3–4 marks):** A recommendation with some justification linked to the scenario; an alternative is mentioned but the comparison is limited or one-sided. Some accurate terminology.

**Level 1 (1–2 marks):** Generic description of one or more methodologies with little application to the scenario; recommendation missing or unjustified.

**0 marks:** No creditable response.

**Question 5 — 6 marks**

**5(a) [2]** Primary key: `AppointmentID` (1). Foreign key: `PatientID` (which links to the primary key of `Patient`) (1).

**5(b) [3]** Example answer:

```
SELECT Surname, DateOfBirth
FROM Patient
WHERE DateOfBirth > '2005-01-01'
ORDER BY Surname ASC
```

1 mark: `SELECT Surname, DateOfBirth` with `FROM Patient`. 1 mark: `WHERE` clause with a correct comparison on `DateOfBirth`. 1 mark: `ORDER BY Surname` (`ASC` optional). Accept any unambiguous date literal.

**5(c) [1]** Ensuring that links between tables remain consistent — a foreign key value must refer to an existing record (e.g. no `Appointment` can exist for a `PatientID` that is not in `Patient`), preventing orphaned records.

**Question 6 — 6 marks**

**6(a) [2]** Any two, 1 mark each: source (IP) address; destination (IP) address; packet sequence number; checksum / error-detection value; time to live / hop limit; protocol / port number.

**6(b) [2]** The Domain Name System translates the human-readable **domain name into an IP address** (1); the browser queries a DNS resolver, which searches the hierarchy of name servers (asking higher-level/authoritative servers as needed) and returns the IP address so the browser can request the page from that server (1).

**6(c) [2]** Client-side code can be **bypassed, disabled or modified** by the user (JavaScript can be turned off or the request forged), so invalid or malicious data could still reach the server (1); the server-side check is the only one the organisation fully controls, protecting the database from bad data and attacks (e.g. SQL injection) (1).

**Question 7 (starred) — 9 marks (levels of response)**

Indicative content:

*Compression:*
- Lossy compression (e.g. JPEG) removes detail permanently — hugely reduces upload time and storage cost for gallery/preview images where slight quality loss is invisible.
- Lossless compression (e.g. run-length encoding / dictionary-based methods, PNG-style) allows the original to be perfectly reconstructed — essential for the paid "vault", which guarantees exact preservation, even though files stay larger.
- Recommendation: lossy for streamed gallery/thumbnails, lossless for vault originals.

*Encryption:*
- In transit: photos and login details travel over the internet, so use encryption (e.g. TLS/HTTPS) — asymmetric encryption to exchange keys securely, then faster symmetric encryption for the bulk photo data.
- At rest: encrypt stored photos on the servers so a stolen disk or breached server does not expose users' private images; key management becomes the critical issue.

*Hashing:*
- Passwords must **never** be stored in plain text or merely encrypted; store a **hash** of each password (with a salt) — hashing is one-way, so the password cannot be recovered from the stored value.
- At login, hash the entered password and compare with the stored hash.
- Hashing could also detect duplicate/corrupted uploads (same hash = same file) — a legitimate extension point.

*Conclusion:* justified recommendations, e.g. lossy compression by default with lossless for the vault, TLS for all transfers plus encryption at rest, and salted hashes for credentials — each choice tied to the service's needs.

**Levels of response:**

**Level 3 (7–9 marks):** Addresses all three techniques with clear, accurate application to PhotoVault (lossy vs lossless tied to gallery vs vault; in transit and at rest; salted one-way password hashing). Weighs alternatives and reaches justified recommendations. Coherent, well-structured response using accurate terminology.

**Level 2 (4–6 marks):** Addresses at least two techniques with some application to the scenario; explanations mostly accurate but with limited depth or balance; recommendations present but only partially justified.

**Level 1 (1–3 marks):** Identifies relevant techniques with generic or partially accurate descriptions; little application to the scenario; no real justification.

**0 marks:** No creditable response.

**Question 8 — 6 marks**

**8(a) [2]** +90 = `01011010` (1); flip the bits and add 1: `10100101` + 1 = **`10100110`** (1). (Also accept the method of setting −128 bit: −128 + 32 + 4 + 2 = −90.)

**8(b) [1]** AC.

**8(c) [2]** Mantissa `010110` = 0.10110₂ = 0.6875; exponent `0011` = 3, so move the binary point 3 places right: 010.110₂ (1) = **5.5** (1). Working must be shown for full marks; a correct answer alone gains 1.

**8(d) [1]** Any one: Unicode can represent a far greater range of characters (most of the world's alphabets, symbols, emoji) because it uses more bits per character; ASCII is limited to 128 (7-bit) characters — essentially unaccented English.

**Question 9 — 7 marks**

**9(a) [2]** The pops return **7** then **5** (1). Final stack contents: `4` at the bottom, **`2` on top** (1).

**9(b) [1]** A queue is first in, first out — print jobs are processed in the order they arrive, which is fair / preserves the order users sent them.

**9(c) [2]** Completed table — 1 mark for the two intermediate columns correct, 1 mark for column Q correct:

| A | B | A OR B | A AND B | Q |
|---|---|--------|---------|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 |

(Q is the exclusive OR of A and B.)

**9(d) [2]** `A OR (A AND B)` simplifies to **`A`** (1); by the **absorption** law (1).

**Question 10 — 6 marks (levels of response)**

Indicative content:
- Caching benefit: each price lookup is served from the terminal's own memory instead of a round trip to the central database — scans register faster and the system still works during short network outages; load on the central server falls (thinking ahead: reusable data identified in advance).
- Caching drawback: the cached price list can become **stale** — a mid-day price change or special offer would not appear; needs a refresh/invalidation policy, and holding the list uses local storage/memory.
- Concurrency benefit: steps that do not depend on each other (e.g. printing the receipt while the next customer starts scanning; contacting the bank while the customer bags items) can overlap, cutting the time per customer and using multi-core hardware.
- Concurrency drawback: payment must not complete before the total is known — genuine **dependencies** limit what can overlap; concurrent code is harder to write, test and debug, and shared data (e.g. the running total) risks race conditions.
- Justified conclusion, e.g. adopt both, with a scheduled cache refresh and concurrency only for the genuinely independent steps.

**Levels of response:**

**Level 3 (5–6 marks):** Both proposals discussed with benefits **and** drawbacks applied to the self-checkout (staleness, dependencies between sale steps), leading to a justified conclusion. Accurate terminology, coherent structure.

**Level 2 (3–4 marks):** Both proposals discussed but coverage is uneven or drawbacks are thin; some application to the scenario; conclusion present but weakly justified.

**Level 1 (1–2 marks):** Generic statements about caching or concurrency with little scenario link; one proposal ignored; no justified conclusion.

**0 marks:** No creditable response.

**Question 11 — 7 marks**

**11(a) [4]** Example answer:

```
function countVowels(word)
    count = 0
    for i = 0 to word.length - 1
        letter = word.substring(i, 1)
        letter = letter.lower
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" then
            count = count + 1
        endif
    next i
    return count
endfunction
```

1 mark each:
- Correct function definition that **returns** the count (`function` … `return` … `endfunction`).
- Loop that visits every character, e.g. `for i = 0 to word.length - 1`.
- Case handled (e.g. `.lower` or `.upper` applied, or both cases tested) so upper-case vowels are counted.
- Correct selection testing the character against all five vowels, with the counter initialised and incremented correctly.

Accept any working equivalent (e.g. `for letter in word`-style iteration written in OCR pseudocode conventions).

**11(b) [1]** A function **returns a value** to the code that called it; a procedure does not (it just carries out its statements). Accept: a function call can be used in an expression.

**11(c) [2]** By value: a **copy** of the data is passed, so changes inside the subroutine do not affect the original variable (1). By reference: the **address/reference** of the variable is passed, so the subroutine works on the original and changes persist after it returns (1).

---

## Verified mark total

7 + 4 + 6 + 6 + 6 + 6 + 9 + 6 + 7 + 6 + 7 = **70 marks**.

Levels-of-response questions: Question 4 **[6]**, Question 10 **[6]**, Question 7 (starred) **[9]** — 21 marks; remaining short/structured questions — 49 marks.

**Confirmed total: 70 marks.**
