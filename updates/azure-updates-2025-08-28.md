# 2025年08月28日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年08月28日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Public Preview: Azure SQL updates for late-August 2025 

**公開日時**: 2025年08月27日 16:00:53 UTC
**リンク**: [Public Preview: Azure SQL updates for late-August 2025 ](https://azure.microsoft.com/updates?id=500780)

**アップデートID**: 500780
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

- 何が更新されたか  
Azure SQL Databaseにレプリケーション遅延メトリックが追加されました。

- 主な変更点や新機能  
Geo-DR有効時のRPO（復旧時点目標）をリアルタイムで監視可能に。運用上の可視性が向上します。

- 影響を受ける対象  
Geo-DR構成でAzure SQL Databaseを利用する技術者や運用チーム。

- 注意点があれば記載  
プレビュー機能のため、本番環境での利用は慎重に検討してください。

情報源: https://azure.microsoft.com/updates?id=500780

**詳細**:

2025年8月下旬にAzure SQL Databaseのパブリックプレビューとして、Geo-DR（地理的災害復旧）機能利用時のレプリケーション遅延を示す「レプリケーションラグ」メトリックが追加されました。これにより、リアルタイムで復旧時点目標（RPO）の達成状況を可視化可能となり、災害発生時のデータ損失リスクを定量的に把握できます。技術的には、プライマリとセカンダリ間のトランザクション適用遅延を監視し、Azure MonitorやAzure Metrics Explorerで参照可能なメトリックとして提供されます。これにより、運用担当者はGeo-DR構成の健全性を継続的に評価し、必要に応じてフェイルオーバー判断を迅速化できます。活用例としては、ミッションクリティカルなグローバルサービスでの災害復旧計画の最適化や、SLA遵守のための監視強化が挙げられます。注意点としては、現時点でプレビュー機能であるため、商用環境での利用は慎重に行い、Azure SQLのバージョンやリージョンによる対応状況を確認する必要があります。また、Azure Monitorとの連携により、アラート設定やダッシュボード統合が可能で、Azure Site Recoveryなど他のDR関連サービスとの組み合わせで運用効率を高められます。詳細は公式ドキュメントを参照してください。  
https://azure.microsoft.com/updates?id=500780

---

### 2. Generally Available: Schema migration is now available in Azure Database Migration Service (DMS) 

**公開日時**: 2025年08月27日 16:00:53 UTC
**リンク**: [Generally Available: Schema migration is now available in Azure Database Migration Service (DMS) ](https://azure.microsoft.com/updates?id=500770)

**アップデートID**: 500770
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Migration, Azure Database Migration Service, Features

**要約**:

- 何が更新されたか  
Azure Database Migration Service（DMS）でスキーマ移行機能が一般提供開始。

- 主な変更点や新機能  
Azure SQL Databaseへの移行時に、データと共に不足しているスキーマオブジェクトをワンクリックで同時移行可能に。

- 影響を受ける対象  
Azure SQL Databaseへのデータベース移行を行う技術者や運用チーム。

- 注意点があれば記載  
複雑なスキーマ依存関係がある場合は事前検証が推奨される。

**詳細**:

Azure Database Migration Service（DMS）がスキーマ移行機能をGA（一般提供）しました。本アップデートは、Azure SQL Databaseへの移行時にスキーマオブジェクト（テーブル定義、インデックス、制約など）が不足している場合でも、データ移行と同時にこれらを自動的に作成可能とすることで、移行作業の効率化と信頼性向上を目的としています。具体的には、DMSの移行プロジェクト設定に「スキーマ移行」オプションが追加され、チェックボックスを有効化するだけでスキーマの差分検出と適用が行われます。技術的には、DMSがソースデータベースのスキーマ情報を解析し、ターゲットのAzure SQL Databaseに存在しないオブジェクトを生成するスクリプトを自動生成・実行します。これにより、手動でのスキーマ準備作業が不要となり、移行の自動化が促進されます。活用シナリオとしては、オンプレミスSQL Serverや他クラウドのSQLデータベースからAzure SQL Databaseへのリフト＆シフト移行で、スキーマ整合性を保ちながら迅速に移行を完了させたい場合に有効です。注意点としては、複雑なストアドプロシージャやトリガーの移行は別途対応が必要であり、完全な互換性保証はないため事前検証が推奨されます。Azure DMSはAzure MonitorやAzure Active Directoryと連携し、移行状況の監視やアクセス管理を強化可能です。詳細は公式アップデート（https://azure.microsoft.com/updates?id=500770）を参照してください。

---

### 3. Public Preview: Azure Cosmos DB for MongoDB (vCore)—add shards and rebalance data 

**公開日時**: 2025年08月27日 16:00:53 UTC
**リンク**: [Public Preview: Azure Cosmos DB for MongoDB (vCore)—add shards and rebalance data ](https://azure.microsoft.com/updates?id=500755)

**アップデートID**: 500755
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Internet of Things, Azure Cosmos DB, Features

**要約**:

- 何が更新されたか  
Azure Cosmos DB for MongoDB (vCore)で物理シャードの追加とデータのリバランスがパブリックプレビューで利用可能に。

- 主な変更点や新機能  
クラスターのスケールアウトが容易になり、シャード追加による性能向上とデータ分散の最適化が可能に。コンピュートとストレージの弾力的構成を活用。

- 影響を受ける対象  
Azure Cosmos DB for MongoDB (vCore)を利用する開発者・運用者。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に。シャード追加時のデータリバランスによる一時的なパフォーマンス変動に留意。

**詳細**:

本アップデートは、Azure Cosmos DB for MongoDB (vCore) クラスターのスケーラビリティ向上を目的に、物理シャードの追加とデータのリバランス機能をパブリックプレビューで提供開始したものです。従来はシャード数固定のため、クラスター拡張時に柔軟なスケールアウトが困難でしたが、本機能により増加するワークロードに応じて物理ノード単位でシャードを追加可能となり、計算リソースとストレージを効率的に拡張できます。実装面では、Azure Cosmos DBの分散アーキテクチャを活かし、新規シャード追加時に自動的にデータの再分散（リバランス）が行われ、クエリ性能とデータ整合性を維持します。活用例としては、IoTや大規模ログ収集などデータ増加が急激なシナリオで、ダウンタイムなしにスケールアウトが可能となり、運用負荷を軽減します。注意点としては、プレビュー機能のため一部制限や既存のシャード構成との互換性確認が必要であり、パフォーマンス監視を推奨します。関連サービスではAzure Monitorによるパフォーマンス監視やAzure Automationでのスケール管理と連携可能です。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2025-08-28 12:01:25 JST*