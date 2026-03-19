# 2026年03月19日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年03月19日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 10 件

## 更新一覧

### 1. Retirement: Emissions Impact Dashboard for Azure

**公開日時**: 2026年03月18日 18:45:54 UTC
**リンク**: [Retirement: Emissions Impact Dashboard for Azure](https://azure.microsoft.com/updates?id=558278)

**アップデートID**: 558278
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

- 何が更新されたか  
Emissions Impact Dashboard for Azure（Power BI で提供されているAzureの排出量インパクトダッシュボード）が2027年3月31日をもって廃止されることが発表されました。

- 主な変更点や新機能  
本ダッシュボードは2027年3月31日以降利用できなくなり、以降はアクセス不可となります。また、技術サポートも終了します。新機能の追加はありません。

- 影響を受ける対象  
現在Emissions Impact Dashboard for Azureを利用している全てのユーザーおよび組織が影響を受けます。特に、Azureのカーボン排出量レポートや分析を本ダッシュボードで行っている技術者や管理者が該当します。

- 注意点  
2027年3月31日以降はダッシュボードへのアクセスができなくなり、サポートも受けられません。必要なデータは事前にエクスポートしておくことが強く推奨されています。今後の代替手段については、公式情報の確認をおすすめします。

**詳細**:

本アップデートは、「Emissions Impact Dashboard for Azure」が2027年3月31日をもって廃止されることを告知するものです。Emissions Impact Dashboard for Azureは、Power BI上で提供されてきたダッシュボードであり、Azure環境における排出量の可視化を目的としたサービスです。これにより、利用者は自組織のAzureリソースが生み出すカーボンフットプリントを定量的に把握し、サステナビリティ目標の達成やレポーティングに活用することができました。

今回のアップデートの背景には、サービスのライフサイクル管理や、今後の機能統合・刷新などが考えられますが、詳細な目的については公式情報に記載されていません。2027年3月31日以降は、当該ダッシュボードへのアクセスができなくなり、技術サポートも提供されなくなります。そのため、現在ダッシュボードを利用しているユーザーは、必要なデータやレポートを事前にエクスポートすることが強く推奨されています。

Emissions Impact Dashboard for Azureは、Power BIを活用してAzureのリソース消費データを集約・可視化する仕組みを持ちます。Azureの各種サービス利用状況をもとに、推定排出量を算出し、グラフィカルなレポートとして提示することで、組織の環境負荷を分析することが可能でした。技術的には、Azureから取得したデータをPower BIに連携し、ダッシュボードとして構築・配信する形態を取っています。

本ダッシュボードは、企業のサステナビリティ担当者やクラウド管理者が、Azure利用に伴う環境インパクトを定量的に評価し、社内外への報告や改善活動の根拠データとして活用するシナリオが想定されていました。例えば、月次や四半期ごとにAzure利用によるCO2排出量をレポートし、クラウド最適化やグリーンIT推進の指標として利用するケースが一般的です。

廃止に伴い、2027年3月31日以降はダッシュボードへのアクセスが完全に停止されるため、過去のデータやカスタムレポートを保持したい場合は、事前にエクスポート作業を行う必要があります。また、廃止後は技術的な問い合わせやサポートも受けられなくなるため、運用上の注意が必要です。

Emissions Impact Dashboard for Azureは、Azureの各種サービスと連携してデータを取得していましたが、今後は代替手段の検討や他のAzureサービスとの連携方法の見直しが必要となります。現時点では、後継サービスや移行先についての案内はありません。詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=558278）を参照してください。

---

### 2. General availability: Azure SQL updates for mid-March 2026 

**公開日時**: 2026年03月18日 18:30:05 UTC
**リンク**: [General availability: Azure SQL updates for mid-March 2026 ](https://azure.microsoft.com/updates?id=558121)

**アップデートID**: 558121
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

【Azure SQL 2026年3月中旬アップデート要約】

■ 何が更新されたか  
Azure SQLに対して、2026年3月中旬に新機能と改善が一般提供（GA）されました。

■ 主な変更点や新機能  
1. Visual Studio CodeからSQLデータベースプロジェクトを直接発行できるようになりました。これにより、データベースのデプロイメントワークフローが効率化されます。  
2. MSSQLでSQLテーブルデータを直接閲覧・編集できる機能が追加されました。これにより、データ操作がより直感的に行えるようになります。

■ 影響を受ける対象  
Azure SQL Databaseを利用している開発者やDBA、特にVisual Studio Codeを用いて開発・運用している技術者が対象です。

■ 注意点  
新機能の利用には最新バージョンのVisual Studio Codeおよび関連拡張機能が必要となる場合があります。既存のデプロイメントフローやデータ操作手順に影響が出る可能性があるため、事前にテスト環境で動作確認を行うことを推奨します。

**詳細**:

2026年3月中旬に、Azure SQLに対して複数のアップデートと機能強化が実施されました。今回のアップデートの背景には、開発者やデータベース管理者の作業効率向上と、より直感的かつ迅速なデータベース運用を実現する目的があります。従来、SQLデータベースプロジェクトのデプロイメントやテーブルデータの編集作業は、複数のツールや手順を必要とする場合が多く、運用の複雑化や作業時間の増大が課題となっていました。これらの課題を解消するため、Azure SQLは開発環境との連携強化と操作性の向上を図っています。

具体的な機能変更として、Visual Studio CodeからSQLデータベースプロジェクトを直接公開できる機能が追加されました。これにより、開発者はVisual Studio Code上でプロジェクトを管理し、そのままAzure SQLへデプロイすることが可能となります。従来は、SQL Server Data Toolsや他の専用ツールを経由してデプロイする必要がありましたが、このアップデートによりワークフローが大幅に簡略化され、CI/CDパイプラインの構築や運用が効率化されます。技術的な仕組みとしては、Visual Studio Codeの拡張機能を活用し、Azure SQLへの接続情報やデプロイメント設定をGUIまたはコマンドラインで指定することで、プロジェクトの公開が実現されています。

また、MSSQ（Microsoft SQL）環境において、SQLテーブルデータを直接閲覧・編集できる機能が追加されました。これにより、データベース管理者や開発者は、テーブルデータの内容を即座に確認し、必要に応じてデータの修正を行うことができます。従来は、SQLクエリを手動で作成してデータの参照や更新を行う必要がありましたが、この機能によってGUIベースで直感的な操作が可能となり、データ管理の効率が向上します。

活用シナリオとしては、開発環境から本番環境へのデータベースプロジェクトの迅速なデプロイメントや、テストデータの即時編集、運用中のデータベースのトラブルシューティングなどが挙げられます。これらの機能は、Azure DevOpsやGitHub ActionsなどのCI/CDサービスと組み合わせることで、より高度な自動化や運用効率化を実現できます。

注意点としては、Visual Studio Codeからのデプロイメントやテーブルデータ編集機能を利用する際には、適切な権限設定やセキュリティ対策が必要です。特に本番環境での操作は、誤操作によるデータ損失やセキュリティリスクを防ぐため、アクセス制御や監査ログの活用が推奨されます。

今回のアップデートは、Azure SQLの運用効率と開発体験を大きく向上させるものであり、Azureの他サービスとの連携を強化することで、クラウドベースのデータベース運用をより柔軟かつ安全に実現することが可能です。

---

### 3. Generally Available: Azure Red Hat OpenShift Managed Identity and Workload Identity

**公開日時**: 2026年03月18日 18:30:05 UTC
**リンク**: [Generally Available: Azure Red Hat OpenShift Managed Identity and Workload Identity](https://azure.microsoft.com/updates?id=557917)

**アップデートID**: 557917
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Red Hat OpenShift, Compliance, Management

**要約**:

- 何が更新されたか  
Azure Red Hat OpenShift（ARO）で、Managed IdentityおよびWorkload Identityのサポートが一般提供（GA）となりました。

- 主な変更点や新機能  
これにより、OpenShiftクラスターやアプリケーションが、長期間有効なService Principalの資格情報を使用せずにAzureリソースへアクセスできるようになりました。Managed IdentityとWorkload Identityを活用することで、認証情報の管理が容易になり、セキュリティが向上します。

- 影響を受ける対象  
Azure Red Hat OpenShiftを利用しているユーザーおよび、OpenShift上でAzureリソースへのアクセスが必要なアプリケーションを運用している技術者が対象です。

- 注意点があれば記載  
既存のService Principalベースの認証から移行する場合は、設定変更や動作確認が必要です。導入にあたっては、公式ドキュメントを参照し、各機能の利用条件や制約事項を確認してください。

**詳細**:

Azure Red Hat OpenShiftにおいて、Managed IdentityおよびWorkload Identityのサポートが一般提供（GA）となりました。このアップデートの背景には、従来のサービスプリンシパルによる認証方式が持つ長期間有効な認証情報の管理負荷やセキュリティリスクの軽減が挙げられます。Azure Red Hat OpenShiftクラスタやアプリケーションをAzure上で運用する際、これまで必要だったサービスプリンシパルの資格情報を長期間保持する必要がなくなり、より安全かつ効率的な認証方式を利用できるようになりました。

具体的な機能としては、Azure Managed Identityを利用することで、OpenShiftクラスタやその上で稼働するアプリケーションがAzureリソースにアクセスする際、Azure ADによって自動的に認証情報が管理されます。Workload Identityは、クラスタ内のワークロードごとに個別のアイデンティティを割り当てることができ、細粒度なアクセス制御が可能となります。これにより、各ワークロードが必要な権限のみを持つ形でAzureリソースへアクセスできるため、最小権限の原則を実現しやすくなります。

技術的な仕組みとしては、Managed IdentityはAzure ADと連携し、OpenShiftクラスタやアプリケーションがAzureリソースにアクセスする際に、動的にアクセストークンを取得します。Workload Identityは、KubernetesのサービスアカウントとAzure ADのアイデンティティをマッピングすることで、Podごとに異なる認証情報を割り当てることが可能です。これらの機能は、AzureのIAM（Identity and Access Management）と密接に連携して動作します。

活用シナリオとしては、例えばOpenShift上で稼働するアプリケーションがAzure Key VaultやAzure Storage、Azure SQL Databaseなどのリソースにアクセスする場合、従来はサービスプリンシパルの資格情報をアプリケーションに組み込む必要がありましたが、Managed IdentityやWorkload Identityを利用することで、資格情報の管理やローテーションが不要となり、運用負荷とセキュリティリスクが大幅に低減します。

注意点としては、Managed IdentityやWorkload Identityの利用には、Azure ADやKubernetesの設定が正しく行われている必要があります。また、既存のサービスプリンシパル認証方式から移行する場合、アプリケーション側の認証ロジックやアクセス権限の見直しが必要となる場合があります。

関連するAzureサービスとの連携については、Managed IdentityやWorkload IdentityはAzure Key Vault、Azure Storage、Azure SQL Databaseなど、Azureの主要なリソースとシームレスに統合されており、これらのリソースへのアクセス権限管理をより効率的かつ安全に行うことができます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=557917）をご参照ください。

---

### 4. Public preview: GitHub Copilot integration in Schema Designer for the MSSQL extension 

**公開日時**: 2026年03月18日 18:15:04 UTC
**リンク**: [Public preview: GitHub Copilot integration in Schema Designer for the MSSQL extension ](https://azure.microsoft.com/updates?id=558169)

**アップデートID**: 558169
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

- 何が更新されたか  
Visual Studio Code用MSSQL拡張機能のSchema Designerに、GitHub Copilotとの連携機能がパブリックプレビューとして追加されました。

- 主な変更点や新機能  
Schema Designer内でGitHub CopilotのAI支援を利用できるようになり、スキーマ設計時の提案やコード補完などのサポートが受けられます。これにより、スキーマ設計作業の効率化や品質向上が期待できます。

- 影響を受ける対象  
Visual Studio Code上でMSSQL拡張機能を利用している開発者やデータベース設計者が対象です。特にスキーマ設計作業を行うユーザーにとって有用なアップデートです。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、動作の安定性や一部機能に制限がある可能性があります。また、GitHub Copilotの利用には別途ライセンス契約が必要な場合があります。

**詳細**:

本アップデートは、Visual Studio Code向けのMSSQL拡張機能において、Schema DesignerにGitHub Copilotの統合がパブリックプレビューとして提供開始されたことを示しています。この統合の背景には、開発者からのフィードバックやワークフローの進化があり、より効率的かつ直感的なスキーマ設計体験を実現することが目的とされています。

具体的な変更内容としては、Schema Designer内でGitHub CopilotのAI支援機能が利用可能となり、スキーマ設計作業においてAIによる提案や補助が受けられるようになりました。これにより、テーブル設計やリレーションシップの構築、カラム定義などの作業時に、自然言語による説明やコード補完、設計案の提案など、CopilotのAIがリアルタイムで支援を行います。

技術的な仕組みとしては、Visual Studio CodeのMSSQL拡張機能とGitHub Copilotサービスが連携し、ユーザーの操作や入力内容をもとにAIモデルが適切な提案を生成します。Schema DesignerのUI上でCopilotからのサジェストが表示され、ユーザーはそれを選択・編集してスキーマ設計に反映できます。GitHub Copilot自体はクラウド上のAIサービスとして動作し、Visual Studio Codeの拡張機能経由でAPIを介してやり取りが行われます。

活用シナリオとしては、データベース設計の初期段階でテーブルやカラムの定義を効率化したい場合や、既存のスキーマに対して最適な変更案を得たい場合、またはSQLのベストプラクティスに基づいた設計をAIから提案してもらいたい場合などが挙げられます。特に、スキーマ設計に不慣れな開発者や、設計作業の生産性向上を目指すチームにとって有用です。

注意点や制限事項としては、現時点ではパブリックプレビュー段階であるため、機能の安定性や精度に関しては今後の改善が見込まれます。また、GitHub Copilotの利用には別途ライセンスやアカウントが必要となる場合があります。さらに、AIによる提案内容は必ずしも正確または最適とは限らないため、最終的な設計判断は開発者自身が行う必要があります。

関連するAzureサービスとの連携については、MSSQL拡張機能自体がAzure SQL DatabaseやSQL Serverと連携可能であり、Schema Designerで設計したスキーマをAzure上のデータベースに適用することができます。これにより、クラウド上でのデータベース開発・運用の効率化が期待できます。

---

### 5. Public Preview: Database DevOps in SSMS powered by SQL projects 

**公開日時**: 2026年03月18日 18:15:04 UTC
**リンク**: [Public Preview: Database DevOps in SSMS powered by SQL projects ](https://azure.microsoft.com/updates?id=558155)

**アップデートID**: 558155
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

- 何が更新されたか  
SQL Server Management Studio（SSMS）において、「Database DevOps in SSMS powered by SQL projects」がパブリックプレビューとして提供開始されました。

- 主な変更点や新機能  
SQLプロジェクト機能がSSMSに統合され、データベーススキーマをソース管理できるようになりました。これにより、スキーマのコード化（schema-as-code）が可能となり、信頼性の高いデプロイメントや、開発プロセスへのコード品質チェックの統合が実現します。あらゆる環境へのデプロイもサポートされます。

- 影響を受ける対象  
SSMSを利用してSQL ServerやAzure SQL Databaseの開発・運用を行う技術者や、データベースのDevOpsプロセスを強化したい開発チームが対象です。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用は慎重に検討してください。機能やUIが今後変更される可能性があります。

詳細は公式アップデートページをご参照ください。

**詳細**:

本アップデートは、「Database DevOps in SSMS powered by SQL projects」のパブリックプレビューに関するものです。今回のアップデートの背景には、データベース開発において「スキーマをコードとして管理する」手法（schema-as-code）の導入が求められていることがあります。これにより、アプリケーション開発と同様に、データベースのスキーマ変更をバージョン管理し、信頼性の高いデプロイメントやコード品質のチェックを実現することが目的です。

具体的には、SQL Server Management Studio（SSMS）上でSQLプロジェクトを活用したDatabase DevOpsの機能が利用可能となります。SQLプロジェクトは、データベーススキーマをプロジェクトファイルとして管理し、ソースコントロールシステム（例：Git）と連携することで、スキーマの変更履歴を追跡できます。これにより、複数の開発者が同時にデータベース開発を行う場合でも、変更の競合や品質低下を防ぎやすくなります。また、SQLプロジェクトを利用したデプロイメントにより、任意の環境（開発、テスト、本番など）への一貫したスキーマ適用が可能です。さらに、開発フローの中でコード品質チェックを組み込むことができるため、スキーマ変更の品質を担保しやすくなります。

技術的な仕組みとしては、SSMS内でSQLプロジェクトを作成・管理し、プロジェクトファイルをソースコントロールに登録します。デプロイメント時には、プロジェクトから差分スクリプトを生成し、ターゲット環境に適用します。これにより、手動によるスクリプト管理の手間やミスを削減できます。

活用シナリオとしては、複数人でのデータベース開発やCI/CDパイプラインへの統合が挙げられます。例えば、アプリケーションコードと同様にPull Requestベースでスキーマ変更をレビューし、承認後に自動デプロイメントを実施する、といった運用が可能です。

注意点としては、現時点でパブリックプレビューであるため、本番環境での利用は推奨されません。また、利用可能な機能やサポート範囲に制限がある場合がありますので、事前に公式ドキュメントやアップデート情報を確認することが重要です。

関連するAzureサービスとの連携については、SQL DatabaseやAzure DevOpsなどと組み合わせることで、より高度なDevOps運用が実現できます。例えば、Azure DevOpsのパイプラインを利用して、SQLプロジェクトのビルドやデプロイメントを自動化することが可能です。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=558155）を参照してください。

---

### 6. Public Preview: SQL MCP Server

**公開日時**: 2026年03月18日 18:15:04 UTC
**リンク**: [Public Preview: SQL MCP Server](https://azure.microsoft.com/updates?id=558150)

**アップデートID**: 558150
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

- 何が更新されたか  
SQL MCP Serverのパブリックプレビューが発表されました。これは、Model Context Protocol (MCP) コネクタを利用した、プロダクションデータベース向けの新しい機能です。

- 主な変更点や新機能  
SQL MCP Serverは、Data API Builder (DAB) の機能拡張として提供され、AIエージェントをデータワークフローに安全かつシンプルに統合できるようになります。これにより、AIベースのアプリケーションやサービスが、MCPプロトコルを通じて既存のSQLデータベースと連携しやすくなります。

- 影響を受ける対象  
既存のSQLデータベースを運用している技術者や、Data API Builder (DAB) を利用している開発者、またはAIエージェントとのデータ連携を検討しているユーザーが対象です。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用には十分な検証が必要です。また、MCPプロトコルやDABのバージョン互換性についても事前に確認することを推奨します。

**詳細**:

本アップデートは、SQL MCP Serverのパブリックプレビュー開始を発表するものです。SQL MCP Serverは、Model Context Protocol（MCP）コネクタとして、プロダクションデータベースに対してAIエージェントを安全かつ予測可能な方法で組み込むことを目的としています。本機能はData API Builder（DAB）の主要コンポーネントの一つとして提供され、データワークフローにAIの力をシームレスに統合することを支援します。

SQL MCP Serverの主な特徴は、AIエージェントが既存のデータベースにアクセスし、データの取得や操作を行う際のセキュリティと一貫性を確保する点にあります。MCPコネクタとして動作することで、AIエージェントがデータベースのコンテキストを理解し、適切なデータ操作を実行できるように設計されています。これにより、AIを活用した自動化やデータ分析のワークフローを、従来よりも簡単かつ安全に実装することが可能となります。

技術的には、SQL MCP ServerはData API Builderの拡張機能として実装されており、既存のDAB環境に組み込むことで利用できます。DABは、REST APIやGraphQL APIを通じてデータベースリソースへのアクセスを抽象化するミドルウェアであり、SQL MCP Serverはこの仕組みを活用してAIエージェントとの連携を実現します。これにより、AIエージェントは直接データベースにアクセスすることなく、DABを介して安全にデータ操作を行うことができます。

活用シナリオとしては、AIエージェントによるデータ分析の自動化、インテリジェントなデータフィードバックループの構築、またはAIによるデータベース運用支援などが考えられます。たとえば、チャットボットや業務自動化エージェントが、SQL MCP Serverを通じてリアルタイムにデータベースの情報を取得し、業務プロセスを効率化することが可能です。

注意点としては、現時点ではパブリックプレビュー段階であるため、本番環境での利用には慎重な検証が必要です。また、DABおよびMCPコネクタのバージョン互換性や、セキュリティ設定の適切な構成が求められます。

関連するAzureサービスとしては、Azure SQL DatabaseやData API Builderが挙げられます。これらのサービスと組み合わせることで、クラウドネイティブなAIデータワークフローの構築が容易になります。

詳細については、公式アップデートページ（https://azure.microsoft.com/updates?id=558150）を参照してください。

---

### 7. Generally Available: GitHub Copilot in SQL Server Management Studio 22 

**公開日時**: 2026年03月18日 18:15:04 UTC
**リンク**: [Generally Available: GitHub Copilot in SQL Server Management Studio 22 ](https://azure.microsoft.com/updates?id=558134)

**アップデートID**: 558134
**情報源**: Azure Updates API

**カテゴリ**: Launched, Features

**要約**:

【何が更新されたか】  
GitHub CopilotがSQL Server Management Studio（SSMS）22で一般提供（GA）されました。

【主な変更点や新機能】  
SSMS 22内でGitHub CopilotのAI支援機能が利用可能となり、自然言語を用いてSQLコードの作成、説明、修正などが行えるようになりました。これにより、SQLクエリの生成やトラブルシューティングが効率化されます。

【影響を受ける対象】  
SSMS 22を利用しているSQL Server管理者や開発者が対象です。日常的にSSMSを使用している技術者は、CopilotのAI機能による生産性向上や作業効率化の恩恵を受けることができます。

【注意点】  
GitHub Copilotの利用には、対応するライセンスや設定が必要です。また、AIによるコード生成の結果は必ずレビューし、セキュリティやパフォーマンス面で問題がないか確認することを推奨します。

**詳細**:

本アップデートは、GitHub CopilotがSQL Server Management Studio（SSMS）22において一般提供（GA）となったことを示しています。これにより、SSMS 22を利用する技術者は、日常的に使用するデータベース管理ツール内で、AIによる支援機能を直接活用できるようになりました。アップデートの背景には、開発者やデータベース管理者がSQLクエリの作成や修正、理解をより効率的かつ正確に行えるようにするという目的があります。

具体的な機能としては、GitHub Copilotが自然言語入力を受け付け、それを基にSQLクエリの生成、既存クエリの説明、バグ修正などを支援します。ユーザーは英語などの自然言語で意図を記述するだけで、Copilotが適切なSQLコードを提案し、開発作業の効率化を実現します。また、既存のSQLコードの内容を分かりやすく説明したり、潜在的な問題点を指摘したりする機能も提供されます。

技術的な仕組みとしては、GitHub CopilotはOpenAIの大規模言語モデルを基盤としており、SSMS 22の拡張機能として統合されています。ユーザーがSSMS内でCopilotを有効化することで、エディタ上で直接AIによるコード補完や提案を受けることが可能です。これにより、従来の手動によるクエリ作成やデバッグ作業が大幅に効率化されます。

活用シナリオとしては、複雑なSQLクエリの作成や最適化、既存のストアドプロシージャやビューの理解、エラー発生時の修正案の提示などが挙げられます。たとえば、データベースのパフォーマンスチューニングや新規テーブル設計時に、自然言語で要件を記述するだけで、Copilotが最適なSQL文を提案してくれるため、開発スピードの向上と品質の担保が期待できます。

注意点としては、Copilotが生成するコードや説明はあくまでAIによる提案であり、最終的な検証やレビューは開発者自身が行う必要があります。また、組織のセキュリティポリシーやデータガバナンス要件に従い、AIによるコード生成の利用範囲を適切に管理することが重要です。

関連するAzureサービスとの連携については、SSMS自体がAzure SQL DatabaseやAzure SQL Managed InstanceなどのAzureベースのデータベースサービスに対応しているため、Copilotの支援機能をこれらのクラウドデータベース管理にも活用できます。これにより、オンプレミスとクラウド双方のデータベース運用において、統一的かつ効率的な開発体験を実現します。

---

### 8. Generally Available: Lakeflow Connect Free Tier now available in Azure Databricks  

**公開日時**: 2026年03月18日 17:00:05 UTC
**リンク**: [Generally Available: Lakeflow Connect Free Tier now available in Azure Databricks  ](https://azure.microsoft.com/updates?id=558810)

**アップデートID**: 558810
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Analytics, Azure Databricks, Features

**要約**:

- 何が更新されたか  
Azure Databricksにおいて、Lakeflow ConnectのFree Tierが一般提供（GA）となりました。

- 主な変更点や新機能  
Lakeflow Connect Free Tierでは、各ワークスペースごとに1日あたり100 DBU（Databricks Unit）が無償で提供されます。この枠内で、SaaSアプリケーションやデータベースからのデータインジェスト（取り込み）が可能です。これにより、1ワークスペースあたり1日約1億レコードのデータを取り込むことができます。

- 影響を受ける対象  
Azure Databricksを利用している組織や開発者、特にSaaSや各種データベースから大量データを取り込みたいユーザーが対象です。コストを抑えつつデータ連携を試したい場合に有用です。

- 注意点があれば記載  
Free Tierの利用は1ワークスペースあたり1日100 DBUまでに制限されています。これを超える場合は追加の課金が発生しますので、利用量には注意が必要です。

**詳細**:

Azure Databricksにおいて、Lakeflow Connect Free Tierが一般提供（GA）されたことにより、各ワークスペースごとに1日あたり100DBU（Databricks Unit）が無償で付与されるようになりました。このアップデートの背景には、データエンジニアリングやデータ分析の現場で、SaaSアプリケーションや各種データベースからのデータ取り込み（インジェスト）のニーズが高まっていることがあります。Lakeflow Connect Free Tierは、これらのニーズに応えるため、コストを気にせずにデータ連携を試行・導入できる環境を提供することを目的としています。

具体的な機能としては、Lakeflow Connectを利用することで、SaaSアプリケーションやデータベースからAzure Databricksのワークスペースへデータを取り込む際に、1日あたり100DBUまで無償で利用可能となります。これにより、1ワークスペースにつき約1億件のレコードを1日で取り込むことが可能です。DBUはDatabricksのリソース消費量を示す単位であり、Free Tierではこの消費量の範囲内でLakeflow Connectの機能を利用できます。

技術的な仕組みとしては、Lakeflow Connectが提供するコネクタを用いて、各種SaaSアプリケーションやデータベースとAzure Databricksを連携させ、データのインジェスト処理を自動化します。これにより、データエンジニアは複雑なETL処理やカスタムスクリプトの作成を省略でき、迅速かつ効率的にデータを取り込むことが可能です。Lakeflow ConnectはDatabricksのワークスペース単位で管理されるため、複数のワークスペースで同時にFree Tierを活用することもできます。

活用シナリオとしては、データ分析基盤の構築初期段階や、PoC（概念実証）環境でのデータ連携の検証、または小規模なデータ取り込みニーズに対応する場合などが考えられます。例えば、SalesforceやDynamics 365などのSaaSアプリケーションからデータを取り込み、Databricks上で分析や機械学習モデルのトレーニングを行うケースで、Free Tierを利用することでコストを抑えつつ迅速なデータ連携が可能となります。

注意点としては、Free Tierの利用上限が1日あたり100DBUであるため、これを超過する場合は追加のコストが発生します。また、1ワークスペースごとに上限が設定されているため、大規模なデータ取り込みや複数ワークスペースでの利用時には、DBU消費量の管理が必要です。さらに、Lakeflow Connect Free Tierはインジェスト処理に限定されているため、他のDatabricks機能や高度なデータ処理には別途リソースや課金が必要となります。

関連するAzureサービスとしては、Azure Databricks自体がAzure Data Lake StorageやAzure Synapse Analyticsなどと連携可能であり、Lakeflow Connectを通じて取り込んだデータをこれらのサービスと組み合わせて活用することができます。これにより、データの一元管理や高度な分析、レポーティングなどの統合的なデータ活用が実現します。

以上のように、Lakeflow Connect Free Tierの一般提供は、Azure Databricks環境でのデータ連携をより手軽かつ低コストで実現するための重要なアップデートです。

---

### 9. Generally Available: Versionless key support for transparent data encryption in Azure SQL Database 

**公開日時**: 2026年03月18日 17:00:05 UTC
**リンク**: [Generally Available: Versionless key support for transparent data encryption in Azure SQL Database ](https://azure.microsoft.com/updates?id=558183)

**アップデートID**: 558183
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

- 何が更新されたか  
Azure SQL Databaseの透過的データ暗号化（TDE）で、バージョンレスキーのサポートが一般提供（GA）されました。

- 主な変更点や新機能  
これまでTDEでカスタマーマネージドキー（CMK）を利用する場合、Azure Key VaultやManaged HSM内の特定のキーのバージョンを参照する必要がありました。今回のアップデートにより、キーのバージョンを指定せずにバージョンレスキーを利用できるようになり、キー管理がよりシンプルかつ信頼性の高いものになりました。

- 影響を受ける対象  
Azure SQL DatabaseでTDEとカスタマーマネージドキー（BYOK）を利用しているユーザーや、今後導入を検討している技術者が対象です。

- 注意点があれば記載  
バージョンレスキーを利用することで、キーのローテーションや管理が容易になりますが、既存の運用フローやセキュリティポリシーへの影響について事前に確認することを推奨します。また、詳細な利用方法や制限事項については公式ドキュメントを参照してください。

**詳細**:

Azure SQL Databaseにおいて、透過的データ暗号化（TDE）のためのバージョンレスキーサポートが一般提供となりました。このアップデートの背景には、暗号化キー管理の簡素化と信頼性向上があります。従来はAzure Key VaultやManaged HSMに保存された暗号化キーの特定バージョンを明示的に参照する必要がありましたが、今回の変更により、キーのバージョンを指定せずに管理できるようになりました。これにより、キーのローテーションや更新時にアプリケーションやデータベースの設定変更が不要となり、運用負荷が大幅に軽減されます。

具体的な機能としては、Azure SQL DatabaseのTDE設定時に、Azure Key VaultやManaged HSMに格納された暗号化キーのバージョンを指定することなく、キーの参照が可能となります。これにより、キーの更新やローテーションが発生しても、データベース側では自動的に最新のキーが利用されるため、セキュリティと可用性が向上します。技術的な仕組みとしては、Azure SQL Databaseがキー管理サービスと連携し、バージョンレスでキーを取得することで、暗号化処理を継続的に実施します。

実際の活用シナリオとしては、金融や医療など高いセキュリティ要件を持つ業界で、暗号化キーの頻繁なローテーションが求められる場合に有効です。キーのバージョン管理から解放されることで、運用管理者はセキュリティポリシーに従ったキーの更新を容易に実施でき、アプリケーションやデータベースの設定変更によるダウンタイムやリスクを回避できます。

注意点としては、バージョンレスキーの利用にあたっては、Azure Key VaultやManaged HSMのアクセス権限設定や監査ログ管理が重要となります。キーのローテーションや削除時には、適切な権限管理と監査が求められます。また、バージョンレスキーのサポートはAzure SQL DatabaseのTDEに限定されており、他の暗号化機能やサービスでは従来通りバージョン指定が必要な場合があります。

関連するAzureサービスとの連携としては、Azure Key VaultやManaged HSMが暗号化キーの保存・管理を担い、Azure SQL Databaseがこれらのサービスと連携してTDEを実現します。これにより、セキュリティポリシーに基づいたキー管理とデータベース暗号化がシームレスに統合されます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=558183）をご参照ください。

---

### 10. Public Preview: Data API builder with built-in GitHub Copilot in MSSQL extension 

**公開日時**: 2026年03月18日 17:00:05 UTC
**リンク**: [Public Preview: Data API builder with built-in GitHub Copilot in MSSQL extension ](https://azure.microsoft.com/updates?id=558178)

**アップデートID**: 558178
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

- 何が更新されたか  
Visual Studio Code用MSSQL拡張機能に、Data API builderのパブリックプレビュー版が追加されました。GitHub Copilotとの統合も組み込まれています。

- 主な変更点や新機能  
Data API builderを利用することで、RESTおよびGraphQL APIのバックエンドをガイド付きで自動生成できるようになりました。さらに、GitHub CopilotのAI支援により、API構築作業を効率化できます。これにより、開発ワークフロー内で直接APIの設計・生成が可能です。

- 影響を受ける対象  
Visual Studio Code上でMSSQL拡張機能を利用している開発者や、SQLデータベースからAPIを迅速に構築したい技術者が対象です。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用は推奨されません。機能や仕様が今後変更される可能性がありますので、検証環境での利用を推奨します。

**詳細**:

本アップデートは、Visual Studio Code向けのMSSQL拡張機能において、Data API builderのパブリックプレビュー版が提供開始されたことを示しています。このData API builderにはGitHub Copilotが組み込まれており、開発者がバックエンドの生成をよりガイド付きで効率的に行えるようになっています。これにより、開発ワークフローの中で直接RESTやGraphQLエンドポイントの生成が可能となります。

本機能の主な目的は、データベース駆動型アプリケーションのバックエンド構築を自動化・効率化し、開発者の生産性を向上させることです。従来、MSSQLデータベースを利用したアプリケーション開発では、APIの設計や実装に多くの時間と労力が必要でしたが、Data API builderの導入により、これらの作業を大幅に簡略化できます。さらに、GitHub Copilotとの連携により、AIによるコード補完や提案を活用しながら、より迅速かつ正確なAPI構築が実現できます。

技術的には、Visual Studio CodeのMSSQL拡張機能内でData API builderが動作し、ユーザーはインタラクティブなUIやコマンドパレットを通じてAPIエンドポイントを生成できます。GitHub Copilotの組み込みにより、開発者は自然言語による指示やコードスニペットの提案を受けながら、必要なAPIの定義や設定を行うことが可能です。RESTおよびGraphQLエンドポイントの生成がサポートされており、これによりフロントエンドや他のサービスからのデータアクセスが容易になります。

活用シナリオとしては、MSSQLデータベースをバックエンドに持つWebアプリケーションやモバイルアプリケーションの開発、プロトタイピング、PoC（概念実証）などが挙げられます。特に、迅速なAPI構築が求められるアジャイル開発や、複数のAPIエンドポイントを短期間で用意する必要があるプロジェクトにおいて有用です。

注意点としては、本機能がパブリックプレビュー段階であるため、運用環境での利用には慎重な検討が必要です。また、GitHub Copilotの利用には別途ライセンス契約が必要となる場合があります。機能の安定性やサポート範囲についても、正式リリース版と比較して制限がある可能性があります。

関連するAzureサービスとしては、Azure SQL DatabaseやAzure App Serviceなどが挙げられます。これらのサービスと連携することで、クラウド上でのスケーラブルなアプリケーション開発やデプロイが容易になります。MSSQL拡張機能を活用することで、ローカル開発環境とAzureクラウドサービス間のシームレスな連携が期待できます。

---


*このレポートは自動生成されました - 2026-03-19 12:03:50 JST*