# 2025年12月04日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年12月04日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 6 件

## 更新一覧

### 1. Retirement: Remove dependency on these Azure ML SDKs before June 30, 2026

**公開日時**: 2025年12月03日 21:00:12 UTC
**リンク**: [Retirement: Remove dependency on these Azure ML SDKs before June 30, 2026](https://azure.microsoft.com/updates?id=501668)

**アップデートID**: 501668
**情報源**: Azure Updates API

**カテゴリ**: AI + machine learning, Internet of Things, Azure Machine Learning, Retirements, Features

**要約**:

- 何が更新されたか  
AzureML SDK V1および関連SDK（azureml-train-core、azureml-pipeline等）が2026年6月30日にサポート終了となる。

- 主な変更点や新機能  
これらのSDKは廃止され、以降はAzureML SDK V2への移行が推奨される。

- 影響を受ける対象  
AzureML SDK V1を利用している開発者やシステム。

- 注意点  
サポート終了後はセキュリティ更新やサポートが受けられなくなるため、早期のSDK移行計画が必要。

**詳細**:

本アップデートは、Azure Machine Learning SDK V1および連携SDK群（azureml-train-core、azureml-pipeline、azureml-pipeline-core、azureml-pipeline-internal、azureml-pipeline-steps）が2026年6月30日にサポート終了（EOL）となるため、これらへの依存を段階的に除去することを目的としています。SDK V1は旧来のAPI設計であり、最新のAzureML SDK V2ではよりモジュール化・効率化されたパイプライン構築やトレーニング管理が可能です。具体的には、V1のパイプライン定義やステップ管理機能が廃止され、V2の新しいPython SDKを用いたMLワークフローの構築へ移行が推奨されます。技術的には、V2 SDKはREST APIベースで設計されており、より柔軟かつ拡張性の高い実装が可能です。活用シナリオとしては、モデルのトレーニング、評価、デプロイまでの一連のMLパイプラインをコードベースで管理し、AzureML StudioやCLIと連携して運用自動化を実現します。注意点としては、既存のV1 SDKベースのコードは2026年6月以降動作保証がなくなるため、早期のコード改修とテストが必須です。また、V2 SDKは一部API仕様が異なるため、移行時にAPIリファクタリングが必要です。関連サービスとしては、AzureMLパイプラインはAzure DevOpsやGitHub Actionsと連携しCI/CDパイプライン構築が可能であり、Azure Blob StorageやAzure Key Vaultとの統合も引き続きサポートされます。詳細は公式ドキュメントを参照し、段階的な移行計画を策定してください。  
https://azure.microsoft.com/updates?id=501668

---

### 2. Generally Available: Azure Database for PostgreSQL Flexible Server in Belgium Central 

**公開日時**: 2025年12月03日 17:30:15 UTC
**リンク**: [Generally Available: Azure Database for PostgreSQL Flexible Server in Belgium Central ](https://azure.microsoft.com/updates?id=534523)

**アップデートID**: 534523
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible ServerがBelgium Centralリージョンで一般提供開始。

- 主な変更点や新機能  
新リージョン追加により、低遅延かつ地域的に近い環境でのデータベース展開が可能に。

- 影響を受ける対象  
欧州地域のユーザーやアプリケーションで、PostgreSQL Flexible Serverを利用する技術者。

- 注意点があれば記載  
既存リージョンからの移行やデータレプリケーション設計時にリージョン特性を考慮する必要あり。

**詳細**:

本アップデートにより、Azure Database for PostgreSQL Flexible Serverがベルギー中央（Belgium Central）リージョンで一般提供（GA）開始されました。背景には、欧州地域のデータ主権要件や低遅延アクセスのニーズに応えるため、地域拡充による柔軟なサーバー配置が求められたことがあります。Flexible Serverは、シングルサーバーに比べて高い可用性、スケーラビリティ、メンテナンス制御を提供し、カスタマイズ可能なバックアップやフェイルオーバー設定が可能です。ベルギー中央リージョンでの展開により、現地法規制に準拠したデータ管理が可能となり、ネットワーク遅延の低減も期待できます。実装はAzureポータル、CLI、ARMテンプレートを通じて行い、VNet統合やプライベートエンドポイント設定もサポートされるため、セキュアな環境構築が可能です。活用シナリオとしては、欧州内の金融、ヘルスケア、製造業など、データ主権と高可用性を重視するアプリケーションに最適です。注意点として、リージョン固有のリソース制限やサービスのバージョン対応状況を事前に確認する必要があります。関連サービスとしては、Azure Monitorによるパフォーマンス監視、Azure Backupとの連携、Azure Private Linkによるセキュア接続が挙げられます。これにより、ベルギー中央リージョンにおけるPostgreSQL環境の運用効率とセキュリティが大幅に向上します。

---

### 3. Generally Available: Update pg_squeeze to version 1.9.1 in Azure Database for PostgreSQL Flexible Server 

**公開日時**: 2025年12月03日 17:30:15 UTC
**リンク**: [Generally Available: Update pg_squeeze to version 1.9.1 in Azure Database for PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=534518)

**アップデートID**: 534518
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverでpg_squeeze拡張機能がバージョン1.9.1にアップデート可能になりました。

- 主な変更点や新機能  
pg_squeeze 1.9.1では、テーブルの断片化解消とストレージ効率改善が強化され、パフォーマンス最適化が期待できます。

- 影響を受ける対象  
Azure Database for PostgreSQL Flexible Serverを利用し、pg_squeeze拡張を使用している技術者や運用担当者。

- 注意点があれば記載  
アップグレード前にバックアップを推奨。互換性や既存の運用スクリプトへの影響を事前に検証してください。

**詳細**:

Azure Database for PostgreSQL Flexible Serverにおいて、pg_squeeze拡張機能がバージョン1.9.1にアップデートされ、一般提供（GA）されました。pg_squeezeはPostgreSQLのテーブルやインデックスの断片化を解消し、ディスク使用量削減とパフォーマンス向上を目的とした拡張機能です。バージョン1.9.1では、VACUUM FULLに近い効果をより低負荷で実現可能となり、オンライン環境でのメンテナンス効率が向上しています。実装はSQL関数として提供され、ALTER EXTENSIONコマンドで簡単にアップグレード可能です。活用シナリオとしては、大規模データベースの断片化解消や定期メンテナンス自動化が挙げられ、Flexible Serverのスケーラビリティと組み合わせることで運用負荷を軽減します。注意点として、アップデート適用時は事前にバックアップを推奨し、特定のPostgreSQLバージョンとの互換性を確認する必要があります。Azure MonitorやAzure Automationと連携することで、メンテナンスジョブの監視・自動化が可能です。詳細は公式ドキュメントを参照してください。

---

### 4. Generally Available: The ip4r extension in Azure Database for PostgreSQL Flexible Server 

**公開日時**: 2025年12月03日 17:30:15 UTC
**リンク**: [Generally Available: The ip4r extension in Azure Database for PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=534509)

**アップデートID**: 534509
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverでip4r拡張機能がGA（一般提供）となりました。

- 主な変更点や新機能  
ip4rはIPv4/IPv6アドレスおよび範囲の効率的な格納とインデックス作成をサポートします。

- 影響を受ける対象  
PostgreSQL Flexible Serverを利用し、IPアドレス関連のデータ管理を行う技術者。

- 注意点があれば記載  
利用前に拡張機能のインストールが必要です。既存のIPデータ構造との互換性を確認してください。

**詳細**:

本アップデートにより、Azure Database for PostgreSQL Flexible Serverでip4r拡張機能がGA（一般提供）されました。ip4rはIPv4およびIPv6アドレスやアドレスレンジの効率的な格納・インデックス作成を可能にするPostgreSQL拡張で、ネットワーク関連データの高速検索や範囲クエリを実現します。導入はFlexible Serverの拡張管理画面またはSQLコマンド（CREATE EXTENSION ip4r;）で行い、B-treeやGiSTインデックスを活用した高速な検索性能を得られます。主な活用シナリオはIPアドレスベースのアクセス制御、ログ解析、ネットワーク監視システムなどで、複雑なIP範囲のクエリを簡潔に記述可能です。注意点としては、拡張の利用にはFlexible Serverのバージョン対応が必要であり、拡張機能の管理権限が必要です。また、Azure MonitorやAzure Network Watcherと組み合わせることで、IP情報を活用した高度な分析やアラート設定が可能となります。今回の対応により、Azure上でのネットワークデータ処理がより効率化されるため、IPアドレス関連のアプリケーション開発において有用です。

---

### 5. Generally Available: The credcheck extension in Azure Database for PostgreSQL Flexible Server 

**公開日時**: 2025年12月03日 17:30:15 UTC
**リンク**: [Generally Available: The credcheck extension in Azure Database for PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=534504)

**アップデートID**: 534504
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverでcredcheck拡張機能がGA（一般提供）となりました。

- 主な変更点や新機能  
credcheck拡張により、PostgreSQL内で直接パスワードや認証情報の検証ポリシーを適用可能に。

- 影響を受ける対象  
Azure Database for PostgreSQL Flexible Serverを利用する開発者・運用者。

- 注意点があれば記載  
ポリシー設定は適切に管理しないと認証エラーが発生する可能性があるため、導入前に検証推奨。

**詳細**:

本アップデートにより、Azure Database for PostgreSQL Flexible Serverでcredcheck拡張機能がGA（一般提供）されました。credcheckはPostgreSQL内で直接パスワードや認証情報の検証ポリシーを強制する拡張機能で、セキュリティ強化を目的としています。具体的には、パスワードの複雑性や長さ、履歴管理などのポリシーを設定可能で、不適切な認証情報の登録を防止します。実装はPostgreSQLの拡張機能としてインストールし、SQLコマンドでポリシーを定義・適用します。活用例としては、企業のセキュリティ基準に準拠したパスワード管理や、コンプライアンス対応が挙げられます。注意点として、既存の認証方式との互換性確認や、ポリシー設定の過度な制限によるユーザビリティ低下に留意が必要です。Azure MonitorやAzure Policyと連携することで、監査ログ収集やポリシー遵守状況の管理が可能となり、運用効率の向上に寄与します。詳細は公式ドキュメントを参照してください。

---

### 6. Generally Available: Azure Load Balancer bandwidth metrics now support Protocol dimension

**公開日時**: 2025年12月03日 17:00:27 UTC
**リンク**: [Generally Available: Azure Load Balancer bandwidth metrics now support Protocol dimension](https://azure.microsoft.com/updates?id=536747)

**アップデートID**: 536747
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Load Balancer

**要約**:

- 何が更新されたか  
Azure Load Balancerの帯域幅メトリックに「Protocol」ディメンションが追加され、TCPなどプロトコル別のトラフィック解析が可能に。

- 主な変更点や新機能  
Byte、Packet、SYN Countの各メトリックでプロトコル（例：TCPはProtocol=6）ごとの詳細な監視がAzureポータルで可能。

- 影響を受ける対象  
Azure Load Balancerを利用し、トラフィックの詳細分析や監視を行う技術者・運用者。

- 注意点があれば記載  
既存のメトリック取得APIにProtocolディメンションが追加されたため、メトリック取得クエリの更新が必要になる場合がある。

**詳細**:

本アップデートにより、Azure Load Balancerの帯域幅（Bandwidth）メトリクスに「Protocol」ディメンションが正式対応しました。これまではByte数やパケット数、SYNカウントがプロトコル別に区分されず集計されていましたが、今回の対応でTCP（Protocol=6）やUDPなどのプロトコル単位でのトラフィック解析が可能となり、詳細な通信状況の把握が容易になります。AzureポータルやAzure Monitor APIでメトリクスを取得する際に、Protocolディメンションを指定することで、プロトコル別のトラフィック量を可視化・監視可能です。実装はLoad Balancerの内部トラフィック解析機構がパケットヘッダのプロトコル番号を識別し、メトリクスに付与する形で行われています。これにより、TCP/UDP混在環境での負荷分散性能評価や異常検知、セキュリティ監査が精緻化されます。注意点として、Protocolディメンションは現時点で主要プロトコルに限定されており、全プロトコルの網羅はされていません。また、メトリクスの遅延や集計粒度は既存のLoad Balancerメトリクスと同様です。Azure MonitorやLog Analyticsと連携することで、アラート設定やダッシュボード作成に活用でき、Application GatewayやNetwork Watcherなど他のネットワーク監視サービスとの統合分析も可能です。詳細は公式ドキュメントおよび更新情報を参照してください。

---


*このレポートは自動生成されました - 2025-12-04 12:02:06 JST*