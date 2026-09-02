# 2026年09月02日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年09月02日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 9 件

## 更新一覧

### 1. Generally Available: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)

**公開日時**: 2026年09月01日 22:34:43 UTC
**リンク**: [Generally Available: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)](https://azure.microsoft.com/updates?id=570282)

**アップデートID**: 570282
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Container Apps, Feature

**要約**:

【何が更新されたか】  
Microsoft Defender for CloudがAzure Container Apps環境のServerless Containers Posture管理に対応し、一般提供（GA）となりました。

【主な変更点や新機能】  
Azure Container AppsをMicrosoft Defender for CloudのServerless Containers Posture管理ワークフローに統合できるようになりました。これにより、セキュリティチームは複数のコンテナ環境のセキュリティポスチャーを一元的に管理・監視できるようになります。

【影響を受ける対象】  
Azure Container Appsを利用している組織や、Microsoft Defender for Cloudを導入しているセキュリティ担当者・運用管理者が対象です。特にサーバーレスコンテナのセキュリティ管理を強化したい技術者にとって重要なアップデートです。

【注意点】  
新機能を利用するには、Microsoft Defender for Cloudの設定やAzure Container Apps環境の適切な構成が必要です。既存のセキュリティポリシーやワークフローへの影響を事前に確認してください。

**詳細**:

本アップデートは、Microsoft Defender for CloudにおいてAzure Container Apps環境のサポートが一般提供（GA）されたことを示しています。これにより、セキュリティチームはServerless Containers Postureの機能を活用し、Azure Container Appsを含むより広範なコンテナ環境に対して一元的なセキュリティポスチャ管理を実現できるようになりました。

このアップデートの主な目的は、Azure Container Appsのようなサーバーレスコンテナサービスに対しても、Microsoft Defender for Cloudのセキュリティ管理機能を適用し、組織全体のコンテナセキュリティの可視性と管理性を向上させることにあります。従来、Defender for CloudのServerless Containers Postureは主にAzure Kubernetes Service（AKS）などのマネージドKubernetes環境を対象としていましたが、今回のアップデートによりAzure Container Appsもサポート対象となりました。

具体的な機能としては、Azure Container Apps環境をDefender for Cloudに統合することで、セキュリティベストプラクティスの適用状況や構成の脆弱性、セキュリティリスクの検出などが可能になります。これにより、複数のコンテナプラットフォームを運用する組織でも、単一のワークフローからセキュリティポスチャの監視と管理を行うことができます。

技術的な仕組みとしては、Azure Container AppsリソースをDefender for Cloudの管理対象に追加することで、ポスチャ管理エンジンが各種セキュリティ設定や構成情報を自動的に評価し、推奨事項やアラートを生成します。これにより、セキュリティ担当者はAzure Portal上で一貫したダッシュボードやレポートを通じて、コンテナ環境全体のセキュリティ状況を把握できます。

活用シナリオとしては、マイクロサービスアーキテクチャをAzure Container Apps上で展開している組織が、既存のDefender for Cloud運用にシームレスに組み込むことで、セキュリティガバナンスを強化するケースが想定されます。また、複数のAzureサービスを横断してセキュリティ管理を統合したい場合にも有効です。

注意点としては、本機能の利用にはMicrosoft Defender for Cloudの該当プランが必要となる場合があるため、ライセンスやコスト面の確認が必要です。また、サポートされるセキュリティチェックやアラートの種類は、他のコンテナサービスと異なる場合がありますので、公式ドキュメントで詳細を確認することが推奨されます。

関連するAzureサービスとの連携としては、Azure Kubernetes ServiceやAzure Container Registryなど、既存のコンテナ関連サービスとDefender for Cloudの統合管理が可能であり、これによりクラウドネイティブなセキュリティ運用の効率化が期待できます。

---

### 2. Generally Available: Windows Server 2025 on AKS

**公開日時**: 2026年09月01日 22:31:50 UTC
**リンク**: [Generally Available: Windows Server 2025 on AKS](https://azure.microsoft.com/updates?id=570090)

**アップデートID**: 570090
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）で、Windows Server 2025のサポートが一般提供（GA）となりました。

- 主な変更点や新機能  
これまでサポートされていた旧バージョンのWindows Serverに加え、AKS上でWindows Server 2025を利用したコンテナワークロードのデプロイと運用が可能になりました。これにより、最新のWindows Server機能やセキュリティ強化を活用できます。

- 影響を受ける対象  
AKS上でWindowsベースのワークロードを運用している組織や、既存のWindows Serverノードプールを利用しているユーザーが対象です。特に、旧バージョンのサポート終了に備えて移行を検討している技術者にとって重要なアップデートです。

- 注意点があれば記載  
Windows Server 2025を利用するには、対応するノードイメージを選択する必要があります。また、アプリケーションやミドルウェアの互換性について事前検証を行うことを推奨します。既存環境からの移行時は、十分なテストを実施してください。

**詳細**:

Azure Kubernetes Service（AKS）において、Windows Server 2025の一般提供（GA）が開始されたアップデートは、Windowsベースのワークロードを運用する組織にとって重要な意味を持ちます。背景として、従来のWindows Serverバージョンのサポート終了が近づいており、既存のシステムを最新環境へ移行する必要性が高まっています。このアップデートの目的は、顧客がサポート期限切れによるリスクを回避し、最新のWindows Server環境で安全かつ効率的にワークロードを運用できるようにすることです。

具体的な機能として、AKS上でWindows Server 2025をベースとしたノードプールの作成や管理が可能となります。これにより、Windowsコンテナを利用したアプリケーションを最新のOS環境でデプロイし、運用することができます。AKSは、LinuxとWindowsの混在環境をサポートしており、今回のアップデートによりWindows Server 2025を含む複数バージョンのノードプールを柔軟に構成することができます。

技術的な仕組みとしては、AKSのクラスタ作成時やノードプール追加時にWindows Server 2025イメージを選択することで、該当バージョンのOS上でコンテナランタイムが動作します。これにより、Windows Server 2025のセキュリティ機能やパフォーマンス改善を活用したコンテナ運用が可能となります。また、AKSの管理機能や自動スケーリング、アップグレード機能もWindows Server 2025ノードプールに対して適用されます。

活用シナリオとしては、既存のWindows Serverベースのアプリケーションをコンテナ化し、AKS上で運用する場合や、最新のWindows Server機能を必要とする新規アプリケーションのデプロイに適しています。特に、サポート期限が迫る旧バージョンからの移行や、セキュリティ要件が厳しいシステムの運用において、Windows Server 2025の利用は有効です。

注意点として、Windows Server 2025ノードプールを利用する際は、対応するコンテナイメージやアプリケーションが新OSに適合しているか事前に検証する必要があります。また、AKSの機能やサードパーティ製ツールがWindows Server 2025に対応しているかも確認が必要です。制限事項については、AKSのドキュメントやサポート情報を参照し、既存の運用環境との互換性や移行計画を慎重に検討することが求められます。

関連するAzureサービスとしては、Azure Container Registry（ACR）によるコンテナイメージ管理や、Azure Monitorによる運用監視、Azure Active Directoryによる認証管理などが挙げられます。これらのサービスと連携することで、Windows Server 2025ノードプールを含むAKS環境の運用効率とセキュリティを高めることができます。

---

### 3. Generally Available: Artifact Streaming on AKS

**公開日時**: 2026年09月01日 22:30:59 UTC
**リンク**: [Generally Available: Artifact Streaming on AKS](https://azure.microsoft.com/updates?id=570095)

**アップデートID**: 570095
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Feature

**要約**:

【何が更新されたか】  
Azure Kubernetes Service（AKS）で、Azure Container Registry（ACR）を利用したArtifact Streaming機能が一般提供（GA）されました。

【主な変更点や新機能】  
Artifact Streamingにより、コンテナイメージの全体をプル（ダウンロード）完了する前に、必要な部分から順次読み込むことが可能になりました。これにより、ワークロードの起動時間が短縮され、スケーラビリティが向上します。

【影響を受ける対象】  
AKS上でコンテナ化されたワークロードを運用している技術者や、ACRを利用してイメージ管理を行っているユーザーが対象です。特に大規模なイメージや頻繁なスケールアウトを行う環境で効果が期待できます。

【注意点】  
Artifact Streamingを利用することで、イメージのプル完了を待たずにワークロードを開始できますが、従来のイメージ管理や起動フローと異なるため、運用や監視方法の見直しが必要になる場合があります。詳細な利用方法や制約については公式ドキュメントを参照してください。

**詳細**:

Azure Kubernetes Service（AKS）において、Artifact Streaming機能が一般提供（Generally Available）となりました。このアップデートの背景には、コンテナ化されたワークロードの起動やスケール時のパフォーマンス向上へのニーズがあります。従来、AKS上でコンテナイメージをAzure Container Registry（ACR）から取得する際、イメージ全体をノードにプル（ダウンロード）し終えるまでワークロードの起動が完了しませんでした。そのため、大容量イメージや多数のノードへのスケール時には、起動時間がボトルネックとなるケースがありました。

今回のArtifact Streaming機能は、AKSとACRの連携により、コンテナイメージの全体をプルし終える前に、必要な部分から順次ストリーミングしてワークロードを起動できるようになります。これにより、イメージのダウンロード待ち時間を短縮し、スケールアウトやローリングアップデート時のパフォーマンスが向上します。技術的には、イメージのレイヤー単位で必要なデータをオンデマンドで取得する仕組みが採用されており、コンテナランタイムとAKSのインフラがACRと連携してストリーミングを実現しています。

実際の活用シナリオとしては、マイクロサービスアーキテクチャを採用した大規模なシステムや、頻繁なデプロイ・スケール操作が求められる環境において、ワークロードの起動時間短縮やリソース効率化が期待できます。また、CI/CDパイプラインでの自動デプロイや、突発的なトラフィック増加への迅速な対応にも有効です。

注意点としては、Artifact Streamingが有効な場合でも、イメージの全体が必要なタイミングでは引き続きダウンロードが発生するため、ネットワーク帯域やACRのパフォーマンスに依存する部分があります。また、対応するイメージフォーマットやコンテナランタイム、AKSのバージョンなど、利用環境によって制限が存在する可能性があります。詳細な制限事項や推奨設定については、公式ドキュメントの参照が必要です。

本機能は、Azure Container RegistryとAzure Kubernetes Serviceの密接な連携によって提供されており、Azure上でのクラウドネイティブなアプリケーション運用において、より効率的なワークロード管理を実現します。

---

### 4. Generally Available: Confidential VMs for Azure Linux

**公開日時**: 2026年09月01日 22:30:18 UTC
**リンク**: [Generally Available: Confidential VMs for Azure Linux](https://azure.microsoft.com/updates?id=570100)

**アップデートID**: 570100
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Feature

**要約**:

【何が更新されたか】  
Azure Linux向けのConfidential Virtual Machines（CVM）が、AKS（Azure Kubernetes Service）で一般提供（GA）されました。

【主な変更点や新機能】  
AKSのノードプールでCVMを利用できるようになり、機密性の高いコンテナワークロードを安全にAKSへ移行することが可能になりました。CVMは、テナントのデータや処理内容を強力に保護し、セキュリティとプライバシーを高める機能を提供します。

【影響を受ける対象】  
Azure Linuxを利用しているAKS環境の技術者や、機密性の高いデータやワークロードをクラウド上で運用する必要がある組織が対象です。特に、セキュリティ要件が厳しい業界や、コンテナ化された機密データ処理を行うユーザーにとって重要なアップデートです。

【注意点】  
CVMを利用する際は、対応するVMサイズやAKSのバージョン、Linuxディストリビューションなどの要件を事前に確認する必要があります。また、既存のワークロードをCVMノードプールへ移行する際は、アプリケーションの互換性やパフォーマンスへの影響も考慮してください。

**詳細**:

Azure Update「Generally Available: Confidential VMs for Azure Linux」について説明します。

本アップデートは、Azure Linux上で稼働するConfidential Virtual Machines（CVM）が一般提供（GA）となったことを示しています。CVMは、テナントのセキュリティと機密性を強化するために設計された仮想マシンであり、特にAzure Kubernetes Service（AKS）環境での利用が可能となっています。これにより、AKSのノードプールにCVMを導入することで、機密性の高いコンテナワークロードをAKSへ移行する際のセキュリティ要件を満たすことができます。

具体的な機能としては、CVMが提供するハードウェアベースの隔離と暗号化により、仮想マシン内のデータや処理内容がクラウドプロバイダーや他のテナントから保護されます。これにより、クラウド上でのデータ漏洩リスクを低減し、規制やコンプライアンス要件を満たすことが可能です。AKSのノードプールにCVMを適用することで、従来の仮想マシンよりも高いレベルのセキュリティを確保しながら、コンテナ化されたアプリケーションを運用できます。

技術的な仕組みとしては、CVMはハードウェアのTrusted Execution Environment（TEE）を活用し、仮想マシンのメモリや処理内容を暗号化します。これにより、ホストOSやハイパーバイザーからもワークロードの内容が不可視となり、クラウド管理者によるアクセスや操作からも保護されます。AKSとの連携においては、ノードプールの作成時にCVMを選択することで、機密性の高いワークロード専用のノードを構成できます。

活用シナリオとしては、金融、医療、政府機関など、極めて高い機密性が求められる業界のコンテナワークロードのクラウド移行や運用に適しています。特に、規制対応やデータ保護が必須となるケースで、CVMを利用することでセキュリティ要件を満たしつつ、AKSのスケーラビリティや運用効率を享受できます。

注意点としては、CVMは従来の仮想マシンと比較して一部機能やパフォーマンスに制限がある場合があります。また、AKSでCVMを利用する際には、対応するAzure Linuxイメージや特定の構成要件が必要となる場合があるため、事前に公式ドキュメントで詳細を確認することが推奨されます。

関連するAzureサービスとしては、AKSとの連携が中心ですが、Azure Confidential ComputingやAzure Security Centerなどのサービスと組み合わせることで、より包括的なセキュリティ対策を実現できます。

以上が「Generally Available: Confidential VMs for Azure Linux」の技術者向け詳細説明です。

---

### 5. Generally Available: Purchase order mapping available in Microsoft Marketplace 

**公開日時**: 2026年09月01日 18:40:59 UTC
**リンク**: [Generally Available: Purchase order mapping available in Microsoft Marketplace ](https://azure.microsoft.com/updates?id=569700)

**アップデートID**: 569700
**情報源**: Azure Updates API

**カテゴリ**: Launched, Feature

**要約**:

【何が更新されたか】  
Microsoft Marketplaceで購入したサービスや製品に対して、購入オーダー（PO）のマッピング機能が一般提供（GA）されました。

【主な変更点や新機能】  
購入オーダーのマッピング機能により、Marketplace経由で購入したクラウドやAIサービスの請求書を自社の会計処理に合わせて割り当てることが可能になりました。これにより、請求書の突合や支出管理が効率化されます。

【影響を受ける対象】  
Microsoft Marketplaceを利用してクラウドやAIサービスを購入している企業や組織の会計担当者、管理者、及びクラウド運用担当者が主な対象です。

【注意点】  
本機能はMicrosoft Marketplaceでの購入に限定されており、利用する際は自社の会計システムとの連携方法や運用フローの確認が必要です。また、詳細や補足情報は公式ドキュメントやサポートを参照してください。

このアップデートにより、クラウド支出の管理や会計処理がより正確かつ効率的に行えるようになります。

**詳細**:

本アップデートは、「Purchase order mapping available in Microsoft Marketplace」の一般提供開始に関するものです。Microsoft Marketplaceを通じて行われる購入に対して、企業の会計要件に合わせた購入注文（Purchase Order、PO）のマッピング機能が提供されることが主な内容です。これにより、Marketplace経由で発生するクラウドやAI関連の支出を含むMicrosoftの請求書に対し、PO情報を割り当てることが可能となります。これまで、Marketplaceでの購入は請求書上で他のサービス利用料と区別がつきにくく、会計処理や支出の突合せ作業に手間がかかるケースがありました。本機能の導入により、組織の会計処理や監査対応が効率化され、支出管理の透明性が向上します。

具体的には、Microsoft Marketplaceでの購入時に、各取引に対してPO番号を指定し、その情報が請求書に反映される仕組みが提供されます。これにより、会計部門は請求書上の各アイテムと社内の発注情報を容易に照合でき、経費精算や予算管理の精度が向上します。技術的には、Marketplaceの購入フローにPO番号入力フィールドが追加され、購入情報とPO情報がMicrosoftの請求システム上で紐付けられる形となります。請求書のフォーマットもこれに対応し、PO番号が明記されるため、従来の手動による照合作業が不要となります。

活用シナリオとしては、複数部門がMarketplaceから異なるSaaSやクラウドサービスを調達している大規模組織において、各部門ごとにPOを発行し、支出を正確に部門別管理したい場合などが挙げられます。また、監査対応や内部統制の観点からも、支出の根拠となるPO情報が請求書に明示されることで、証跡管理が容易になります。

注意点としては、本機能が利用可能なMarketplace購入の範囲や、PO番号の入力方法、既存の請求書発行プロセスとの互換性など、詳細な仕様については公式ドキュメントやサポート情報を参照する必要があります。また、PO情報の反映タイミングや、複数POの割り当て可否など、組織の運用要件に応じた事前確認が推奨されます。

本機能は、Azureの請求管理やコスト管理サービスと連携して利用することで、より高度な支出分析や予算統制が可能となります。Microsoft Marketplaceを通じたクラウドリソース調達のガバナンス強化を図る上で、非常に有用なアップデートです。

---

### 6. Generally Available: Azure Firewall auto-learn SNAT routes 

**公開日時**: 2026年09月01日 17:10:38 UTC
**リンク**: [Generally Available: Azure Firewall auto-learn SNAT routes ](https://azure.microsoft.com/updates?id=570474)

**アップデートID**: 570474
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Azure Firewall, Features

**要約**:

- 何が更新されたか  
Azure Firewallの「auto-learn SNAT routes」機能が一般提供（GA）されました。

- 主な変更点や新機能  
この機能は、Azure Firewallが登録済みおよびプライベートな宛先プレフィックスを定期的に自動検出し、それらをNo-SNAT範囲として適用します。これにより、元の送信元IPアドレスを保持しつつ、SNAT（Source Network Address Translation）管理が簡素化されます。手動でNo-SNAT範囲を設定する必要がなくなり、運用負荷が軽減されます。

- 影響を受ける対象  
Azure Firewallを利用している環境、特にSNAT管理や送信元IP保持が重要なシナリオで影響を受けます。ネットワーク管理者やセキュリティ担当者にとって利便性が向上します。

- 注意点があれば記載  
自動検出されたNo-SNAT範囲が適用されるため、既存の手動設定との重複や競合に注意が必要です。運用中のFirewallポリシーやルーティング設定を事前に確認し、影響範囲を把握してから導入してください。

**詳細**:

Azure Firewallのauto-learn SNAT routes機能が一般提供（GA）となりました。本機能は、Azure Firewallが定期的に登録済みおよびプライベートな宛先プレフィックスを自動的に学習し、それらをNo-SNAT範囲として適用することで、元の送信元IPアドレスを保持し、SNAT（Source Network Address Translation）管理を簡素化することを目的としています。これまでAzure Firewallでは、宛先によってSNATが適用されるか否かを手動で設定する必要があり、管理の複雑化や誤設定による通信障害が発生するリスクがありました。auto-learn SNAT routesの導入により、Firewallが自動的に宛先プレフィックスを認識し、適切なNo-SNAT範囲を設定することで、管理者の負担を大幅に軽減できます。

具体的な機能としては、Azure Firewallがネットワーク内の登録済みおよびプライベートな宛先プレフィックスを定期的にスキャンし、それらをNo-SNAT範囲として自動的に設定します。これにより、これらの宛先への通信時に送信元IPアドレスが保持され、トラフィックの可視性やトレーサビリティが向上します。また、SNAT範囲の手動設定が不要となるため、運用効率が高まります。技術的な仕組みとしては、FirewallがAzureリソースの登録情報やプライベートアドレス空間を定期的に取得し、動的にNo-SNAT範囲を更新する形となります。

この機能は、複数のVNetやオンプレミス環境との接続、またはマルチリージョン構成など、複雑なネットワーク構成を持つ環境で特に有効です。例えば、VNet間通信やプライベートエンドポイントへのアクセス時に、送信元IPアドレスを保持したまま通信を行いたい場合に活用できます。これにより、セキュリティ監査やログ管理、アクセス制御の精度が向上します。

注意点としては、本機能が自動的にNo-SNAT範囲を設定するため、意図しない宛先がNo-SNAT対象となる可能性があります。運用上、Firewallの挙動や通信ログを定期的に確認し、必要に応じて手動設定との整合性を取ることが推奨されます。また、Azure Firewallのバージョンや構成によっては本機能が利用できない場合があるため、事前に対応状況を確認する必要があります。

関連するAzureサービスとしては、Azure Virtual Network、Private Endpoint、ExpressRoute、VPN Gatewayなどが挙げられます。これらのサービスと連携することで、Azure FirewallによるSNAT管理が自動化され、よりセキュアかつ効率的なネットワーク運用が可能となります。

---

### 7. Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans

**公開日時**: 2026年09月01日 16:31:14 UTC
**リンク**: [Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans](https://azure.microsoft.com/updates?id=570250)

**アップデートID**: 570250
**情報源**: Azure Updates API

**カテゴリ**: Launched, DevOps, Management and governance, Azure Monitor, Azure Copilot, Feature

**要約**:

【何が更新されたか】  
Azure Copilot Observability Agentが、Azure MonitorのLog Analyticsデータにおいて、BasicおよびAuxiliaryテーブルプランをサポートするようになりました。

【主な変更点や新機能】  
これまでサポートされていなかったBasicおよびAuxiliaryテーブルプランのデータも、Copilot Observability Agentによるインタラクティブな分析や詳細調査で利用可能になりました。これにより、高ボリュームのテレメトリデータも効率的に分析できます。

【影響を受ける対象】  
Azure Monitorを利用している技術者や運用チーム、特にLog AnalyticsのBasic/Auxiliaryテーブルプランを活用しているユーザーが対象です。

【注意点】  
本アップデートにより、従来のStandardテーブルプランだけでなく、コスト効率を重視したBasic/AuxiliaryプランのデータもAIによる運用支援の恩恵を受けられるようになりました。導入時は、既存のデータプラン設定やアクセス権限を確認してください。

**詳細**:

本アップデートは、Azure MonitorにおけるAI搭載の運用支援エージェントであるAzure Copilot Observability Agentが、Log AnalyticsのBasicテーブルおよびAuxiliaryテーブルプランをサポートするようになったことを示しています。これにより、インタラクティブな分析や詳細な調査の際に、これまで対応していなかったBasicおよびAuxiliaryテーブルに格納されたログデータも対象として扱うことが可能となりました。

Azure Copilot Observability Agentは、Azure Monitorの一部として、AI技術を活用し運用担当者の分析やトラブルシューティングを支援する役割を持っています。今回のアップデートにより、Log Analyticsワークスペース内でコスト効率を重視したBasicテーブルや、補助的な用途で利用されるAuxiliaryテーブルに保存された大量のテレメトリデータも、Copilot Observability Agentのインタラクティブな分析機能や深堀り調査機能の対象となります。これにより、従来は主にAnalyticsテーブルに限定されていたAI支援による運用分析の適用範囲が拡大し、より多様なデータソースからのインサイト抽出が可能となります。

技術的には、Copilot Observability AgentがLog Analyticsのデータ構造を拡張してサポートすることで、BasicおよびAuxiliaryテーブルに格納された高ボリュームのテレメトリデータも、AIによる対話型クエリや根本原因分析などの高度な運用支援機能の対象となります。これにより、コスト最適化のためにBasicテーブルを選択している環境や、補助的なログ管理をAuxiliaryテーブルで行っているシナリオでも、Copilot Observability Agentのメリットを享受できます。

活用シナリオとしては、コストを抑えつつ大量のログデータを蓄積しているシステムにおいて、障害発生時やパフォーマンス問題の調査時に、AIの支援を受けながら迅速かつ効率的に原因究明を進めることが可能です。また、補助的なログデータも含めた全体的な運用状況の可視化や、複数テーブルを横断した分析が容易になります。

注意点としては、BasicおよびAuxiliaryテーブルはAnalyticsテーブルと比較して機能や保持期間、クエリのパフォーマンスに制限がある場合があるため、運用要件に応じたテーブルプランの選択が重要です。また、Copilot Observability Agentの機能を最大限活用するためには、Azure MonitorおよびLog Analyticsの設定と権限管理が適切に行われている必要があります。

本機能はAzure MonitorおよびLog Analyticsと密接に連携して動作し、既存の運用監視基盤にシームレスに統合可能です。これにより、Azure上での運用監視とインシデント対応の効率化がさらに進むことが期待されます。

---

### 8. Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions

**公開日時**: 2026年09月01日 16:29:24 UTC
**リンク**: [Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions](https://azure.microsoft.com/updates?id=569899)

**アップデートID**: 569899
**情報源**: Azure Updates API

**カテゴリ**: Launched, DevOps, Management and governance, Azure Monitor, Features

**要約**:

【何が更新されたか】  
Azure Monitor LogsのAuxiliary Logsプランが、Azure Government（Fairfax）および中国リージョンで一般提供（GA）されました。

【主な変更点や新機能】  
Auxiliary Logsプランは、大量かつ詳細なログデータ（コンプライアンスや監査用途）をコスト効率よく取り込み・保持できるオプションです。これにより、従来のログプランよりも低コストで高ボリュームのログ管理が可能となります。

【影響を受ける対象】  
Azure Governmentおよび中国リージョンでAzure Monitor Logsを利用している技術者や組織が対象です。特に、監査やコンプライアンス要件で大量のログデータを扱うユーザーにとってメリットがあります。

【注意点】  
Auxiliary Logsプランは、主に高ボリュームかつ冗長なログの取り込み・保持に適しているため、用途に応じてプラン選択が必要です。既存のログプランとの違いを理解し、コストやデータ保持要件に合わせて活用してください。

**詳細**:

Azure Monitor Auxiliary Logs PlanがAzure GovernmentおよびChinaリージョンで一般提供されたことについて説明します。今回のアップデートは、Azure Monitor LogsにおけるAuxiliary table planの導入を、主権クラウド（Azure Government Fairfax）で利用可能としたものです。背景として、コンプライアンスや監査目的で大量かつ詳細なログデータを長期間保持するニーズが高まっており、従来のログプランではコスト面や運用面で課題がありました。Auxiliary Logs Planは、こうした高ボリューム・冗長性の高いログデータのインジェストと保持を、よりコスト効率よく実現することを目的としています。

具体的な機能として、Auxiliary table planはAzure Monitor Logs内でAuxiliaryテーブルを利用し、通常のログテーブルと区別して保存・管理します。このAuxiliaryテーブルは、主にコンプライアンスや監査用途で必要となる詳細なログデータを大量に格納するために設計されています。従来のログテーブルと比較して、インジェストコストや保持コストが最適化されている点が特徴です。これにより、ログデータの保持期間や保存容量を拡大しつつ、コストを抑えることが可能になります。

技術的な仕組みとしては、Azure MonitorのLog Analyticsワークスペース内でAuxiliaryテーブルを作成し、対象となるログデータをAuxiliaryテーブルにインジェストします。データの保持や検索は、通常のLog Analyticsと同様にKusto Query Language（KQL）を用いて実施できます。Auxiliary Logs Planは、Azure GovernmentやChinaリージョンの主権クラウド環境に最適化されており、これらのリージョンのコンプライアンス要件に対応しています。

活用シナリオとしては、金融機関や公共機関など、法規制や内部統制のために大量の監査ログを長期間保存する必要があるケースが挙げられます。例えば、ユーザーアクティビティやシステムイベントの詳細な記録をAuxiliaryテーブルに保存し、必要に応じて監査や調査に利用することができます。

注意点としては、Auxiliary Logs Planは主権クラウドでの提供が前提となっており、Azure GovernmentおよびChinaリージョン以外では利用できません。また、Auxiliaryテーブルに保存されたデータは、通常のLog Analyticsテーブルとは異なる料金体系や保持ポリシーが適用されるため、導入前にコスト計算や保持要件の確認が必要です。

関連するAzureサービスとしては、Azure Monitor、Log Analytics、Kusto Query Language（KQL）が挙げられます。Auxiliary Logs Planは、これらのサービスと連携し、既存の監視・ログ分析基盤の拡張として活用できます。今回のアップデートにより、主権クラウド環境におけるコンプライアンス対応や監査業務の効率化が期待できます。

---

### 9. Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching

**公開日時**: 2026年09月01日 16:25:33 UTC
**リンク**: [Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching](https://azure.microsoft.com/updates?id=569904)

**アップデートID**: 569904
**情報源**: Azure Updates API

**カテゴリ**: Launched, DevOps, Management and governance, Azure Monitor, Features

**要約**:

- 何が更新されたか  
Azure Monitor LogsのAuxiliary Logs Planが一般提供（GA）となり、Azure Tablesのサポートとプラン切り替え機能が追加されました。

- 主な変更点や新機能  
Auxiliary Logs Planは、コンプライアンスや監査目的で大量かつ詳細なログを安価に保存できるプランです。今回、Azure Tablesへの対応と、既存のログプランからAuxiliary Logs Planへの切り替えが可能になりました。これにより、用途に応じてコスト最適化や柔軟な運用が実現できます。

- 影響を受ける対象  
Azure Monitor Logsを利用しているユーザー、特に大量のログデータを長期間保存する必要がある技術者や管理者が対象です。

- 注意点があれば記載  
Auxiliary Logs Planは主に保存目的のため、頻繁なクエリには向いていません。プラン切り替え時には、既存データの移行やアクセス制御などに注意が必要です。

**詳細**:

Azure Monitor LogsのAuxiliary table planは、コンプライアンスや監査目的で大量かつ詳細なログを長期間保持する必要があるものの、実際には頻繁にクエリされないログデータのインジェストと保持を、コスト効率良く実現するためのプランです。今回のアップデートでは、技術者から要望の多かった2つの機能が一般提供（GA）となりました。これにより、Auxiliary table planがAzure Monitor Logs内のAzure Tablesに対応し、さらにプランの切り替えが可能になっています。

具体的な変更内容として、Auxiliary table planのサポート対象がAzure Tablesに拡張されました。これにより、Azure Monitor Logsに格納されるテーブル型データに対しても、Auxiliary planのコスト効率の高いインジェストと保持が適用できるようになっています。また、既存のプランからAuxiliary table planへの切り替え、あるいはその逆の切り替えがサポートされたことで、運用中のログデータの用途やアクセス頻度に応じて柔軟にプランを選択できるようになりました。

技術的な仕組みとしては、Auxiliary table planは通常のLog Analyticsワークスペースの料金体系とは異なり、主に保持期間の長期化とインジェストコストの最適化を重視した設計となっています。ログデータのインジェスト時にAuxiliary planを選択することで、保持期間やアクセス頻度に応じたコスト管理が可能となります。プランの切り替えはAzure PortalやAPIを通じて実施でき、既存テーブルのデータに対しても適用が可能です。

活用シナリオとしては、例えばセキュリティ監査ログやシステムイベントログなど、法令や社内規定により一定期間以上の保存が義務付けられているが、実際にはほとんど参照されないログデータの管理が挙げられます。Auxiliary table planを利用することで、これらのデータを低コストで保持しつつ、必要に応じてアクセスやクエリが可能となります。

注意点としては、Auxiliary table planは主に保持とインジェストのコスト最適化を目的としているため、頻繁なクエリやリアルタイム分析には向いていません。また、プラン切り替え時にはデータの保持ポリシーやアクセス権限の変更が必要となる場合があります。詳細な制限事項や料金体系については公式ドキュメントを参照する必要があります。

関連するAzureサービスとしては、Azure Monitor Logs、Log Analyticsワークスペース、Azure Tablesが挙げられます。これらのサービスとの連携により、監査やコンプライアンス要件を満たしつつ、運用コストの削減が可能となります。今回のアップデートは、Azure Monitor Logsを利用した大規模なログ管理環境において、より柔軟かつ効率的な運用を実現するものです。

---


*このレポートは自動生成されました - 2026-09-02 12:03:13 JST*