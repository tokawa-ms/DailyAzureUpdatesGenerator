# 2025年07月22日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年07月22日
**対象期間**: 過去 100 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Generally Available:  Azure Firewall now supports ingestion-time transformation in Log Analytics for flexible, cost-efficient logging

**公開日時**: 2025年07月18日 16:45:08 UTC
**リンク**: [Generally Available:  Azure Firewall now supports ingestion-time transformation in Log Analytics for flexible, cost-efficient logging](https://azure.microsoft.com/updates?id=498568)

**アップデートID**: 498568
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Azure Firewall, Features, Services

**要約**:

- 何が更新されたか  
Azure FirewallがLog Analyticsでのログ取り込み時変換（ingestion-time transformation）を正式サポート開始。

- 主な変更点や新機能  
ログの選択的記録や高度なフィルタリングが可能になり、不要なログの取り込みを削減しコスト効率を向上。

- 影響を受ける対象  
Azure FirewallのログをLog Analyticsで分析・管理している技術者や運用チーム。

- 注意点があれば記載  
設定ミスによる重要ログの取り込み漏れに注意し、フィルタリングポリシーを適切に設計する必要あり。

**詳細**:

今回のアップデートにより、Azure FirewallのログをLog Analyticsへ送信する際に「ingestion-time transformation（取り込み時変換）」が可能になりました。これにより、ログの一部のみを選択的に取り込み、不要なデータを除外できるため、ログの保存コストとクエリコストを大幅に削減できます。

具体的には、Log AnalyticsのData Collection Rules（DCR）を用いて、Azure Firewallの診断ログをフィルタリング・変換し、必要なフィールドだけを抽出・加工して取り込みます。これにより、膨大なログの中から重要な情報だけを効率的に分析可能です。

実装はAzure PortalやAzure CLIでDCRを作成し、Azure Firewallの診断設定に適用します。例えば、特定のアクション（許可・拒否）やIPアドレス範囲のログのみを収集する設定が可能です。

活用例としては、セキュリティ監査で重要な通信のみを抽出し、コストを抑えつつ迅速なインシデント対応を実現できます。一方、変換ルールの誤設定によるログ欠落リスクや、DCRの複雑化に注意が必要です。

本機能はAzure Monitor、Log Analytics、Azure Firewallの連携強化であり、セキュリティ運用の効率化とコスト最適化に寄与します。

---


*このレポートは自動生成されました - 2025-07-22 10:58:25 JST*