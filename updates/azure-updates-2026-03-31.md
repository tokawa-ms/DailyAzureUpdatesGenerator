# 2026年03月31日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年03月31日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Public Preview: Ephemeral OS Disk with full caching for VM/VMSS

**公開日時**: 2026年03月30日 21:45:47 UTC
**リンク**: [Public Preview: Ephemeral OS Disk with full caching for VM/VMSS](https://azure.microsoft.com/updates?id=559322)

**アップデートID**: 559322
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Virtual Machine Scale Sets, Virtual Machines, Features

**要約**:

- 何が更新されたか  
Azure VMおよびVMSS向けに、「Ephemeral OS Disk with full caching（フルキャッシュ対応エフェメラルOSディスク）」がパブリックプレビューとして提供開始されました。

- 主な変更点や新機能  
この機能により、OSディスク全体のイメージをローカルVMストレージ（キャッシュディスクやリソースディスク）にキャッシュすることが可能になります。これにより、OSディスクのパフォーマンスが大幅に向上し、より高速かつ信頼性の高いワークロード実行が実現できます。

- 影響を受ける対象  
Azure仮想マシン（VM）および仮想マシンスケールセット（VMSS）を利用している環境が対象です。特に、起動時間やI/O性能が重要なワークロードを運用している技術者にとって有用なアップデートです。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用には慎重な検討が必要です。また、ローカルストレージを利用するため、VMの再配置や停止時のデータ保持については既存のエフェメラルOSディスクと同様の注意が必要です。

**詳細**:

本アップデートは、「Ephemeral OS Disk with full caching」がAzure Virtual Machines（VM）およびVirtual Machine Scale Sets（VMSS）でパブリックプレビューとして利用可能になったことを示しています。従来のEphemeral OS Diskは、一時的なOSディスクをローカルVMストレージ上に配置することで、迅速なデプロイやスケールアウト、コスト削減を実現してきました。今回のアップデートでは、OSディスクイメージ全体をVMのローカルストレージ（キャッシュディスクやリソースディスク）に完全にキャッシュする「full caching」機能が追加されています。これにより、OSディスクへのI/Oパフォーマンスが大幅に向上し、より高速かつ信頼性の高いOSディスクアクセスが可能となります。

技術的には、Ephemeral OS Disk with full cachingは、VMまたはVMSSのローカルストレージを活用して、OSディスク全体をキャッシュします。これにより、ディスクI/Oがネットワーク経由のリモートストレージではなく、ローカルディスクで完結するため、レイテンシの低減とスループットの向上が期待できます。VMの起動や再起動、スケールアウト時のプロビジョニング速度も向上し、特に短期間で大量のVMを展開するシナリオや、頻繁に再イメージングが発生する環境に適しています。

活用シナリオとしては、Dev/Test環境や自動スケールが求められるWebアプリケーションのフロントエンド、または一時的なバッチ処理ワークロードなど、OSディスクの永続性が不要なケースが挙げられます。Ephemeral OS DiskはVMの停止や削除時にデータが失われるため、永続的なデータ保存が必要なワークロードには適していません。

注意点として、Ephemeral OS Disk with full cachingは、ローカルストレージの容量や性能に依存するため、利用可能なVMサイズや構成に制限があります。また、OSディスクの内容はVMのライフサイクルに依存し、VMの停止や再配置、障害発生時には内容が失われるため、重要なデータや永続化が必要な設定は別途管理する必要があります。

本機能は、Azure VMおよびVMSSの標準的な管理機能と連携して動作しますが、永続ディスク（Managed Disk）やバックアップ、スナップショットなどの永続化機能とは異なる運用が求められます。詳細や最新情報については、公式ドキュメントやアップデートページ（https://azure.microsoft.com/updates?id=559322）を参照してください。

---

### 2. Generally Available: Azure Red Hat OpenShift in Indonesia Central

**公開日時**: 2026年03月30日 21:30:50 UTC
**リンク**: [Generally Available: Azure Red Hat OpenShift in Indonesia Central](https://azure.microsoft.com/updates?id=559552)

**アップデートID**: 559552
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Red Hat OpenShift, Open Source

**要約**:

【Azure Update要約】

- 何が更新されたか  
Azure Red Hat OpenShift（ARO）が、インドネシア中央リージョンで一般提供（GA）されました。

- 主な変更点や新機能  
これまで利用できなかったインドネシア中央リージョンで、ミッションクリティカルなOpenShiftワークロードをAzure上で稼働させることが可能になりました。これにより、現地のデータレジデンシー要件や低レイテンシーのニーズにも対応できます。

- 影響を受ける対象  
インドネシア中央リージョンでAzureを利用する企業や組織、特にOpenShiftを活用したコンテナベースのアプリケーションを運用している技術者や開発者が対象です。

- 注意点があれば記載  
新リージョンでの利用開始に伴い、リージョン固有の制約や価格設定、サービスレベルアグリーメント（SLA）などの詳細を事前に確認することを推奨します。また、既存環境からの移行や新規構築時には、ネットワーク構成やセキュリティ設定にご注意ください。

【参考URL】  
https://azure.microsoft.com/updates?id=559552

**詳細**:

Azure Red Hat OpenShift（ARO）がインドネシア中央リージョンで一般提供（GA）されたことにより、ミッションクリティカルなOpenShiftワークロードをAzure上で運用する顧客のリージョン選択肢が拡大しました。本アップデートの背景には、インドネシア国内および周辺地域の企業や組織が、データレジデンシーやレイテンシ要件を満たしつつ、エンタープライズグレードのKubernetesプラットフォームを利用したいというニーズがあります。これにより、現地の法規制やガバナンス要件に対応しながら、グローバル水準のクラウドネイティブアプリケーション開発・運用が可能となります。

AROは、Microsoft Azure上でRed Hat OpenShiftをフルマネージドサービスとして提供するもので、Red HatとMicrosoftが共同でサポートを行います。利用者は、OpenShiftのインストール、パッチ適用、アップグレード、スケーリング、モニタリングといった運用管理作業をAzureのマネージドサービスとして享受でき、インフラストラクチャの管理負荷を大幅に軽減できます。今回のアップデートにより、インドネシア中央リージョンでもこれらの機能が利用可能となりました。

技術的には、AROはAzureの仮想マシン、ストレージ、ネットワークリソース上にOpenShiftクラスターを自動デプロイし、Azure Resource Manager（ARM）を通じてリソース管理を一元化します。クラスターの作成やスケーリングはAzure CLIやAzure Portal、ARMテンプレートから操作でき、Red Hat OpenShiftの機能（Operator、OpenShift Container Registry、OpenShift Service Meshなど）も利用可能です。また、Azure Active Directoryとの連携による認証・認可や、Azure Monitorによる監視、Azure Policyによるガバナンス強化も実現できます。

活用シナリオとしては、金融・公共・製造業など、厳格なデータ主権や高可用性が求められる業界でのコンテナ化アプリケーションの運用、DevOpsパイプラインの構築、マイクロサービスアーキテクチャの導入などが挙げられます。特に、既存のOpenShift環境をクラウドへ移行したい場合や、ハイブリッドクラウド戦略を推進する企業にとって有用です。

注意点として、利用可能なリージョンが拡大したものの、各リージョンで提供されるVMサイズやサービスレベル、サポート体制に差異がある場合があるため、事前に公式ドキュメントで詳細を確認する必要があります。また、Red Hat OpenShiftのバージョンやサポートポリシーもAzureの提供範囲に準拠します。

関連するAzureサービスとしては、Azure Kubernetes Service（AKS）との比較検討や、Azure DevOps、Azure Container Registry、Azure Key Vaultなどとの統合利用が挙げられます。これにより、セキュアかつスケーラブルなエンタープライズ向けコンテナ基盤の構築が可能となります。

---

### 3. Retirement: Deprecation of sidecar for remote-write for Azure Monitor managed service for Prometheus

**公開日時**: 2026年03月30日 21:30:50 UTC
**リンク**: [Retirement: Deprecation of sidecar for remote-write for Azure Monitor managed service for Prometheus](https://azure.microsoft.com/updates?id=550519)

**アップデートID**: 550519
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, DevOps, Management and governance, Azure Kubernetes Service (AKS), Azure Monitor, Retirements

**要約**:

【何が更新されたか】  
Azure Monitorのマネージドサービス for Prometheusにおいて、remote-write用のsidecarが2027年3月31日に廃止されることが発表されました。

【主な変更点や新機能】  
sidecar経由でPrometheusメトリクスをAzure Monitor Workspaceへ送信する機能が非推奨となります。今後はsidecarを利用せず、直接remote-writeの設定を行うことが推奨されます。これにより、システムの信頼性向上と構成の簡素化が図られます。

【影響を受ける対象】  
現在、Azure Monitor WorkspaceへのPrometheusメトリクス送信にsidecarを利用しているユーザーやシステムが対象となります。特にself-hosted Prometheus環境を運用している技術者は、設定変更が必要となります。

【注意点】  
2027年3月31日以降、sidecar経由でのremote-writeは利用できなくなります。今後の運用に向けて、sidecarを使用しない方法への移行を早めに検討・実施してください。公式ドキュメントやサポート情報を参照し、移行計画を立てることを推奨します。

**詳細**:

Azure Monitor managed service for Prometheusに関する今回のアップデートは、2027年3月31日をもって「sidecar for remote-write」の機能が廃止されることを告知するものです。このアップデートの背景には、Azure Monitorの信頼性向上とシステムの複雑性軽減という目的があります。従来、PrometheusのメトリクスをAzure Monitor Workspaceへ送信する際、sidecarコンポーネントを利用してremote-write機能を実装していました。sidecarは、Prometheusサーバーの外部プロセスとして動作し、メトリクスデータをAzure Monitor Workspaceに転送する役割を担っていました。

今回の変更により、sidecarによるremote-writeのサポートが終了するため、今後はこの方法でPrometheusメトリクスをAzure Monitor Workspaceへ送信することができなくなります。技術的には、sidecarはPrometheusのremote-write APIを利用し、データをAzure Monitorのエンドポイントに送信していましたが、この仕組みが廃止されることで、ユーザーは代替手段の検討が必要となります。Azure Monitor Workspaceへのメトリクス送信を継続する場合、今後はsidecar以外の方法や、Azureが推奨する新しい構成への移行が求められます。

このアップデートは、主に自社でPrometheusをホストしている環境や、Kubernetes上でPrometheusを運用している技術者に影響を与えます。例えば、現行のsidecar構成を利用してメトリクスをAzure Monitor Workspaceへ転送している場合、2027年3月31日以降はこの方法が利用できなくなるため、早期に移行計画を立てる必要があります。Azure Monitor managed service for Prometheusは、Azure上でPrometheusの運用を簡素化し、統合的な監視環境を提供するサービスであり、Azure Monitor Workspaceや他の監視サービスとの連携が可能です。

注意点として、sidecar for remote-writeの廃止は既存の監視構成に直接影響を与えるため、事前にAzure公式ドキュメントやアップデート情報を確認し、推奨される移行方法や代替構成を検討することが重要です。また、今後のAzure MonitorやPrometheus関連サービスのアップデートに注視し、最新のベストプラクティスに従うことが求められます。関連するAzureサービスとしては、Azure Monitor WorkspaceやAzure Kubernetes Service（AKS）、その他のAzure監視ソリューションが挙げられますが、今回のアップデートは主にPrometheusのremote-write経路に限定された内容です。

---

### 4. Retirement: Azure Cosmos DB for PostgreSQL will retire on March 31, 2029

**公開日時**: 2026年03月30日 17:45:08 UTC
**リンク**: [Retirement: Azure Cosmos DB for PostgreSQL will retire on March 31, 2029](https://azure.microsoft.com/updates?id=556085)

**アップデートID**: 556085
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

【何が更新されたか】  
Azure Cosmos DB for PostgreSQLが2029年3月31日にサービス終了（リタイア）することが発表されました。

【主な変更点や新機能】  
現行のAzure Cosmos DB for PostgreSQLは廃止され、今後はAzure Database for PostgreSQL Elastic Clusterへの移行が必要となります。Elastic Clusterは、分散型PostgreSQLの機能を引き続き提供します。

【影響を受ける対象】  
Azure Cosmos DB for PostgreSQLを利用しているユーザーおよびシステムが対象となります。既存のデータベースやアプリケーションは、リタイアまでにElastic Clusterへ移行する必要があります。

【注意点】  
2029年3月31日以降はAzure Cosmos DB for PostgreSQLが利用できなくなるため、計画的な移行が必須です。移行先のElastic Clusterは同等の分散PostgreSQL機能を提供しますが、移行作業や互換性の確認が必要です。早めに移行計画を立て、必要なテストや検証を行うことを推奨します。

**詳細**:

2029年3月31日をもって、Azure Cosmos DB for PostgreSQLがサービス終了となります。このアップデートは、分散型PostgreSQLデータベースを利用しているユーザーに対して、Azure Database for PostgreSQL Elastic Clusterへの移行を促すものです。Azure Cosmos DB for PostgreSQLは、スケーラブルな分散型PostgreSQLデータベースとして、複数ノードにまたがるデータ管理や高可用性、パーティショニングなどの機能を提供してきました。今回のリタイアメントにより、これらの機能はAzure Database for PostgreSQL Elastic Clusterに引き継がれることになります。

Azure Database for PostgreSQL Elastic Clusterは、分散型PostgreSQLの機能を維持しつつ、クラウドネイティブな設計による柔軟なスケーリングや、複数ノード構成による高い可用性を提供します。データの分散管理やシャーディング、パーティション分割などの機能が引き続き利用可能であり、従来のCosmos DB for PostgreSQLからの移行に際しても、アプリケーション側の大きな変更は不要です。技術的な実装としては、PostgreSQLの拡張機能を活用し、分散クエリ処理やノード間のデータ同期を効率的に実現しています。

活用シナリオとしては、IoTやリアルタイム分析、マルチテナントアプリケーションなど、大量データの分散管理が求められるケースに適しています。Elastic Clusterは、既存のAzure Database for PostgreSQLサービスとの連携が可能であり、Azure MonitorやAzure Backupなどの周辺サービスとも統合できます。これにより、運用監視やバックアップ、セキュリティ管理など、エンタープライズ用途にも対応できます。

注意点として、2029年3月31日以降はCosmos DB for PostgreSQLの新規作成やサポートが終了するため、早期にElastic Clusterへの移行計画を立てる必要があります。移行時には、データの整合性やアプリケーションの接続設定、パフォーマンス要件などを十分に検証することが重要です。また、Elastic Clusterは分散型PostgreSQLの機能を提供しますが、Cosmos DB固有のAPIや機能は利用できませんので、移行前に機能差異を確認することが推奨されます。

関連するAzureサービスとしては、Azure Database for PostgreSQL Elastic Clusterを中心に、Azure Monitorによるパフォーマンス監視、Azure Backupによるデータ保護、Azure Active Directoryによる認証管理などが挙げられます。これらのサービスと組み合わせることで、分散型PostgreSQL環境の運用効率とセキュリティを高めることが可能です。

---

### 5. Generally Available: Azure Premium SSD v2 Disk is now available in South India

**公開日時**: 2026年03月30日 16:30:50 UTC
**リンク**: [Generally Available: Azure Premium SSD v2 Disk is now available in South India](https://azure.microsoft.com/updates?id=559526)

**アップデートID**: 559526
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Compute, Azure Disk Storage, Virtual Machines, Features, Services

**要約**:

【何が更新されたか】  
Azure Premium SSD v2ディスクが、South Indiaリージョン（Availability Zoneなし）で一般提供（GA）開始されました。

【主な変更点や新機能】  
Azure Premium SSD v2は、Azure仮想マシン向けの次世代汎用ブロックストレージです。サブミリ秒の低レイテンシと優れた価格性能比を提供します。従来のPremium SSDよりも高いパフォーマンスと柔軟なスケーリングが可能です。

【影響を受ける対象】  
South Indiaリージョンで仮想マシンを利用する技術者や、ストレージ性能を重視するアプリケーションの運用者が対象となります。

【注意点】  
South IndiaリージョンはAvailability Zone非対応です。高可用性構成を検討する場合は、リージョン特性に留意してください。Premium SSD v2の利用には、対応VMサイズやディスク管理方法の確認が必要です。

**詳細**:

Azure Premium SSD v2ディスクがSouth Indiaリージョン（アベイラビリティゾーン非対応リージョン）で一般提供開始されたことは、Azure仮想マシン向けのブロックストレージサービスの選択肢拡大を意味します。本アップデートの背景には、より高性能かつコスト効率の高いストレージを必要とするワークロードが増加していることが挙げられます。Premium SSD v2は、次世代の汎用ブロックストレージとして設計されており、サブミリ秒のレイテンシと優れた価格性能比を提供することが特徴です。

具体的な機能として、Premium SSD v2ディスクは、従来のPremium SSDよりも低遅延かつ高いスループットを実現しています。これにより、データベースやトランザクション処理、仮想デスクトップなど、ストレージI/O性能が重要なエンタープライズワークロードに最適です。また、ディスクのプロビジョニングや管理はAzureポータル、CLI、ARMテンプレートなどの標準的なAzure管理ツールを通じて行うことができます。

技術的な仕組みとしては、Premium SSD v2はAzureの分散ストレージアーキテクチャ上に構築されており、仮想マシンにアタッチしてOSディスクやデータディスクとして利用可能です。I/Oパフォーマンスはディスクサイズに応じて自動的にスケーリングされ、アプリケーションの要件に柔軟に対応できます。

活用シナリオとしては、OLTPデータベース、ビッグデータ分析、ミッションクリティカルな業務アプリケーションなど、低レイテンシと高スループットが求められるケースが想定されます。特にSouth Indiaリージョンで高性能ストレージを必要とする場合に有効です。

注意点として、South Indiaリージョンはアベイラビリティゾーンに対応していないため、ゾーン冗長性を必要とするシステムには適していません。また、Premium SSD v2の利用には対応する仮想マシンサイズや構成が必要となる場合がありますので、事前にAzureの公式ドキュメントで互換性を確認することが重要です。

関連するAzureサービスとの連携としては、Azure BackupやAzure Site Recoveryなどのデータ保護・災害復旧サービスと組み合わせて利用することで、エンタープライズレベルの可用性とデータ保護を実現できます。Premium SSD v2は、他のAzureディスクサービスと同様に、スナップショットやディスク暗号化などの機能もサポートしています。

詳細については、公式アップデートページ（https://azure.microsoft.com/updates?id=559526）を参照してください。

---


*このレポートは自動生成されました - 2026-03-31 12:02:09 JST*