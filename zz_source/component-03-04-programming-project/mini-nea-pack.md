# Mini-NEA Pack (Weeks 29–36) — Practice Programming Project

*OCR A Level Computer Science (H446) — preparation for Component 03/04 (Programming Project)*

The **mini-NEA** is an eight-week practice run of the real Programming Project. You will take one small, tightly-scoped problem through all four assessed stages — **Analysis → Design → Development → Evaluation** — producing a short project report in the **NEA Project Template** and a working program. It is marked out of **35** using a grid scaled directly from the real OCR criteria, so the feedback you get tells you exactly where you would sit on the real 70-mark project.

> ⚠️ This is *practice*. The real NEA (started in Year 13) must be your own new problem — you may **not** reuse a brief from this pack as your real project. What you *can* reuse is everything you learn about evidencing each stage.

**What you need alongside this pack:**

- The **NEA Guide** (how each stage is marked and how to hit the top band).
- The **NEA Project Template** (type your write-up into it — Stage 1–4 sections match this pack's milestones).

---

## Part 1 — Choose your project brief

Pick **one** of the three briefs below. All three are deliberately small: the point is to complete every stage well, not to build something huge. Each brief gives you a **stakeholder**, **scope boundaries**, and a **requirements seed** in MoSCoW form (*must / should / could*). The seed is a starting point — your Analysis must turn it into **measurable success criteria** justified by your own stakeholder research.

For every brief, your stakeholder should be a **real, named person** you can actually talk to (a subject teacher, a member of staff, a younger student, a club leader). Interview them in week 29 and record what they said.

### Brief A — Revision flashcard app

A subject teacher wants a simple flashcard program their class can use for retrieval practice. Cards are question/answer pairs grouped by topic; the program quizzes the user and tracks which cards they keep getting wrong.

**Stakeholder:** a teacher of any subject (or a Year 10/11 student revising for GCSEs). Their core need: quick, repeatable self-testing that focuses effort on weak cards.

**Scope boundaries:**

| In scope | Out of scope |
|----------|--------------|
| Text question/answer cards stored in a file (CSV or text) | Images, audio, rich formatting |
| Topics/decks; the user picks a deck to revise | Online sync, accounts, multiple users |
| Quiz loop with self-marked or exact-match answers | Fuzzy answer matching / AI marking |
| A "leitner"-style weighting so wrong cards reappear more often | Spaced repetition across calendar days |
| A score/summary at the end of a session | Graphs and long-term analytics dashboards |

**Requirements seed (develop and justify these in your Analysis):**

- **Must:** load a deck of cards from a file; quiz the user on every card in a chosen deck; record right/wrong per card; show an end-of-session score; reject/handle a missing or malformed deck file without crashing.
- **Should:** let the user add, edit and delete cards from within the program (saved back to the file); make wrong cards reappear more frequently in the next round.
- **Could:** shuffle order each session; a simple hardest-cards report; support for more than one saved user profile.

**Where the algorithmic content is:** the wrong-card weighting (a priority queue or weighted selection), file parsing with validation, and searching/sorting cards by topic or success rate.

### Brief B — Canteen pre-order system

The school canteen wants students to pre-order lunch from a daily menu so the kitchen knows quantities in advance and queues are shorter.

**Stakeholder:** the canteen manager (kitchen side) and a student (ordering side) — interview at least one of them for real; role-play the other if necessary and say so.

**Scope boundaries:**

| In scope | Out of scope |
|----------|--------------|
| A daily menu of items with prices and limited stock, loaded from a file | Real payment processing |
| Students place an order (name/ID + items) before a cut-off | Accounts with passwords, online ordering |
| Stock decreases as orders are taken; sold-out items cannot be ordered | Nutrition data, allergy management |
| A kitchen report: totals per item, list of orders, takings | Multi-day forecasting |
| Orders saved to file so the program can be closed and reopened | Networked/multi-terminal operation |

**Requirements seed (develop and justify these in your Analysis):**

- **Must:** load the menu (items, prices, stock) from a file; take an order made of one or more valid items; refuse items that are sold out or not on the menu; save orders to file; produce a kitchen report of quantities per item and total takings.
- **Should:** enforce an order cut-off (e.g. a maximum number of orders or a "close orders" action); allow a student to amend or cancel their order before cut-off; validate student ID format.
- **Could:** a daily-special discount rule; search orders by student; export the kitchen report to a separate file.

**Where the algorithmic content is:** record-style data structures for menu and orders, linear/binary search for order lookup, aggregation for the report, and robust validation throughout.

### Brief C — PE fixtures manager

The PE department runs inter-form sports fixtures each term and currently tracks them on paper. They want a program that stores teams, generates a fixture list, records results, and produces a league table.

**Stakeholder:** a PE teacher or the sports captain who runs the tournament. Their core need: no more clashes/missed fixtures, and an always-up-to-date league table.

**Scope boundaries:**

| In scope | Out of scope |
|----------|--------------|
| One sport, one competition, 4–10 teams | Multiple simultaneous sports/seasons |
| Round-robin fixture generation (each team plays each other once) | Knockout brackets, seeding, scheduling to real dates/venues |
| Entering results (score per team per fixture) | Player-level statistics |
| League table sorted by points, then goal/point difference | Web publishing, live updates |
| Data saved to and loaded from file | Databases with SQL (allowed, but not required) |

**Requirements seed (develop and justify these in your Analysis):**

- **Must:** store a list of teams; generate a complete round-robin fixture list with no team playing itself and no duplicate pairing; record a result against a fixture; calculate points (e.g. win 3 / draw 1 / loss 0); display a league table sorted by points then difference; save/load all data.
- **Should:** prevent a result being entered twice for the same fixture (with an option to correct one); validate scores as non-negative integers; show remaining (unplayed) fixtures.
- **Could:** a form/recent-results column; a top-scoring-team report; handle a team withdrawing part-way through.

**Where the algorithmic content is:** the round-robin pairing algorithm (nested iteration or the circle method), a two-key sort for the league table, and structured records for fixtures and results.

---

## Part 2 — Week-by-week milestones

The eight weeks match the four stages: **29–30 Analysis, 31–32 Design + test plan, 33–34 Implementation, 35–36 Evaluation**. Each week has a deliverable checklist — tick everything off before the next lesson. The template sections referred to are in the **NEA Project Template**.

### Week 29 — Analysis 1 (define the problem)

Choose your brief, identify your real stakeholder, and carry out your research.

**Deliverables checklist:**

- ☐ Brief chosen and stakeholder named (a real person, not "any user")
- ☐ Stakeholder interviewed — questions and answers recorded in Template 1.2
- ☐ Problem description written: what the problem is and why it suits a computational solution (Template 1.1)
- ☐ One existing/similar solution examined with strengths/weaknesses noted (Template 1.3)
- ☐ First draft of requirements from the MoSCoW seed, amended to match what your stakeholder actually said

### Week 30 — Analysis 2 (measurable success criteria)

Turn requirements into numbered, **measurable** success criteria and finish the Analysis write-up.

**Deliverables checklist:**

- ☐ Success criteria table complete (Template 1.4): every criterion specific and testable, each justified by stakeholder need
- ☐ At least one criterion covering robustness (invalid/erroneous input handled without crashing)
- ☐ Scope boundaries stated: what is deliberately excluded and why
- ☐ Peer review done: a partner has checked your Analysis against the NEA checklist and you have acted on their comments
- ☐ Analysis section finished and complete

### Week 31 — Design 1 (structure, algorithms, data)

Plan the solution in enough detail that someone else could build it.

**Deliverables checklist:**

- ☐ Decomposition: structure chart or module list covering the whole solution (Template 2.1)
- ☐ Key algorithm(s) written in pseudocode or flowchart — at minimum the "algorithmic content" named in your brief (Template 2.2)
- ☐ Data structures chosen and **justified** (why an array of records? why a file in this format?) (Template 2.3)
- ☐ UI sketch/wireframe with navigation (a menu map is fine for a console program) (Template 2.4)
- ☐ Every design decision traced back to a numbered requirement

### Week 32 — Design 2 (test plan)

Complete the design and write the test plan **before** you write any code.

**Deliverables checklist:**

- ☐ Test plan table complete (Template 2.5): typical, boundary and erroneous data for every input and every key algorithm
- ☐ Every test mapped to a numbered success criterion
- ☐ Expected results stated precisely (an exact value or behaviour, not "it works")
- ☐ Design reviewed against the Design checklist in the template
- ☐ Iteration plan drafted: what Iteration 1, 2, 3 will each deliver

### Week 33 — Implementation 1 (first iterations)

Build the core in small iterations, testing each one as you go.

**Deliverables checklist:**

- ☐ Iteration 1 built (typically: data structures + file loading) and evidenced in Template Stage 3
- ☐ Iteration 2 started (core algorithm from your design)
- ☐ Each iteration entry has: goal, annotated code evidence, tests run this iteration with results
- ☐ At least one failed test shown with the fix explained (do not hide failures — they earn marks)
- ☐ Development diary/log kept up to date as you go, not reconstructed afterwards

### Week 34 — Implementation 2 (robustness and completion)

Complete the *must* requirements; add validation and error handling.

**Deliverables checklist:**

- ☐ All *must* requirements implemented (park unfinished *should/could* items — that is what evaluation is for)
- ☐ Validation and error handling added: bad input, missing/corrupt files, boundary values all handled without crashing
- ☐ The claimed algorithmic complexity is demonstrably working, with evidence
- ☐ Code quality pass: meaningful names, subroutines with parameters, comments where logic is non-obvious
- ☐ File check ready: every piece of code evidence is annotated (what it does and which requirement it serves)

### Week 35 — Evaluation 1 (test against every criterion)

Run your full test plan and gather stakeholder feedback.

**Deliverables checklist:**

- ☐ Every success criterion tested with evidence — screenshots/output plus the test number (Template 4.1)
- ☐ Boundary and erroneous tests from the week-32 plan all executed and recorded
- ☐ Each criterion honestly judged: Met / Partly met / Not met
- ☐ Stakeholder has seen the working program; their feedback recorded verbatim
- ☐ Every evaluation point maps back to a numbered criterion from the Analysis

### Week 36 — Evaluation 2 (judgement and improvements)

Finish the evaluation and submit.

**Deliverables checklist:**

- ☐ Evaluation of the solution written, using stakeholder feedback as evidence (Template 4.2)
- ☐ Usability evaluated from the stakeholder's point of view (Template 4.3)
- ☐ Improvements/future development: specific and justified, not "add more features" (Template 4.4)
- ☐ Final self-check in the template completed; report and code submitted
- ☐ Post-mortem note to yourself: two things to do differently in the real NEA (bring this to your first Year 13 NEA lesson)

---

## Part 3 — Marking grid (out of 35)

The mini-NEA is marked out of **35** — exactly half the real project's 70 marks, using the same weighting as OCR's real criteria (Analysis 10, Design 15, Development 25, Evaluation 20 → scaled to **5, 7, 13, 10**). Development keeps its two real sub-strands: **iterative development** and **using testing to inform development**. Three bands per strand; a strand showing nothing creditworthy scores 0.

| Strand | Real NEA marks | Mini-NEA marks |
|--------|---------------|----------------|
| Analysis | 10 | 5 |
| Design | 15 | 7 |
| Development — iterative development | 15 | 8 |
| Development — testing to inform development | 10 | 5 |
| Evaluation | 20 | 10 |
| **Total** | **70** | **35** |

### Analysis (5 marks)

| Band | Marks | Descriptor |
|------|-------|-----------|
| High | 5 | Problem clearly defined and justified as suited to a computational solution. Named stakeholder with documented research (interview evidence). Existing solution analysed for usable ideas. A full set of **specific, measurable** success criteria, each justified against stakeholder need; scope limits stated. |
| Middle | 3–4 | Problem described and a stakeholder identified with some research. Requirements listed and mostly measurable, but some criteria are vague or not clearly linked to the stakeholder; limited analysis of existing solutions. |
| Low | 1–2 | Problem outlined; stakeholder generic or unresearched. Requirements are a feature wish-list — few or none are testable. Little evidence the problem was investigated. |

### Design (7 marks)

| Band | Marks | Descriptor |
|------|-------|-----------|
| High | 6–7 | Full decomposition into modules. Key algorithms in pseudocode/flowcharts including the project's genuine algorithmic content. Data structures and file formats chosen **and justified**. Usable UI design. A complete test plan with typical, boundary and erroneous data mapped to numbered success criteria. Design decisions trace to requirements. |
| Middle | 3–5 | Decomposition and some algorithm design present but the hardest parts are under-specified. Data structures listed with limited justification. Test plan exists but has gaps (e.g. no erroneous data, tests not mapped to criteria). |
| Low | 1–2 | Fragmentary design: screenshots of intended UI or a module list only. No meaningful algorithm design; no usable test plan. The solution could not be built from this design. |

### Development — iterative development (8 marks)

| Band | Marks | Descriptor |
|------|-------|-----------|
| High | 7–8 | Clear iterations, each with a stated goal, annotated code and a review that shapes the next iteration (develop → test → review → refine is visible). The complexity claimed in Design is implemented and shown working. Good practice throughout: meaningful names, modular subroutines with parameters, validation, comments. All *must* requirements delivered. |
| Middle | 4–6 | A working solution built in recognisable stages, but the narrative is thin — code evidence present with limited annotation, and reviews between iterations are superficial. Most *must* requirements delivered; some good practice. |
| Low | 1–3 | Code presented as a single final lump with little evidence of process. Sparse or no annotation. Solution incomplete or missing the claimed complexity; little validation. |

### Development — testing to inform development (5 marks)

| Band | Marks | Descriptor |
|------|-------|-----------|
| High | 5 | Testing evidenced **during every iteration**, not just at the end. Failures shown honestly with diagnosis and fix. Boundary and erroneous data used while developing; the program is robust to bad input as a result. |
| Middle | 3–4 | Some testing during development with evidence, but mostly typical data; failures rarely shown or explained. Robustness patchy. |
| Low | 1–2 | Testing only at the end (or only claimed). No evidence that testing changed the code. Program crashes on invalid input. |

### Evaluation (10 marks)

| Band | Marks | Descriptor |
|------|-------|-----------|
| High | 8–10 | **Every** success criterion tested with cross-referenced evidence, including boundary and erroneous cases. Honest judgements — partially-met and unmet criteria acknowledged and explained. Stakeholder feedback gathered and used. Usability evaluated. Improvements are specific, justified and prioritised. |
| Middle | 4–7 | Most criteria addressed with some evidence, but coverage is incomplete or judgements are generous/unevidenced. Stakeholder feedback mentioned but not really used. Improvements listed without justification. |
| Low | 1–3 | General "it works well" commentary with little reference to the success criteria. No stakeholder feedback. Vague or no improvements. |

---

## Part 4 — Annotated exemplar extracts

Two short extracts from a high-band mini-NEA (Brief A, the flashcard app) showing the evidence standard expected. Annotations in *italics* explain why each part earns credit.

### Exemplar 1 — Analysis: success criteria table (Template 1.4)

| # | Success criterion (measurable) | Why it's needed (link to stakeholder) |
|---|-------------------------------|----------------------------------------|
| 1 | The program loads a deck of at least 50 cards from `deck.csv` in under 2 seconds and reports how many cards were loaded. | Ms Patel said her Biology deck has "about 60 cards" and she "won't use anything slow" (interview, Q3). |
| 2 | If `deck.csv` is missing or a line has the wrong number of fields, the program shows a clear error message naming the problem line and continues (or exits cleanly) — it never crashes. | Ms Patel edits the CSV in Excel and "will definitely break it sometimes" (interview, Q5). |
| 3 | In a quiz session, every card in the chosen topic is asked exactly once before any card repeats. | Students complained the paper flashcards get shuffled unevenly — same cards keep coming up (interview, Q4). |
| 4 | A card answered wrongly is at least twice as likely to appear in the next session as a card answered correctly, verified by counting appearances over 10 test sessions. | The core need: "focus effort on the ones they get wrong" (interview, Q1). |
| 5 | The end-of-session summary shows score as n/total and lists every card answered wrongly. | Ms Patel wants students to "leave knowing exactly what to revise" (interview, Q2). |

*Annotations — what makes this top-band:*

- *Every criterion has a number, so Design tests and the Evaluation can cross-reference it exactly ("criterion 4 — see Test 12").*
- *Every criterion is measurable: "under 2 seconds", "exactly once", "at least twice as likely, verified by counting over 10 sessions" — nothing here is "the app should be user-friendly".*
- *Every criterion is justified by a cited piece of stakeholder research (interview question numbers), not invented after the fact.*
- *Criterion 2 builds robustness into the success criteria — this is what makes the erroneous-data tests in the week-32 test plan compulsory rather than an afterthought.*
- *Criterion 4 is the algorithmic content: it commits the student to implementing and then measuring the weighted-selection algorithm, which is exactly the "complexity evidenced in design and code" the top band demands.*

### Exemplar 2 — Development: iterative diary entry (Template Stage 3)

> **Iteration 2 — weighted card selection (targets criterion 4)**
>
> **Goal:** replace Iteration 1's random choice with weighting so wrong cards appear more often.
>
> **Built:** each `Card` record now has a `weight` field (starts at 1; set to 4 on a wrong answer, halved — minimum 1 — on a right answer). `chooseCard()` does a weighted random pick: sum all weights, pick a random number in that range, walk the list subtracting weights until it goes below zero.
>

```python
def choose_card(cards):
    total = sum(card.weight for card in cards)
    pick = random.randint(1, total)
    for card in cards:
        pick = pick - card.weight
        if pick <= 0:
            return card
```

>
> *(Full annotated screenshot in Appendix B — each line labelled with what it does.)*
>
> **Testing this iteration:** Test 9 (typical): with weights [1, 4, 1], the middle card should appear roughly 4× as often. I ran 600 picks and counted 98 / 217 / 285 — **failed**: card 3 appeared far too often.
>
> **Diagnosis:** I was subtracting `card.weight` *after* the `<= 0` check in my first version, so the walk always overshot by one card. Traced it by hand with weights [1, 4, 1] and pick = 2 (trace table in Appendix B).
>
> **Fix and retest:** moved the subtraction before the check (code above is the fixed version). Re-ran Test 9: counts 103 / 396 / 101 over 600 picks — middle card ≈ 3.9× as frequent. **Pass** against criterion 4's "at least twice as likely".
>
> **Review → next iteration:** weighted picking works, but weights reset every run because nothing is saved. Iteration 3 will persist weights in the CSV (extends criterion 1's file format — design updated in section 2.3, change noted and justified).

*Annotations — what makes this top-band:*

- *The iteration has a stated goal tied to a numbered criterion, so the examiner can see requirements driving development.*
- *A real failure is shown with the count evidence, the diagnosis (including a hand trace), the fix, and a retest with new evidence. This one entry is worth more than ten screenshots of working code — it is the develop → test → review → refine cycle made visible.*
- *Testing uses measured results (counts over 600 picks) against the measurable criterion, not "I tested it and it works".*
- *The closing review sets up the next iteration and honestly records a design change, with the Design section updated to match — evidence of genuine iteration, not a post-hoc write-up.*

---

## Part 5 — Common pitfalls (and the band they cost you)

| Pitfall | Strand it hits | Why it caps your band |
|---------|---------------|----------------------|
| "My stakeholder is anyone who wants to revise" | Analysis | A generic, unresearched stakeholder is the defining feature of the low band — with no real needs, nothing else can be justified. |
| Success criteria like "the app should be easy to use" | Analysis, Evaluation | Unmeasurable criteria stall Analysis in the middle band and make a high-band Evaluation impossible — there is nothing concrete to test against later. |
| Test plan written after the code, or with only typical data | Design, Testing | Design's high band requires typical **and** boundary **and** erroneous data mapped to criteria; testing that never uses bad data leaves the program fragile and the testing strand in the low band. |
| Algorithms "designed" as a screenshot of finished code | Design | The design must plan the build, not describe it afterwards; reverse-engineered designs read as fragmentary and sit in the low band. |
| One giant code dump at the end labelled "Development" | Iterative development | Without visible iterations, goals and reviews, the develop → test → review → refine narrative is missing — the descriptor for the low band, however good the program is. |
| Unannotated code screenshots | Iterative development | Evidence with no explanation cannot show good practice or the claimed complexity; annotation is the difference between the middle and high bands. |
| Hiding failures ("all my tests passed first time") | Testing | Failures found and fixed are the strongest evidence that testing informed development; a wall of green passes suggests testing happened only at the end — middle band at best. |
| No validation — crashes on an empty input or missing file | Iterative development, Testing | Robustness is explicitly rewarded in the high band of both development strands; a program that crashes on erroneous data cannot score there. |
| Evaluation says "overall the project went well" | Evaluation | Commentary that never cites criterion numbers or test evidence is the low-band descriptor verbatim. Every judgement needs "criterion n — see Test m". |
| Claiming every criterion was fully met | Evaluation | Examiners reward honesty: "criterion 6 partly met because…" with evidence outscores an implausible clean sweep, which reads as unevidenced generosity (middle band). |
| Vague improvements ("add more features", "make it look better") | Evaluation | The high band needs specific, justified, prioritised improvements linked to stakeholder feedback — anything less is the middle band's "improvements listed without justification". |
| Scope creep — starting *could* features before *must* ones are done | Iterative development, Evaluation | An unfinished core caps the development band and leaves criteria untestable, dragging the Evaluation down with it. Park the extras; finishing beats featuring. |

---

*Next step after week 36: keep your marked mini-NEA. In Year 13 you will start the real 70-mark project — your first task will be choosing a problem, and your mini-NEA post-mortem (week 36 checklist) is the best guide you'll have.*
