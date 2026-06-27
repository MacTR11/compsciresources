# Quiz Banks (multiple-choice)

Self-test multiple-choice question banks — **14 questions per topic** (112 total), each with four options, the correct answer, and a one-line explanation. These power the [Interactive Revision Hub](../interactive-quiz/README.md) and can also be used directly.

## Files
One JSON file per spec section (`1.1` … `2.3`). Schema:
```json
{
  "topic": "1.1 Processors, Input, Output & Storage",
  "spec": "Component 01 — 1.1",
  "questions": [
    { "q": "…", "options": ["A","B","C","D"], "answer": 0, "explain": "why A is correct" }
  ]
}
```
`answer` is the 0-based index of the correct option.

## Ways to use them
- **Easiest:** open the [Interactive Hub](../interactive-quiz/index.html) and pick *Quiz* — it marks you and tracks your best score.
- **Import:** the JSON is easy to convert into Google Forms, Quizizz, Kahoot, or a teacher's own quiz tool.
- **Quick self-test:** read the `q` and `options`, decide, then check `answer`/`explain`.

> After editing a quiz, rebuild the hub data with `python3 revision-tools/interactive-quiz/build_data.py`.
