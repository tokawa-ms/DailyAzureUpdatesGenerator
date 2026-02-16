# ドキュメント ディレクトリ

このディレクトリには、Daily Azure Updates Generator の設計・運用ドキュメントを格納しています。

## 文書一覧

- [詳細設計書 (detailed-design.md)](./detailed-design.md)
  - 日本語の詳細設計。`getlatestupdate_mid.py` / `getlatestupdate_en_mid.py`、`repository_dispatch` ワークフロー、`--details` / `--backfill-*` の挙動を記載。
- [Detailed Design (detailed-design_en.md)](./detailed-design_en.md)
  - English technical design summary for the current implementation.

## 関連文書

- [README.md](../README.md) - 日本語の利用手順
- [README_EN.md](../README_EN.md) - English usage guide
- [dailycheck.yaml](../.github/workflows/dailycheck.yaml) - 実運用の GitHub Actions ワークフロー

## 更新履歴

| 日付       | バージョン | 更新内容                                                       | 更新者  |
| ---------- | ---------- | -------------------------------------------------------------- | ------- |
| 2026-02-16 | 1.2        | 現行実装（mid版・backfill・repository_dispatch）に合わせて更新 | Copilot |
| 2026-02-15 | 1.1        | 認証方式更新・英語版文書追加                                   | Copilot |
| 2025-07-22 | 1.0        | 初版作成                                                       | Bot     |

## メンテナンス方針

- 実装変更時は README と詳細設計書を同一PRで更新する。
- コマンドライン引数の追加・変更時は利用例を README に反映する。
- ワークフロー変更時はトリガー/シークレット/実行順序を設計書へ反映する。
