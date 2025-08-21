# 2025年08月21日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年08月21日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Public Preview: Azure Bastion now supports connectivity to private AKS clusters via tunneling

**公開日時**: 2025年08月20日 17:45:19 UTC
**リンク**: [Public Preview: Azure Bastion now supports connectivity to private AKS clusters via tunneling](https://azure.microsoft.com/updates?id=500996)

**アップデートID**: 500996
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Compute, Containers, Azure Bastion, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure Bastionがプレビュー機能として、プライベートAKSクラスターへのトンネリング接続をサポート開始。

- 主な変更点や新機能  
ローカル環境からAzure Bastion経由でAKSのAPIサーバーへ安全にトンネル接続可能に。標準のKubernetesツールでプライベートおよびパブリッククラスターにシームレスアクセス可能。

- 影響を受ける対象  
AKSのプライベートクラスターを運用する開発者や運用担当者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討を。ネットワーク設定や権限管理の確認が必要。

**詳細**:

本アップデートにより、Azure BastionからプライベートAKSクラスターのAPIサーバーへ直接トンネル接続が可能となりました。従来、プライベートAKSはVNet内限定アクセスで、開発者はVPNやジャンプボックス経由の複雑な接続が必要でしたが、本機能によりローカル端末から標準的なkubectlなどのKubernetesツールで安全にAPIサーバーへアクセス可能です。技術的には、Azure BastionがSSHトンネルを中継し、クラスターのAPIエンドポイントへ透過的に接続を確立します。これにより、ネットワーク構成の簡素化とセキュリティ強化が両立されます。活用例としては、開発環境からの直接操作やCI/CDパイプラインの安全なAPIアクセスが挙げられます。制限としては、Bastionが配置されたVNetとAKSクラスターが同一またはピアリング済みである必要があり、パブリックAPIエンドポイントが無効なプライベートクラスター限定の機能です。Azure MonitorやAzure Policyと連携し、運用監視やアクセス制御の一元管理も可能です。詳細は公式ドキュメント参照推奨。

---

### 2. Public Preview: Azure NetApp Files Flexible service level now supports cool access

**公開日時**: 2025年08月20日 17:30:35 UTC
**リンク**: [Public Preview: Azure NetApp Files Flexible service level now supports cool access](https://azure.microsoft.com/updates?id=500712)

**アップデートID**: 500712
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure NetApp Files, Features

**要約**:

- 何が更新されたか  
Azure NetApp FilesのFlexibleサービスレベルがパブリックプレビューで「Coolアクセス」対応を開始。

- 主な変更点や新機能  
ストレージ容量とスループットを独立して設定可能なFlexibleレベルで、低頻度アクセス向けのCoolストレージが利用可能に。コスト最適化が図れる。

- 影響を受ける対象  
Azure NetApp Filesを利用し、性能と容量を柔軟に調整したいユーザーや、低アクセス頻度の大容量データを扱う技術者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に。性能要件とコストのバランスを検討のこと。

**詳細**:

本アップデートは、Azure NetApp Files（ANF）のFlexibleサービスレベルに「クールアクセス（Cool Access）」がパブリックプレビューで追加されたことを示します。Flexibleレベルはストレージ容量とスループットを独立して設定可能で、低スループットかつ大容量のワークロードに最適化されています。今回のクールアクセス対応により、アクセス頻度の低いデータをコスト効率よく管理可能となり、ストレージコスト削減が期待できます。技術的には、Flexibleレベルのボリュームに対し、データのアクセスパターンに基づく自動階層化が可能となり、クール層へのデータ移行を透過的に実施します。実装はAzure PortalやCLI、APIから設定可能で、既存のFlexibleボリュームに対しても適用可能です。活用シナリオとしては、バックアップデータやアーカイブ、ログファイルなどアクセス頻度が低いが容量が大きいデータの保存に適しています。注意点として、クールアクセスはパブリックプレビュー段階であり、SLAやサポート範囲が限定される点、またアクセス頻度が急増した場合のパフォーマンス影響を考慮する必要があります。Azure Blob StorageのCool Tierとは異なり、ANFのNFS/SMBプロトコル対応ストレージとして高性能を維持しつつコスト最適化が可能であり、Azure Kubernetes Service（AKS）やAzure Virtual Machines（VM）などのファイル共有ニーズと連携して利用できます。詳細は公式ドキュメントおよびAzure Portalのアップデート情報を参照してください。

---

### 3. Private Preview: DCesv6 and ECesv6 series confidential VMs with Intel® TDX

**公開日時**: 2025年08月20日 16:45:09 UTC
**リンク**: [Private Preview: DCesv6 and ECesv6 series confidential VMs with Intel® TDX](https://azure.microsoft.com/updates?id=489745)

**アップデートID**: 489745
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Virtual Machines, Features, Services, Security

**要約**:

- 何が更新されたか  
AzureでIntel® TDX対応の次世代機密VM「DCesv6」「ECesv6」シリーズがプライベートプレビュー開始。

- 主な変更点や新機能  
5世代Intel® Xeon® Emerald Rapidsプロセッサ搭載で、ハードウェアベースの信頼ドメイン拡張により強化された機密性を提供。

- 影響を受ける対象  
高度なセキュリティが求められる企業や組織のクラウド環境。

- 注意点があれば記載  
現時点はプライベートプレビューのため、利用には申請が必要。今後の一般提供時に詳細確認推奨。

**詳細**:

本アップデートは、Intel® Trust Domain Extensions（Intel® TDX）を搭載した第5世代Intel® Xeon®プロセッサ（Emerald Rapids）を基盤とするAzureの次世代Confidential VMシリーズ「DCesv6」と「ECesv6」のプライベートプレビュー提供開始を告知するものです。背景には、クラウド上でのデータ機密性とプライバシー保護の強化ニーズがあり、Intel TDXによりハードウェアレベルで仮想マシンのメモリと処理を隔離し、ホストや他のVMからの不正アクセスを防止します。DCesv6は汎用向け、ECesv6は高性能コンピューティング向けに最適化されています。実装はIntel TDX対応CPUとAzureのセキュア基盤を組み合わせ、信頼できる実行環境（TEE）を提供。活用シナリオとしては、金融・医療など高いコンプライアンス要件を持つアプリケーションの機密データ処理や、マルチテナント環境での安全なワークロード分離が挙げられます。現時点ではプライベートプレビューのため利用には申請が必要で、対応リージョンやOSイメージに制限があります。Azure Key VaultやAzure Confidential Ledgerなどの機密性強化サービスと連携可能で、統合的なセキュリティ強化が期待されます。

---

### 4. Retirement: Microsoft Sentinel Deprecation in Microsoft Azure operated by 21Vianet Announcement

**公開日時**: 2025年08月20日 16:30:32 UTC
**リンク**: [Retirement: Microsoft Sentinel Deprecation in Microsoft Azure operated by 21Vianet Announcement](https://azure.microsoft.com/updates?id=498754)

**アップデートID**: 498754
**情報源**: Azure Updates API

**カテゴリ**: Hybrid + multicloud, Security, Microsoft Sentinel, Retirements

**要約**:

- 何が更新されたか  
Microsoft Azure（21Vianet運営）におけるMicrosoft Sentinelサービスの廃止が発表されました。

- 主な変更点や新機能  
インフラおよび運用の複雑化に伴い、同地域でのSentinel提供が終了します。

- 影響を受ける対象  
21Vianet運営のAzure環境でSentinelを利用している顧客。

- 注意点  
サービス終了に伴い、代替のセキュリティ監視ソリューションへの移行計画が必要です。

**詳細**:

本アップデートは、中国市場向けにAzureを運営する21VianetによるMicrosoft Sentinelサービスの廃止を告知するものです。背景には、インフラおよび運用の複雑性増大に伴い、サービスの高水準な保護・信頼性維持が困難となったための判断があります。具体的には、Microsoft Sentinelのログ収集、分析、脅威検出機能が利用不可となり、代替のセキュリティ監視ソリューションへの移行が必要です。技術的には、Azure MonitorやLog Analyticsと連携したSIEM機能が停止し、21Vianet運営環境でのセキュリティイベント管理は別途構築が求められます。活用シナリオとしては、従来Sentinelで実現していたリアルタイム脅威検出や自動応答が利用できなくなるため、他のAzure Security Centerやサードパーティ製品への切替が推奨されます。注意点として、データの移行計画や運用体制の見直しが必須であり、サービス停止に伴うセキュリティギャップを回避するため早期対応が求められます。関連サービスでは、Azure Monitor、Log Analytics、Security Centerとの連携が影響を受けるため、これらの設定変更や代替手段の検討が必要です。詳細は公式リンクを参照してください。

---

### 5. Retirement: Microsoft Defender for Cloud Deprecation in Microsoft Azure Operated by 21Vianet Announcement

**公開日時**: 2025年08月20日 16:30:32 UTC
**リンク**: [Retirement: Microsoft Defender for Cloud Deprecation in Microsoft Azure Operated by 21Vianet Announcement](https://azure.microsoft.com/updates?id=498749)

**アップデートID**: 498749
**情報源**: Azure Updates API

**カテゴリ**: Hybrid + multicloud, Security, Microsoft Defender for Cloud, Retirements

**要約**:

- 何が更新されたか  
Microsoft Azure（21Vianet運営）環境におけるMicrosoft Defender for Cloudの提供終了が発表されました。

- 主な変更点や新機能  
インフラと運用の複雑化により、同サービスの継続提供が困難となり、段階的に廃止されます。

- 影響を受ける対象  
21Vianet運営のAzure利用者でMicrosoft Defender for Cloudを利用中の技術者および運用チーム。

- 注意点  
代替のセキュリティソリューションの検討と移行計画を早急に進める必要があります。

**詳細**:

本アップデートは、中国市場向けにMicrosoft Azureを運営する21Vianet環境における「Microsoft Defender for Cloud」の廃止を告知するものです。背景には、インフラおよび運用の複雑性の増大に伴い、同サービスの維持が困難となったため、セキュリティ保護と信頼性の高いサービス提供を継続するための判断がなされています。具体的には、21Vianet運営下のAzure環境で提供されていたMicrosoft Defender for Cloudの機能が段階的に廃止され、代替のセキュリティ対策や運用モデルへの移行が推奨されます。技術的には、Defender for Cloudが提供していた脅威検出、脆弱性管理、セキュリティポリシー適用などの機能が利用できなくなるため、ユーザーはAzure Security Centerの代替機能やサードパーティ製品の導入を検討する必要があります。活用シナリオとしては、クラウドリソースのセキュリティ監視やコンプライアンス遵守のための自動化された脅威検出が挙げられますが、21Vianet環境ではこれらが制限されるため、運用設計の見直しが不可欠です。注意点として、廃止に伴い既存のセキュリティアラートやレポート機能が停止し、移行期間中のセキュリティリスクが増大する可能性があるため、早期の対応が求められます。関連サービスとしては、Azure SentinelやAzure Policyなどの他のセキュリティ管理ツールとの連携強化が推奨されますが、21Vianet環境固有の制約を考慮した設計が必要です。

---


*このレポートは自動生成されました - 2025-08-21 12:01:46 JST*