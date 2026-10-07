# Digital Employee Development Sandbox

This repository is a deliberately small target for end-to-end tests of the Digital Employee development team.

## Behavioural contract

`calculate_reference_value(base_amount, adjustment_percent)` returns a reference value after applying a percentage adjustment.

Required behaviour:

- positive adjustments increase the value;
- `-100%` reduces the value to exactly zero;
- an adjustment below `-100%` must **never produce a negative reference value** — the result must be clamped to `0.0`;
- the returned value is rounded to two decimal places.

## Known defect

The current implementation does not satisfy the contract for adjustments below `-100%`.

For example:

```python
calculate_reference_value(100.0, -150.0)
```

must return:

```text
0.0
```

The existing tests intentionally do not cover this defect yet.

## Development task

Fix the documented defect in `reference_value.py`, add a regression test that demonstrates the required edge-case behaviour, and verify the change with the repository's `verify.yml` workflow.

Do not merge or release anything as part of the task.
