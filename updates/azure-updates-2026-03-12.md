# 2026年03月12日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年03月12日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Generally Available: Terraform, Bicep, Ansible support for elastic clusters on Azure Database for PostgreSQL 

**公開日時**: 2026年03月11日 18:00:35 UTC
**リンク**: [Generally Available: Terraform, Bicep, Ansible support for elastic clusters on Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=558145)

**アップデートID**: 558145
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQLのエラスティッククラスターに対し、Terraform、Bicep、Ansibleによるプロビジョニングおよび管理が一般提供（GA）されました。

- 主な変更点や新機能  
インフラストラクチャ自動化ツール（Terraform、Bicep、Ansible）を用いて、エラスティッククラスターの作成、スケール、管理がネイティブにサポートされるようになりました。これにより、Infrastructure as Code（IaC）による一貫した運用が可能となります。

- 影響を受ける対象  
Azure Database for PostgreSQLのエラスティッククラスターを利用している、または今後利用予定のある開発者や運用担当者、DevOpsエンジニアが対象です。

- 注意点があれば記載  
本機能はGAのため、商用環境でも安心して利用できますが、各ツールのバージョンやAzureリソースプロバイダーの対応状況には注意してください。詳細な利用方法や制限事項は公式ドキュメントを参照してください。

**詳細**:

本アップデートは、Azure Database for PostgreSQLのエラスティッククラスターに対して、Terraform、Bicep、Ansibleによるプロビジョニングおよび管理が一般提供（GA）されたことを示しています。これにより、インフラストラクチャをコードとして管理するInfrastructure as Code（IaC）ツールを活用し、エラスティッククラスターの作成、スケール、管理を一貫して自動化できるようになりました。

具体的には、Terraform、Bicep、Ansibleの各ツールがAzure Database for PostgreSQLのエラスティッククラスターに対するリソース定義や構成管理をサポートします。Terraformは宣言的な構成ファイルを用いてインフラのプロビジョニングを自動化し、BicepはAzure Resource Manager（ARM）テンプレートの簡易記法としてAzureリソースのデプロイを効率化します。Ansibleは構成管理やアプリケーションデプロイの自動化を可能にし、Playbookを通じてエラスティッククラスターの状態を管理できます。

技術的な実装としては、これらのIaCツールがAzure Resource Manager APIを介してエラスティッククラスターのリソース作成や設定変更を行います。これにより、開発者や運用担当者はコードベースでインフラのライフサイクル管理を行い、環境間での一貫性や再現性を確保できます。

活用シナリオとしては、複数環境（開発、検証、本番）でのエラスティッククラスターの自動構築、スケールアウトやスケールインの自動化、CI/CDパイプラインへの組み込みなどが挙げられます。これにより、手動作業によるヒューマンエラーを削減し、迅速かつ確実なインフラ運用が実現します。

注意点としては、各IaCツールのバージョンやAzure Providerの対応状況、エラスティッククラスター固有の設定項目や制約事項を事前に確認する必要があります。また、既存のリソースとの連携や依存関係の管理にも留意する必要があります。

関連するAzureサービスとしては、Azure Resource Managerをはじめ、Azure DevOpsやGitHub ActionsなどのCI/CDサービスとの連携が考えられます。これにより、エラスティッククラスターの構築・運用をより効率的に自動化することが可能です。

---

### 2. Generally Available: Azure Database for PostgreSQL dashboards with Grafana 

**公開日時**: 2026年03月11日 18:00:35 UTC
**リンク**: [Generally Available: Azure Database for PostgreSQL dashboards with Grafana ](https://azure.microsoft.com/updates?id=558140)

**アップデートID**: 558140
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQLにおいて、Azureポータル上でGrafanaのダッシュボードが一般提供（GA）されました。

- 主な変更点や新機能  
Azure Monitorとのネイティブ統合により、Azureポータルから直接、PostgreSQLのパフォーマンスや稼働状況を可視化できるリッチなGrafanaダッシュボードが利用可能になりました。これにより、別途Grafanaインスタンスのセットアップや運用管理が不要となります。

- 影響を受ける対象  
Azure Database for PostgreSQL（シングルサーバーおよびフレキシブルサーバー）を利用している技術者や運用担当者が対象です。監視やトラブルシューティングの効率化が期待できます。

- 注意点があれば記載  
本機能はAzureポータル内で提供されるため、既存の独立したGrafana環境との連携やカスタムダッシュボードの移行については、事前に検証を行うことを推奨します。また、利用にはAzure Monitorの権限設定が必要です。

**詳細**:

本アップデートは、Azure Database for PostgreSQLの監視機能を強化するため、Azureポータル上でGrafanaのダッシュボードをネイティブに利用できるようになったことを示しています。これにより、従来は個別にGrafanaインスタンスを構築・管理する必要があったところ、Azure Monitorとの統合により、Azureポータル内で直接、リッチな可視化ダッシュボードを利用できるようになりました。

今回の変更点としては、Azure Database for PostgreSQLの各種メトリックやパフォーマンスデータを、Azureポータル上の組み込みGrafanaダッシュボードで即時に可視化できる点が挙げられます。これにより、データベースの稼働状況やリソース使用率、クエリパフォーマンスなどの詳細な監視が容易になります。また、Azure Monitorとのネイティブ連携により、追加の設定や外部サービスへのデータ転送を行うことなく、シームレスに監視基盤を構築できます。

技術的な仕組みとしては、Azure Monitorが収集したPostgreSQLの各種メトリックを、Azureポータル内の組み込みGrafanaダッシュボードに自動的に連携・表示する形となります。これにより、ユーザーはGrafanaのインストールや個別のデータソース設定を行う必要がなく、Azureの管理画面から直接監視・分析作業を実施できます。

活用シナリオとしては、運用担当者やデータベース管理者が、Azure Database for PostgreSQLのパフォーマンス監視や障害検知、リソース最適化のための分析を迅速に行うことが可能です。たとえば、急激な負荷上昇やクエリ遅延の兆候をダッシュボードで即座に把握し、迅速な対応につなげることができます。

注意点としては、組み込みダッシュボードの機能やカスタマイズ性が、独自に構築したGrafana環境と比較して制限される場合がある点が考えられます。また、利用可能なメトリックやアラート設定の範囲についても、Azure Monitorの仕様に依存するため、要件に応じた事前確認が必要です。

関連サービスとの連携については、Azure Monitorを中心としたAzureの監視エコシステムとシームレスに連携できるため、他のAzureリソースと統合した運用監視基盤の構築が容易になります。これにより、Azure環境全体の可観測性向上に寄与します。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=558140）を参照してください。

---

### 3. Public Preview: Customer‑managed encryption keys now supported on Premium SSD v2 disks for Azure Database for PostgreSQL 

**公開日時**: 2026年03月11日 18:00:35 UTC
**リンク**: [Public Preview: Customer‑managed encryption keys now supported on Premium SSD v2 disks for Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=557527)

**アップデートID**: 557527
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQLにおいて、Premium SSD v2ディスクでカスタマー管理キー（CMK）による暗号化がパブリックプレビューとしてサポートされました。

- 主な変更点や新機能  
これまでAzureが管理するキーによる暗号化が標準でしたが、今回のアップデートにより、ユーザー自身がAzure Key Vaultを利用して暗号化キーを管理できるようになりました。これにより、データの保存時暗号化（at-rest encryption）に対する制御性とセキュリティが強化されます。

- 影響を受ける対象  
Premium SSD v2ディスクを利用しているAzure Database for PostgreSQLのワークロードが対象となります。特に、コンプライアンス要件やセキュリティポリシーで独自のキー管理が求められるシナリオに有用です。

- 注意点があれば記載  
本機能は現在パブリックプレビュー段階であり、本番環境での利用には注意が必要です。また、利用にはAzure Key Vaultの設定や運用が必要となります。

**詳細**:

本アップデートは、Azure Database for PostgreSQLのワークロードにおいて、Premium SSD v2ディスクでカスタマー管理の暗号化キー（Customer-managed keys: CMK）を利用できるようになったことを示しています。これにより、保存データ（data at rest）の暗号化に対する制御性が向上し、ユーザー自身が管理する暗号化キーを用いて、より厳格なセキュリティポリシーを実現できるようになりました。本機能はパブリックプレビューとして提供されており、Azure環境でのデータセキュリティ強化を目的としています。

今回の変更により、Premium SSD v2ディスクをバックエンドストレージとして利用するAzure Database for PostgreSQLインスタンスにおいて、従来のMicrosoft管理キー（Microsoft-managed keys: MMK）による暗号化に加え、ユーザーがAzure Key Vaultで管理するカスタマー管理キーを暗号化に利用できるようになります。これにより、暗号化キーのローテーションやアクセス制御、監査などをユーザー自身が細かく設定・運用することが可能となります。

技術的な実装としては、Azure Key Vaultに格納されたカスタマー管理キーをPremium SSD v2ディスクの暗号化プロセスに組み込む形となります。ユーザーはKey Vaultでキーを生成・管理し、ディスクの暗号化設定時にそのキーを指定することで、ディスク上のデータが指定したCMKで暗号化されます。この仕組みにより、キーのライフサイクル管理やアクセス権限の制御を細かく行うことができ、コンプライアンス要件や内部統制の強化に寄与します。

活用シナリオとしては、金融、医療、公共機関など、高度なセキュリティやコンプライアンス要件が求められる業界において、データの暗号化キーを自社で管理したい場合に有効です。たとえば、特定の規制により暗号化キーの管理責任がユーザー側に求められるケースや、キーのローテーションや失効を独自のポリシーで運用したい場合に活用できます。

注意点としては、本機能はパブリックプレビュー段階であるため、商用環境での利用には慎重な検討が必要です。また、Premium SSD v2ディスクを利用しているAzure Database for PostgreSQLインスタンスが対象であり、他のディスクタイプやデータベースサービスでは利用できない点に留意する必要があります。さらに、CMKの管理にはAzure Key Vaultの適切な権限設定や運用管理が求められます。

関連するAzureサービスとしては、Azure Key Vaultが暗号化キーの管理基盤として必須となります。また、Azure Disk EncryptionやAzure RBAC（ロールベースアクセス制御）など、他のセキュリティ関連サービスと組み合わせることで、より強固なセキュリティアーキテクチャを構築できます。今回のアップデートにより、Azure Database for PostgreSQLのデータ保護に関する柔軟性と制御性が大きく向上しています。

---

### 4. Generally Available: Azure SRE Agent with new capabilities 

**公開日時**: 2026年03月11日 17:45:49 UTC
**リンク**: [Generally Available: Azure SRE Agent with new capabilities ](https://azure.microsoft.com/updates?id=558321)

**アップデートID**: 558321
**情報源**: Azure Updates API

**カテゴリ**: Launched, Features, Gallery, Open Source, Services

**要約**:

- 何が更新されたか  
Azure SRE Agentが一般提供（GA）となりました。

- 主な変更点や新機能  
Azure SRE AgentはAIを活用した運用エージェントで、システムの稼働率向上、インシデントの影響軽減、運用負荷の削減を支援します。GAリリースでは、障害診断の迅速化やレスポンスワークフローの自動化に加え、「deep context g」などの新機能が追加されています。

- 影響を受ける対象  
Azure上で運用管理やSRE（Site Reliability Engineering）業務を担当する技術者や運用チームが対象です。特に、インシデント対応や運用自動化を強化したい組織に有用です。

- 注意点があれば記載  
本機能の利用にはAzure環境への導入が必要です。詳細な機能や設定方法については公式ドキュメントを参照してください。新機能の一部は今後も継続的にアップデートされる可能性があります。

**詳細**:

Azure SRE Agentは、AIを活用した運用エージェントであり、今回一般提供（GA）となりました。本サービスの主な目的は、システムの稼働率向上、インシデントの影響低減、運用負荷の削減にあります。これを実現するために、障害発生時の診断プロセスを迅速化し、レスポンスワークフローの自動化を支援します。今回のGAリリースでは、「deep context g」と記載されている新機能が導入されており、これによりシステムの状況把握や障害発生時の根本原因分析が一層強化されています。

技術的には、Azure SRE AgentはAIベースのアルゴリズムを用いて、システムから収集した各種メトリックやログデータを解析します。これにより、異常検知やインシデントのトリアージを自動化し、運用担当者が迅速に対応できるよう支援します。また、インシデント発生時には、関連する情報を統合的に提示し、問題解決までのフローを効率化します。これらの機能は、Azureの既存の監視・運用サービスと連携することで、より包括的な運用自動化を実現します。

活用シナリオとしては、複数のAzureリソースを運用している大規模環境において、障害発生時の迅速なインシデント対応や、日常的な運用タスクの自動化が挙げられます。例えば、仮想マシンやアプリケーションサービスで発生したパフォーマンス異常を自動検知し、関連する情報を即座に運用担当者へ通知することで、対応までの時間を大幅に短縮できます。

注意点としては、AIによる自動化機能を活用するためには、十分な監視データやログがAzure上で正しく収集・保管されている必要があります。また、運用フローの自動化にあたっては、既存の運用プロセスとの整合性や、誤検知・過検知への対応方針の策定が求められます。

Azure SRE Agentは、Azure MonitorやAzure Logic Appsなどの他のAzureサービスと連携することで、より高度な自動化やインシデント管理が可能となります。これにより、運用現場の効率化とサービス品質の向上に貢献します。

---

### 5. Public Preview: Query Profiler in MSSQL extension for Visual Studio Code 

**公開日時**: 2026年03月11日 17:45:49 UTC
**リンク**: [Public Preview: Query Profiler in MSSQL extension for Visual Studio Code ](https://azure.microsoft.com/updates?id=558164)

**アップデートID**: 558164
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

- 何が更新されたか  
Visual Studio Code用MSSQL拡張機能に「Query Profiler」がパブリックプレビューとして追加されました。

- 主な変更点や新機能  
Query Profilerを利用することで、Visual Studio Code上でリアルタイムにデータベースのクエリやアクティビティをキャプチャし、分析できるようになりました。これにより、クエリのパフォーマンスや実行状況を可視化し、問題の特定や最適化が容易になります。

- 影響を受ける対象  
SQL ServerやAzure SQL DatabaseをVisual Studio Codeから操作している開発者やデータベース管理者が主な対象です。特に、クエリのチューニングやパフォーマンス分析を行う技術者にとって有用な機能です。

- 注意点があれば記載  
現在パブリックプレビュー段階のため、機能や操作性に一部制限や不具合がある可能性があります。本番環境での利用は慎重に検討してください。

**詳細**:

本アップデートは、Visual Studio Code用MSSQL拡張機能においてQuery Profilerがパブリックプレビューとして導入されたことを示しています。これにより、開発者やデータベース管理者はVisual Studio Codeの統合開発環境内で、リアルタイムにデータベースのクエリやアクティビティの状況を直接把握できるようになります。従来、SQL Server Management Studio（SSMS）などの専用ツールでしか利用できなかったクエリプロファイリング機能が、軽量なエディタ環境で利用可能となることで、開発フローの効率化が期待されます。

Query Profilerの主な機能としては、実行中のクエリやデータベースアクティビティのキャプチャが挙げられます。これにより、クエリのパフォーマンス分析やボトルネックの特定、実行計画の可視化が可能となります。Visual Studio Code内でこれらの情報を即座に取得できるため、開発者はコードの修正や最適化を迅速に行うことができます。

技術的には、MSSQL拡張機能がSQL Serverへの接続を通じて、クエリ実行時の統計情報やアクティビティデータを取得し、エディタ内で可視化する仕組みです。これにより、外部ツールへの切り替えが不要となり、開発環境を一元化できます。

活用シナリオとしては、アプリケーション開発中にパフォーマンスの悪いクエリを特定したい場合や、データベースの負荷状況をリアルタイムで監視したい場合などが考えられます。また、チーム開発においても、各開発者が自身の環境で即座にクエリの挙動を確認できるため、品質向上に寄与します。

注意点としては、本機能がパブリックプレビュー段階であるため、安定性や機能面で一部制限がある可能性がある点です。プロダクション環境での利用や、クリティカルな業務用途で deploy する際には十分な検証が必要です。

本機能は、Azure SQL DatabaseやAzure SQL Managed InstanceなどのAzure上のデータベースサービスとも連携可能です。これにより、クラウド上のデータベースに対しても、ローカル環境と同様にクエリプロファイリングを行うことができます。

詳細は公式アップデート情報（https://azure.microsoft.com/updates?id=558164）を参照してください。

---


*このレポートは自動生成されました - 2026-03-12 12:02:33 JST*