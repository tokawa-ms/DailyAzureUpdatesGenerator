# 2025年09月09日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月09日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Retirement: Operating System (OS) Disks on Standard HDD will be retired on 08 September 2028 

**公開日時**: 2025年09月08日 21:00:36 UTC
**リンク**: [Retirement: Operating System (OS) Disks on Standard HDD will be retired on 08 September 2028 ](https://azure.microsoft.com/updates?id=500157)

**アップデートID**: 500157
**情報源**: Azure Updates API

**カテゴリ**: Storage, Azure Disk Storage, Retirements

**要約**:

- 何が更新されたか  
Azureの標準HDDを使用したOSディスクが2028年9月8日に廃止されることが発表されました。

- 主な変更点や新機能  
標準HDDのOSディスクは廃止され、今後はパフォーマンス向上を目的としたSSDなどのディスク利用が推奨されます。

- 影響を受ける対象  
標準HDDのOSディスクを利用している仮想マシンやサービスが対象です。

- 注意点があれば記載  
廃止までにディスクの種類変更や移行計画を立てる必要があります。パフォーマンス要件に応じたディスク選択を検討してください。

**詳細**:

本アップデートは、2028年9月8日をもってStandard HDDを用いたOSディスクの提供を終了することを発表しています。背景には、顧客の利用動向の変化とディスク性能向上への投資を最適化する狙いがあります。具体的には、従来のStandard HDD OSディスクは性能面でSSD系ディスク（Standard SSDやPremium SSD）に劣るため、より高速かつ信頼性の高いストレージへの移行を促進します。技術的には、OSディスクのストレージアカウントをStandard HDDからSSDベースに切り替えることで、I/O性能やスループットが大幅に向上します。活用シナリオとしては、仮想マシンの起動速度やアプリケーションの応答性を重視する環境でのSSD利用が推奨されます。注意点として、移行前に既存VMのOSディスクのバックアップやスナップショット取得を行い、互換性やコスト増加の影響を評価する必要があります。関連サービスとしては、Azure VM、Managed Disks、Azure Backupが連携し、移行作業や運用管理を支援します。今後はSSD系OSディスクへの移行計画を早期に策定し、パフォーマンス向上と運用安定化を図ることが重要です。詳細は公式リンクを参照してください。

---

### 2. Public Preview: Graph Query Language (GQL) in KQL graph semantics

**公開日時**: 2025年09月08日 12:00:02 UTC
**リンク**: [Public Preview: Graph Query Language (GQL) in KQL graph semantics](https://azure.microsoft.com/updates?id=502638)

**アップデートID**: 502638
**情報源**: Azure Updates API

**カテゴリ**: In preview, Analytics, Azure Data Explorer, Microsoft Fabric, Features

**要約**:

- 何が更新されたか  
KQLのグラフセマンティクスにISO標準準拠のGraph Query Language（GQL）サポートがパブリックプレビューで追加されました。

- 主な変更点や新機能  
Fabric EventhouseやAzure Data Explorer上でGQLクエリを実行可能となり、標準化された言語でグラフデータの操作が容易になります。

- 影響を受ける対象  
グラフデータを扱うAzure Data ExplorerやFabric Eventhouseのユーザー、KQLを利用する技術者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

本アップデートは、Kusto Query Language（KQL）のグラフセマンティクスにISO標準のGraph Query Language（GQL）サポートを追加し、グラフデータ操作の標準化と利便性向上を目的としています。これにより、Azure Data ExplorerやFabric Eventhouse上でGQLクエリを直接実行可能となり、複雑なグラフ構造の探索や分析が容易になります。技術的には、KQLのグラフ拡張にGQLパーサーを統合し、ノード・エッジの定義やパターンマッチングをISO準拠の構文で記述可能です。活用例としては、ソーシャルネットワーク分析、サプライチェーンの依存関係解析、セキュリティログの攻撃パス追跡などが挙げられます。注意点としては、現状プレビュー段階のため一部GQL機能が未対応であり、パフォーマンス最適化や拡張機能は今後のアップデートを要確認です。Azure Data ExplorerのスケーラビリティやFabric Eventhouseのリアルタイムデータ取り込み機能と連携し、大規模グラフ解析基盤の構築が可能です。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2025-09-09 12:01:09 JST*