# 2026年06月18日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年06月18日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Public Preview: Azure Migrate – GitHub Copilot Modernization integration for at scale code assessments

**公開日時**: 2026年06月17日 18:00:18 UTC
**リンク**: [Public Preview: Azure Migrate – GitHub Copilot Modernization integration for at scale code assessments](https://azure.microsoft.com/updates?id=566145)

**アップデートID**: 566145
**情報源**: Azure Updates API

**カテゴリ**: In preview, Management and governance, Migration, Azure Migrate, Feature

**要約**:

【何が更新されたか】  
Azure MigrateがGitHub Copilot Modernizationとの連携機能をパブリックプレビューとして提供開始しました。

【主な変更点や新機能】  
Azure Migrateのポートフォリオレベルのアプリケーション発見・評価機能と、GitHub Copilotによるコンテキスト認識型コード分析が統合されました。これにより、大規模なコードベースのモダナイゼーションに向けたコードインサイトを効率的に取得できるようになります。

【影響を受ける対象】  
Azure Migrateを利用してアプリケーションのクラウド移行やモダナイゼーションを検討している技術者や開発チームが対象です。特にGitHub Copilot Modernizationを活用したコード評価を行いたい場合に有効です。

【注意点】  
本機能はパブリックプレビュー段階のため、商用環境での利用には慎重な検討が必要です。正式リリース前のため、機能やサポート内容が変更される可能性があります。利用時は最新のドキュメントやアップデート情報を確認してください。

**詳細**:

本アップデートは、Azure MigrateとGitHub Copilot Modernizationの統合によるコードアセスメント機能のパブリックプレビュー公開に関するものです。背景として、クラウド移行やアプリケーションのモダナイゼーションにおいて、既存コードの品質や移行適合性の評価が重要視されています。Azure Migrateは従来より、インフラやアプリケーションのポートフォリオ全体を対象とした発見・評価機能を提供してきましたが、今回のアップデートにより、GitHub Copilot Modernizationの文脈認識型コード分析機能と連携することで、より広範かつ詳細なコードインサイトを得られるようになりました。

具体的には、Azure Migrateのポートフォリオレベルのディスカバリーおよびアセスメント機能と、GitHub Copilot Modernizationが提供するコード分析機能が組み合わさることで、大規模なコードベースに対して効率的な評価が可能となります。GitHub Copilot Modernizationは、AIを活用したコード解析により、コードの改善点や移行時のリスク、モダナイゼーションの推奨事項などを提示します。Azure Migrate側では、既存のインベントリ収集や依存関係分析といった機能と合わせて、コードレベルの洞察を一元的に取得できる仕組みとなっています。

技術的な実装方法としては、Azure Migrateの評価プロセスの中でGitHub Copilot ModernizationのAPIやサービスと連携し、対象コードの解析結果を取得・統合します。これにより、従来のインフラやアプリケーション単位の評価に加え、コード品質や移行適合性に関する詳細なレポートを生成することが可能です。

活用シナリオとしては、オンプレミスからAzureへの移行を検討している企業や、既存アプリケーションのクラウドネイティブ化を進めたい技術者が、移行前にコードの現状を把握し、リファクタリングやモダナイゼーションの必要性を評価する際に有効です。また、複数プロジェクトや大規模なコードベースを一括で評価する場合にも、効率的な作業が期待できます。

注意点としては、本機能がパブリックプレビュー段階であるため、正式リリース前の制限や一部機能の未実装が考えられます。また、GitHub Copilot Modernizationとの連携には、対応するアカウントや権限設定が必要となる場合があります。

関連するAzureサービスとしては、Azure Migrateの既存機能に加え、Azure DevOpsやGitHubとの連携が想定されます。これにより、移行プロジェクト全体の計画から実行、コード評価までを一元的に管理できる環境が構築可能です。

以上が、Azure MigrateとGitHub Copilot Modernization統合によるコードアセスメント機能のパブリックプレビューに関する技術者向け詳細説明です。

---

### 2. Generally Available: Azure Databricks native read access to Microsoft OneLake 

**公開日時**: 2026年06月17日 18:00:18 UTC
**リンク**: [Generally Available: Azure Databricks native read access to Microsoft OneLake ](https://azure.microsoft.com/updates?id=565733)

**アップデートID**: 565733
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Analytics, Azure Databricks, Features

**要約**:

【何が更新されたか】  
Azure Databricksが、Unity Catalogを通じてMicrosoft OneLake内のデータへのネイティブな読み取りアクセスをサポートするようになりました。この機能は一般提供（GA）となっています。

【主な変更点や新機能】  
ユーザーはOneLakeに保存されたデータを、データの移動やコピーを行うことなく、Azure Databricks上で直接クエリや分析が可能になりました。これにより、データアクセスの効率化とパフォーマンス向上が期待できます。

【影響を受ける対象】  
Azure DatabricksとUnity Catalogを利用している技術者や組織が対象です。特に、Microsoft OneLakeをデータレイクとして活用している環境で恩恵を受けます。

【注意点】  
本機能を利用するには、Unity Catalogの設定やOneLakeとの連携が必要です。既存のデータ管理やアクセス権限の構成に影響が出る場合があるため、事前にドキュメントを確認し、適切な設定を行うことを推奨します。

**詳細**:

Azure Databricksは、Unity Catalogを介してMicrosoft OneLake内のデータに対するネイティブな読み取りアクセスをサポートするようになりました。この機能は一般提供（GA）となっており、Azure DatabricksユーザーはOneLakeに保存されたデータを移動やコピーすることなく、直接クエリや分析を実行できるようになっています。これにより、データのアクセス速度が向上し、データ管理の効率化が図られます。

今回のアップデートの背景としては、データレイクの分散管理やデータ移動の負担を軽減し、データ分析基盤の統合を推進する目的があります。従来は、DatabricksでOneLakeのデータを利用する場合、データの移動や複製が必要でしたが、ネイティブアクセスの実現により、ストレージ間のデータ移動を伴わずに分析処理が可能となりました。

具体的な機能としては、Unity Catalogを利用したOneLakeデータへの直接アクセスが挙げられます。Unity CatalogはDatabricksのデータガバナンス機能であり、データの管理やアクセス制御を統一的に行うことができます。今回のアップデートにより、Unity Catalog経由でOneLakeのデータセットを参照し、DatabricksのノートブックやSQLエンドポイントから直接クエリを実行することが可能です。これにより、データの一貫性やセキュリティを維持しつつ、分析ワークロードのパフォーマンス向上が期待できます。

技術的な仕組みとしては、DatabricksとOneLakeの統合がUnity Catalogを通じて実現されています。ユーザーはUnity Catalog内でOneLakeのデータセットを登録し、認証やアクセス権限の管理を行うことで、Databricksから安全かつ効率的にデータを参照できます。これにより、Azure上のデータガバナンスやセキュリティポリシーと連携しながら、複数のストレージサービスを横断的に利用することが可能となっています。

活用シナリオとしては、OneLakeに集約された大規模なデータをDatabricksで分析するケースや、データサイエンス、機械学習、BIレポーティングなどの用途が想定されます。例えば、OneLakeに保存されたログデータやトランザクションデータをDatabricksのSparkエンジンで高速に処理し、分析結果を可視化することができます。また、データの移動を伴わないため、データの最新性や整合性を保ったままリアルタイム分析が可能です。

注意点としては、Unity Catalogを利用したアクセスには適切な権限設定や認証が必要であり、データガバナンスのポリシーに従う必要があります。また、OneLakeのデータ構造やフォーマットによっては、Databricks側でのクエリや処理に制限が生じる場合があります。詳細な制限事項や対応フォーマットについては、公式ドキュメントを参照することが推奨されます。

関連するAzureサービスとしては、Azure Databricks、Microsoft OneLake、Unity Catalogが主要な構成要素となります。これらのサービス間の連携によって、Azure上のデータ分析基盤の統合と効率化が実現されています。

---

### 3. Public Preview: Azure Databricks natively storing data in Microsoft OneLake 

**公開日時**: 2026年06月17日 18:00:18 UTC
**リンク**: [Public Preview: Azure Databricks natively storing data in Microsoft OneLake ](https://azure.microsoft.com/updates?id=565706)

**アップデートID**: 565706
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Analytics, Azure Databricks, Features

**要約**:

【何が更新されたか】  
Azure Databricksが、Microsoft OneLakeに対してネイティブに管理されたDeltaテーブルを書き込める機能がパブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
これまでAzure Databricksでは、データの保存先として個別のストレージアカウント（例：Azure Data Lake Storageなど）の管理が必要でしたが、今回のアップデートによりOneLakeを統一的なストレージレイヤーとして利用できるようになりました。Databricksから直接OneLakeにDeltaテーブルを保存できるため、データ管理の効率化と運用負荷の軽減が期待できます。

【影響を受ける対象】  
Azure Databricksを利用している技術者やデータエンジニア、データサイエンティストが主な対象です。特に、Delta Lake形式でデータ管理を行っているユーザーや、ストレージ管理の簡素化を求めている組織にとって有益なアップデートです。

【注意点】  
本機能はパブリックプレビュー段階のため、本番環境での利用には慎重な検討が必要です。機能の安定性やサポート範囲については、公式ドキュメントやAzureサポートを参照してください。

**詳細**:

本アップデートは、Azure DatabricksがMicrosoft OneLakeに対してネイティブにマネージドDeltaテーブルを書き込めるようになったことを示しています。これにより、Azure Databricksのワークロードにおいて、個別のストレージアカウントを管理することなく、OneLakeを統一的なストレージレイヤーとして利用できるようになります。従来、Databricksでデータを管理する場合、Azure Data Lake Storage Gen2やBlob Storageなど、個別のストレージサービスとの連携や管理が必要でしたが、本機能によりOneLakeへの直接的なデータ書き込みがサポートされ、ストレージ管理の複雑さが大幅に軽減されます。

具体的には、DatabricksのマネージドDeltaテーブルがOneLake上にネイティブに保存されるため、データの一元管理やガバナンスが容易になります。これにより、データエンジニアやデータサイエンティストは、データの保存先を意識することなく、Databricksの分析・機械学習ワークロードをOneLake上でシームレスに実行できます。技術的には、Databricksの内部ストレージレイヤーがOneLakeと統合されており、ユーザーは特別な設定や追加のストレージアカウント管理を行う必要がありません。

活用シナリオとしては、企業内のさまざまなデータソースをOneLakeに集約し、Databricksを用いたETL処理やデータ分析、機械学習パイプラインを構築するケースが考えられます。これにより、データのサイロ化を防ぎつつ、データガバナンスやセキュリティポリシーの一元化が可能となります。

注意点としては、本機能はパブリックプレビュー段階であるため、本番環境での利用には慎重な検証が必要です。また、既存のDatabricksワークスペースやストレージ構成との互換性や移行手順については、公式ドキュメントでの確認が推奨されます。

関連するAzureサービスとしては、OneLakeを中心としたデータファブリックの構築や、Microsoft Fabricとの連携が挙げられます。これにより、Azure上でのデータ統合・分析基盤の拡張性と運用効率が向上します。

---

### 4. Generally Available: ICMP Support for Azure Standard V2 NAT Gateway

**公開日時**: 2026年06月17日 16:30:04 UTC
**リンク**: [Generally Available: ICMP Support for Azure Standard V2 NAT Gateway](https://azure.microsoft.com/updates?id=565487)

**アップデートID**: 565487
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Azure NAT Gateway, Features, Services

**要約**:

【何が更新されたか】  
Azure StandardV2 NAT Gatewayにおいて、ICMP Echo RequestおよびEcho Reply（いわゆるping通信）のアウトバウンドトラフィックが正式にサポートされるようになりました。

【主な変更点や新機能】  
これまでStandardV2 NAT Gatewayを経由したワークロードからのpingによる外部接続確認やネットワーク障害の切り分けが困難でしたが、今回のアップデートにより、pingなどのICMPツールを利用したアウトバウンド接続性の検証やトラブルシューティングが可能となりました。

【影響を受ける対象】  
StandardV2 NAT Gatewayを利用している仮想ネットワーク内のVMやサービスが対象です。これらのワークロードから外部宛てにpingを実行することで、ネットワークの疎通確認や障害調査が容易になります。

【注意点】  
ICMPサポートはアウトバウンド通信に限定されており、インバウンド通信については従来通り制限があります。また、セキュリティポリシーやネットワーク構成によっては追加の設定が必要になる場合がありますので、運用環境に合わせてご確認ください。

**詳細**:

Azure StandardV2 NAT Gatewayにおいて、ICMP Echo RequestおよびEcho Replyトラフィックのアウトバウンド通信がサポートされるようになりました。本アップデートの背景には、従来のNAT GatewayではICMPプロトコルを用いた通信、特にpingコマンドによる疎通確認やネットワーク障害のトラブルシューティングが困難であったという課題があります。ICMPはネットワーク診断や監視に不可欠なプロトコルであり、多くの技術者がpingによる接続確認を日常的に利用しています。今回のアップデートにより、StandardV2 NAT Gateway配下のワークロードから外部宛てにICMP Echo Requestを送信し、その応答（Echo Reply）を受信することが可能となりました。

具体的な機能としては、StandardV2 NAT Gatewayを経由するアウトバウンド通信において、TCPやUDPに加えてICMPプロトコルが正式にサポートされます。これにより、仮想マシンやコンテナなどのワークロードが、NAT Gatewayを通じてインターネット上の任意の宛先に対してpingを実行し、応答を受け取ることができます。技術的な仕組みとしては、NAT GatewayがICMPパケットの変換および転送を行い、内部IPアドレスから外部IPアドレスへのマッピングを維持しつつ、ICMPトラフィックの双方向通信を実現しています。

活用シナリオとしては、ネットワークの疎通確認や障害切り分け、監視ツールによる外部接続性の定期チェックなどが挙げられます。例えば、Azure上の仮想マシンからインターネット上のサービスや他のクラウド環境へのpingを実施し、応答結果をもとにネットワーク状態を評価することが可能です。また、複数のサブネットやワークロードがStandardV2 NAT Gatewayを共有している場合でも、ICMPによる接続確認が容易になります。

注意点としては、ICMPサポートはアウトバウンド通信に限定されており、インバウンドのICMPトラフィックについては本アップデートの対象外です。また、ICMP通信が許可されている外部宛先に対してのみ疎通確認が可能であり、宛先側でICMPをブロックしている場合は応答が得られません。さらに、NAT Gatewayの設定やネットワークセキュリティグループ（NSG）のルールにより、ICMPトラフィックが制限される場合がありますので、適切な設定が必要です。

関連するAzureサービスとしては、仮想ネットワーク（VNet）、仮想マシン（VM）、ネットワークセキュリティグループ（NSG）、およびStandardV2 NAT Gateway自体が挙げられます。これらのサービスと連携することで、より柔軟かつ安全なネットワーク構成を実現できます。今回のアップデートにより、Azure環境におけるネットワーク運用やトラブルシューティングの効率が向上し、技術者の利便性が大きく改善されます。

---


*このレポートは自動生成されました - 2026-06-18 12:02:01 JST*