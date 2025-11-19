# 2025年11月19日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年11月19日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 143 件

## 更新一覧

### 1. Generally Available: Claude in Microsoft Foundry

**公開日時**: 2025年11月19日 00:00:31 UTC
**リンク**: [Generally Available: Claude in Microsoft Foundry](https://azure.microsoft.com/updates?id=532303)

**アップデートID**: 532303
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
AnthropicのClaudeモデルがMicrosoft Foundryで一般提供開始。

- 主な変更点や新機能  
Claude Sonnet 4.5、Opus 4.1、Haiku 4.5が利用可能に。長文コンテキスト処理、コード生成、マルチモーダル対応が強化。

- 影響を受ける対象  
AI活用を進める企業や開発者が高度なAI機能をFoundry上で統合的に利用可能。

- 注意点  
利用にはMicrosoft Foundryの環境整備が必要。モデルの特性理解と適切な運用が重要。

**詳細**:

本アップデートにより、Anthropic社のClaudeモデル（Sonnet 4.5、Opus 4.1、Haiku 4.5）がMicrosoft Foundryプラットフォーム上で一般提供（GA）され、先端AIの統合エコシステムが拡充されました。Claude Sonnet 4.5は長文コンテキストの高度な推論に、Opus 4.1はコード生成や解析に、Haiku 4.5はマルチモーダル処理に特化しています。Microsoft FoundryはこれらモデルをAPI経由で提供し、企業は既存のデータパイプラインや分析基盤とシームレスに統合可能です。実装はRESTful API呼び出しを基本とし、Azure Active Directoryによる認証管理やスケーラブルなコンテナ基盤上で動作するため、高可用性とセキュリティを確保します。活用例としては、複雑なビジネス文書の自動要約・解析、ソフトウェア開発支援、画像とテキストの統合解析などが挙げられます。一方、長文処理に伴うレイテンシやAPI利用制限、モデルの応答品質に対する監視が必要です。Azure Synapse AnalyticsやAzure Data Factoryとの連携により、データ収集からAI解析までのワークフロー自動化が可能であり、エンタープライズのAI活用を加速します。

---

### 2. Public Preview: Azure Copilot agents - a closer look at the deployment agent 

**公開日時**: 2025年11月18日 20:15:19 UTC
**リンク**: [Public Preview: Azure Copilot agents - a closer look at the deployment agent ](https://azure.microsoft.com/updates?id=526751)

**アップデートID**: 526751
**情報源**: Azure Updates API

**カテゴリ**: In preview, Management and governance, Azure Copilot

**要約**:

- 何が更新されたか  
Azure Copilotの新機能として、6つのエージェントのうち「デプロイメントエージェント」がパブリックプレビューで提供開始。

- 主な変更点や新機能  
クラウドワークロードの検出、計画、展開を自動化し、迅速かつ確実にデプロイ可能にするエージェント機能を追加。

- 影響を受ける対象  
Azure上でのクラウドリソース管理やデプロイを行う開発者・運用担当者。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討し、フィードバック提供が推奨される。

**詳細**:

本アップデートは、Azure Copilotのエージェント機能強化の一環として公開された「Deployment Agent」のパブリックプレビュー提供を目的としています。Deployment Agentはクラウドワークロードの発見、計画、展開を自動化・高速化し、運用の信頼性を向上させるエージェント型AIツールです。具体的には、既存環境のリソースをスキャンし最適な展開プランを生成、IaC（Infrastructure as Code）テンプレートの自動作成やデプロイ実行を支援します。技術的にはAzure Resource Manager（ARM）APIやTerraformなどのIaCツールと連携し、Azure DevOpsやGitHub Actionsを通じたCI/CDパイプラインに組み込むことが可能です。活用例としては、複雑なマルチリソース環境の一括展開や既存リソースのリファクタリング計画策定が挙げられます。注意点としては、現時点でプレビュー段階のため一部リソースタイプの対応が限定的であり、商用環境導入前に十分な検証が必要です。関連サービスとしてAzure MonitorやAzure Policyと連携し、展開後の監視・ガバナンス強化も図れます。詳細は公式ドキュメントを参照してください。

---

### 3. Private Preview: Azure HorizonDB 

**公開日時**: 2025年11月18日 18:00:28 UTC
**リンク**: [Private Preview: Azure HorizonDB ](https://azure.microsoft.com/updates?id=529806)

**アップデートID**: 529806
**情報源**: Azure Updates API

**カテゴリ**: In development

**要約**:

- 何が更新されたか  
Azure HorizonDB for PostgreSQLがプライベートプレビューで提供開始。

- 主な変更点や新機能  
最大128TBの自動スケーリングストレージ、オープンソースPostgreSQL比で最大3倍の高速性能、最大3,072vCoreまでの迅速なコンピュートスケールが可能。

- 影響を受ける対象  
大規模データベースを扱う開発者や運用者、パフォーマンスとスケーラビリティを重視するエンタープライズユーザー。

- 注意点  
現時点はプライベートプレビューのため、利用には申請が必要で一般提供前。

**詳細**:

Azure HorizonDB for PostgreSQLは、高性能と大規模スケーラビリティを実現するために設計された新しいマネージドデータベースサービスで、現在プライベートプレビュー段階にあります。最大128TBの自動スケーリングストレージを備え、オープンソースのPostgreSQLと比較して最大3倍のパフォーマンス向上を実現。コンピュートリソースは最大3,072vCoreまで迅速にスケール可能です。内部的には、分散ストレージとコンピュートの分離アーキテクチャを採用し、負荷に応じたリソース割り当てを動的に調整。これにより、高負荷時でも一貫した低レイテンシと高スループットを維持します。主な活用シナリオは、大規模なトランザクション処理や分析ワークロード、リアルタイムデータ処理が求められるエンタープライズアプリケーションです。注意点としては、現時点でプライベートプレビューのため利用には申請が必要で、一般提供時まで機能や性能が変更される可能性があります。また、既存のAzure Database for PostgreSQLとは異なるサービスであり、移行時は互換性や接続設定の確認が必要です。Azure Synapse AnalyticsやAzure Data Factoryとの連携により、データ統合や分析基盤の構築が容易になるため、エンドツーエンドのデータパイプライン構築に適しています。

---

### 4. Generally Available: Private Marketplace for VS Code

**公開日時**: 2025年11月18日 18:00:28 UTC
**リンク**: [Generally Available: Private Marketplace for VS Code](https://azure.microsoft.com/updates?id=526909)

**アップデートID**: 526909
**情報源**: Azure Updates API

**カテゴリ**: Launched, Developer tools, Visual Studio, Features, SDK and Tools, Microsoft Ignite

**要約**:

- 何が更新されたか  
VS Code向けのPrivate Marketplaceが一般提供（GA）開始。

- 主な変更点や新機能  
企業内で拡張機能を安全にホスト・管理可能。VS Codeと完全統合され、チームによるセルフホスティング、簡単な展開、柔軟な更新管理が可能。

- 影響を受ける対象  
エンタープライズ環境でVS Code拡張機能の管理を行う開発チーム。

- 注意点  
内部管理のためのインフラ整備や運用ルールの策定が必要。  

詳細：https://azure.microsoft.com/updates?id=526909

**詳細**:

Azureの「VS Code Private Marketplace」機能が一般提供（GA）されました。本機能は、企業内でVS Code拡張機能を安全かつ効率的にホスティング・管理するためのエンタープライズ対応ソリューションです。背景には、組織独自のポリシーに準拠した拡張機能の配布や、外部マーケットプレイスに依存しない管理ニーズの高まりがあります。

主な機能として、拡張機能の社内ホスティング、バージョン管理、配布制御が可能で、VS Codeとシームレスに統合されます。これにより、チームは拡張機能の導入・更新を自律的に行え、セキュリティリスクを低減しつつ柔軟な運用が実現します。技術的には、拡張機能のパッケージをプライベートリポジトリに登録し、VS Codeの設定でプライベートマーケットプレイスを指定することで利用可能です。

活用例としては、社内開発標準に沿ったカスタム拡張機能の配布や、特定バージョンの強制適用、外部公開前の検証環境構築などが挙げられます。注意点としては、プライベートマーケットプレイスの運用には適切なアクセス制御と更新管理が必要であり、外部拡張機能との競合や依存関係の管理にも留意が必要です。

Azure DevOpsやAzure Active Directoryとの連携により、認証・権限管理やCI/CDパイプラインを通じた自動デプロイが可能で、企業の開発プロセスに統合しやすくなっています。詳細は公式ドキュメント（https://azure.microsoft.com/updates?id=526909）を参照ください。

---

### 5. Public Preview: Microsoft Defender for Cloud + GitHub Advanced Security 

**公開日時**: 2025年11月18日 18:00:28 UTC
**リンク**: [Public Preview: Microsoft Defender for Cloud + GitHub Advanced Security ](https://azure.microsoft.com/updates?id=526876)

**アップデートID**: 526876
**情報源**: Azure Updates API

**カテゴリ**: In preview, Hybrid + multicloud, Security, DevOps, Microsoft Defender for Cloud, GitHub Advanced Security for Azure DevOps

**要約**:

- 何が更新されたか  
Microsoft Defender for CloudとGitHub Advanced Securityの統合がパブリックプレビューで提供開始。

- 主な変更点や新機能  
コードからクラウドまでのアプリライフサイクル全体を保護し、開発者とセキュリティチームが一つのワークフローで連携可能に。

- 影響を受ける対象  
クラウドネイティブアプリケーションの開発・運用に関わる技術者およびセキュリティ担当者。

- 注意点があれば記載  
現段階はパブリックプレビューのため、本番環境での利用は慎重に検討すること。

**詳細**:

本アップデートは、Microsoft Defender for CloudとGitHub Advanced Securityを統合し、クラウドネイティブアプリケーションの開発から運用までのセキュリティを一元管理することを目的としています。これにより、開発者とセキュリティチームが同一ワークフロー内で連携可能となり、コードの脆弱性検出からクラウド環境の保護までシームレスに対応可能です。具体的には、GitHubリポジトリ内のコードスキャンや依存関係の解析結果をDefender for Cloudのセキュリティポスチャ管理に統合し、リアルタイムでリスクを可視化します。技術的には、GitHub Actionsを活用した自動コード解析とDefender for Cloudのポリシー評価が連携し、アラートや推奨事項をAzureポータルで一元管理可能です。活用シナリオとしては、CI/CDパイプライン内での脆弱性検出と修正、及び運用中のクラウドリソースのセキュリティ強化が挙げられます。注意点としては、現段階がパブリックプレビューであるため、機能の安定性やサポート範囲に制限がある点に留意が必要です。関連サービスとしては、Azure Security Center（Defender for Cloudの前身）、Azure DevOps、Azure Monitorとの連携が可能で、統合的なセキュリティ運用を実現します。

---

### 6. Public Preview: Smart Tier account level tiering (Azure Blob Storage and ADLS)

**公開日時**: 2025年11月18日 18:00:28 UTC
**リンク**: [Public Preview: Smart Tier account level tiering (Azure Blob Storage and ADLS)](https://azure.microsoft.com/updates?id=526188)

**アップデートID**: 526188
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Analytics, Azure Blob Storage, Azure Data Lake Storage

**要約**:

- 何が更新されたか  
Azure Blob StorageおよびAzure Data Lake Storageで、アカウントレベルのスマートティアリング機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
データのアクセスパターンに応じて自動的にストレージ階層を切り替える完全マネージドの自動データティアリングを実現。手動での階層管理が不要に。

- 影響を受ける対象  
Azure Blob StorageおよびADLSを利用するストレージアカウント全般。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に。利用前に動作検証を推奨。  

情報源: https://azure.microsoft.com/updates?id=526188

**詳細**:

本アップデートは、Azure Blob StorageおよびAzure Data Lake Storage（ADLS）におけるアカウントレベルのスマートティアリング機能のパブリックプレビュー開始を告知するものです。背景として、従来の手動によるデータ階層管理の煩雑さと運用負荷を軽減し、コスト最適化とパフォーマンス維持を自動化するニーズが高まったことが挙げられます。スマートティアは、アクセスパターンを機械学習で解析し、ホット、クール、アーカイブの各ストレージ階層間でデータを自動的に移動させるフルマネージドサービスです。アカウント単位での設定により、個別のコンテナやBLOB単位での手動設定が不要となり、運用効率が大幅に向上します。実装はAzureポータルやCLI、ARMテンプレートから有効化可能で、既存データに対しても即座に適用されます。活用シナリオとしては、ログデータやIoTデータの長期保存、分析データのコスト効率的な管理が挙げられます。注意点としては、スマートティア適用中のデータ移動に伴う一時的なアクセスレイテンシ増加や、アーカイブ階層からの復元に時間がかかる点が挙げられます。また、特定のリージョンやストレージアカウントの種類によっては対応状況が異なるため事前確認が必要です。関連サービスとしては、Azure Monitorによるアクセスパターンの監視や、Azure Cost Managementでのコスト分析と組み合わせることで、運用の最適化が図れます。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 7. Public Preview: Managed Instance on Azure App Service

**公開日時**: 2025年11月18日 18:00:28 UTC
**リンク**: [Public Preview: Managed Instance on Azure App Service](https://azure.microsoft.com/updates?id=523623)

**アップデートID**: 523623
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Mobile, Web, App Service

**要約**:

- 何が更新されたか  
Azure App Serviceで「Managed Instance」がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
オンプレやVM上の.NETアプリをコード変更なしでクラウド移行可能に。設定も最小限で済むため、移行工数を大幅削減。

- 影響を受ける対象  
既存の.NETアプリケーション開発者および運用者、クラウド移行を検討中の技術者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、商用利用前に機能制限やサポート状況を確認すること。

**詳細**:

Azure App Serviceの新機能「Managed Instance on Azure App Service」がパブリックプレビューとして公開されました。本機能は、オンプレミスやVM上で稼働する.NET Webアプリをコード変更なしでクラウド移行可能にすることを目的としています。具体的には、従来複雑だったインフラ設定や環境構築をAzureが管理するマネージドインスタンスとして提供し、アプリのホスティングとスケーリングを容易にします。技術的には、App ServiceのPaaS環境上に専用の管理インスタンスを構築し、既存のアプリケーション設定をほぼそのまま利用可能です。活用シナリオとしては、レガシー.NETアプリのクラウド移行やハイブリッド環境からの段階的移行が挙げられます。注意点としては、現時点で対応する言語やフレームワークに制限があり、パブリックプレビューのためSLA保証や一部機能が限定される可能性があります。Azure SQL Managed InstanceやAzure Monitorとの連携により、データベース管理やパフォーマンス監視も統合的に行えます。詳細は公式ドキュメントを参照してください。

---

### 8. Public Preview: Entra-only identities support with Azure Files SMB 

**公開日時**: 2025年11月18日 17:30:44 UTC
**リンク**: [Public Preview: Entra-only identities support with Azure Files SMB ](https://azure.microsoft.com/updates?id=527713)

**アップデートID**: 527713
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure Files

**要約**:

- 何が更新されたか  
Azure FilesがEntra-onlyアイデンティティをサポートするパブリックプレビューを開始。

- 主な変更点や新機能  
オンプレのドメインコントローラー不要で、Microsoft Entra KerberosによるクラウドネイティブなSMB認証が可能に。

- 影響を受ける対象  
Azure Filesを利用し、SMBアクセスを管理する企業や技術者。

- 注意点  
現時点はパブリックプレビューのため、本番環境での利用は慎重に。オンプレ依存からの移行計画が必要。

**詳細**:

本アップデートは、Azure FilesのSMBアクセスにおいてオンプレミスのドメインコントローラー不要でMicrosoft Entra ID（旧Azure AD）単独の認証を可能にすることを目的としています。従来はオンプレ環境のActive Directory連携が必須でしたが、Entra-only identities対応により完全クラウドネイティブなKerberos認証が実現され、ハイブリッド環境の複雑さや運用コストを削減します。技術的にはMicrosoft Entra Kerberosを用い、Azure FilesのSMB共有に対してEntra IDのユーザー・グループ情報を基にトークン発行と認証を行います。実装はAzureポータルやPowerShellでEntra ID統合設定を有効化し、クライアント側はWindows 11以降や最新のSMBクライアントで対応可能です。活用例としては、オンプレADの廃止やクラウドネイティブ環境への移行を進める企業が、ファイル共有のセキュリティを維持しつつ管理負荷を軽減できます。注意点としては、現時点で一部の古いOSやクライアントは非対応であり、Entra IDのKerberosチケット取得に関するポリシー設定が必要です。関連サービスとしてMicrosoft Entra ID、Azure AD Kerberosサービスプリンシパル、Azure Filesが密接に連携し、統合認証基盤を構築します。詳細は公式ドキュメントを参照し、環境に応じた設定検証を推奨します。

---

### 9. Private Preview: Azure Boost confidential device

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Private Preview: Azure Boost confidential device](https://azure.microsoft.com/updates?id=530661)

**アップデートID**: 530661
**情報源**: Azure Updates API

**カテゴリ**: In development

**要約**:

- 何が更新されたか  
Azure Boost confidential device機能がプライベートプレビューで提供開始。

- 主な変更点や新機能  
ハイパーバイザーやホストOSの仮想化タスク（ネットワーク、ストレージ、ホスト管理）を専用ハードウェアとソフトウェアにオフロードし、性能とセキュリティを向上。

- 影響を受ける対象  
仮想化環境を運用するAzureユーザーやクラウドインフラ技術者。

- 注意点  
現時点はプライベートプレビューのため、利用には申請が必要であり、一般提供時期は未定。

**詳細**:

Azure Boost confidential deviceは、現在プライベートプレビュー段階にある機能で、仮想化環境のパフォーマンスとセキュリティを向上させることを目的としています。従来、ハイパーバイザーやホストOSが担っていたネットワーク、ストレージ、ホスト管理といった仮想化タスクを、専用設計のハードウェアおよびソフトウェアにオフロードする仕組みです。これにより、ホストの負荷軽減と処理効率の最適化が実現され、機密性の高いデータ処理においてもセキュリティ強化が期待できます。

技術的には、Azure Boostは専用のセキュアなハードウェアモジュールを用い、仮想化スタックの一部を分離・専任化することで、ホストOSの攻撃面を低減します。実装はAzureの仮想マシンホスト上で動作し、ハイパーバイザーの負担を軽減しつつ、ネットワークI/OやストレージI/Oの処理を高速化します。これにより、特に高負荷なクラウドサービスや機密データを扱うワークロードに最適です。

活用シナリオとしては、金融や医療などの規制産業における機密情報の処理、または大規模な仮想ネットワークを持つ環境でのパフォーマンス改善が挙げられます。注意点としては、現時点でプライベートプレビューのため利用には申請が必要であり、対応するVMサイズやリージョンが限定される可能性があります。

Azure Confidential ComputingやAzure Virtual Machinesとの連携が想定され、これらと組み合わせることで、より強固なセキュリティと効率的なリソース管理が可能となります。今後の正式リリースに向けて、検証環境での評価が推奨されます。詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=530661）を参照してください。

---

### 10. Public Preview: Microsoft HTTP DDoS Ruleset 1.0 on Application Gateway WAF v2

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Microsoft HTTP DDoS Ruleset 1.0 on Application Gateway WAF v2](https://azure.microsoft.com/updates?id=530609)

**アップデートID**: 530609
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Application Gateway, Azure DDoS Protection, Web Application Firewall

**要約**:

- 何が更新されたか  
Application Gateway WAF v2向けにHTTP DDoSルールセット1.0がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
HTTPレイヤーのDDoS攻撃に対し、従来の静的ルールを超える動的検知・防御が可能に。進化するボットネット対策を強化。

- 影響を受ける対象  
Application Gateway WAF v2を利用するWebアプリケーション。

- 注意点があれば記載  
プレビュー版のため、本番環境での利用は慎重に。設定や挙動を十分検証することを推奨。

**詳細**:

本アップデートは、Application Gateway WAF v2におけるHTTPレイヤーDDoS攻撃対策強化を目的とした「Microsoft HTTP DDoS Ruleset 1.0」のパブリックプレビュー提供開始を告知するものです。HTTP層のDDoS攻撃はアプリケーション停止の主要因であり、従来の静的ルールでは高度化するボットネットに対応困難でした。本ルールセットは動的かつシグネチャベースの検知ロジックを組み込み、異常なHTTPリクエストパターンをリアルタイムで識別し遮断します。実装はWAF v2のカスタムルールとして適用可能で、自動更新により最新の攻撃手法にも対応可能です。典型的な活用例は、Webアプリケーションへの大量リクエストによるサービス妨害防止で、特にeコマースや金融系アプリケーションでの利用が想定されます。注意点としては、プレビュー機能のため一部環境での挙動検証が必要であり、誤検知による正常トラフィック遮断リスクを考慮し段階的な適用が推奨されます。Azure MonitorやAzure Sentinelと連携することで、攻撃検知ログの分析や自動応答ルール構築が可能です。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 11. Private Preview: Azure Boost remote storage throughput and network bandwidth enhancements

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Private Preview: Azure Boost remote storage throughput and network bandwidth enhancements](https://azure.microsoft.com/updates?id=530287)

**アップデートID**: 530287
**情報源**: Azure Updates API

**カテゴリ**: In development

**要約**:

- 何が更新されたか  
Azure Boostの最新アーキテクチャにおけるリモートストレージのスループットとネットワーク帯域幅の性能強化がプライベートプレビューで提供開始。

- 主な変更点や新機能  
仮想化のオフロード機能を強化し、ストレージI/Oとネットワーク通信の効率を向上。これにより、リモートストレージアクセスの高速化と帯域幅の最適化が可能に。

- 影響を受ける対象  
Azure上で仮想化環境を利用し、リモートストレージやネットワーク性能を重視するエンタープライズユーザーやクラウドインフラ技術者。

- 注意点があれば記載  
現時点はプライベートプレビューのため、利用には申請が必要であり、一般提供前の機能である点に留意。

**詳細**:

本プライベートプレビューは、Azure Boostアーキテクチャの最新強化により、リモートストレージのスループットおよびネットワーク帯域幅性能を大幅に向上させることを目的としています。Azure Boostは、仮想化環境におけるネットワーク、ストレージ、ホスト管理の処理負荷を専用ハードウェアにオフロードすることで、ホストのCPUリソースを節約し、I/O性能を最適化するシステムです。今回のアップデートでは、特にリモートストレージアクセスの遅延削減と帯域幅拡張に注力し、RDMA（Remote Direct Memory Access）技術やカスタムネットワークスタックの改良を通じて、データ転送効率を高めています。これにより、大規模分散ストレージや高スループットを要求するアプリケーションでのパフォーマンス向上が期待されます。実装はAzureの仮想ネットワークおよびストレージサービスと密接に連携し、既存のVMやコンテナ環境に透過的に適用可能です。ただし、現時点ではプライベートプレビューのため利用には申請が必要であり、対応リージョンやVMサイズに制限があります。今後、Azure NetApp FilesやAzure Blob Storageなどのストレージサービスとの連携強化も見込まれており、高性能クラウドストレージ基盤の構築に寄与します。

---

### 12. Public Preview: NVv6 Virtual Machines

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: NVv6 Virtual Machines](https://azure.microsoft.com/updates?id=530208)

**アップデートID**: 530208
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Virtual Machines

**要約**:

- 何が更新されたか  
AzureでNCシリーズの次世代VM「NCv6 RTX PRO 6000 Blackwell Server Edition」のパブリックプレビューが開始されました。

- 主な変更点や新機能  
最新のNVIDIA RTX PRO 6000 BSE GPUを搭載し、高度なグラフィックス処理やAI、シミュレーションなど幅広いワークロードの高速化が可能です。

- 影響を受ける対象  
GPUを活用するグラフィックス処理、機械学習、科学計算などの技術者や開発者。

- 注意点があれば記載  
プレビュー段階のため、商用利用前に性能や互換性を検証する必要があります。

**詳細**:

AzureはNCシリーズの次世代GPU仮想マシンとして、Public PreviewでNVv6（NCv6 RTX PRO 6000 Blackwell Server Edition）VMを提供開始しました。本アップデートは、NVIDIA RTX PRO 6000 Blackwell GPUを搭載し、グラフィック集約型やAI推論、3Dレンダリング、シミュレーションなど多様なワークロードの高速化を目的としています。NVv6はAMD EPYC CPUと組み合わせ、GPUリソースを仮想化することで柔軟なスケーラビリティを実現。PCIe Gen4接続により高帯域幅を確保し、低レイテンシでGPUアクセラレーションを提供します。活用例としては、リアルタイムレンダリング、CAD/CAM、機械学習推論環境の構築が挙げられます。注意点としては、プレビュー段階のためリージョン展開が限定的であり、利用にはAzureサブスクリプションの申請が必要です。また、GPUドライバの最新バージョン適用や対応するAzure Machine LearningやAzure Kubernetes Serviceとの連携により、GPUリソースの効率的な管理とスケジューリングが可能です。NVv6は高性能GPUをクラウドで柔軟に利用したい技術者にとって有力な選択肢となります。詳細は公式ドキュメント参照推奨。

---

### 13. Public Preview: New integration and extensibility capabilities to Azure SRE Agent

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: New integration and extensibility capabilities to Azure SRE Agent](https://azure.microsoft.com/updates?id=529944)

**アップデートID**: 529944
**情報源**: Azure Updates API

**カテゴリ**: In preview

**要約**:

- 何が更新されたか  
Azure SRE Agentに新たな統合・拡張機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
AI駆動の運用自動化レイヤーが他のツールやサービスと連携可能になり、カスタム拡張もサポート。運用ワークフローの柔軟性と効率が向上します。

- 影響を受ける対象  
Azureのクラウド運用担当者やSREチーム、運用自動化を推進する技術者。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討してください。  

https://azure.microsoft.com/updates?id=529944

**詳細**:

本アップデートは、Azure SRE Agentのパブリックプレビューとして、新たな統合および拡張機能を提供し、運用自動化の柔軟性と効率性を向上させることを目的としています。Azure SRE AgentはAIを活用し、従来の静的なスクリプトベース自動化から脱却し、プロンプト駆動型の統合運用レイヤーを実現します。今回の拡張では、外部システムやカスタムAPIとの連携が強化され、WebhookやREST APIを介した双方向通信が可能となりました。これにより、運用フローのカスタマイズやサードパーティツールとの統合が容易になり、複雑なワークロードの自動化が促進されます。技術的には、Azure SRE AgentのAIモデルがユーザーのプロンプトを解析し、適切なAPI呼び出しやスクリプト実行を動的に生成・実行する仕組みを採用しています。活用例としては、インシデント対応時の自動診断・修復、運用ダッシュボードからのリアルタイム操作、複数クラウド環境の統合管理などが挙げられます。注意点としては、プレビュー段階のためAPI仕様変更の可能性や一部機能の制限がある点、また適切な認証設定と権限管理が必須です。Azure Monitor、Azure Logic Apps、Azure Functionsとの連携により、監視データのトリガーから自動化実行までの一連の運用プロセスをシームレスに構築可能です。

---

### 14. Generally Available: Advanced sampling and richer data collection in Azure Monitor OpenTelemetry Distro

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Advanced sampling and richer data collection in Azure Monitor OpenTelemetry Distro](https://azure.microsoft.com/updates?id=529519)

**アップデートID**: 529519
**情報源**: Azure Updates API

**カテゴリ**: Launched, DevOps, Management and governance, Azure Monitor

**要約**:

- 何が更新されたか  
Azure Monitor OpenTelemetry Distroに高度なサンプリング機能と詳細なデータ収集機能がGA（一般提供）された。

- 主な変更点や新機能  
レート制限付きサンプリングとトレースベースのログサンプリングが追加され、効率的なデータ収集とコスト最適化が可能に。

- 影響を受ける対象  
Azure Monitor Application Insightsを利用する開発者や運用チーム。

- 注意点  
サンプリング設定の最適化が必要で、誤設定によるデータ欠落に注意。

**詳細**:

本アップデートは、Azure Monitor Application Insightsの基盤であるAzure Monitor OpenTelemetry Distroに対し、オープンスタンダードの採用を強化し、より高度なサンプリング機能と豊富なデータ収集を実現することを目的としています。具体的には、レート制限付きサンプリングとトレースベースのログサンプリングが新たに追加されました。レート制限付きサンプリングは、一定時間内に収集するトレース数を制御し、過負荷を防止します。一方、トレースベースログサンプリングは、関連するトレース情報に基づきログを選択的に収集することで、関連性の高いデータの効率的な取得を可能にします。これらはOpenTelemetryのSDK設定や環境変数で容易に有効化でき、トレースとログの一貫性を保ちながらコスト最適化を図れます。活用例としては、高トラフィック環境でのパフォーマンス監視や異常検知時の詳細ログ収集が挙げられます。注意点として、サンプリング率の設定ミスにより重要なデータが欠落するリスクがあるため、適切なチューニングが必要です。Azure MonitorやApplication Insightsとの連携により、収集データは統合的に分析・可視化可能で、運用効率の向上に寄与します。

---

### 15. Public Preview: Azure Network Watcher Topology – Agentless Connection Troubleshoot

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Network Watcher Topology – Agentless Connection Troubleshoot](https://azure.microsoft.com/updates?id=527815)

**アップデートID**: 527815
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Management and governance, Networking, Azure Kubernetes Service (AKS), Network Watcher

**要約**:

- 何が更新されたか  
Azure Network WatcherのTopology機能にて、AKSクラスタの可視化がパブリックプレビューで提供開始。

- 主な変更点や新機能  
AKS環境のネットワーク構成をエンドツーエンドで視覚化可能に。エージェント不要の接続トラブルシュートもサポート。

- 影響を受ける対象  
AKSを利用するネットワーク管理者や運用技術者。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に。機能やUIは今後変更される可能性あり。

**詳細**:

本アップデートは、Azure Network WatcherのTopology機能において、Azure Kubernetes Service（AKS）クラスタのネットワーク構成をエージェント不要で可視化するパブリックプレビューを提供します。従来、AKSのネットワークトポロジー把握にはエージェントの導入や複雑な設定が必要でしたが、本機能によりAzureポータル上で直接AKSのPod、ノード、サービス間の通信経路を視覚的に確認可能となり、トラブルシューティングの効率化を実現します。技術的には、AzureのコントロールプレーンとNetwork Watcherが連携し、API経由でAKSのネットワーク状態情報を取得、解析してTopology図を生成します。これにより、エージェントレスでの接続問題検出や通信経路の把握が可能です。活用例としては、AKS内の通信障害調査やネットワークポリシーの影響分析が挙げられます。制限事項としては、現時点でパブリックプレビューのため一部リージョン非対応や機能制限が存在し、正式リリース前の仕様変更リスクがあります。関連サービスとして、Network Watcherの接続トラブルシュート機能やAzure Monitorと連携し、ログ解析やアラート設定と組み合わせることで包括的なネットワーク監視が可能です。

---

### 16. Public Preview: Azure Network Watcher Topology – AKS Visualization

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Network Watcher Topology – AKS Visualization](https://azure.microsoft.com/updates?id=527810)

**アップデートID**: 527810
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Management and governance, Networking, Azure Kubernetes Service (AKS), Network Watcher

**要約**:

- 何が更新されたか  
Azure Network WatcherのTopology機能にて、AKSクラスタの可視化がパブリックプレビューで提供開始。

- 主な変更点や新機能  
AKS環境のネットワーク構成をAzureポータル上でエンドツーエンドに視覚化可能に。クラスタ内のリソース間接続や通信経路を直感的に把握できる。

- 影響を受ける対象  
AKSを利用するネットワーク管理者や運用技術者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、商用環境での利用は慎重に。フィードバックを基に今後機能改善が予定されている。

**詳細**:

Azure Network WatcherのTopology機能において、AKSクラスタの可視化がパブリックプレビューとして提供開始されました。本アップデートは、AKSのネットワーク構成をAzureポータル内で一元的に把握しやすくすることを目的としています。具体的には、クラスタ内のノード、Pod、サービス間のネットワーク接続や負荷分散の状態をグラフィカルに表示し、トラブルシューティングや設計検証を支援します。技術的には、Network WatcherがAKSのAPIを通じてクラスタ情報を取得し、仮想ネットワークやサブネット、ネットワークインターフェースとの関連付けを行い、Topology図として描画します。活用シナリオとしては、複雑なマイクロサービス間通信の可視化、ネットワークポリシー適用状況の確認、障害発生時の通信経路解析が挙げられます。制限事項としては、現時点で対応するAKSバージョンやリージョンが限定的であること、またプレビュー機能のため一部UIや機能が変更される可能性があります。関連サービスとしては、Network Watcherのパケットキャプチャや接続モニターと連携し、より詳細なネットワーク診断が可能です。実運用前にプレビュー環境で動作検証を推奨します。

---

### 17. Public Preview: Azure VNet Flow Log - Filtering 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure VNet Flow Log - Filtering ](https://azure.microsoft.com/updates?id=527805)

**アップデートID**: 527805
**情報源**: Azure Updates API

**カテゴリ**: In preview, Management and governance, Networking, Network Watcher

**要約**:

- 何が更新されたか  
Azure VNet Flow Logに高度なフィルタリング機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
VNet、サブネット、NICを流れるIPトラフィックのログ収集時に、特定のトラフィックのみを抽出可能となり、監視やトラブルシューティング、セキュリティ分析の効率が向上します。

- 影響を受ける対象  
VNet Flow Logを利用しているネットワーク管理者やセキュリティエンジニア。

- 注意点  
パブリックプレビューのため、本番環境での利用は慎重に行い、フィードバックを活用してください。

**詳細**:

本アップデートは、Azure VNet Flow Logに高度なフィルタリング機能をPublic Previewとして追加したものです。従来のVNet Flow LogはVNet、サブネット、NIC間のIPトラフィックを全量記録し、監視やトラブルシューティングに利用されていましたが、トラフィック量増大に伴うログの膨大化や解析負荷が課題でした。本機能は、特定のIPアドレス、ポート、プロトコル、方向（送信/受信）などを条件にログ記録対象を絞り込むことで、必要なトラフィックのみを効率的に収集可能とします。実装はNetwork WatcherのFlow Log設定においてJSON形式のフィルターポリシーを適用し、Azure MonitorやStorage Accountへのログ送信前にフィルタリングを実施します。これにより、セキュリティインシデントの特定やネットワークパフォーマンス分析の精度向上が期待されます。活用例としては、特定サブネット内の異常通信検知や、特定ポートのみの通信監査が挙げられます。注意点としては、フィルタリング設定の誤りにより重要なログが除外されるリスクや、現時点で一部のリージョン・リソースタイプでの対応状況に制限がある点が挙げられます。Azure SentinelやNetwork Security Group (NSG) と連携することで、より高度なセキュリティ分析や自動化運用が可能です。詳細は公式ドキュメントを参照してください。

---

### 18. Generally Available: ExpressRoute Scalable Gateway

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: ExpressRoute Scalable Gateway](https://azure.microsoft.com/updates?id=526729)

**アップデートID**: 526729
**情報源**: Azure Updates API

**カテゴリ**: Launched, Hybrid + multicloud, Networking, Azure ExpressRoute, Features, Services, Microsoft Ignite

**要約**:

- 何が更新されたか  
ExpressRouteの新世代ゲートウェイ「ExpressRoute Scalable Gateway」が一般提供開始。

- 主な変更点や新機能  
ゲートウェイのインフラを動的にスケール可能となり、柔軟性とパフォーマンス、運用の簡素化を実現。

- 影響を受ける対象  
ExpressRouteを利用するAzureネットワーク技術者やインフラ運用者。

- 注意点があれば記載  
既存のゲートウェイからの移行計画やスケール設定の理解が必要。  

https://azure.microsoft.com/updates?id=526729

**詳細**:

AzureのExpressRoute Scalable Gateway（ErGwScale）は、従来のExpressRouteゲートウェイの性能・柔軟性を大幅に向上させる次世代ソリューションです。背景には、クラウド環境のトラフィック増加や多様化するネットワーク要件に対応するため、ゲートウェイのスケーラビリティと運用効率の強化が求められたことがあります。ErGwScaleは、ゲートウェイのインフラを動的にスケールアウト可能とし、帯域幅の増減に応じて自動的にリソースを調整。これによりピーク時のパフォーマンス低下を防ぎつつ、コスト効率も最適化します。技術的には、複数のゲートウェイユニットをクラスタリングし、負荷分散と冗長性を実現。Azure PortalやCLI、APIからスケール操作が可能で、既存のExpressRoute回線やVirtual Network Gateway設定との互換性を保ちます。活用例としては、大規模なオンプレミスネットワークとの接続や、複数リージョン間の高帯域幅通信が挙げられます。注意点として、スケールアウト時に一時的な接続遅延が発生する可能性があり、また一部古いSKUとの併用は制限されます。関連サービスでは、Azure Virtual WANやNetwork Managerと連携し、統合的なネットワーク管理とセキュリティポリシー適用が可能です。ErGwScaleは、拡張性と運用の簡素化を両立し、Azureネットワーク設計の柔軟性を大幅に向上させる重要なアップデートです。

---

### 19. Generally Available: Azure Container Registry Repository Permissions with Attribute-based Access Control (ABAC)

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Container Registry Repository Permissions with Attribute-based Access Control (ABAC)](https://azure.microsoft.com/updates?id=526644)

**アップデートID**: 526644
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Container Registry

**要約**:

- 何が更新されたか  
Azure Container Registry（ACR）でリポジトリ単位の権限管理がABAC（属性ベースアクセス制御）に対応し、一般提供（GA）となった。

- 主な変更点や新機能  
Microsoft Entra IDの属性に基づき、最小権限でのイメージのプッシュ・プル権限を細かく制御可能に。

- 影響を受ける対象  
ACRを利用し、セキュアにコンテナイメージのアクセス管理を行いたい組織や開発チーム。

- 注意点があれば記載  
ABAC設定にはMicrosoft Entraの属性設計が必要で、適切なポリシー設計が求められる。

**詳細**:

本アップデートは、Azure Container Registry（ACR）におけるリポジトリ単位の権限管理を属性ベースアクセス制御（ABAC）で実現し、最小権限の原則を強化することを目的としています。従来のロールベースアクセス制御（RBAC）ではリポジトリ全体へのアクセス権付与が主であったのに対し、ABAC導入によりユーザーやサービスプリンシパルの属性（例：所属部署、環境タグ）に基づき、特定リポジトリのプッシュ・プル権限を細かく制御可能です。実装はMicrosoft Entra IDの属性を活用し、ACRのリポジトリスコープに対して条件付きアクセスポリシーを設定する形で行います。これにより、CI/CDパイプラインやマルチテナント環境でのセキュアなイメージ管理が容易になります。活用例としては、開発チームごとに異なるリポジトリアクセス権を付与し、不必要な権限拡大を防止するケースが挙げられます。注意点としては、ABAC対応はACR Premium SKU以上が必要であり、属性管理の整備が前提となる点です。また、Azure DevOpsやGitHub ActionsなどのCI/CDツールと連携しやすく、ID管理とアクセス制御の一元化が可能です。

---

### 20. Public Preview: Azure Kubernetes Service desktop 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Kubernetes Service desktop ](https://azure.microsoft.com/updates?id=526242)

**アップデートID**: 526242
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）向けの新しいデスクトップアプリ「AKS desktop」がパブリックプレビューで提供開始。

- 主な変更点や新機能  
アプリケーション中心のGUIで、AKSのワークロード展開・管理をガイド付きかつセルフサービスで実施可能。AKSの既存機能やベストプラクティス、オープンソースHeadlampをベースに構築。

- 影響を受ける対象  
AKSを利用する開発者・運用担当者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に。今後のアップデートに注意。

**詳細**:

Azure Kubernetes Service (AKS) desktopは、AKS上のワークロード管理をアプリケーション中心に簡素化する新しいデスクトップアプリケーションで、現在パブリックプレビューとして提供されています。本アップデートは、複雑なKubernetes操作をGUIで直感的に行えるようにし、開発者や運用担当者の生産性向上を目的としています。AKSの標準機能やベストプラクティスをベースに、オープンソースのHeadlampプロジェクトを活用し、セルフサービス型のガイド付きインターフェースを実現。具体的には、クラスターの状態監視、ポッドやサービスの管理、ログ閲覧、リソースのデプロイなどを一元的に操作可能です。技術的には、AKS APIとKubernetes APIを統合し、認証はAzure ADと連携してセキュアに管理。ローカル環境にインストールして利用し、ネットワーク経由でAKSクラスターに接続します。活用例としては、マルチクラスター運用時のリソース管理や、CI/CDパイプラインのトラブルシューティング、開発環境での迅速な検証が挙げられます。注意点としては、プレビュー版のため一部機能が限定的であり、商用環境での利用は慎重を要します。Azure MonitorやAzure Policyと連携することで、監視・ガバナンス機能を強化可能です。これにより、AKSの運用効率化と開発速度向上が期待されます。

---

### 21. Generally Available: Pod sandboxing on AKS 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Pod sandboxing on AKS ](https://azure.microsoft.com/updates?id=526237)

**アップデートID**: 526237
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
AKSでPodサンドボックス機能が一般提供開始されました。

- 主な変更点や新機能  
各Podを専用のVM上で実行し、コンテナ間の分離とセキュリティを強化。共有環境でのワークロード隔離が向上します。

- 影響を受ける対象  
AKSを利用し、セキュリティや分離性を重視するコンテナワークロードの運用者。

- 注意点があれば記載  
PodごとにVMが割り当てられるため、リソース消費やコスト増加に注意が必要です。

**詳細**:

Azure Kubernetes Service (AKS)におけるPodサンドボックス機能が一般提供(GA)となりました。本アップデートは、共有環境でのコンテナワークロード実行時に懸念されるセキュリティとワークロード分離の強化を目的としています。具体的には、各Podを専用の軽量仮想マシン（Pod VM）上で実行することで、ホストOSや他Podからの影響を最小化し、強固な分離を実現します。技術的には、Kata Containersなどの軽量仮想化技術を活用し、従来のコンテナランタイムに加えてPod単位の仮想化レイヤーを導入。これにより、カーネルレベルの分離を提供しつつ、パフォーマンスへの影響を抑制しています。活用シナリオとしては、マルチテナント環境や高セキュリティ要件のある金融・医療分野のワークロードに最適です。注意点としては、Pod VMの起動時間が通常のPodより長くなる点や、リソース消費が増加する可能性があるため、リソースプランニングが重要です。また、Azure MonitorやAzure Policyと連携し、監視・ガバナンスを強化可能です。既存のAKSクラスターに対してオプションで有効化でき、段階的な導入が可能です。詳細は公式ドキュメントを参照してください。

---

### 22. Generally Available: Managed namespaces on AKS 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Managed namespaces on AKS ](https://azure.microsoft.com/updates?id=526232)

**アップデートID**: 526232
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
AKSでManaged Namespaces機能が一般提供（GA）となりました。

- 主な変更点や新機能  
複数AKSクラスター間でのnamespace設定を自動管理でき、手動設定や誤設定のリスクを軽減します。

- 影響を受ける対象  
AKSを利用し、複数クラスターでnamespace管理を行う開発者・運用者。

- 注意点があれば記載  
既存の手動管理から移行する際は設定の整合性を確認してください。

**詳細**:

Azure Kubernetes Service (AKS)の「Managed Namespaces」機能がGA（一般提供）となりました。従来、複数AKSクラスター間でのnamespace設定は手動管理が必要で、設定ミスや運用負荷が課題でした。本機能はnamespaceの作成・管理をAKSが自動化し、一貫性のある設定を保証します。具体的には、namespaceのライフサイクル管理、RBAC設定、リソースクオータ適用を統合的に行い、複数クラスターでの環境標準化を実現します。技術的には、AKSコントロールプレーンがnamespace定義を管理し、API経由でクラスターに反映。TerraformやAzure CLIからの操作もサポートされます。活用例としては、マルチテナント環境での権限分離やリソース管理の効率化が挙げられ、DevOpsパイプラインへの組み込みも容易です。注意点としては、既存の手動設定との競合回避や、対応するAKSバージョンの確認が必要です。Azure PolicyやAzure Monitorと連携し、ガバナンス強化や監視の一元化も可能です。詳細は公式リンク参照。

---

### 23. Public Preview: Azure Kubernetes Fleet Manager for Arc-enabled clusters 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Kubernetes Fleet Manager for Arc-enabled clusters ](https://azure.microsoft.com/updates?id=526227)

**アップデートID**: 526227
**情報源**: Azure Updates API

**カテゴリ**: In preview, Containers, Compute, Azure Kubernetes Fleet Manager, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
Azure Kubernetes Fleet ManagerがAzure Arc対応Kubernetesクラスターをサポートし、パブリックプレビューを開始。

- 主な変更点や新機能  
ハイブリッド・マルチクラウド環境のCNCF準拠クラスターを一元管理可能に。複数環境の運用管理を簡素化。

- 影響を受ける対象  
Azure Arcで管理するKubernetesクラスターを運用する企業や技術者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は注意が必要。今後の正式リリースに注目。

**詳細**:

Azure Kubernetes Fleet ManagerのPublic Previewが開始され、Azure Arc対応のKubernetesクラスター管理が統合されました。背景には、ハイブリッドおよびマルチクラウド環境で分散・断片化しがちなKubernetesクラスターの一元管理ニーズがあります。本アップデートにより、CNCF準拠の任意のKubernetesクラスターをAzure Arc経由でFleet Managerに登録し、単一のポータルからポリシー適用、監視、アップデート管理が可能となります。技術的には、Azure Arcの拡張機能を用いてクラスターをAzureに接続し、Fleet ManagerがAPIベースでクラスター情報を集約、管理します。活用例としては、オンプレミスや他クラウドのKubernetesを含む大規模環境での統合運用やセキュリティポリシーの一括適用が挙げられます。注意点としては、現時点での対応KubernetesバージョンやArcエージェントのインストール要件、プレビュー段階のため機能制限や安定性に留意が必要です。Azure MonitorやAzure Policyとの連携により、監視・ガバナンス強化が可能で、Azure Arcの拡張性を活かした包括的なクラスタ管理基盤として活用できます。

---

### 24. Public Preview: Windows Server 2025 on AKS

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Windows Server 2025 on AKS](https://azure.microsoft.com/updates?id=526213)

**アップデートID**: 526213
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
AKSでWindows Server 2025のパブリックプレビューが開始されました。

- 主な変更点や新機能  
Windowsベースのワークロード向けに最新のWindows Server 2025をサポートし、モダナイゼーションとサポート終了対応を促進。

- 影響を受ける対象  
AKS上でWindowsコンテナを運用する企業や開発者。

- 注意点があれば記載  
プレビュー段階のため本番環境での利用は慎重に。既存のWindows Serverバージョンからの移行計画が必要です。

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）上でのWindowsベースワークロードの近代化を支援するため、Windows Server 2025のプレビュー対応を開始したものです。従来のWindows Serverバージョンのサポート終了に伴い、最新OSへの移行を円滑化し、セキュリティ強化やパフォーマンス向上を図ります。具体的には、AKSクラスター内でWindows Server 2025コンテナイメージを利用可能とし、Windowsコンテナの互換性と安定性を向上させました。実装面では、AKSのノードプールにWindows Server 2025を指定し、既存のLinuxノードと混在可能なハイブリッド環境を構築可能です。CI/CDパイプラインに組み込むことで、最新OSベースのアプリケーション展開が容易になります。活用例としては、レガシーWindowsアプリケーションのコンテナ化やマイクロサービス化が挙げられ、クラウドネイティブ化推進に寄与します。注意点としては、プレビュー段階のため一部APIや機能に制限があり、本番環境での利用は慎重に検討が必要です。また、Windows Server 2025対応のコンテナイメージはMicrosoft Container Registryから取得可能です。Azure MonitorやAzure Policyとの連携により、運用監視やガバナンスも強化できます。詳細は公式ドキュメントを参照してください。

---

### 25. Generally Available: AKS Automatic pod readiness SLA

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: AKS Automatic pod readiness SLA](https://azure.microsoft.com/updates?id=526208)

**アップデートID**: 526208
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
AKSのAutomaticクラスタに対して、ポッドのレディネスSLAが一般提供開始。

- 主な変更点や新機能  
対象ポッドが99.9パーセンタイルで5分以内にレディ状態になることを保証。

- 影響を受ける対象  
AKS Automaticクラスタを利用するユーザー、特にミッションクリティカルなワークロードを運用する技術者。

- 注意点があれば記載  
SLA適用対象は条件を満たすポッドに限定されるため、詳細は公式ドキュメントで確認が必要。

**詳細**:

本アップデートは、Azure Kubernetes Service (AKS) の自動クラスターに対し、ポッドの準備完了（readiness）に関するSLA（サービスレベルアグリーメント）を99.9パーセンタイルで5分以内に保証するものです。背景には、ミッションクリティカルなワークロードの安定稼働を支援し、運用信頼性を向上させる狙いがあります。具体的には、AKSの自動スケーリングやノード管理機能と連携し、対象ポッドがreadinessプローブの条件を満たすまでの時間を短縮・安定化します。技術的には、AKSのコントロールプレーンがポッドの状態監視を強化し、リソース割当やスケジューリングの最適化を行うことで実現しています。活用シナリオとしては、金融や医療など高可用性が求められるサービスのコンテナ化に適しており、デプロイ後のサービス開始遅延を抑制可能です。注意点としては、SLA対象は自動クラスターに限定され、readinessプローブの正確な設定が前提となる点が挙げられます。また、関連サービスとしてAzure MonitorやAzure Policyと連携し、ポッドの状態監視やコンプライアンス管理を強化できます。詳細は公式リンクを参照してください。

---

### 26. Public Preview: AKS Automatic managed system node pools

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: AKS Automatic managed system node pools](https://azure.microsoft.com/updates?id=526203)

**アップデートID**: 526203
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
AKSでシステムノードプールの自動管理機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
システムノードプールのスケーリング、パッチ適用、可用性維持を自動化し、運用負荷を軽減。

- 影響を受ける対象  
AKSクラスタの運用担当者やDevOpsエンジニア。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に検討が必要。  

情報源: https://azure.microsoft.com/updates?id=526203

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）におけるシステムノードプールのプロビジョニングと運用負荷を軽減するために導入された「Automatic managed system node pools」のパブリックプレビュー提供開始を示すものです。従来、システムノードプールはスケーリング、パッチ適用、可用性確保などの管理作業が手動で必要であり、これが運用コストやリソース分散の要因となっていました。本機能は、これらの運用作業を自動化し、AKSがシステムノードプールのライフサイクル管理を担うことで、運用負荷を大幅に削減します。

具体的には、AKSがシステムノードプールのスケールアウト・スケールイン、OSやKubernetesコンポーネントのパッチ適用、障害時の自動回復を自動的に実行します。ユーザーはノードプールの設定に集中でき、手動でのメンテナンス作業が不要となります。実装はAKSのコントロールプレーンが管理ノードとして機能し、Azure Resource Manager（ARM）を介してノードプールの状態を監視・制御します。

活用シナリオとしては、大規模なAKSクラスター運用での運用効率化や、DevOpsチームのリソースをアプリケーション開発に集中させたい場合に有効です。注意点としては、現時点ではパブリックプレビューであるため、商用環境での利用は慎重に検討し、最新のドキュメントや制限事項を確認する必要があります。また、カスタムノードプール設定や特殊な構成が自動管理に対応していない場合があります。

関連サービスとしては、Azure Monitorによるノードプールの状態監視、Azure Policyによるコンプライアンス管理、Azure DevOpsやGitHub Actionsと連携したCI/CDパイプラインの自動化が挙げられます。これにより、システムノードプールの運用自動化と継続的デリバリーがシームレスに統合可能です。

---

### 27. Public Preview: Add durability to AI agents in Azure Functions using Microsoft Agent Framework

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Add durability to AI agents in Azure Functions using Microsoft Agent Framework](https://azure.microsoft.com/updates?id=526179)

**アップデートID**: 526179
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Internet of Things, Azure Functions

**要約**:

- 何が更新されたか  
Microsoft Agent FrameworkとAzure FunctionsのDurable Extensionが統合され、AIエージェントの耐久性と信頼性が向上しました（パブリックプレビュー開始）。

- 主な変更点や新機能  
Durable Functionsのオーケストレーション機能を活用し、状態管理や再試行が可能な堅牢なAIエージェントを構築・ホスト可能に。

- 影響を受ける対象  
Azure上でAIエージェントを開発・運用する技術者や開発チーム。

- 注意点  
現段階はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

本アップデートは、Microsoft Agent FrameworkとAzure FunctionsのDurable Functions拡張機能を統合し、AIエージェントの耐久性と信頼性を向上させることを目的としています。これにより、状態管理や長時間実行が必要なAIエージェントをサーバーレス環境で安定的に運用可能です。具体的には、Microsoft Agent Frameworkの会話やタスク管理機能とDurable Functionsのオーケストレーション機能を組み合わせ、状態遷移や再試行、分散トランザクションを効率的に実装できます。実装はAzure Functions上にエージェントロジックを配置し、Durable Orchestratorでワークフローを制御する形で行います。活用例としては、カスタマーサポートチャットボットの長期対話管理や複雑な業務プロセス自動化が挙げられます。注意点として、Durable Functionsの実行時間制限やスケーリング特性を考慮し、適切なタイムアウト設定やエラーハンドリング設計が必要です。関連サービスとしてAzure Cognitive ServicesやAzure Bot Serviceとの連携が容易で、AI機能の拡張や多様なチャネルへの展開が可能です。詳細は公式ドキュメントと更新情報を参照してください。

---

### 28. Public Preview: Cross region pool association support for Azure Virtual Network Manager IP address management

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Cross region pool association support for Azure Virtual Network Manager IP address management](https://azure.microsoft.com/updates?id=526174)

**アップデートID**: 526174
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Azure Virtual Network Manager

**要約**:

- 何が更新されたか  
Azure Virtual Network ManagerのIPアドレス管理で、複数リージョンの仮想ネットワークに対し単一のIPAMプールを関連付ける機能がパブリックプレビューで提供開始。

- 主な変更点や新機能  
複数リージョン間でIPアドレス空間の一元管理が可能となり、CIDR割り当ての一貫性と管理の簡素化を実現。

- 影響を受ける対象  
複数リージョンにまたがる仮想ネットワークを管理するネットワーク管理者やインフラエンジニア。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での使用は慎重に行い、最新のドキュメントを参照すること。

**詳細**:

本アップデートは、複数リージョンにまたがるIPアドレス管理の複雑性とミスリスクを軽減する目的で提供される、Azure Virtual Network Manager（VNet Manager）のIPアドレス管理機能拡張です。従来はIPAMプールをリージョン単位で管理していたため、複数リージョンの仮想ネットワークに対して一貫したCIDR割り当てが困難でした。今回のパブリックプレビューでは、単一のIPAMプールを複数リージョンのVNetに関連付け可能となり、IPアドレス空間の統合管理とガバナンスが強化されます。

技術的には、Azure Virtual Network ManagerのIPAMプール設定に「クロスリージョンプールアソシエーション」機能が追加され、IPAMプールのスコープがリージョンを超えて拡張されます。これにより、複数リージョンのVNetに対して同一のIPAMプールからCIDRブロックを割り当て、重複や競合を防止できます。設定はAzureポータル、CLI、またはARMテンプレートを通じて行い、既存のIPAMポリシーと連携可能です。

活用例としては、グローバルに展開するマルチリージョン環境でのIPアドレス管理統一や、ハイブリッドクラウド環境における一貫したネットワーク設計が挙げられます。これにより、運用負荷の軽減とネットワーク設計の標準化が実現します。

注意点としては、本機能は現時点でパブリックプレビュー段階であり、商用環境での利用は慎重に検討する必要があります。また、IPAMプールのクロスリージョン関連付けは既存のリージョン限定設定との互換性に留意し、適切なテストを推奨します。

関連サービスとしては、Azure Virtual Network Manager自体の管理機能、Azure Resource Manager（ARM）によるポリシー管理、さらにAzure MonitorによるIPAMポリシー適用状況の監視と連携が可能です。これにより、包括的なネットワーク管理と運用自動化が促進されます。

---

### 29. Generally Available: Azure Virtual Network Manager address overlap prevention in mesh 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Virtual Network Manager address overlap prevention in mesh ](https://azure.microsoft.com/updates?id=526169)

**アップデートID**: 526169
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Azure Virtual Network Manager

**要約**:

- 何が更新されたか  
Azure Virtual Network Managerのメッシュ内アドレス空間重複防止機能が一般提供（GA）となりました。

- 主な変更点や新機能  
複数の仮想ネットワーク間でのIPアドレス重複を自動検出・防止し、トラフィックのドロップや通信障害を回避します。

- 影響を受ける対象  
マルチVNet環境でAzure Virtual Network Managerを利用するネットワーク管理者やインフラ技術者。

- 注意点  
既存のメッシュ構成で重複がある場合は事前に確認・調整が必要です。

**詳細**:

Azure Virtual Network Managerの「アドレス空間重複防止機能」がメッシュ環境で一般提供開始されました。本機能は複数の仮想ネットワーク（VNet）をメッシュ構成で管理する際に、アドレス空間の重複を自動検出・防止し、通信障害やトラフィックのドロップを未然に防ぐことを目的としています。具体的には、VNet間のIPアドレス範囲を比較し、重複がある場合は設定変更を促すアラートや適用ブロックを行います。実装はAzure Virtual Network Managerのポリシー管理機能に統合され、管理ポータルやCLIから一元的に設定可能です。活用シナリオとしては、大規模なマルチVNet環境でのネットワーク設計時に、誤って重複するアドレスを割り当てるリスクを低減し、運用の信頼性向上に寄与します。注意点としては、既存の重複がある場合は手動での修正が必要であり、オンプレや他クラウドとの接続時は別途IP管理が求められます。関連サービスとしては、Azure FirewallやAzure Route Serverとの連携でトラフィック制御を強化でき、Azure Monitorと組み合わせて重複検出のログ監視も可能です。

---

### 30. Public Preview: Azure Functions support for Node.js 24 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Functions support for Node.js 24 ](https://azure.microsoft.com/updates?id=526077)

**アップデートID**: 526077
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Internet of Things, Azure Functions

**要約**:

- 何が更新されたか  
Azure FunctionsがNode.js 24をパブリックプレビューでサポート開始。

- 主な変更点や新機能  
ローカル開発からWindows/LinuxのAzure Functionsへのデプロイが可能に。  

- 影響を受ける対象  
Node.js 24を利用する開発者およびAzure Functionsユーザー。  

- 注意点  
Node.js 24はWindowsの32ビット環境をサポートせず、新規Windows Function Appは64ビットがデフォルト。

**詳細**:

本アップデートは、Azure FunctionsがNode.jsの最新バージョン24をパブリックプレビューでサポート開始したことを示します。背景には、Node.jsの新機能やパフォーマンス改善を活用し、よりモダンなJavaScript/TypeScript開発環境を提供する狙いがあります。具体的には、ローカル環境でNode.js 24を用いた関数開発が可能となり、WindowsおよびLinuxのAzure Functions環境へデプロイ可能です。ただし、Node.js 24はWindowsの32ビットシステムをサポートしないため、新規Windows Function Appは64ビットがデフォルト設定となります。技術的には、Azure FunctionsランタイムがNode.js 24のランタイム環境を認識し、対応したホスティングスタックを提供する形で実装されています。活用例としては、最新のNode.js機能（例：ESMモジュール、最新のV8エンジン最適化）を利用したサーバーレスAPIやイベント駆動型処理の構築が挙げられます。注意点として、既存の32ビットWindows環境では動作しないため、移行計画が必要です。また、Node.js 24対応のAzure Functions Core Tools最新版の利用が推奨されます。関連サービスとしては、Azure DevOpsやGitHub Actionsと連携したCI/CDパイプライン構築時に、Node.js 24環境のビルド・デプロイ設定を更新する必要があります。詳細は公式リンクを参照してください。

---

### 31. Public Preview: Azure Functions support for Java 25 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Functions support for Java 25 ](https://azure.microsoft.com/updates?id=526072)

**アップデートID**: 526072
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Internet of Things, Azure Functions

**要約**:

- 何が更新されたか  
Azure FunctionsがJava 25をサポートするパブリックプレビューを開始。

- 主な変更点や新機能  
ローカル開発およびWindows/Linux環境へのデプロイが可能に。セキュリティ強化、サポート期間延長、Azure Functionsとの互換性維持。

- 影響を受ける対象  
JavaでAzure Functionsを開発・運用する技術者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討を。

**詳細**:

本アップデートにより、Azure FunctionsがJava 25のパブリックプレビュー対応を開始しました。これにより、開発者はローカル環境でJava 25を用いた関数開発が可能となり、WindowsおよびLinux上のAzure Functionsへデプロイできます。Java 25はセキュリティ強化や長期サポートが特徴で、最新のJDK機能を活用しつつAzure Functionsの互換性を維持します。実装面では、Azure Functions Core ToolsやMavenプラグインがJava 25をサポートし、既存のJava 17や11からのアップグレードがスムーズに行えます。典型的な活用例としては、高セキュリティ要件のAPIバックエンドやイベント駆動型処理のモダナイズが挙げられます。注意点としては、現時点で一部のサードパーティライブラリがJava 25に未対応の可能性や、プレビュー段階のため本番環境での利用は慎重を要します。Azure MonitorやApplication Insightsとの連携により、パフォーマンス監視やトラブルシューティングも容易です。今後の正式リリースに向けて、Java 25対応の関数開発環境を早期に整備することが推奨されます。

---

### 32. Generally Available: Application Gateway for Containers – Slow start

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Application Gateway for Containers – Slow start](https://azure.microsoft.com/updates?id=525893)

**アップデートID**: 525893
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
Application Gateway for Containersに「Slow start」機能が一般提供開始。

- 主な変更点や新機能  
バックエンドのスケールアップ時に、新規Podへのトラフィックを段階的に増加させ、安定性とパフォーマンスを向上。

- 影響を受ける対象  
Kubernetes環境でApplication Gatewayを利用し、スケールアップを行う技術者。

- 注意点があれば記載  
トラフィック増加の時間ウィンドウは設定可能で、適切な調整が必要。

**詳細**:

Azure Application Gateway for Containersにおいて、ロードバランシングアルゴリズム「Slow start」が一般提供（GA）されました。本機能は、バックエンドのスケールアップ時に新規Podへのトラフィックを段階的に増加させることで、急激な負荷集中を防ぎ、サービスの安定性とパフォーマンスを向上させることを目的としています。具体的には、設定可能な時間ウィンドウ内で新規Podに対するリクエスト数を徐々に増やし、初期の過負荷やエラー発生リスクを低減します。実装はApplication Gatewayのロードバランサーに組み込まれ、Kubernetes環境下でのコンテナスケールアップと連動して動作します。活用シナリオとしては、マイクロサービスの自動スケーリング時に新規インスタンスの安定稼働を確保したいケースが挙げられます。注意点として、slow startの時間設定は適切に調整する必要があり、過度に長い設定はレスポンス遅延を招く可能性があります。また、Application GatewayはAzure Kubernetes Service（AKS）や他のコンテナオーケストレーション環境と連携し、Ingressコントローラーとして機能するため、これらの環境での運用に最適化されています。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 33. Public Preview: Application Gateway for Containers Istio Service Mesh integration

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Application Gateway for Containers Istio Service Mesh integration](https://azure.microsoft.com/updates?id=525874)

**アップデートID**: 525874
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
Application Gateway for ContainersがIstioサービスメッシュとの統合をパブリックプレビューで提供開始。

- 主な変更点や新機能  
サービスメッシュ拡張機能により、外部クライアントとIstio内サービス間のセキュアなノースサウス通信が簡素化。

- 影響を受ける対象  
Istioサービスメッシュを利用するコンテナ環境のアプリケーション開発者や運用者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討する必要あり。

**詳細**:

本アップデートは、Azure Application Gateway for ContainersがIstioサービスメッシュと統合可能となるパブリックプレビューの提供開始を示す。背景には、マイクロサービス環境での北南方向（外部クライアント⇔サービスメッシュ内サービス）通信のセキュリティ強化と運用簡素化のニーズがある。新機能として、Application Gatewayにサービスメッシュ拡張機能が追加され、IstioのEnvoyプロキシと連携しTLS終端やルーティングを一元管理可能。これにより、外部トラフィックを安全かつ効率的にメッシュ内サービスへ誘導できる。実装は、Azure PortalまたはCLIから拡張機能を有効化し、Istioのゲートウェイリソースと連携設定を行う形で行う。活用例は、Kubernetes上のIstioメッシュ環境で外部API公開やトラフィック制御を行うケース。注意点としては、現時点でプレビュー機能のため、商用環境での利用は慎重に検討すること、及びIstioのバージョン互換性を確認する必要がある。関連サービスとしては、Azure Kubernetes Service（AKS）との連携が想定され、Application GatewayのWAF機能と組み合わせることでセキュリティ強化が可能である。詳細は公式ドキュメント参照推奨。

---

### 34. Public Preview: Azure DocumentDB high-performance storage 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure DocumentDB high-performance storage ](https://azure.microsoft.com/updates?id=525549)

**アップデートID**: 525549
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure DocumentDBで高性能ストレージがパブリックプレビューとして提供開始。

- 主な変更点や新機能  
物理シャードあたり最大64TiB容量、80,000 IOPS、1,200MB/sスループットを実現し、より大規模かつ高速なワークロードを少ないノードで処理可能に。

- 影響を受ける対象  
Azure DocumentDBを利用する開発者・運用者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討が必要。  

情報源: https://azure.microsoft.com/updates?id=525549

**詳細**:

本アップデートは、Azure DocumentDB（現Azure Cosmos DBの旧称）におけるストレージ性能向上を目的とし、大規模かつ高負荷なワークロードをより少ないノードで効率的に処理可能にします。具体的には、物理シャード（ノード）あたり最大64TiBのストレージ容量、80,000 IOPS、1,200MB/sのスループットを実現。これにより、従来の制約を超えた大容量データの高速読み書きが可能となります。技術的には、高性能ストレージ層の導入とI/Oパスの最適化により、物理シャード単位でのI/O性能を大幅に強化。シャードのスケーリングやパーティショニング戦略の見直しも推奨されます。活用シナリオとしては、大規模なリアルタイム分析、IoTデータの高速集約、グローバル分散アプリケーションのレスポンス改善などが挙げられます。注意点としては、現時点でプレビュー段階のため、リージョン対応状況やサポート範囲に制限があること、既存のアプリケーションとの互換性検証が必要です。Azure FunctionsやAzure Synapse Analyticsとの連携により、データ処理の自動化や分析基盤の強化が可能であり、全体的なエコシステム内でのパフォーマンス向上に寄与します。

---

### 35. Generally Available: Model Context Protocol (MCP) tool trigger for Azure Functions 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Model Context Protocol (MCP) tool trigger for Azure Functions ](https://azure.microsoft.com/updates?id=525523)

**アップデートID**: 525523
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Internet of Things, Azure Functions

**要約**:

- 何が更新されたか  
Model Context Protocol（MCP）のAzure Functions用ツールトリガーが一般提供（GA）となりました。

- 主な変更点や新機能  
MCPを利用し、Azure FunctionsをAIエージェントのツールとして連携可能に。これにより、大規模言語モデルが関数を呼び出してタスクを実行できます。

- 影響を受ける対象  
Azure Functionsを活用したAI統合や自動化を行う開発者・技術者。

- 注意点があれば記載  
MCPの仕様理解とAzure Functionsの適切な設計が必要です。セキュリティ設定も考慮してください。

**詳細**:

Azureの新機能「Model Context Protocol（MCP）ツールトリガー for Azure Functions」が一般提供開始されました。MCPは大規模言語モデル（LLM）に対し、アプリケーションの機能やコンテキストを提供するプロトコルで、AIエージェントがタスク遂行に必要な外部ツールを呼び出せる点が特徴です。本アップデートでは、Azure FunctionsをMCPツールとして直接トリガー可能となり、LLMからのリクエストに応じてサーバーレス関数を柔軟に実行できます。技術的には、MCPサーバーがAzure FunctionsのHTTPエンドポイントを認識し、JSONベースの入力を受け取り処理結果を返す仕組みです。これにより、カスタムロジックや外部API連携を容易に組み込み、LLMの応答を動的に拡張可能です。活用例としては、チャットボットがユーザー問い合わせに応じて在庫確認や注文処理をAzure Functions経由で実行するケースが挙げられます。注意点として、関数の応答時間やスケーリング設定がLLMのリアルタイム性に影響するため、適切なパフォーマンスチューニングが必要です。また、認証・認可の設定を厳格に管理し、不正アクセスを防止することが推奨されます。Azure OpenAI ServiceやAzure API Managementとの連携により、MCPツールトリガーの運用管理やセキュリティ強化が可能です。今回のアップデートにより、LLMとAzure Functionsの統合が進み、より高度で柔軟なAI駆動アプリケーションの構築が実現します。

---

### 36. Generally Available: Azure Functions durable task scheduler Dedicated SKU (GA) & Consumption SKU (Public Preview)

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Functions durable task scheduler Dedicated SKU (GA) & Consumption SKU (Public Preview)](https://azure.microsoft.com/updates?id=525518)

**アップデートID**: 525518
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Internet of Things, Azure Functions

**要約**:

- 何が更新されたか  
Azure Functions Durable Task SchedulerのDedicated SKUがGA（一般提供）となり、Consumption SKUがパブリックプレビューで利用可能に。

- 主な変更点や新機能  
複雑なワークフローのオーケストレーションを自動チェックポイントで耐障害性を強化。Dedicated SKUは安定稼働向け、Consumption SKUはスケーラブルな従量課金モデルを提供。

- 影響を受ける対象  
Azure Functionsで耐久性の高いワークフローを構築する開発者・運用者。

- 注意点  
Consumption SKUは現時点でプレビューのため、本番環境での利用は慎重に。

**詳細**:

本アップデートは、Azure FunctionsのDurable Task SchedulerがDedicated SKUで一般提供（GA）され、Consumption SKUがパブリックプレビューとなったことを示します。Durable Task Schedulerは複雑なワークフローやインテリジェントエージェント向けのオーケストレーションエンジンで、自動的に進捗をチェックポイントし、オーケストレーション状態を保護することで高い耐障害性を実現します。Dedicated SKUは専用リソース上で安定したパフォーマンスを提供し、大規模・長時間実行のタスクに適しています。一方、Consumption SKUはイベント駆動型でコスト効率が高く、スケールアウトが容易ですが、プレビュー段階のため一部機能制限があります。実装はAzure FunctionsのDurable Functions拡張機能を利用し、状態管理はAzure Storageに保持されます。典型的な活用例としては、複雑なビジネスプロセス自動化、長時間実行のバッチ処理、IoTデバイスの状態管理などが挙げられます。注意点としては、Consumption SKUのプレビュー版ではSLAsが未提供であり、専用環境が必要な場合はDedicated SKUを選択すべきです。Azure Logic AppsやEvent Gridとの連携により、トリガーや通知機能を強化可能で、Azure Monitorでオーケストレーションの監視・診断が行えます。

---

### 37. Public Preview: Self-hosted remote MCP servers on Azure Functions 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Self-hosted remote MCP servers on Azure Functions ](https://azure.microsoft.com/updates?id=525505)

**アップデートID**: 525505
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Internet of Things, Azure Functions

**要約**:

- 何が更新されたか  
Azure Functions上で自己ホスト型のリモートModel Context Protocol（MCP）サーバーを構築・運用可能なパブリックプレビューを開始。

- 主な変更点や新機能  
MCP SDKを用いたサーバーをFunctionsでホスティングでき、サーバー認証の組み込みや自動スケーリングが利用可能に。

- 影響を受ける対象  
MCPプロトコルを利用する開発者やシステム運用者。

- 注意点  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討が必要。  

情報源: https://azure.microsoft.com/updates?id=525505

**詳細**:

本アップデートは、Model Context Protocol（MCP）SDKで構築したリモートMCPサーバーをAzure Functions上でセルフホスト可能にするパブリックプレビュー機能の提供開始を示す。背景には、MCPサーバーのスケーラビリティ向上と運用負荷軽減のニーズがあり、Azure Functionsのサーバーレス環境を活用することで、インフラ管理不要かつ自動スケーリングを実現することが目的。主な機能としては、Functionsプラットフォームによる組み込みのサーバー認証、イベント駆動型の自動起動・停止、MCP通信の効率化が挙げられる。実装は、MCP SDKで作成したサーバーコードをAzure FunctionsのHTTPトリガーやタイマートリガーにデプロイし、Function Appとして管理する形を取る。これにより、リモートMCPサーバーを柔軟かつコスト効率良く運用可能となる。活用シナリオとしては、分散型AIモデル管理や複数環境でのモデルコンテキスト同期、オンデマンドでのモデル更新通知などが想定される。注意点としては、Functionsの実行時間制限やコールドスタートによる遅延、プレビュー段階のAPI安定性に留意が必要。Azure Key VaultやAzure ADとの連携により認証・認可を強化でき、Azure Monitorでログ監視やパフォーマンス分析も可能。これにより、MCPサーバーの運用効率とセキュリティを高めつつ、サーバーレスの利便性を享受できる。

---

### 38. Announcing: Resources for migrating to Azure Functions Flex Consumption 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Announcing: Resources for migrating to Azure Functions Flex Consumption ](https://azure.microsoft.com/updates?id=525500)

**アップデートID**: 525500
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Internet of Things, Azure Functions

**要約**:

- 何が更新されたか  
Azure Functions Flex Consumptionへの移行支援リソースが公開されました。

- 主な変更点や新機能  
Flex Consumptionプランは高度なスケーリング、ネットワーク機能、コスト最適化を提供し、従来のConsumptionプランやAWS Lambdaからの移行をサポートします。

- 影響を受ける対象  
Azure FunctionsのConsumptionプラン利用者およびAWS Lambdaからの移行を検討している技術者。

- 注意点があれば記載  
移行時は新プランのスケーリング特性やネットワーク設定を理解し、適切に設計する必要があります。

**詳細**:

本アップデートは、Azure Functions Flex Consumptionプランをサーバーレス環境における高度なスケーリング、ネットワーク構成、コスト最適化を必要とするワークロード向けの推奨ホスティングプランとして位置付けることを目的としています。従来のConsumptionプランやAWS Lambdaからの移行を支援するため、移行リソースやガイドが提供されます。Flex Consumptionは、より柔軟なスケーリング（秒単位のスケールアウト・イン）、VNet統合によるセキュアなネットワーク接続、カスタムドメインや専用IPの利用が可能であり、複雑なエンタープライズ要件に対応します。実装はAzure Functionsのホスティングプラン選択時にFlex Consumptionを指定し、必要に応じてVNet設定やストレージアカウントの構成を行います。典型的な活用例としては、大量イベント処理や複数サービス間の安全な通信が求められるマイクロサービスアーキテクチャ、AWS Lambdaからの移行によるコスト削減とパフォーマンス向上が挙げられます。注意点として、Flex Consumptionは従来のConsumptionプランに比べて起動時間が若干長くなる場合があり、また一部のリージョンでの提供状況を確認する必要があります。関連サービスとしてAzure Monitorによる詳細なパフォーマンス監視、Azure Virtual Networkとの連携、Azure API Managementを介したAPI管理が効果的です。詳細は公式移行ガイド（https://azure.microsoft.com/updates?id=525500）を参照してください。

---

### 39. Generally Available: Azure Functions enables OpenTelemetry support 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Functions enables OpenTelemetry support ](https://azure.microsoft.com/updates?id=525479)

**アップデートID**: 525479
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Internet of Things, Azure Functions

**要約**:

- 何が更新されたか  
Azure FunctionsがOpenTelemetryのサポートを一般提供（GA）開始。

- 主な変更点や新機能  
ログ、トレース、メトリクスをOpenTelemetry標準でエクスポート可能に。プレビュー版から安定した本番対応の可観測性を実現。

- 影響を受ける対象  
Azure Functionsを利用する開発者や運用チーム。

- 注意点があれば記載  
既存のOpenTelemetryツールとの連携が容易になるが、設定やバージョン互換性に注意が必要。

**詳細**:

Azure FunctionsがOpenTelemetryの一般提供(GA)を開始しました。これにより、開発者はオープンスタンダードに準拠したログ、トレース、メトリクスの収集とエクスポートが可能となり、従来のプレビュー版から安定した本番環境対応の観測性を実現します。具体的には、Azure FunctionsのランタイムにOpenTelemetry SDKが統合され、トレースデータやメトリクスをAzure Monitorや他の互換性のあるバックエンドへ送信可能です。実装は、関数アプリの設定でOpenTelemetryエクスポーターを有効化し、環境変数やコードレベルでカスタマイズが可能です。活用例としては、分散トレーシングによる関数間の呼び出し遅延分析や、メトリクスによるパフォーマンス監視が挙げられます。注意点として、現時点でサポートされる言語やランタイムバージョンに制限があり、カスタムエクスポーター利用時は追加設定が必要です。Azure MonitorやApplication Insightsとの連携により、統合的な監視・分析環境を構築でき、運用効率の向上に寄与します。

---

### 40. Public Preview: Azure Container Apps adds support for agentic Docker Compose 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Container Apps adds support for agentic Docker Compose ](https://azure.microsoft.com/updates?id=525470)

**アップデートID**: 525470
**情報源**: Azure Updates API

**カテゴリ**: In preview, Containers, Azure Container Apps

**要約**:

- 何が更新されたか  
Azure Container AppsがDocker Composeのエージェント機能をパブリックプレビューでサポート開始。

- 主な変更点や新機能  
開発者はDocker Composeファイルを使い、複数コンテナのアプリケーションをAzure Container Apps上で直接定義・デプロイ可能に。

- 影響を受ける対象  
マルチコンテナ構成をAzure Container Appsで管理・運用する開発者やDevOpsエンジニア。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討が必要。今後の正式リリースに注目。

**詳細**:

本アップデートは、Azure Container AppsがDocker Composeのサポートをパブリックプレビューで開始したものです。背景には、開発者がローカル環境で馴染み深いDocker Composeを用いて複数コンテナの定義・管理を行うワークフローを、そのままAzure上でシームレスに展開可能にする狙いがあります。具体的には、docker-compose.ymlファイルを直接Azure Container Appsにデプロイでき、複雑なマルチコンテナアプリケーションの構成を簡素化。内部的には、Composeファイルのサービス定義をAzure Container Appsのリソースにマッピングし、必要なスケーリングやネットワーク設定を自動的に適用します。活用例としては、マイクロサービス構成の開発・テスト環境の迅速構築や、既存Composeベースのアプリケーションのクラウド移行が挙げられます。注意点としては、Composeファイルの一部機能（例：特定のボリュームマウントやネットワークモード）が未対応のため、事前に対応可否を確認する必要があります。また、Azure MonitorやAzure Log Analyticsと連携し、コンテナのパフォーマンス監視やログ収集が可能です。本機能により、開発者はローカルとクラウド環境間で一貫したマルチコンテナ運用を実現し、デプロイ効率と運用の一元化が促進されます。

---

### 41. Public Preview: Azure Container Apps introduces flexible workload profile 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Container Apps introduces flexible workload profile ](https://azure.microsoft.com/updates?id=525465)

**アップデートID**: 525465
**情報源**: Azure Updates API

**カテゴリ**: In preview, Containers, Azure Container Apps

**要約**:

- 何が更新されたか  
Azure Container Appsに「Flexible workload profile」がパブリックプレビューで追加されました。

- 主な変更点や新機能  
従来の消費モデルの手軽さと専用プロファイルの性能・制御性を融合。サーバーレスの使った分だけ課金されるモデルを維持しつつ、柔軟なリソース割当が可能です。

- 影響を受ける対象  
Azure Container Appsを利用する開発者や運用者で、性能とコストのバランスを最適化したい技術者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure Container Appsに新たに導入されたFlexible Workload Profileは、従来の消費モデルのシンプルさと専用ワークロードプロファイルの高性能・制御性を融合させた新オプションです。これにより、サーバーレスの使いやすい課金体系を維持しつつ、CPUやメモリの割り当てをより柔軟に調整可能となり、パフォーマンス要件に応じた最適化が可能です。実装面では、従来のコンテナアプリ設定に加え、ワークロードプロファイルの種類として「Flexible」を指定し、リソース上限やスケール設定を細かく制御します。これにより、バースト負荷や長時間稼働するバックグラウンド処理など多様なユースケースに対応可能です。注意点としては、Flexibleプロファイルはプレビュー段階のため、リージョンや機能に制限があるほか、従来の専用プロファイルに比べてコスト構造が異なるため、運用コストの見積もりが必要です。Azure MonitorやLog Analyticsとの連携により、リソース使用状況の詳細な監視・分析が可能で、Azure DevOpsやGitHub Actionsを用いたCI/CDパイプライン構築も容易です。総じて、Flexible Workload Profileは多様な負荷特性を持つコンテナアプリケーションの運用効率化とコスト最適化を実現する重要なアップデートです。

---

### 42. Generally Available: Azure Container Apps serverless GPUs in additional regions 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Container Apps serverless GPUs in additional regions ](https://azure.microsoft.com/updates?id=525460)

**アップデートID**: 525460
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Container Apps

**要約**:

- 何が更新されたか  
Azure Container AppsのサーバーレスGPU機能が追加リージョンで一般提供（GA）開始。

- 主な変更点や新機能  
AI推論やモデル学習、GPUアクセラレーションが可能なサーバーレス環境をより多くの地域で利用可能に。

- 影響を受ける対象  
GPUを活用したコンテナアプリケーション開発者やAI/機械学習エンジニア。

- 注意点があれば記載  
利用可能リージョンの拡大に伴い、リージョンごとのリソース制限や価格を確認する必要あり。

**詳細**:

本アップデートは、GPUを活用したワークロードの需要増加に対応し、Azure Container AppsのサーバーレスGPU機能を追加リージョンで一般提供（GA）したものです。これにより、開発者はAI推論、機械学習モデルのトレーニング、GPUアクセラレーションが必要な処理を、サーバーレスの利便性を維持しつつ実行可能となります。技術的には、コンテナ単位でGPUリソースを割り当て、スケーラブルかつイベント駆動型でGPU搭載環境を動的に管理します。利用者はAzure CLIやARMテンプレートでGPUリソースを指定し、従量課金制でコスト効率良く運用可能です。主な活用例は、リアルタイムAI推論サービス、画像・動画処理、深層学習モデルの分散トレーニングなどです。制限としては、GPU搭載リージョンの限定や対応GPU種類の制約、起動時間の若干の遅延が挙げられます。Azure Machine LearningやAzure Kubernetes Service（AKS）と組み合わせることで、より高度なAIパイプラインやハイブリッドクラウド環境の構築が可能です。詳細は公式ドキュメントを参照してください。

---

### 43. Public Preview: Confidential computing in Azure Container Apps

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Confidential computing in Azure Container Apps](https://azure.microsoft.com/updates?id=525455)

**アップデートID**: 525455
**情報源**: Azure Updates API

**カテゴリ**: In preview, Containers, Azure Container Apps

**要約**:

- 何が更新されたか  
Azure Container Appsで機密コンピューティングがパブリックプレビューとして提供開始。

- 主な変更点や新機能  
ハードウェアベースのTrusted Execution Environments（TEE）により、コンテナ内のワークロードを安全に実行可能。データの暗号化に加え、実行時の保護が強化。

- 影響を受ける対象  
Azure Container Appsを利用する開発者や運用者で、機密性の高い処理をコンテナ化したい技術者。

- 注意点  
プレビュー版のため、本番環境での使用は慎重に。対応するハードウェアやリージョン制限がある可能性あり。

**詳細**:

Azure Container AppsにおけるConfidential Computingのパブリックプレビューが開始されました。本アップデートは、コンテナ化されたワークロードに対してハードウェアベースのTrusted Execution Environments（TEE）を提供し、データの機密性と処理中の安全性を強化することを目的としています。従来のAzureはデータの保存時および転送時の暗号化を提供していましたが、本機能により実行中のデータも保護可能となります。具体的には、Intel SGXやAMD SEVなどのTEE技術を活用し、コンテナ内のコードとデータをハードウェアレベルで隔離・暗号化します。実装はAzure Container Appsの設定でConfidential Computingオプションを有効化する形で行い、既存のCI/CDパイプラインに組み込みやすい設計です。活用シナリオとしては、金融・医療分野の機密データ処理や、マルチテナント環境でのデータ分離強化が挙げられます。一方、現時点では対応リージョンやインスタンスタイプに制限があり、パフォーマンスオーバーヘッドも考慮が必要です。Azure Key Vaultとの連携により、機密情報の安全な管理とTEE内での利用が可能であり、Azure Monitorでの監視もサポートされています。これにより、セキュリティ要件の高いコンテナアプリケーションの開発・運用が容易になります。

---

### 44. Public Preview: Standard V2 NAT Gateway and StandardV2 Public IPs

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Standard V2 NAT Gateway and StandardV2 Public IPs](https://azure.microsoft.com/updates?id=525405)

**アップデートID**: 525405
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Azure NAT Gateway

**要約**:

- 何が更新されたか  
Standard V2 NAT GatewayおよびStandard V2 Public IPがパブリックプレビューで提供開始。

- 主な変更点や新機能  
ゾーン冗長対応による高可用性の強化、スケーラビリティと耐障害性の向上、アウトバウンド接続の信頼性向上。

- 影響を受ける対象  
Azureで大規模かつ高可用なアウトバウンド接続を必要とするネットワーク設計者や運用者。

- 注意点があれば記載  
パブリックプレビューのため本番環境での利用は慎重に。リージョンによってゾーン冗長対応状況が異なる。

**詳細**:

AzureはStandardV2 SKUのNAT GatewayとStandardV2 Public IPをパブリックプレビューとして提供開始しました。本アップデートは、スケーラブルかつ高可用性を実現するアウトバウンド接続の強化を目的としています。主な新機能はゾーン冗長対応で、可用性ゾーン対応リージョンにおいて障害耐性を向上させ、単一障害点を排除します。StandardV2 NAT Gatewayは従来よりも大幅にスループットが向上し、接続数の上限も増加。パフォーマンスの最適化により、大規模環境での安定したアウトバウンド通信が可能です。実装は既存の仮想ネットワークに対し、StandardV2 NAT Gatewayをアタッチし、StandardV2 Public IPを割り当てる形で行います。活用シナリオとしては、大規模なマイクロサービス構成や、ゾーン冗長性が求められるミッションクリティカルなアプリケーションのアウトバウンド通信に適しています。注意点としては、現時点で一部リージョンでのみゾーン冗長が利用可能であること、また旧Standard SKUとの互換性に制限があるため移行計画が必要です。関連サービスとしては、Azure Load BalancerやAzure Firewallとの組み合わせでネットワークの冗長性とセキュリティを強化可能です。詳細は公式ドキュメントとプレビューの利用条件を参照してください。

---

### 45. Generally Available: SQL database in Microsoft Fabric

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: SQL database in Microsoft Fabric](https://azure.microsoft.com/updates?id=525388)

**アップデートID**: 525388
**情報源**: Azure Updates API

**カテゴリ**: Launched, Analytics, Microsoft Fabric

**要約**:

- 何が更新されたか  
Microsoft Fabric上のSQL DatabaseがGA（一般提供）開始。

- 主な変更点や新機能  
SQL ServerおよびAzure SQL Databaseエンジンを基盤とし、完全SaaSネイティブで運用・分析ワークロードを高速かつ安全に統合可能。

- 影響を受ける対象  
Azure上でデータ統合や分析基盤を構築する開発者・データエンジニア。

- 注意点があれば記載  
既存のSQL Databaseとの互換性や移行計画を検討する必要がある。

**詳細**:

Microsoft FabricにおけるSQL Databaseの一般提供（GA）が開始されました。本サービスはSQL ServerおよびAzure SQL Databaseの信頼性の高いエンジンを基盤とし、完全なSaaSネイティブ環境で提供されます。これにより、運用系と分析系のワークロードを単一プラットフォーム上で高速かつ安全に統合可能です。具体的には、トランザクション処理と分析処理を同一SQLエンジンで実行でき、データの一貫性を保ちながらリアルタイム分析が可能となります。実装はMicrosoft Fabricの統合環境内で行い、スケーラブルなクラウドリソースを活用しつつ、従来のSQLクエリやツールがそのまま利用可能です。活用例としては、IoTデバイスからの大量データのリアルタイム処理や、BIツールとの連携による即時レポーティングが挙げられます。制限事項としては、Fabric環境固有のリソース制約や、既存Azure SQL Databaseとの一部機能差異に注意が必要です。Azure Synapse AnalyticsやPower BIとのシームレスな連携により、エンドツーエンドのデータ分析基盤構築が容易になります。詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=525388）を参照してください。

---

### 46. Public Preview: Support for Italian and Portuguese in Azure Cosmos DB for NoSQL full-text search 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Support for Italian and Portuguese in Azure Cosmos DB for NoSQL full-text search ](https://azure.microsoft.com/updates?id=523824)

**アップデートID**: 523824
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DB for NoSQLの全文検索機能で、イタリア語とポルトガル語のサポートがパブリックプレビューとして追加されました。

- 主な変更点や新機能  
これにより、イタリア語・ポルトガル語の言語特性を考慮したインデックス作成や検索が可能となり、多言語対応の検索体験が強化されます。

- 影響を受ける対象  
多言語対応の全文検索を利用する開発者やアプリケーションが恩恵を受けます。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。  

情報源: https://azure.microsoft.com/updates?id=523824

**詳細**:

本アップデートにより、Azure Cosmos DB for NoSQLの全文検索機能がイタリア語およびポルトガル語をサポートするパブリックプレビュー版として提供開始されました。これにより、言語特有の形態素解析やステミング、ストップワード処理が可能となり、これら言語に最適化された検索体験を実現します。実装はAzure Cosmos DBの全文検索インデックス設定において、言語パラメータを「it」または「pt」に指定することで有効化され、既存のJSONドキュメント構造に対して自然言語検索が適用可能です。活用シナリオとしては、イタリア語・ポルトガル語のコンテンツを含む多言語対応アプリケーションや、地域特化型のカスタマーサポートシステムでの高度な検索機能強化が挙げられます。注意点としては、現段階がパブリックプレビューであるため、SLA保証や一部機能の制限が存在し、商用環境での利用は慎重に検討する必要があります。Azure Cognitive Searchとの連携により、さらに高度な検索機能やAIベースのテキスト分析を組み合わせることも可能です。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 47. Public Preview: Azure Cosmos DB MCP ToolKit for Microsoft Foundry Agent Service 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Cosmos DB MCP ToolKit for Microsoft Foundry Agent Service ](https://azure.microsoft.com/updates?id=523814)

**アップデートID**: 523814
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DB for NoSQL向けに、Microsoft Foundry Agent Serviceと連携可能なMCP Toolkitがパブリックプレビューで提供開始。

- 主な変更点や新機能  
Microsoft Foundry Agentを通じて、Cosmos DBのデータへ直接接続・操作が可能に。データ統合やリアルタイム処理が容易になる。

- 影響を受ける対象  
Azure Cosmos DBを利用し、Microsoft Foundry Agent Serviceを活用する開発者や運用担当者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に。今後のアップデートに注意が必要。

**詳細**:

本アップデートは、Azure Cosmos DB for NoSQLにMicrosoft Foundry Agent Service向けのMCP（Microsoft Connected Platform）Toolkitをパブリックプレビューとして提供開始したものです。背景には、IoTやエッジデバイスからのデータ収集とリアルタイム分析をシームレスに統合し、迅速な意思決定を支援する狙いがあります。MCP ToolkitはMicrosoft Foundry Agentと直接連携し、Cosmos DBのデータをエージェント経由で効率的に取得・送信可能にします。技術的には、Foundry AgentがCosmos DBのAPIに接続し、データの読み書きを行うためのSDKや認証機構を備え、低レイテンシかつスケーラブルなデータフローを実現。活用例としては、製造業の現場でエッジデバイスが収集したセンサーデータをCosmos DBに格納し、Foundry Agentがリアルタイムで分析・モニタリングするケースが挙げられます。注意点としては、現段階がパブリックプレビューであるため、機能の安定性やサポート範囲に制限がある点、また認証設定やネットワーク構成に注意が必要です。Azure IoT HubやAzure Synapse Analyticsなどと組み合わせることで、より高度なデータパイプラインや分析基盤の構築が可能です。詳細は公式ドキュメントを参照してください。

---

### 48. Generally Available: Fuzzy search in Azure Cosmos DB for NoSQL full-text search 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Fuzzy search in Azure Cosmos DB for NoSQL full-text search ](https://azure.microsoft.com/updates?id=523809)

**アップデートID**: 523809
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DB for NoSQLの全文検索機能にファジー検索がGAで対応。

- 主な変更点や新機能  
タイプミスや誤入力を許容するファジー検索により、より柔軟で誤りに強い検索体験を提供可能に。

- 影響を受ける対象  
Cosmos DBの全文検索を利用する開発者やアプリケーション。

- 注意点があれば記載  
ファジー検索の利用により検索結果の精度やパフォーマンスに影響が出る可能性があるため、適切な設定が必要。

**詳細**:

Azure Cosmos DB for NoSQLの全文検索機能において、誤字やタイプミスを許容する「ファジー検索」がGA（一般提供）されました。これにより、ユーザーの検索クエリに誤字や入力ミスがあっても、関連性の高い結果を返すことが可能となり、検索体験の向上を目的としています。ファジー検索はLevenshtein距離に基づき、指定した許容誤差範囲内での文字列マッチングを実現します。実装はAzure Cosmos DBのSQL APIの全文検索クエリに`FUZZY`オプションを追加する形で行い、既存のインデックス構造を活用しつつパフォーマンスを最適化しています。具体的には、`CONTAINS`関数に`FUZZY`パラメータを付与して利用可能です。活用例としては、ECサイトの商品検索やFAQシステムでのユーザー入力の誤りを吸収し、正確な情報提供を支援します。注意点として、ファジー検索は誤差許容度を高く設定すると検索結果が過剰に広がる可能性があり、パフォーマンスへの影響も考慮が必要です。また、全文検索はAzure Cognitive Searchとの連携も可能で、より高度な検索機能やAI解析と組み合わせることで柔軟な検索体験を構築できます。詳細は公式ドキュメントを参照してください。

---

### 49. Generally Available: Vector indexing performance improvements in Azure Cosmos DB for NoSQL 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Vector indexing performance improvements in Azure Cosmos DB for NoSQL ](https://azure.microsoft.com/updates?id=523803)

**アップデートID**: 523803
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DB for NoSQLのベクトルインデックス性能がGA（一般提供）となり、挿入とインデックス構築が高速化。

- 主な変更点や新機能  
アルゴリズム改善により、大規模AIワークロードのデータ取り込みおよびインデックス作成時間を短縮。

- 影響を受ける対象  
ベクトル検索や類似度検索を利用するAI/機械学習アプリケーション開発者。

- 注意点があれば記載  
既存のAPIは変わらず、性能向上のみのため互換性問題はなし。大規模データ処理で効果が顕著。

**詳細**:

本アップデートは、Azure Cosmos DB for NoSQLにおけるベクトルインデックスの性能向上を目的としています。大規模AIワークロードでのデータ取り込みおよびインデックス構築時間を短縮するため、ベクトルインデックスのアルゴリズムを最適化しました。具体的には、ベクトルデータの挿入処理とインデックスビルドの高速化を実現し、リアルタイム性が求められる機械学習や類似検索のパフォーマンスを改善しています。技術的には、近似最近傍探索（ANN）アルゴリズムの改良により、インデックス構造の効率化と計算負荷の低減を図っています。活用例としては、画像認識や自然言語処理で生成される高次元ベクトルの高速検索や、AIモデルの推論結果を即時に反映させるシナリオが挙げられます。注意点としては、既存のベクトルインデックスとの互換性や、インデックス更新時の一時的なパフォーマンス変動に留意が必要です。Azure Cognitive ServicesやAzure Machine Learningと連携することで、AIパイプライン全体の効率化が期待できます。詳細は公式ドキュメントを参照してください。

---

### 50. Generally Available: Float16 data type for vector indexes in Azure Cosmos DB 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Float16 data type for vector indexes in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=523796)

**アップデートID**: 523796
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DBのベクターインデックスでfloat16データ型がGA（一般提供）となりました。

- 主な変更点や新機能  
半精度浮動小数点（float16）を使うことで、float32に比べてストレージ使用量を半減可能。高い検索精度を維持しつつ、効率的なベクター検索が可能です。

- 影響を受ける対象  
ベクター検索を利用する開発者やデータベース管理者。

- 注意点があれば記載  
float16は精度がfloat32より低いため、用途に応じて精度とストレージ効率のバランスを検討してください。

情報源: https://azure.microsoft.com/updates?id=523796

**詳細**:

本アップデートにより、Azure Cosmos DBのベクターインデックスでfloat16（半精度浮動小数点）データ型が正式サポートされました。従来はfloat32（単精度浮動小数点）が主流でしたが、float16を利用することでベクターのストレージ容量を約半分に削減可能です。これにより、大規模な類似検索や機械学習モデルの埋め込みベクトルを効率的に管理でき、コスト削減と高速なクエリ応答が期待されます。技術的には、float16は16ビットで表現され、精度はfloat32より低いものの、多くの類似検索用途で十分な精度を維持します。実装は、ベクター型のスキーマ定義時にデータ型をfloat16に指定する形で行い、既存のAPIやSDKから透過的に利用可能です。活用例としては、画像・音声・テキストの埋め込みベクトル検索やレコメンドシステムの高速化が挙げられます。注意点として、float16の精度低下が検索結果に影響を与える可能性があるため、用途に応じた精度検証が必要です。また、float16対応はベクターインデックスに限定され、他のデータ型やインデックスには影響しません。Azure Cognitive SearchやAzure Machine Learningと連携することで、ベクター検索の前処理や後処理を効率化でき、エンドツーエンドのAIソリューション構築に寄与します。詳細は公式ドキュメントを参照してください。

---

### 51. Generally Available: Azure Cosmos DB for Visual Studio Code  

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Cosmos DB for Visual Studio Code  ](https://azure.microsoft.com/updates?id=523782)

**アップデートID**: 523782
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DBのVisual Studio Code拡張機能が一般提供（GA）となりました。

- 主な変更点や新機能  
VS Code内で直接Cosmos DBのデータベース作成、クエリ実行、リソース管理が可能に。開発効率が向上し、インテリジェントアプリ開発を支援します。

- 影響を受ける対象  
Azure Cosmos DBを利用する開発者、特にVS Codeユーザー。

- 注意点があれば記載  
既存の拡張機能利用者は最新版への更新を推奨。接続設定や認証情報の管理に注意してください。

**詳細**:

Azure Cosmos DB for Visual Studio Codeが一般提供（GA）されました。本アップデートは、開発者がより効率的に分散型データベースを操作・管理できるようにすることを目的としています。Visual Studio Code拡張機能として提供され、Azure Cosmos DBのデータベース作成、クエリ実行、ドキュメント編集、パーティションキー管理などの操作をIDE内でシームレスに行えます。技術的には、Azure Cosmos DBのREST APIやSDKを拡張機能が利用し、認証はAzure ADや接続文字列をサポート。リアルタイムでのデータ変更反映やクエリ結果の即時表示が可能です。活用シナリオとしては、ローカル開発環境から直接クラウドのCosmos DBリソースを操作し、迅速なデバッグやデータ検証が挙げられます。注意点としては、大規模データの一括操作には向かず、拡張機能のバージョン管理やAzure側のアクセス権設定が必要です。Azure FunctionsやAzure Logic Appsなど他のAzureサービスと連携し、イベント駆動型のアプリケーション開発を支援します。

---

### 52. Generally Available: Azure Cosmos DB Mirroring in Microsoft Fabric 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Cosmos DB Mirroring in Microsoft Fabric ](https://azure.microsoft.com/updates?id=523773)

**アップデートID**: 523773
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DB Mirroring機能がMicrosoft Fabricで一般提供開始。

- 主な変更点や新機能  
既存のCosmos DB運用データをFabricの分析環境にリアルタイムでミラーリング可能。FabricのSQLクエリエンジンなど分析機能とシームレスに連携できる。

- 影響を受ける対象  
Cosmos DBを利用しつつ、Microsoft Fabricで高度な分析を行いたい技術者やデータエンジニア。

- 注意点があれば記載  
ミラーリング設定時のネットワーク帯域やコスト影響を考慮し、運用設計を行う必要がある。  

情報源: https://azure.microsoft.com/updates?id=523773

**詳細**:

Azure Cosmos DB Mirroring in Microsoft Fabricが一般提供開始されました。本機能は、既存のAzure Cosmos DBの運用データをMicrosoft Fabricの分析環境とシームレスに連携させることを目的としています。具体的には、Cosmos DBのデータをリアルタイムまたは近リアルタイムでFabricにミラーリングし、Fabric上のSQLクエリエンジンや分析ツールで高度な分析処理を実行可能にします。技術的には、Cosmos DBの変更データキャプチャ（CDC）やストリーム処理を活用し、データ同期の遅延を最小化。設定はAzureポータルやCLIから行い、既存のCosmos DBアカウントに対して簡単にミラーリングを有効化できます。活用シナリオとしては、運用DBの負荷を抑えつつリアルタイム分析やBIダッシュボードの構築が挙げられ、特にIoTやeコマースのトランザクション分析に有効です。注意点としては、ミラーリング対象のデータサイズや更新頻度により同期遅延やコストが増加する可能性があるため、設計段階での負荷評価が必要です。また、Fabricの分析機能はSQLベースのクエリに最適化されているため、複雑なNoSQLクエリは事前変換が推奨されます。関連サービスとしてAzure Synapse AnalyticsやPower BIとの連携も容易で、統合的なデータ分析基盤構築に貢献します。詳細は公式ドキュメント（https://azure.microsoft.com/updates?id=523773）を参照してください。

---

### 53. Generally Available: Cosmos DB in Microsoft Fabric 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Cosmos DB in Microsoft Fabric ](https://azure.microsoft.com/updates?id=523768)

**アップデートID**: 523768
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Analytics, Azure Cosmos DB, Microsoft Fabric

**要約**:

- 何が更新されたか  
Microsoft FabricでのAzure Cosmos DBが一般提供（GA）開始。

- 主な変更点や新機能  
Fabric上でCosmos DBのAI機能を活用し、JSONデータに対するSQLクエリ実行やリアルタイム分析が可能に。

- 影響を受ける対象  
Microsoft Fabricを利用する開発者やデータエンジニア、リアルタイム分析を行う技術者。

- 注意点があれば記載  
既存のCosmos DBユーザーはFabric統合による運用やコスト面の影響を検討する必要あり。

**詳細**:

Microsoft FabricにおけるAzure Cosmos DBの一般提供開始により、運用系および分析系ワークロードを単一プラットフォーム上で統合的に構築可能となった。本アップデートは、Fabricの分散データ処理基盤とCosmos DBのマルチモデルNoSQLデータベース機能を融合し、JSONデータに対するSQLクエリのリアルタイム実行やAI機能の活用を実現することを目的としている。技術的には、Fabric内でCosmos DBのAPIをネイティブサポートし、低レイテンシかつスケーラブルなデータアクセスを提供。データの整合性と高可用性を維持しつつ、分析処理とトランザクション処理の両立を可能にしている。活用例としては、IoTデバイスからの大量JSONデータのリアルタイム分析や、ユーザ行動ログの即時集計・AIによる異常検知などが挙げられる。注意点としては、Fabric環境特有のリソース管理やスケーリング設定が必要であり、既存のCosmos DB単体利用時と異なる運用面の考慮が求められる。さらに、Power BIやAzure Synapse Analyticsとの連携により、より高度なBIやデータウェアハウス機能との統合が可能である。詳細は公式ドキュメントおよび更新情報を参照のこと。

---

### 54. Public Preview: Index Advisor for Azure DocumentDB 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Index Advisor for Azure DocumentDB ](https://azure.microsoft.com/updates?id=523763)

**アップデートID**: 523763
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure DocumentDB（Cosmos DB）のVS Code拡張機能に「Index Advisor」がパブリックプレビューで追加されました。

- 主な変更点や新機能  
自然言語で最適なインデックス設計やベストプラクティスを推奨し、MongoDBワークロードのパフォーマンス解析とデバッグを支援します。

- 影響を受ける対象  
Azure Cosmos DBのMongoDB APIを利用する開発者やDB管理者。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に行い、フィードバックを活用してください。

**詳細**:

Azure DocumentDB（Cosmos DBのMongoDB API対応版）向けの新機能「Index Advisor」がVS Code拡張機能にパブリックプレビューとして統合されました。本機能は、MongoDBワークロードのパフォーマンス最適化を目的に、自然言語解析を用いて最適なインデックス設計を推奨し、データベースのクエリ効率を向上させます。具体的には、VS Code上で実行したクエリの解析結果から、不要なインデックスの削減や新規インデックスの追加を提案し、パフォーマンスボトルネックの特定と改善を支援します。技術的には、クエリパターンを収集しAzureの機械学習モデルで解析、最適化案を自然言語で提示する仕組みです。活用例としては、運用中のMongoDB APIデータベースに対し、クエリ遅延の原因を迅速に特定し、適切なインデックス設計を適用することでレスポンス改善が可能です。注意点としては、プレビュー段階のため推奨内容の検証が必要であり、全てのクエリパターンに対応しきれない場合があります。また、VS CodeのDocumentDB拡張機能の最新版が必須です。関連サービスとしては、Cosmos DBのMongoDB APIと連携し、Azure MonitorやAzure Advisorと組み合わせて総合的なパフォーマンス管理が可能です。詳細は公式ドキュメントを参照してください。  
https://azure.microsoft.com/updates?id=523763

---

### 55. Generally Available: Priority-based execution in Azure Cosmos DB 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Priority-based execution in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=523754)

**アップデートID**: 523754
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DBで優先度ベースの実行が一般提供（GA）されました。

- 主な変更点や新機能  
リソース競合時に高優先度リクエストを優先処理し、低優先度リクエストを先にスロットリングする機能が追加されました。

- 影響を受ける対象  
高負荷環境でのパフォーマンス制御が必要なCosmos DB利用者。

- 注意点があれば記載  
優先度設定の適切な管理が必要で、誤設定によるリクエスト遅延に注意してください。

**詳細**:

Azure Cosmos DBにおける「Priority-based execution」機能がGA（一般提供）されました。本機能は、リソース競合が発生した際に高優先度リクエストを優先的に処理し、低優先度リクエストを先にスロットリングすることで、重要な操作の遅延を最小化することを目的としています。具体的には、リクエストに優先度タグを付与し、Azure Cosmos DBのスループット制御機構が優先度に基づくスロットリングを実施します。これにより、ピーク時やリソース制約下でもミッションクリティカルなトランザクションやクエリの応答性を維持可能です。実装はSDKやREST APIのリクエストヘッダーに優先度パラメータを設定する形で行い、既存のスループット管理とシームレスに統合されます。活用例としては、IoTデバイスからの重要なデータ書き込みやリアルタイム分析クエリの優先処理が挙げられます。一方で、優先度設定は適切に設計しないと低優先度リクエストの遅延が過度に発生するため注意が必要です。また、Azure FunctionsやEvent Gridなど他のAzureサービスと連携し、優先度付き処理のトリガーや監視を組み合わせることで運用効率を高められます。詳細は公式ドキュメントおよびアップデートページを参照してください。https://azure.microsoft.com/updates?id=523754

---

### 56. Public Preview: Azure Cosmos DB Fleet Analytics 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Cosmos DB Fleet Analytics ](https://azure.microsoft.com/updates?id=523745)

**アップデートID**: 523745
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DB Fleet Analyticsがパブリックプレビューとして提供開始。

- 主な変更点や新機能  
複数のCosmos DBアカウントやサブスクリプションを横断してデータを統合分析可能。大規模環境の運用管理を支援。

- 影響を受ける対象  
複数アカウント・サブスクリプションでCosmos DBを運用する技術者や運用チーム。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に。機能やAPIが変更される可能性あり。

**詳細**:

Azure Cosmos DB Fleet Analyticsは、複数のAzure Cosmos DBアカウントやサブスクリプションにまたがるデータベースの運用状況を一元的に可視化・分析するための新機能で、パブリックプレビューとして提供開始されました。背景には、大規模かつ分散したCosmos DB環境の運用管理の複雑化があり、運用負荷軽減とパフォーマンス最適化を目的としています。主な機能は、複数アカウントのクエリパフォーマンス、スループット使用率、ストレージ消費、エラー率などのメトリクスを統合ダッシュボードで確認可能な点です。技術的には、各アカウントからメトリクスを収集しAzure MonitorやLog Analyticsと連携してデータを集約、Kustoクエリ言語(KQL)を用いた詳細分析が可能です。実装はAzure Portal上でFleet Analyticsを有効化し、対象アカウントを登録する形で行います。活用例としては、グローバル展開するマルチリージョン環境のパフォーマンスボトルネック特定やコスト最適化、運用アラートの一元管理が挙げられます。注意点としては、パブリックプレビュー段階のため機能変更や制限がある可能性、また大量アカウントの監視時にデータ収集の遅延が発生する場合があります。関連サービスとしてAzure Monitor、Log Analytics、Azure Advisorとの連携が強化されており、包括的な運用管理基盤構築に寄与します。

---

### 57. Generally Available: Azure Cosmos DB fleet pools  

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Cosmos DB fleet pools  ](https://azure.microsoft.com/updates?id=523740)

**アップデートID**: 523740
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DBの「fleet pools」が一般提供（GA）となりました。

- 主な変更点や新機能  
マルチテナントSaaSアプリ向けに、複数アカウントでリソースをプール化し、容量管理を簡素化。大規模運用時のスケーラビリティと効率性が向上します。

- 影響を受ける対象  
Azure Cosmos DBを大規模かつマルチテナント環境で運用する開発者・運用者。

- 注意点があれば記載  
既存の単一アカウント運用からの移行計画やプール設定の最適化が必要です。

**詳細**:

Azure Cosmos DB fleet poolsは、大規模なマルチテナントSaaSアプリケーション向けに設計された新機能で、複数のCosmos DBアカウントを一元管理し、容量管理を簡素化します。従来は個別アカウント単位でのスケーリングやリソース割当てが必要でしたが、fleet poolsにより複数アカウントをプール化し、リソースを共有・動的に配分可能です。これにより、テナントごとの負荷変動に柔軟に対応でき、運用コストや管理負担を削減します。技術的には、プール内のアカウントが共通のスループットリソースを利用し、API経由でプールの作成・管理が可能です。活用例としては、SaaS事業者が顧客ごとに独立したCosmos DBアカウントを割り当てつつ、全体のリソースを効率的に配分するケースが挙げられます。注意点としては、プール内のリソース競合やスループット制限に留意が必要で、適切なモニタリングとスケーリング戦略が求められます。Azure FunctionsやAzure Monitorと連携し、運用自動化やパフォーマンス監視を強化可能です。

---

### 58. Generally Available: Azure DocumentDB - an open-source, MongoDB-compatible document database service for hybrid and multicloud

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure DocumentDB - an open-source, MongoDB-compatible document database service for hybrid and multicloud](https://azure.microsoft.com/updates?id=523735)

**アップデートID**: 523735
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure DocumentDBが一般提供（GA）となり、オープンソースのMongoDB互換ドキュメントデータベースサービスとして正式リリース。

- 主な変更点や新機能  
Linux Foundation管理のMongoDB互換エンジンを採用し、ハイブリッドおよびマルチクラウド環境での利用が可能に。完全マネージドサービスでスケーラビリティと運用負荷軽減を実現。

- 影響を受ける対象  
MongoDB互換のドキュメントDBを利用する開発者や企業、特にAzure環境でのハイブリッド・マルチクラウド戦略を検討する技術者。

- 注意点があれば記載  
既存のAzure Cosmos DB for MongoDBユーザーは移行や互換性を確認する必要がある。オープンソース版の特性理解も重要。

**詳細**:

Microsoftは、オープンソースでMongoDB互換のドキュメントデータベースサービス「Azure DocumentDB」を一般提供開始しました。これは従来のAzure Cosmos DB for MongoDB APIをベースに、Linux Foundationの管理下にあるDocumentDBをフルマネージドで提供するもので、ハイブリッドおよびマルチクラウド環境での柔軟なデータ管理を目的としています。主な機能はMongoDBのAPI互換性を維持しつつ、高可用性・自動スケーリング・グローバル分散レプリケーションをネイティブにサポート。技術的には、DocumentDBのコアエンジンをAzureインフラ上に最適化し、MongoDBドライバとの互換性を確保しています。活用例としては、既存MongoDBアプリケーションの移行や、オンプレミスとAzure間でのデータ同期、マルチクラウド戦略の一環としての利用が挙げられます。注意点としては、MongoDBの一部機能（特定の集計パイプラインやトランザクション機能）が完全対応していない場合があるため、移行前の検証が必要です。また、Azure FunctionsやAzure Logic Appsとの連携によりイベント駆動型の処理が可能で、Azure Monitorでパフォーマンス監視も行えます。これにより、MongoDB互換の柔軟性とAzureのマネージドサービスの信頼性を両立した運用が実現します。

---

### 59. Public Preview: Dynamic data masking with Azure Cosmos DB 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Dynamic data masking with Azure Cosmos DB ](https://azure.microsoft.com/updates?id=523726)

**アップデートID**: 523726
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DBで動的データマスキング（DDM）がパブリックプレビューとして利用可能に。

- 主な変更点や新機能  
サーバー側のポリシーベースで非特権ユーザーに対し、機密データを動的にマスクし、不正アクセスを防止。

- 影響を受ける対象  
Cosmos DBを利用し、機密情報のアクセス制御を強化したい開発者や運用者。

- 注意点があれば記載  
プレビュー機能のため、本番環境での利用は慎重に検討し、最新ドキュメントを確認すること。

**詳細**:

本アップデートは、Azure Cosmos DBにおける機密データ保護強化を目的とし、動的データマスキング（Dynamic Data Masking：DDM）機能をパブリックプレビューとして提供開始しました。DDMはサーバーサイドで動作するポリシーベースのセキュリティ機能で、権限のないユーザーに対して特定のフィールドのデータを動的にマスク表示し、実データの漏洩を防止します。設定はAzureポータルやARMテンプレート、Azure CLIで行い、マスキングルールはフィールド単位で指定可能です。マスクパターンは部分マスクや全マスクなど複数から選択でき、クエリ実行時に自動適用されます。主な活用シナリオは、開発・テスト環境での機密情報非表示や、権限分離が求められる業務システムでのデータアクセス制御です。注意点として、DDMはクエリレベルでのマスキングであり、ストレージ上のデータは暗号化されていないため、他のセキュリティ対策と併用が推奨されます。また、マスキングはSQL API利用時に有効で、他APIでは対応状況を確認する必要があります。Azure RBACやAzure ADと連携し、ユーザー権限に応じた柔軟なアクセス制御が可能です。これにより、Azure Cosmos DBのデータ保護ポリシーを強化しつつ、運用負荷を低減できます。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 60. Public Preview: Online and offline migrations in Azure DocumentDB Migration extension 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Online and offline migrations in Azure DocumentDB Migration extension ](https://azure.microsoft.com/updates?id=523721)

**アップデートID**: 523721
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure DocumentDB Migration拡張機能がVisual Studio Code向けにパブリックプレビューで提供開始されました。

- 主な変更点や新機能  
MongoDBからAzure DocumentDBへの移行をオンライン・オフライン両モードでサポートし、シームレスかつ無償で移行可能です。

- 影響を受ける対象  
MongoDBをAzure DocumentDBに移行したい開発者や運用技術者。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

本アップデートは、MongoDBからAzure Cosmos DB（旧称DocumentDB）への移行を容易にするため、Visual Studio Code用のAzure DocumentDB Migration拡張機能をパブリックプレビューとして提供開始したものです。これにより、MongoDBのデータやスキーマをオンライン（稼働中のデータベースからリアルタイムで同期）およびオフライン（事前にエクスポートしたデータを移行）両モードで無償かつシームレスに移行可能となり、移行作業の工数削減とダウンタイム最小化を実現します。拡張機能はVS Code上で動作し、MongoDB接続情報とCosmos DB接続情報を設定後、GUIベースで移行ジョブを管理可能。オンライン移行ではChange Streamを活用し、変更差分をリアルタイムに同期します。主な活用シナリオは、既存のMongoDBアプリケーションをAzureのグローバル分散型Cosmos DBに移行し、スケーラビリティや高可用性を確保するケースです。注意点として、MongoDBの一部機能（例：特定のインデックスやトランザクション）はCosmos DBで完全互換がない場合があり、移行前の検証が必要です。また、移行中はネットワーク帯域やリソース消費に留意してください。関連サービスとしてAzure Cosmos DBのMongoDB APIを利用し、Azure MonitorやAzure CLIと連携して移行状況の監視や自動化が可能です。

---

### 61. Generally Available: Online migration from Azure Cosmos DB for MongoDB RU to Azure DocumentDB

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Online migration from Azure Cosmos DB for MongoDB RU to Azure DocumentDB](https://azure.microsoft.com/updates?id=523716)

**アップデートID**: 523716
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB

**要約**:

- 何が更新されたか  
Azure Cosmos DB for MongoDB APIのRUからAzure DocumentDBへのオンライン移行機能が一般提供開始。

- 主な変更点や新機能  
Azureポータル上で自己完結型のシームレスなオンライン移行が可能に。ダウンタイムなしでMongoDBワークロードのモダナイズが実現。

- 影響を受ける対象  
Cosmos DB MongoDB APIを利用中で、DocumentDBへの移行を検討している技術者・組織。

- 注意点があれば記載  
移行前に互換性やアプリケーション動作確認を推奨。移行中のパフォーマンス影響に注意。

**詳細**:

本アップデートは、Azure Cosmos DB for MongoDB APIのRU（Request Unit）ベース課金モデルからAzure DocumentDB（Cosmos DBのネイティブSQL API）へのオンラインマイグレーション機能をAzureポータル上でセルフサービスで提供開始したものです。これにより、MongoDB互換ワークロードを停止時間ゼロで最新のDocumentDB環境へ移行可能となり、運用負荷とダウンタイムを大幅に削減します。技術的には、データ同期をリアルタイムで行いながら、書き込み・読み込みを継続し、移行完了後に切り替えを実施する仕組みを採用。Azureポータルのマイグレーションウィザードから簡単に操作でき、データ整合性とパフォーマンスを維持します。活用例としては、MongoDB APIの制約を超えた高度なクエリやトランザクション、スケーラビリティをDocumentDBで実現したいケースに最適です。注意点としては、マイグレーション中のスキーマ互換性や一部MongoDB固有機能の非対応に留意が必要です。さらに、Azure MonitorやAzure Advisorと連携し、移行状況の監視や最適化が可能です。

---

### 62. Public Preview: Oracle to PostgreSQL migration tooling in Visual Studio Code 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Oracle to PostgreSQL migration tooling in Visual Studio Code ](https://azure.microsoft.com/updates?id=523593)

**アップデートID**: 523593
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Visual Studio CodeのAzure Database for PostgreSQL拡張機能に、OracleからPostgreSQLへのマイグレーションツールがパブリックプレビューで追加されました。

- 主な変更点や新機能  
OracleのスキーマやデータをPostgreSQL形式に自動変換し、移行作業を効率化。コード内で直接操作可能で、手動作業を大幅削減します。

- 影響を受ける対象  
Oracle DBからPostgreSQLへ移行を検討している開発者やDB管理者、Azure上でのデータベース移行を行う技術者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での使用は慎重に。移行前に十分なテストと検証が必要です。

**詳細**:

本アップデートは、OracleデータベースからPostgreSQLへの移行を効率化するため、Visual Studio CodeのAzure Database for PostgreSQL拡張機能にOracle-to-PostgreSQL移行ツールをパブリックプレビューとして追加したものです。これにより、SQLスクリプトやスキーマの自動変換が可能となり、手作業でのコード修正や移行時間を大幅に削減します。ツールはOracleのPL/SQL構文を解析し、PostgreSQL互換のSQLに変換、依存関係のあるオブジェクトも考慮して一括変換を実現します。Visual Studio Code上で直接操作できるため、開発環境に統合しやすく、CI/CDパイプラインへの組み込みも容易です。典型的な活用例は、Oracleの既存資産をAzure Database for PostgreSQLに移行する際の事前検証やスキーマ変換作業の自動化です。注意点としては、完全な自動変換が保証されないため、変換後のコードレビューやテストが必須であり、複雑なPL/SQLロジックは手動調整が必要な場合があります。また、現時点ではパブリックプレビューのため、機能追加や仕様変更の可能性があります。Azure Database for PostgreSQLとの連携により、移行後のデータベース管理やパフォーマンスチューニングも一元的に行えます。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 63. Generally Available: 2025 REST API for Azure Database for PostgreSQL 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: 2025 REST API for Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=523588)

**アップデートID**: 523588
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL向けの2025 REST APIが一般提供開始。

- 主な変更点や新機能  
PostgreSQL 17および18をサポートし、新バージョンへの移行が自動化パターンの変更なしで可能に。デフォルトデータベース設定もAPI経由で指定可能に。

- 影響を受ける対象  
Azure Database for PostgreSQLを利用し、REST APIで管理や自動化を行う技術者。

- 注意点  
既存のAPI利用者は新バージョン対応のためAPIバージョン確認とテスト推奨。

**詳細**:

Azure Database for PostgreSQLの2025 REST APIが一般提供（GA）されました。本アップデートはPostgreSQL 17および18のサポートを追加し、既存の自動化スクリプトや運用フローを変更せずに最新バージョンを利用可能にすることを目的としています。新APIでは、デフォルトデータベースの設定が可能となり、インスタンス作成時の初期構成が柔軟に行えます。REST APIはHTTPベースでAzure Resource Manager（ARM）と連携し、認証はAzure ADトークンを用いるためセキュアかつ統一的な管理が可能です。活用例としては、CI/CDパイプライン内でのPostgreSQLインスタンスのプロビジョニングやバージョンアップ自動化、運用監視ツールとの統合が挙げられます。注意点としては、新バージョンのPostgreSQL固有の機能や互換性に関する検証が必要であり、APIのバージョン管理に留意することが推奨されます。Azure MonitorやAzure Policyとの連携により、運用の可視化とガバナンス強化が可能です。詳細は公式ドキュメントおよびAzureポータルのAPIリファレンスを参照してください。

---

### 64. Generally Available: Elastic clusters on Azure Database for PostgreSQL – Flexible Server 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Elastic clusters on Azure Database for PostgreSQL – Flexible Server ](https://azure.microsoft.com/updates?id=523583)

**アップデートID**: 523583
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL – Flexible ServerでElastic Clusters機能が一般提供開始。

- 主な変更点や新機能  
行ベース・スキーマベースのシャーディングにより水平スケールが可能に。シャード管理やテナント分離を自動化し、マルチテナントアプリの構築が容易に。

- 影響を受ける対象  
PostgreSQL Flexible Serverを利用するアプリ開発者や運用者。

- 注意点があれば記載  
シャーディング設計の理解が必要で、既存環境への適用時は検証を推奨。

**詳細**:

Azure Database for PostgreSQL – Flexible Serverにおいて、Elastic Clusters機能がGA（一般提供）されました。本機能は、行ベースおよびスキーマベースのシャーディングによる水平スケーリングを実現し、マルチテナントアプリケーションの構築を容易にします。従来、シャード管理やテナント分離は開発者の負担でしたが、Elastic Clustersはこれらの運用を自動化し、シャードの追加・削除やクエリルーティングを効率化します。技術的には、複数のPostgreSQLインスタンスをクラスタとして連携させ、データ分散と整合性を保ちながらスケールアウトを可能にします。典型的な活用例は、SaaS環境でのテナントごとのデータ分割や大規模データセットの分散処理です。注意点としては、シャーディング設計の適切な計画が必要であり、トランザクションの跨るシャード間処理は制限される場合があります。Azure MonitorやAzure Arcとの連携により、運用監視やガバナンスも強化可能です。詳細は公式ドキュメントを参照してください。

---

### 65. Public Preview: Native Microsoft Foundry support for Azure Database for PostgreSQL

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Native Microsoft Foundry support for Azure Database for PostgreSQL](https://azure.microsoft.com/updates?id=523578)

**アップデートID**: 523578
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQLがMicrosoft Foundryとネイティブ連携し、パブリックプレビューを開始。

- 主な変更点や新機能  
Azure PostgreSQL MCPサーバーがMicrosoft Foundryに統合され、AIエージェントによる安全なクエリ実行とデータ分析が可能に。

- 影響を受ける対象  
Azure PostgreSQLを利用する開発者やデータサイエンティスト、AIエージェント構築者。

- 注意点  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討が必要。

**詳細**:

本アップデートは、Azure Database for PostgreSQLのMCP（Managed Compute Platform）サーバーがMicrosoft Foundryとネイティブ統合されたことを発表するものです。背景として、AIエージェントによるデータベースへの安全なクエリ実行と分析ニーズの高まりがあり、Foundryの導入によりこれを実現します。具体的には、Foundry上でAIモデルが直接PostgreSQLデータベースにアクセスし、自然言語クエリや高度な分析を行うことが可能となりました。技術的には、Foundryのセキュアな認証・認可機構を介してMCPサーバーと連携し、API経由でクエリを送受信します。活用例としては、AIチャットボットによるリアルタイムデータ分析や、カスタムAIエージェントによる業務自動化が挙げられます。注意点としては、現段階がパブリックプレビューであるため、機能の安定性やサポート範囲に制限がある点、及びFoundry利用に伴う追加コストが考慮すべき事項です。関連サービスとしては、Azure AI、Azure Identity（Azure AD）による認証管理、Azure Monitorによる運用監視との連携が推奨されます。詳細は公式リンク参照。

---

### 66. Generally Available: Azure Database for PostgreSQL – Flexible Server anon extension 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Database for PostgreSQL – Flexible Server anon extension ](https://azure.microsoft.com/updates?id=523569)

**アップデートID**: 523569
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverでanon拡張機能がGA（一般提供）となりました。

- 主な変更点や新機能  
anon拡張により、データの匿名化処理が可能となり、プライバシー保護やコンプライアンス対応が強化されます。

- 影響を受ける対象  
PostgreSQL Flexible Serverを利用する開発者や運用者。

- 注意点  
anon拡張の利用にはPostgreSQLの拡張機能の理解が必要で、適切な設定とテストを推奨します。

**詳細**:

Azure Database for PostgreSQL Flexible Serverにanon拡張機能がGA（一般提供）されました。本拡張はデータ匿名化を目的とし、個人情報保護やコンプライアンス対応を強化します。anon拡張は、テーブル内の特定カラムに対しマスキングやトークナイゼーション、ランダム化などの匿名化関数を提供し、クエリ実行時に動的にデータを変換可能です。実装はPostgreSQLの拡張機能として組み込まれ、SQL関数として利用できるため既存のアプリケーション変更を最小限に抑えられます。典型的な活用例は、開発・検証環境での個人情報を含むデータの安全な利用や、GDPRやCCPAなどの規制対応です。注意点としては、匿名化は完全な不可逆性を保証しないため、機密度に応じた適切な匿名化手法の選択が必要です。また、パフォーマンス影響を考慮し、大量データ処理時は事前バッチ処理も検討します。Azure Data FactoryやAzure Synapse Analyticsと連携し、匿名化済みデータのETLや分析基盤構築が可能です。詳細は公式ドキュメントを参照してください。

---

### 67. Public Preview: Azure Database for PostgreSQL – Flexible Server v6 series VMs and AMD v6 Confidential Compute

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Database for PostgreSQL – Flexible Server v6 series VMs and AMD v6 Confidential Compute](https://azure.microsoft.com/updates?id=523564)

**アップデートID**: 523564
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverでv6シリーズVM（Intel/AMD）とAMD v6 Confidential Computeのパブリックプレビューが開始。

- 主な変更点や新機能  
一般用途およびメモリ最適化のv6シリーズVMがローカルNVMeストレージ対応で利用可能に。AMDの機密コンピュートも選択可能。

- 影響を受ける対象  
Azure Database for PostgreSQL Flexible Server利用者、特に高性能・セキュア環境を求める技術者。

- 注意点  
パブリックプレビューのため、本番環境での利用は慎重に。対応リージョンや価格を事前確認推奨。

**詳細**:

本アップデートでは、Azure Database for PostgreSQL Flexible Serverにおいて、v6シリーズの一般用途およびメモリ最適化型VMがパブリックプレビューで利用可能となりました。v6シリーズはIntelおよびAMDプロセッサを選択可能で、ローカルNVMeストレージを搭載し、高速I/O性能を実現します。これにより、データベースのスループットとレイテンシが大幅に改善され、大規模トランザクション処理や分析ワークロードに適しています。特にAMD v6 Confidential Computeは、ハードウェアベースの機密コンピューティング機能を提供し、データの暗号化と保護を強化します。実装はAzureポータルやCLIからv6シリーズのFlexible Serverを選択するだけで可能で、既存のPostgreSQL環境との互換性も維持されます。活用シナリオとしては、金融や医療などセキュリティ要件が高い業界での機密データ処理、または高I/O性能を必要とするアプリケーションに最適です。注意点として、パブリックプレビュー段階のため一部リージョンでの提供制限やSLAの適用外がある点に留意が必要です。関連サービスとしては、Azure Monitorによるパフォーマンス監視やAzure Key Vaultとの連携による鍵管理が推奨されます。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 68. Public Preview: Azure Database for PostgreSQL – Flexible Server pg_duckdb extension 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure Database for PostgreSQL – Flexible Server pg_duckdb extension ](https://azure.microsoft.com/updates?id=523559)

**アップデートID**: 523559
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverでpg_duckdb拡張機能がパブリックプレビューとして利用可能になりました。

- 主な変更点や新機能  
DuckDBのベクトル化・カラムナー実行により、高速な分析処理が可能になります。

- 影響を受ける対象  
PostgreSQL Flexible Serverを利用するデータ分析やBI用途の技術者。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

本アップデートは、Azure Database for PostgreSQL Flexible Serverにおいてpg_duckdb拡張機能のパブリックプレビュー提供を開始したものです。背景には、分析処理の高速化ニーズに応え、DuckDBのベクトル化・カラムナ実行エンジンをPostgreSQL上で活用可能にする狙いがあります。具体的には、pg_duckdb拡張を有効化することで、SQLクエリ内でDuckDBの高速分析機能を呼び出せ、複雑な集計やOLAP処理を効率化可能です。実装はFlexible Server上で拡張をCREATE EXTENSIONコマンドにより追加し、標準SQLと連携して利用します。活用例としては、大規模データのインタラクティブ分析やBIツールとの連携によるリアルタイム分析が挙げられます。注意点としては、現時点でプレビュー版のため、機能制限やパフォーマンスの変動があり、商用環境での利用は慎重を要します。また、Azure Synapse AnalyticsやAzure Data Factoryと組み合わせることで、ETL処理後の分析高速化やデータパイプラインの最適化が可能です。詳細は公式ドキュメントを参照してください。

---

### 69. Public Preview: Azure SQL change event streaming 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure SQL change event streaming ](https://azure.microsoft.com/updates?id=523533)

**アップデートID**: 523533
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database

**要約**:

- 何が更新されたか  
Azure SQL Databaseからのデータ変更をほぼリアルタイムでAzure Event Hubsへストリーミング可能なChange Event Streaming（CES）がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
データ統合の効率化、イベント駆動型アーキテクチャや高度な分析のサポートが強化。

- 影響を受ける対象  
Azure SQL Database利用者、イベント駆動型システムやリアルタイム分析を構築する技術者。

- 注意点があれば記載  
パブリックプレビューのため、商用環境での利用は慎重に。機能やAPIが変更される可能性あり。

**詳細**:

本アップデートは、Azure SQL Databaseのデータ変更イベントをほぼリアルタイムでAzure Event Hubsへ直接ストリーミング可能にする「Change Event Streaming（CES）」のパブリックプレビュー提供開始を示すものです。背景には、従来のデータ連携がバッチ処理中心で遅延が発生しやすかった課題を解消し、イベント駆動型アーキテクチャやリアルタイム分析を促進する狙いがあります。

CESでは、トランザクションログの変更データキャプチャ（CDC）を活用し、挿入・更新・削除などの変更イベントを抽出。これをAzure Event Hubsに直接送信することで、下流のストリーム処理や分析基盤へ即時連携が可能です。実装はAzureポータルやCLIでCESを有効化し、Event Hubsの接続設定を行うだけで開始でき、専用のコード変更は不要です。

活用例としては、リアルタイムのデータ同期、異種システム間のイベント連携、Power BIやAzure Stream Analyticsによる即時分析などが挙げられます。注意点としては、現時点でパブリックプレビューのためSLAs非適用、対応リージョンやデータベースSKU制限、イベントの遅延や重複発生の可能性がある点に留意が必要です。

本機能はEvent Hubsを介してAzure FunctionsやLogic Apps、Azure Stream Analytics、Databricksなど多様なサービスと連携可能で、モダンなイベント駆動型データパイプライン構築に有効です。今後のGAに向けて性能や信頼性の強化が期待されます。

---

### 70. Generally Available: PostgreSQL 18 with in-place upgrade on Azure Database for PostgreSQL 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: PostgreSQL 18 with in-place upgrade on Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=523196)

**アップデートID**: 523196
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQLでPostgreSQL 18が一般提供開始されました。

- 主な変更点や新機能  
最新のPostgreSQL機能を利用可能になり、サーバーエンドポイントを変更せずに既存バージョンからのインプレースアップグレードが可能です。

- 影響を受ける対象  
Azure上でPostgreSQLを利用する開発者・運用者。

- 注意点があれば記載  
アップグレード前に互換性やバックアップを確認し、運用影響を最小限に抑えることが推奨されます。

**詳細**:

Azure Database for PostgreSQLにおいて、PostgreSQL 18が一般提供（GA）され、従来バージョンからのインプレースアップグレードが可能となりました。本アップデートは、最新のPostgreSQL機能を活用しつつ、サーバーエンドポイントを変更せずにバージョン移行を実現することで、運用負荷とダウンタイムの削減を目的としています。具体的には、PostgreSQL 18の新機能（パフォーマンス改善、拡張機能の強化、セキュリティ向上など）を利用可能となり、AzureポータルやCLIを通じてワンクリックでのアップグレード操作が提供されます。技術的には、バックグラウンドでのデータ整合性チェックとバージョン互換性検証を行い、既存データベースのスキーマや設定を保持したままアップグレードを実施します。活用シナリオとしては、既存のPostgreSQL環境を最新機能で強化したいWebアプリケーションや分析基盤の運用が挙げられます。一方、アップグレード前には互換性のある拡張機能の確認やバックアップ取得が必須であり、一部のカスタム設定や非対応拡張は手動対応が必要です。さらに、Azure MonitorやAzure Arcと連携することで、アップグレード後のパフォーマンス監視や運用管理を効率化可能です。

---

### 71. Generally Available: PostgreSQL extension for Visual Studio Code with GitHub Copilot  

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: PostgreSQL extension for Visual Studio Code with GitHub Copilot  ](https://azure.microsoft.com/updates?id=523187)

**アップデートID**: 523187
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Visual Studio Code向けのPostgreSQL拡張機能が一般提供（GA）となりました。

- 主な変更点や新機能  
PostgreSQLインスタンスへの接続、クエリ実行、接続プロファイル管理が可能。Microsoft Entra IDによる認証もサポートし、GitHub Copilotとの連携で開発効率が向上します。

- 影響を受ける対象  
VS Codeを使ってPostgreSQLを操作する開発者やDB管理者。

- 注意点があれば記載  
Microsoft Entra ID利用時は適切な権限設定が必要です。

**詳細**:

本アップデートは、Visual Studio Code向けPostgreSQL拡張機能の一般提供開始を告知するものです。背景には、開発者の生産性向上とクラウドデータベース管理の効率化があり、GitHub Copilotとの連携によりコード補完やクエリ作成支援が強化されています。主な機能は、PostgreSQLインスタンスへの接続管理、SQLクエリの実行、接続プロファイルの作成・編集、Microsoft Entra ID（旧Azure AD）による認証対応です。技術的にはVS Codeの拡張APIを活用し、Entra ID連携はOAuth 2.0ベースでセキュアな認証を実現。GitHub CopilotはAIによるコード補完を提供し、クエリ作成の効率化に寄与します。活用例としては、ローカル開発環境からAzure Database for PostgreSQLやオンプレミスPostgreSQLへのシームレスな接続、複雑なクエリの自動補完、認証管理の一元化が挙げられます。制限事項としては、Entra ID連携は対応リージョンやPostgreSQLのバージョンに依存する場合があり、GitHub Copilot利用には別途ライセンスが必要です。Azure Database for PostgreSQLとの連携により、クラウド上のデータベース管理が統合され、Azureのセキュリティ基盤と開発ツールの融合が促進されます。詳細は公式リンク参照。

---

### 72. Generally Available: Mirroring in Fabric for PostgreSQL Flexible Server  

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Mirroring in Fabric for PostgreSQL Flexible Server  ](https://azure.microsoft.com/updates?id=523177)

**アップデートID**: 523177
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Server向けに、Microsoft Fabricのミラーリング機能が一般提供（GA）となりました。

- 主な変更点や新機能  
Fabricミラーリングにより、OneLake上で組織のデータ統合が可能になり、ネットワーク分離環境でもデータ分析が簡素化されます。

- 影響を受ける対象  
PostgreSQL Flexible Serverを利用し、Fabricを活用したデータ分析や統合を検討している技術者や組織。

- 注意点  
ネットワーク分離環境での利用に対応していますが、設定や運用におけるセキュリティ要件を確認してください。

**詳細**:

本アップデートにより、Azure Database for PostgreSQL Flexible ServerがMicrosoft Fabricのミラーリング機能に対応し、一般提供（GA）となりました。背景には、組織内の分散データをOneLake上で統合し、分析基盤を簡素化するニーズの高まりがあります。Fabricミラーリングは、PostgreSQL Flexible ServerのデータをリアルタイムでFabricのOneLakeに複製し、ネットワーク分離環境下でも安全にデータ連携を実現します。技術的には、PostgreSQLのレプリケーション機能を活用しつつ、Fabricのデータレイクストレージと連携することで、データの整合性と可用性を確保します。活用例としては、複数のPostgreSQLインスタンスのデータをOneLakeに集約し、Power BIやSynapse Analyticsでの高度な分析を行うケースが挙げられます。注意点として、ミラーリングは対応リージョンとネットワーク構成に制限があり、設定時にネットワークポリシーや認証方式の整合性確認が必要です。関連サービスとして、Microsoft FabricのOneLake、Power BI、Azure Synapse Analyticsとの連携がスムーズで、統合データ分析基盤の構築に最適です。詳細は公式ドキュメントを参照してください。

---

### 73. Generally Available: Azure Database for PostgreSQL storage extension support for Parquet 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Database for PostgreSQL storage extension support for Parquet ](https://azure.microsoft.com/updates?id=523167)

**アップデートID**: 523167
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverで、Parquet形式のAzure Storage拡張機能がGAリリースされました。

- 主な変更点や新機能  
Parquetファイルの読み書きが直接可能になり、複数の圧縮オプションもサポート。データ連携や分析処理が高速化します。

- 影響を受ける対象  
PostgreSQL Flexible Serverを利用する開発者やデータエンジニア。

- 注意点があれば記載  
利用には対応するストレージ設定が必要で、圧縮オプションの選択に注意してください。

**詳細**:

Azure Database for PostgreSQL Flexible Serverが、Azure Storage拡張機能におけるParquetフォーマットの読み書きを正式サポートしました。本アップデートは、大容量データの効率的な入出力を目的とし、Parquetの列指向かつ圧縮対応の形式を活用することで、I/O性能とストレージ効率を大幅に向上させます。対応圧縮方式はSnappy、Gzip、Brotliなど複数を選択可能で、データの圧縮率と処理速度のバランス調整が可能です。技術的には、PostgreSQLの外部テーブル機能や拡張モジュールを通じて、Azure Blob Storage上のParquetファイルを直接クエリ可能とし、COPYコマンドや外部テーブル定義での読み書きを実現します。これにより、ETL処理やデータレイクとの連携が容易になり、BIツールや分析ワークロードの高速化が期待されます。活用例としては、Azure Synapse AnalyticsやAzure Data Factoryと連携し、PostgreSQLデータをParquet形式で効率的にエクスポート・インポートするケースが挙げられます。注意点としては、Parquetファイルのスキーマ管理や圧縮設定の整合性を保つ必要があり、既存のSQLクエリとの互換性検証も推奨されます。さらに、Azure Blob Storageのアクセス権限設定（SASトークンやマネージドID）を適切に構成することが重要です。本機能はAzureのストレージサービスと密接に連携し、柔軟かつ高速なデータ処理基盤を構築可能です。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 74. Generally Available: Azure SQL Managed Instance Next-gen General Purpose service tier 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure SQL Managed Instance Next-gen General Purpose service tier ](https://azure.microsoft.com/updates?id=523125)

**アップデートID**: 523125
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Azure SQL Managed Instance

**要約**:

- 何が更新されたか  
Azure SQL Managed InstanceのNext-gen General Purposeサービス層がGA（一般提供）開始。

- 主な変更点や新機能  
従来比で大幅なパフォーマンス向上を実現しつつ、コスト効率も維持。より高い計算能力と柔軟性を提供し、PaaSの管理の簡便さはそのまま。

- 影響を受ける対象  
Azure SQL Managed Instanceを利用する開発者・運用者。

- 注意点があれば記載  
既存のGeneral Purpose層からの移行時は性能やコストのバランスを検討すること。

**詳細**:

Azure SQL Managed InstanceのNext-gen General Purposeサービス層がGA（一般提供）となりました。本アップデートは、従来のGeneral Purpose層のコスト効率を維持しつつ、パフォーマンスを大幅に向上させることを目的としています。具体的には、最新のハードウェアとストレージ技術を活用し、CPU性能やI/Oスループットが強化され、より柔軟なコンピューティングリソース割り当てが可能となりました。これにより、PaaSの管理の簡便さを損なうことなく、高負荷なトランザクション処理や分析ワークロードへの対応力が向上します。実装面では、Azureの分散ストレージと高速ネットワークインフラを組み合わせ、レイテンシ低減とスケーラビリティを実現しています。活用シナリオとしては、ミッションクリティカルな業務アプリケーションやハイブリッドクラウド環境でのデータベース移行に適しています。注意点としては、現行のGeneral Purpose層からの移行時に互換性やパフォーマンス特性の違いを検証する必要があり、リージョン展開状況も確認が必要です。Azure MonitorやAzure Security Centerとの連携により、運用監視やセキュリティ強化も容易に行えます。詳細は公式ドキュメントを参照してください。

---

### 75. Public Preview: Azure SQL Database DiskANN vector indexing 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure SQL Database DiskANN vector indexing ](https://azure.microsoft.com/updates?id=523110)

**アップデートID**: 523110
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance

**要約**:

- 何が更新されたか  
Azure SQL Database、Azure SQL Managed Instance、Microsoft FabricのSQLデータベースでDiskANNを用いたベクトルインデックス機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
DiskANNアルゴリズムによる高速かつ効率的なベクトル類似検索が可能となり、特に製品推薦や類似コンテンツ検索に適している。

- 影響を受ける対象  
Azure SQL Database、Azure SQL Managed Instance、Microsoft FabricのSQLデータベース利用者。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討し、最新のドキュメントや制限事項を確認すること。

**詳細**:

本アップデートは、Azure SQL Database、Azure SQL Managed Instance、およびMicrosoft Fabric内のSQL Databaseにおいて、効率的なベクトル類似検索を実現するDiskANNベクトルインデックスのパブリックプレビューを提供するものです。背景には、AIや機械学習の発展に伴い、大規模なベクトルデータの高速検索ニーズが高まっている点があります。DiskANNはディスクベースの近似最近傍探索アルゴリズムで、メモリ消費を抑えつつ高精度な類似検索を可能にします。今回の実装では、SQLの拡張機能としてベクトル型カラムのインデックス作成が可能となり、従来のRDBMS上で直接ベクトル検索を行える点が特徴です。活用例としては、製品推薦、画像検索、自然言語処理の類似文書検索などが挙げられます。注意点としては、パブリックプレビュー段階のため性能や機能に制限があり、対応するベクトルの次元数やデータサイズに制約が存在する可能性があります。関連サービスとしては、Azure Cognitive ServicesやAzure Machine Learningと組み合わせることで、AIモデルの出力ベクトルを直接SQL内で効率的に検索・活用可能です。これにより、データベース中心のAIアプリケーション開発が促進されます。詳細は公式ドキュメントを参照してください。

---

### 76. Generally Available: MSSQL extension integration with GitHub Copilot in Visual Studio Code  

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: MSSQL extension integration with GitHub Copilot in Visual Studio Code  ](https://azure.microsoft.com/updates?id=523105)

**アップデートID**: 523105
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database

**要約**:

- 何が更新されたか  
Visual Studio CodeのMSSQL拡張機能がGitHub Copilotと統合され、正式リリースされた。

- 主な変更点や新機能  
AIによるSQLコード補完やスキーマ設計支援が可能になり、繰り返し作業の削減や開発速度の向上を実現。

- 影響を受ける対象  
VS CodeでMSSQL拡張を利用するデータベース開発者や運用担当者。

- 注意点があれば記載  
AI支援は提案ベースのため、生成コードの検証が必要。Copilot利用には別途ライセンスが必要となる場合がある。

**詳細**:

本アップデートは、Visual Studio CodeのMSSQL拡張機能にGitHub Copilotを統合し、AIによるSQLコード補完と生成を実現するものです。背景には、SQL開発の反復作業軽減と生産性向上のニーズがあり、Copilotの自然言語解析能力を活用して迅速なクエリ作成やスキーマ設計支援を目的としています。具体的には、SQL文の自動補完、クエリ最適化提案、テーブル定義やストアドプロシージャのコード生成が可能となり、開発者は自然言語で要件を入力するだけで適切なSQLコードを得られます。技術的には、VS Codeの拡張機能内でGitHub CopilotのAIモデルと連携し、リアルタイムにコード補完を提供。Azure SQL DatabaseやManaged Instanceと接続した状態で利用することで、実際のデータベース構造を踏まえた提案が可能です。活用シナリオとしては、複雑なクエリ作成やスキーマ変更時のコード生成、テストデータ作成の自動化が挙げられます。一方、AI生成コードの正確性やセキュリティ面の検証は必須であり、特に本番環境適用前のレビューが推奨されます。Azure DevOpsやGitHub Actionsとの連携により、CI/CDパイプライン内でのコード品質向上にも寄与します。

---

### 77. Generally Available: Azure SQL Database long-term retention (LTR) backup immutability 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure SQL Database long-term retention (LTR) backup immutability ](https://azure.microsoft.com/updates?id=523095)

**アップデートID**: 523095
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure SQL Database

**要約**:

- 何が更新されたか  
Azure SQL Databaseの長期保持（LTR）バックアップに対して不変性（immutability）が一般提供開始。

- 主な変更点や新機能  
LTRバックアップを不変設定でき、指定した保持期間中はバックアップの編集・削除が不可に。ランサムウェア対策やコンプライアンス遵守に有効。

- 影響を受ける対象  
Azure SQL Databaseの長期保持バックアップを利用するユーザー。

- 注意点  
不変性設定後は保持期間満了までバックアップの削除や変更ができないため、運用設計時に保持期間を慎重に設定する必要あり。

**詳細**:

Azure SQL Databaseの長期保持（LTR）バックアップに対し、バックアップの不変性（immutability）設定が一般提供（GA）されました。これはコンプライアンスや規制要件を満たすために、指定した保持期間中はバックアップの改変・削除を防止する機能です。ランサムウェア攻撃などによるバックアップの改ざんリスクを軽減し、データ保護を強化します。

技術的には、LTRバックアップの保存時に不変性ポリシーを適用し、Azure StorageのWORM（Write Once Read Many）機能を活用してデータの書き換えや削除を禁止します。設定はAzureポータル、Azure CLI、PowerShell、REST APIから可能で、保持期間はユーザーが指定できます。

活用例としては、金融や医療など厳格なデータ保持義務がある業界でのバックアップ管理に適しています。例えば、法令で定められた7年間のバックアップ保存期間中はデータを完全に保護し、監査対応を容易にします。

注意点として、不変性設定後は保持期間終了までバックアップの削除や変更ができないため、誤設定による不要なコスト増加に注意が必要です。また、LTRバックアップにのみ適用可能で、通常の短期バックアップには影響しません。

関連サービスとしては、Azure SQL Databaseの自動バックアップ機能と連携し、Azure Blob Storageのセキュリティ機能を活用する形で実装されています。これにより、Azureの統合されたバックアップ・リカバリ戦略の一環として運用可能です。

---

### 78. Generally Available: SQL Server Management Studio (SSMS) 22 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: SQL Server Management Studio (SSMS) 22 ](https://azure.microsoft.com/updates?id=522586)

**アップデートID**: 522586
**情報源**: Azure Updates API

**カテゴリ**: Launched

**要約**:

- 何が更新されたか  
SQL Server Management Studio (SSMS) 22が一般提供開始。

- 主な変更点や新機能  
Visual Studio 2026ベースで構築され、SQL Server 2025をサポート。SQLデータベースとの統合が強化され、管理やトラブルシューティングが効率化。

- 影響を受ける対象  
SQL ServerやAzure SQLを管理するDB管理者や開発者。

- 注意点があれば記載  
既存環境との互換性確認と新機能の習熟が推奨される。

**詳細**:

SQL Server Management Studio (SSMS) 22は、Visual Studio 2026基盤上に構築され、SQL Server 2025を正式サポートするGA版です。これにより最新のSQL Server機能に対応し、管理・開発効率が向上します。主な変更点は、SQL Server 2025の新機能対応、Azure SQL Databaseとの統合強化、クエリ編集やデバッグ機能の改善です。特にAzure SQL Databaseとの連携が深まり、クラウド環境でのデータベース管理がシームレスになりました。内部的にはVisual Studioの拡張機構を活用し、モジュール化されたプラグイン設計で拡張性を確保。活用例としては、オンプレミスとAzure環境のハイブリッド運用、最新T-SQL機能の検証、パフォーマンスチューニングが挙げられます。注意点としては、SSMS 22は従来版との共存が可能ですが、Visual Studio 2026の環境依存性に留意が必要です。また、一部旧バージョンSQL Serverとの互換性に制限があります。Azure Data StudioやAzureポータルとの連携により、統合的なデータ管理が実現可能です。詳細は公式ドキュメント参照を推奨します。

---

### 79. Generally Available: Microsoft Python driver for SQL Server 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Microsoft Python driver for SQL Server ](https://azure.microsoft.com/updates?id=522581)

**アップデートID**: 522581
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure SQL Database

**要約**:

- 何が更新されたか  
MicrosoftのPython向けSQL Serverドライバー（mssql-python）がGA（一般提供）となりました。

- 主な変更点や新機能  
高性能かつ開発者に優しい設計で、SQL ServerやAzure SQL Databaseとの接続・操作が容易に。最新のPython環境に対応し、安定性とパフォーマンスが向上。

- 影響を受ける対象  
PythonでSQL ServerやAzure SQL Databaseを利用する開発者。

- 注意点  
既存のドライバーからの移行時はAPIの互換性を確認し、最新ドキュメントを参照してください。

**詳細**:

Microsoftは、Python開発者向けのSQL Serverドライバー「mssql-python」を一般提供（GA）開始しました。本ドライバーは、SQL ServerおよびAzure SQL Databaseとの接続を最適化し、高性能かつモダンなAPIを提供することを目的としています。従来のODBCベースのドライバーに比べ、非同期処理や最新のPython標準に準拠した設計が特徴です。実装はC言語ベースの高速なネイティブ拡張を用い、DB接続、クエリ実行、トランザクション管理を効率化しています。活用例としては、Pythonアプリケーションからのデータ取得・更新、自動化スクリプト、機械学習パイプラインのデータ連携などが挙げられます。注意点としては、現時点での対応Pythonバージョンや一部のSQL Server機能（例：特定の認証方式や拡張機能）に制限があるため、公式ドキュメントで互換性を確認する必要があります。Azure Data FactoryやAzure Functionsとの連携により、サーバーレス環境やETL処理での利用も容易です。詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=522581）を参照してください。

---

### 80. Generally Available: New SQL Server migration in Azure Arc 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: New SQL Server migration in Azure Arc ](https://azure.microsoft.com/updates?id=522572)

**アップデートID**: 522572
**情報源**: Azure Updates API

**カテゴリ**: Launched, Hybrid + multicloud, Azure Arc

**要約**:

- 何が更新されたか  
Azure Arc対応の新しいSQL Server移行ソリューションが一般提供開始。

- 主な変更点や新機能  
Azure Database Migration ServiceとCopilotを活用し、Azure SQL Managed Instanceへの自動化されたエンドツーエンド移行を実現。

- 影響を受ける対象  
オンプレミスや他クラウドのSQL ServerをAzure SQL Managed Instanceへ移行する技術者。

- 注意点  
移行前の環境評価やネットワーク設定を適切に行う必要がある。  

https://azure.microsoft.com/updates?id=522572

**詳細**:

本アップデートは、Azure Arc環境におけるSQL ServerのAzure SQL Managed Instanceへの移行を効率化することを目的としています。従来の移行作業は複雑かつ手動工程が多かったため、Azure Database Migration Service（DMS）とCopilotの支援により、エンドツーエンドで自動化された移行プロセスを提供します。具体的には、オンプレミスや他クラウドのSQL ServerをAzure Arc対応環境に登録し、DMSがデータベースのスキーマやデータの移行を管理、Copilotが移行計画の最適化やトラブルシューティングを支援します。これにより、移行時間の短縮と人的ミスの低減が実現可能です。活用シナリオとしては、ハイブリッド環境での段階的クラウド移行や、法規制によりデータを特定地域に保持しつつクラウド管理を行うケースが挙げられます。注意点として、移行対象のSQL Serverバージョンや構成によっては一部機能が制限される場合があり、事前の互換性検証が推奨されます。また、Azure Arc、Azure SQL Managed Instance、Azure Database Migration Serviceとの密接な連携が必須であり、各サービスの権限設定やネットワーク構成にも留意が必要です。詳細は公式ドキュメントを参照し、環境に応じた最適な移行計画を策定してください。

---

### 81. Generally Availabe: SQL Server 2025 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Availabe: SQL Server 2025 ](https://azure.microsoft.com/updates?id=522559)

**アップデートID**: 522559
**情報源**: Azure Updates API

**カテゴリ**: Launched

**要約**:

- 何が更新されたか  
SQL Server 2025が一般提供開始されました。

- 主な変更点や新機能  
AI対応の組み込み機能を搭載し、Microsoft Fabricとのシームレスな統合を実現。エンタープライズ向けデータプラットフォームの近代化を推進します。

- 影響を受ける対象  
エンタープライズ環境でSQL Serverを利用する開発者・DBA。

- 注意点があれば記載  
既存環境との互換性やAI機能の活用方法を事前に検証することを推奨します。

情報源: https://azure.microsoft.com/updates?id=522559

**詳細**:

MicrosoftはSQL Server 2025を一般提供開始し、エンタープライズ向けデータプラットフォームの近代化を推進しています。本バージョンはAI対応を大幅に強化し、組み込みのAI機能をネイティブに搭載。これにより、機械学習モデルのトレーニングや推論をSQL Server内部で直接実行可能となり、データ移動のオーバーヘッドを削減します。Microsoft Fabricとのシームレスな統合により、クラウドとオンプレミスのハイブリッド環境でのデータ連携が容易です。技術的には、拡張されたT-SQL関数群や新たなAI推論エンジンを備え、PythonやRのスクリプト実行も強化。これにより、リアルタイム分析や予測分析の高速化が実現します。活用例としては、顧客行動分析や異常検知、需要予測などが挙げられます。一方、AIモデルのリソース消費やセキュリティ設定には注意が必要で、適切な権限管理とパフォーマンス監視が推奨されます。Azure SynapseやAzure Machine Learningとの連携により、エンドツーエンドのデータ分析パイプライン構築が可能で、柔軟かつ拡張性の高い運用が期待されます。

---

### 82. Generally Available: Azure SQL updates for November 2025 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure SQL updates for November 2025 ](https://azure.microsoft.com/updates?id=522523)

**アップデートID**: 522523
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance

**要約**:

- 何が更新されたか  
2025年11月にAzure SQLのGeneral Purpose層のゾーン冗長Azure SQL Managed Instanceに対し、1年または3年の予約割引が標準コンピュートに適用可能になりました。

- 主な変更点や新機能  
ゾーン冗長構成のManaged Instanceで予約インスタンス割引が利用でき、コスト最適化が可能に。

- 影響を受ける対象  
Azure SQL Managed InstanceのGeneral Purpose層をゾーン冗長で利用するユーザー。

- 注意点があれば記載  
予約期間は1年または3年のみ適用可能で、割引は標準コンピュートに限定されます。

**詳細**:

2025年11月のAzure SQLアップデートでは、ゾーン冗長構成のAzure SQL Managed Instance（General Purpose層）に対し、1年または3年の予約インスタンス割引が標準コンピューティングとストレージ両方に適用可能となりました。背景には、可用性向上を図るゾーン冗長インスタンスのコスト最適化ニーズがあり、長期利用者のTCO削減を目的としています。技術的には、予約インスタンス購入時にゾーン冗長のGeneral Purpose層を選択し、割引が自動的に標準コンピューティングおよびストレージリソースに反映されます。これにより、災害対策を考慮した高可用性構成をコスト効率良く運用可能です。活用例としては、複数リージョンでの業務継続計画（BCP）やミッションクリティカルなアプリケーションの冗長化に最適です。注意点として、予約割引はゾーン冗長General Purpose層に限定され、他の層や単一ゾーン構成には適用されません。また、予約期間中の構成変更は割引適用に影響する可能性があります。関連サービスとしては、Azure Monitorによるパフォーマンス監視やAzure Backupとの連携で運用管理を強化可能です。詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=522523）を参照してください。

---

### 83. Public Preview: Azure SQL updates for November 2025 

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Azure SQL updates for November 2025 ](https://azure.microsoft.com/updates?id=522514)

**アップデートID**: 522514
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance

**要約**:

- 何が更新されたか  
Azure SQLのMSSQL拡張機能において、Visual Studio Code上で対話的にデータの閲覧・編集・挿入が可能に。

- 主な変更点や新機能  
T-SQLコードを手動で書かずに、Edit Dataインターフェースからテーブル操作ができるようになった。

- 影響を受ける対象  
Azure SQLをVS CodeのMSSQL拡張で操作する開発者。

- 注意点があれば記載  
現在パブリックプレビュー段階のため、本番環境での使用は慎重に。  

詳細：https://azure.microsoft.com/updates?id=522514

**詳細**:

2025年11月のAzure SQLアップデートでは、Visual Studio CodeのMSSQL拡張機能において、対話型の「Edit Data」インターフェースがパブリックプレビューとして提供開始されました。これにより、従来はT-SQLコードを手動で記述していたテーブルの行の閲覧・編集・挿入操作が、GUI上で直感的に行えるようになりました。技術的には、VS Codeの拡張機能がAzure SQL Databaseと直接通信し、リアルタイムでデータ操作を反映する仕組みを採用しています。これにより、開発者はSQL文の知識が浅くても効率的にデータ管理が可能となり、データベース開発やデバッグの生産性が向上します。活用例としては、クエリ結果の即時編集やテストデータの投入、運用中のデータ修正作業が挙げられます。一方で、複雑なトランザクション制御や大量データの一括更新には向かず、GUI操作のため誤操作に注意が必要です。また、Azure SQL DatabaseやManaged Instanceとの連携が前提であり、適切な接続権限が必要です。本機能はAzureの他サービスと連携しやすく、例えばAzure DevOpsのCI/CDパイプラインでのデータ検証にも活用可能です。詳細は公式ドキュメントを参照してください。

---

### 84. Public Preview: Dynamic sessions shell environment and MCP support in Azure Container Apps

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Dynamic sessions shell environment and MCP support in Azure Container Apps](https://azure.microsoft.com/updates?id=512949)

**アップデートID**: 512949
**情報源**: Azure Updates API

**カテゴリ**: In preview, Containers, Azure Container Apps, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Container Appsで動的シェルセッション機能とMCP（Managed Control Plane）サポートがパブリックプレビューで提供開始。

- 主な変更点や新機能  
プラットフォーム管理のコンテナ内でシェルコマンドを隔離環境で実行可能に。デバッグや運用作業が容易に。

- 影響を受ける対象  
Azure Container Appsを利用する開発者・運用者。

- 注意点があれば記載  
プレビュー機能のため本番環境での使用は慎重に。今後のアップデートにより仕様変更の可能性あり。

**詳細**:

本アップデートは、Azure Container Appsにおける開発・運用効率向上を目的に、動的シェルセッション機能とMCP（Managed Control Plane）サポートをパブリックプレビューで提供開始したものです。動的シェルセッションは、プラットフォーム管理下の組み込みコンテナとして起動し、隔離されたサンドボックス環境内で標準的なシェルコマンドを実行可能にします。これにより、ユーザーは既存のコンテナアプリケーションに影響を与えずにリアルタイムでトラブルシューティングや設定変更が行えます。技術的には、Azure Container Appsのコントロールプレーンが動的にシェルコンテナを生成・管理し、Kubernetesベースの基盤上でセキュアに実行。MCPサポートにより制御面の管理が強化され、運用の一元化が図れます。活用例としては、アプリケーションのデバッグ、ログ確認、環境変数の動的変更などが挙げられます。注意点としては、プレビュー機能のため一部制限や将来的な仕様変更があり得ること、またシェルセッションは一時的な用途に限定される点が挙げられます。Azure MonitorやAzure DevOpsとの連携により、シェルセッションでの操作ログ取得やCI/CDパイプラインへの組み込みも可能で、運用自動化の幅が広がります。

---

### 85. Public Preview: Deployment labels in Azure Container Apps

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: Deployment labels in Azure Container Apps](https://azure.microsoft.com/updates?id=512900)

**アップデートID**: 512900
**情報源**: Azure Updates API

**カテゴリ**: In preview, Containers, Azure Container Apps, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Container Appsで「デプロイメントラベル」機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
デプロイメントに意味のあるラベルを付与可能になり、環境管理が容易に。高度なデプロイ戦略（例：ブルーグリーン、カナリア）を実装しやすくなる。

- 影響を受ける対象  
Azure Container Appsを利用している開発者や運用チーム。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に。今後仕様変更の可能性あり。

**詳細**:

Azure Container Appsにおける「Deployment labels」機能がパブリックプレビューとして提供開始されました。本機能は、従来のデプロイメント管理を簡素化し、環境ごとの識別や高度なデプロイ戦略を実現するために導入されました。具体的には、デプロイメントに対して任意のラベル（キー・バリュー形式）を付与可能となり、これにより複数環境（開発・検証・本番など）やバージョン管理を容易に行えます。技術的には、Azure Container AppsのAPIおよびCLIでラベル指定が可能で、ラベルによるフィルタリングやロールバック操作が効率化されます。活用例として、ブルーグリーンデプロイやカナリアリリース時に特定ラベルを用いてトラフィック制御やモニタリング対象を限定することが挙げられます。注意点として、現時点ではプレビュー機能のため、ラベルの付与上限や互換性に制限がある可能性があり、運用前にドキュメント確認が推奨されます。さらに、Azure MonitorやAzure DevOpsとの連携により、ラベル情報を活用したCI/CDパイプラインの自動化やログ分析が可能となり、運用効率向上に寄与します。詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=512900）を参照ください。

---

### 86. Generally Available: Rule-based routing in Azure Container Apps

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Rule-based routing in Azure Container Apps](https://azure.microsoft.com/updates?id=512850)

**アップデートID**: 512850
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Container Apps, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Container Appsでルールベースのルーティング機能がGA（一般提供）となりました。

- 主な変更点や新機能  
トラフィックの振り分けを柔軟に設定可能となり、マイクロサービスの構成やA/Bテスト、ブルーグリーンデプロイが容易に実現できます。

- 影響を受ける対象  
Azure Container Appsを利用する開発者や運用者。

- 注意点があれば記載  
既存のルーティング設定との互換性や設定ミスによるトラフィック制御の影響に注意が必要です。

**詳細**:

Azure Container Appsにおけるルールベースルーティング機能がGA（一般提供）となりました。本機能はマイクロサービス構成のアプリケーションにおいて、トラフィックの振り分けを柔軟かつ簡潔に実現することを目的としています。具体的には、HTTPリクエストのヘッダーやパス、クエリパラメータに基づき、異なるバージョンや環境のコンテナ間でトラフィックを分割可能です。これにより、A/Bテストやブルーグリーンデプロイメントの実装が容易になります。技術的には、Azure Container AppsのIngress設定内でルーティングルールをYAMLまたはAzure CLIを用いて定義し、トラフィック管理を行います。例えば、特定のユーザーグループに新機能を段階的に展開する際に有効です。注意点として、ルール数や複雑度に制限があり、過度なルール設定はパフォーマンスに影響を与える可能性があります。また、Azure Front DoorやApplication Gatewayと連携することで、より高度なグローバル負荷分散やセキュリティ機能と組み合わせた運用が可能です。詳細は公式ドキュメントを参照してください。

---

### 87. Generally Available: Premium Ingress in Azure Container Apps

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Premium Ingress in Azure Container Apps](https://azure.microsoft.com/updates?id=512813)

**アップデートID**: 512813
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Container Apps, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Container AppsのプレミアムIngress機能が一般提供（GA）となりました。

- 主な変更点や新機能  
環境単位でのIngress設定が可能になり、特にカスタマイズ可能なIngressスケーリングをサポート。トラフィック増減に応じた柔軟なスケールアウトが可能です。

- 影響を受ける対象  
Azure Container Appsを利用し、Ingressのスケーリングやトラフィック管理を高度化したい開発者・運用者。

- 注意点  
既存のIngress設定からの移行やスケーリング挙動の理解が必要です。環境単位の設定変更が全アプリに影響するため慎重な運用が求められます。

**詳細**:

Azure Container AppsにおけるプレミアムIngress機能が一般提供（GA）となりました。本アップデートは、環境単位でのIngress設定を可能にし、特にカスタマイズ可能なIngressスケーリングを実現することを目的としています。従来のIngressはアプリ単位の設定が中心でしたが、環境レベルでの統合管理により、複数アプリのトラフィックを効率的に制御可能です。技術的には、環境ごとにIngressのスケールアウト/スケールインポリシーを設定でき、トラフィック負荷に応じた柔軟なリソース割当てが可能です。実装はAzure PortalやCLIで環境設定を行い、Ingressのスケーリングパラメータ（最大・最小レプリカ数、CPU/メモリ使用率閾値など）を指定します。活用例としては、複数のマイクロサービスを含むContainer Apps環境でのトラフィック集中時の自動スケールや、ピーク時の安定稼働確保が挙げられます。注意点として、プレミアムIngressは追加コストが発生し、環境単位の設定がアプリ単位の細かな制御を制限する場合があるため、設計段階での検討が必要です。Azure Front DoorやApplication Gatewayとの連携も可能で、グローバル負荷分散やWAF機能と組み合わせることでセキュアかつ高可用性なアプリケーション配信が実現します。

---

### 88. Public Preview: JWT Validation in Azure Application Gateway

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Public Preview: JWT Validation in Azure Application Gateway](https://azure.microsoft.com/updates?id=489855)

**アップデートID**: 489855
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Application Gateway, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Application GatewayでJWT（JSON Web Token）検証機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
トラフィックがバックエンドに到達する前に、Application Gateway上で認証とトークン検証を実施可能に。APIやアプリケーションのセキュリティ強化が可能。

- 影響を受ける対象  
Azure Application Gatewayを利用しAPIやWebアプリを保護する開発者・運用者。

- 注意点があれば記載  
プレビュー機能のため、本番環境での使用は慎重に。設定ミスによるアクセス障害に注意。

**詳細**:

Azure Application GatewayにおけるJWT（JSON Web Token）検証機能のパブリックプレビューが開始されました。本機能は、アプリケーションゲートウェイレベルでJWTの認証およびトークン検証を実施し、バックエンドのAPIやアプリケーションに到達する前に不正なトークンを遮断することを目的としています。これにより、セキュリティ強化とバックエンド負荷の軽減が可能です。具体的には、Application GatewayのWAF（Web Application Firewall）ポリシーにJWT検証ルールを設定し、Issuer、Audience、署名キー、トークンの有効期限などを検証します。実装はAzure Portal、CLI、ARMテンプレートで設定可能で、OIDCプロバイダーからの公開鍵を利用した署名検証をサポートします。活用例としては、API管理前段での認証強化やマイクロサービス間のトークン検証が挙げられます。注意点としては、現時点でのプレビュー版であり、対応するトークン形式や暗号アルゴリズムに制限があるほか、複雑なカスタム認証フローには対応していない点が挙げられます。Azure ADやAzure API Managementとの連携により、より高度な認証・認可シナリオの構築が可能です。詳細は公式ドキュメントを参照してください。

---

### 89. Generally Available: Azure Application Gateway mTLS passthrough support

**公開日時**: 2025年11月18日 17:01:02 UTC
**リンク**: [Generally Available: Azure Application Gateway mTLS passthrough support](https://azure.microsoft.com/updates?id=488990)

**アップデートID**: 488990
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Application Gateway, Features, Services, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Application GatewayがmTLSパススルーをGA対応し、バックエンドでのクライアント証明書と認証ヘッダーの検証を可能に。

- 主な変更点や新機能  
Web Application Firewall(WAF)によるトラフィック検査を維持しつつ、バックエンドでのmTLS認証処理をサポート。

- 影響を受ける対象  
mTLS認証を用いるアプリケーションをAzure Application Gateway経由で運用する技術者。

- 注意点があれば記載  
バックエンドでの証明書検証を行うため、適切な証明書管理とWAF設定の理解が必要。  

情報源: https://azure.microsoft.com/updates?id=488990

**詳細**:

本アップデートは、Azure Application GatewayにおけるmTLS（相互TLS）パススルー機能の一般提供開始を告知するものです。従来、Application GatewayのWeb Application Firewall（WAF）を介したトラフィック検査と、バックエンドでのクライアント証明書検証は両立が困難でした。本機能により、クライアント証明書およびAuthorizationヘッダーの検証をバックエンドアプリケーション側で行いつつ、WAFによるHTTPトラフィックの検査を継続可能となります。

技術的には、Application GatewayがTLS終端を行わずにTLSトラフィックをそのままバックエンドに転送（パススルー）し、バックエンドでmTLSハンドシェイクを完結させます。一方で、WAFはトラフィックのメタデータやヘッダー情報を解析し、セキュリティポリシーを適用します。これにより、セキュリティ強化と柔軟な認証処理の両立が実現します。

活用シナリオとしては、金融や医療など高セキュリティを要求する業界で、クライアント証明書による厳格な認証が必須かつWAFによる攻撃防御も必要なケースが想定されます。実装時は、バックエンドアプリケーションがmTLS対応であること、Application Gatewayの設定でmTLSパススルーを有効化する必要があります。

注意点として、パススルー設定時はApplication GatewayでのTLS終端が行われないため、SSLポリシーや証明書管理はバックエンド側に委ねられます。また、WAFの検査機能は限定的になるため、ポリシー設計に注意が必要です。

関連サービスとしては、Azure Key Vaultによる証明書管理、Azure Monitorでのログ監視、Azure Front Doorとの組み合わせによるグローバル負荷分散などが挙げられます。これらと連携することで、より堅牢かつ運用性の高いセキュリティアーキテクチャを構築可能です。

---

### 90. Public Preview: Azure Copilot observability agent

**公開日時**: 2025年11月18日 16:30:36 UTC
**リンク**: [Public Preview: Azure Copilot observability agent](https://azure.microsoft.com/updates?id=528538)

**アップデートID**: 528538
**情報源**: Azure Updates API

**カテゴリ**: In preview, DevOps, Management and governance, Azure Monitor

**要約**:

- 何が更新されたか  
Azure Copilot observability agentがパブリックプレビューで提供開始。

- 主な変更点や新機能  
リソース全体にわたるインテリジェントな監視を実現し、異常検知時に具体的な改善アクションを提示。従来のリアクティブなトラブルシューティングを超えた高度な可観測性を提供。

- 影響を受ける対象  
クラウド運用担当者やSRE、DevOpsエンジニアが主な利用者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討が必要。最新のドキュメントを参照し適切に設定を行うこと。

**詳細**:

Azure Copilot observability agentは、クラウド運用における従来のリアクティブなトラブルシューティングを超え、リソース全体にスケール可能なインテリジェントな可観測性を提供することを目的としたパブリックプレビュー機能です。本エージェントは、Azureリソースのパフォーマンス低下や異常検知時に自動的にデータ収集と分析を行い、具体的な改善アクションを提示します。技術的には、エージェントが各リソースにデプロイされ、ログ・メトリクス・トレース情報を統合的に収集し、Azure MonitorやAzure AIサービスと連携してリアルタイム分析を実現します。活用シナリオとしては、複数サービス間の依存関係分析やパフォーマンスボトルネックの特定、運用自動化のトリガー生成が挙げられます。注意点としては、現時点で対応リソースが限定的であり、パブリックプレビューのため機能変更の可能性がある点に留意が必要です。Azure Monitor、Azure Log Analytics、Azure AIと密接に連携し、既存の監視基盤に高度なインサイトを付加する形で導入可能です。

---

### 91. Private Preview: ActiveMQ and JMS connector for Azure Logic Apps

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Private Preview: ActiveMQ and JMS connector for Azure Logic Apps](https://azure.microsoft.com/updates?id=531783)

**アップデートID**: 531783
**情報源**: Azure Updates API

**カテゴリ**: In development, Integration, Internet of Things, Logic Apps

**要約**:

- 何が更新されたか  
Azure Logic AppsにActiveMQおよびJMSコネクタのプライベートプレビューが追加されました。

- 主な変更点や新機能  
ActiveMQ/JMSベースのエンタープライズメッセージングシステムと連携可能となり、複雑なハイブリッド統合シナリオを実現します。

- 影響を受ける対象  
Logic Appsを用いたメッセージング連携やハイブリッド統合を行う開発者・運用者。

- 注意点  
現時点はプライベートプレビューのため、利用には申請が必要であり、機能や仕様が変更される可能性があります。

**詳細**:

本アップデートは、Azure Logic AppsにおけるActiveMQおよびJMSコネクタのプライベートプレビュー開始を告知するものです。背景として、オンプレミスやクラウドの既存エンタープライズメッセージング基盤（ActiveMQ/JMS）とAzureの統合ニーズが高まっていることが挙げられます。今回のコネクタにより、Logic Appsから直接ActiveMQブローカーやJMSキュー/トピックへメッセージの送受信が可能となり、複雑なハイブリッド統合シナリオを実現します。技術的には、JMSプロトコルに準拠したメッセージングAPIをLogic Appsのワークフロー内で利用でき、接続設定にはActiveMQの接続文字列や認証情報を指定します。活用例としては、オンプレミスのActiveMQを介したイベント駆動型処理や、複数システム間の非同期メッセージ連携が挙げられます。現時点ではプライベートプレビューのため、利用には申請が必要で、機能制限やサポート範囲の限定がある点に注意が必要です。なお、Azure Service BusやEvent Gridなど他のメッセージングサービスとも組み合わせることで、より柔軟なハイブリッド連携基盤を構築可能です。詳細は公式ドキュメントおよびプレビュー参加申請ページを参照してください。

---

### 92. Public Preview: New healthcare connectors for Azure Logic Apps

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: New healthcare connectors for Azure Logic Apps](https://azure.microsoft.com/updates?id=531778)

**アップデートID**: 531778
**情報源**: Azure Updates API

**カテゴリ**: In preview, Integration, Internet of Things, Logic Apps

**要約**:

- 何が更新されたか  
Azure Logic Appsに新しい医療向けコネクタがパブリックプレビューで追加されました。

- 主な変更点や新機能  
HL7コネクタをはじめとする複数の医療データ連携用コネクタが提供され、HL7メッセージのシームレスな交換が可能に。

- 影響を受ける対象  
医療システムの統合やヘルスケアデータ連携を行う開発者・システムインテグレーター。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討してください。

**詳細**:

本アップデートは、Azure Logic Appsに新たな医療分野向けコネクタを追加し、医療データの相互運用性を強化することを目的としています。公開プレビューとして提供されるHL7コネクタは、医療機関間で広く利用されるHL7メッセージの送受信を容易にし、既存の医療システムとのシームレスな連携を実現します。技術的には、Logic Appsのワークフロー内でHL7メッセージのパースや生成を行い、FHIRやDICOMなど他の医療標準フォーマットとの変換もサポート可能です。実装はLogic Appsのデザイナーを用いてコネクタをドラッグ＆ドロップで組み込み、API接続設定を行うだけで開始できます。活用例としては、病院の電子カルテシステムと保険会社のシステム間での患者情報交換や検査結果の自動連携が挙げられます。注意点としては、プレビュー段階のため一部機能が限定的であり、メッセージのカスタム拡張には追加設定が必要です。Azure API ManagementやEvent Gridとの連携により、より高度な監視やイベント駆動型処理も可能となっています。これにより、医療機関のデジタルトランスフォーメーションを加速させる実用的なツールとして期待されます。

---

### 93. Generally Available: Scheduled Actions 

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Scheduled Actions ](https://azure.microsoft.com/updates?id=530797)

**アップデートID**: 530797
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Virtual Machines

**要約**:

- 何が更新されたか  
Azureの「Scheduled Actions」が一般提供（GA）となり、VMのライフサイクル管理を大規模かつ定期的に自動化可能に。

- 主な変更点や新機能  
サブスクリプションのスロットリングや一時的なエラーによるリトライを自動処理し、運用負荷を軽減。

- 影響を受ける対象  
大量のVMを運用するAzureユーザーや自動化を推進する技術者。

- 注意点  
スケジュール設定時の権限管理やリトライ動作の理解が重要。  

情報源: https://azure.microsoft.com/updates?id=530797

**詳細**:

AzureのScheduled Actions機能は、大規模なVMのライフサイクル管理を定期的に自動化するために開発されました。従来、複数VMの起動・停止やスケール操作を手動やスクリプトで実施する際、サブスクリプションのスロットリングや一時的なエラー対応が課題でした。本機能はこれらを自動的に処理し、再試行や負荷分散を組み込み、運用負荷を大幅に軽減します。具体的には、AzureポータルやAPIからスケジュールを設定し、指定時間にVMの起動・停止、スケール操作を実行可能です。内部的には、Azure Resource ManagerのAPI呼び出しを管理し、サブスクリプションの制限に応じてリクエストを調整、失敗時は自動リトライを行います。活用例としては、開発環境の夜間停止や週末のコスト削減、定期的なスケールアップダウンによるリソース最適化が挙げられます。注意点としては、スケジュール設定時にタイムゾーンや依存関係を考慮する必要があり、複雑なワークフローにはAzure AutomationやLogic Appsとの併用が推奨されます。関連サービスとしては、Azure Monitorのアラート連携やAzure Policyによるガバナンス強化と組み合わせることで、より堅牢な運用が可能です。詳細は公式ドキュメント（https://azure.microsoft.com/updates?id=530797）を参照してください。

---

### 94. Generally Available: Microsoft Marketplace

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Microsoft Marketplace](https://azure.microsoft.com/updates?id=530614)

**アップデートID**: 530614
**情報源**: Azure Updates API

**カテゴリ**: Launched

**要約**:

- 何が更新されたか  
Microsoft Marketplaceが米国に続きグローバル展開され、正式に一般提供（GA）となりました。

- 主な変更点や新機能  
従来のAzure MarketplaceおよびAppSourceからの全トラフィックがMicrosoft Marketplaceへリダイレクトされ、一元化されたクラウドソリューションやAIアプリの提供が強化されました。

- 影響を受ける対象  
Azure利用者、ISV、クラウドソリューション開発者が対象で、マーケットプレイスの利用環境が統合されます。

- 注意点  
従来のストアフロントは廃止されるため、リンクやAPIの更新対応が必要です。

**詳細**:

Microsoft Marketplaceが米国でのローンチを経てグローバル展開され、従来のAzure MarketplaceおよびAppSourceのトラフィックはすべて新Marketplaceへリダイレクトされる形に統合されました。本アップデートの目的は、クラウドソリューションやAIアプリ、エージェントの発見・導入を一元化し、ユーザー体験の向上と管理の効率化を図ることにあります。新Marketplaceは統合されたUI/UXを提供し、検索機能の強化やフィルタリング、サブスクリプション管理の簡素化が特徴です。技術的には、REST APIを介したサービス連携やAzure Active Directory認証によるセキュアなアクセス管理が実装されており、CI/CDパイプラインへの組み込みも可能です。活用例としては、DevOpsチームが必要なソリューションを迅速に導入し、AIモデルやエージェントをAzure環境にシームレスに展開するケースが挙げられます。注意点としては、旧MarketplaceのURLが廃止されるため、既存のリンクやスクリプトの更新が必要です。また、提供されるソリューションの互換性やサポート範囲を事前に確認することが推奨されます。Azure Logic AppsやAzure Kubernetes Service（AKS）などとの連携により、Marketplaceから導入したアプリケーションを自動化・スケールさせることが可能です。

---

### 95. Generally Available: Resale enabled offers through Microsoft Marketplace  

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Resale enabled offers through Microsoft Marketplace  ](https://azure.microsoft.com/updates?id=530593)

**アップデートID**: 530593
**情報源**: Azure Updates API

**カテゴリ**: Launched, Microsoft Ignite, Features

**要約**:

- 何が更新されたか  
Microsoft Marketplaceで「再販対応オファー」が一般提供開始されました。

- 主な変更点や新機能  
チャネルパートナーがAzure向けソフトウェアを再販可能になり、販売ルートの拡大と顧客への柔軟な提供が可能に。

- 影響を受ける対象  
AzureのISV、チャネルパートナー、商用顧客。

- 注意点があれば記載  
再販対応オファーの利用にはMicrosoftの認定と適切な契約が必要です。

情報源: https://azure.microsoft.com/updates?id=530593

**詳細**:

本アップデートは、Microsoft Marketplaceにおけるチャネルパートナー経由の販売促進を目的に、Resale Enabled Offers（再販対応オファー）の一般提供を開始したものです。これにより、ISVやソフトウェアプロバイダーは、Azure Marketplace上で販売する製品をパートナーが再販可能な形で公開でき、パートナーは顧客への一括請求や契約管理を容易に行えます。技術的には、Azure Marketplaceのオファー作成時に「Resale Enabled」オプションを選択し、パートナーIDの紐付けや価格設定を行うことで実装されます。これにより、パートナーは自身の顧客に対してAzureリソースとソフトウェアを統合した請求を提供可能です。活用例としては、マネージドサービスプロバイダーが自社サービスとISV製品を組み合わせて販売し、単一請求書で管理するケースが挙げられます。注意点として、再販対応オファーはMicrosoftの承認プロセスを経る必要があり、価格設定や契約条件に制約があるため、事前の確認が必要です。また、Azure Cost ManagementやAzure ADと連携し、利用状況の可視化やアクセス制御を強化できます。これにより、チャネルパートナーのビジネス拡大と顧客管理の効率化が実現します。

---

### 96. Public Preview: GitHub Copilot app modernization expanded capabilities

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: GitHub Copilot app modernization expanded capabilities](https://azure.microsoft.com/updates?id=530257)

**アップデートID**: 530257
**情報源**: Azure Updates API

**カテゴリ**: In preview, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
GitHub Copilot App Modernizationの機能拡張がパブリックプレビューで提供開始。

- 主な変更点や新機能  
アプリケーション、データベース、コンテナのモダナイズ支援が強化され、Azureへの移行がより迅速かつ容易に。

- 影響を受ける対象  
Azureへ移行・モダナイズを検討する開発者や運用エンジニア。

- 注意点があれば記載  
現段階はパブリックプレビューのため、本番環境での利用は慎重に検討を。今後のアップデートに注目。

**詳細**:

本アップデートは、GitHub Copilot App Modernizationのパブリックプレビュー拡張機能を提供し、アプリケーションやデータベース、コンテナのモダナイゼーションおよびAzureへの移行を効率化することを目的としています。主な新機能として、コード解析によるレガシーコードのモダナイゼーション提案、コンテナイメージの最適化支援、データベーススキーマの変換アシストが追加されました。技術的には、GitHub CopilotのAIモデルを活用し、リポジトリ内コードや構成ファイルを解析、Azureのマイグレーションツールと連携して自動変換案を提示します。活用シナリオとしては、既存のオンプレミスアプリケーションのクラウド移行、マイクロサービス化、コンテナ化が挙げられ、開発者は提案されたコード修正や構成変更をレビュー・適用するだけで効率的にモダナイゼーションが可能です。注意点としては、現状プレビュー段階のため全ての言語やフレームワークに対応しておらず、複雑な依存関係の解析には手動調整が必要な場合があります。関連サービスとしてAzure Migrate、Azure Database Migration Service、Azure Kubernetes Service（AKS）との連携が強化されており、これらと組み合わせることで移行プロセス全体の自動化と最適化が実現します。

---

### 97. Public Preview: Industry-leading storage performance Ebsv6 VM series

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Industry-leading storage performance Ebsv6 VM series](https://azure.microsoft.com/updates?id=529416)

**アップデートID**: 529416
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Virtual Machines

**要約**:

- 何が更新されたか  
AzureのEbsv6 VMシリーズがパブリックプレビューとして公開されました。

- 主な変更点や新機能  
第5世代Intel Xeonプロセッサ搭載で、最大80万IOPS・14GB/sのリモートディスクストレージスループットを実現し、業界最高クラスのストレージ性能を提供します。

- 影響を受ける対象  
高性能ストレージを必要とするアプリケーションやワークロードを運用する技術者。

- 注意点があれば記載  
プレビュー段階のため、本番環境での利用は慎重に検討してください。詳細は公式ドキュメントを参照してください。

**詳細**:

本アップデートは、5世代目Intel® Xeon®プロセッサ搭載のEbsv6 VMシリーズのパブリックプレビュー開始を告知するものです。Ebsv6およびEbdsv6 VMは、最大80万IOPS、14GB/sのリモートディスクストレージスループットを実現し、業界最高水準のストレージ性能を提供します。これにより、大規模データベース、高性能分析、トランザクション処理などI/O集約型ワークロードの処理能力が大幅に向上します。技術的には、最新のIntel Xeonプロセッサと高速NVMeベースのEBS（Elastic Block Storage）を組み合わせ、低レイテンシかつ高スループットを実現。VMサイズは多様な構成が用意され、柔軟なリソース割当が可能です。活用例としては、リアルタイムビッグデータ解析、金融取引プラットフォーム、機械学習トレーニング環境などが挙げられます。注意点としては、現段階がパブリックプレビューであるため、SLAsが正式提供されていない点や、特定リージョンでの利用制限があることに留意が必要です。Azure Blob StorageやAzure NetApp Filesなどの高性能ストレージサービスと組み合わせることで、さらに最適なデータ処理環境を構築可能です。詳細は公式ドキュメントを参照してください。

---

### 98. Public Preview: User and group quota reports in Azure NetApp Files 

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: User and group quota reports in Azure NetApp Files ](https://azure.microsoft.com/updates?id=528899)

**アップデートID**: 528899
**情報源**: Azure Updates API

**カテゴリ**: In development, Storage, Azure NetApp Files

**要約**:

- 何が更新されたか  
Azure NetApp Filesでユーザーおよびグループのクォータレポート機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
NFS、SMB、デュアルプロトコルボリュームの個別ユーザー・グループクォータの使用状況や制限を可視化可能に。

- 影響を受ける対象  
Azure NetApp Filesでクォータ管理を行う組織や技術者。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討が必要。

**詳細**:

Azure NetApp Filesのパブリックプレビューとして提供される「ユーザーおよびグループクォータレポート」機能は、NFS、SMB、デュアルプロトコルボリュームにおける個別ユーザー・グループの容量管理を強化する目的で導入されました。本機能は、各ユーザーやグループのクォータ上限、使用容量、残容量などの詳細なメトリクスを可視化し、容量管理の透明性と効率性を向上させます。技術的には、Azure NetApp Filesのクォータ管理APIと連携し、定期的にクォータ情報を収集・集約、AzureポータルやAPI経由でレポートを提供します。これにより、ストレージ管理者は特定ユーザーやグループの容量超過リスクを早期に検知し、適切な容量割当てやポリシー調整が可能です。活用シナリオとしては、大規模組織での部門別容量管理や、開発環境におけるユーザー単位のリソース制限が挙げられます。注意点としては、現時点でパブリックプレビュー段階のため、機能の安定性やAPI仕様が変更される可能性があり、商用環境での利用は慎重に検討する必要があります。また、Azure MonitorやAzure Policyと連携することで、クォータ超過時のアラート設定や自動対応の実装が可能です。詳細は公式ドキュメントおよびアップデートページ（https://azure.microsoft.com/updates?id=528899）を参照してください。

---

### 99. Generally Available: New Hybrid Integration Connectors for Azure Logic Apps

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: New Hybrid Integration Connectors for Azure Logic Apps](https://azure.microsoft.com/updates?id=527683)

**アップデートID**: 527683
**情報源**: Azure Updates API

**カテゴリ**: Launched, Integration, Internet of Things, Logic Apps

**要約**:

- 何が更新されたか  
Azure Logic Appsに新しいハイブリッド統合コネクタが一般提供開始されました。

- 主な変更点や新機能  
Confluent Kafkaコネクタが追加され、Logic AppsからConfluent Cloudへのイベントストリーミング連携が可能に。

- 影響を受ける対象  
ハイブリッド環境でイベント駆動型アプリケーションを構築する開発者や運用者。

- 注意点  
既存のLogic Apps環境でのコネクタ利用時は接続設定や認証情報の確認が必要です。

**詳細**:

本アップデートは、Azure Logic Appsのハイブリッド統合機能を強化するため、新たなコネクタ群を一般提供（GA）したものです。特にConfluent Kafkaコネクタが追加され、Logic AppsからConfluent Cloudのイベントストリーミングサービスへシームレスに接続可能となりました。これにより、オンプレミスやクラウド環境を跨いだリアルタイムデータ連携が容易になります。技術的には、Logic Appsのワークフロー内でKafkaトピックの送受信をトリガーやアクションとして利用でき、OAuth認証やAPIキーによるセキュアな接続をサポートします。実装はAzureポータルやVisual Studio CodeのLogic Apps拡張機能から設定可能です。活用例としては、IoTデバイスからのイベント収集、マイクロサービス間の非同期連携、リアルタイム分析基盤へのデータ投入などが挙げられます。注意点として、Kafkaのスループットやレイテンシ要件に応じたスケーリング設計が必要であり、コネクタの利用にはConfluent Cloudのアカウントが必須です。なお、本コネクタはAzure Event HubsやService Busなどの他のメッセージングサービスとも併用可能で、Logic Appsを介した多様なハイブリッド統合シナリオを実現します。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 100. Public Preview: Redesigned designer experience for Azure Logic Apps [Standard]

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Redesigned designer experience for Azure Logic Apps [Standard]](https://azure.microsoft.com/updates?id=527673)

**アップデートID**: 527673
**情報源**: Azure Updates API

**カテゴリ**: In preview, Integration, Internet of Things, Logic Apps

**要約**:

- 何が更新されたか  
Azure Logic Apps (Standard) のデザイナーが再設計され、パブリックプレビューとして公開。

- 主な変更点や新機能  
ワークフローの作成・編集・管理が高速化・直感的に。実行履歴の表示やワークフロー編集の統合が強化。

- 影響を受ける対象  
Logic Apps Standardを利用する開発者・運用担当者。

- 注意点  
プレビュー版のため、本番環境での利用は慎重に。既存ワークフローとの互換性確認が必要。

**詳細**:

本アップデートは、Azure Logic Apps（Standard）のワークフロー設計体験を大幅に刷新し、開発効率と操作性を向上させることを目的としています。新しいデザイナーは、直感的なUIを採用し、ワークフローのビジュアル編集を高速化。特に、実行履歴の統合表示によりデバッグや運用監視が容易になりました。技術的には、モダンなフロントエンドフレームワークを用い、リアルタイムでの状態反映と編集同期を実現。これにより、複雑な条件分岐やループ構造の編集もスムーズに行えます。活用シナリオとしては、複数API連携やイベント駆動型の自動化ワークフロー構築が挙げられ、特にDevOpsパイプラインや業務プロセス自動化に適しています。注意点としては、現時点で一部旧デザイナー機能が未対応であるため、既存ワークフローの完全移行前に動作検証が推奨されます。Azure FunctionsやEvent Gridとの連携も強化されており、より柔軟なイベント処理が可能です。詳細は公式ドキュメントおよびプレビュー版の利用を通じて確認してください。

---

### 101. Public Preview: New Agent Loop capabilities in Azure Logic Apps

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: New Agent Loop capabilities in Azure Logic Apps](https://azure.microsoft.com/updates?id=527663)

**アップデートID**: 527663
**情報源**: Azure Updates API

**カテゴリ**: In preview, Integration, Internet of Things, Logic Apps

**要約**:

- 何が更新されたか  
Azure Logic AppsのAgent Loop機能がパブリックプレビューとして新たに拡張されました。

- 主な変更点や新機能  
エージェントベースのワークフロー構築がより柔軟に可能となり、セキュリティ強化やエンタープライズ環境への展開が容易に。AIオーケストレーションの幅が広がります。

- 影響を受ける対象  
Logic Appsを用いたAI連携や自動化ワークフローを構築する開発者・運用者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure Logic AppsのAgent Loop機能がパブリックプレビューとして拡張されました。本アップデートは、エンタープライズ環境でのエージェントベースのワークフロー構築・運用をより柔軟かつ安全に実現することを目的としています。具体的には、複数のAIエージェントをループ処理で連携させる機能が強化され、動的なエージェント呼び出しや条件分岐、状態管理が可能となりました。技術的には、Logic Appsのワークフロー内でAgent Loopアクションを利用し、REST APIやコネクタ経由で外部AIサービスやカスタムエージェントと連携します。これにより、AIオーケストレーションの自動化が進み、チャットボットの多段階対話やドキュメント処理のワークフローなどに適用可能です。注意点としては、パブリックプレビュー段階のため、SLAsやサポート範囲が限定的であり、スケーラビリティやセキュリティ設定の検証が必要です。Azure Cognitive ServicesやAzure Functionsとの連携により、カスタムAIモデルの統合やイベント駆動型処理が容易になります。詳細は公式ドキュメントと更新ページを参照してください。

---

### 102. Public Preview: Agent Loop in Azure Logic Apps [Consumption]

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Agent Loop in Azure Logic Apps [Consumption]](https://azure.microsoft.com/updates?id=527658)

**アップデートID**: 527658
**情報源**: Azure Updates API

**カテゴリ**: In preview, Integration, Internet of Things, Logic Apps

**要約**:

- 何が更新されたか  
Azure Logic Apps（Consumption）で「Agent Loop」のパブリックプレビューが開始されました。

- 主な変更点や新機能  
エージェントベースのインテリジェンスと適応型ワークフローをサーバーレス環境で実現し、従来の静的な自動化を超えた動的な処理が可能に。

- 影響を受ける対象  
Logic Appsを利用する開発者や運用担当者。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure Logic Apps（Consumption）における「Agent Loop」のパブリックプレビューが開始されました。本アップデートは、従来の静的なワークフロー自動化を超え、エージェント型インテリジェンスと適応型ワークフローをサーバーレス環境で実現することを目的としています。Agent Loopは、ループ処理内でAIエージェントが動的に判断・実行を繰り返す仕組みを提供し、複雑な条件分岐や反復処理を柔軟に制御可能です。実装はLogic Appsの標準コネクタと統合され、JSONベースの定義でエージェントの行動を記述し、APIや外部サービスとの連携も容易です。典型的な活用例としては、カスタマーサポートの自動応答や多段階承認プロセスの自動化、動的なデータ検証・修正フローが挙げられます。現時点ではプレビュー版のため、スケーラビリティや一部APIの制限があり、商用利用前に十分な検証が必要です。Azure Cognitive ServicesやAzure Functionsとの連携により、自然言語処理やカスタムロジックの組み込みも可能で、より高度な自動化シナリオの構築が期待されます。

---

### 103. Generally Available: Agent Loop in Azure Logic Apps [Standard]

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Agent Loop in Azure Logic Apps [Standard]](https://azure.microsoft.com/updates?id=527649)

**アップデートID**: 527649
**情報源**: Azure Updates API

**カテゴリ**: Launched, Integration, Internet of Things, Logic Apps

**要約**:

- 何が更新されたか  
Azure Logic Apps (Standard)でAgent Loop機能が一般提供開始(GA)となりました。

- 主な変更点や新機能  
Agent Loopにより、従来のワークフロー自動化を超え、エージェントベースのループ処理が可能に。複雑なビジネスプロセスの設計・自動化が容易になります。

- 影響を受ける対象  
Logic Appsを用いた業務自動化を行う開発者や運用者。

- 注意点があれば記載  
既存のLogic Apps Standard環境での適用時は、Agent Loopの設計パターンを理解し最適化が必要です。

**詳細**:

Azure Logic Apps（Standard）におけるAgent Loop機能が一般提供（GA）となりました。本機能は従来のワークフロー自動化を超え、エージェントベースの反復処理を可能にすることで、複雑なビジネスプロセスの設計と自動化を革新します。Agent Loopは、複数のエージェント（処理単位）が並列または逐次的にタスクを実行し、動的にループ制御を行う仕組みを提供。これにより、状態管理やエラー処理が効率化され、スケーラブルな分散処理が実現可能です。実装はLogic Appsの標準ワークフロー内でエージェントの起動・監視を行い、Azure FunctionsやService Busと連携することで柔軟な拡張が可能です。典型的な活用例としては、大量データのバッチ処理、複数システム間の調整作業、動的なタスク割り当てなどが挙げられます。注意点としては、エージェント数の増加に伴うリソース消費や実行時間制限に留意が必要です。Agent LoopはAzure MonitorやApplication Insightsと連携し、運用監視やトラブルシューティングを強化できます。これにより、Logic Appsの自動化範囲が拡大し、より複雑かつ柔軟な業務プロセスの実装が可能となります。

---

### 104. Generally Available: Automated Testing Framework for Logic Apps [Standard]

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Automated Testing Framework for Logic Apps [Standard]](https://azure.microsoft.com/updates?id=527644)

**アップデートID**: 527644
**情報源**: Azure Updates API

**カテゴリ**: Launched, Integration, Internet of Things, Logic Apps

**要約**:

- 何が更新されたか  
Azure Logic Apps（Standard）向けの自動テスト機能がVisual Studio Code拡張で一般提供開始。

- 主な変更点や新機能  
ワークフローの信頼性向上を目的に、テストの自動化が可能となり、開発・統合の効率化を実現。

- 影響を受ける対象  
Logic Apps開発者および統合エンジニア。

- 注意点があれば記載  
既存のLogic Apps環境でのテスト設定や拡張機能の最新化が必要。

**詳細**:

Azure Logic Apps（Standard）向けの自動テスト機能がVisual Studio Code拡張機能で一般提供（GA）されました。本アップデートは、Logic Appsのワークフロー開発における品質向上と信頼性確保を目的としています。具体的には、開発者がテストケースをコードベースで定義し、ワークフローの各ステップやトリガー、アクションの動作検証を自動化可能です。テストはVisual Studio Code内で実行でき、結果のログやエラー詳細を即座に確認できるため、継続的インテグレーション（CI）環境への組み込みも容易です。実装はLogic AppsのJSON定義に基づき、テスト用の入力データや期待される出力を設定し、API呼び出しや条件分岐の動作を検証します。活用例としては、複雑な統合フローの変更後に自動テストを実行し、既存機能の回帰を防止するケースが挙げられます。注意点としては、Standardプラン専用機能であり、Consumptionプランでは利用不可、また一部のコネクタやカスタムコネクタの動作検証に制限がある点に留意が必要です。Azure DevOpsやGitHub Actionsとの連携により、CI/CDパイプライン内での自動テスト運用が推奨されます。詳細は公式ドキュメントおよびVS Code拡張機能のリリースノートを参照してください。

---

### 105. Generally Available: Govern Model Context Protocol (MCP) endpoints using Azure API Management

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Govern Model Context Protocol (MCP) endpoints using Azure API Management](https://azure.microsoft.com/updates?id=527626)

**アップデートID**: 527626
**情報源**: Azure Updates API

**カテゴリ**: Launched, Integration, Internet of Things, Mobile, Web, API Management

**要約**:

- 何が更新されたか  
Azure API Management（APIM）でModel Context Protocol（MCP）エンドポイントのガバナンス機能が一般提供（GA）となった。

- 主な変更点や新機能  
APIMの既存のガバナンス、セキュリティ、可観測性機能がAI駆動のMCPワークロードに対応。API管理を通じてAIモデルの利用制御や監視が可能に。

- 影響を受ける対象  
AIモデルをMCP経由で運用する企業や開発者、API管理者。

- 注意点  
MCP対応によりAIサービスのセキュリティ強化が期待されるが、設定や運用ポリシーの見直しが必要。

**詳細**:

本アップデートにより、Azure API Management（APIM）でModel Context Protocol（MCP）エンドポイントのガバナンスが一般提供（GA）となりました。背景には、AIモデルの利用拡大に伴い、APIレベルでのセキュリティ・アクセス制御・監視を統合的に行う必要性が高まったことがあります。今回の機能拡張により、APIMの既存の認証、レート制限、ログ収集、ポリシー適用といったガバナンス機能をMCP対応のAIサービスに適用可能となり、企業はAIモデル呼び出しを安全かつ効率的に管理できます。技術的には、MCPエンドポイントをAPIMのAPIとして登録し、ポリシー設定やトラフィック管理を行うことで、APIゲートウェイを介した一元的な制御が実現します。活用例としては、社内外のAIモデル提供時にアクセス制御や使用量監視を強化し、コンプライアンス遵守やコスト管理を支援します。注意点として、MCP対応のAIサービスがAPIMに対応している必要があり、レイテンシ増加の影響評価も推奨されます。関連サービスとしてAzure Cognitive ServicesやAzure Machine Learningと連携し、AIモデルのAPI管理を包括的に行うことが可能です。

---

### 106. Announcing: API Center Standard now included at no additional cost for linked Azure API Management Standard and Premium tiers

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Announcing: API Center Standard now included at no additional cost for linked Azure API Management Standard and Premium tiers](https://azure.microsoft.com/updates?id=527621)

**アップデートID**: 527621
**情報源**: Azure Updates API

**カテゴリ**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Features, Microsoft Ignite, Pricing & Offerings

**要約**:

- 何が更新されたか  
Azure API Management StandardおよびPremium層において、API Center Standardが追加費用なしで利用可能に。

- 主な変更点や新機能  
API Center Standardが従来の有料オプションから無償提供へ。API Managementサービスと連携することで利用可能。

- 影響を受ける対象  
Azure API Management StandardおよびPremiumプランのユーザー。

- 注意点  
API CenterインスタンスをAPI Managementサービスにリンクする必要がある。

**詳細**:

本アップデートは、Azure API Management（APIM）StandardおよびPremium層の顧客向けに、従来有償だったAPI Center Standardが追加コストなしで利用可能となったことを発表しています。API CenterはAPIのカタログ管理と開発者ポータルの強化を目的とし、APIの発見性向上やドキュメント一元管理を支援します。技術的には、API Centerインスタンスを既存のAPIM Standard/Premiumサービスにリンクすることで、自動的にAPI情報が同期され、APIの登録・管理が容易になります。これにより、API開発チームはAPIのライフサイクル管理を効率化し、組織内外の開発者へのAPI提供を円滑化可能です。活用例としては、複数APIのカタログ化やバージョン管理、利用状況の可視化が挙げられます。注意点としては、API CenterはAPIM Standard/Premiumにリンクが必須であり、Basic層や単独利用は対象外です。また、API Centerの機能はStandardプラン相当で提供されるため、Premium固有機能は含まれません。関連サービスとしては、Azure DevOpsやAzure Monitorと連携し、CI/CDパイプラインやAPIパフォーマンス監視と組み合わせることで、より高度なAPI運用が可能です。

---

### 107. Generally Available: Premium v2 tier in Azure API Management

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Premium v2 tier in Azure API Management](https://azure.microsoft.com/updates?id=527612)

**アップデートID**: 527612
**情報源**: Azure Updates API

**カテゴリ**: Launched, Integration, Internet of Things, Mobile, Web, API Management

**要約**:

- 何が更新されたか  
Azure API ManagementのPremium v2ティアが一般提供開始となりました。

- 主な変更点や新機能  
エンタープライズ向けに最適化された高性能・高スケーラビリティを実現し、最高のエンティティ制限と無制限のAPIコールを提供します。

- 影響を受ける対象  
大規模API管理を必要とする企業ユーザーや技術者。

- 注意点  
既存のPremiumプランからの移行計画やコスト面の検討が必要です。

情報源: https://azure.microsoft.com/updates?id=527612

**詳細**:

Azure API ManagementのPremium v2ティアが一般提供（GA）されました。これはエンタープライズ規模のAPI管理に最適化された最上位プランで、従来のPremiumよりも高いパフォーマンスとスケーラビリティを実現します。主な特徴は、APIコール数の無制限化、最大エンティティ数の増加（API、製品、ユーザーなど）、および強化されたスループットです。技術的には、改良されたインフラストラクチャと分散アーキテクチャにより、低レイテンシかつ高可用性を提供し、複数リージョン展開やVNET統合もサポートします。実装時は、既存のPremiumインスタンスからのアップグレードが可能で、APIゲートウェイのスケールアウトやセキュリティポリシーの適用も容易です。活用例としては、大量トラフィックを扱うグローバル企業のAPI管理や、複雑なマイクロサービス環境での統合が挙げられます。注意点としては、コストが高めであるため、利用規模に応じたプラン選定が重要です。また、VNET統合時のネットワーク設定やリージョン間レプリケーションの遅延に留意が必要です。Azure FunctionsやLogic Apps、Azure Monitorとの連携により、APIの自動化や監視、分析が強化され、包括的なAPI運用が可能となります。

---

### 108. Generally Available: OpenShift Virtualization now available on Azure Red Hat OpenShift

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: OpenShift Virtualization now available on Azure Red Hat OpenShift](https://azure.microsoft.com/updates?id=527236)

**アップデートID**: 527236
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Red Hat OpenShift

**要約**:

- 何が更新されたか  
Azure Red Hat OpenShift (ARO)上でRed Hat OpenShift Virtualizationが一般提供（GA）開始。

- 主な変更点や新機能  
コンテナと仮想マシンを単一のクラウドネイティブプラットフォームで統合管理可能に。プレビュー版のフィードバックを反映し安定性と機能を強化。

- 影響を受ける対象  
ARO利用者でコンテナとVMの統合運用を検討する開発者・運用者。

- 注意点  
既存環境への導入時はプレビュー版との差異を確認し、運用影響を評価すること。

**詳細**:

Azure Red Hat OpenShift（ARO）上でRed Hat OpenShift Virtualizationが一般提供（GA）されました。これにより、コンテナと仮想マシン（VM）を単一のクラウドネイティブプラットフォームで一元管理可能となり、ハイブリッドワークロードの運用効率が向上します。OpenShift VirtualizationはKubeVirtを基盤とし、OpenShiftのネイティブなKubernetes環境内でVMを管理・実行できるため、従来の仮想化環境とコンテナ環境の統合を実現します。今回のGAではプレビュー段階のフィードバックを反映し、安定性やスケーラビリティが強化されています。技術的には、OpenShiftのOperatorを通じてVMのライフサイクル管理やネットワーク、ストレージの連携を行い、AROのマネージドKubernetes基盤上でシームレスに動作します。活用シナリオとしては、レガシーアプリケーションのコンテナ移行前の段階的運用や、VMベースのワークロードとコンテナワークロードの共存環境構築が挙げられます。注意点として、VMのパフォーマンスは基盤のノードリソースに依存し、ストレージやネットワーク設定に制限があるため、事前のリソース計画が必要です。Azure Blob StorageやAzure NetApp Filesとの連携により、永続ストレージの柔軟な利用が可能で、Azure MonitorやAzure Policyと組み合わせた運用管理も推奨されます。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 109. Public Preview: Microsoft Foundry Fine-Tuning Updates

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Microsoft Foundry Fine-Tuning Updates](https://azure.microsoft.com/updates?id=526742)

**アップデートID**: 526742
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft Foundry Fine-TuningのUIが全面刷新され、エージェント中心の操作性を実現。

- 主な変更点や新機能  
モデル作成、評価、デプロイがより直感的に行え、Visual Studioとの統合が強化。

- 影響を受ける対象  
開発者やデータサイエンティストが対象。

- 注意点  
現在パブリックプレビュー段階のため、本番環境での利用は慎重に。

**詳細**:

Microsoft Foundry Fine-Tuningのパブリックプレビューでは、UIが全面的に再設計され、開発者やデータサイエンティストがエージェント中心の操作を行いやすくなりました。これにより、モデルの作成、評価、デプロイが一連のワークフローとしてシームレスに実行可能です。新UIはVisual Studioとの統合を強化し、コードベースでの微調整やデバッグが容易になっています。技術的には、FoundryのFine-Tuning機能がAPI経由でVSと連携し、モデルパラメータの調整やトレーニングジョブの管理を効率化。活用例としては、カスタムAIエージェントの迅速な開発や、特定ドメイン向けのモデル最適化が挙げられます。注意点としては、現時点でパブリックプレビューのため、機能の安定性やAPI仕様が変更される可能性がある点に留意が必要です。Azure Machine LearningやAzure Cognitive Servicesとの連携も可能で、これらと組み合わせることでエンドツーエンドのAI開発環境を構築できます。

---

### 110. Public Preview: Microsoft Foundry Control Plane & Entra Agent ID

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Microsoft Foundry Control Plane & Entra Agent ID](https://azure.microsoft.com/updates?id=526665)

**アップデートID**: 526665
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft FoundryのControl PlaneとEntra Agent IDがパブリックプレビューで提供開始。

- 主な変更点や新機能  
エンタープライズAIエージェントの統合監視、セキュリティ、ガバナンスを実現。ID管理、モニタリング、コンプライアンスを一元化し、深い可視化と制御を提供。

- 影響を受ける対象  
AIエージェントを運用する企業や開発チーム。

- 注意点  
プレビュー段階のため、本番環境での利用は慎重に検討が必要。

**詳細**:

Microsoft FoundryのPublic Previewとして提供されるControl PlaneおよびEntra Agent IDは、エンタープライズ向けAIエージェントの観測性、セキュリティ、ガバナンスを統合的に管理するプラットフォームです。背景には、AIエージェントの増加に伴う運用監視やコンプライアンス管理の複雑化があり、これを一元化することで運用効率とセキュリティ強化を目的としています。Control PlaneはエージェントのID管理（Entra Agent ID）、モニタリング、コンプライアンスチェックを統合し、中央制御を実現。Entra Agent IDはAzure ADベースのエージェント専用IDで、認証・認可を強化します。技術的には、Azure MonitorやAzure Policyと連携し、リアルタイムのログ収集やポリシー適用を自動化。活用例としては、複数AIエージェントの動作監視やアクセス制御、コンプライアンス違反の早期検知が挙げられます。現時点ではプレビュー版のため機能制限やAPIの変更可能性があり、本番環境導入時は注意が必要です。Azure AD、Azure Monitor、Azure Policyとの連携により、既存のAzureセキュリティ基盤にシームレスに統合可能です。

---

### 111. Generally Available: GitHub Copilot app modernization expanded capabilities

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: GitHub Copilot app modernization expanded capabilities](https://azure.microsoft.com/updates?id=526618)

**アップデートID**: 526618
**情報源**: Azure Updates API

**カテゴリ**: Launched

**要約**:

- 何が更新されたか  
GitHub Copilot App Modernizationの機能拡張が一般提供（GA）開始。

- 主な変更点や新機能  
アプリケーション、データベース、コンテナのモダナイゼーション支援が強化され、Azureへの移行がより迅速かつ容易に。

- 影響を受ける対象  
Azure上でのアプリケーション開発・移行を行う開発者やDevOpsエンジニア。

- 注意点があれば記載  
既存のワークフローに統合する際は、最新のCopilot機能と互換性を確認すること。

**詳細**:

本アップデートは、GitHub Copilot App Modernizationの機能拡張を一般提供（GA）化し、アプリケーションやデータベース、コンテナのモダナイゼーションおよびAzureへの移行を一層容易にすることを目的としています。具体的には、コード生成支援の高度化により、レガシーコードの解析からクラウドネイティブアーキテクチャへのリファクタリング、コンテナ化の自動化、データベーススキーマの最適化提案が可能となりました。技術的には、GitHub CopilotのAIモデルがAzureのモダナイゼーションツール群と連携し、コードベースの解析結果を基に最適なモダナイゼーションパターンを提示します。活用例としては、オンプレミスのWebアプリケーションをAzure App ServiceやAzure Kubernetes Service（AKS）へ移行する際のコード変換や、SQL ServerからAzure SQL Databaseへのスキーマ変換支援が挙げられます。注意点として、複雑なカスタムコードや特殊な依存関係を持つアプリケーションでは自動変換の精度が低下する可能性があるため、生成コードのレビューが必須です。関連サービスとしてAzure Migrate、Azure Database Migration Service、Azure Container Registryとの統合により、移行プロセス全体の自動化と効率化が実現されます。詳細は公式リンク参照。

---

### 112. Generally Available: Model Router in Microsoft Foundry

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Model Router in Microsoft Foundry](https://azure.microsoft.com/updates?id=526330)

**アップデートID**: 526330
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft FoundryのModel Routerが一般提供（GA）開始。

- 主な変更点や新機能  
AIオーケストレーション層として、プロンプトごとに最適なモデルを動的に選択可能。GPT-4/5ファミリー、GPT-oss、Deepseなど幅広いモデルをサポート。

- 影響を受ける対象  
AIモデル運用やマルチモデル活用を検討する開発者・データサイエンティスト。

- 注意点があれば記載  
対応モデルの拡充により運用設計の見直しが必要になる可能性あり。

**詳細**:

Microsoft FoundryのModel Routerが一般提供（GA）となりました。本機能はAIオーケストレーション層として、ユーザーのプロンプトに対し最適なAIモデルを動的に選択します。対応モデルはGPT-4、GPT-5ファミリーに加え、オープンソースモデル（GPT-oss）やDeepseなど多様化し、柔軟なモデル選択が可能です。技術的には、リクエストごとにモデルの性能・コスト・レイテンシを評価し、最適化アルゴリズムでルーティングを実施。API経由でFoundryに統合され、シームレスなモデル切替を実現します。活用例としては、ユーザー体験向上のための応答品質向上やコスト効率化、複数モデルの比較検証が挙げられます。制限事項としては、モデルの追加や更新時にルーティングポリシーの調整が必要であり、特定モデルの利用制限やリージョン依存性にも注意が必要です。Azure Cognitive ServicesやAzure Machine Learningと連携し、モデル管理やデプロイメントの自動化が可能で、エンドツーエンドのAI運用を支援します。詳細は公式リンク参照。

---

### 113. Private Preview: Foundry Local Android support

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Private Preview: Foundry Local Android support](https://azure.microsoft.com/updates?id=526198)

**アップデートID**: 526198
**情報源**: Azure Updates API

**カテゴリ**: In development, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Foundry LocalがプライベートプレビューでAndroid対応を開始。

- 主な変更点や新機能  
従来のWindows/Macに加え、Android端末（スマホ、タブレット、IoT）での高度なオンデバイスAI処理が可能に。Whisperモデル統合により、プライバシー保護された音声・音響処理を実現。

- 影響を受ける対象  
Androidアプリ開発者やIoTデバイス向けAI組み込み技術者。

- 注意点  
現時点はプライベートプレビューのため、利用には申請が必要。SDKやAPIの仕様が今後変更される可能性あり。

**詳細**:

本アップデートは、Foundry Localの対応プラットフォームを従来のWindowsおよびMacからAndroidへ拡大し、スマートフォンやタブレット、IoTデバイス上での高度なオンデバイスAI処理を実現することを目的としています。これにより、デバイス単体での低遅延かつプライバシー保護されたAI処理が可能となり、クラウド依存を軽減します。具体的には、Whisperモデルの統合により、音声認識や音声処理がローカルで行われ、ネットワーク通信を伴わずに高精度な音声解析が可能です。技術的には、Foundry LocalのSDKがAndroidネイティブ環境に対応し、TensorFlow LiteやONNX Runtimeなどの軽量推論エンジンと連携してモデルを効率的に実行します。活用シナリオとしては、オフライン環境での音声コマンド認識、プライバシー重視の音声メモアプリ、IoTデバイスの音声制御などが挙げられます。注意点としては、Androidデバイスのハードウェア性能に依存するため、推論速度やバッテリー消費に配慮が必要であり、プレビュー段階のためAPIの変更や機能追加が予想されます。Azure Cognitive ServicesやAzure IoT Hubとの連携により、ローカル処理とクラウド分析を組み合わせたハイブリッドアーキテクチャの構築も可能です。詳細は公式ドキュメントを参照してください。

---

### 114. Public Preview: Foundry Local updates

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Foundry Local updates](https://azure.microsoft.com/updates?id=526193)

**アップデートID**: 526193
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Foundry LocalがパブリックプレビューでWhisperモデル対応を開始し、スマホ・タブレット・IoT向けの高度なオンデバイスAIを強化。

- 主な変更点や新機能  
プライバシー保護を強化した音声・オーディオ処理が可能になり、デバイス上でのリアルタイム処理性能が向上。

- 影響を受ける対象  
モバイル端末やIoTデバイスでの音声認識・処理を行う開発者やシステム設計者。

- 注意点  
パブリックプレビュー段階のため、商用利用前に動作検証や制限事項の確認が必要。

**詳細**:

AzureのFoundry LocalがパブリックプレビューでWhisperモデルと高度なオンデバイスAIをサポート開始しました。本アップデートは、スマートフォン、タブレット、IoTデバイス上でのプライバシー保護を強化しつつ、高精度な音声・オーディオ処理を可能にすることを目的としています。WhisperモデルはMicrosoftの音声認識技術をベースにしており、ローカル環境での音声認識や翻訳、ノイズ耐性の高い音声解析を実現します。Foundry Localの再設計により、デバイスの計算リソースを効率的に活用し、低遅延かつオフライン環境での処理が可能です。実装はAzure IoT EdgeやAzure Machine Learningと連携し、モデルのデプロイや更新を自動化できます。活用例としては、プライバシー重視の音声コマンド認識、現場でのリアルタイム音声分析、IoTデバイスの音声インターフェース強化が挙げられます。制限としては、デバイスのハードウェア性能に依存するため、リソースが限られた環境では処理速度が低下する可能性があります。Azure Cognitive Servicesとの連携により、クラウドとローカルのハイブリッド処理も可能で、用途に応じた柔軟なAI活用が期待されます。詳細は公式リンクを参照してください。

---

### 115. Public Preview: Foundry IQ by Azure AI Search

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Foundry IQ by Azure AI Search](https://azure.microsoft.com/updates?id=526150)

**アップデートID**: 526150
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Azure AI Searchを活用した「Foundry IQ」がパブリックプレビューとして公開されました。

- 主な変更点や新機能  
複数のデータソースを単一のナレッジベースに統合し、エージェントが複数APIを管理せずに企業データにアクセス可能に。

- 影響を受ける対象  
エンタープライズデータを活用するチャットボットやAIエージェント開発者。

- 注意点があれば記載  
プレビュー段階のため、商用利用前に機能や制限を確認する必要があります。

**詳細**:

Azure AI SearchによるFoundry IQのPublic Previewは、エンタープライズデータを統合的に活用するための知識システムです。従来、複数のデータソースやAPIを個別に管理・接続する必要がありましたが、Foundry IQは単一のナレッジベースに接続するだけで、多様なデータソースを横断的に検索・参照可能にします。技術的にはAzure AI Searchの強力なインデクシングと自然言語処理機能を活用し、エージェントが企業内のドキュメント、データベース、APIなどを統合的に理解・応答できる仕組みを提供します。実装はAzure Cognitive Searchのインデックス作成とスキルセットを基盤とし、カスタムコネクタで多様なデータソースを統合。活用例としては、カスタマーサポートチャットボットの知識基盤強化や社内ナレッジ管理の効率化が挙げられます。注意点としては、プレビュー段階のため機能変更や制限があること、またデータセキュリティやアクセス制御の設計が重要です。Azure Cognitive Search、Azure AIサービス、Azure Functionsとの連携により、柔軟なデータ統合とリアルタイム更新が可能です。

---

### 116. Generally Available: Foundry Tools (rebrand from Azure AI Services)

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Foundry Tools (rebrand from Azure AI Services)](https://azure.microsoft.com/updates?id=526132)

**アップデートID**: 526132
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Azure AI Servicesが「Foundry Tools」として正式リブランドされ、一般提供開始。

- 主な変更点や新機能  
音声、動画、画像、ドキュメント、テキスト向けの事前構築済みAI機能を統合し、Microsoft Foundryプラットフォーム上でシームレスに利用可能に。

- 影響を受ける対象  
AI機能を活用する開発者や企業、特にマルチメディア処理を行うアプリケーション開発者。

- 注意点  
既存のAzure AI ServicesユーザーはFoundry Toolsへの移行や統合方法を確認する必要がある。

**詳細**:

本アップデートは、従来の「Azure AI Services」を「Foundry Tools」としてリブランドし、Microsoft Foundryプラットフォームに統合された生産準備済みのAI機能群を提供するものです。音声、映像、画像、文書、テキスト解析を対象とし、開発者はAPIやSDKを通じてこれらのマルチモーダルAI機能をシームレスに組み込めます。技術的には、各AIモデルはスケーラブルなクラウドインフラ上でホストされ、RESTful APIやAzure SDKにより容易に呼び出し可能です。活用例としては、顧客サポートの自動音声認識、動画コンテンツの自動タグ付け、文書の高度な自然言語処理などが挙げられます。注意点として、利用時のAPI呼び出し制限やデータプライバシー遵守が必要であり、特に機密情報を扱う場合は暗号化やアクセス制御の設定が推奨されます。関連サービスとしては、Azure Cognitive Services、Azure Machine Learning、Azure Blob Storageとの連携が可能で、データの保存・前処理からモデルのカスタマイズ、結果の分析まで一貫したワークフロー構築が支援されます。

---

### 117. Generally Available: Content Understanding in Microsoft Foundry

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Content Understanding in Microsoft Foundry](https://azure.microsoft.com/updates?id=526123)

**アップデートID**: 526123
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Content Understandingが一般提供（GA）となり、Microsoft Foundryモデルへの接続が可能に。

- 主な変更点や新機能  
Foundryモデルのデプロイ利用対応、VNET接続、マネージドID、顧客管理キー（CMK）をサポート。

- 影響を受ける対象  
Foundryモデルを活用するAzureユーザー、セキュリティ強化やネットワーク分離を求める技術者。

- 注意点があれば記載  
VNETやManaged Identity利用時は設定の整合性を確認し、CMK利用時はキー管理ポリシーを遵守すること。

**詳細**:

Microsoft FoundryのContent Understanding機能が一般提供（GA）となり、Foundryモデルへの接続が可能になりました。これにより、顧客はFoundry上で展開されたモデルを直接利用でき、文書解析やコンテンツ分類などの高度なAI処理を自社環境で実装可能です。主なアップデートとして、仮想ネットワーク（VNET）統合によりセキュアなネットワーク環境での利用が可能となり、マネージドIDによる認証管理が簡素化されました。さらに、顧客管理キー（CMK）を用いたデータ暗号化対応で、コンプライアンス要件にも対応しています。技術的には、FoundryモデルのAPIエンドポイントをContent Understandingサービスに紐付け、VNET内から安全に呼び出す構成が推奨されます。活用例としては、金融や医療分野での機密文書解析や、カスタムモデルを用いた自動分類ワークフロー構築が挙げられます。注意点として、VNET設定やマネージドIDの権限付与は正確に行う必要があり、CMK利用時はキー管理ポリシーに留意してください。Azure Cognitive ServicesやAzure Key Vaultとの連携により、セキュアかつスケーラブルなAIコンテンツ処理環境を構築可能です。

---

### 118. Public Preview: Enrich agents with a unified catalog of prebuilt and custom tools in Microsoft Foundry

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Enrich agents with a unified catalog of prebuilt and custom tools in Microsoft Foundry](https://azure.microsoft.com/updates?id=526114)

**アップデートID**: 526114
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft Foundryがパブリックプレビューで、エージェントにリアルタイムのビジネスコンテキストやマルチモーダル機能、カスタムビジネスロジックを統合可能な統一カタログ（MCPツール）を提供開始。

- 主な変更点や新機能  
Model Context Protocol（MCP）対応の事前構築およびカスタムツールを一元管理し、エージェントの機能拡張が容易に。

- 影響を受ける対象  
Azure上でMicrosoft Foundryを利用する開発者やシステムインテグレーター。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討が必要。

**詳細**:

本アップデートは、Microsoft Foundryにおいてエージェントの機能拡張を目的に、リアルタイムの業務コンテキストやマルチモーダル対応、カスタムビジネスロジックを統合カタログで提供するModel Context Protocol（MCP）ツールをパブリックプレビューで公開したものです。これにより、開発者は単一のカタログから事前構築済みおよび独自開発のツールを組み合わせ、エージェントに対して動的かつ柔軟な機能付与が可能となります。技術的には、MCP準拠のツールがFoundryのエージェントフレームワークに統合され、API経由でリアルタイムデータやビジネスロジックを注入し、多様な入力（テキスト、画像など）に対応するマルチモーダル処理を実現します。活用例としては、顧客対応チャットボットが最新の業務データを参照しつつ画像認識やカスタム計算ロジックを組み込み、より高度な応答生成が可能です。注意点としては、プレビュー段階のためMCPツールの互換性や安定性に制限があり、運用環境での利用は慎重に検討が必要です。Azure Cognitive ServicesやAzure Functionsとの連携により、外部AIモデルやサーバーレスロジックを組み込むことで、さらに高度なカスタマイズが可能となります。

---

### 119. Public Preview: Built-in memory in Foundry Agent Service

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Built-in memory in Foundry Agent Service](https://azure.microsoft.com/updates?id=526004)

**アップデートID**: 526004
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Foundry Agent Serviceに長期メモリ機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
エージェントがセッションやワークフローを跨いで情報を保持・適応・一貫した動作が可能に。Foundryランタイムに統合された永続メモリ基盤を提供します。

- 影響を受ける対象  
Foundry Agentを利用する開発者やシステム設計者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure Foundry Agent Serviceにおける「Built-in memory」のパブリックプレビューは、エージェントがセッションやワークフローを跨いで情報を持続的に記憶・活用できる長期メモリ機能を提供します。これにより、エージェントはユーザーの過去の対話や状態を保持し、より一貫性のある応答や適応的な動作が可能となります。メモリはFoundryランタイムに統合されており、スケーラブルかつ堅牢なストレージ基盤を備えています。実装面では、メモリデータはエージェントのコンテキストとして管理され、API経由で読み書きが可能で、状態管理や履歴追跡を容易にします。活用例としては、カスタマーサポートチャットボットが過去の問い合わせ内容を記憶し、継続的な対話を実現するケースや、複数ワークフロー間で情報を共有する業務自動化が挙げられます。注意点としては、プレビュー段階のためAPI仕様やパフォーマンスが変更される可能性があり、データ保持ポリシーやセキュリティ設定の確認が必要です。Azure Cognitive ServicesやAzure Bot Serviceとの連携により、自然言語処理や対話管理と組み合わせた高度なエージェント開発が促進されます。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 120. Public Preview: Multi-agent workflows in Foundry Agent Service

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Multi-agent workflows in Foundry Agent Service](https://azure.microsoft.com/updates?id=525999)

**アップデートID**: 525999
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Foundry Agent Serviceでマルチエージェントワークフローがパブリックプレビューに対応しました。

- 主な変更点や新機能  
ビジュアルデザイナーとコードファーストAPIで複数エージェントの連携を構築可能。状態管理、コンテキスト共有、エラーリカバリ機能を備えた堅牢なオーケストレーションが実現します。

- 影響を受ける対象  
複雑な企業プロセスを自動化・管理する開発者やシステムインテグレーター。

- 注意点  
プレビュー版のため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure Foundry Agent Serviceの新しいPublic Preview機能「Multi-agent workflows」は、複数のエージェント間での高度なワークフロー構築を可能にします。背景には、複雑な企業業務の自動化において単一エージェントでは対応困難なシナリオが増加している点があり、これを解決するために設計されました。本機能は、ビジュアルデザイナーとコードファーストAPIの両方を提供し、開発者は視覚的にフローを設計するか、プログラム的に詳細な制御を実装可能です。ワークフローは状態の永続化、コンテキスト共有、エラーリカバリ機能を備え、複数エージェント間での協調動作や段階的な処理進行を実現します。実装はモジュラー構造で、各エージェントは独立したタスクを担当しつつ、メッセージや状態を共有することで連携します。典型的な活用例としては、複数部門間の承認プロセスや複雑なデータ処理パイプラインの自動化が挙げられます。注意点としては、現時点でプレビュー段階のためAPI仕様の変更や機能追加が予想されること、またスケーラビリティやパフォーマンス要件に応じた設計が必要です。Azure Logic AppsやAzure Functionsとの連携により、外部サービスとの統合やイベント駆動型処理が容易に行え、エンタープライズ向けの堅牢な自動化基盤構築に貢献します。詳細は公式ドキュメント（https://azure.microsoft.com/updates?id=525999）を参照してください。

---

### 121. Public Preview: Hosted agents in Foundry Agent Service

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Hosted agents in Foundry Agent Service](https://azure.microsoft.com/updates?id=525994)

**アップデートID**: 525994
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Foundry Agent Serviceにホスト型エージェントのパブリックプレビューが追加されました。

- 主な変更点や新機能  
Microsoft Agent FrameworkやLangGraph、CrewAIなどで開発したカスタムコードエージェントをクラウド上で簡単にデプロイ・運用可能に。

- 影響を受ける対象  
エージェント開発者やチームで、ローカル実験から本番環境へのスムーズな移行を目指す技術者。

- 注意点  
現段階はパブリックプレビューのため、商用利用時は機能制限や変更の可能性に注意が必要です。

**詳細**:

AzureのFoundry Agent Serviceにおける「Hosted agents」のPublic Previewは、ローカル環境での実験から本格的なプロダクション環境へのスムーズな移行を支援するためのアップデートです。これにより、Microsoft Agent Framework、LangGraph、CrewAI、その他のオープンソースフレームワークで開発されたカスタムコードエージェントをクラウド上でホスト可能となり、運用負荷を大幅に軽減します。技術的には、エージェントのコンテナ化とスケーラブルなホスティング環境を提供し、API経由での管理やモニタリングが可能です。典型的な活用例としては、チャットボットや自動化ワークフローの大規模展開が挙げられ、Azure FunctionsやAzure Monitorとの連携によりイベント駆動型処理やパフォーマンス監視が容易になります。一方、現時点ではプレビュー版のため、対応フレームワークやリージョンに制限があり、商用利用前に十分な検証が必要です。これにより、開発から運用までの一貫したエージェント管理がAzure環境内で実現可能となります。

---

### 122. Generally Available: Observability in Foundry Control Plane

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Observability in Foundry Control Plane](https://azure.microsoft.com/updates?id=525985)

**アップデートID**: 525985
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Foundry Control PlaneのObservability機能が一般提供（GA）となりました。

- 主な変更点や新機能  
エージェントの監視・評価が可能になり、モデルの品質、性能、安全性を総合的に評価・最適化できる機能が強化されています。

- 影響を受ける対象  
Foundryを利用する開発者や運用チーム。

- 注意点  
現在はパブリックプレビューからGAへの移行段階のため、モデル評価機能は事前案内中です。

**詳細**:

本アップデートは、Foundry Control PlaneにおけるObservability機能の一般提供（GA）開始に伴うもので、開発者がモデル評価（model evals）を含む機械学習ワークロードの品質・性能・安全性を総合的に監視・最適化できる環境を提供します。具体的には、エージェントベースのデータ収集により、リアルタイムでモデルの動作状況や異常検知、パフォーマンスメトリクスを可視化可能です。技術的には、Foundry Control Plane上で動作するエージェントがログやトレース、メトリクスを収集し、Azure MonitorやApplication Insightsと連携して分析・アラート設定を行います。活用例としては、モデルの推論精度低下検知やリソース使用率の最適化、セキュリティ監査が挙げられ、運用効率向上に寄与します。注意点としては、エージェント導入時のリソース負荷やプライバシー保護の設定が必要であり、現時点で一部機能はプレビュー段階のため仕様変更の可能性があります。Azure Machine LearningやAzure Monitorとの統合により、包括的なML運用管理が実現可能です。

---

### 123. Public Preview: Enterprise MCP enhancements in Foundry Agent Service

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Enterprise MCP enhancements in Foundry Agent Service](https://azure.microsoft.com/updates?id=525976)

**アップデートID**: 525976
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft FoundryのFoundry Agent ServiceがEnterprise MCPとの連携を強化し、認証済みかつ安全な接続をサポート。

- 主な変更点や新機能  
MCPサーバーへの認証情報を安全に渡せるようになり、接続の柔軟性とセキュリティ、コンプライアンスが向上。

- 影響を受ける対象  
Enterprise MCPを利用するAzure環境の運用技術者やセキュリティ担当者。

- 注意点  
プレビュー段階のため、本番環境での利用は慎重に検討し、最新ドキュメントを確認すること。

**詳細**:

本アップデートは、Microsoft FoundryのAgent ServiceにおけるEnterprise MCP（Microsoft Cloud Platform）との統合強化を目的としています。従来、MCPサーバーへの認証情報の受け渡しはセキュリティ面で課題がありましたが、今回の改良により、Agent ServiceがMCPサーバーへ安全かつ認証済みの接続を確立し、認証情報を安全に伝達可能となりました。具体的には、TLSを用いた暗号化通信とトークンベースの認証機構を組み合わせ、認証情報の漏洩リスクを低減しています。実装面では、Agent Serviceの設定にてEnterprise MCP接続用の認証情報管理が強化され、API呼び出し時に安全な認証トークンを自動的に取得・更新します。これにより、セキュリティ要件の高い環境下でもMCPとの連携が容易になり、運用効率とコンプライアンス遵守が向上します。活用例としては、大規模なエンタープライズ環境でFoundry Agentを用いて複数MCPサーバーと安全に連携し、監査ログや構成管理を一元化するケースが挙げられます。注意点としては、現時点でプレビュー段階のため、対応リージョンや機能の一部制限が存在し、正式リリース前に十分な検証が推奨されます。Azure Active Directoryとの連携により、認証情報管理の一元化やポリシーベースのアクセス制御が可能であり、Azure MonitorやAzure Security Centerとの統合による運用監視強化も期待できます。

---

### 124. Public Preview: Microsoft Foundry one-click deploy channels in Teams, M365 and non-Microsoft

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Microsoft Foundry one-click deploy channels in Teams, M365 and non-Microsoft](https://azure.microsoft.com/updates?id=525971)

**アップデートID**: 525971
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft Foundryで、カスタムエージェントをMicrosoft TeamsやM365 Copilotへワンクリック・ノーコードで展開可能に。

- 主な変更点や新機能  
プロコード不要の簡単デプロイ機能を追加し、非Microsoftチャネルへの展開もサポート。

- 影響を受ける対象  
TeamsやM365を活用する開発者・IT管理者、カスタムエージェント導入を検討する組織。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に。機能制限や変更の可能性あり。

**詳細**:

Microsoft Foundryの新機能「one-click deploy channels」は、カスタムエージェントをMicrosoft TeamsおよびMicrosoft 365 Copilotに対してコード不要で即時公開可能にするパブリックプレビューです。これにより、従来のプロコードによる複雑なデプロイ作業を排除し、組織は迅速に数百万ユーザーへエージェントを展開できます。技術的には、FoundryのGUIからエージェントを選択し、ワンクリックでTeamsチャネルやM365環境に連携可能な形でパッケージング・公開される仕組みです。非Microsoftプラットフォームへの展開も視野に入れており、API連携による拡張性も提供されます。活用例としては、社内ヘルプデスクの自動応答エージェントや営業支援チャットボットの即時配信が挙げられ、開発工数削減と迅速なユーザーアクセスが期待されます。注意点としては、パブリックプレビュー段階のため一部機能制限や安定性の課題があり、運用前に十分な検証が必要です。Azure Bot ServiceやAzure Cognitive Servicesとの連携により、自然言語処理や多言語対応の強化も可能です。

---

### 125. Public Preview: LLM Speech in Microsoft Foundry

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: LLM Speech in Microsoft Foundry](https://azure.microsoft.com/updates?id=525962)

**アップデートID**: 525962
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft Foundryにて、LLM（大規模言語モデル）を活用した音声認識・翻訳APIがパブリックプレビューとして提供開始。

- 主な変更点や新機能  
高度な文脈理解による高精度な文字起こしと翻訳、多言語対応の強化、プロンプトチューニング機能の追加。

- 影響を受ける対象  
音声認識・翻訳を利用する開発者や企業、特に多言語対応アプリケーションの構築者。

- 注意点  
パブリックプレビュー段階のため、商用利用時はAPIの安定性や制限を確認する必要あり。

**詳細**:

Microsoft FoundryのPublic Previewとして提供される「LLM Speech」は、大規模言語モデル（LLM）を活用した音声認識および翻訳APIです。背景には、従来の音声認識技術の限界を超え、より自然で文脈を理解した高精度な文字起こしと多言語翻訳を実現する狙いがあります。主な機能は、高度なプロンプトチューニングによる文脈適応性の向上、多言語対応の強化、リアルタイムおよびバッチ処理での音声入力からのテキスト生成です。技術的には、Microsoftの大規模言語モデルを音声認識パイプラインに統合し、音声信号から抽出した特徴量をLLMに入力、文脈情報を活用して精度を高めています。実装はREST API経由で利用可能で、API呼び出し時にプロンプトや言語設定を細かく調整可能です。活用例としては、多言語カスタマーサポートの自動文字起こしと翻訳、国際会議のリアルタイム字幕生成、音声ドキュメントの多言語化などが挙げられます。注意点としては、現時点でプレビュー版のためAPIの安定性や対応言語に制限がある可能性があり、商用利用前に十分な検証が必要です。Azure Cognitive ServicesのSpeechサービスやTranslatorとの連携により、既存の音声処理ワークフローに容易に統合可能で、Azureのセキュリティおよびスケーラビリティ基盤を活用できます。詳細は公式ドキュメントおよびプレビューAPI仕様を参照してください。

---

### 126. Public Preview: Bring Your Own AI Gateway to Foundry Agent Service

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Bring Your Own AI Gateway to Foundry Agent Service](https://azure.microsoft.com/updates?id=525957)

**アップデートID**: 525957
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Foundry Agent Serviceで「Bring Your Own AI Model Gateway」機能がパブリックプレビュー提供開始。

- 主な変更点や新機能  
Azure API ManagementやMulesoft、Kongなど任意のAIゲートウェイ経由でFoundryモデル接続可能に。LLMの前後フックやポリシーベースのモデル制御もサポート。

- 影響を受ける対象  
Foundry Agent Serviceを利用する企業や開発者で、独自AIゲートウェイ統合を検討する技術者。

- 注意点があれば記載  
プレビュー機能のため本番環境での利用は慎重に。対応ゲートウェイの設定やセキュリティポリシー確認が必要。

**詳細**:

本アップデート「Bring Your Own AI Gateway to Foundry Agent Service」は、Foundry Agent Serviceに外部AIゲートウェイ（例：Azure API Management、Mulesoft、Kong）を接続可能にするパブリックプレビュー機能です。これにより、企業はFoundry上でホストされるAIモデルを自社の既存API管理基盤やゲートウェイ経由で柔軟に呼び出せます。Foundry Agent Serviceは、事前・事後処理のLLMフックやポリシーベースのモデル選択をサポートし、セキュリティやガバナンスを維持しつつ運用可能です。技術的には、外部ゲートウェイがFoundry Agent ServiceのAPIエンドポイントと連携し、トラフィック制御や認証、ログ収集を一元管理します。活用例としては、企業が既存のAPI管理環境を活かしつつFoundryの高度なAIモデルを統合し、業務アプリケーションにシームレスに組み込むケースが想定されます。注意点としては、現時点でプレビュー段階のため、対応ゲートウェイの種類や機能制限、パフォーマンス面の検証が必要です。Azure API Managementとの連携が特に推奨され、Azureのセキュリティ機能や監査ログと組み合わせることで堅牢な運用が可能です。

---

### 127. Announcing: Developer Training tier for low-cost fine-tuning training

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Announcing: Developer Training tier for low-cost fine-tuning training](https://azure.microsoft.com/updates?id=525952)

**アップデートID**: 525952
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft Foundryに「Developer Training」ティアが追加され、低コストでのファインチューニング用モデル学習が可能に。

- 主な変更点や新機能  
スポットキャパシティを活用し、ホスティングのDeveloperティア同様の価格帯でトレーニングを提供。

- 影響を受ける対象  
コストを抑えてモデルのファインチューニングを行いたい開発者やデータサイエンティスト。

- 注意点があれば記載  
スポットインスタンスの特性上、トレーニング中断リスクがあるため、ワークロード設計に注意が必要。

**詳細**:

Microsoft Foundryに新設されたDeveloper Training tierは、スポットキャパシティを活用することで、ファインチューニングのトレーニング工程を極めて低コストで実行可能にするプランです。これにより、従来のDeveloper tierがホスティングに提供していたコスト効率を、トレーニング段階にも拡張しました。具体的には、スポットインスタンスを利用して計算リソースを動的に割り当てることで、通常のオンデマンド料金より大幅に安価な価格でモデルの微調整が可能です。実装面では、Azure Machine LearningやAzure Kubernetes Serviceと連携し、スポットVMの中断リスクを考慮したチェックポイント保存や再開機能を組み込むことが推奨されます。活用シナリオとしては、開発初期段階のモデル調整や頻繁なパラメータチューニング、コスト制約のあるスタートアップや個人開発者向けに適しています。一方で、スポットインスタンスの特性上、トレーニング中断の可能性があるため、長時間連続実行やミッションクリティカルな処理には注意が必要です。Azure Cognitive ServicesやAzure Machine Learningと組み合わせることで、トレーニングからデプロイまでの一連のMLワークフローを低コストかつ効率的に構築可能です。

---

### 128. Generally Available: Streamline IT governance, security, and cost management experiences with Microsoft Foundry

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Streamline IT governance, security, and cost management experiences with Microsoft Foundry](https://azure.microsoft.com/updates?id=525942)

**アップデートID**: 525942
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft FoundryのAI開発・管理機能が一般提供（GA）開始。

- 主な変更点や新機能  
エンタープライズ向けにITガバナンス、セキュリティ、コンプライアンス、コスト管理を統合し、AIソリューションの安全かつ効率的な展開を支援。

- 影響を受ける対象  
企業のIT管理者やAI開発チーム。

- 注意点があれば記載  
導入時は既存のガバナンス・セキュリティポリシーとの整合性を確認すること。

**詳細**:

Microsoft Foundryは、エンタープライズ向けAI開発と管理を効率化するプラットフォームとしてGA（一般提供）されました。本アップデートは、ITガバナンス、セキュリティ、コスト管理を一元化し、企業の厳格なコンプライアンス要件に適合したAIソリューションの展開を支援します。主な機能として、ポリシーベースのアクセス制御、監査ログの統合管理、コスト分析ダッシュボードが提供され、これによりIT管理者はAIリソースの利用状況をリアルタイムで把握・制御可能です。技術的にはAzure Active Directoryとの連携による認証・認可管理、Azure Policyを活用したガバナンスルールの自動適用、Azure Cost Managementとの統合によるコスト最適化が実装されています。活用シナリオとしては、複数部門にまたがるAIプロジェクトの統合管理や、規制遵守が必須な金融・医療分野での安全なAI導入が挙げられます。注意点として、既存環境とのポリシー整合性や権限設計の適切な設定が必要であり、初期設定における運用フローの見直しが推奨されます。関連サービスにはAzure Machine Learning、Azure Synapse Analytics、Azure Monitorがあり、Foundryを中心に統合的なAI運用基盤を構築可能です。詳細は公式ドキュメント（https://azure.microsoft.com/updates?id=525942）を参照してください。

---

### 129. Public Preview: New granular controls for network and integration security in Microsoft Foundry

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: New granular controls for network and integration security in Microsoft Foundry](https://azure.microsoft.com/updates?id=525933)

**アップデートID**: 525933
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft Foundryにおいて、ネットワークおよび統合セキュリティのより細かい制御機能がパブリックプレビューで提供開始。

- 主な変更点や新機能  
IT管理者がAIソリューションの展開時に、ネットワークアクセスやリソース統合のセキュリティ設定を詳細に管理可能に。

- 影響を受ける対象  
エンタープライズでMicrosoft Foundryを利用し、AI開発・運用を行うIT管理者やセキュリティ担当者。

- 注意点  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討し、最新ドキュメントを参照すること。

**詳細**:

Microsoft Foundryのパブリックプレビューで提供開始された新しいネットワークおよび統合セキュリティの細分化制御は、エンタープライズ向けAI開発の安全性と管理性を強化することを目的としています。背景には、AIソリューションの複雑化に伴うセキュリティリスクの増大と、IT管理者による厳格なアクセス制御ニーズの高まりがあります。本アップデートでは、仮想ネットワーク（VNet）統合の詳細設定や、APIおよびリソース間の通信ポリシーを細かく設定可能となり、特定のサブネットやIP範囲、サービスエンドポイント単位でのアクセス制御が可能です。技術的には、Azure PolicyやAzure RBACと連携し、Foundry内のAIリソースごとにネットワークルールを適用、Azure Private Linkを活用したプライベート接続もサポートします。これにより、企業はAIモデルの開発・デプロイ環境を外部から隔離しつつ、必要な統合サービスとの安全な連携を実現できます。活用例としては、金融機関が内部ネットワークに限定したAI分析環境を構築しつつ、外部データソースとの安全な連携を維持するケースが挙げられます。注意点として、プレビュー段階のため一部機能は制限される可能性があり、既存のネットワーク構成との整合性確認が重要です。関連サービスとしては、Azure Virtual Network、Azure Private Link、Azure Policy、Azure Active Directoryが密接に連携し、統合的なセキュリティ管理を実現しています。

---

### 130. Public Preview: Agent mitigations and guardrail customization 

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Agent mitigations and guardrail customization ](https://azure.microsoft.com/updates?id=525923)

**アップデートID**: 525923
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite, Security

**要約**:

- 何が更新されたか  
Microsoft Foundry Control Planeで、エージェント単位で適用可能なガードレール（旧コンテンツフィルター）がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
ガードレールがモデル展開だけでなくエージェントレベルで設定可能に。プロンプトインジェクション対策を含む既存の制御機能を強化。

- 影響を受ける対象  
Microsoft Foundry上でエージェントを運用する開発者や運用担当者。

- 注意点  
パブリックプレビューのため、本番環境適用時は動作検証を推奨。

**詳細**:

本アップデートは、Microsoft Foundry Control Planeにおけるエージェント単位でのガードレール（旧称コンテンツフィルター）適用をパブリックプレビューとして提供開始したものです。従来はモデル展開単位でのみ制御可能だったプロンプトインジェクション対策などのセキュリティ制御を、エージェントレベルで細かく設定可能とし、より柔軟かつ強固な運用を実現します。技術的には、ガードレール設定をエージェントのメタデータとして管理し、プロンプト処理時にリアルタイムで検査・制御を行う仕組みです。これにより、複数のエージェントが異なるポリシーを持つ環境下でも安全な対話が可能となります。活用例としては、社内チャットボットやカスタマーサポートエージェントにおける不適切入力の自動検知・遮断が挙げられます。注意点としては、パブリックプレビュー段階のためAPI仕様変更の可能性や一部制限が存在し、運用前に十分な検証が必要です。また、Azure OpenAI ServiceやAzure Cognitive Servicesと連携することで、より高度な自然言語処理とセキュリティ制御を組み合わせたソリューション構築が可能です。詳細は公式ドキュメントを参照してください。

---

### 131. Public Preview: OpenTelemetry visualizations and enhanced monitoring experience in Azure Monitor for Azure VMs and Arc Servers

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: OpenTelemetry visualizations and enhanced monitoring experience in Azure Monitor for Azure VMs and Arc Servers](https://azure.microsoft.com/updates?id=525536)

**アップデートID**: 525536
**情報源**: Azure Updates API

**カテゴリ**: In preview, DevOps, Management and governance, Azure Monitor

**要約**:

- 何が更新されたか  
Azure MonitorにOpenTelemetryベースの可視化機能がパブリックプレビューで追加され、Azure VMとArcサーバー向けの統合監視体験が強化された。

- 主な変更点や新機能  
OpenTelemetryデータの視覚化が可能になり、複数の監視機能を単一ビューで一元管理できるようになった。

- 影響を受ける対象  
Azure Virtual MachinesおよびAzure Arc対応サーバーの監視を行う技術者。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に。将来的に機能やAPIが変更される可能性あり。

**詳細**:

本アップデートは、Azure MonitorにおけるAzure VMおよびAzure Arc対応サーバーの監視体験を統合・強化することを目的とし、OpenTelemetryベースの可視化機能をパブリックプレビューとして提供開始しました。従来は複数のツールやビューに分散していたメトリクス、トレース、ログ情報を一元的に表示可能とし、監視運用の効率化を図ります。具体的には、OpenTelemetry SDKから収集したトレースデータをAzure Monitorのワークスペースに送信し、Azure Monitorのワークブックやダッシュボード上で詳細な分散トレーシングや依存関係マップを表示可能です。実装はAzure Monitor Agentを介してOpenTelemetryコレクターを組み込み、Azure Arc対応サーバーにも同様の監視機能を拡張しています。活用シナリオとしては、ハイブリッド環境におけるアプリケーションのパフォーマンスボトルネック解析や障害箇所特定が挙げられ、オンプレミスや他クラウド環境のサーバーも一元監視可能です。注意点としては、パブリックプレビュー段階のため一部機能が限定的であり、Azure Monitor Log Analyticsワークスペースの設定やOpenTelemetry SDKのバージョン管理が必要です。関連サービスとしてAzure Monitor Logs、Azure Monitor Metrics、Azure Arc、Azure Monitor Workbooksと密接に連携し、統合的な監視ソリューションを実現しています。

---

### 132. Public Preview: Large volumes up to 7.2 PiB     

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Large volumes up to 7.2 PiB     ](https://azure.microsoft.com/updates?id=525150)

**アップデートID**: 525150
**情報源**: Azure Updates API

**カテゴリ**: In development, Storage, Azure NetApp Files

**要約**:

- 何が更新されたか  
Azure NetApp Filesで専用容量上に最大7.2PiBの大容量ボリュームを作成可能に（Public Preview）。  

- 主な変更点や新機能  
「Cool Access」機能が拡張され、アクセス頻度の低いデータ向けに大容量ボリュームをサポート。  

- 影響を受ける対象  
大容量ストレージを必要とし、コスト最適化を図りたいAzure NetApp Files利用者。  

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に検討が必要。

**詳細**:

本アップデートは、Azure NetApp Files（ANF）における大容量ボリュームのニーズ増加に対応するため、専用キャパシティ上で最大7.2PiBのボリューム作成を可能にする「Large Volumes up to 7.2 PiB with Cool Access」機能のパブリックプレビュー提供を開始したものです。これにより、アクセス頻度の低いデータを格納する大規模ストレージ環境の構築が容易になります。

具体的には、従来の最大容量制限を大幅に引き上げ、かつ「Cool Access」機能を拡張。Cool Accessは、データのアクセス頻度に応じてストレージ階層を自動的に最適化し、コスト効率を高める仕組みであり、今回のアップデートで大容量ボリュームにも適用可能となりました。専用容量プール上でのボリューム作成時に、容量指定とCool Access設定を組み合わせることで実装されます。

活用シナリオとしては、アーカイブデータやログ、バックアップデータなど、アクセス頻度は低いが高い耐久性とパフォーマンスを求めるエンタープライズワークロードに最適です。例えば、大規模な医療画像データやメディアファイルの長期保存に適用可能です。

注意点として、Cool Accessはアクセスパターンに基づく自動階層化のため、頻繁にアクセスされるデータはパフォーマンスに影響を与える可能性があるため、ワークロード特性の把握が重要です。また、専用容量プールの管理や容量計画も従来以上に慎重に行う必要があります。

関連サービスとしては、Azure Monitorによるパフォーマンス監視やAzure Backupとの連携により、運用管理が容易になります。さらに、ANFのNFS/SMBプロトコル対応により、既存のオンプレミス環境からの移行もスムーズです。今回のアップデートは、大容量データ管理のコスト最適化とパフォーマンス維持を両立するための重要な拡張機能です。

---

### 133. Public Preview: Built-in CIS benchmarks for Azure endorsed Linux distros in Machine Config

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Built-in CIS benchmarks for Azure endorsed Linux distros in Machine Config](https://azure.microsoft.com/updates?id=523614)

**アップデートID**: 523614
**情報源**: Azure Updates API

**カテゴリ**: In preview, Management and governance, Azure Policy

**要約**:

- 何が更新されたか  
Azure Machine Configurationで、Azure推奨のLinuxディストリビューション向けにCISベンチマークが組み込みで利用可能に（パブリックプレビュー）。

- 主な変更点や新機能  
azure-osconfigを活用し、カスタマイズ可能なセキュリティベンチマークを提供。CIS基準に基づくセキュリティ設定の自動適用・管理が可能。

- 影響を受ける対象  
Azure上で稼働するAzure推奨Linuxディストリビューションを利用する技術者や運用チーム。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討し、最新のドキュメントを参照すること。

**詳細**:

本アップデートは、Azureが推奨するLinuxディストリビューション向けに、CIS（Center for Internet Security）ベンチマークをAzure Machine Configuration（azure-osconfig）上で組み込み提供する機能のパブリックプレビュー開始を示します。背景には、クラウド環境でのセキュリティ標準準拠を自動化・効率化するニーズがあり、CISベンチマーク適用を容易にすることが目的です。具体的には、Azure Machine Configurationのカスタマイズ可能なセキュリティベンチマーク機能により、Azure認定Linuxディストリビューション（例：Ubuntu、Red Hat、CentOSなど）に対してCIS推奨設定を自動適用・監査可能となります。技術的には、azure-osconfigエージェントがVM上で動作し、CISベンチマークに基づく設定変更やコンプライアンスチェックを実行。ユーザーはAzureポータルやCLIからポリシーを選択・カスタマイズし、対象VMに適用します。活用例としては、セキュリティ基準準拠が必須の環境での一括設定適用や定期的な準拠状況の監査が挙げられます。注意点としては、現時点がパブリックプレビューであり、全機能が正式リリース前のため一部制限や変更の可能性がある点、またカスタマイズ時に既存設定との競合に注意が必要です。関連サービスとしては、Azure Security CenterやAzure Policyと連携し、より包括的なセキュリティ管理・監査が可能です。詳細は公式ドキュメントおよびアップデートページを参照ください。

---

### 134. Public Preview: New AI templates in Microsoft Foundry

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: New AI templates in Microsoft Foundry](https://azure.microsoft.com/updates?id=522554)

**アップデートID**: 522554
**情報源**: Azure Updates API

**カテゴリ**: In preview, AI + machine learning, Microsoft Foundry

**要約**:

- 何が更新されたか  
Microsoft Foundryにライブ音声エージェントやリリース管理、データ統合、SharePoint連携向けのAIテンプレートがパブリックプレビューで追加。

- 主な変更点や新機能  
再利用可能なカスタマイズ可能テンプレートで、セットアップ工数を削減し迅速な開発を支援。

- 影響を受ける対象  
AIソリューション開発者やDevOpsエンジニア、データ統合担当者。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に検討が必要。

**詳細**:

Microsoft Foundryの新しいAIテンプレートは、ライブボイスエージェント、リリース管理、データ統合、SharePoint連携などの一般的なユースケース向けに設計されたカスタマイズ可能なテンプレート群を提供します。これにより、繰り返し発生するセットアップ作業を自動化し、開発工数を大幅に削減可能です。テンプレートはAzure Cognitive ServicesやAzure Bot Serviceと連携し、音声認識や自然言語処理を活用したインタラクティブなエージェント構築を支援します。リリース管理テンプレートはAzure DevOpsとの統合により、CI/CDパイプラインの効率化を実現。データ統合テンプレートはAzure Data Factoryをベースに複数ソースのデータ統合を容易にします。SharePoint連携テンプレートはMicrosoft Graph APIを活用し、ドキュメント管理やワークフロー自動化を促進します。利用時はテンプレートのカスタマイズ性を活かしつつ、Azureリソースの権限設定やコスト管理に注意が必要です。これらのテンプレートはMicrosoft Foundryの環境内で展開・管理され、Azureの各種サービスとシームレスに統合することで、迅速なAIソリューション開発を可能にします。

---

### 135. Generally Available: Azure Monitor unified onboarding experience for AKS and VMs

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Azure Monitor unified onboarding experience for AKS and VMs](https://azure.microsoft.com/updates?id=521941)

**アップデートID**: 521941
**情報源**: Azure Updates API

**カテゴリ**: Launched, DevOps, Management and governance, Azure Monitor

**要約**:

- 何が更新されたか  
Azure MonitorでAKSクラスターとVM向けの統合オンボーディング機能が一般提供開始。

- 主な変更点や新機能  
単一クリックで最新のAzure Monitor機能を自動展開し、セットアップが大幅に簡素化。

- 影響を受ける対象  
Azure Kubernetes Service利用者およびAzure仮想マシン管理者。

- 注意点  
既存の監視設定との互換性やカスタマイズ要件は事前に確認が必要。

**詳細**:

本アップデートは、Azure MonitorのオンボーディングプロセスをAKSクラスターとVMに対して統合し、運用効率を向上させることを目的としています。従来はAKSとVMで別々に設定が必要だった監視エージェントの導入を、単一のクリック操作で最新のAzure Monitor機能を自動展開する仕組みに刷新しました。具体的には、Azure PortalやCLIからの操作で、Log AnalyticsエージェントやAzure Monitor Container Insightsなどのコンポーネントが一括でデプロイされ、設定ミスや手動作業の負荷を軽減します。技術的には、ARMテンプレートや拡張機能を活用し、リソースグループ単位での一括適用が可能です。活用シナリオとしては、複数のAKSクラスターやVM環境を持つ大規模インフラでの監視導入が迅速化され、運用開始までの時間短縮に寄与します。注意点としては、既存のカスタム設定がある場合は上書きされる可能性があるため、事前の設定確認が必要です。また、対応リージョンやサポートされるVMイメージに制限があるため、公式ドキュメントの確認を推奨します。Azure Monitorの他サービス（Log Analytics、Alerts、Workbooks）と連携し、統合的な運用監視基盤構築が容易になります。

---

### 136. Public Preview: Azure Copilot brings new intelligent agents to support end-to-end lifecycle management of workloads

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Azure Copilot brings new intelligent agents to support end-to-end lifecycle management of workloads](https://azure.microsoft.com/updates?id=520762)

**アップデートID**: 520762
**情報源**: Azure Updates API

**カテゴリ**: In preview, Management and governance, Azure Copilot, Microsoft Ignite, Features

**要約**:

- 何が更新されたか  
Azure Copilotがパブリックプレビューで新たに専門エージェントを導入し、ワークロードの移行・運用・モダナイズを支援。

- 主な変更点や新機能  
GPT-5による高度な推論とアーティファクト生成を活用し、チャットからフルスクリーンのコマンドセンターへ進化。エンドツーエンドのライフサイクル管理が可能に。

- 影響を受ける対象  
Azure上のワークロード管理やモダナイズを担当する技術者・運用者。

- 注意点があれば記載  
専門エージェントはゲーテッドプレビューのため、利用には申請や承認が必要。

**詳細**:

本アップデートは、Azure CopilotにGPT-5ベースの高度なインテリジェントエージェントを導入し、ワークロードの移行・運用・モダナイゼーションを包括的に支援することを目的としています。新たに追加された専門エージェント（ゲーテッドプレビュー）は、ユーザーの対話を超え、フルスクリーンのコマンドセンターとして機能し、複雑なタスクの自動化やアーティファクト生成を実現します。技術的には、GPT-5の推論能力を活用し、Azureリソース管理APIやDevOpsツールと連携して動的に操作指示を生成・実行可能です。活用例としては、オンプレミスからAzureへの移行計画策定、運用中のリソース最適化提案、最新技術へのアップデート支援などが挙げられます。現時点ではゲーテッドプレビューのため利用には申請が必要で、対応リージョンやサービスに制限があります。Azure Monitor、Azure Arc、Azure DevOpsなどと連携し、統合的なライフサイクル管理を実現する点も特徴です。

---

### 137. Public Preview: Dynamic threshold for Log search alerts

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Dynamic threshold for Log search alerts](https://azure.microsoft.com/updates?id=503704)

**アップデートID**: 503704
**情報源**: Azure Updates API

**カテゴリ**: In preview, DevOps, Management and governance, Azure Monitor, Microsoft Ignite, Features

**要約**:

- 何が更新されたか  
Azure MonitorのLog検索アラートに動的閾値機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
ユーザーが閾値を手動設定する必要がなく、システムがログデータに基づき最適な閾値を自動算出します。

- 影響を受ける対象  
Azure MonitorのLog検索アラートを利用する技術者や運用チーム。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に検討してください。  
詳細は公式リンク参照ください。

**詳細**:

本アップデートは、Azure Monitorのログ検索アラートに動的しきい値機能を追加し、従来の静的しきい値設定の課題を解消することを目的としています。動的しきい値は、過去のログデータの傾向や変動を機械学習モデルで解析し、アラート発生に最適なしきい値を自動算出するため、運用負荷の軽減と誤検知の削減が期待できます。実装は、Log Analyticsのクエリ結果に対して動的しきい値アルゴリズムを適用し、異常検知をリアルタイムに行う仕組みです。活用例としては、トラフィック量やエラー数の変動が大きいサービスの監視に適し、静的設定では見逃しや誤警報が発生しやすいケースで効果的です。注意点としては、動的しきい値の学習期間やデータの質に依存するため、初期設定時に十分な履歴データが必要であり、異常検知の感度調整も可能ですが過剰検知のリスクもあります。Azure MonitorやLog Analyticsとシームレスに連携し、既存のアラートルールに動的しきい値を適用できるため、モニタリングの高度化に貢献します。詳細は公式ドキュメント（https://azure.microsoft.com/updates?id=503704）を参照してください。

---

### 138. Generally Available: Custom error pages on Azure App Service

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Generally Available: Custom error pages on Azure App Service](https://azure.microsoft.com/updates?id=492303)

**アップデートID**: 492303
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Mobile, Web, App Service, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure App Serviceでカスタムエラーページ機能が一般提供（GA）となりました。

- 主な変更点や新機能  
アプリケーションで標準のエラーページではなく、任意のカスタムエラーページを設定可能に。ユーザー体験の向上やブランド統一が図れます。

- 影響を受ける対象  
Azure App Service上でWebアプリを運用する開発者・運用者。

- 注意点  
カスタムエラーページの設定方法や対応エラーコードを事前に確認し、適切に実装してください。  

詳細：https://azure.microsoft.com/updates?id=492303

**詳細**:

Azure App Serviceにおいて、カスタムエラーページ機能が一般提供（GA）となりました。本機能は、従来の標準エラーページに代わり、ユーザー体験を向上させるために独自のエラーページを設定可能とするものです。具体的には、HTTPステータスコード（例：404、500など）に応じて任意のHTMLページやURLを指定でき、アプリケーションのブランドイメージを損なわずにエラー対応が可能です。実装はAzureポータル、Azure CLI、またはARMテンプレートを通じて設定でき、App Serviceの「カスタムエラーページ」設定項目に対象ステータスコードと対応ページを登録します。活用例としては、ユーザーにわかりやすいエラーメッセージの表示や、トラブルシューティング用の案内ページへの誘導が挙げられます。注意点として、カスタムエラーページは静的コンテンツである必要があり、動的な処理を含む場合は別途アプリ側で対応が必要です。また、App Serviceの診断ログやApplication Insightsと組み合わせることで、エラー発生時の詳細分析が可能です。さらに、Azure Front DoorやAzure CDNと連携させることで、グローバル配信環境下でも一貫したカスタムエラーページの提供が実現します。詳細は公式ドキュメントを参照してください。

---

### 139. Public Preview: Online container copy in Azure Cosmos DB 

**公開日時**: 2025年11月18日 16:00:16 UTC
**リンク**: [Public Preview: Online container copy in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=467471)

**アップデートID**: 467471
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Internet of Things, Azure Cosmos DB, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Cosmos DBでコンテナ間のデータコピーがオンラインで可能に（Public Preview）。

- 主な変更点や新機能  
稼働中のソースコンテナからリアルタイムにデータを別コンテナへコピーでき、ダウンタイムを最小化。

- 影響を受ける対象  
Cosmos DBを利用し、コンテナ間でデータ移行や複製を行う開発者・運用者。

- 注意点があれば記載  
プレビュー機能のため、本番環境での利用は慎重に。パフォーマンス影響や制限事項を確認のこと。

**詳細**:

Azure Cosmos DBの新機能「オンラインコンテナコピー（Public Preview）」は、コンテナ間のデータ移行時のダウンタイムを最小化することを目的としています。従来はコンテナコピー時にソースコンテナの利用を制限する必要がありましたが、本機能によりリアルタイムでデータを別コンテナへコピー可能となり、アプリケーションの継続稼働が可能です。技術的には、ソースコンテナの変更を継続的に追跡し、差分をターゲットコンテナに反映する仕組みを採用。実装はAzure CLIやAzure Portal、SDK経由で操作可能で、既存のCosmos DBアカウント内のコンテナ間で利用できます。活用例としては、データ移行やバックアップ、テスト環境へのデータ複製が挙げられます。注意点としては、プレビュー段階のため一部リージョンやAPIに制限があり、スループットの影響を考慮する必要があります。Azure FunctionsやAzure Data Factoryと組み合わせることで、コピー完了後の自動処理やパイプライン構築が容易になります。詳細は公式ドキュメントを参照してください。

---

### 140. Generally Available: The Archive access tier for Azure Blob Storage is now generally available in the Taiwan North region

**公開日時**: 2025年11月18日 14:00:03 UTC
**リンク**: [Generally Available: The Archive access tier for Azure Blob Storage is now generally available in the Taiwan North region](https://azure.microsoft.com/updates?id=527181)

**アップデートID**: 527181
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Blob Storage

**要約**:

- 何が更新されたか  
Azure Blob StorageのArchiveアクセス層が台湾北部リージョンで一般提供開始。

- 主な変更点や新機能  
台湾北部リージョンで低頻度アクセス向けのコスト効率の高いArchive層が利用可能に。

- 影響を受ける対象  
台湾のAzureユーザーで、長期保存や低頻度アクセスデータのコスト削減を検討している技術者。

- 注意点があれば記載  
Archive層はデータ取り出しに時間がかかるため、アクセスパターンを考慮して利用を推奨。

**詳細**:

本アップデートにより、Azure Blob StorageのArchiveアクセス層が台湾北部リージョンで一般提供（GA）となりました。これにより、台湾地域の顧客はアクセス頻度の低いデータを低コストで長期保存可能となり、データの地域要件（データレジデンシー）を満たしつつコスト最適化が図れます。Archive層はデータの即時アクセスを想定せず、復元には数時間を要するため、バックアップやアーカイブ用途に適しています。Blobのアクセス層はホット、クール、アーカイブ間で動的に変更可能で、Azure PortalやCLI、REST APIを用いて実装可能です。活用例としては、法規制によりデータを台湾国内に保存しつつ、アクセス頻度が低いログや監査データの保管が挙げられます。注意点として、アーカイブ層からのデータ復元にはリハイドレーション処理が必要で、復元時間やコストが発生するため運用設計時に考慮が必要です。また、Azure Data FactoryやAzure Synapse Analyticsなど他サービスと連携し、データパイプラインの一部としてアーカイブ層を活用することも可能です。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 141. Public preview: Support for large volume breakthrough mode

**公開日時**: 2025年11月18日 14:00:03 UTC
**リンク**: [Public preview: Support for large volume breakthrough mode](https://azure.microsoft.com/updates?id=516656)

**アップデートID**: 516656
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure NetApp Files, Features

**要約**:

- 何が更新されたか  
Azure NetApp FilesのBreakthroughモードがパブリックプレビューで大容量ボリューム（最大2PiB）をサポート開始。

- 主な変更点や新機能  
最大50GiBpsのスループットを実現し、HPCやEDAなど高負荷ワークロードに最適化。

- 影響を受ける対象  
大規模データ処理や高性能ストレージを必要とする技術者・企業。

- 注意点があれば記載  
プレビュー段階のため、商用利用前に制限やサポート状況を確認すること。

**詳細**:

本アップデートは、Azure NetApp FilesのBreakthroughモードにおいて、大容量ボリューム（最大2PiB）と高スループット（最大50GiBps）をパブリックプレビューでサポート開始したものです。背景には、HPC（高性能計算）やEDA（電子設計自動化）など、極めて高いI/O性能と大容量ストレージを必要とするワークロードの増加があります。Breakthroughモードは、従来のモードよりも高いIOPSとスループットを実現するため、NVMeベースの高速ストレージ技術と最適化されたネットワークパスを活用し、ボリュームサイズの拡大と性能向上を両立しています。実装面では、Azure NetApp Filesのファイルシステムが大容量データの並列処理を効率化し、スケールアウト構成をサポートします。活用例としては、シミュレーションデータの高速読み書きやEDA設計データの大規模解析が挙げられます。注意点としては、対応リージョンやサブスクリプションの制限、利用可能なプロトコル（NFSv3/v4.1など）を事前確認する必要があります。また、Azure Compute（VMやAzure Batch）との連携により、HPCクラスターのストレージとして最適化可能で、Azure Monitorによるパフォーマンス監視も推奨されます。詳細は公式ドキュメントで最新情報を確認してください。

---

### 142. Public Preview: Threat Detection in Azure Backup powered by MDC

**公開日時**: 2025年11月18日 13:45:04 UTC
**リンク**: [Public Preview: Threat Detection in Azure Backup powered by MDC](https://azure.microsoft.com/updates?id=520454)

**アップデートID**: 520454
**情報源**: Azure Updates API

**カテゴリ**: In preview, Management and governance, Storage, Azure Backup

**要約**:

- 何が更新されたか  
Azure BackupにMicrosoft Defender for Cloud連携の脅威検出機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
Azure VMバックアップの復元ポイントに対し、マルウェアなどの脅威を検出し、バックアップの健全性を評価可能に。

- 影響を受ける対象  
Azure VMのバックアップを利用しているユーザー。

- 注意点  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

本アップデートは、Azure BackupのAzure VMバックアップに対してMicrosoft Defender for Cloud（MDC）を活用した脅威検出機能をパブリックプレビューで提供開始したものです。背景として、ランサムウェアやマルウェアによるバックアップデータの改ざんリスクが増大しており、バックアップの健全性をリアルタイムに評価・監視するニーズが高まっています。新機能は、Azure VMのバックアップ復元ポイント（RP）をスキャンし、不正な変更や悪意ある活動を検知してアラートを発行します。技術的には、MDCの脅威インテリジェンスと異常検知アルゴリズムを用い、バックアップデータの整合性や異常パターンを分析。検出結果はAzureポータルやMDCのセキュリティアラートとして可視化され、迅速な対応を可能にします。実装はAzure BackupとMDCの統合設定が必要で、MDCの有効化および適切な権限設定を行うことで利用可能です。活用例としては、ランサムウェア攻撃後の復旧準備や定期的なバックアップ健全性チェックが挙げられ、運用負荷軽減とセキュリティ強化に寄与します。注意点としては、現時点でAzure VMバックアップに限定され、他のバックアップタイプは対象外であること、またパブリックプレビューのため仕様変更の可能性がある点に留意が必要です。関連サービスとして、Azure Security Center（MDCの前身）やAzure Monitorと連携し、統合的なセキュリティ管理が可能です。

---

### 143. Public Preview: Query-based metric alerts in Azure Monitor

**公開日時**: 2025年11月18日 08:00:28 UTC
**リンク**: [Public Preview: Query-based metric alerts in Azure Monitor](https://azure.microsoft.com/updates?id=518469)

**アップデートID**: 518469
**情報源**: Azure Updates API

**カテゴリ**: In preview, DevOps, Management and governance, Azure Monitor, Microsoft Ignite, Features

**要約**:

- 何が更新されたか  
Azure Monitorのメトリアラートがパブリックプレビューでクエリベースに対応。

- 主な変更点や新機能  
プラットフォームメトリック、Prometheus、カスタムメトリックを含む全Azureメトリックに対応し、PromQLによる高度なクエリが可能に。

- 影響を受ける対象  
Azure Monitorを利用した監視・アラート設定を行う技術者や運用チーム。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討すること。

**詳細**:

本アップデートにより、Azure MonitorのメトリックアラートはすべてのAzureメトリック（プラットフォームメトリック、Prometheusメトリック、カスタムメトリック）をサポートし、監視範囲が大幅に拡大されました。特にPromQLによるクエリベースのアラート設定がパブリックプレビューで利用可能となり、複雑な条件指定や多次元分析が可能です。技術的には、Azure MonitorのメトリックストアとPrometheus互換のクエリエンジンを統合し、リアルタイムに柔軟なクエリ処理を実現しています。これにより、Kubernetes環境やカスタムアプリケーションの詳細なパフォーマンス監視が容易になります。活用例としては、複数のメトリックを組み合わせた異常検知や、PromQLの強力な集約関数を用いたリソース使用率の高度な分析が挙げられます。注意点としては、パブリックプレビュー段階のため、SLAs未適用や一部機能制限が存在し、運用環境での利用には検証が推奨されます。Azure Monitor AlertsはAzure Metrics AdvisorやLog Analyticsとも連携可能で、統合的な監視・分析基盤構築に寄与します。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2025-11-19 12:29:31 JST*