# 2026年11月25日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年11月25日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 8 件

## 更新一覧

### 1. Generally Available: Azure Site Recovery support for zonal disaster recovery for Ultra disks

**公開日時**: 2026年11月24日 17:48:22 UTC
**リンク**: [Generally Available: Azure Site Recovery support for zonal disaster recovery for Ultra disks](https://azure.microsoft.com/updates?id=582171)

**アップデートID**: 582171
**情報源**: Azure Updates API

**カテゴリ**: Launched, Management and governance, Migration, Azure Site Recovery, Management, Feature

**要約**:

- 何が更新されたか  
Azure Site Recoveryが、Azure Ultra Diskに対するゾーン間災害復旧（Zonal Disaster Recovery）を正式にサポートするようになりました。

- 主な変更点や新機能  
これまでサポートされていなかったUltra Disk搭載の仮想マシンに対して、可用性ゾーン間でのレプリケーションと復旧が可能になりました。これにより、パフォーマンス要求の高いVMもゾーン障害時に別の可用性ゾーンへ迅速に復旧できます。

- 影響を受ける対象  
Azure Ultra Diskを利用している仮想マシンを運用しているユーザーや、ゾーン障害に備えたDR構成を検討している技術者が対象です。特に、高性能ストレージを必要とするワークロードの可用性向上に役立ちます。

- 注意点があれば記載  
Ultra Diskのゾーン間レプリケーションには追加のコストや構成要件が発生する場合があります。導入前にAzure Site Recoveryの対応リージョンや制約事項を確認することを推奨します。

**詳細**:

Azure Site RecoveryがAzure Ultra Diskに対するゾーン間災害復旧（Zonal Disaster Recovery、Zonal DR）をサポートするようになりました。本アップデートの背景には、パフォーマンス要求の高い仮想マシン（VM）を運用する顧客が、可用性ゾーン間での障害対策を求めていたことがあります。これまでUltra Diskを利用したVMについては、ゾーン障害時の復旧手段が限定されていましたが、今回のアップデートにより、Azure Site Recoveryを用いてUltra Disk搭載VMのゾーン間レプリケーションと復旧が可能となりました。

具体的な機能としては、Azure Site RecoveryがUltra Diskを利用するVMのデータを、同一リージョン内の異なる可用性ゾーンにレプリケートし、ゾーン障害発生時には別ゾーンへ迅速にフェールオーバーできるようになった点が挙げられます。これにより、ミッションクリティカルなワークロードや高いIO性能を要求するシステムに対して、より高い可用性と災害復旧対策を提供できます。

技術的な仕組みとしては、Azure Site RecoveryがVMのディスク（Ultra Diskを含む）を定期的にレプリケートし、障害発生時にはレプリケーション先のゾーンでVMを復旧します。レプリケーションはAzureの内部ネットワークを利用して行われ、復旧時には事前に設定されたターゲットゾーンにVMが再構築されます。Ultra Diskの特性上、高いIOPSや低レイテンシを維持しつつ、ゾーン間でのデータ整合性を確保することが可能です。

活用シナリオとしては、金融機関や大規模なデータ処理を行う企業など、Ultra Diskを利用している高性能VMを複数ゾーンにまたがって保護したい場合に有効です。例えば、トランザクション処理やリアルタイム分析を行うシステムで、ゾーン障害時にも業務継続性を担保する必要がある場合に、Azure Site RecoveryによるZonal DRが活用できます。

注意点としては、Ultra Diskのレプリケーションや復旧にはAzure Site Recoveryの設定が必要であり、事前に対応するVMサイズやディスク構成、ゾーンの選択などを確認する必要があります。また、レプリケーションの頻度や復旧時のパフォーマンスについては、Azure Site Recoveryの仕様に依存しますので、サービスのドキュメントを参照し、要件に合致するか検証することが重要です。

関連するAzureサービスとしては、Azure Site Recovery自体が主要な災害復旧サービスであり、可用性ゾーンやUltra Disk、仮想マシン、ネットワーク構成などと連携して動作します。これにより、Azure上での高可用性設計やBCP（事業継続計画）において、より柔軟な災害復旧構成を実現できます。

---

### 2. Public Preview: Optimize agents from insights in Foundry Agent Service

**公開日時**: 2026年11月24日 16:52:07 UTC
**リンク**: [Public Preview: Optimize agents from insights in Foundry Agent Service](https://azure.microsoft.com/updates?id=581483)

**アップデートID**: 581483
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**要約**:

【何が更新されたか】  
Foundry Agent Serviceにおいて、「Optimization from insights」機能がパブリックプレビューとして公開されました。

【主な変更点や新機能】  
Foundryポータル上で、プロンプトエージェントのトレースから得られるインサイトを起点に、エージェントの命令やFunction Callingツールの説明文の候補変更を自動生成・評価できるようになりました。これにより、エージェントの動作改善や最適化が効率的に行えます。

【影響を受ける対象】  
Foundry Agent Serviceを利用している技術者や開発者が対象です。特に、エージェントのパフォーマンスや応答精度の向上を目指している方に有用な機能です。

【注意点】  
本機能はパブリックプレビュー段階のため、運用環境での利用には十分な検証が必要です。正式リリース前のため、仕様変更や不具合が発生する可能性があります。

詳細は公式アップデートページをご参照ください。

**詳細**:

本アップデートは、Foundry Agent Serviceにおける「Optimization from insights」機能のパブリックプレビュー公開に関するものです。Foundry Agent Serviceは、Azure上でエージェントの挙動やパフォーマンスを管理・最適化するためのサービスです。今回のアップデートの背景には、エージェントの運用において得られるインサイトを活用し、エージェントの指示や機能呼び出しツールの記述を効率的に改善するニーズがあります。これにより、エージェントの応答品質や処理効率の向上が期待されています。

具体的な機能として、Foundryポータル上でプロンプトエージェントのトレースから取得できる適格なインサイトを起点に、エージェントの指示やfunction-calling tool descriptionの候補変更を生成・評価することが可能となります。ユーザーは、トレースデータに基づいたインサイトを選択し、エージェントの設定やツール記述を最適化するための候補を自動生成し、それらを評価することで、より良いエージェント構成を目指すことができます。

技術的な仕組みとしては、Foundryポータル内でプロンプトエージェントのトレース情報からインサイトを抽出し、そのインサイトに基づいてエージェントの指示やfunction-calling tool descriptionの変更候補を生成します。これらの候補は、ポータル上で評価・比較することができ、最適な構成を選択するプロセスが支援されます。実装面では、トレースデータの解析とインサイト抽出、候補生成ロジック、評価インターフェースが連携して動作します。

活用シナリオとしては、エージェントの応答精度やパフォーマンス改善を目指す開発者が、運用中のエージェントのトレースから得られるインサイトを活用し、指示やツール記述の最適化を効率的に実施するケースが想定されます。例えば、エージェントの応答が期待通りでない場合に、トレースから問題点を抽出し、改善候補を自動生成・評価することで、迅速なチューニングが可能となります。

注意点としては、本機能がパブリックプレビュー段階であるため、商用環境での利用や安定性、サポート範囲には制限がある可能性があります。また、利用にはFoundry Agent ServiceおよびFoundryポータルへのアクセスが必要となります。

関連するAzureサービスとしては、Foundry Agent Service自体がAzure上で動作するサービスであり、他のAzure AIサービスやデータ分析サービスと連携することで、より高度なエージェント最適化や運用が実現できます。今回のアップデートは、エージェント運用の効率化と品質向上を支援する重要な機能追加となっています。

---

### 3. Public Preview: Govern MCP tools with your own gateway in Microsoft Foundry Agent Service

**公開日時**: 2026年11月24日 16:50:47 UTC
**リンク**: [Public Preview: Govern MCP tools with your own gateway in Microsoft Foundry Agent Service](https://azure.microsoft.com/updates?id=581498)

**アップデートID**: 581498
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**要約**:

【何が更新されたか】  
Microsoft Foundry Agent Serviceにおいて、MCP（Microsoft Cloud Platform）ツールのトラフィックを組織が管理するAI GatewayやAzure API Managementのエンドポイント経由でルーティングできる機能がパブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
MCPツールの通信経路を既存のAI GatewayやAzure API Managementに設定することで、組織独自のポリシーやセキュリティ制御を適用可能となりました。設定はまずゲートウェイ側でMCPルートを構成し、その後Foundry Agent Serviceでゲートウェイ経由のエンドポイントを指定します。

【影響を受ける対象】  
MCPツールを利用している組織や、Foundry Agent Serviceを導入している技術者が対象です。特にAPI管理やセキュリティ強化を求める企業にとって有用です。

【注意点】  
本機能はパブリックプレビュー段階のため、本番環境での利用には慎重な検証が必要です。設定手順やゲートウェイ構成の詳細は公式ドキュメントを参照してください。

**詳細**:

本アップデートは、「Microsoft Foundry Agent Service」において、MCP（Microsoft Cloud Platform）ツールのトラフィックを、組織が管理する既存のAI GatewayまたはAzure API Managementエンドポイントを経由してルーティングできる機能がパブリックプレビューとして提供されたことを示しています。これにより、従来はMicrosoftが提供する標準の経路を利用していたMCPツールの通信を、企業独自のガバナンスやセキュリティポリシーに基づいて制御できるようになります。

具体的な機能としては、まず組織が管理するAI GatewayまたはAzure API Managementにおいて、MCPツール用のルート設定を行います。その後、Foundry Agent Serviceの設定において、ゲートウェイ経由でルーティングされたエンドポイント情報を入力することで、MCPツールのトラフィックが指定したゲートウェイを通過するようになります。これにより、組織はトラフィックの監視、認証、アクセス制御、ロギング、レートリミットなどの高度な管理を自社のポリシーに合わせて実施することが可能となります。

技術的な仕組みとしては、MCPツールが発生させるAPIリクエストやデータトラフィックを、まず組織のAI GatewayまたはAzure API Managementに転送し、そこから必要な認証やポリシー適用を経て、最終的にMicrosoftのクラウドサービスに到達させる形となります。これにより、既存のゲートウェイやAPI管理基盤を活用しつつ、セキュリティや運用の一元化が図れます。

活用シナリオとしては、たとえば金融や医療など高いセキュリティ要件が求められる業界において、MCPツールの利用時に組織独自のアクセス制御や監査ログを強化したい場合や、APIトラフィックの可視化・分析を自社のツールで行いたい場合に有効です。また、複数のMCPツールやサービスを統合的に管理したい場合にも、既存のAPI管理基盤を活用できる点がメリットとなります。

注意点としては、本機能は現時点でパブリックプレビューであるため、商用環境での利用には慎重な検証が必要です。また、ゲートウェイやAPI Managementの設定ミスやパフォーマンスボトルネックが発生した場合、MCPツールの通信に影響を及ぼす可能性があるため、十分な監視と運用設計が求められます。

関連するAzureサービスとしては、AI GatewayおよびAzure API Managementが挙げられます。これらのサービスとFoundry Agent Serviceを連携させることで、より柔軟かつセキュアなMCPツール運用が実現可能となります。

---

### 4. Generally Available: Use Azure Storage permissions in Azure AI Search and Foundry IQ

**公開日時**: 2026年11月24日 16:49:39 UTC
**リンク**: [Generally Available: Use Azure Storage permissions in Azure AI Search and Foundry IQ](https://azure.microsoft.com/updates?id=581303)

**アップデートID**: 581303
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**要約**:

【何が更新されたか】  
Azure AI SearchおよびMicrosoft Foundry内のFoundry IQが、Azure Storageのアクセス権限を利用して検索結果へのアクセス制御ができるようになりました。

【主な変更点や新機能】  
Azure Storageの権限設定を検索アプリケーションやAIエージェントに適用することで、ユーザーごとのアクセス権に基づいた検索結果の返却が可能になりました。これにより、個別のアクセス管理を構築する手間が削減され、既存のストレージ権限をそのまま検索サービスに活用できます。

【影響を受ける対象】  
Azure AI SearchおよびFoundry IQを利用している技術者や開発者が対象です。特に、検索結果のセキュリティやアクセス制御を強化したい場合に有効です。

【注意点】  
Azure Storageの権限設定が正しく構成されていない場合、検索結果のアクセス制御が意図通りに機能しない可能性があります。導入時はストレージ権限の設定を十分に確認してください。

**詳細**:

今回のアップデートは、「Azure AI Search」と「Foundry IQ」がMicrosoft Foundry内でAzure Storageの権限を利用できるようになったことを示しています。これにより、検索結果へのアクセス制御がAzure Storageの権限設定に基づいて行えるようになりました。アップデートの背景としては、検索アプリケーションやAIエージェントがユーザーごとに適切なコンテンツを返すためのアクセス管理の強化が求められていたことが挙げられます。従来は、検索結果のアクセス制御を独自に実装する必要がありましたが、今回の機能追加によりAzure Storageの既存のアクセス権限をそのまま活用できるようになりました。

具体的な機能としては、Azure Storageに設定されたアクセス権限を検索結果のフィルタリングに利用できる点が特徴です。ユーザーが検索を行う際、検索アプリケーションやAIエージェントは、そのユーザーのAzure Storage権限を参照し、許可されたコンテンツのみを返します。これにより、ユーザーごとに異なる検索結果を返すことが可能となり、セキュリティやデータガバナンスの向上につながります。

技術的な仕組みとしては、Azure AI SearchやFoundry IQがAzure Storageのアクセス権限情報を取得し、検索結果の生成時にその権限情報を適用します。これにはAzure Storageの認証・認可機能が活用されており、検索アプリケーション側で権限管理を再実装する必要がなくなります。実装方法としては、Azure Storage側でユーザーやグループごとにアクセス権限を設定し、検索アプリケーションやAIエージェントがその権限情報を参照する形となります。

活用シナリオとしては、企業内のドキュメント検索やデータ分析において、ユーザーごとにアクセス可能な情報のみを検索結果として返す必要がある場合に有効です。例えば、部門ごとにアクセス権限が異なるファイルストレージを検索対象とする場合、Azure Storageの権限設定により部門ごとに異なる検索結果を返すことができます。

注意点としては、Azure Storageの権限設定が正しく行われていない場合、検索結果のアクセス制御が意図通りに機能しない可能性があるため、権限管理の運用には十分な注意が必要です。また、対応しているAzure Storageの権限モデルや認証方式については、公式ドキュメントを参照して確認する必要があります。

関連するAzureサービスとしては、Azure AI Search、Foundry IQ、Azure Storageが連携して動作します。これにより、ストレージのアクセス権限を検索機能に直接反映できるため、システム全体のセキュリティと運用効率が向上します。

---

### 5. Public Preview: Native A2A passthrough for hosted agents in Foundry Agent Service

**公開日時**: 2026年11月24日 16:48:25 UTC
**リンク**: [Public Preview: Native A2A passthrough for hosted agents in Foundry Agent Service](https://azure.microsoft.com/updates?id=581313)

**アップデートID**: 581313
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**要約**:

【何が更新されたか】  
Agent Serviceにおいて、ネイティブA2A（Agent2Agent）パススルー機能がパブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
これまでAgent Serviceは、受信したA2AリクエストをResponsesプロトコルへ変換して処理していましたが、今回のアップデートにより、プロトコル変換レイヤーを介さずに、ネイティブA2Aリクエストを直接転送できるようになりました。これにより、既存のA2AエージェントをFoundry Agent Serviceにシームレスに統合可能となります。

【影響を受ける対象】  
A2Aプロトコルを利用している既存のエージェントや、Foundry Agent Service上でホストされるエージェントが対象です。A2A通信を利用するシステムやサービスの開発者・運用者にとって、移行や統合の手間が軽減されます。

【注意点】  
本機能はパブリックプレビュー段階のため、商用利用時には安定性やサポート範囲に注意が必要です。導入前に最新のドキュメントやサポート情報を確認してください。

**詳細**:

本アップデートは、Foundry Agent Serviceにおいて、Agent2Agent（A2A）プロトコルのネイティブパススルー機能がパブリックプレビューとして提供されることを示しています。従来、Agent Serviceは受信したA2AリクエストをResponsesプロトコルへ変換する変換レイヤーを介して処理していましたが、今回のアップデートにより、Agent ServiceはA2Aリクエストをネイティブ形式のまま直接転送できるようになります。これにより、既存のA2Aエージェントをプロトコル変換なしでAgent Serviceに持ち込むことが可能となります。

この機能の主な目的は、A2Aプロトコルを利用する既存のエージェントの統合を簡素化し、プロトコル変換によるオーバーヘッドや複雑性を排除することです。具体的な変更内容としては、Agent ServiceがA2Aリクエストを受信した際、従来のようにResponsesプロトコルへ変換せず、A2Aリクエストをそのままネイティブ形式で転送する点が挙げられます。これにより、エージェント間通信のパフォーマンス向上や、既存システムとの互換性維持が期待できます。

技術的な仕組みとしては、Agent Serviceがプロトコル変換レイヤーをバイパスし、A2Aリクエストの内容を変更せずに転送するパススルー方式を採用しています。これにより、A2Aプロトコルに特化したエージェントの動作を損なうことなく、Agent Service経由での通信が可能となります。

活用シナリオとしては、A2Aプロトコルを利用している既存のエージェントをAzure上のFoundry Agent Serviceに移行したい場合や、プロトコル変換による遅延や互換性問題を回避したい場合に有効です。例えば、オンプレミス環境で稼働しているA2Aエージェントをクラウド環境へ移行する際、追加の開発や変換処理を行うことなく、Agent Service上でそのまま利用できるようになります。

注意点としては、パブリックプレビュー段階であるため、商用利用や大規模運用に際しては十分な検証が必要です。また、A2Aプロトコルの仕様やエージェントの実装によっては、パススルー機能の利用に制限が生じる場合があります。詳細な制限事項や推奨構成については、公式ドキュメントやアップデートページを参照してください。

本機能はFoundry Agent Serviceに限定されており、他のAzureサービスとの直接的な連携については明記されていませんが、Agent Serviceを介したA2Aエージェントの統合が容易になることで、Azure上のさまざまなサービスやワークロードとの連携が促進される可能性があります。

---

### 6. Public Preview: Azure Developer CLI extension for Azure Document Intelligence and Content Understanding in Foundry Tools

**公開日時**: 2026年11月24日 16:45:59 UTC
**リンク**: [Public Preview: Azure Developer CLI extension for Azure Document Intelligence and Content Understanding in Foundry Tools](https://azure.microsoft.com/updates?id=581318)

**アップデートID**: 581318
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Developer CLI（azd）向けの拡張機能として、「Azure Document Intelligence」と「Content Understanding」をFoundry Tools内で利用できる機能がパブリックプレビューとして提供開始されました。

- 主な変更点や新機能  
新たに「azd ai cu」コマンドが追加され、Foundry Tools内でドキュメントの分析を実行できるようになりました。分析結果はMarkdownまたはJSON形式で保存可能です。

- 影響を受ける対象  
Microsoft Foundry環境でAzure Developer CLIを利用している開発者や、ドキュメント分析・コンテンツ理解機能を開発ワークフローに組み込みたい技術者が対象です。

- 注意点  
本機能はパブリックプレビュー段階のため、商用利用や本番環境での利用には注意が必要です。今後の仕様変更や不具合の可能性も考慮してください。

**詳細**:

本アップデートは、「Azure Developer CLI（azd）」の拡張機能として、Microsoft Foundry内でAzure Document IntelligenceおよびContent Understandingを利用できるようになることを目的としています。これにより、Foundry Toolsにおいて「azd ai cu」コマンドを使用してドキュメントの分析を実施し、その結果をMarkdownまたはJSON形式で保存することが可能となります。

具体的な機能としては、Azure Developer CLIに新たな拡張機能が追加され、ユーザーはコマンドラインから直接Azure Document IntelligenceとContent Understandingの機能を呼び出すことができます。分析対象となるドキュメントは、Foundry Toolsの環境下で処理され、結果は構造化されたデータとして出力されます。これにより、分析結果をMarkdown形式でレポートとしてまとめたり、JSON形式でシステム間連携や後続処理に活用することができます。

技術的な仕組みとしては、Azure Developer CLIの拡張機能がAzure Document IntelligenceおよびContent UnderstandingのAPIと連携し、ドキュメント解析処理を実行します。ユーザーは「azd ai cu」コマンドを用いて解析を開始し、CLI上で結果を取得できます。Foundry Toolsの統合により、開発者は既存のワークフローに組み込むことができ、効率的なドキュメント分析が実現します。

活用シナリオとしては、例えば大量の業務ドキュメントや契約書、技術資料などを自動的に解析し、内容理解や構造化データの抽出を行う場面で有効です。分析結果をMarkdownで保存することで、レビューや社内共有が容易になり、JSON形式で保存することで他のアプリケーションやサービスとの連携が可能となります。

注意点としては、本機能はパブリックプレビュー段階であり、正式リリース前のため安定性や機能面で制限がある可能性があります。また、Azure Document IntelligenceやContent UnderstandingのAPI利用にあたっては、適切なAzureサブスクリプションや権限設定が必要です。出力形式もMarkdownとJSONに限定されているため、他のフォーマットでの利用を希望する場合は追加の変換処理が必要です。

関連するAzureサービスとしては、Azure Document Intelligenceがドキュメント解析の基盤となり、Content Understandingが内容把握や構造化データ抽出を担います。これらのサービスはAzure Developer CLIを通じてFoundry Toolsと連携し、開発者が効率的にドキュメント分析を行うための環境を提供します。

---

### 7. Public Preview: Cost controls for model and agent spending in Microsoft Foundry

**公開日時**: 2026年11月24日 16:43:40 UTC
**リンク**: [Public Preview: Cost controls for model and agent spending in Microsoft Foundry](https://azure.microsoft.com/updates?id=581323)

**アップデートID**: 581323
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**要約**:

【何が更新されたか】  
Microsoft Foundryにおいて、モデルやエージェントの利用に対するコスト管理機能がパブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
Foundryリソースやプロジェクトごとに、利用額やトークン消費量の予算を設定できるようになりました。設定した閾値に達すると、Azure Event Gridを通じてアラートを送信したり、新規リクエストをブロックすることが可能です。これにより、予算超過の防止やコスト管理が容易になります。

【影響を受ける対象】  
Microsoft Foundryを利用している技術者や管理者が対象です。特に、モデルやエージェントの利用コストを管理したいプロジェクトやチームに有効です。

【注意点】  
本機能はパブリックプレビュー段階のため、正式リリース前の仕様変更や制限がある可能性があります。運用環境での利用時は、最新のドキュメントやサポート情報を確認してください。

**詳細**:

Microsoft Foundryにおける「Cost controls for model and agent spending」のパブリックプレビューは、Foundryリソースやプロジェクト単位で支出やトークン消費量の予算を設定できる機能です。このアップデートの背景には、AIモデルやエージェントの利用が拡大する中で、コスト管理の重要性が高まっていることがあります。特に、予期しない消費や予算超過による運用リスクを低減することが目的です。

具体的な機能としては、管理者がFoundryリソースやプロジェクトごとに支出やトークンの上限を設定でき、その使用量が設定した閾値に達した際に、Azure Event Gridを通じてアラートを送信するか、あるいは新規リクエストをブロックする動作が可能です。これにより、リアルタイムでコスト状況を把握し、必要に応じて即座に対応することができます。

技術的な仕組みとしては、コストコントロール機能がFoundryのリソース管理層に組み込まれており、利用状況をモニタリングし、設定された閾値に達した際にAzure Event Gridと連携して通知を行います。Event GridはAzureのイベント駆動型アーキテクチャの一部であり、アラートを受信した後、他のAzureサービスや外部システムと連携して自動化された対応を実装することも可能です。また、閾値超過時にはリクエストのブロック機能も提供されているため、予算超過を確実に防止できます。

活用シナリオとしては、AIモデルやエージェントの運用コストを厳格に管理したい場合や、複数プロジェクトを同時に運用する際に各プロジェクトごとの予算管理を徹底したい場合に有効です。例えば、開発環境と本番環境で異なる予算を設定し、開発環境での無駄な消費を防ぐことができます。また、アラート通知を活用して、運用担当者が迅速に対応する仕組みを構築することも可能です。

注意点として、予算設定や閾値の管理はFoundryリソースやプロジェクト単位で行う必要があります。また、アラート通知やリクエストブロックの動作はAzure Event Gridとの連携に依存しているため、Event Gridの設定や運用にも注意が必要です。さらに、パブリックプレビュー段階であるため、本番環境での利用には慎重な検証が求められます。

関連するAzureサービスとしては、Azure Event Gridが中心となりますが、他のAzure監視・管理サービスと組み合わせて、より高度なコスト管理や自動化対応を実現することも可能です。今回のアップデートにより、Microsoft Foundry上でのAIモデルやエージェントの運用コストを効率的かつ安全に管理できるようになります。

---

### 8. Public Preview: Central governance of hosted-agent outbound domains in Foundry Agent Service

**公開日時**: 2026年11月24日 16:42:20 UTC
**リンク**: [Public Preview: Central governance of hosted-agent outbound domains in Foundry Agent Service](https://azure.microsoft.com/updates?id=581328)

**アップデートID**: 581328
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**要約**:

【何が更新されたか】  
Foundry Agent Serviceにおいて、ホスト型エージェントのアウトバウンド通信先ドメインを中央管理できる機能がパブリックプレビューとして提供されました。

【主な変更点や新機能】  
Azure Policyを利用して、ホスト型エージェントのアウトバウンド通信先（egress先）を制御できるようになりました。エージェント作成者は、エージェントバージョン作成前に、準拠したegressポリシーを設定・適用する必要があります。このポリシーによって、エージェントのアウトバウンドリクエストが管理されます。

【影響を受ける対象】  
Foundry Agent Serviceを利用している管理者およびエージェント作成者が対象です。特に、セキュリティや通信制御を重視する環境でのエージェント運用に関わる技術者に影響があります。

【注意点】  
パブリックプレビュー段階のため、本番環境での利用には注意が必要です。エージェント作成時には、必ずAzure Policyによるegressポリシーの設定が求められるため、既存の運用フローに組み込む必要があります。

**詳細**:

本アップデートは、Foundry Agent Serviceにおけるホスト型エージェントのアウトバウンド通信先を中央で管理・統制する機能のパブリックプレビュー開始を示しています。背景としては、クラウド環境におけるセキュリティとコンプライアンスの強化が求められる中、エージェントが外部と通信する際の宛先管理を一元化することで、不要な通信やリスクを低減することが目的です。

具体的な機能として、管理者はAzure Policyを利用してFoundry Agent Serviceのホスト型エージェントが通信可能なアウトバウンド先を制御できます。エージェントの作成者は、エージェントバージョンを作成する前に、Azure Policyで定義された準拠したイグレス（egress）ポリシーを構成し、エージェントに付与する必要があります。このイグレスポリシーが、エージェントのアウトバウンドリクエストを制御し、許可されたドメインのみへの通信を許可します。

技術的な仕組みとしては、Azure Policyを用いたポリシーベースのガバナンスが中心となります。エージェント作成時にポリシーの適用が必須となるため、ポリシー違反のエージェントは作成できません。これにより、組織全体で一貫した通信先管理が可能となり、セキュリティや監査要件への対応が容易になります。

活用シナリオとしては、例えば複数の開発チームがFoundry Agent Serviceを利用している場合、管理者がAzure Policyで許可ドメインを定義することで、各チームが不用意に外部サービスへ通信するリスクを排除できます。また、金融や医療など高いコンプライアンスが求められる業界において、アウトバウンド通信先の制限を厳格に管理することができます。

注意点としては、イグレスポリシーの適用が必須となるため、ポリシー設定を誤ると必要な通信先へのアクセスが遮断される可能性があります。エージェント作成者は、事前に管理者と連携し、必要な通信先がポリシーに含まれていることを確認する必要があります。また、パブリックプレビュー段階であるため、機能や仕様が今後変更される可能性があります。

関連するAzureサービスとしては、Azure Policyが中心となりますが、Foundry Agent Serviceのホスト型エージェントの運用において、Azure MonitorやAzure Security Centerなどの監視・セキュリティサービスと併用することで、より高度なガバナンスと運用管理が実現できます。

---


*このレポートは自動生成されました - 2026-11-25 12:02:53 JST*