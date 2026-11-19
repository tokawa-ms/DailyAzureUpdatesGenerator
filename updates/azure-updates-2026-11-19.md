# 2026年11月19日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年11月19日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Public Preview: AI bot ruleset for Azure Front Door Premium WAF

**公開日時**: 2026年11月18日 18:27:29 UTC
**リンク**: [Public Preview: AI bot ruleset for Azure Front Door Premium WAF](https://azure.microsoft.com/updates?id=581604)

**アップデートID**: 581604
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Azure Front Door, Web Application Firewall, Features, Microsoft Ignite

**要約**:

【何が更新されたか】  
Azure Front Door PremiumのWeb Application Firewall（WAF）において、AIボットルールセットのパブリックプレビューが開始されました。

【主な変更点や新機能】  
AIボットルールセットを利用することで、AIクローラーやエージェントによるアクセスを細かく制御できるようになりました。従来のrobots.txtでは制御できないケースにも対応し、許可したいボットと拒否したいボットを柔軟に設定できます。

【影響を受ける対象】  
Azure Front Door Premiumを利用しているWebアプリケーションの管理者やセキュリティ担当者が対象となります。特にWAFを活用してボット対策を強化したい場合に有効です。

【注意点】  
本機能はパブリックプレビュー段階のため、商用環境での利用には慎重な検証が必要です。また、AIボットの識別や制御設定には十分な理解が求められます。

以上の内容により、Azure Front Door Premium WAFのボット管理機能が強化され、より高度なセキュリティ対策が可能となります。

**詳細**:

Azure Front Door PremiumのWeb Application Firewall（WAF）において、AI bot rulesetのパブリックプレビューが発表されました。本アップデートの背景には、Webサイトへのアクセスが多様化し、AIクローラーや各種エージェントによるアクセスが増加している現状があります。従来、robots.txtファイルを用いてクローラーのアクセス制御を行う方法が一般的でしたが、robots.txtは善意のクローラーにしか効果がなく、悪意のあるボットや意図しないAIエージェントのアクセスを防ぐことは困難でした。今回のAI bot rulesetは、これらの課題を解決するために導入されています。

具体的な機能として、Azure Front Door Premium WAFにAI bot rulesetが追加されることで、WebサイトにアクセスするAIクローラーやエージェントの識別および制御が可能となります。これにより、許可したいボットのみを通過させ、不要または悪意のあるボットのアクセスをブロックすることができます。従来のシグネチャベースのボット検出に加え、AIを活用したルールセットが適用されることで、より高度なボット管理が実現します。

技術的な仕組みとしては、Azure Front Door PremiumのWAFポリシーに新たなAI bot rulesetを適用することで、HTTPリクエストのヘッダーやパターンを解析し、AIクローラーやエージェントを識別します。これにより、従来の静的なルールでは検知できなかった新種のボットや変則的なアクセスパターンにも対応可能となります。設定はAzureポータルやARMテンプレートを通じて行うことができ、既存のWAFルールセットと組み合わせて運用することが可能です。

活用シナリオとしては、検索エンジンのクローラーは許可しつつ、スクレイピングや自動化された攻撃を行うボットをブロックしたい場合や、特定のAIエージェントによるアクセスのみを許可したい場合などが挙げられます。これにより、Webサイトのパフォーマンスやセキュリティを維持しつつ、必要なAIサービスとの連携を確保できます。

注意点として、パブリックプレビュー段階であるため、運用環境での利用には慎重な検証が必要です。また、AI bot rulesetによる判定の精度や挙動については、今後のアップデートやフィードバックによって改善される可能性があります。既存のWAFルールや他のセキュリティ機能との重複や競合にも注意が必要です。

本機能はAzure Front Door PremiumのWAF機能の一部として提供されており、他のAzureセキュリティサービスや監視機能と連携して利用することで、より包括的なWebアプリケーション防御を実現できます。

---

### 2. Announcing: The new Azure Databricks on Azure Government is now in Beta

**公開日時**: 2026年11月18日 18:01:03 UTC
**リンク**: [Announcing: The new Azure Databricks on Azure Government is now in Beta](https://azure.microsoft.com/updates?id=581645)

**アップデートID**: 581645
**情報源**: Azure Updates API

**カテゴリ**: AI + machine learning, Analytics, Azure Databricks, Microsoft Ignite, Announcement

**要約**:

- 何が更新されたか  
Azure DatabricksがAzure Government環境で新たにベータ版として利用可能になりました。

- 主な変更点や新機能  
これまでグローバルAzureで提供されていたAzure Databricksのデータ分析・AIプラットフォームが、米国公共機関向けのAzure Governmentで利用できるようになりました。Azure Databricksは、Apache Sparkベースの高速なデータ処理、機械学習、分析ワークロードをサポートする第一級サービスとして提供されます。

- 影響を受ける対象  
米国の公共機関やそのパートナーがAzure Government環境で高度なデータ分析やAIワークロードを実施できるようになります。Azure Governmentを利用している技術者やデータエンジニア、データサイエンティストが主な対象です。

- 注意点があれば記載  
現在はベータ版のため、本番環境での利用やサポート範囲に制限がある可能性があります。利用に際してはベータ版特有の制約や、今後の正式リリースに向けた変更点に注意してください。

**詳細**:

Azure DatabricksがMicrosoft Azure Government環境で新たにベータ提供されることが発表されました。本アップデートの背景には、米国公共機関およびそのパートナーがグローバルAzureで利用可能な最新のデータおよびAIプラットフォームを、Azure Government環境上で利用できるようにするという目的があります。Azure Governmentは、米国政府機関向けに設計されたクラウドサービスであり、厳格なセキュリティ基準やコンプライアンス要件を満たすことが求められています。今回のアップデートにより、Azure Databricksがこの環境に対応し、政府機関向けのデータ分析や機械学習ワークロードの実行が可能となります。

具体的な機能や変更内容としては、Azure DatabricksがAzure Governmentのインフラストラクチャ上で動作する点が挙げられます。これにより、データレイクの構築、ETL処理、ビッグデータ分析、機械学習モデルのトレーニングおよびデプロイなど、Databricksの主要機能を政府機関向けのセキュアなクラウド環境で利用できます。Azure Databricksは、Apache Sparkベースの分析プラットフォームであり、ノートブックによるコラボレーション、スケーラブルな計算リソース、データ統合機能を提供します。Azure Government環境での実装方法は、グローバルAzureと同様に、AzureポータルからDatabricksワークスペースを作成し、必要なリソースをプロビジョニングする形となります。

活用シナリオとしては、政府機関が保有する大量のデータを分析し、政策立案や業務効率化に役立てるケースが考えられます。例えば、公共サービスの利用状況分析、セキュリティログの解析、機械学習による異常検知などが挙げられます。また、パートナー企業が政府機関向けのデータ分析ソリューションを提供する際にも、Azure Databricks on Azure Governmentを活用することができます。

注意点や制限事項としては、現在ベータ版であるため、本番環境での利用には慎重な検証が必要です。また、Azure Government環境特有の制約や、グローバルAzureと異なる点が存在する可能性があります。利用に際しては、公式ドキュメントやサポート情報を参照し、最新の仕様や制限事項を確認することが重要です。

関連するAzureサービスとの連携については、Azure DatabricksはAzure Data Lake StorageやAzure Synapse Analytics、Azure Machine Learningなどと統合して利用することが可能です。これにより、データの蓄積、分析、可視化、機械学習モデルの運用までを一貫してAzure Government環境内で実現できます。今回のアップデートは、米国公共機関におけるデータ活用の幅を大きく広げるものとなっています。

---

### 3. Generally Available: Cross-subscription backup for Azure Virtual Machines in Azure Backup

**公開日時**: 2026年11月18日 18:00:04 UTC
**リンク**: [Generally Available: Cross-subscription backup for Azure Virtual Machines in Azure Backup](https://azure.microsoft.com/updates?id=581048)

**アップデートID**: 581048
**情報源**: Azure Updates API

**カテゴリ**: Launched, Management and governance, Storage, Azure Backup, Management, Microsoft Ignite, Feature

**要約**:

- 何が更新されたか  
Azure Backupで、Azure Virtual Machines（VM）のクロスサブスクリプションバックアップ機能が一般提供（GA）されました。

- 主な変更点や新機能  
同一テナント内で、異なるAzureサブスクリプションにあるRecovery Services Vaultを利用してVMのバックアップが可能になりました。これにより、バックアップ管理を一元化したり、複数サブスクリプション間で柔軟なバックアップ運用が実現できます。

- 影響を受ける対象  
Azure Virtual Machinesを利用しているユーザーや、複数サブスクリプションを運用している企業・組織が対象です。バックアップ運用やポリシー管理を統合したい管理者にとって有用な機能です。

- 注意点があれば記載  
Recovery Services Vaultは同一テナント内の異なるサブスクリプションに限り利用可能です。テナントを跨いだバックアップには対応していません。また、既存のバックアップ設定や運用ポリシーに影響がないか事前に確認することを推奨します。

**詳細**:

Azure Backupにおいて、Azure Virtual Machinesのクロスサブスクリプションバックアップ機能が一般提供開始されました。本アップデートの背景には、企業や組織が複数のAzureサブスクリプションを運用する中で、バックアップ管理の一元化や運用効率の向上が求められていたことがあります。従来は、バックアップ対象のVMとRecovery Services vaultが同一サブスクリプション内に存在する必要がありましたが、今回のアップデートにより、同一テナント内であれば異なるサブスクリプションに配置されたRecovery Services vaultを利用してVMのバックアップが可能となりました。

具体的な機能としては、Azure Virtual Machinesのバックアップ設定時に、バックアップ対象VMと異なるサブスクリプションに存在するRecovery Services vaultを選択できるようになります。これにより、組織内でバックアップポリシーやリソース管理を集中化したい場合や、部門ごとにサブスクリプションを分けて運用している場合でも、バックアップデータの保管先を統一することができます。技術的には、Azure Active Directoryテナント内でのリソース認証とアクセス制御を活用し、サブスクリプション間のバックアップ連携を実現しています。

実装方法としては、Azure PortalやAzure CLI、PowerShellを用いてバックアップ設定を行う際、Recovery Services vaultの選択画面で同一テナント内の他サブスクリプションのvaultが表示されるようになっています。これにより、バックアップジョブの管理や復旧操作も一元的に行うことが可能です。

活用シナリオとしては、例えば複数部門が独立したサブスクリプションでVMを運用している場合に、全社共通のRecovery Services vaultにバックアップを集約することで、バックアップ管理の統制やコスト最適化が図れます。また、セキュリティやコンプライアンス要件に応じてバックアップデータの保存先を柔軟に選択できる点もメリットです。

注意点としては、クロスサブスクリプションバックアップは同一Azure ADテナント内でのみ利用可能であり、異なるテナント間では利用できません。また、バックアップ設定や復旧操作時には、必要な権限（Recovery Services vaultへのアクセス権やVMのバックアップ権限）が適切に付与されている必要があります。

関連するAzureサービスとしては、Azure Backupの他、Recovery Services vault、Azure Virtual Machines、Azure Active Directoryが密接に連携しています。これらのサービス間での認証やアクセス制御が、クロスサブスクリプションバックアップの基盤となっています。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=581048）をご参照ください。

---

### 4. Public Preview: AI-powered application and database modernization with Modernize CLI

**公開日時**: 2026年11月18日 17:58:45 UTC
**リンク**: [Public Preview: AI-powered application and database modernization with Modernize CLI](https://azure.microsoft.com/updates?id=579943)

**アップデートID**: 579943
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**要約**:

【何が更新されたか】  
Modernize CLIのパブリックプレビューが開始されました。これは、アプリケーションとデータベースのモダナイゼーションを支援するCLIツールです。

【主な変更点や新機能】  
Modernize CLIは、アプリケーションのアーキテクチャや依存関係、クラウド移行の準備状況を評価します。また、アプリケーションが依存するデータベースを自動的に検出し、専門的な移行プロセスを実行できる点が特徴です。AIを活用して、アプリケーションとデータベースのモダナイゼーションを一貫してサポートします。

【影響を受ける対象】  
Azure上でアプリケーションやデータベースのモダナイゼーションやクラウド移行を検討している技術者や開発者が主な対象です。既存システムのクラウド対応や移行作業を効率化したい場合に有用です。

【注意点】  
現時点ではパブリックプレビューの段階であり、本番環境での利用には注意が必要です。機能やサポート範囲は今後変更される可能性があります。

**詳細**:

本アップデートは、「Modernize CLI」のパブリックプレビュー公開に関するものです。Modernize CLIは、アプリケーションとデータベースのモダナイゼーションを一体化したプロセスとして提供されます。従来、アプリケーションのクラウド移行やモダナイゼーションは、アプリケーション本体とその依存するデータベースを個別に評価・移行する必要がありましたが、本CLIはこれらを連携させ、統合的な移行・モダナイゼーションを実現することを目的としています。

具体的な機能としては、Modernize CLIがアプリケーションのアーキテクチャ、依存関係、クラウド対応状況を評価します。また、アプリケーションが依存しているデータベースを自動的に検出し、専門的な処理を呼び出すことが可能です。これにより、アプリケーションとデータベースの移行やモダナイゼーションの全体像を把握しやすくなり、移行計画の策定や実施が効率化されます。

技術的な仕組みとしては、CLIツールがアプリケーションの構成情報や依存関係を解析し、クラウド対応度を評価します。さらに、アプリケーションが利用しているデータベースを検出し、必要に応じてデータベースのモダナイゼーションや移行を支援する機能を備えています。これらの機能は、Azure上でのクラウド移行やモダナイゼーションを前提とした設計となっています。

活用シナリオとしては、オンプレミス環境やレガシーシステムからAzureへの移行を検討している場合、Modernize CLIを用いることで、アプリケーションとデータベースの現状評価から移行計画の立案、実施までを一貫して支援することが可能です。例えば、複数の依存データベースを持つ業務アプリケーションをAzureへ移行する際、CLIによる自動評価と検出機能を活用することで、移行対象の特定やクラウド適合性の確認作業を効率化できます。

注意点としては、現時点ではパブリックプレビュー段階であるため、機能や対応範囲に制限がある可能性があります。また、CLIツールの利用にはAzure環境へのアクセス権や適切な権限設定が必要です。さらに、アプリケーションやデータベースの構成によっては、検出や評価が完全に自動化されない場合も想定されます。

関連するAzureサービスとしては、Azure Database Migration ServiceやAzure App Service、Azure SQL Databaseなど、アプリケーションおよびデータベースの移行・モダナイゼーションを支援する各種サービスとの連携が考えられます。Modernize CLIはこれらのサービスと組み合わせて利用することで、より高度なクラウド移行やモダナイゼーションを実現できます。

---


*このレポートは自動生成されました - 2026-11-19 12:01:46 JST*