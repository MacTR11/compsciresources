# Exam Technique — Turning Knowledge into Marks

You can know the whole spec and still drop a grade through poor exam technique. This page is the "how to sit the paper" guide for both H446/01 and H446/02.

---

## Before the exam: the 3 things that move grades most

1. **Past papers under timed conditions, marked against the official mark scheme.** Nothing else builds technique as fast. Aim to complete *every* available past paper at least once.
2. **Learn the mark scheme's language.** OCR mark schemes reward specific terms. Read mark schemes *as a revision resource*, not just to check answers — notice the exact wording that scores.
3. **Drill the discriminator topics** (the ones that separate A from A\*): floating-point & two's complement (1.4.1), Boolean simplification & adders (1.4.3), Big O & tracing standard algorithms (2.3), recursion & OOP (2.2.1), and extended-response ethics (1.5).

---

## Timing strategy

Both papers are **2h 30m for 140 marks** ≈ **just over 1 minute per mark**, leaving a buffer for the long questions and checking.

- **Roughly a minute a mark.** A 6-mark question deserves ~6 minutes — no more, no less.
- **Don't camp on a hard question.** Mark it, move on, come back. A blank 1-mark later in the paper is the same loss as a blank 1-mark here, and easier to recover.
- **Leave ~10 minutes at the end** to return to flagged questions and check calculations/traces.
- **Long-answer questions (9–12 marks):** spend 1–2 minutes *planning* (jot a bullet skeleton in the margin) before writing. Planned answers reach the top band far more often.

---

## In the question: a repeatable method

1. **Read the whole question first**, including the scenario stem — later parts often reference it.
2. **Decode the command word and tariff** (see [command-words guide](command-words-and-assessment-objectives.md)).
3. **For AO2/AO3, anchor to the scenario.** If the question is about "a hospital booking system", your answer must talk about *that*, not a generic one.
4. **Make your points distinct and developed.** Examiners count *separate* valid points. Repeating the same idea in new words scores once.
5. **Use connectives that force development:** *because, which means, therefore, so that, whereas, in contrast, overall.*
6. **Show all working** for number/logic/trace questions — method marks survive a wrong final answer.

---

## Question-type playbooks

### Calculation / number representation (1.4.1)
- Write each conversion step. For two's complement, **state the column values** and show the flip-and-add-1.
- For floating point, **label the mantissa and exponent**, and for normalisation state the rule you're using.
- Sanity-check magnitude (is a "negative" number's leftmost bit a 1?).

### Trace tables / algorithm tracing (2.2, 2.3)
- Draw a **column per variable** and a row per iteration. Update one step at a time.
- Don't do it in your head — the marks are for the *table*, and it stops silly slips.

### "Write/complete the algorithm" (2.2, 2.3)
- **Initialise** variables. Handle the **edge cases** (empty list, not found, first/last element).
- Use clear OCR pseudocode (or a consistent high-level language). Indentation and `next`/`endif`/`endwhile` show structure.
- Re-trace your own code on one example before moving on.

### Boolean algebra & logic (1.4.3)
- Build the **truth table** if unsure; it's almost always worth the marks.
- When simplifying, **name the law** you apply at each step (De Morgan's, distribution, etc.).

### Compare / evaluate (AO3)
- Use a **point-by-point** structure, not two separate descriptions.
- End with a **judgement**: "X is more suitable here *because*…". A comparison with no conclusion stalls in the middle band.

### Extended response / ethics essays (1.5, "discuss")
- Follow the **FOR → AGAINST → FOR → AGAINST → justified conclusion** skeleton.
- Name **multiple stakeholders** and **multiple angles** (legal, ethical, economic, environmental, social).
- See the worked levels-of-response example in the [1.5 resource](../../component-01-computer-systems/1.5-legal-moral-cultural-ethical.md).

---

## Things that silently cost marks

- **One-word answers to "describe/explain".** Add the detail / the "because".
- **Ignoring the scenario** on application questions (instant cap on AO2 marks).
- **Final answer with no working** — no method marks to fall back on.
- **Listing instead of comparing/evaluating** when the command word asked for judgement.
- **Repeating one idea** in different words and expecting multiple marks.
- **Running out of time** because you over-wrote 1–2 mark questions early on.
- **Vague terminology** — "it's faster" (why? cache? fewer cycles?). Precision scores.

---

## The night before & the morning of
- Re-read your **RAG tracker** Reds/Ambers and the **glossary**, not the whole spec.
- Skim the **common-mistakes** sheet — it's the cheapest marks you'll ever bank.
- Bring the basics: black pen (+ spare), pencil and ruler (for logic circuits/graphs), and a watch to pace yourself.

Technique is a skill you *practise*. Every past paper you mark against the scheme makes the real thing more familiar — which is exactly what calm, high-scoring exam performance is built on.
