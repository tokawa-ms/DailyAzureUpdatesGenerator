# 2025年09月18日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月18日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Public Preview: Azure Functions .NET 10 support 

**公開日時**: 2025年09月17日 17:15:04 UTC
**リンク**: [Public Preview: Azure Functions .NET 10 support ](https://azure.microsoft.com/updates?id=503134)

**アップデートID**: 503134
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Internet of Things, Azure Functions, Features

**要約**:

- 何が更新されたか  
Azure Functionsが.NET 10をパブリックプレビューでサポート開始。

- 主な変更点や新機能  
Functionsプロジェクトのターゲットフレームワークを.NET 10に変更し、Microsoft.Azure.Functions.Worker.Sdkを2.0.5以降に更新する必要あり。これにより.NET 10環境でのデプロイが可能に。

- 影響を受ける対象  
Azure Functionsを使用し、.NET環境で開発・運用している技術者。

- 注意点  
プレビュー版のため本番環境での利用は慎重に。SDKバージョンの更新を忘れないこと。

**詳細**:

本アップデートはAzure Functionsが.NET 10をパブリックプレビューでサポート開始したもので、最新の.NETランタイムの機能や性能向上を活用可能とすることを目的としています。利用には、Functionsプロジェクトのターゲットフレームワークをnet10.0に変更し、Microsoft.Azure.Functions.Worker.Sdkを2.0.5以降に更新する必要があります。これにより、最新のC#言語機能やパフォーマンス最適化、セキュリティ強化が利用可能となり、より効率的なサーバーレス開発が実現します。実装面では、既存のAzure Functions Workerモデルを継承しつつ、.NET 10の新APIやランタイム最適化が反映されているため、コードの互換性を保ちつつ最新環境に移行可能です。活用シナリオとしては、高負荷処理やリアルタイムデータ処理、マイクロサービス連携などで最新の.NET機能を活かした開発が挙げられます。注意点としては、現時点でプレビュー版のため、本番環境での利用は推奨されず、SDKバージョンの互換性や依存パッケージの更新を慎重に行う必要があります。また、Azure Functionsの他のバージョンや拡張機能との互換性検証も重要です。関連サービスとしては、Azure App Service上でのデプロイが可能で、Azure MonitorやApplication Insightsと連携しパフォーマンス監視やトラブルシューティングが行えます。詳細は公式ドキュメントを参照し、段階的な移行を推奨します。

---

### 2. Generally Available: Introducing the new Network Security Hub experience

**公開日時**: 2025年09月17日 16:30:45 UTC
**リンク**: [Generally Available: Introducing the new Network Security Hub experience](https://azure.microsoft.com/updates?id=503617)

**アップデートID**: 503617
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Azure DDoS Protection, Azure Firewall, Azure Firewall Manager, Web Application Firewall, Services, Features

**要約**:

- 何が更新されたか  
Azure Firewall Managerが「Network Security Hub」として一般提供開始され、統合管理インターフェースに刷新。

- 主な変更点や新機能  
Azure Firewall、WAF、DDoS Protectionを一元管理可能に。セキュリティ運用の効率化と可視化が向上。

- 影響を受ける対象  
Azureネットワークセキュリティを管理する技術者や運用チーム。

- 注意点があれば記載  
既存のFirewall Managerからの移行時は設定確認を推奨。新UIに慣れる必要あり。

**詳細**:

本アップデートは、従来のAzure Firewall Managerを拡張・改称し、Network Security Hubとして一般提供を開始したものです。背景には、Azure上のネットワークセキュリティ管理を一元化し、Firewall、WAF、DDoS Protectionの統合運用を容易にする狙いがあります。Network Security Hubは単一のポータルでこれらセキュリティ機能のポリシー作成・適用・監視を可能にし、管理負荷を軽減します。技術的には、各サービスのポリシー管理APIを統合し、共通のUI/UXを提供。ポリシーの階層的適用やスコープ管理もサポートします。活用例としては、大規模な複数サブスクリプション環境での一括セキュリティポリシー展開や、WAFルールとDDoS防御の連携強化が挙げられます。注意点として、既存Firewall Managerの設定移行時にポリシーの互換性確認が必要であり、一部機能は段階的に展開されるため最新ドキュメントの確認が推奨されます。関連サービスではAzure SentinelやAzure Monitorと連携し、統合ログ分析やアラート管理が可能です。これにより運用効率とセキュリティ強度の向上が期待されます。

---

### 3. Public Preview: Databricks One in Azure Databricks 

**公開日時**: 2025年09月17日 16:30:45 UTC
**リンク**: [Public Preview: Databricks One in Azure Databricks ](https://azure.microsoft.com/updates?id=503408)

**アップデートID**: 503408
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Analytics, Azure Databricks, Features

**要約**:

- 何が更新されたか  
Azure Databricksに「Databricks One」がパブリックプレビューで追加され、データエンジニアリング、分析、AI開発を統合した単一プラットフォームを提供。

- 主な変更点や新機能  
コラボレーションワークフローの統合、エンタープライズ向けガバナンス強化、パフォーマンス最適化を実現。

- 影響を受ける対象  
Azure Databricksを利用するデータエンジニア、データサイエンティスト、AI開発者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討が必要。

**詳細**:

Azure Databricksの新機能「Databricks One」は、データエンジニアリング、分析、AI開発を単一プラットフォーム上で統合し、運用管理を簡素化することを目的としたパブリックプレビューです。これにより、複数ツール間の断絶を解消し、コラボレーションワークフローを強化。エンタープライズレベルのガバナンス機能を備え、アクセス制御やデータセキュリティを一元管理可能です。技術的には、統合されたUIとAPIを通じてジョブ管理、モデル開発、データパイプラインの構築をシームレスに実現。Azure Active Directory連携による認証・認可や、Azure Purviewとの連携でデータカタログ管理も強化されます。活用例としては、データサイエンスチームが共同でモデル開発を行いながら、運用チームがパイプラインの監視・管理を一元化するケースが挙げられます。現時点ではパブリックプレビューのため、一部機能は制限される可能性があり、商用利用前に検証が推奨されます。Azure Data FactoryやAzure Synapse Analyticsとの連携により、エンドツーエンドのデータ統合・分析基盤構築が容易になります。

---

### 4. Generally Available: Confidential computing for Azure Database for PostgreSQL flexible server 

**公開日時**: 2025年09月17日 15:45:39 UTC
**リンク**: [Generally Available: Confidential computing for Azure Database for PostgreSQL flexible server ](https://azure.microsoft.com/updates?id=500795)

**アップデートID**: 500795
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL flexible serverで機密コンピューティングが一般提供開始。

- 主な変更点や新機能  
ハードウェアベースの信頼実行環境（TEE）内でデータを暗号化・処理し、クラウド上でもデータの機密性を強化。

- 影響を受ける対象  
Azure Database for PostgreSQL flexible serverを利用するセキュリティ重視の開発者や運用者。

- 注意点  
TEE対応のハードウェア環境が必要で、対応リージョンや構成要件を事前に確認すること。

**詳細**:

本アップデートは、Azure Database for PostgreSQL flexible serverにおけるConfidential Computing対応の一般提供開始を告知するものです。背景として、クラウド上でのデータ保護強化ニーズの高まりがあり、特にデータ処理中の機密性確保が課題となっていました。今回の機能追加により、ハードウェアベースの信頼実行環境（TEE）を利用し、データを暗号化したまま安全に処理可能となります。具体的には、CPU内のセキュアエンクレーブでデータを復号・処理し、クラウド管理者やOSレベルからの不正アクセスを防止します。実装はIntel SGXやAMD SEVなどのTEE技術を活用し、PostgreSQL flexible serverのインスタンス作成時にConfidential Computingを有効化する形で利用可能です。活用シナリオとしては、金融・医療など高い機密性が求められる業務データベースの運用に最適です。注意点としては、TEE対応ハードウェアのリージョン制限やパフォーマンスオーバーヘッドが発生する可能性がある点、また一部拡張機能やプラグインとの互換性に留意が必要です。Azure Key Vaultとの連携により暗号鍵管理を強化でき、Azure MonitorでTEEの稼働状況やセキュリティイベントの監視も可能です。これにより、クラウド上でのデータ処理におけるセキュリティレベルを大幅に向上させることができます。

---


*このレポートは自動生成されました - 2025-09-18 12:01:31 JST*