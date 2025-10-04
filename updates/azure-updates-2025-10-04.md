# 2025年10月04日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年10月04日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 7 件

## 更新一覧

### 1. Retirement: Azure Monitor SCOM Managed Instance will be retired on Sep 30, 2026

**公開日時**: 2025年10月03日 18:15:20 UTC
**リンク**: [Retirement: Azure Monitor SCOM Managed Instance will be retired on Sep 30, 2026](https://azure.microsoft.com/updates?id=501673)

**アップデートID**: 501673
**情報源**: Azure Updates API

**カテゴリ**: DevOps, Management and governance, Azure Monitor, Retirements

**要約**:

- 何が更新されたか  
Azure Monitor SCOM Managed Instanceが2026年9月30日で廃止される。

- 主な変更点や新機能  
サービスへのアクセスが廃止され、以降利用不可となる。

- 影響を受ける対象  
Azure Monitor SCOM Managed Instanceを利用しているユーザー。

- 注意点  
オンプレミスの監視はOperations Managerへの移行を推奨。廃止までに移行計画を立てる必要がある。  
詳細は公式廃止ドキュメント参照。

**詳細**:

本アップデートは、Azure Monitor SCOM Managed Instanceのサービス終了（2026年9月30日）を告知するものです。背景には、オンプレミスの監視ニーズに対し、より専用性の高いSystem Center Operations Manager（SCOM）への移行を促進し、クラウドサービスの効率化を図る狙いがあります。Azure Monitor SCOM Managed Instanceは、Azure上でSCOMの管理インスタンスを提供し、オンプレミス環境の監視データをクラウドで一元管理可能でしたが、サービス終了に伴いアクセス不可となります。技術者は、オンプレミス監視を継続する場合、従来のOperations Managerのオンプレミス展開へ移行する必要があります。移行時は、既存の監視ルールや管理パックの互換性を確認し、データ収集やアラート設定の再構築が求められます。なお、Azure Monitorの他の機能（ログ分析やアラート機能）は引き続き利用可能であり、Azure Arcを活用したハイブリッド監視との連携も検討可能です。サービス終了に伴う影響を最小化するため、早期の移行計画策定とテスト実施が推奨されます。詳細は公式リタイアメントドキュメントを参照してください。  
https://azure.microsoft.com/updates?id=501673

---

### 2. Generally Available: CLI command for migration from Availability Sets and basic load balancer on AKS 

**公開日時**: 2025年10月03日 16:45:25 UTC
**リンク**: [Generally Available: CLI command for migration from Availability Sets and basic load balancer on AKS ](https://azure.microsoft.com/updates?id=503258)

**アップデートID**: 503258
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSでAvailability SetsおよびBasic Load Balancerからの移行を自動化するAzure CLIコマンドがGAとなりました。

- 主な変更点や新機能  
2025年9月30日で廃止予定のAvailability SetsとBasic Load Balancerから、仮想マシンのノードプールへ簡単に移行・アップグレード可能。

- 影響を受ける対象  
既存のAKSクラスタでAvailability SetsやBasic Load Balancerを使用しているユーザー。

- 注意点  
移行は2025年9月30日までに実施が必要。移行前にバックアップや検証を推奨。

**詳細**:

本アップデートは、2025年9月30日をもってAvailability SetsおよびBasic Load Balancerが非推奨となることを受け、AKSクラスタの移行を円滑化するために提供されました。新CLIコマンドにより、既存のAvailability Setsベースのノードプールを、より高機能なVirtual Machinesノードプール（VMSSベース）へ自動的に移行可能です。これにより、スケーラビリティや可用性が向上し、Standard Load Balancerへの移行も促進されます。技術的には、CLIコマンドがノードプールの再構築とVMSSへの置換を行い、クラスタの稼働中断を最小限に抑えつつアップグレードを実施します。活用例としては、既存AKS環境のモダナイゼーションや将来的な機能拡張準備が挙げられます。注意点として、移行中は一時的なパフォーマンス低下や設定の再検証が必要であり、Basic Load Balancer固有の機能制限も考慮すべきです。関連サービスとしては、Azure MonitorやAzure Policyと連携し、移行後の運用監視やガバナンス強化が可能です。詳細は公式ドキュメントを参照してください。

---

### 3. Generally Available: Cross-tenant customer-managed keys for Azure NetApp Files volume encryption

**公開日時**: 2025年10月03日 16:15:04 UTC
**リンク**: [Generally Available: Cross-tenant customer-managed keys for Azure NetApp Files volume encryption](https://azure.microsoft.com/updates?id=501340)

**アップデートID**: 501340
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure NetApp Files, Features

**要約**:

- 何が更新されたか  
Azure NetApp Filesのボリューム暗号化におけるクロステナントのカスタマー管理キー(CMK)機能が一般提供開始。

- 主な変更点や新機能  
異なるAzureテナント間で自分の暗号化キーを管理可能となり、セキュリティと運用の柔軟性が向上。

- 影響を受ける対象  
複数テナントでAzure NetApp Filesを利用し、キー管理を一元化したい企業や組織。

- 注意点  
キー管理の権限設定やアクセス制御を適切に行わないとセキュリティリスクが増大する可能性あり。

**詳細**:

Azure NetApp Filesのボリューム暗号化におけるクロステナントCustomer-Managed Keys（CMK）がGAとなりました。これにより、異なるAzureテナント間で顧客自身が管理するキーを用いた暗号化が可能となり、複数テナント環境でのセキュリティ管理とコンプライアンス遵守が強化されます。具体的には、Azure Key Vaultに保存されたCMKを別テナントのAzure NetApp Filesボリューム暗号化に利用可能で、キー管理の一元化や権限分離を実現します。実装は、対象ボリュームの暗号化設定時にキーのAzure Key Vault URIを指定し、適切なアクセス許可（Key Vaultのアクセスポリシー設定）が必要です。活用例としては、マルチテナント環境でのデータ保護や、顧客が管理するキーを用いたセキュリティポリシーの統合運用が挙げられます。注意点として、クロステナントアクセスのためのネットワーク設定や権限管理を厳密に行う必要があり、キーのローテーションや廃止時の影響範囲を十分理解することが重要です。Azure Key VaultおよびAzure NetApp Filesの連携により、柔軟かつ高度な暗号化管理が可能となります。詳細は公式ドキュメント参照を推奨します。

---

### 4. Retirement: Azure Static Web Apps database connection feature

**公開日時**: 2025年10月03日 16:15:04 UTC
**リンク**: [Retirement: Azure Static Web Apps database connection feature](https://azure.microsoft.com/updates?id=500848)

**アップデートID**: 500848
**情報源**: Azure Updates API

**カテゴリ**: Compute, Web, Static Web Apps, Retirements

**要約**:

- 何が更新されたか  
Azure Static Web Appsのデータベース接続機能（パブリックプレビュー中）が、基盤インフラの変更に伴い2025年11月30日で廃止予定。

- 主な変更点や新機能  
該当機能のサポート終了により、今後は別の方法でデータベース接続を実装する必要がある。

- 影響を受ける対象  
Static Web Appsでこのデータベース接続機能を利用している開発者・運用者。

- 注意点  
廃止までに該当機能を使ったデプロイをリファクタリングし、影響を回避することが推奨される。

**詳細**:

本アップデートは、Azure Static Web Appsのデータベース接続機能（現在パブリックプレビュー中）が、基盤インフラの変更に伴い2025年11月30日をもって廃止されることを通知するものです。この機能は、Static Web Appsから直接Azure SQLやCosmos DBなどのデータベースへシームレスに接続できる仕組みを提供していましたが、インフラ刷新によりサポート継続が困難となりました。具体的には、従来の接続管理や認証フローが非推奨となり、代替としてAPI経由でのデータアクセスやAzure Functionsを用いた中間層の実装が推奨されます。活用シナリオとしては、静的サイトからの動的データ取得やユーザーデータ管理が挙げられますが、今後は直接接続ではなく、APIやサーバーレス関数を介した設計が必須です。注意点として、廃止後に旧機能を利用したデプロイは失敗するため、早期のコードリファクタリングが必要です。また、Azure FunctionsやAPI Managementとの連携により、認証・認可やスケーラビリティを確保しつつ安全なデータアクセスを実現可能です。詳細は公式ドキュメントを参照し、移行計画を早急に策定してください。

---

### 5. Public Preview:  Azure NetApp Files Support for OpenLDAP, FreeIPA, and Red Hat Directory Server LDAP services    

**公開日時**: 2025年10月03日 16:01:01 UTC
**リンク**: [Public Preview:  Azure NetApp Files Support for OpenLDAP, FreeIPA, and Red Hat Directory Server LDAP services    ](https://azure.microsoft.com/updates?id=508748)

**アップデートID**: 508748
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure NetApp Files, Features

**要約**:

- 何が更新されたか  
Azure NetApp FilesがFreeIPA、OpenLDAP、Red Hat Directory ServerのLDAPサービス統合をパブリックプレビューでサポート開始。

- 主な変更点や新機能  
NFSv3/v4.1ボリュームでTLSによる安全なLDAP認証が可能に。

- 影響を受ける対象  
これらのLDAPサービスを利用する企業のファイル共有環境。

- 注意点  
プレビュー機能のため本番環境での利用は慎重に。TLS設定の適切な構成が必要。

**詳細**:

本アップデートにより、Azure NetApp Files（ANF）がPublic PreviewとしてFreeIPA、OpenLDAP、Red Hat Directory Serverといった主要なLDAPサービスとの統合をサポートします。これにより、NFSv3およびNFSv4.1ボリュームに対し、TLSによるセキュアなLDAP認証が可能となり、従来のActive Directory依存から拡張された認証基盤を提供します。技術的には、ANFのNFSアクセス時にLDAPサーバーへTLS接続を確立し、ユーザー認証および権限管理を行う仕組みで、LDAPサーバーのエンドポイント設定や証明書の登録が必要です。これにより、Linux環境中心の企業が既存のOpenLDAPやFreeIPA基盤を活用しつつ、クラウド上で高性能なファイル共有を実現可能です。利用シナリオとしては、オンプレのLDAP管理下にあるユーザー認証をそのままANFに適用し、セキュリティポリシーを統一するケースが想定されます。なお現時点ではPublic Previewのため、一部機能制限やサポート範囲の限定があるため、運用前に公式ドキュメントで対応状況を確認する必要があります。Azure Active DirectoryやAzure AD Domain Servicesとの併用も可能で、多様な認証環境に柔軟に対応可能です。

---

### 6. Retirement: Azure VPN Gateway support for SSTP Protocol will be retired on March 31, 2027

**公開日時**: 2025年10月03日 16:01:01 UTC
**リンク**: [Retirement: Azure VPN Gateway support for SSTP Protocol will be retired on March 31, 2027](https://azure.microsoft.com/updates?id=499923)

**アップデートID**: 499923
**情報源**: Azure Updates API

**カテゴリ**: Networking, Security, VPN Gateway, Retirements

**要約**:

- 何が更新されたか  
Azure VPN GatewayのSSTPプロトコルサポートが2027年3月31日に廃止予定。

- 主な変更点や新機能  
SSTPはスケーラビリティと性能が低いため、IKEv2やOpenVPNへの移行を推奨。これらは最大1万接続をサポートし性能が大幅向上。

- 影響を受ける対象  
SSTPを利用中のVPN接続ユーザー。

- 注意点  
移行計画を早めに立て、IKEv2またはOpenVPNへの切替を実施する必要がある。

**詳細**:

本アップデートは、Azure VPN GatewayにおけるSSTP（Secure Socket Tunneling Protocol）サポートの2027年3月31日付け廃止を告知するものです。SSTPはスケーラビリティが限定的でパフォーマンス面で最適でないため、より高性能かつ大規模接続に対応可能なIKEv2およびOpenVPNへの移行を推奨しています。具体的には、IKEv2/OpenVPNは最大1万接続までサポートし、接続安定性や暗号化強度が向上します。技術的には、IKEv2はIPsecベースのトンネリングを用い、OpenVPNはSSL/TLSを利用した柔軟なVPN構築を可能にします。Azure VPN Gatewayの設定変更はAzure PortalやAzure CLIで行い、既存のSSTPクライアントは対応プロトコルへの切替が必要です。活用シナリオとしては、大規模なリモートアクセスVPN環境やハイブリッドネットワーク接続が挙げられます。注意点として、クライアント側もIKEv2またはOpenVPN対応が必須であり、移行計画を早期に策定する必要があります。Azure Virtual NetworkやAzure Active Directoryとの連携により、認証強化やアクセス制御の高度化が可能です。詳細は公式ドキュメントを参照し、段階的な移行を推進してください。

---

### 7. Retirement: General Purpose v1 (GPv1) and legacy blob storage accounts  

**公開日時**: 2025年10月03日 14:15:21 UTC
**リンク**: [Retirement: General Purpose v1 (GPv1) and legacy blob storage accounts  ](https://azure.microsoft.com/updates?id=496964)

**アップデートID**: 496964
**情報源**: Azure Updates API

**カテゴリ**: Storage, Storage Accounts, Retirements

**要約**:

- 何が更新されたか  
AzureはGeneral Purpose v1（GPv1）およびレガシーブロブストレージアカウントの廃止を発表しました。

- 主な変更点や新機能  
GPv1の廃止により、より高性能でスケーラブル、コスト効率の良いGPv2やプレミアムストレージへの移行が推奨されます。

- 影響を受ける対象  
GPv1およびレガシーブロブストレージアカウントを利用中のユーザー。

- 注意点  
廃止に伴い、早期のストレージアカウント移行計画が必要であり、移行しない場合はサービス停止のリスクがあります。

**詳細**:

本アップデートは、Azure Storageのパフォーマンス向上とコスト最適化を目的に、旧世代のGeneral Purpose v1（GPv1）およびレガシーブロブストレージアカウントの廃止を発表したものです。GPv1は従来のストレージアカウントタイプで、GPv2やBlob Storageアカウントに比べてスケーラビリティや機能面で劣るため、最新のストレージアーキテクチャへの移行を促進します。廃止に伴い、GPv1アカウントは新規作成が不可となり、既存アカウントはGPv2へのアップグレードが推奨されます。技術的には、GPv2はホット・クール・アーカイブのアクセス層をサポートし、トランザクション単価の最適化や高いスループットを実現。移行はAzure PortalやPowerShell、CLIで可能で、データ移行時のダウンタイムや互換性に注意が必要です。活用シナリオとしては、データアクセスパターンに応じたアクセス層の選択や、Azure FunctionsやLogic Appsとの連携による自動化が挙げられます。関連サービスではAzure Monitorでパフォーマンス監視、Azure Cost Managementでコスト分析が有効です。廃止に伴う影響を最小化するため、早期の移行計画策定が必須です。

---


*このレポートは自動生成されました - 2025-10-04 12:01:57 JST*