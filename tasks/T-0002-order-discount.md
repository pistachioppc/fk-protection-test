+++
id = "T-0002"
title = "Order discount"
status = "review"
owner = "claude"
reviewer = "codex"
created = 2026-11-16
updated = 2026-11-16
branch = "task/T-0002-discount"
pr = 4
+++

## Why
fk review live run (ticket 08): a small change with a planted bug.

## Definition of done
- [ ] `total_with_discount(amounts, percent)` takes `percent` off the total, rounded to cents
- [ ] A discount above 100 % is refused with ValueError

## Notes

## Evidence
