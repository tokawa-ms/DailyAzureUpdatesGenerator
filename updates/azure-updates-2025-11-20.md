# 2025年11月20日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年11月20日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 10 件

## 更新一覧

### 1. Generally Available: Azure Managed Lustre Support for Azure MCP Server

**公開日時**: 2025年11月19日 21:00:38 UTC
**リンク**: [Generally Available: Azure Managed Lustre Support for Azure MCP Server](https://azure.microsoft.com/updates?id=529381)

**アップデートID**: 529381
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Managed Lustre

**要約**:

- 何が更新されたか  
Azure Managed LustreがAzure MCP Serverと完全統合され、一般提供（GA）となりました。

- 主な変更点や新機能  
Azure MCP Serverを通じて、Managed Lustreファイルシステムの管理がAPIベースで一元化・自動化可能に。

- 影響を受ける対象  
Azure上で高性能ファイルシステムを利用する開発者・インフラ運用チーム。

- 注意点があれば記載  
既存環境での移行時はAPI仕様の確認が必要です。  

https://azure.microsoft.com/updates?id=529381

**詳細**:

本アップデートにより、Azure Managed LustreがAzure MCP Serverと完全統合され、一般提供（GA）されました。背景として、高性能ファイルシステムの運用管理を一元化し、開発者やインフラ担当者の効率化を図る目的があります。具体的には、Azure MCP Serverの管理コンソールやAPIを通じて、Managed Lustreファイルシステムの作成・設定・監視・スケーリングが可能となり、従来の個別管理から統合管理へと進化しました。技術的には、Azure MCP ServerがAzure Resource Manager（ARM）を介してManaged Lustreのリソースプロビジョニングとライフサイクル管理を行い、REST APIやCLIからも操作可能です。活用シナリオとしては、大規模データ解析やHPC環境での高速ストレージ管理が挙げられ、特に複数のManaged Lustreインスタンスを効率的に運用したい場合に有効です。注意点として、MCP Serverの利用には対応リージョンと権限設定が必要であり、既存のManaged Lustre環境は段階的に移行が推奨されます。関連サービスではAzure HPC CacheやAzure Batchとの連携により、ストレージ性能と計算リソースの最適化が可能です。詳細は公式ドキュメントを参照してください。

---

### 2. Generally Available: CSI Dynamic Provisioning for Azure Managed Lustre

**公開日時**: 2025年11月19日 21:00:38 UTC
**リンク**: [Generally Available: CSI Dynamic Provisioning for Azure Managed Lustre](https://azure.microsoft.com/updates?id=529368)

**アップデートID**: 529368
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Managed Lustre, Features, Management, Open Source, Services, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Managed Lustre（AMLFS）のCSIダイナミックプロビジョニングがGA（一般提供）となりました。

- 主な変更点や新機能  
Kubernetes上でStorageClassとPersistentVolumeClaimを使い、AMLFSの永続ボリュームをオンデマンドで動的に作成可能に。

- 影響を受ける対象  
AMLFSを利用するKubernetes環境の開発者・運用者。

- 注意点があれば記載  
既存の静的ボリュームからの移行計画を検討し、CSIドライバーのバージョン管理を行うことを推奨します。

**詳細**:

Azure Managed Lustre (AMLFS)向けのCSI Dynamic Provisioningが一般提供（GA）となりました。本アップデートは、Kubernetes環境でAMLFSを利用する際に、StorageClassおよびPersistentVolumeClaim（PVC）を用いてオンデマンドで永続ボリュームを動的にプロビジョニング可能にすることを目的としています。従来は手動でのボリューム作成が必要でしたが、これにより運用効率が大幅に向上します。技術的には、CSI（Container Storage Interface）ドライバーがKubernetesのAPIと連携し、PVC作成時にAzure Managed Lustreのボリュームを自動生成・マウントします。これにより、高性能な分散ファイルシステムをKubernetesワークロードにシームレスに統合可能です。活用シナリオとしては、大規模なデータ解析やHPCジョブでの高速ストレージ要求に適しており、Azure Kubernetes Service（AKS）との連携が推奨されます。注意点として、CSIドライバーのバージョン管理やアクセス権限設定、ネットワーク構成の最適化が必要です。また、AMLFSのスケーラビリティやパフォーマンス特性を理解した上でストレージクラスパラメータを調整することが重要です。関連サービスとして、Azure NetApp FilesやAzure Blob Storageと比較検討し、用途に応じた最適なストレージ選択が求められます。詳細は公式ドキュメントとアップデートページを参照してください。

---

### 3. Public Preview: 20 MB/s/TiB Performance Tier for Azure Managed Lustre 

**公開日時**: 2025年11月19日 21:00:38 UTC
**リンク**: [Public Preview: 20 MB/s/TiB Performance Tier for Azure Managed Lustre ](https://azure.microsoft.com/updates?id=529359)

**アップデートID**: 529359
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure Managed Lustre

**要約**:

- 何が更新されたか  
Azure Managed Lustreに新たに20 MB/s/TiBのパフォーマンス階層がパブリックプレビューで追加されました。

- 主な変更点や新機能  
大規模AIやHPC向けに最大25 PiBまでのファイルシステムを高スループットで構築可能となり、I/O性能が向上。

- 影響を受ける対象  
大容量・高性能ストレージを必要とするAI、HPC、ビッグデータ解析の技術者や運用者。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討し、最新のドキュメントを確認してください。

**詳細**:

Azure Managed Lustreに新たに追加された「20 MB/s/TiBパフォーマンスティア」は、大規模AIやHPCワークロードの高スループット要求に対応するためのパブリックプレビュー機能です。本ティアは、1TiBあたり20MB/sの読み書き性能を提供し、最大25PiBまでのファイルシステムをプロビジョニング可能です。これにより、大容量データセットの高速処理が求められるシナリオで効率的なI/O性能を実現します。技術的には、Lustreファイルシステムのスケーラブルな並列I/O特性を活かしつつ、ストレージノードの帯域幅を強化し、性能向上を図っています。実装はAzureポータルやCLIからパフォーマンスティア選択時に指定可能で、既存のManaged Lustre環境への適用も可能です。活用例としては、機械学習のトレーニングデータ高速読み込み、大規模シミュレーション結果のリアルタイム解析などが挙げられます。注意点として、パフォーマンス向上に伴いコストが増加するため、ワークロードのI/O特性を事前に評価することが推奨されます。また、最大容量制限やリージョン対応状況の確認も必要です。Azure HPC CacheやAzure NetApp Filesとの連携により、データアクセスの最適化や多様なストレージニーズに対応可能です。

---

### 4. Public Preview: Auto-import for Azure Managed Lustre

**公開日時**: 2025年11月19日 20:00:49 UTC
**リンク**: [Public Preview: Auto-import for Azure Managed Lustre](https://azure.microsoft.com/updates?id=529342)

**アップデートID**: 529342
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure Managed Lustre, Features, Microsoft Ignite, Services

**要約**:

- 何が更新されたか  
Azure Managed Lustre (AMLFS)にAuto-import機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
Azure Blob StorageのコンテナからAMLFSクラスターへ、ポリシーに基づく自動同期が可能になり、新規・変更データを自動的に反映します。

- 影響を受ける対象  
AMLFSを利用するユーザーで、Blob Storageとのデータ連携を効率化したい技術者。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に検討してください。今後の変更に注意が必要です。

**詳細**:

Azure Managed Lustre（AMLFS）におけるAuto-import機能がパブリックプレビューとして提供開始されました。本機能は、Azure Blob Storageのコンテナ内データをポリシーに基づき自動的にAMLFSクラスターへ同期・反映することを目的としています。これにより、Blobストレージ上の新規・変更ファイルがAMLFSにリアルタイムまたはスケジュールでインポートされ、手動同期の手間を削減します。技術的には、Blob Storageのイベントや変更検知をトリガーとして、AMLFSのファイルシステムに対してデータのインポート処理が実行される仕組みです。設定はAzureポータルやCLIでポリシーを定義し、対象コンテナと同期ルールを指定します。活用例として、大規模なデータ分析やHPCワークロードでBlob Storageに蓄積されたデータをAMLFS上で高速に処理するケースが挙げられます。注意点として、プレビュー段階のためパフォーマンスや対応リージョンに制限がある可能性があり、同期対象のBlobサイズやファイル数により処理時間が変動します。関連サービスとして、Azure Blob Storage、Azure HPC、Azure CLI/PowerShellが連携し、統合的なデータ管理と高速処理環境の構築を支援します。詳細は公式ドキュメントで最新情報を確認してください。

---

### 5. Public Preview: Recommended alerts for Azure Monitor Workspace

**公開日時**: 2025年11月19日 17:45:05 UTC
**リンク**: [Public Preview: Recommended alerts for Azure Monitor Workspace](https://azure.microsoft.com/updates?id=515505)

**アップデートID**: 515505
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, DevOps, Management and governance, Azure Kubernetes Service (AKS), Azure Monitor, Features

**要約**:

- 何が更新されたか  
Azure Monitor Workspace向けに推奨アラートのワンクリック有効化機能がパブリックプレビューで提供開始。

- 主な変更点や新機能  
Azure Monitor Managed Service for Prometheus利用者が、Azureポータル上で簡単に推奨アラートを有効化可能。これにより、ワークスペースのメトリクス取り込み制限を監視しやすくなる。

- 影響を受ける対象  
Azure Monitor WorkspaceおよびManaged Service for Prometheusを利用する技術者・運用者。

- 注意点  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討すること。

**詳細**:

本アップデートは、Azure Monitor Managed Service for Prometheus利用者向けに、Azure Monitor Workspaceのメトリクス取り込み上限を監視可能な推奨アラートをAzureポータル上でワンクリック有効化できる機能をパブリックプレビューとして提供開始したものです。これにより、取り込み制限超過によるデータ欠損リスクを事前に検知し、運用の安定性向上が図れます。具体的には、Azure Monitor Workspaceの取り込みレートや容量のメトリクスを監視対象とし、閾値超過時にアラートを発報。ポータル上のUIから推奨アラートを選択し即座に有効化できるため、設定工数を大幅に削減します。技術的には、Azure Monitorのアラートルール機能を活用し、Prometheusデータの取り込み状況をメトリクスとして収集・評価。アラートはLog Analyticsワークスペースに紐づく形で管理されます。活用例としては、大規模Prometheus環境でのメトリクス取り込み過負荷の早期検知や、容量計画の補助が挙げられます。注意点としてはパブリックプレビュー段階のため、機能仕様やUIが変更される可能性がある点、また一部リージョンでの提供状況に制限がある場合があります。関連サービスとしては、Log Analyticsワークスペース、Azure Monitorアラート、Prometheus互換の監視環境との連携が重要です。これにより、Prometheusベースの監視運用における信頼性と効率性が向上します。

---

### 6. Public Preview: Azure Managed Redis integration with Microsoft Foundry

**公開日時**: 2025年11月19日 17:30:18 UTC
**リンク**: [Public Preview: Azure Managed Redis integration with Microsoft Foundry](https://azure.microsoft.com/updates?id=532188)

**アップデートID**: 532188
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Azure Managed RedisがMicrosoft FoundryのMCPツールカタログにパブリックプレビューで統合されました。

- 主な変更点や新機能  
RedisをAIエージェントのナレッジストアやメモリストアとして簡単に利用可能になり、Foundryベースのエージェントとの接続が容易に。

- 影響を受ける対象  
AIエージェント開発者やMicrosoft Foundry利用者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

本アップデートは、Azure Managed RedisをMicrosoft FoundryのMCPツールカタログに統合し、AIエージェントの知識格納やメモリストアとしてRedisを容易に利用可能にすることを目的としています。これにより、FoundryベースのAIエージェントは低レイテンシかつ高スループットのRedisキャッシュを活用し、状態管理や高速データアクセスが可能となります。技術的には、Foundryのエージェント開発環境からRedisインスタンスへの接続設定が簡素化され、API経由でのデータ読み書きがシームレスに行えます。具体的には、エージェントのコンテキスト情報や学習データをRedisに格納し、リアルタイムでの情報更新や問い合わせ応答の高速化を実現します。活用例としては、チャットボットの会話履歴管理やパーソナライズドAIの状態保持が挙げられます。注意点として、Redisのスケーリングやデータ永続化設定は別途管理が必要であり、Foundryとの接続時には認証情報の適切な管理が求められます。また、Redisのキャッシュ特性を踏まえたデータ設計が重要です。関連サービスとしては、Azure AIサービスやAzure Functionsと連携し、Redisを介した高速データアクセスを活用した高度なAIソリューション構築が可能です。

---

### 7. Generally Available: TLS and TCP termination on Azure Application Gateway

**公開日時**: 2025年11月19日 17:00:30 UTC
**リンク**: [Generally Available: TLS and TCP termination on Azure Application Gateway](https://azure.microsoft.com/updates?id=532202)

**アップデートID**: 532202
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Application Gateway

**要約**:

- 何が更新されたか  
Azure Application GatewayでTLSおよびTCPプロトコルの終了処理がGA（一般提供）となりました。

- 主な変更点や新機能  
HTTP(S)以外のTCP/TLSトラフィックのロードバランシングとセキュアな処理が可能に。

- 影響を受ける対象  
TCP/TLSベースのアプリケーションをAzure Application Gatewayで運用する技術者。

- 注意点があれば記載  
既存の設定との互換性やセキュリティポリシーの見直しが必要になる場合があります。

**詳細**:

Azure Application GatewayがTLSおよびTCPプロトコルの終端処理をGA（一般提供）しました。従来はHTTP/HTTPSトラフィックに限定されていたロードバランシングが、TLSやTCPベースの非HTTP(S)アプリケーションにも拡張され、セキュアかつ効率的なトラフィック管理が可能となりました。これにより、例えばカスタムTLSアプリケーションやデータベース接続、メッセージングプロトコルなど多様なTCPサービスをApplication Gateway経由で負荷分散しつつ、TLS終端による暗号化解除や検査が行えます。実装は、リスナー設定でTCP/TLSを選択し、証明書管理やポリシー適用が可能。バックエンドプールにはTCP対応のサーバーを指定し、ヘルスプローブもTCP/TLSに対応しています。活用例としては、マルチプロトコル対応のマイクロサービス環境や、TLS終端によるセキュリティ強化が求められる非HTTPアプリケーションの負荷分散が挙げられます。注意点としては、HTTP固有の機能（Cookieベースのセッション維持やWAF）はTCP/TLS終端では利用できないため、用途に応じた設計が必要です。Azure Front DoorやAzure Firewallなど他のネットワークサービスと組み合わせることで、より高度なトラフィック管理やセキュリティ対策が可能です。詳細は公式ドキュメントを参照してください。

---

### 8. Public Preview: Microsoft Foundry data connection for Azure Databricks

**公開日時**: 2025年11月19日 17:00:30 UTC
**リンク**: [Public Preview: Microsoft Foundry data connection for Azure Databricks](https://azure.microsoft.com/updates?id=527678)

**アップデートID**: 527678
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Analytics, Azure Databricks

**要約**:

- 何が更新されたか  
Azure DatabricksのGenieがMicrosoft Foundryと統合され、パブリックプレビューとして提供開始。

- 主な変更点や新機能  
GenieスペースからModel Context Protocol（MCP）を使い、Microsoft Foundryのエージェントへ直接接続可能に。信頼性の高いデータへシームレスにアクセスできる。

- 影響を受ける対象  
Azure DatabricksユーザーおよびMicrosoft Foundryを利用するデータエンジニアやデータサイエンティスト。

- 注意点  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討が必要。MCPの設定や権限管理に注意。

**詳細**:

本アップデートは、Azure DatabricksのGenie機能とMicrosoft FoundryのデータエージェントをModel Context Protocol（MCP）経由で直接接続可能にしたもので、現在パブリックプレビュー段階です。背景には、データサイロの解消と信頼性の高いデータアクセスの簡素化があり、データエンジニアやデータサイエンティストが統合環境で効率的に分析基盤を構築できることを目的としています。具体的には、GenieスペースからFoundryのエージェントへMCPを用いて接続し、Foundryに蓄積された検証済みデータセットを直接参照・利用可能です。技術的には、MCPがデータモデルとコンテキスト情報を標準化し、両サービス間の相互運用性を実現。実装はAzure Databricksのワークスペース内でGenie設定を行い、Foundryエージェントのエンドポイント情報を登録する形で行います。活用例としては、Foundryの信頼性の高いデータをDatabricksの分析ジョブや機械学習モデル構築に直接活用し、データ準備工数を削減可能です。注意点としては、現時点でパブリックプレビューのため、機能の安定性やサポート範囲に制限があり、MCP対応のFoundryエージェントが必要です。関連サービスとしては、Azure Databricks、Microsoft Foundry、Azure Data Factoryなどが連携し、エンドツーエンドのデータパイプライン構築が促進されます。

---

### 9. Public Preview: Azure Databricks Genie in Copilot Studio 

**公開日時**: 2025年11月19日 17:00:30 UTC
**リンク**: [Public Preview: Azure Databricks Genie in Copilot Studio ](https://azure.microsoft.com/updates?id=527668)

**アップデートID**: 527668
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Analytics, Azure Databricks

**要約**:

- 何が更新されたか  
Azure Databricks GenieがMicrosoft Copilot Studioでパブリックプレビュー提供開始。

- 主な変更点や新機能  
Azure Databricksのデータに対し、エンタープライズ対応のAI会話型分析が可能に。自然言語での高度なクエリやインサイト取得が容易になる。

- 影響を受ける対象  
Azure Databricksを利用するデータエンジニアやデータサイエンティスト、BI担当者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、商用利用前に機能や制限を確認することを推奨。

**詳細**:

本アップデートは、Azure Databricksの大規模データ分析環境に対し、Microsoft Copilot Studio内で「Azure Databricks Genie」をパブリックプレビューとして提供開始したものです。目的は、自然言語による対話型AIを活用し、エンタープライズレベルの高度な分析クエリや洞察を迅速に引き出すことで、データ活用の生産性向上を図る点にあります。具体的には、Copilot Studioのインターフェースから直接DatabricksのデータレイクやDelta Lakeに格納された膨大なデータセットに対し、Genieが自然言語解析を行い、SQLクエリや分析結果を生成・提示します。技術的には、GenieがAzure DatabricksのAPIと連携し、ユーザーの質問を解析して最適なSpark SQLクエリを自動生成、実行結果を対話形式で返す仕組みです。活用シナリオとしては、データサイエンティストやアナリストが複雑なクエリ作成なしに、ビジネスインサイトを即座に抽出できる点が挙げられます。なお、現時点ではパブリックプレビューのため、対応言語やデータソースの種類に制限があり、商用利用前に動作検証が推奨されます。Azure Synapse AnalyticsやAzure Machine Learningとの連携も可能で、統合的なデータ分析・AIワークフロー構築に寄与します。詳細は公式ドキュメントを参照してください。

---

### 10. Public Preview: Azure API Management adds support for A2A Agent APIs

**公開日時**: 2025年11月19日 17:00:30 UTC
**リンク**: [Public Preview: Azure API Management adds support for A2A Agent APIs](https://azure.microsoft.com/updates?id=527635)

**アップデートID**: 527635
**情報源**: Azure Updates API

**カテゴリ**: In preview, Integration, Internet of Things, Mobile, Web, API Management

**要約**:

- 何が更新されたか  
Azure API ManagementがA2A（Agent to Agent）APIのサポートをパブリックプレビューで開始。

- 主な変更点や新機能  
AIモデルAPIやMCPツールに加え、エージェントAPIも一元管理・ガバナンス可能に。

- 影響を受ける対象  
API管理を行う開発者や運用チーム、特にエージェントAPIを利用する組織。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に検討が必要。今後の正式リリースに注目。

**詳細**:

本アップデートは、Azure API Management（APIM）がAgent-to-Agent（A2A）APIをサポートするパブリックプレビューを開始したことを示します。背景として、AIモデルAPIやModel Context Protocol（MCP）ツールなど、多様化するAPI形態の統合管理ニーズが高まっている点があります。今回の機能追加により、APIM上でA2AエージェントAPIを他のAPIと同様に管理・ガバナンス可能となり、APIポリシー適用や認証・認可の一元化が実現します。技術的には、APIMがA2A通信のAPIエンドポイントをプロキシし、トラフィック制御やモニタリングを行う仕組みを提供。実装は既存のAPIMインスタンスにA2A APIを登録し、ポリシー設定でセキュリティや変換ルールを適用する形で行います。活用例としては、複数のAIエージェント間通信の標準化や、MCPツールとの連携強化が挙げられます。注意点としては、パブリックプレビュー段階のため、機能の安定性やサポート範囲に制限があり、商用環境での利用は慎重に検討が必要です。関連サービスとしては、Azure Cognitive ServicesやAzure Functionsとの連携により、AIモデルのAPI管理とエージェント間通信を統合的に運用可能です。

---


*このレポートは自動生成されました - 2025-11-20 12:02:44 JST*