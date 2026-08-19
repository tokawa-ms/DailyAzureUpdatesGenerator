# 2026年08月19日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年08月19日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Retirement: Azure VMware Solution License-included service will be retired August 30, 2027

**公開日時**: 2026年08月18日 19:52:06 UTC
**リンク**: [Retirement: Azure VMware Solution License-included service will be retired August 30, 2027](https://azure.microsoft.com/updates?id=569535)

**アップデートID**: 569535
**情報源**: Azure Updates API

**カテゴリ**: Compute, Azure VMware Solution, Retirements

**要約**:

- 何が更新されたか  
Azure VMware Solutionの「ライセンス込みサービス」が2027年8月30日に廃止されることが発表されました。

- 主な変更点や新機能  
BroadcomによるVMwareのライセンス方針変更により、今後はVMware Cloud Foundation（VCF）利用時に「持ち込みライセンス（BYOL）」が必須となります。Azure側でVMwareライセンスを提供する「ライセンス込み」モデルは終了します。

- 影響を受ける対象  
Azure VMware Solutionのライセンス込みサービスを利用している全てのユーザーが対象です。VCFをAzure上で利用する場合、2027年8月30日以降は自身でVMwareライセンスを調達・管理する必要があります。

- 注意点があれば記載  
既存環境の移行計画やライセンス調達方法の検討が必要です。サービス終了後はAzureによるVMwareライセンス提供がなくなるため、BYOL対応への準備を早めに進めることを推奨します。

**詳細**:

Azure Update「Retirement: Azure VMware Solution License-included service will be retired August 30, 2027」について詳細に説明します。

本アップデートの背景として、2023年11月にBroadcomがVMwareのライセンス方針を変更し、すべてのハイパースケーラー・プラットフォームにおいてVMware Cloud Foundation（VCF）利用時に「持ち込み可能なライセンス（BYOL: Bring Your Own License）」を必須とする運用へと移行しました。これにより、Azure VMware Solutionにおいても、従来提供されていたライセンス込みサービスの継続が困難となり、2027年8月30日をもってライセンス込みサービスの提供が終了することになりました。

具体的な変更内容としては、Azure VMware Solutionの「License-included」オプションが廃止される点が挙げられます。これまでAzure上でVMware環境を構築する際、MicrosoftがVMwareライセンスを含めて提供していましたが、今後はユーザー自身がVMware Cloud Foundationのライセンスを調達し、Azure環境に持ち込む必要があります。これにより、ライセンス管理や調達のプロセスがユーザー側の責任となります。

技術的な仕組みとしては、Azure VMware SolutionはAzure上でVMware vSphere、vSAN、NSX-TなどのVMware製品をネイティブに実行できるサービスです。従来はMicrosoftがVMwareライセンスを一括管理し、ユーザーはライセンス込みでサービスを利用できましたが、今後はBYOL方式により、ユーザーが自身のVMwareライセンスをAzure環境に適用する必要があります。これには、VMware Cloud Foundationのポータブルライセンスが必要となり、ライセンスの適用方法や管理手順についてはVMwareおよびAzureの公式ドキュメントを参照する必要があります。

活用シナリオとしては、オンプレミスのVMware環境をAzureへ移行する際や、ハイブリッドクラウド構成を実現する場合にAzure VMware Solutionが利用されてきました。今後も同様のシナリオで利用可能ですが、ライセンス調達と管理がユーザー側の作業となるため、移行計画や運用設計時にライセンス要件を十分に考慮する必要があります。

注意点として、2027年8月30日以降はライセンス込みサービスが利用できなくなるため、既存のAzure VMware Solution環境を利用している場合は、期限までにBYOL方式への移行準備が必須となります。また、VMware Cloud Foundationのライセンス調達や適用に関する詳細は、VMwareおよびBroadcomの最新情報を確認することが重要です。

関連するAzureサービスとしては、Azure MigrateやAzure Site Recoveryなど、VMware環境の移行やバックアップに関わるサービスとの連携が挙げられます。これらのサービスを活用する場合も、VMwareライセンスの管理方法が変更される点に留意する必要があります。

以上が本アップデートの詳細な説明です。

---

### 2. Generally Available: Managed Instance on Azure App Service

**公開日時**: 2026年08月18日 17:26:25 UTC
**リンク**: [Generally Available: Managed Instance on Azure App Service](https://azure.microsoft.com/updates?id=568952)

**アップデートID**: 568952
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Mobile, Web, App Service, Services, Feature

**要約**:

【何が更新されたか】  
Azure App Service上で「Managed Instance」が一般提供（GA）されました。

【主な変更点や新機能】  
Managed Instanceは、オンプレミスや仮想マシン上で稼働しているWebアプリケーションを、最小限の設定変更かつコード変更なしでAzure App Serviceへ移行できる機能です。これにより、従来の環境からクラウドへの移行が容易になり、アプリの互換性や運用負荷を軽減できます。

【影響を受ける対象】  
オンプレミスや仮想マシン上でWebアプリケーションを運用している組織や開発者が主な対象です。特に、既存アプリをクラウドへ移行したいが、コード修正や大規模な再構成を避けたい場合に有効です。

【注意点】  
Managed Instanceの利用にあたっては、App Serviceの既存機能や制約を十分に理解する必要があります。また、移行後の運用やセキュリティ要件についても事前に確認することを推奨します。

**詳細**:

Managed Instance on Azure App Serviceが一般提供（GA）となりました。本アップデートの背景には、企業がオンプレミスや仮想マシン上で稼働しているWebアプリケーションを、Azure App Serviceへ移行する際の構成作業やコード変更の負担を最小化するニーズがあります。Managed Instanceは、これまでのApp Serviceの標準的なホスティングモデルに加え、より柔軟な移行パスを提供することを目的としています。

具体的な機能として、Managed Instanceは既存のWebアプリケーションをAzure App Service上に展開する際、アプリケーションのコードを変更することなく、最小限の構成変更のみで移行を可能にします。これにより、従来のオンプレミス環境や仮想マシン上で動作していたアプリケーションを、クラウドネイティブなApp Serviceの管理機能やスケーラビリティを活用しながら運用できるようになります。

技術的な仕組みとしては、Managed InstanceはApp Serviceのインフラストラクチャ上で動作し、アプリケーションの実行環境を抽象化することで、移行時の互換性を担保しています。具体的な実装方法については、アプリケーションのデプロイメントや構成管理がAzureポータルやCLIを通じて容易に行えることが特徴です。これにより、従来のApp Serviceの利点である自動スケーリング、パッチ適用、セキュリティ管理などの機能をそのまま利用することができます。

活用シナリオとしては、既存のWebアプリケーションをクラウドへ迅速に移行したい場合や、コード変更を伴わずにクラウドの管理機能を導入したい場合に有効です。また、App Serviceの他の機能やAzureのサービス群と連携することで、DevOpsやCI/CDパイプラインの構築、セキュリティ強化、監視・運用の効率化など、幅広い用途に対応できます。

注意点や制限事項については、現時点で提供されている情報が限定的であり、詳細な制約やサポート範囲については公式ドキュメントやアップデートページを参照する必要があります。特に、アプリケーションの互換性やサポートされるフレームワーク、構成の詳細については、移行前に十分な検証が求められます。

関連するAzureサービスとの連携については、Managed InstanceはApp Serviceの管理機能を活用できるため、Azure MonitorやApplication Insightsによる監視、Azure Active Directoryによる認証、Azure DevOpsによる継続的デプロイなど、既存のAzureエコシステムとの統合が容易です。これにより、クラウド移行後も一貫した運用管理が可能となります。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=568952）を参照してください。

---

### 3. Public Preview: Ipv6 support in Azure Firewall

**公開日時**: 2026年08月18日 17:25:30 UTC
**リンク**: [Public Preview: Ipv6 support in Azure Firewall](https://azure.microsoft.com/updates?id=569520)

**アップデートID**: 569520
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Azure Firewall, Features

**要約**:

【何が更新されたか】  
Azure FirewallがIPv6対応となり、パブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
Azure FirewallおよびFirewall Policyで、IPv4とIPv6の両方のトラフィックを処理するデュアルスタックモードが利用可能になりました。これにより、ネイティブなIPv6ネットワークルールによるフィルタリングや、DNS Proxy機能のIPv6対応が実現されています。

【影響を受ける対象】  
Azure Firewallを利用しているユーザーや、IPv6対応が求められるネットワーク環境を構築している技術者が対象となります。特に、クラウド環境でIPv6トラフィックの管理やセキュリティ強化を必要とするケースで有効です。

【注意点】  
現在はパブリックプレビュー段階のため、本番環境での利用は慎重に検討してください。機能やサポート内容が今後変更される可能性がありますので、最新情報や公式ドキュメントの確認を推奨します。

**詳細**:

Azure FirewallにおけるIPv6対応がパブリックプレビューとして提供開始されました。本アップデートの背景には、クラウド環境におけるIPv6の需要増加と、従来のIPv4アドレス枯渇への対応が挙げられます。これにより、Azure FirewallおよびFirewall Policyをデュアルスタックモードで構成し、IPv4とIPv6双方のトラフィックを管理できるようになります。

具体的な機能として、Azure FirewallはネイティブなIPv6ネットワークルールのフィルタリングをサポートします。これにより、IPv6アドレスを用いたアクセス制御やトラフィック管理が可能となります。また、DNS Proxy機能もIPv6に対応し、DNSクエリのプロキシ処理をIPv6環境でも利用できるようになっています。これらの機能は、Firewall Policyの設定画面からIPv4/IPv6両方のルールを定義することで実現されます。

技術的な仕組みとしては、Azure Firewallのデプロイメント時にデュアルスタックモードを選択することで、仮想ネットワーク上でIPv4とIPv6の両方のアドレス空間を扱うことができます。ネットワークルールやアプリケーションルールの定義において、IPv6アドレスやプレフィックスを指定することが可能です。DNS Proxy機能についても、IPv6対応DNSサーバーへのクエリ転送がサポートされます。

活用シナリオとしては、グローバルなサービス展開や、IPv6対応が求められるアプリケーション環境でのセキュリティ強化が挙げられます。例えば、外部からのIPv6トラフィックを制御したり、内部ネットワークでIPv6ベースの通信を監視・制御する用途に適しています。また、DNS Proxy機能を活用することで、IPv6環境下でもDNSクエリのセキュアな管理が可能となります。

注意点として、現時点ではパブリックプレビュー段階であるため、本番環境での利用は推奨されません。機能や仕様が今後変更される可能性があるため、テスト環境での検証や評価を行うことが重要です。また、既存のAzure Firewall構成との互換性や、IPv6アドレス空間の設計についても十分な考慮が必要です。

関連するAzureサービスとの連携については、Azure Virtual NetworkやDNSサービスとの組み合わせが想定されます。デュアルスタック構成の仮想ネットワーク上でAzure Firewallを利用することで、IPv4/IPv6両方のトラフィックを統合的に管理できます。また、DNS Proxy機能を活用する際は、Azure DNSや外部DNSサービスとの連携も可能です。

以上が、Azure FirewallのIPv6対応パブリックプレビューに関する技術者向け詳細説明です。

---


*このレポートは自動生成されました - 2026-08-19 12:01:35 JST*