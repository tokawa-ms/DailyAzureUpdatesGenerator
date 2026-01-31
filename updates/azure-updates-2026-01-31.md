# 2026年01月31日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年01月31日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Retirement: "Send data to Event Hubs & Storage (Preview)" retiring July 31, 2026

**公開日時**: 2026年01月30日 18:30:02 UTC
**リンク**: [Retirement: "Send data to Event Hubs & Storage (Preview)" retiring July 31, 2026](https://azure.microsoft.com/updates?id=551523)

**アップデートID**: 551523
**情報源**: Azure Updates API

**カテゴリ**: DevOps, Management and governance, Azure Monitor

**要約**:

- 何が更新されたか  
「Send data to Event Hubs & Storage (Preview)」機能が2026年7月31日に廃止されます。

- 主な変更点や新機能  
新規のデータ収集ルール作成ができなくなり、Microsoftのサポートも終了します。

- 影響を受ける対象  
このプレビュー機能を利用している仮想マシンのデータ送信設定を行っている技術者や運用チーム。

- 注意点  
廃止後は代替手段への移行が必要です。既存の設定も継続利用できなくなるため、早めの対応を推奨します。

**詳細**:

本アップデートは、2026年7月31日をもって「Send virtual machine client data to Event Hubs and Storage (Preview)」機能のプレビュー版を廃止し、新規データ収集ルールの作成を停止するものです。本機能はAzure Monitorのデータ収集ルール（DCR）を通じて、仮想マシンの診断データをEvent HubsやAzure Storageに送信し、リアルタイム分析や長期保存を可能にしていました。技術的には、VMエージェントが収集データをDCRに基づきEvent Hubs/Storageへ転送し、イベント駆動型の監視や外部システム連携を実現していました。活用例としては、カスタム分析基盤へのログ統合や、ストリーム処理による異常検知が挙げられます。廃止に伴い、新規ルール作成不可となり既存ルールも将来的に非推奨となるため、Azure Monitorの標準データ収集機能やAzure Event Grid、Log Analyticsへの移行検討が必要です。関連サービスとしては、Azure Monitor、Event Hubs、Storageアカウント、Log Analyticsが密接に連携しており、移行時はこれらの設定見直しが重要です。

---


*このレポートは自動生成されました - 2026-01-31 12:01:08 JST*