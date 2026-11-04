# 2026年11月04日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年11月04日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 6 件

## 更新一覧

### 1. Public Preview: JWT validation for Application Gateway for Containers

**公開日時**: 2026年11月03日 21:17:08 UTC
**リンク**: [Public Preview: JWT validation for Application Gateway for Containers](https://azure.microsoft.com/updates?id=576382)

**アップデートID**: 576382
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Application Gateway, Features

**要約**:

【何が更新されたか】  
Application Gateway for Containersにおいて、JWT（JSON Web Token）バリデーション機能がパブリックプレビューとして追加されました。

【主な変更点や新機能】  
AuthPolicyカスタムリソースを利用することで、JWTの署名、発行者（issuer）、有効期限（lifetime）、および指定されたaudienceの検証が可能になりました。署名鍵は信頼できるHTTPエンドポイントから取得できます。これにより、認証処理をゲートウェイ側で一元管理でき、アプリケーションごとに認証ロジックを実装する必要がなくなります。

【影響を受ける対象】  
Application Gateway for Containersを利用している開発チームや運用担当者が対象です。特に、APIやWebサービスの認証強化を検討している技術者にとって重要なアップデートです。

【注意点】  
本機能はパブリックプレビュー段階のため、商用利用時には十分な検証が必要です。また、AuthPolicyの設定や署名鍵の管理方法について公式ドキュメントを参照し、セキュリティ要件を満たすよう注意してください。

**詳細**:

Azure Application Gateway for Containersにおいて、JSON Web Token（JWT）検証機能がAuthPolicyカスタムリソースを通じて新たにサポートされ、パブリックプレビューとして提供されています。このアップデートの背景には、コンテナベースのアプリケーション環境における認証・認可の強化と、セキュリティ管理の一元化を実現する目的があります。従来、アプリケーションごとに個別にJWT検証を実装する必要がありましたが、今回の機能追加により、Application Gateway for Containers上で中央集権的にJWT検証を行うことが可能となります。

具体的な機能としては、AuthPolicyカスタムリソースを利用して、JWTの署名、発行者（issuer）、有効期間（lifetime）、および設定されたaudience（受信者）の検証を実施できます。署名検証に必要な鍵は、信頼できるHTTPエンドポイントから取得される仕組みとなっており、これにより外部の認証基盤と連携したセキュアなトークン検証が実現されます。技術的には、Application Gateway for Containersがリクエストを受けた際に、AuthPolicyで定義された条件に基づきJWTを解析し、署名や各種クレームの検証を行います。検証に失敗した場合はリクエストを拒否し、成功した場合のみバックエンドサービスへ転送されます。

この機能は、複数チームやサービスが同一のApplication Gateway for Containersを利用する場合に、認証ポリシーを統一して管理する際に有効です。例えば、マイクロサービスアーキテクチャで複数のAPIが存在する場合、各APIで個別にJWT検証を実装する必要がなくなり、ゲートウェイ側で一括して認証処理を行うことで、開発・運用の効率化やセキュリティレベルの均一化が図れます。

注意点としては、パブリックプレビュー段階であるため、本番環境での利用は慎重に検討する必要があります。また、AuthPolicyカスタムリソースの設定や、署名鍵の取得先となるHTTPエンドポイントの信頼性・可用性にも十分配慮する必要があります。関連するAzureサービスとしては、Azure Active Directoryや他の認証基盤と連携することで、より高度な認証・認可シナリオを構築することが可能です。

以上のように、今回のアップデートはApplication Gateway for Containersのセキュリティ機能強化に寄与し、認証処理の一元化による運用効率向上と、Azure環境におけるマイクロサービスのセキュアな運用を支援するものです。

---

### 2. Public Preview: MCP gateway for Application Gateway for Containers

**公開日時**: 2026年11月03日 21:16:36 UTC
**リンク**: [Public Preview: MCP gateway for Application Gateway for Containers](https://azure.microsoft.com/updates?id=576388)

**アップデートID**: 576388
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Application Gateway, Features

**要約**:

【何が更新されたか】  
Application Gateway for Containersにおいて、MCP（Model Context Protocol）ゲートウェイ機能がパブリックプレビューとして追加されました。

【主な変更点や新機能】  
新たにMCPRouteというカスタムリソースが導入され、MCPサーバーへのルーティングが可能になりました。これにより、プラットフォームチームは安定したホスト名やパスの背後にMCPサーバーを公開でき、TLS終端、JWT認証、Web Application Firewall（WAF）などのセキュリティ機能を中央管理することができます。

【影響を受ける対象】  
Application Gateway for Containersを利用している技術者やプラットフォーム管理者が対象です。特にMCPプロトコルを活用したアプリケーションの運用やセキュリティ管理を行う場合に恩恵があります。

【注意点】  
本機能はパブリックプレビュー段階のため、本番環境での利用には注意が必要です。正式リリース前の機能であるため、サポートや安定性について十分に確認してください。

**詳細**:

本アップデートは、Application Gateway for ContainersにおいてMCP（Model Context Protocol）ゲートウェイのパブリックプレビューが開始されたことを示しています。これにより、MCPRouteという新しいカスタムリソースを用いたMCPプロトコルによるルーティングがサポートされます。アップデートの目的は、プラットフォームチームがMCPサーバーを安定したホスト名とパスの背後に公開し、TLS終端、JWT認証、Web Application Firewall（WAF）などのセキュリティ機能を集約して管理できるようにすることです。

具体的な機能としては、MCPRouteカスタムリソースを利用することで、Application Gateway for ContainersがMCPプロトコルに基づいたルーティングを実現します。これにより、従来のHTTPやHTTPSルーティングだけでなく、MCPプロトコルを用いたサービス公開が可能となります。また、TLS終端やJWT認証、WAFを中央集権的に設定できるため、セキュリティポリシーの一貫性と運用効率が向上します。

技術的な仕組みとしては、MCPRouteカスタムリソースをKubernetes上で定義し、Application Gateway for Containersがその設定を参照してMCPプロトコルのルーティングを行います。これにより、プラットフォームチームはMCPサーバーのエンドポイントを安定したホスト名とパスで公開でき、バックエンドサービスの変更や拡張にも柔軟に対応できます。TLS終端やJWT認証、WAFの設定はApplication Gateway側で集中管理されるため、各サービスごとに個別設定する必要がなくなります。

活用シナリオとしては、複数のMCPサーバーを運用する場合に、各サーバーを安定したホスト名とパスで公開し、セキュリティ機能を一元管理したい場合に有効です。例えば、マイクロサービスアーキテクチャを採用している環境で、各サービスがMCPプロトコルを利用している場合、Application Gateway for Containersを利用することで、運用負荷を軽減しつつセキュリティを強化できます。

注意点や制限事項としては、現在パブリックプレビュー段階であるため、本番環境での利用には慎重な検討が必要です。また、MCPRouteカスタムリソースやMCPプロトコルの詳細な仕様については公式ドキュメントを参照する必要があります。今後のアップデートや機能追加にも留意する必要があります。

関連するAzureサービスとしては、Application Gateway for Containers自体がAzure Kubernetes Service（AKS）などのコンテナ基盤と連携して動作します。また、TLS終端やWAF、JWT認証などのセキュリティ機能は、Azureのセキュリティサービスと統合されているため、既存のAzureインフラストラクチャとシームレスに連携できます。

---

### 3. Public Preview: Private ingress for Application Gateway for Containers

**公開日時**: 2026年11月03日 21:15:46 UTC
**リンク**: [Public Preview: Private ingress for Application Gateway for Containers](https://azure.microsoft.com/updates?id=576393)

**アップデートID**: 576393
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Application Gateway, Features

**要約**:

【何が更新されたか】  
Application Gateway for Containersにおいて、プライベートインフラ（Private ingress）がパブリックプレビューとして利用可能になりました。

【主な変更点や新機能】  
このアップデートにより、Application Gateway for ContainersのフロントエンドをAzure Private Linkのプライベートエンドポイント経由でのみアクセス可能にすることができます。これにより、内部アプリケーションや共有サービス、クラスタ間のトラフィックをパブリックネットワークから隔離し、セキュリティを強化することが可能です。

【影響を受ける対象】  
Azure上でApplication Gateway for Containersを利用している組織や、内部向けのアプリケーションやサービスをプライベートネットワークで運用したい技術者が対象となります。

【注意点】  
本機能はパブリックプレビュー段階のため、本番環境での利用には慎重な検討が必要です。また、Azure Private Linkの設定やエンドポイント管理が必要となるため、関連するネットワーク構成や権限管理にも注意してください。

**詳細**:

Azure Application Gateway for Containersにおいて、Private ingressの機能がパブリックプレビューとして提供開始されました。本アップデートの背景には、企業や組織が内部アプリケーションや共有サービス、クラスタ間通信などのトラフィックを完全にプライベートなネットワーク上で管理したいというニーズがあります。従来、Application Gateway for Containersはパブリックなフロントエンドを通じてアクセスされることが一般的でしたが、今回のアップデートにより、Azure Private Linkのプライベートエンドポイントを利用した限定的なアクセスが可能となりました。

具体的な機能としては、Application Gateway for Containersのフロントエンドをプライベート化し、承認されたAzure Private Linkのプライベートエンドポイント経由のみでアクセスできるようになります。これにより、外部からのアクセスを遮断し、内部ネットワークや特定のAzureリソースからのみトラフィックを受け付ける構成が実現できます。技術的な仕組みとしては、Application Gateway for ContainersがAzure Private Linkと連携し、プライベートエンドポイントを介してトラフィックを受け入れることで、ネットワークの分離とセキュリティ強化が可能となります。

実装方法としては、Application Gateway for Containersの設定時にフロントエンドをプライベートとして構成し、Azure Private Linkのプライベートエンドポイントを作成・関連付ける必要があります。これにより、アクセス制御やネットワークポリシーの適用が容易になり、内部アプリケーションや共有サービスのセキュアな公開が可能となります。

活用シナリオとしては、社内向けの業務アプリケーションや、複数クラスタ間で共有されるサービスへのアクセスを完全にプライベートネットワーク内で管理したい場合に有効です。また、セキュリティ要件が高い環境や、外部からのアクセスを厳格に制限したい場合にも適しています。

注意点としては、パブリックプレビュー段階であるため、機能やサポート範囲に制限がある可能性があります。運用環境での利用に際しては、公式ドキュメントやサポート情報を十分に確認することが重要です。

関連するAzureサービスとしては、Azure Private Linkが主要な連携先となります。これにより、Application Gateway for Containersと他のAzureリソース間のプライベート通信が実現し、ネットワークセキュリティの向上とアクセス制御の強化が可能となります。

---

### 4. Public Preview: Advanced capacity insights are now available in Azure Storage Discovery

**公開日時**: 2026年11月03日 20:20:29 UTC
**リンク**: [Public Preview: Advanced capacity insights are now available in Azure Storage Discovery](https://azure.microsoft.com/updates?id=578655)

**アップデートID**: 578655
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Storage Accounts, Azure Storage Discovery, Feature

**要約**:

【何が更新されたか】  
Azure Storage Discoveryに「高度な容量インサイト」がパブリックプレビューとして追加されました。

【主な変更点や新機能】  
今回のアップデートにより、ストレージ利用状況の可視化が強化されました。具体的には、アクセスパターン、データの経過年数、ストレージ階層、オブジェクトサイズ分布、保持期間などの詳細なインサイトが提供されます。これにより、ストレージの最適化やコスト管理、データライフサイクル管理がより効率的に行えるようになります。

【影響を受ける対象】  
Azure Storage Discoveryを利用している技術者やストレージ管理者が対象です。特に、ストレージリソースの運用や最適化に関わる方にとって有用な機能です。

【注意点】  
本機能は現在パブリックプレビュー段階のため、正式リリース前の機能となります。運用環境で利用する際は、プレビュー機能であることを考慮し、十分な検証を行ってください。

**詳細**:

Azure Storage Discoveryにおいて、Advanced capacity insightsがパブリックプレビューとして利用可能になりました。このアップデートの背景は、Azureストレージの利用状況をより詳細に把握し、効率的な管理や最適化を支援することにあります。従来のストレージ管理機能では、容量や基本的な使用状況の把握に留まっていましたが、今回のアップデートにより、アクセスパターンやデータの経過年数、ストレージ階層、オブジェクトサイズの分布、保持期間など、より多角的な視点からストレージの利用状況を分析できるようになりました。

具体的な機能としては、Storage Discoveryが提供するインサイトの範囲が拡張され、ストレージ内のデータがどのようにアクセスされているか、どれくらい古いデータが存在しているか、どのストレージ階層にどれだけのデータが格納されているか、オブジェクトサイズの分布やデータの保持期間など、詳細な容量分析が可能となっています。これにより、ストレージの最適化やコスト管理、パフォーマンス向上のための意思決定を支援します。

技術的な仕組みとしては、Azure Storage Discoveryがストレージアカウント内のメタデータやアクセスログなどを解析し、各種インサイトを生成しています。これらの情報はAzureポータル上で可視化され、管理者や運用担当者が容易に利用状況を把握できるようになっています。

活用シナリオとしては、ストレージの容量管理やコスト最適化、データのライフサイクル管理、アクセス頻度に応じたストレージ階層の見直し、不要データの削除やアーカイブ化などが挙げられます。例えば、アクセス頻度の低い古いデータを低コストのストレージ階層へ移動する判断や、オブジェクトサイズの分布を分析してパフォーマンスチューニングを行う際に有効です。

注意点としては、現時点ではパブリックプレビューであるため、機能やインサイトの精度、対応範囲に制限がある可能性があります。また、プレビュー期間中は商用環境での利用や運用に際して十分な検証が必要です。

関連するAzureサービスとしては、Azure Storage全般（Blob Storage、File Storageなど）との連携が前提となっており、ストレージアカウントの管理やデータ分析、コスト管理などの用途で利用されます。今回のアップデートは、ストレージ管理の高度化を目指す技術者にとって、運用効率化やコスト削減のための有用な情報を提供するものです。

---

### 5. Public Preview: Extend immutability for PITR backups for Azure SQL Database and Azure SQL Managed Instance

**公開日時**: 2026年11月03日 18:36:12 UTC
**リンク**: [Public Preview: Extend immutability for PITR backups for Azure SQL Database and Azure SQL Managed Instance](https://azure.microsoft.com/updates?id=579305)

**アップデートID**: 579305
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance, Feature

**要約**:

- 何が更新されたか  
Azure SQL DatabaseおよびAzure SQL Managed InstanceのPITR（Point-In-Time Restore）バックアップに対して、イミュータブル（変更不可）期間を拡張できる機能がパブリックプレビューとして提供されました。

- 主な変更点や新機能  
従来はイミュータブルバックアップの保持期間がデフォルトで7日間でしたが、今回のアップデートにより、設定したPITR保持期間までイミュータブル状態をロックできるようになりました。これにより、バックアップの改ざん防止が強化され、より長期間のデータ保護が可能となります。

- 影響を受ける対象  
Azure SQL DatabaseおよびAzure SQL Managed Instanceを利用しているユーザーが対象です。特に金融業界など、35日間以上のバックアップ保持が求められるケースで有用です。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用には慎重な検討が必要です。設定したイミュータブル期間中はバックアップの削除や変更ができませんので、運用時の保持期間設定に注意してください。

**詳細**:

本アップデートは、Azure SQL DatabaseおよびAzure SQL Managed Instanceにおけるポイントインタイムリストア（PITR）バックアップのイミュータビリティ（不変性）期間を拡張する機能のパブリックプレビューです。従来、イミュータブルなバックアップはデフォルトで7日間保持されていましたが、この拡張により、ユーザーは自身が設定したPITRバックアップ保持期間に合わせてイミュータビリティをロックできるようになりました。これにより、金融業界など、長期間のバックアップ保持が求められる顧客にとって、バックアップの改ざん防止とコンプライアンス要件への対応が容易になります。

具体的な機能としては、PITRバックアップの保持期間を設定する際、その期間全体に対してバックアップのイミュータビリティを適用できるようになります。これにより、バックアップデータが設定期間中は変更や削除ができない状態となり、データの安全性と信頼性が向上します。既存の7日間のイミュータブルバックアップに加えて、例えば金融業界で一般的な35日間の保持期間にも対応できるため、業界ごとの規制や社内ポリシーに柔軟に対応可能です。

技術的な仕組みとしては、Azure SQL DatabaseおよびAzure SQL Managed Instanceのバックアップ管理機能において、PITRバックアップの保持期間設定とイミュータビリティ設定が連動します。管理者はAzure PortalやAPIを通じて保持期間を指定し、その期間に対してイミュータビリティを有効化することで、バックアップデータの不変性を保証できます。バックアップデータはAzureのストレージ上で管理され、イミュータビリティ設定が適用されることで、期間中の削除や変更が制限されます。

活用シナリオとしては、金融機関や医療機関など、長期間のバックアップ保持とデータ改ざん防止が求められるケースで有効です。例えば、法令や監査要件により35日間以上のバックアップ保持が必要な場合、今回の機能拡張によってその期間中のバックアップデータの不変性を確保できます。また、内部統制やセキュリティ強化の観点からも、バックアップのイミュータビリティは重要な役割を果たします。

注意点としては、イミュータビリティを設定したバックアップは保持期間中に削除や変更ができないため、設定前に保持期間や運用方針を十分に検討する必要があります。また、パブリックプレビュー段階であるため、正式リリース前の機能制限や仕様変更の可能性がある点にも留意してください。

本機能はAzure SQL DatabaseおよびAzure SQL Managed Instanceのバックアップ管理機能と密接に連携しており、Azureのセキュリティやコンプライアンス機能と組み合わせることで、より高度なデータ保護と運用管理が実現できます。

---

### 6. Generally Available: Enhanced Azure Site Recovery support for VMSS Flex

**公開日時**: 2026年11月03日 18:32:01 UTC
**リンク**: [Generally Available: Enhanced Azure Site Recovery support for VMSS Flex](https://azure.microsoft.com/updates?id=578926)

**アップデートID**: 578926
**情報源**: Azure Updates API

**カテゴリ**: Launched, Management and governance, Migration, Azure Site Recovery, Feature

**要約**:

- 何が更新されたか  
Azure Site Recoveryが、Virtual Machine Scale Sets（VMSS）Flex構成の仮想マシンに対して、災害復旧機能の強化を一般提供（GA）しました。

- 主な変更点や新機能  
今回のアップデートにより、VMSS Flex環境でのターゲット構成やエンドツーエンドのリカバリワークフロー（フェールオーバー、再保護など）が改善されました。これにより、柔軟なオーケストレーションを利用したVMSSの災害復旧プロセスがより効率的かつ信頼性の高いものになります。

- 影響を受ける対象  
VMSS Flex構成で運用している仮想マシンをAzure Site Recoveryで保護・管理しているユーザーやシステムが対象となります。

- 注意点があれば記載  
本アップデートはVMSS Flex構成のみに適用されます。従来のVMSS Uniform構成には影響しません。既存のSite Recovery設定を利用している場合は、今回の強化点を活用するために設定の見直しやテストを推奨します。  

詳細は公式情報（https://azure.microsoft.com/updates?id=578926）をご参照ください。

**詳細**:

本アップデートは、Azure Site Recovery（ASR）がVirtual Machine Scale Sets（VMSS）のフレキシブルオーケストレーションモデル（VMSS Flex）に対して、より強化されたディザスターリカバリー機能を一般提供したことを示しています。従来、ASRは主に従来型のVMSSや単一の仮想マシンに対する災害復旧をサポートしていましたが、今回のアップデートにより、柔軟なスケーリングや多様な構成が可能なVMSS Flex環境にも対応が拡張されました。

具体的な機能強化としては、ターゲット構成の改善や、フェールオーバー、再保護などのエンドツーエンドのリカバリーワークフローが最適化されています。これにより、VMSS Flex上の仮想マシンに対しても、ASRを用いた効率的かつ信頼性の高いディザスターリカバリーが実現できます。たとえば、フェールオーバー時の自動化や、復旧後の再保護プロセスがよりシームレスに実行されるようになっています。

技術的な仕組みとしては、ASRがVMSS Flexの構成情報やスケールセット内の各仮想マシンの状態を正確に把握し、必要なレプリケーションや復旧手順を自動化することで、運用負荷を軽減しています。これにより、複数インスタンスの大規模なスケールセット環境でも、迅速かつ一貫性のある復旧が可能です。

活用シナリオとしては、可用性やスケーラビリティを重視してVMSS Flexを利用しているミッションクリティカルなアプリケーションやサービスにおいて、災害発生時の業務継続性を担保するためにASRを組み合わせるケースが挙げられます。たとえば、複数リージョンでの冗長構成や、計画的なフェールオーバーテストなどにも有効です。

注意点としては、VMSS Flex特有の構成や運用ポリシーに依存する部分があるため、ASRの導入前には公式ドキュメントで対応バージョンやサポートされる機能範囲を確認する必要があります。また、従来型VMSSとの違いを理解し、適切な運用設計を行うことが重要です。

関連するAzureサービスとしては、Azure BackupやAzure Monitorなどと連携することで、より包括的なBCP（事業継続計画）ソリューションを構築できます。ASRはこれらのサービスと組み合わせることで、監視・通知・バックアップといった多層的な保護体制を実現します。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=578926）をご参照ください。

---


*このレポートは自動生成されました - 2026-11-04 12:02:07 JST*