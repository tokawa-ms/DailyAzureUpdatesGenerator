# 2025年07月24日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年07月24日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Generally Available: Azure Managed Lustre now supports VNet Encryption for in-transit data protection

**公開日時**: 2025年07月23日 14:45:55 UTC
**リンク**: [Generally Available: Azure Managed Lustre now supports VNet Encryption for in-transit data protection](https://azure.microsoft.com/updates?id=498993)

**アップデートID**: 498993
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Managed Lustre, Security, Features

**要約**:

- 何が更新されたか  
Azure Managed LustreがVNet Encryptionをサポートし、データ転送時の暗号化が可能に。

- 主な変更点や新機能  
Azure Managed LustreとクライアントVM間の通信が仮想ネットワーク内で暗号化され、データの機密性とコンプライアンス要件を強化。

- 影響を受ける対象  
Azure Managed Lustreを利用するユーザーおよびデータ転送のセキュリティ強化を求める組織。

- 注意点があれば記載  
VNet Encryptionの有効化により、ネットワークパフォーマンスや設定に影響が出る可能性があるため、事前検証を推奨。

**詳細**:

Azure Managed Lustreは、高性能ファイルシステムをクラウド上で提供するサービスであり、今回のアップデートによりVNet Encryption（仮想ネットワーク内通信の暗号化）をサポートしました。これにより、Managed LustreとクライアントVM間のデータ転送時にTLSベースの暗号化が適用され、データの機密性を強化し、規制遵守要件（例：GDPR、HIPAA）に対応可能となります。技術的には、Azureの仮想ネットワーク内での通信経路に対し自動的に暗号化が有効化され、追加の設定はAzureポータルまたはCLIからManaged LustreのVNet Encryptionオプションを有効にするだけで完了します。これにより、ネットワーク層での盗聴リスクを低減し、特に金融、医療、政府機関など高いセキュリティ要件を持つ環境での利用が推奨されます。注意点としては、VNet EncryptionはAzure Managed Lustreと同一VNetまたはピアリング済みVNet内の通信に限定され、パブリックネットワーク経由の通信は対象外です。また、暗号化に伴う若干のレイテンシ増加が発生する可能性があります。関連サービスとしては、Azure Virtual Network、Azure Private Link、Azure Active Directoryと連携し、セキュアかつ認証されたアクセス管理が可能です。これにより、クラウド上の高性能ファイルストレージのセキュリティ強化とコンプライアンス対応が一層進展します。

---

### 2. Generally Available: Search Job Enhancements in Log Analytics 

**公開日時**: 2025年07月23日 06:30:03 UTC
**リンク**: [Generally Available: Search Job Enhancements in Log Analytics ](https://azure.microsoft.com/updates?id=498462)

**アップデートID**: 498462
**情報源**: Azure Updates API

**カテゴリ**: Launched, DevOps, Management and governance, Azure Monitor, Features

**要約**:

- 何が更新されたか  
Log AnalyticsのSearch Job機能がGA（一般提供）となり、非同期クエリの実行と結果の新Analyticsテーブルへの保存が可能に。

- 主な変更点や新機能  
長期保持データも含む任意のデータに対し非同期検索が可能。結果はワークスペース内の新しいテーブルで再利用でき、効率的な後続クエリが実現。

- 影響を受ける対象  
Log Analyticsを利用するAzure監視・分析の技術者や運用チーム。

- 注意点があれば記載  
非同期処理のためクエリ完了まで待機が不要だが、結果の反映タイミングに留意が必要。

**詳細**:

Azure Log Analyticsの「Search Job」機能がGA（一般提供）となりました。Search Jobは、Log Analyticsワークスペース内のデータ全体（長期保持データも含む）に対して非同期クエリを実行し、その結果を新たなAnalyticsテーブルとして保存可能にする機能です。これにより、大量データの長時間クエリを効率化し、結果を再利用した二次分析が容易になります。実装はKustoクエリをベースにし、非同期処理で負荷分散を図りつつ、結果テーブルは既存のKustoテーブルと同様に扱えます。活用例としては、長期保持データのトレンド分析やセキュリティインシデントの詳細調査などが挙げられます。注意点としては、結果テーブルのストレージコストやクエリ実行時間に留意が必要です。また、Azure MonitorやAzure Sentinelと連携し、検出ルールやアラートの高度化に活用可能です。詳細は公式リンク参照ください。

---


*このレポートは自動生成されました - 2025-07-24 12:01:05 JST*