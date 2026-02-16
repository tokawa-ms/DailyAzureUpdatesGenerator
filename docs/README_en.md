# Documentation Directory

This directory contains design and operational documentation for Daily Azure Updates Generator.

## Document List

- [Detailed Design (detailed-design_en.md)](./detailed-design_en.md)
  - English design summary for the current implementation.
- [詳細設計書 (detailed-design.md)](./detailed-design.md)
  - Full Japanese detailed design document.

## Related Documents

- [README.md](../README.md) - Japanese usage guide
- [README_EN.md](../README_EN.md) - English usage guide
- [dailycheck.yaml](../.github/workflows/dailycheck.yaml) - Production GitHub Actions workflow

## Update History

| Date       | Version | Description                                                                          | Author  |
| ---------- | ------- | ------------------------------------------------------------------------------------ | ------- |
| 2026-02-16 | 1.1     | Updated to match current implementation (mid scripts, backfill, repository_dispatch) | Copilot |
| 2026-02-15 | 1.0     | Initial English docs and authentication updates                                      | Copilot |

## Maintenance Policy

- Update README and design docs in the same PR whenever behavior changes.
- Reflect CLI option changes in usage examples immediately.
- Reflect workflow trigger/secret/order changes in design documentation.
