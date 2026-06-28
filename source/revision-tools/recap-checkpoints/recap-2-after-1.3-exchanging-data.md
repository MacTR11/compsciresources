# Recap Checkpoint 2 — after 1.3 (Exchanging Data) — cumulative 1.1 + 1.2 + 1.3

Name: ______________________   Date: __________   Mark: ______ / 30

*OCR H446 cumulative recap — mixes every topic taught so far. Show all working.*

## Questions

**Q1.** State the function of the **MAR** and the **MDR** during the fetch phase of the FDE cycle. **[2]** *(AO1)* — *1.1.1*

**Q2.** A laptop uses **L1, L2 and L3 cache**. Explain how cache improves CPU performance, referring to **one** difference between L1 and L3 cache. **[3]** *(AO1)* — *1.1.1*

**Q3.** Explain how the operating system uses **interrupts and the interrupt service routine (ISR)** to respond to a key press while a program is running. **[3]** *(AO1)* — *1.2.1*

**Q4.** A program is distributed as **bytecode** to be run by a **virtual machine**.
(a) Explain **one** advantage of distributing bytecode rather than machine code. **[2]** *(AO2)*
(b) State **one** disadvantage. **[1]** *(AO2)*
**[3 total]** — *1.2.2*

**Q5.** Explain what is meant by **hashing**, and give **two** reasons why hashing is used to store passwords rather than storing the passwords directly. **[3]** *(AO1)* — *1.3.1*

**Q6.** A row of pixels in a monochrome image is shown below, where each letter is a pixel colour:

`RRRRRGGGGGGGRRRR`

(a) Show how **run length encoding (RLE)** would encode this row. **[2]** *(AO2)*
(b) State **one** type of image for which RLE gives **little or no compression**, and explain why. **[1]** *(AO2)*
**[3 total]** — *1.3.1*

**Q7.** A company sends confidential data over the internet to a new client it has never contacted before.
(a) State the difference between **symmetric** and **asymmetric** encryption. **[2]** *(AO1)*
(b) Explain why **asymmetric** encryption solves the problem of exchanging keys securely with a brand-new client. **[2]** *(AO2)*
**[4 total]** — *1.3.1*

**Q8.** A flat-file table storing orders is being normalised:

`Order(OrderID, CustomerID, CustomerName, CustomerEmail, ProductID, ProductName)`

Here `CustomerName` and `CustomerEmail` are determined by `CustomerID`, and `ProductName` is determined by `ProductID`.
(a) State the rule a table must satisfy to be in **first normal form (1NF)**. **[1]** *(AO1)*
(b) Explain why this table is **not** in **third normal form (3NF)** and list the tables produced after normalising to 3NF. **[3]** *(AO2)*
**[4 total]** — *1.3.2*

**Q9.** A `Booking` table has fields `BookingID`, `Surname`, `Town`, `Nights` and `Cost`.
Write an SQL statement to display the `Surname` and `Cost` of all bookings where `Town` is `'York'` **and** `Nights` is greater than `3`, sorted by `Cost` in **descending** order. **[4]** *(AO2)* — *1.3.2*

**Q10.** Data is sent across the internet using the **TCP/IP** protocol stack.
(a) Name the **four layers** of the TCP/IP stack in order from top (application) to bottom. **[2]** *(AO1)*
(b) State the layer at which the **IP address** is added, and the layer responsible for **splitting data into packets / reassembly**. **[2]** *(AO1)*
**[4 total]** — *1.3.3*

**Q11.** An online retailer's web pages load slowly and rank poorly in search results. The developers are considering moving some processing from **server-side to client-side**, and improving how pages are **indexed and ranked** by search engines. Evaluate how these two changes could help, referring to specific web technologies. **[3]** *(AO3)* — *synoptic 1.3.4 (+ 1.1/1.2 performance)*

---

## Mark scheme

*Total = 30 marks. Award marks for valid alternatives in line with OCR positive-marking.*

**Q1 — [2] (AO1)** — *1.1.1*
- MAR holds the **address** of the memory location to be read from / written to (1).
- MDR holds the **data or instruction** fetched from, or to be written to, memory (1).

**Q2 — [3] (AO1)** — *1.1.1*
- Cache is **fast memory close to / on the CPU** holding **frequently/recently used instructions and data** (1)…
- …so the CPU avoids slower fetches from main memory, reducing access time (1).
- Difference (1): **L1 is smaller but faster (and closest to the core); L3 is larger but slower** (and often shared between cores).

**Q3 — [3] (AO1)** — *1.2.1*
- The key press generates an **interrupt** / sets an interrupt flag (1).
- At the end of the current FDE cycle the CPU **saves the current state to the stack** and **runs the ISR** for the keyboard (1).
- After the ISR completes, the **saved state is restored** and the interrupted program resumes (1).

**Q4 — [3]** — *1.2.2*
(a) Bytecode is **platform-independent / portable** (1) — the same file runs on any device with the appropriate virtual machine, so it need not be recompiled per platform (1). *(AO2)*
(b) Any one (1): it **runs slower** than native machine code (translation/JIT overhead at run time); the **VM must be installed**. *(AO2)*

**Q5 — [3] (AO1)** — *1.3.1*
- Hashing applies a **one-way function** to input to produce a **fixed-length hash/digest** that cannot feasibly be reversed (1).
- Reason 1 (1): if the database is stolen, the **original passwords are not exposed** (irreversible).
- Reason 2 (1): the stored hash can still be **verified** at login by hashing the entry and comparing, without storing the plaintext.

**Q6 — [3]** — *1.3.1*
(a) **5R 7G 4R** (accept equivalent notation such as `R5 G7 R4`, or value/run pairs) (2 marks; 1 mark if one run count wrong). *(AO2)*
(b) An image with **no long runs of identical pixels** — e.g. a **photograph / highly detailed or noisy image** (1) — RLE may even **increase** size because every short run still needs a count + value. *(AO2)*
*Check: 5 + 7 + 4 = 16 pixels ✓.*

**Q7 — [4]** — *1.3.1*
(a) **Symmetric** uses **the same (single) key** to encrypt and decrypt; **asymmetric** uses a **key pair — public to encrypt, private to decrypt** (or vice versa for signing) (2; 1 per type). *(AO1)*
(b) With asymmetric encryption the recipient's **public key can be shared openly** (1), so the sender encrypts with it and only the holder of the matching **private key can decrypt** — **no secret key ever needs to be exchanged**, solving key distribution for first contact (1). *(AO2)*

**Q8 — [4]** — *1.3.2*
(a) Every field/attribute is **atomic** (single value) with **no repeating groups** (and a primary key) (1). *(AO1)*
(b) It is not in 3NF because of **transitive / non-key dependencies**: non-key fields depend on other non-key fields (`CustomerName`/`CustomerEmail` on `CustomerID`; `ProductName` on `ProductID`) (1). Resulting tables (2): *(AO2)*
- `Customer(CustomerID, CustomerName, CustomerEmail)`
- `Product(ProductID, ProductName)`
- `Order(OrderID, CustomerID*, ProductID*)`
*(Award 1 for identifying the transitive dependency, 1 for the Customer/Product split, 1 for the linking Order table with foreign keys.)*

**Q9 — [4] (AO2)** — *1.3.2*
```sql
SELECT Surname, Cost
FROM Booking
WHERE Town = 'York' AND Nights > 3
ORDER BY Cost DESC;
```
- `SELECT Surname, Cost` (1)
- `FROM Booking` (1)
- `WHERE Town = 'York' AND Nights > 3` (1)
- `ORDER BY Cost DESC` (1)

**Q10 — [4] (AO1)** — *1.3.3*
(a) **Application → Transport → Network (Internet) → Link (Data Link/Network Access)** (2; 1 mark if one pair out of order).
(b) The **IP address is added at the Network layer** (1); the **Transport layer splits data into packets and reassembles them** (TCP) (1).

**Q11 — [3] (AO3)** — *synoptic 1.3.4*
Up to 3 from a reasoned evaluation:
- Moving work **client-side (e.g. JavaScript validation/rendering)** reduces **server load and round-trips**, so pages feel faster / scale to more users (1).
- Trade-off: client-side code **runs on the user's device** and can be **disabled/bypassed**, so security-critical checks must stay server-side (1).
- Better **indexing / using meta-data, relevant content and inbound links** improves how a search engine's algorithm (e.g. **PageRank**) ranks the site, raising visibility (1).
*Indicative answer links faster pages + stronger ranking signals to more traffic, while noting client-side limits.*
