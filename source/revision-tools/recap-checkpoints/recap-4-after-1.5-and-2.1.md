# Recap Checkpoint 4 — Cumulative: 1.1–1.5 + 2.1 (Computational Thinking)

Name: ______________________   Date: __________   Mark: ______ / 30

*OCR H446 cumulative recap — mixes every topic taught so far. Show all working.*

## Questions

**Q1 [3] (AO1).** *(1.1 — Processors)* State the three phases of the **fetch–decode–execute cycle** and, for the fetch phase, name **one** register whose contents are used and **one** register that is updated.

**Q2 [4] (AO2).** *(1.4 — Data representation)* Show all working.
(a) Convert the denary number **205** to **8-bit binary**. **[1]**
(b) Convert **205** to **hexadecimal**. **[2]**
(c) State **one** reason programmers prefer hexadecimal to binary when reading memory dumps. **[1]**

**Q3 [4] (AO2).** *(1.4 — Two's complement)* Using **8-bit two's complement**, calculate **38 − 53**.
(a) Show 38 and 53 in 8-bit binary. **[1]**
(b) Form the two's complement of 53. **[1]**
(c) Perform the addition and state the final **denary** result. **[2]**

**Q4 [3] (AO1/AO2).** *(1.2 — Software development)* A team is building software where requirements are expected to change frequently and the customer wants working software early.
(a) Name a suitable **development methodology**. **[1]**
(b) Give **two** reasons it suits this situation. **[2]**

**Q5 [4] (AO1).** *(1.3 — Exchanging data / networks)* A file is sent across the Internet using the **TCP/IP stack**.
(a) Name the **four layers** of the TCP/IP stack in order from top to bottom. **[2]**
(b) State the layer at which **packets are routed** between networks and name the layer that **adds port numbers**. **[2]**

**Q6 [3] (AO3).** *(1.5 — Legal/ethical)* A company plans to use AI to monitor employees' keystrokes to measure productivity.
Discuss **one legal** and **one ethical** issue this raises. **[3]**

**Q7 [4] (AO2).** *(2.1 — Computational thinking)* A weather app requests live temperature data for thousands of users every few seconds.
(a) Explain how **caching** the data on the server improves performance. **[2]**
(b) State **one** trade-off of caching in this scenario. **[1]**
(c) State what is meant by *abstraction* in the context of modelling the weather. **[1]**

**Q8 [5] (AO3).** *(2.1 synoptic, extended response)* A car-park company is building software to control entry/exit barriers, track free spaces and serve a mobile app showing live availability.
Explain how **decomposition** and **abstraction** would help the developers manage this problem, and identify **one** part of the system best suited to a **concurrent** (parallel) approach. **[5]**

---

## Mark scheme

**Q1 [3] (AO1).**
- Fetch (1); Decode (1); Execute (1) — must be in this order.
- Fetch phase: register **used** = **PC (Program Counter)** or **MAR**; register **updated** = **MAR/MDR/CIR**, or the **PC is incremented** (accept any valid pairing as the named registers within the 3 marks — award the phase marks; named registers are credited within the description).

*Examiner tip: PC holds the address of the next instruction; it is copied to the MAR, then incremented. The fetched instruction lands in the MDR and is copied to the CIR.*

---

**Q2 [4] (AO2).**
- (a) 205 = `1100 1101` (1). *(128+64+8+4+1 = 205)*
- (b) 205 ÷ 16 = 12 remainder 13 → high nibble 12 = C, low nibble 13 = D → **CD** (1 for method, 1 for answer).
- (c) Hex is **more compact / easier to read / less error-prone** — each hex digit maps to exactly 4 bits (1).

*Examiner tip: cross-check (b) against (a): `1100` = C, `1101` = D → CD. The two answers must agree.*

---

**Q3 [4] (AO2).** 38 − 53 in 8-bit two's complement:
- (a) 38 = `0010 0110`, 53 = `0011 0101` (1 for both correct).
- (b) Two's complement of 53: invert `0011 0101` → `1100 1010`, add 1 → **`1100 1011`** (1).
- (c) `0010 0110` + `1100 1011` = `1111 0001` (1). `1111 0001` is negative; magnitude = invert+1 = `0000 1111` = 15, so result = **−15** (1).

*Examiner tip: 38 − 53 = −15. The result `1111 0001` has a leading 1, confirming it is negative — decode it back to check.*

---

**Q4 [3] (AO1/AO2).**
- (a) **Agile** (accept extreme programming / iterative / rapid application development) (1).
- (b) Any two (1 each): delivers **working software early/in iterations**; **adapts easily to changing requirements**; **frequent customer feedback**; less wasted effort on full up-front documentation.

*Examiner tip: the cue words "requirements change frequently" and "working software early" point straight at Agile over the Waterfall model.*

---

**Q5 [4] (AO1).**
- (a) **Application, Transport, Network (Internet), Link (Data Link / Network Access)** — top to bottom (2 marks: 2 for all four correct/ordered, 1 for two/three correct).
- (b) Routing happens at the **Network/Internet layer** (1); port numbers are added at the **Transport layer** (1).

*Examiner tip: Transport = TCP/UDP and ports; Network = IP addressing and routing. Don't confuse the two.*

---

**Q6 [3] (AO3).**
- Legal issue (1–2): must comply with **data protection legislation (e.g. GDPR/Data Protection Act)** — keystroke data is personal data, needs a lawful basis and must be processed fairly; collecting it secretly could be unlawful.
- Ethical issue (1–2): raises concerns about **employee privacy / surveillance / trust / consent and proportionality** — monitoring may be intrusive and damage morale even if technically lawful.
- Up to 3 marks total: at least one valid legal point and one valid ethical point, with reasoning.

*Examiner tip: keep legal (the law) and ethical (right/wrong, fairness) distinct — examiners look for both strands.*

---

**Q7 [4] (AO2).**
- (a) Caching stores a **recently computed/fetched copy** of the data so repeated identical requests are served **from the cache rather than recomputing/re-querying** (1), reducing server load and **response latency** (1).
- (b) Trade-off (1): the cached data can be **stale/out of date** between refreshes, so users may see slightly old temperatures; or it uses extra memory.
- (c) Abstraction = **removing/hiding unnecessary detail** to focus on the essential features needed for the model (1).

*Examiner tip: a cache speeds up reads but introduces a freshness trade-off — both halves are needed for full marks.*

---

**Q8 [5] (AO3).** Indicative content (up to 5; reward a reasoned, applied response):
- **Decomposition**: break the system into independent sub-problems — barrier control, space counting, charge calculation, app/availability service — so each can be designed, built and tested separately (1–2).
- **Abstraction**: model only the essentials (e.g. represent a bay as free/occupied, ignore vehicle colour/make) so the software stays manageable (1–2).
- **Concurrency**: serving many simultaneous app requests for live availability is well suited to **parallel/concurrent processing** (handling requests on separate threads), since they are largely independent (1).
- Marks for clear, applied reasoning tied to the scenario rather than generic definitions.

*Examiner tip: name the part suited to concurrency explicitly (the app/availability requests), not just "the whole system".*

---

**Total: 30 marks.**
