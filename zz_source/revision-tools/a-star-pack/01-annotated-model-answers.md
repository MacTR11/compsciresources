# Annotated Model Answers — How A\*/A Answers Are Built

This resource shows **full-mark exemplar answers** for OCR A Level Computer Science (H446), each dissected so you can see *exactly* where every mark is earned. The point is not to memorise these answers — it is to copy the **technique**: how the top band links knowledge to the scenario (AO2), shows working, weighs trade-offs and reaches a justified conclusion (AO3).

> **The grade is decided in AO2/AO3.** Almost everyone picks up the AO1 recall marks. The A/A\* boundary lives in *applying* ideas to the specific scenario, *showing every step* of a calculation, and *committing to a defended judgement*. Watch for those moves flagged in each "Why this scores" section.

Questions span **Component 01 (Computer Systems)** and **Component 02 (Algorithms & Programming)**.

---

## Question 1 — Two's complement & floating-point (1.4.1) · 7 marks · AO1/AO2

> A computer represents real numbers using **8-bit two's complement** for the mantissa and a **4-bit two's complement** exponent. The mantissa has the binary point after the first (sign) bit.
>
> **(a)** Convert the denary value **−20** into 8-bit two's complement. **[2]**
> **(b)** A floating-point number is stored as mantissa `0.1010000` and exponent `0011`. Calculate the denary value it represents. Show your working. **[3]**
> **(c)** State **one** advantage and **one** disadvantage of increasing the number of bits in the mantissa while keeping the total number of bits fixed. **[2]**

### Model answer

**(a)** +20 in binary (8 bit) = `0001 0100`.
Invert all bits: `1110 1011`. Add 1: `1110 1011 + 1 = 1110 1100`.
**−20 = `1110 1100`**

**(b)** Mantissa `0.1010000` with the point after the sign bit. The sign bit is `0`, so the number is positive.
Place values after the point: `0.1010000` = 1×2⁻¹ + 0×2⁻² + 1×2⁻³ = 0.5 + 0.125 = **0.625**.
Exponent `0011` (two's complement) = +3, so move the binary point **3 places right**:
0.625 × 2³ = 0.625 × 8 = **5.0 (denary)**.

**(c)**
- **Advantage:** more mantissa bits give **greater precision** — more significant figures can be stored, so the rounding/representation error is smaller.
- **Disadvantage:** because the total bit count is fixed, the exponent loses bits, so the **range** of numbers that can be represented is reduced (smaller largest/largest-magnitude values).

### Why this scores

- **(a) shows the method, not just the answer.** The two's-complement marks are method marks: writing the positive value, the *invert*, and the *add 1* lines means even a slip in the final addition can still earn credit. **Always lay out flip-and-add-1 explicitly** — a bare `11101100` risks all marks if one bit is wrong.
- **(b) states the sign first.** Identifying that the sign bit `0` makes it positive shows control of two's-complement mantissas (where a `1` sign bit would mean a *negative* fraction). The candidate **shows the place-value expansion** (0.5 + 0.125) and **shows the exponent shift as ×2³** — both are the load-bearing working the examiner is looking for. The final `5.0` is reached by a visible multiplication, not asserted.
- **(c) is a genuine trade-off, not two random facts.** The disadvantage is *linked to the constraint* in the question ("total bit count fixed... exponent loses bits"). That linkage is the AO2 move: the weaker answer just says "less range" without explaining *why* (the bits had to come from somewhere). Precision↔range is the classic floating-point trade-off the spec wants.

### Common weaker response

> (b) "0.625 × 3 = 1.875." (c) "Advantage: more accurate. Disadvantage: takes more memory."

The (b) error is the classic one — **multiplying by the exponent instead of by 2^exponent**. In (c), "takes more memory" is *wrong* (the total is fixed) and "more accurate" is too vague to score — precision is the correct term, and there's no explanation of the range cost. Mid-band answers state outcomes; top-band answers explain the mechanism.

---

## Question 2 — Big O justification (2.3.1) · 6 marks · AO1/AO2

> A program must search an **ordered** array of *n* integers.
>
> **(a)** State the **time complexity** (Big O) of a **binary search** and of a **linear search**. **[2]**
> **(b)** Explain, with reference to how each algorithm works, **why** binary search has a lower time complexity than linear search for large *n*. **[4]**

### Model answer

**(a)** Binary search: **O(log n)**. Linear search: **O(n)**.

**(b)** A linear search checks each element in turn from one end of the array, so in the worst case (the target is last or absent) it makes up to *n* comparisons — the number of comparisons grows **in direct proportion** to *n*, giving O(n).

A binary search exploits the fact that the array is ordered: it compares the target with the **middle** element and, because the data is sorted, can discard the **half** of the array that cannot contain the target. Each comparison therefore **halves** the remaining search space (n → n/2 → n/4 → …). The number of times *n* can be halved before reaching one element is **log₂ n**, so it makes at most log₂ n comparisons, giving O(log n).

For large *n*, log n grows **far more slowly** than n (e.g. for n = 1,000,000, linear ≈ 1,000,000 comparisons but binary ≈ 20), so binary search scales much better — which is why it has the lower time complexity.

### Why this scores

- **(a) uses correct Big O notation** — `O(log n)` not "log n" or "logarithmic time" alone. Precision of notation is an easy mark candidates lose by being sloppy.
- **(b) ties the complexity to the *mechanism*.** The marks here are: "checks each element → up to n comparisons → proportional → O(n)" for linear, and "compares middle → discards half → halves each time → log₂ n → O(log n)" for binary. The phrase **"because the data is sorted"** earns credit because it explains *why binary search is even possible* — a frequent omission.
- **The connectives do the work.** "so", "therefore", "because" turn a list of facts into a *justified* chain (point → reason → consequence). That is the AO2 explain technique.
- **The concrete comparison clinches it.** Quantifying (1,000,000 vs ~20) demonstrates genuine understanding that log n ≪ n for large n, which is the actual reason behind "lower time complexity for large n." The conclusion is explicitly *justified*, not just restated.

### Common weaker response

> "Binary search is O(log n) and linear is O(n). Binary search is faster because it splits the list in half, and linear search is slower because it goes through everything one by one."

This earns the (a) marks and *some* of (b), but it stalls at mid-band: "splits the list in half" never explains that **each step discards half**, never connects the halving to **log₂ n**, and never mentions the array being **sorted** (the precondition). It asserts "faster" without showing how the comparison counts scale. No quantified reasoning, no justified link to *complexity*.

---

## Question 3 — Compare/explain: procedural vs OOP paradigm (1.2.4 / 2.2.1) · 6 marks · AO1/AO2

> A software house is choosing between a **procedural** and an **object-oriented** approach for a large new banking application maintained by many programmers over many years.
>
> Compare the two paradigms and explain which is more suitable for this project. **[6]**

### Model answer

In a **procedural** paradigm the program is structured as a sequence of subroutines (procedures/functions) that operate on data which is generally passed around or held globally. In an **object-oriented (OOP)** paradigm the program is structured as **objects** — instances of **classes** that **encapsulate** both data (attributes) and the methods that act on them.

A key difference is **encapsulation**: in OOP, an account's balance can be made `private` and changed only through controlled methods, **whereas** in procedural code data is more exposed and any procedure can modify it. For a banking application this matters because it protects the integrity of sensitive data and reduces the chance of one programmer accidentally corrupting another's data.

OOP also supports **inheritance** and **polymorphism**: a base `Account` class can be extended into `SavingsAccount` and `CurrentAccount`, reusing common code, **whereas** a procedural approach would tend to duplicate logic. This makes the OOP version **easier to extend and maintain** when new account types are added later. With **many programmers over many years**, the modular, self-contained nature of classes lets teams work on separate objects independently and makes the code easier to understand and debug.

**Overall, OOP is more suitable here:** the large scale, long lifespan, sensitive data and large team mean maintainability, reusability and data protection outweigh the slightly higher initial design overhead — strengths that map directly onto this project's requirements.

### Why this scores

- **It compares, it doesn't describe twice.** The connective **"whereas"** appears repeatedly, placing the two paradigms *side by side* on the **same** criterion (encapsulation, then inheritance). The single biggest "compare" error is writing one paragraph on A and one on B and never linking them — this answer never does that.
- **Every technical point is cashed out *in the scenario*.** "an account's balance can be made `private`", "`SavingsAccount` and `CurrentAccount`", "many programmers over many years" — this is the AO2 move that lifts it above a generic textbook comparison. Examiners reward the link to *this* banking project, not paradigms in the abstract.
- **It reaches a justified decision.** "Overall, OOP is more suitable... because the large scale, long lifespan... outweigh the slightly higher initial overhead" — it **acknowledges a cost** and explains why the benefits win. A judgement that recognises the trade-off scores higher than a flat "OOP is better."
- **Specialist terms are accurate:** encapsulation, class, object, attribute, method, inheritance, polymorphism — all used correctly and in context.

### Common weaker response

> "Procedural uses procedures and functions. OOP uses objects and classes which have methods and attributes. OOP has inheritance and encapsulation. I think OOP is better for big projects."

Accurate but mid-band: it **lists features of each** without ever putting them head-to-head (no "whereas"), it **ignores the banking scenario entirely**, and the conclusion ("I think OOP is better") is an *assertion* with no reasoning tied to scale, team size or data sensitivity. Correct knowledge, missing AO2 application and AO3 justification.

---

## Question 4 — Application: networking / TCP-IP stack (1.3.1) · 5 marks · AO1/AO2

> A user enters a URL into a web browser and a web page is returned from a server on the internet.
>
> Explain how the **TCP/IP stack** is used to transmit the request and receive the web page, referring to the role of **each layer**. **[5]**

### Model answer

The TCP/IP stack has four layers, each adding/removing its own information as data passes through it.

- **Application layer:** the browser uses an application-layer protocol — **HTTP(S)** — to format the request for the web page. This is where the user's data/request originates.
- **Transport layer:** **TCP** splits the request into **packets**, numbers them so they can be reassembled in the correct order at the other end, and adds **port numbers** (e.g. port 443 for HTTPS) so the data reaches the correct application.
- **Network (internet) layer:** **IP** adds the **source and destination IP addresses** to each packet and handles **routing** of the packets across the internet so they reach the correct server.
- **Link (data link) layer:** adds the physical **MAC address** of the next device and handles transmission over the physical hardware/medium.

At the receiving server the process is **reversed**: each layer strips its own information (the link layer first, up to the application layer) until the original HTTP request is reconstructed and the server returns the web page, which travels back down through the same four layers.

### Why this scores

- **All four layers are named *and* given a distinct role.** The marks are awarded per layer's function: Application=protocol/HTTP, Transport=packets+ports, Network=IP addresses+routing, Link=MAC/physical. Missing a layer or merging two is the usual way marks leak away.
- **It applies to the scenario.** HTTPS/port 443, "fetch the web page", "the server returns the web page" — the answer is grounded in the *URL-in-a-browser* scenario rather than reciting the stack abstractly. That is the AO2 credit.
- **It captures the reversal at the receiver.** Strong answers note that the stack is traversed **down** at the sender and **up** at the receiver, with each layer **stripping** its own header — showing understanding of *encapsulation/de-encapsulation*, not just a list of layers.
- **Precision of protocols.** Correctly mapping HTTP→application, TCP→transport, IP→network is the kind of accuracy that distinguishes top answers from "TCP/IP sends the data in packets."

### Common weaker response

> "The application layer is the browser. The transport layer breaks it into packets. The network layer sends it using IP addresses. The link layer is the physical hardware. Then the server sends the page back."

Close, but it's the difference between 3/5 and 5/5: no **port numbers**, no mention of **TCP numbering packets for reassembly**, no **routing**, and "sends it back" glosses over the **layers being reversed/headers stripped** at the server. Each missing detail is a missing mark — application questions reward the *specific function* at each step.

---

## Question 5 — Recursion / code tracing (2.2.2) · 6 marks · AO1/AO2/AO3

> Consider the following recursive subroutine written in OCR pseudocode:
>
> ```
> function mystery(n)
>     if n <= 1 then
>         return 1
>     else
>         return n * mystery(n - 1)
>     endif
> endfunction
> ```
>
> **(a)** State what value `mystery(4)` returns and identify what the subroutine calculates. **[2]**
> **(b)** Identify the **base case** and the **general (recursive) case**, and explain why a base case is essential. **[2]**
> **(c)** State **one** advantage and **one** disadvantage of using recursion rather than an iterative loop for this task. **[2]**

### Model answer

**(a)** `mystery(4)` = 4 × mystery(3) = 4 × 3 × mystery(2) = 4 × 3 × 2 × mystery(1) = 4 × 3 × 2 × 1 = **24**.
The subroutine calculates the **factorial** of `n` (n!).

**(b)**
- **Base case:** `if n <= 1 then return 1` — the condition that stops the recursion.
- **General/recursive case:** `return n * mystery(n - 1)` — the function calls itself with a **smaller** argument, moving towards the base case.
- A base case is **essential** because without it the function would call itself indefinitely; each call adds a new frame to the **call stack**, so the recursion would never terminate and would eventually cause a **stack overflow**.

**(c)**
- **Advantage:** the recursive solution is **shorter and more closely matches the mathematical definition** of factorial, making it easier to read and reason about.
- **Disadvantage:** recursion uses **more memory** because each call adds a stack frame to the call stack, and for large *n* this risks a **stack overflow**; it also carries the overhead of repeated function calls, so it can be slower than an equivalent loop.

### Why this scores

- **(a) shows the unwinding.** Writing out `4 × mystery(3) × …` demonstrates the candidate *traced* the recursion rather than guessing 24. Naming it as **factorial** earns the "identify" mark — pattern-recognition that the examiner is testing.
- **(b) quotes the actual code lines** for base and general case and gets the precise term **call stack / stack overflow**. The explanation is a proper cause→effect chain ("no base case → calls itself indefinitely → stack frames pile up → stack overflow"), which is the AO2/AO3 reasoning rather than just "it would loop forever."
- **(c) gives a real, contrasting trade-off.** The advantage (matches the mathematical definition / concise) and disadvantage (call-stack memory cost, risk of overflow) are *specific to recursion vs iteration* — not generic. Linking the disadvantage back to the **call stack** ties it to (b) and shows joined-up understanding.

### Common weaker response

> (a) "24, it does multiplication." (b) "The base case is the if and the recursive case is the else. You need a base case or it loops forever." (c) "Advantage: it's shorter. Disadvantage: it's harder to understand."

Mid-band: (a) misses **factorial**; (b) gestures at the lines but never says **call stack / stack overflow** ("loops forever" is imprecise — recursion *crashes*, it doesn't loop); (c)'s disadvantage ("harder to understand") is a weak generic point that misses the key technical cost — **memory/stack frames**. The technical vocabulary is exactly what separates the bands here.

---

## Question 6 — Levels-of-response essay: ethics & society (1.5.1) · 12 marks · AO1/AO2/AO3

> A large supermarket chain is introducing **fully automated, AI-driven self-checkout and stock systems** that will replace many of its human checkout and warehouse staff.
>
> Discuss the **impact** of introducing this technology. Your answer should consider the **ethical, legal/cultural, social and economic** issues and reach a **justified conclusion**. **[12]**

### Level 3 descriptors (the band you are aiming for)

> **Level 3 (9–12 marks):** A **thorough discussion** with a wide range of **well-developed points** showing detailed knowledge and understanding, **applied to the context**. Multiple **perspectives/stakeholders** are considered with clear **balance** (benefits *and* drawbacks). The response is **well structured and coherent**, uses **specialist terminology** accurately throughout, and reaches a **reasoned, justified conclusion** that follows from the discussion.
>
> *(Level 2, 5–8: a reasonable discussion with some development and some balance, but one-sided in places or with weaker links to context; conclusion present but limited. Level 1, 1–4: fragmented, mostly assertion/description, little development, no real conclusion.)*

### Model answer

The introduction of fully automated AI checkout and stock systems by the supermarket raises significant ethical, economic, legal, social and cultural issues that affect several stakeholders — the business, its employees, customers and wider society.

**Economically**, the business benefits: automated systems can run continuously without wages, sickness or breaks, **reducing long-term operating costs** and potentially increasing profit and competitiveness. Faster checkout and better-managed stock could also improve customer throughput and reduce waste. **However**, there is a large **initial capital cost** for the hardware, software and maintenance, and the technology requires skilled technicians to support it. So while costs fall in the long run, the change is a significant investment with risk.

**Ethically and socially**, the most serious impact is on **employees**: replacing "many" checkout and warehouse staff causes **redundancies and unemployment**, which is ethically difficult because these are often lower-paid workers with fewer alternative opportunities. There is a moral argument that a profitable company has a **duty of care** to retrain or redeploy staff rather than simply remove them. **On the other hand**, automation removes repetitive, physically demanding warehouse work and can create *new* roles in maintaining and developing the systems — though these typically require **different, higher-level skills**, so the displaced staff may not be able to fill them. Society also bears a cost: higher unemployment can increase the burden on the state through benefits, while a **digital divide** may exclude older or less tech-confident customers who struggle with fully automated checkouts and prefer human interaction.

**Legally and culturally**, the business must comply with **employment law** when making staff redundant (fair process, consultation, redundancy pay) and with **data protection legislation (e.g. the Data Protection Act / GDPR)** because AI systems that track stock and customer behaviour may **collect and process personal data**, which must be stored securely and used lawfully. Culturally, some customers value the **human contact** of a staffed checkout, and removing it entirely may alienate part of the customer base or change the character of the shopping experience, particularly in communities where the supermarket is a social hub.

**In conclusion**, the technology offers the supermarket clear long-term economic and efficiency benefits and can improve some aspects of the customer experience, but these come at a real human cost in lost jobs and a risk of excluding vulnerable customers, alongside legal and data-protection obligations. **On balance, the introduction is likely to be justified for the business commercially**, but it should be done **responsibly** — for example, by retraining and redeploying staff where possible, retaining *some* staffed checkouts to support customers who need them, and ensuring full legal and data-protection compliance — so that efficiency gains are not achieved at an unacceptable social cost.

### Why this scores (Level 3)

- **Breadth: all four required strands are covered** — economic, ethical/social, legal, cultural — and **multiple stakeholders are named** (business, employees, customers, society/the state). Breadth across angles and stakeholders is the single strongest signal of the top band.
- **Every point is *developed*, not just stated.** The structure is consistently **point → because → consequence → linked to a stakeholder** (e.g. "redundancies... because lower-paid workers... duty of care to retrain"). Listing issues without development is what caps an answer at Level 2.
- **Genuine balance.** The connectives **"However", "On the other hand"** force each benefit to meet a drawback, and even the "new jobs" upside is *qualified* ("different, higher-level skills... displaced staff may not be able to fill them"). This nuance is exactly what examiners mean by "well-developed."
- **Applied to the context throughout** — "checkout and warehouse staff", "supermarket is a social hub", AI "track stock and customer behaviour" — never generic AI ethics. That is the AO2 thread running through an AO3 question.
- **Accurate specialist terms** — *digital divide, duty of care, Data Protection Act/GDPR, redundancy/consultation, capital cost* — used correctly, signalling command of the 1.5 vocabulary.
- **A justified conclusion that follows from the discussion.** It doesn't sit on the fence: it **commits** ("likely to be justified commercially") but **conditions** the judgement ("done responsibly... retain some staffed checkouts"), explicitly weighing the trade-off it built up. A decision that references the arguments made is what converts a good discussion into full marks.

### Common weaker response (Level 2)

> "Automation is good for the supermarket because it saves money and doesn't need wages. It's bad because people lose their jobs and become unemployed. Some customers might not like using machines. Also AI could collect data on customers. Overall I think it's good because the supermarket saves money."

Why it stalls at Level 2: the points are **stated but not developed** (no "because/which means" chains, no consequences), it's **thin on balance** and leans toward the business, the **legal/cultural strand is barely touched** (data is mentioned but no legislation; culture is missing), specialist terminology is sparse, and the conclusion is a **bald assertion** ("I think it's good because it saves money") that ignores the human and legal costs it just raised. It has the *ingredients* of a good answer but none of the **development, breadth and justification** that define Level 3.

---

## The transferable A\* moves (use these on every question)

1. **Show working on everything numeric.** Two's-complement flip-and-add-1, place-value expansions, the ×2^exp shift, recursion unwinding, trace tables — visible method earns method marks even when the final number slips.
2. **Use the connective the command word demands.** *Explain* → "because/so that"; *Compare* → "whereas/in contrast"; *Evaluate/Discuss* → "however/on the other hand" + "overall/on balance".
3. **Drag the scenario into every point (AO2).** Name the bank, the supermarket staff, the URL, port 443. Generic textbook recall is a B; applied recall is an A.
4. **Quantify when you can.** "1,000,000 vs ~20 comparisons" proves you understand *why* log n < n, not just that it is.
5. **Commit to a justified conclusion (AO3).** State a decision, acknowledge the cost/trade-off, and say why your side wins. Fence-sitting and bald assertion both cap you below the top band.
6. **Be precise with terminology.** O(log n) not "logarithmic"; call stack/stack overflow not "loops forever"; encapsulation not "hiding stuff". Precise terms are free marks.
