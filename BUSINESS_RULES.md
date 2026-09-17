# Stable business rules — all stages

## Inputs
- Menu: `1` places an order, `2` shows the session summary, `0` exits. Other choices print an error and redisplay the menu.
- Pages per copy: a whole number from 1 to 500, inclusive.
- Copies: a whole number from 1 to 100, inclusive.
- Print mode: `B` for black-and-white or `C` for colour. Accept upper- or lowercase.
- Binding: `Y` or `N`. Accept upper- or lowercase.
- Retry an invalid field; do not restart the entire order.

For stages 1–5, assume that numeric prompts receive valid integer text (possibly out of range). Recovering from `abc`, `2.5` or an empty numeric response is explicitly stage 6 work. Menu, mode and binding always require choice validation. No cancellation partway through an order is required.

## Pricing
| Item | Rule |
|---|---|
| Black-and-white | KES 10 per printed page |
| Colour | KES 30 per printed page |
| Printed pages | pages per copy × number of copies |
| Bulk discount | 10% of printing subtotal when printed pages ≥ 100 |
| Binding | KES 50 per copy when selected |
| Total | printing subtotal − discount + binding charge |

The discount never applies to binding. All tariffs make the discount a whole shilling, so use integer arithmetic: `printing_subtotal // 10`. Do not round a percentage on another tariff without revisiting the money representation. All pages are charged alike; duplex printing, tax and payment processing are out of scope.

## Outputs and state
After a completed order show `Printed pages: N`, `Printing: KES N`, `Discount: KES N`, `Binding: KES N`, and `Total: KES N` on separate lines. Print one label per copy as `Copy i of n`. Increment the completed-order count, accumulate printed pages and add the total exactly once. Invalid attempts must not change these accumulators.

The summary contains `Orders: N`, `Pages: N`, and `Revenue: KES N`. “Revenue” in this teaching project means the sum of accepted order totals, not verified payments. A summary is read-only. Exiting must display the final summary. Stages 1–4 reset everything on restart; stage 5 adds a separate persistent ledger while keeping session totals.
