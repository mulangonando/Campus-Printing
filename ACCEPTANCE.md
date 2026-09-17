# Acceptance scenarios
Run each numbered scenario from a fresh program unless explicitly told to continue. Inputs below are entered one line at a time. Check numeric results; prompt wording can vary. Use the receipt and summary labels in BUSINESS_RULES.md for compatibility with instructor checks.

| # | Input sequence | Expected result |
|---|---|---|
| 1 | `2, 0` | Both summaries show 0 orders, 0 pages, KES 0 |
| 2 | `1, 2, 3, B, N, 0` | Pages 6; printing 60; discount 0; binding 0; total 60; exactly 3 labels |
| 3 | `1, 99, 1, B, N, 0` | Printing 990; discount 0; total 990 |
| 4 | `1, 100, 1, B, N, 0` | Printing 1000; discount 100; total 900 |
| 5 | `1, 25, 4, B, Y, 0` | Pages 100; printing 1000; discount 100; binding 200; total 1100 |
| 6 | `1, 10, 2, c, y, 0` | Printing 600; discount 0; binding 100; total 700 |
| 7 | `1, 500, 100, C, Y, 0` | Pages 50000; printing 1500000; discount 150000; binding 5000; total 1355000 |
| 8 | `1, 0, 501, 1, 0, 101, 1, X, b, X, n, 0` | Each invalid field retried; one order, one page, total 10; one label |
| 9 | `9, 2, 0` | Invalid menu choice reported; no order created; zero summary |
| 10 | `1, 2, 3, B, N, 1, 25, 4, B, Y, 2, 2, 0` | Both orders processed; every summary shows 2 orders, 106 pages, KES 1160 |

Commas separate successive keyboard entries; do not type the commas. Stage 1 intentionally assumes integer text at numeric prompts. Do not report a crash on `abc` as a missing stage 1 requirement: recovery from this input is a later assignment.
