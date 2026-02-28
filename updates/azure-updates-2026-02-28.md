# 2026年02月28日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年02月28日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Generally available: Azure Premium SSD v2 Disk Storage is now available in a third Availability Zone in New Zealan North

**公開日時**: 2026年02月27日 23:15:13 UTC
**リンク**: [Generally available: Azure Premium SSD v2 Disk Storage is now available in a third Availability Zone in New Zealan North](https://azure.microsoft.com/updates?id=558078)

**アップデートID**: 558078
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Disk Storage, Features, Services

**要約**:

- 何が更新されたか  
Azure Premium SSD v2が、ニュージーランド北部リージョンの第3アベイラビリティゾーンで一般提供（GA）となりました。

- 主な変更点や新機能  
Premium SSD v2は、Azure仮想マシン向けの次世代汎用ブロックストレージであり、サブミリ秒の低レイテンシと高いコストパフォーマンスを提供します。今回のアップデートにより、同リージョン内で3つ目のアベイラビリティゾーンでも利用可能となり、可用性と耐障害性が向上しました。

- 影響を受ける対象  
ニュージーランド北部リージョンでAzure Premium SSD v2を利用している、または利用を検討しているユーザーやシステム、特に高可用性構成やゾーン冗長構成を必要とするワークロードが対象です。

- 注意点があれば記載  
今回のアップデートはニュージーランド北部リージョンの第3アベイラビリティゾーンに限定されます。他リージョンやゾーンでの提供状況は別途確認が必要です。利用にあたっては、対応する仮想マシンサイズやサービス要件を事前に確認してください。

**詳細**:

Azure Premium SSD v2 Disk Storageがニュージーランド北部リージョンの第三アベイラビリティゾーンで一般提供されたことは、可用性と冗長性の向上を目的とした重要なアップデートです。Premium SSD v2は、Azure仮想マシン向けの次世代汎用ブロックストレージとして設計されており、サブミリ秒レベルの低レイテンシと優れたコストパフォーマンスを提供します。今回のアップデートにより、ニュージーランド北部リージョン内で三つのアベイラビリティゾーンすべてにPremium SSD v2が展開可能となり、ゾーン障害時のデータ保護や高可用性構成がより柔軟に実現できるようになりました。

Premium SSD v2の主な特徴は、従来のPremium SSDと比較してさらに高速なI/O性能と低レイテンシを実現している点です。これにより、ミッションクリティカルなワークロードや高トランザクション処理が求められるシステムにおいて、ストレージのボトルネックを低減し、安定したパフォーマンスを維持できます。技術的には、Premium SSD v2はAzureの管理ディスクサービスと連携しており、仮想マシンのストレージとして簡単にアタッチ・デタッチが可能です。また、ゾーンごとの冗長性を活用することで、障害発生時にも迅速な復旧が期待できます。

活用シナリオとしては、金融システムや大規模データベース、トランザクション処理を伴う業務システムなど、高速なストレージアクセスが必要な環境でPremium SSD v2が有効です。特に、アベイラビリティゾーンを跨いだ高可用性構成を求める場合、今回のアップデートによってニュージーランド北部リージョンでもより堅牢なシステム設計が可能となります。

注意点としては、Premium SSD v2の利用には対応リージョンおよびゾーンの制約があるため、事前に利用可能なゾーンを確認する必要があります。また、料金体系やディスクサイズ、I/O制限などの詳細はAzure公式ドキュメントを参照し、設計段階で十分な検討が求められます。

関連するAzureサービスとしては、Azure Virtual Machines、Azure Managed Disks、Azure Availability Zonesなどが挙げられます。これらのサービスと組み合わせることで、信頼性の高いインフラストラクチャの構築が可能です。今回のアップデートは、ニュージーランド北部リージョンにおけるAzureのストレージオプションの拡充と、より高度な可用性要件への対応を促進するものです。

---

### 2. Generally Available: DCesv6, DCedsv6, ECesv6, and ECedsv6 confidential VMs

**公開日時**: 2026年02月27日 23:15:13 UTC
**リンク**: [Generally Available: DCesv6, DCedsv6, ECesv6, and ECedsv6 confidential VMs](https://azure.microsoft.com/updates?id=558051)

**アップデートID**: 558051
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Virtual Machines, Features, Services

**要約**:

【何が更新されたか】  
DCesv6、DCedsv6、ECesv6、ECedsv6シリーズの機密性を重視した仮想マシン（VM）が一般提供（GA）されました。

【主な変更点や新機能】  
これらのVMは第5世代Intel® Xeon®プロセッサとIntel® Trust Domain Extensions（Intel® TDX）を採用しています。Intel® TDXにより、VMごとに独立した信頼ドメインが構築され、ホストや他のVMから分離された高度なデータ保護が可能です。これにより、機密データやワークロードのセキュリティが強化されます。

【影響を受ける対象】  
Azure上で機密性の高いデータやワークロードを扱う企業や組織、セキュリティ要件が厳しいシステムを運用する技術者が主な対象です。特に、コンプライアンスやデータ保護が求められる業界に適しています。

【注意点があれば記載】  
新しいVMシリーズの利用には、対応するリージョンやAzureのサービス制限に注意が必要です。また、Intel® TDXの機能を活用するためには、アプリケーション側での対応や設定が必要になる場合があります。

**詳細**:

今回のAzure Updateでは、DCesv6、DCedsv6、ECesv6、ECedsv6シリーズの仮想マシン（VM）が一般提供（Generally Available）となりました。これらのVMは、Azureが提供する次世代の機密性を重視した仮想マシンであり、5世代目のIntel® Xeon®プロセッサとIntel® Trust Domain Extensions（Intel® TDX）を基盤としています。アップデートの背景としては、クラウド上でのデータ保護やプライバシー要求の高まりに対応するため、より高度な機密性を実現するVMの提供が求められていました。これにより、組織はクラウド環境でも高いセキュリティを確保しつつ、柔軟な運用が可能となります。

具体的な機能としては、Intel® TDXを活用することで、仮想マシン内のデータや処理がホストOSや他のVMから隔離され、機密性が強化されています。これにより、クラウドプロバイダーや管理者であっても、VM内部のデータにアクセスできない設計となっています。DCesv6、DCedsv6、ECesv6、ECedsv6は、それぞれ異なるワークロードやパフォーマンス要件に対応するために設計されており、幅広い用途に適用可能です。

技術的な仕組みとしては、Intel® TDXがハードウェアレベルで信頼領域（Trust Domain）を構築し、VMごとに独立したセキュリティ境界を設けています。これにより、従来のVMに比べて、より厳格な機密性が保証されます。実装方法としては、AzureポータルやCLIを用いて、これらのVMシリーズを選択しデプロイすることで、機密性の高いワークロードを簡単にクラウド上で運用できます。

活用シナリオとしては、金融、医療、政府機関など、機密データの保護が必須となる業界での利用が想定されます。例えば、個人情報や財務データ、研究データなどをクラウド上で安全に処理する場合に、これらのVMが有効です。また、ゼロトラストアーキテクチャの実現や、規制対応が求められるシステムにも適しています。

注意点としては、機密性VM特有の制限事項や、対応しているOSやソフトウェア、パフォーマンス要件などを事前に確認する必要があります。従来のVMと異なるセキュリティモデルを採用しているため、アプリケーションや運用設計にも配慮が必要です。

関連するAzureサービスとの連携については、Azure Key VaultやAzure Confidential Computingなど、セキュリティや機密性を強化するサービスと組み合わせることで、より高度なデータ保護を実現できます。これらのVMは、Azureのセキュリティエコシステムの中核を担う存在となります。

---

### 3. Retirement: Managed NGINX Ingress with Application Routing Add-on Retiring November 2026

**公開日時**: 2026年02月27日 21:45:03 UTC
**リンク**: [Retirement: Managed NGINX Ingress with Application Routing Add-on Retiring November 2026](https://azure.microsoft.com/updates?id=555839)

**アップデートID**: 555839
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements, Open Source

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）の「Application Routing Add-on」に含まれるManaged NGINX Ingress Controllerが、2026年11月30日をもってサポート終了となることが発表されました。

- 主な変更点や新機能  
上流のIngress-NGINXプロジェクトが2026年3月以降メンテナンスを終了するため、Microsoftは2026年11月30日まで重大なセキュリティパッチのみ提供します。新機能や通常のアップデートは行われません。

- 影響を受ける対象  
AKS環境でManaged NGINX Ingress Controllerを利用している技術者や組織が対象となります。今後は別のIngressソリューションへの移行を検討する必要があります。

- 注意点があれば記載  
2026年11月30日以降はセキュリティパッチも提供されなくなるため、継続利用は推奨されません。計画的な移行を早めに検討してください。詳細は公式アップデートページをご参照ください。

**詳細**:

本アップデートは、「Managed NGINX Ingress with Application Routing Add-on」のリタイアメントに関するものです。背景として、上流プロジェクトであるIngress-NGINXが2026年3月をもって非推奨となり、以降はアップデートが提供されなくなることが挙げられます。これに伴い、Microsoftは2026年11月30日までクリティカルなセキュリティパッチの提供を継続しますが、それ以降はNGINX Ingress Controllerのサポートを終了します。

具体的な変更内容としては、Azure Kubernetes Service（AKS）環境で利用されてきたManaged NGINX Ingress with Application Routing Add-onが、上流プロジェクトの非推奨化に合わせて段階的に廃止される点が重要です。これにより、2026年11月30日以降は、当該アドオンを利用したIngressの新規デプロイや既存環境のサポートが受けられなくなります。

技術的な仕組みとして、Managed NGINX Ingressは、AKSクラスター上でNGINXベースのIngress Controllerをマネージドサービスとして提供し、アプリケーションへの外部アクセス制御やルーティング、SSL終端などの機能を実装してきました。Application Routing Add-onは、DNS管理や証明書の自動プロビジョニングなど、アプリケーション公開に必要な周辺機能も統合して提供していました。

活用シナリオとしては、マイクロサービスアーキテクチャを採用したAKS環境において、複数のサービスへの外部HTTP/HTTPSアクセスを一元的に管理する用途や、SSL証明書の自動管理、カスタムドメインの設定などが挙げられます。これらのシナリオでは、Managed NGINX Ingressがシンプルな導入と運用性の高さから広く利用されてきました。

注意点として、本アドオンの廃止により、今後はセキュリティパッチの提供も終了し、脆弱性リスクが高まるため、利用中の環境では代替ソリューションへの移行が必須となります。また、サポート終了後はMicrosoftによる技術支援も受けられなくなるため、早期の移行計画策定が求められます。

関連するAzureサービスとの連携については、Managed NGINX IngressはAKSとの統合が前提となっており、Azure DNSやAzure Key Vaultなどと連携して、DNSレコード管理や証明書の安全な保管・自動更新を実現していました。今後は、Azure Application Gateway Ingress Controllerや他のサードパーティ製Ingress Controllerへの移行が推奨される可能性があります。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=555839）を参照してください。

---

### 4. Generally Available: Azure Red Hat OpenShift is now available in Malaysia West, New Zealand North, and Mexico Central

**公開日時**: 2026年02月27日 17:30:41 UTC
**リンク**: [Generally Available: Azure Red Hat OpenShift is now available in Malaysia West, New Zealand North, and Mexico Central](https://azure.microsoft.com/updates?id=557897)

**アップデートID**: 557897
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Red Hat OpenShift, Features, Open Source, Regions & Datacenters

**要約**:

【何が更新されたか】  
Azure Red Hat OpenShift（ARO）が、マレーシア西部、ニュージーランド北部、メキシコ中央の3つのAzureリージョンで一般提供（GA）となりました。

【主な変更点や新機能】  
これまで利用できなかったリージョンでAROが利用可能となり、アジア太平洋およびラテンアメリカ地域でのサービス提供範囲が拡大しました。これにより、各地域のユーザーは高可用性やスケーラビリティ、セキュリティを備えたKubernetesベースのコンテナプラットフォームをAzure上で利用できます。

【影響を受ける対象】  
マレーシア西部、ニュージーランド北部、メキシコ中央リージョンでAzureを利用する企業や開発者が、AROを選択できるようになります。これにより、現地でのデータレジデンシー要件やレイテンシーの最適化が可能です。

【注意点があれば記載】  
新リージョンでのサービス利用にあたり、各リージョンの価格やサービスレベル、サポート内容を事前に確認することを推奨します。既存のARO機能や運用方法に変更はありません。

**詳細**:

Azure Red Hat OpenShiftは、マレーシア西部、ニュージーランド北部、メキシコ中央の3つの新しいAzureリージョンで一般提供が開始されました。このアップデートの背景には、アジア太平洋およびラテンアメリカ地域におけるAzure Red Hat OpenShiftの利用可能性を拡大し、現地の顧客やパートナーがより低遅延かつ高可用性のクラウドネイティブアプリケーションを構築・運用できる環境を提供する目的があります。

具体的な機能や変更内容としては、これらのリージョンにおいてAzure Red Hat OpenShiftのフルマネージドサービスが利用可能となり、企業はKubernetesベースのコンテナオーケストレーションとRed Hat OpenShiftのエンタープライズ機能を組み合わせて活用できます。Azure Red Hat OpenShiftは、Azureインフラストラクチャ上でRed HatとMicrosoftが共同で運用・サポートを行うサービスであり、セキュリティ、スケーラビリティ、運用管理の自動化、統合監視などの機能を提供します。

技術的な仕組みとしては、Azure Red Hat OpenShiftはAzureの仮想マシン上にOpenShiftクラスターをデプロイし、Azure Resource Managerによるリソース管理や、Azure Active Directoryとの認証連携、Azure Monitorによる監視、Azure Policyによるガバナンスなど、Azureの各種サービスと密接に統合されています。ユーザーはAzureポータルやCLI、APIを利用してクラスターの作成や管理を行うことができ、Red Hat OpenShiftの標準機能であるOperatorやCI/CDパイプライン、サービスメッシュなども利用可能です。

活用シナリオとしては、金融、ヘルスケア、製造業などの業界で、コンテナ化されたアプリケーションの迅速なデプロイやマイクロサービスアーキテクチャの導入、DevOpsの推進、ハイブリッドクラウドやマルチクラウド環境での運用などが挙げられます。また、現地リージョンでの提供により、データ主権やコンプライアンス要件に対応しやすくなり、グローバル展開を行う企業にも利便性が向上します。

注意点としては、リージョンごとに利用可能なサービスやSKU、サポート範囲が異なる場合があるため、事前に公式ドキュメントやAzureポータルで詳細を確認する必要があります。また、既存のAzure Red Hat OpenShiftクラスターから新リージョンへの移行や、ネットワーク構成、セキュリティ設定などについても十分な検討が求められます。

関連するAzureサービスとの連携については、Azure DevOpsやGitHub ActionsによるCI/CDパイプラインの構築、Azure Container Registryとのイメージ管理、Azure Key Vaultによるシークレット管理、Azure Load BalancerやApplication Gatewayによるトラフィック制御など、Azureエコシステム内の各種サービスとシームレスに統合できる点が特徴です。これにより、エンタープライズレベルの運用やセキュリティ、可用性を確保しつつ、クラウドネイティブな開発・運用を実現できます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=557897）をご参照ください。

---


*このレポートは自動生成されました - 2026-02-28 12:01:57 JST*