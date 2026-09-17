# Stage 1 lab — selection and iteration

## Your tools today
Use variables, integers, arithmetic, comparisons, Boolean operators, `input`, `print`, `int`, `if/elif/else`, `while`, `for` and `range`. The scaffold also introduces `.strip()` and `.upper()` for normalising choices; your lecturer can demonstrate these. Do not introduce functions, lists, dictionaries, classes, imports or exception handling yet.

## Before coding — 10 minutes
1. Calculate the bill for 25 pages × 4 black-and-white copies with binding.
2. Decide whether the discount condition should use `> 100` or `>= 100`.
3. Identify which values reset per order and which survive across the session.
4. Trace the provided menu loop for inputs `9`, `2`, `0`.

## Implementation — approximately 80 minutes
| TODO | Task | Evidence |
|---|---|---|
| 1 | Validate pages and copies using separate while loops | Rejected 0 pages followed by valid 1 |
| 2 | Validate and normalise both letter choices | Rejected X followed by lowercase b |
| 3 | Select tariff and calculate printed pages | Correct colour and black-and-white subtotals |
| 4 | Apply discount and optional binding | 99 versus 100 printed pages; binding separate |
| 5 | Print an itemised receipt | Five labelled numeric lines |
| 6 | Generate collection labels with a for loop | Exactly three labels for three copies |
| 7 | Accumulate the session results | Two orders counted once each |
| 8 | Show summaries from both menu branches | Summary does not change totals; exit shows totals |

Implement and check one TODO at a time. `pass` is a placeholder meaning “do nothing”; replace it with your own statements. Keep input validation before calculation and accumulator updates. Ask the lecturer for a hint before using concepts that have not been taught.

## Review — 20 minutes
Run every scenario in `ACCEPTANCE.md`. Record actual results and pass/fail. For any failure, include the corrected reasoning and rerun evidence.

## Submission — 10 minutes
Submit the program, scenario evidence and a reflection of approximately 150 words answering:
- Why is `while` suitable for validation and `for` suitable for labels?
- What error occurs if an accumulator is reset inside the menu loop?
- Where did you repeat code? Which parts would you want to reuse next lesson?
- Which boundary case caught a mistake?

Keep a copy named `checkpoint_01.py` before the next lesson. Your next task will preserve these behaviours while extracting functions.

## Optional challenge, only after core completion
Add an order preview and a Y/N confirmation. A declined order must not change session totals. Clearly document this extension; instructor automated inputs target the core workflow and will need adjustment for the extra prompt.
