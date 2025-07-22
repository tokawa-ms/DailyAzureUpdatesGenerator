# 2025 年 07 月 19 日 - Azure Updates 要約レポート

**生成日時**: 2025 年 07 月 19 日
**対象期間**: 過去 24 時間以内
**更新件数**: 1 件

## 更新一覧

### 1. Generally Available: Azure Firewall now supports ingestion-time transformation in Log Analytics for flexible, cost-efficient logging

**公開日時**: 2025 年 07 月 18 日 16:45:08 UTC
**リンク**: [Generally Available: Azure Firewall now supports ingestion-time transformation in Log Analytics for flexible, cost-efficient logging](https://azure.microsoft.com/updates?id=498568)

**アップデート ID**: 498568
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Azure Firewall, Features, Services

**要約**:

- 何が更新されたか  
  Azure Firewall が Log Analytics でのログ取り込み時変換（ingestion-time transformation）を正式サポート。

- 主な変更点や新機能  
  ログの選択的記録や高度なフィルタリングが可能になり、不要なログの取り込みを削減しコスト効率を向上。

- 影響を受ける対象  
  Azure Firewall のログを Log Analytics で分析・管理する技術者や運用チーム。

- 注意点があれば記載  
  設定ミスにより必要なログが除外されるリスクがあるため、変換ルールの設計・検証が重要。

**詳細**:

本アップデートにより、Azure Firewall のログが Log Analytics へ取り込まれる際に「ingestion-time transformation（取り込み時変換）」が正式対応となりました。これにより、ログの選択的抽出や高度なフィルタリングが可能となり、不要なログデータの取り込みを抑制し、コスト効率の向上を実現します。具体的には、Kusto Query Language（KQL）を用いた変換ルールを設定し、必要なフィールドの抽出や条件に基づくログの除外を行うことができます。技術的には、Log Analytics の Data Collection Rule（DCR）に変換ポリシーを組み込み、Azure Firewall の診断設定と連携させる形で実装します。活用例としては、大量のトラフィックログから特定の IP アドレスやポート番号に関連するイベントのみを抽出し、分析負荷とストレージコストを削減するケースが挙げられます。注意点として、変換ルールの誤設定により必要なログが欠落するリスクがあるため、十分なテストが推奨されます。また、変換機能は Log Analytics の DCR 対応リージョンでのみ利用可能です。関連サービスとしては、Azure Monitor、Azure Sentinel との連携が強化され、効率的なセキュリティ監視やインシデント対応に寄与します。

---

_このレポートは自動生成されました - 2025-07-19 15:44:52 JST_
