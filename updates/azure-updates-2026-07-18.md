# 2026年07月18日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年07月18日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Generally Available: Azure Functions support for Python 3.14

**公開日時**: 2026年07月17日 17:47:00 UTC
**リンク**: [Generally Available: Azure Functions support for Python 3.14](https://azure.microsoft.com/updates?id=567646)

**アップデートID**: 567646
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Internet of Things, Azure Functions, Open Source, Services, Feature

**要約**:

- 何が更新されたか  
Azure FunctionsでPython 3.14のサポートが一般提供（GA）されました。

- 主な変更点や新機能  
開発者はPython 3.14を使用してローカルで関数を開発し、LinuxベースのAzure Functionsプランにデプロイできるようになりました。これにより、Python 3.14の強化されたセキュリティ機能や、より長いサポート期間、Azure Functionsとの継続的な互換性を活用できます。

- 影響を受ける対象  
Azure Functionsを利用している技術者や開発者、特にPythonでサーバーレスアプリケーションを構築している方が対象です。既存のPythonアプリケーションを3.14にアップグレードすることで、最新の機能やセキュリティ向上の恩恵を受けられます。

- 注意点があれば記載  
Python 3.14へのアップグレード時には、依存パッケージや既存コードの互換性を事前に確認することを推奨します。また、Linuxプランのみの対応となるため、Windowsプランでは利用できません。

**詳細**:

Azure FunctionsにおいてPython 3.14のサポートが一般提供（Generally Available）となりました。本アップデートの背景として、Azure Functionsはさまざまなプログラミング言語をサポートしており、Pythonの新バージョンへの対応は、セキュリティ強化や長期的なサポート、最新機能の利用を目的としています。これにより、開発者はローカル環境でPython 3.14を用いて関数を開発し、Linux上のAzure Functionsプランへデプロイすることが可能となりました。

具体的な変更内容としては、Azure FunctionsのランタイムがPython 3.14を正式にサポートするようになった点が挙げられます。これにより、Python 3.14の新機能や改善点を活用した関数開発が可能となり、従来のバージョンよりも強化されたセキュリティや、より長いサポート期間を享受できます。また、Azure Functionsの既存の機能やサービスとの互換性も維持されており、既存のワークフローやツールチェーンを活用した開発が継続できます。

技術的な仕組みとしては、開発者はローカル環境にPython 3.14をインストールし、Azure Functions Core Toolsを用いて関数アプリケーションを作成・テストします。その後、Azure CLIやVisual Studio Codeなどのツールを利用して、LinuxベースのAzure Functionsプランへデプロイします。これにより、クラウド上でPython 3.14のランタイムが動作し、関数が実行されます。

活用シナリオとしては、最新のPython機能を必要とするデータ処理やAPIバックエンド、イベント駆動型のアプリケーションなどが考えられます。特に、セキュリティやサポート期間を重視する企業や、Python 3.14固有の機能を利用したい開発者にとって有用です。

注意点としては、現時点でサポートされるのはLinux上のAzure Functionsプランのみであり、Windows上のプランについては言及されていません。また、既存のPythonバージョンからアップグレードする際には、依存パッケージやコードの互換性を事前に確認する必要があります。

関連するAzureサービスとしては、Azure Logic AppsやAzure Event Grid、Azure Storageなどと組み合わせることで、より複雑なイベント駆動型アーキテクチャを構築することが可能です。これらのサービスとの連携も、Python 3.14対応によって今後さらに拡張されることが期待されます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=567646）をご参照ください。

---

### 2. Public Preview: Azure Functions Support for PowerShell 7.6 

**公開日時**: 2026年07月17日 17:44:00 UTC
**リンク**: [Public Preview: Azure Functions Support for PowerShell 7.6 ](https://azure.microsoft.com/updates?id=567651)

**アップデートID**: 567651
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Internet of Things, Azure Functions, Security, Services, Feature

**要約**:

【何が更新されたか】  
Azure FunctionsでPowerShell 7.6のサポートがパブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
これまでのPowerShellバージョンに加え、PowerShell 7.6を利用してローカルでアプリケーションを開発し、Azure Functionsプランにデプロイできるようになりました。これにより、最新のPowerShell機能や改善点を活用したサーバーレスアプリケーションの構築が可能です。

【影響を受ける対象】  
PowerShellを利用してAzure Functionsを開発・運用している技術者や、最新のPowerShellバージョンを必要とする開発チームが対象となります。

【注意点】  
本機能はパブリックプレビュー段階のため、商用環境での利用は慎重に検討してください。今後の正式リリースに向けて仕様変更や追加機能が発生する可能性があります。詳細や制限事項については公式ドキュメントをご確認ください。

**詳細**:

本アップデートは、Azure FunctionsにおけるPowerShell 7.6のサポートがパブリックプレビューとして提供開始されたことを示しています。これにより、開発者はPowerShell 7.6を用いたアプリケーションをローカル環境で開発し、そのままAzure Functionsの各種プランにデプロイできるようになりました。Azure Functionsはイベントドリブンなサーバーレスコンピューティングサービスであり、従来からPowerShellをランタイムとしてサポートしてきましたが、今回のアップデートにより、最新のPowerShell 7.6ランタイムを活用した開発が可能となります。

具体的な機能としては、PowerShell 7.6の新機能や言語仕様を活かしたFunction Appの作成・実行が可能となり、ローカル開発環境での動作検証後、Azure上のFunction Appにシームレスにデプロイできます。これにより、最新のPowerShellモジュールやコマンドレットを利用した自動化処理や、複雑なワークフローの構築が容易になります。技術的には、Azure FunctionsのランタイムがPowerShell 7.6に対応したことで、Function Appのホスト環境で該当バージョンのPowerShellが動作し、従来のバージョンとの互換性も維持されます。

実装方法としては、開発者はローカルマシンにPowerShell 7.6をインストールし、Azure Functions Core Toolsを用いてFunction Appを作成します。その後、Azure CLIやVisual Studio Codeの拡張機能を利用して、Azure上のFunction Appにデプロイすることができます。これにより、ローカルとクラウド間で一貫した動作検証が可能です。

活用シナリオとしては、インフラストラクチャの自動化や運用管理タスクの自動実行、外部システムとの連携処理などが挙げられます。たとえば、Azure AutomationやLogic Appsと連携し、イベント発生時にPowerShellスクリプトを実行することで、柔軟な自動化ソリューションを構築できます。

注意点としては、本機能は現時点でパブリックプレビューであり、運用環境での利用には慎重な検証が必要です。また、プレビュー版のため、今後の正式リリース時に仕様変更や追加機能が発生する可能性があります。既存のFunction AppをPowerShell 7.6へ移行する場合は、互換性や依存モジュールの対応状況を事前に確認することが重要です。

関連するAzureサービスとしては、Azure Logic AppsやAzure Event Grid、Azure Monitorなどが挙げられます。これらのサービスと組み合わせることで、イベント駆動型の自動化や監視、通知など、より高度なクラウドネイティブなシナリオに対応できます。

詳細は公式ドキュメントおよびアップデート情報（https://azure.microsoft.com/updates?id=567651）を参照してください。

---

### 3. Generally Available: Microsoft Defender security assessments for Azure Database for PostgreSQL Flexible Server 

**公開日時**: 2026年07月17日 14:55:28 UTC
**リンク**: [Generally Available: Microsoft Defender security assessments for Azure Database for PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=567527)

**アップデートID**: 567527
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Feature

**要約**:

【何が更新されたか】  
Microsoft Defender Cloud Security Posture Management（CSPM）によるAzure Database for PostgreSQL Flexible Server向けのセキュリティ評価機能が一般提供（GA）されました。

【主な変更点や新機能】  
CSPMの評価機能を利用することで、Azure Database for PostgreSQL Flexible Serverのセキュリティ状態を継続的に監査・評価できるようになりました。これにより、セキュリティベストプラクティスへの準拠状況や潜在的なリスクを自動的に検出し、改善策を提示することが可能です。

【影響を受ける対象】  
Azure Database for PostgreSQL Flexible Serverを利用している環境が対象となります。特に、セキュリティ管理や運用を担当する技術者にとって有用な機能です。

【注意点】  
この機能を利用するにはMicrosoft Defender for Cloudが有効化されている必要があります。導入後は定期的な評価結果の確認と、推奨される対策の実施を行うことが推奨されます。

**詳細**:

Microsoft Defender Cloud Security Posture Management（CSPM）によるAzure Database for PostgreSQL Flexible Server向けのセキュリティアセスメントが一般提供（GA）となりました。このアップデートの背景には、クラウド環境におけるデータベースのセキュリティ強化と、継続的なセキュリティ状態の可視化・評価のニーズがあります。特に、Azure Database for PostgreSQL Flexible Serverは柔軟なスケーリングや高可用性を提供する一方、セキュリティ管理の複雑さが増しているため、CSPMによる自動化された評価機能の導入が重要となっています。

具体的な機能としては、Microsoft Defender CSPMがAzure Database for PostgreSQL Flexible Serverのセキュリティ状態を継続的に評価し、ベストプラクティスに基づくアセスメント結果を提供します。これにより、設定ミスや脆弱性、コンプライアンス違反などのリスクを早期に検出し、対策を講じることが可能です。アセスメントはAzureポータルやAPIを通じて確認でき、推奨事項や改善点が提示されます。

技術的な仕組みとしては、Microsoft Defender CSPMがAzureリソースの構成情報を収集し、既定のセキュリティ基準やポリシーと照合します。評価結果はセキュリティスコアやアラートとして表示され、管理者はこれらの情報をもとにリソースの設定変更や追加対策を実施できます。アセスメントは自動的に実行されるため、手動による監査作業を大幅に削減できます。

活用シナリオとしては、企業のセキュリティ担当者がAzure Database for PostgreSQL Flexible Serverの状態を定期的に監査し、リスク管理やコンプライアンス対応を効率化するケースが挙げられます。また、DevOpsチームがCI/CDパイプラインの一部としてアセスメント結果を活用し、リリース前のセキュリティチェックを自動化することも可能です。

注意点としては、アセスメント結果は推奨事項であり、すべての指摘事項が必ずしも業務要件に適合するとは限りません。評価内容を確認し、必要に応じて例外設定やポリシー調整を行うことが求められます。また、CSPMの利用にはMicrosoft Defenderのライセンスが必要となる場合があります。

関連するAzureサービスとの連携としては、Microsoft Defender for CloudやAzure Policyと組み合わせることで、より包括的なセキュリティ管理が実現できます。これにより、複数のAzureリソースに対して統一的なセキュリティポスチャー管理が可能となり、全社的なセキュリティ強化につながります。

---

### 4. Generally Available: Encryption in Transit for Azure Files NFS Shares in Azure Kubernetes Service (AKS)

**公開日時**: 2026年07月17日 14:54:09 UTC
**リンク**: [Generally Available: Encryption in Transit for Azure Files NFS Shares in Azure Kubernetes Service (AKS)](https://azure.microsoft.com/updates?id=567787)

**アップデートID**: 567787
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Compute, Containers, Azure Files, Azure Kubernetes Service (AKS), Security, Feature

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）で、Azure Files NFS v4.1ボリュームに対する「Encryption in Transit（EiT）」が一般提供（GA）されました。これにより、Azure File CSIドライバー経由でAKSワークロードとAzure Files NFS共有間の通信が暗号化されます。

- 主な変更点や新機能  
EiTが有効化されたことで、AKSからAzure Files NFS v4.1へデータ転送時にTLSによる暗号化が適用されます。これにより、ネットワーク経由のデータ漏洩リスクが低減し、セキュリティが強化されます。

- 影響を受ける対象  
AKS環境でAzure Files NFS v4.1ボリュームを利用しているユーザーや、Azure File CSIドライバーを使用してストレージをマウントしている技術者が対象です。

- 注意点があれば記載  
EiTを利用する際は、AKSクラスターやストレージ構成が最新のAzure File CSIドライバーに対応していることを確認してください。また、暗号化の有効化に伴うパフォーマンスや互換性への影響についても事前に検証することを推奨します。

**詳細**:

Azure Kubernetes Service（AKS）において、Azure Files NFS v4.1ボリュームの「Encryption in Transit（EiT）」が一般提供となりました。本アップデートは、Azure File CSIドライバーを利用したAKSワークロードとAzure Files NFS共有間のデータ転送時に、TLS（Transport Layer Security）による暗号化を適用する機能を正式にサポートするものです。これにより、クラウドネイティブなアプリケーションが機密性の高いデータを安全にやり取りできるようになり、セキュリティ要件の厳しい業界やユースケースにも対応可能となります。

具体的には、AKS上のPodからAzure Files NFS v4.1ボリュームへアクセスする際、従来は転送中のデータが暗号化されていない場合がありましたが、今回のEiTサポートにより、転送経路上のデータがTLSによって暗号化されます。これにより、ネットワーク上での盗聴や改ざんリスクが大幅に低減されます。実装方法としては、Azure File CSIドライバーの設定によりEiTを有効化することで、AKSとAzure Files間の通信が自動的にTLSで保護されます。ユーザーは、PodのPersistentVolumeClaim（PVC）でAzure Files NFS v4.1を指定し、CSIドライバーのバージョンや設定項目を確認することで、EiTの有効化を実現できます。

活用シナリオとしては、金融や医療などの業界で、AKS上で稼働するアプリケーションがAzure Files NFS共有を利用する場合、転送中のデータの暗号化が必須となるケースに適しています。また、コンプライアンス要件を満たすために、データの安全な移動を求める企業にも有効です。例えば、機密性の高いログデータやユーザーファイルをAKSからAzure Files NFSへ保存する際、EiTによりセキュリティを担保できます。

注意点としては、EiTが有効化されていることを確認するために、CSIドライバーのバージョンや設定を適切に管理する必要があります。また、TLS暗号化による通信のオーバーヘッドが発生するため、パフォーマンスへの影響を考慮する必要があります。さらに、Azure Files NFS v4.1のみが対象であり、他のプロトコルやバージョンでは本機能が利用できない点に注意が必要です。

関連するAzureサービスとしては、AKSとAzure Filesの連携が中心となりますが、Azure File CSIドライバーが両者の橋渡し役を担っています。これにより、AKSのコンテナワークロードからAzure Files NFS共有への安全なアクセスが可能となり、クラウドネイティブなストレージソリューションのセキュリティ強化に寄与します。

---


*このレポートは自動生成されました - 2026-07-18 12:01:34 JST*