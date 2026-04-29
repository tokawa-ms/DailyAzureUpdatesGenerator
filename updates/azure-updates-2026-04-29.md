# 2026年04月29日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年04月29日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Public Preview: Memory in Foundry Agent Service 

**公開日時**: 2026年04月29日 00:00:55 UTC
**リンク**: [Public Preview: Memory in Foundry Agent Service ](https://azure.microsoft.com/updates?id=560992)

**アップデートID**: 560992
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry, Features

**要約**:

- 何が更新されたか  
Foundry Agent Serviceにおいて、「Memory」機能（パブリックプレビュー）が追加されました。

- 主な変更点や新機能  
この「Memory」機能は、Foundry Agent Serviceに組み込まれたマネージドな長期記憶機能です。Microsoft Agent FrameworkおよびLangGraphとネイティブに統合されており、外部データベースのプロビジョニング、スケーリング、セキュリティ管理が不要になりました。

- 影響を受ける対象  
Foundry Agent Serviceを利用している開発者や、Microsoft Agent Framework、LangGraphを活用している技術者が対象です。エージェントアプリケーションで長期記憶を必要とするユースケースに特に有用です。

- 注意点があれば記載  
本機能は現在パブリックプレビュー段階です。運用環境での利用には十分な検証が必要です。また、プレビュー機能のため将来的に仕様変更やサポート内容が変わる可能性があります。

**詳細**:

本アップデートは、「Foundry Agent Service」における長期メモリ機能「memory（プレビュー）」がパブリックプレビューとして提供開始されたことを示しています。この機能は、Foundry Agent Serviceに直接組み込まれたマネージドな長期メモリ機能であり、外部データベースのプロビジョニング、スケーリング、セキュリティ管理を必要としない点が大きな特徴です。これにより、エージェントベースのアプリケーション開発において、状態や履歴、知識情報などの長期的なデータを効率的かつ安全に管理することが可能となります。

今回のアップデートにより、Foundry Agent Serviceのmemory機能は、Microsoft Agent FrameworkおよびLangGraphとネイティブに統合されました。これにより、これらのフレームワークを利用したエージェント開発において、追加の外部ストレージやデータベースを用意することなく、エージェントの長期的な記憶や履歴管理を実装できます。たとえば、ユーザーとの対話履歴やエージェントが取得した知識情報を持続的に保持し、次回以降の対話や処理に活用するシナリオが考えられます。

技術的には、Foundry Agent Service内部において長期メモリの管理機能が提供されており、エージェント開発者はAPIやSDKを通じてこの機能を利用できます。外部データベースの構築や運用が不要となるため、システムの複雑性や運用負荷が大幅に軽減されます。また、セキュリティ面でも、Azureのマネージドサービスとして一元的な管理が可能です。

活用例としては、カスタマーサポートボットが過去の問い合わせ履歴を参照してユーザー対応を最適化するケースや、業務プロセス自動化エージェントが過去の処理結果を蓄積して意思決定を支援するケースなどが挙げられます。

注意点としては、本機能は現時点でプレビュー段階であるため、本番環境での利用には慎重な検証が必要です。また、プレビュー期間中は機能やAPI仕様が変更される可能性があります。加えて、外部データベースとの連携が不要となる一方で、Foundry Agent Serviceの提供する範囲内でのみ長期メモリ機能が利用できる点に留意する必要があります。

本機能は、Microsoft Agent FrameworkおよびLangGraphとの統合が強化されており、これらのAzureサービスを利用したエージェント開発において、よりシームレスかつ効率的な長期メモリ管理が実現できます。今後の正式リリースに向けて、さらなる機能拡張や安定性向上が期待されます。

---

### 2. Public Preview: Container Network Insights Agent

**公開日時**: 2026年04月28日 21:30:30 UTC
**リンク**: [Public Preview: Container Network Insights Agent](https://azure.microsoft.com/updates?id=561020)

**アップデートID**: 561020
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

【何が更新されたか】  
Azure Kubernetes Service（AKS）向けに「Container Network Insights Agent」がパブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
このエージェントは、Kubernetesのネットワーク障害のトラブルシューティングを効率化するための軽量なWebベースのインターフェースを提供します。従来は複数のツールに分散していたログやメトリクスを一元的に可視化できるため、インシデント発生時の信号の相関付けが容易になります。

【影響を受ける対象】  
AKS環境でKubernetesネットワークの監視や障害対応を行う技術者が主な対象です。ネットワークの問題解析や運用効率向上を目指すチームに有用です。

【注意点】  
本機能はパブリックプレビュー段階のため、商用利用時には安定性やサポート範囲に注意が必要です。正式リリース前のため、仕様変更や機能追加が行われる可能性があります。

**詳細**:

本アップデートは、「Container Network Insights Agent」のパブリックプレビュー公開に関するものです。Kubernetes環境におけるネットワークのトラブルシューティングは、従来、複数のツールに分散したログやメトリクスをエンジニアが手動で収集・相関させる必要があり、インシデント対応の迅速化が課題となっていました。本アップデートの目的は、これらの課題を解決し、Kubernetesネットワークの問題解析を効率化することにあります。

Container Network Insights Agentは、軽量なWebベースのインターフェースを提供するエージェントです。このエージェントを利用することで、Kubernetesクラスター内のネットワークに関する情報を一元的に可視化し、分散していたログやメトリクスを統合して表示できます。これにより、ネットワーク関連のインシデント発生時に必要な情報を迅速に取得でき、問題の根本原因分析や復旧作業の効率が大幅に向上します。

技術的には、エージェントはKubernetesクラスター内にデプロイされ、各種ネットワークイベントや通信フロー、関連するメトリクスを収集します。収集したデータはWebベースのダッシュボードで可視化され、エンジニアはブラウザから直接ネットワークの状態や異常を確認できます。これにより、従来必要だった複数ツールの切り替えや手動でのデータ突合せ作業が不要となります。

主な活用シナリオとしては、Kubernetesクラスターで発生するネットワーク遅延やパケットロス、通信断などのトラブルシュート時に、迅速に問題箇所を特定する用途が挙げられます。また、ネットワークパフォーマンスの監視や、通信経路の可視化によるセキュリティインシデントの早期発見にも有効です。

注意点としては、本機能がパブリックプレビュー段階であるため、本番環境での利用には慎重な検証が推奨されます。また、サポート範囲や機能の安定性については今後変更される可能性があります。

本エージェントは、Azure Kubernetes Service（AKS）などのAzure上のKubernetesサービスとの連携が想定されており、Azure Monitorなど他の監視系サービスと組み合わせることで、より包括的な運用監視基盤の構築が可能です。

詳細については、公式アップデートページ（https://azure.microsoft.com/updates?id=561020）を参照してください。

---

### 3. Generally Available: Connect to Elastic SAN from Windows VM via VM Extension 

**公開日時**: 2026年04月28日 20:30:56 UTC
**リンク**: [Generally Available: Connect to Elastic SAN from Windows VM via VM Extension ](https://azure.microsoft.com/updates?id=560914)

**アップデートID**: 560914
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Elastic SAN, Features

**要約**:

- 何が更新されたか  
Azure Elastic SANが、Windows仮想マシン（VM）へのボリューム接続をサポートする「Elastic SAN VM Extension」を一般提供（GA）しました。

- 主な変更点や新機能  
AzureポータルからElastic SAN VM Extensionを利用することで、Windows VMのデプロイ時にElastic SANボリュームを直接接続できるようになりました。これにより、仮想マシンのセットアップとストレージ接続の自動化・効率化が可能です。

- 影響を受ける対象  
Elastic SANを利用している、または今後利用予定のAzure上のWindows仮想マシン環境が対象です。特に、ストレージの拡張性や管理性を重視するエンタープライズ環境に有用です。

- 注意点があれば記載  
本機能はWindows VM専用であり、Linux VMなど他のOSには現時点で対応していません。また、Elastic SAN VM Extensionの利用には、対応するAzureリージョンやVMサイズ、ネットワーク要件などの事前確認が必要です。

**詳細**:

Azure Elastic SANは、クラウド上でスケーラブルかつ高性能なストレージを提供するサービスです。今回のアップデートでは、Windows Virtual Machine（VM）からElastic SANボリュームへの接続を、Azure Portal上でVM拡張機能（Elastic SAN VM Extension）を利用して実現できるようになりました。この機能の追加により、従来は手動で行っていたボリューム接続の作業が、VMのデプロイ時に自動化され、運用効率が大幅に向上します。

具体的には、Azure PortalからWindows VMをデプロイする際に、Elastic SAN VM Extensionを選択することで、VM内からElastic SANボリュームへ直接接続できるようになります。これにより、ストレージの初期設定や接続作業が簡略化され、複雑なスクリプトや手動操作が不要となります。Elastic SAN VM Extensionは、VMの拡張機能としてインストールされ、必要なドライバーや設定を自動的に適用する仕組みです。

技術的な実装方法としては、Azure Portal上でVM作成時に拡張機能を追加するだけで、Elastic SANボリュームへの接続が構成されます。これにより、VMの起動後すぐにElastic SANストレージを利用できる状態となります。従来のiSCSIや手動でのストレージマッピングと比較して、作業の簡素化と一貫性の確保が可能です。

この機能は、例えばデータベースサーバーやファイルサーバーなど、高速かつ大容量のストレージを必要とするWindows VMの構築時に有効です。複数のVMからElastic SANボリュームを共有するシナリオや、ストレージの拡張・運用管理を効率化したい場合にも活用できます。

注意点としては、Elastic SAN VM Extensionは現時点でWindows VMのみ対応していることが挙げられます。また、拡張機能の利用にはAzure Portalからの操作が必要であり、他のデプロイ方法やOSではサポート状況が異なる場合があります。Elastic SAN自体の制限事項や、VM拡張機能のバージョン管理にも留意する必要があります。

関連するAzureサービスとしては、Azure Virtual Machines、Azure Elastic SAN、VM Extensionsが挙げられます。これらのサービスを組み合わせることで、クラウド上で柔軟かつ効率的なストレージ運用が可能となります。今回のアップデートは、Windows VMとElastic SANの連携を強化し、ストレージ接続の自動化と運用負荷の軽減を実現する重要な機能追加です。

---

### 4. Public Preview: Microsoft HTTP DDoS Ruleset for Azure WAF on Azure Front Door Premium

**公開日時**: 2026年04月28日 17:45:04 UTC
**リンク**: [Public Preview: Microsoft HTTP DDoS Ruleset for Azure WAF on Azure Front Door Premium](https://azure.microsoft.com/updates?id=561148)

**アップデートID**: 561148
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Azure DDoS Protection, Azure Front Door, Web Application Firewall, Features, Services

**要約**:

- 何が更新されたか  
Azure Front Door Premium向けのAzure WAFにおいて、「Microsoft HTTP DDoS Ruleset（プレビュー版）」が公開されました。

- 主な変更点や新機能  
この新しいHTTP DDoS Rulesetは、アプリケーション層（L7）で発生するHTTPベースのDDoS攻撃に対する検出と防御機能を強化します。従来の静的な制御では対応が難しかった進化するボットネットによる攻撃にも対応可能です。Azure WAFのルールセットとして組み込まれ、リアルタイムでの攻撃緩和を実現します。

- 影響を受ける対象  
Azure Front Door Premiumを利用している環境でAzure WAFを有効化しているユーザーが対象となります。特に、Webアプリケーションの可用性やセキュリティを重視するシステムにとって重要なアップデートです。

- 注意点  
本機能はパブリックプレビュー段階のため、本番環境での利用には十分な検証が推奨されます。また、既存のWAFポリシーやルールとの互換性や動作についても事前に確認する必要があります。

**詳細**:

Azure Front Door Premiumにおいて、HTTP DDoS Rulesetのパブリックプレビューが発表されました。今回のアップデートは、アプリケーションのダウンタイムの主因となっているHTTPレイヤーのDDoS攻撃への対策強化を目的としています。従来の静的な防御策では、進化するボットネットや複雑化する攻撃手法に十分対応できないケースが多く、これを補うために新たなHTTP DDoS Rulesetが導入されました。

具体的には、Azure Front Door PremiumのWeb Application Firewall（WAF）に新しいルールセットが追加され、HTTP層で発生するDDoS攻撃の検知と防御が可能となります。これにより、WAFはアプリケーションレベルのトラフィックをリアルタイムで監視し、不正な大量リクエストや攻撃パターンを識別して遮断することができます。従来のIPベースやネットワーク層でのDDoS対策と異なり、HTTPリクエストの内容や頻度、パターンを精査することで、より高度な攻撃にも対応できる点が特徴です。

技術的な仕組みとしては、Azure Front Door PremiumのWAFがHTTP DDoS Rulesetを適用し、受信したリクエストをルールに基づいて評価します。攻撃と判定されたトラフィックは遮断され、正規のユーザーへの影響を最小限に抑えつつアプリケーションの可用性を維持します。これらのルールはAzureポータル上で設定・管理でき、既存のWAFポリシーと組み合わせて運用することが可能です。

活用シナリオとしては、公開WebアプリケーションやAPIエンドポイントをAzure Front Door Premiumで保護している場合に、HTTP DDoS Rulesetを導入することで、アプリケーション層の攻撃からサービスを守ることができます。特に、頻繁にDDoS攻撃の標的となる金融サービスやECサイト、公共サービスなどで有効です。

注意点としては、現在パブリックプレビュー段階であるため、本番環境での利用には慎重な検証が必要です。また、ルールセットの適用範囲や検知精度、誤検知の可能性など運用上の制約がある場合があります。詳細な制限事項や設定方法については公式ドキュメントを参照する必要があります。

関連するAzureサービスとしては、Azure Front Door PremiumのWAF機能と密接に連携しており、既存のネットワーク層DDoS保護（Azure DDoS Protection）と組み合わせて多層防御を実現できます。これにより、ネットワーク層からアプリケーション層まで包括的なDDoS対策が可能となります。

以上が、Microsoft HTTP DDoS Ruleset for Azure WAF on Azure Front Door Premiumのパブリックプレビューに関する技術者向け詳細説明です。

---

### 5. Generally Available: Cross-region IPAM pool association in Azure Virtual Network Manager

**公開日時**: 2026年04月28日 17:45:04 UTC
**リンク**: [Generally Available: Cross-region IPAM pool association in Azure Virtual Network Manager](https://azure.microsoft.com/updates?id=561067)

**アップデートID**: 561067
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Azure Virtual Network Manager, Features, Management, Services

**要約**:

- 何が更新されたか  
Azure Virtual Network Managerにおいて、「クロスリージョンIPAMプールの関連付け」機能が一般提供（GA）されました。

- 主な変更点や新機能  
これまでIPアドレス管理（IPAM）プールは単一リージョン内でのみ仮想ネットワーク（VNet）に関連付け可能でしたが、今回のアップデートにより、1つのIPAMプールを複数リージョンにまたがるVNetに関連付けできるようになりました。これにより、グローバル規模でのIPアドレス空間の一元管理や、設定ミスのリスク低減、運用の効率化が可能となります。

- 影響を受ける対象  
複数リージョンにVNetを展開し、IPアドレス管理を行っているAzure利用者やネットワーク管理者が主な対象です。

- 注意点があれば記載  
本機能を利用する際は、各リージョン間でのIPアドレス空間の重複や、既存のネットワーク設計との整合性に注意が必要です。また、詳細な利用方法や制限事項については公式ドキュメントを参照してください。

**詳細**:

本アップデートは、「Azure Virtual Network Manager」において、クロスリージョンでのIPAM（IP Address Management）プールの関連付け機能が一般提供（GA）されたことを発表するものです。これまで、複数リージョンにまたがる仮想ネットワーク（VNet）に対してIPアドレス空間を一元的に管理することは、スケーラビリティや設定ミスの観点から課題がありました。今回のアップデートにより、単一のIPAMプールを複数のAzureリージョンにまたがる仮想ネットワークに関連付けることが可能となり、IPアドレス空間の管理が大幅に効率化されます。

具体的には、Azure Virtual Network Manager上で作成したIPAMプールを、従来は単一リージョン内のVNetにしか関連付けできなかったものが、複数リージョンのVNetに対しても関連付けられるようになります。これにより、グローバルに展開するシステムや、複数リージョンをまたぐ災害対策構成などにおいて、IPアドレスの重複や割り当てミスを防ぎつつ、統一的なIPアドレス管理が実現できます。

技術的な仕組みとしては、Azure Virtual Network ManagerのIPAM機能を利用し、IPAMプールを作成した後、そのプールを複数リージョンのVNetに対して関連付ける設定を行います。これにより、各VNetが同じIPAMプールからアドレス空間を取得できるため、IPアドレスの一元的な割り当てと管理が可能となります。また、Azure Resource Manager（ARM）テンプレートやAzure CLI、PowerShellなどの標準的なデプロイ手段を用いて自動化することもできます。

活用シナリオとしては、グローバルに分散したシステム環境や、複数リージョンにまたがるハイブリッドクラウド構成、あるいはBCP（事業継続計画）対策として複数リージョンにVNetを展開するケースが挙げられます。これらのシナリオにおいて、IPアドレス空間の重複や管理ミスを防ぎ、ネットワーク設計の一貫性を保つことが可能です。

注意点としては、クロスリージョンでのIPAMプール関連付けがサポートされるリージョンや、利用可能なVNetの数、IPアドレス空間のサイズなど、Azureのサービス制限に留意する必要があります。また、既存のVNet構成やアドレス空間設計との整合性を十分に確認した上で導入を進めることが推奨されます。

本機能は、Azure Virtual Network ManagerのIPAM機能と密接に連携して動作し、他のネットワーク管理機能やセキュリティ機能と組み合わせて利用することで、より堅牢で拡張性の高いネットワークインフラの構築が可能となります。詳細は公式ドキュメントやアップデートページ（https://azure.microsoft.com/updates?id=561067）を参照してください。

---


*このレポートは自動生成されました - 2026-04-29 12:01:30 JST*