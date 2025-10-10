# 2025年10月10日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年10月10日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Generally Available: Custom port support for Azure Database for MySQL – Flexible Server 

**公開日時**: 2025年10月09日 17:30:09 UTC
**リンク**: [Generally Available: Custom port support for Azure Database for MySQL – Flexible Server ](https://azure.microsoft.com/updates?id=503627)

**アップデートID**: 503627
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Azure Database for MySQL, Features

**要約**:

- 何が更新されたか  
Azure Database for MySQL – Flexible Serverでカスタムポート（25001～26000）のサポートがGAとなりました。

- 主な変更点や新機能  
サーバー作成時にパブリック・プライベートアクセス両方でカスタムポートを指定可能。既存アプリとの統合やセキュリティポリシーに柔軟に対応できます。

- 影響を受ける対象  
Azure Database for MySQL – Flexible Serverを利用する開発者・運用者。

- 注意点  
デフォルトは従来通り3306ポート。ポート変更時はファイアウォール設定などの調整が必要です。

**詳細**:

Azure Database for MySQL – Flexible Serverにおいて、カスタムポート（25001～26000）のサポートがGA（一般提供）されました。これにより、サーバー作成時にデフォルトの3306番ポート以外を指定可能となり、既存アプリケーションとのポート競合回避やセキュリティポリシーへの適合が容易になります。設定はAzureポータル、CLI、ARMテンプレートで可能で、パブリックアクセス・プライベートアクセス両方のサーバーに適用可能です。技術的には、Flexible Serverのネットワーク設定で指定ポートを開放し、ファイアウォールルールやNSG（ネットワークセキュリティグループ）で通信制御を行います。活用例としては、複数のMySQLサーバーを同一ネットワーク内で運用する際のポート衝突回避や、企業のセキュリティ基準に基づく非標準ポート利用が挙げられます。注意点として、カスタムポートは25001～26000の範囲内に限定され、既存の接続文字列やアプリケーション設定の更新が必要です。また、Azure Private LinkやVNet統合と組み合わせることで、より堅牢なネットワーク構成が可能です。今回のアップデートは、Azure Database for MySQLの柔軟性とセキュリティ適合性を向上させる重要な機能拡張です。

---

### 2. Generally Available: Azure Firewall updates - Customer provided public IP address support in secured hubs

**公開日時**: 2025年10月09日 17:00:43 UTC
**リンク**: [Generally Available: Azure Firewall updates - Customer provided public IP address support in secured hubs](https://azure.microsoft.com/updates?id=512875)

**アップデートID**: 512875
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Azure Firewall, Azure Firewall Manager, Features

**要約**:

- 何が更新されたか  
Azure FirewallのVirtual WANセキュアハブで、顧客提供のパブリックIPアドレスが正式サポートされました。

- 主な変更点や新機能  
ユーザーが自身で所有するパブリックIPをAzure Firewallに割り当て可能となり、IP管理の柔軟性と統制が向上。

- 影響を受ける対象  
Virtual WANのセキュアハブ上でAzure Firewallを運用する企業や技術者。

- 注意点があれば記載  
IPアドレスの所有権や割り当て設定に注意し、適切なネットワーク設計を行う必要があります。

**詳細**:

本アップデートにより、Azure Virtual WANのセキュアハブ内でAzure Firewallに顧客所有のパブリックIPアドレスを割り当て可能となりました。従来はAzureが自動割当てするIPのみ対応していたため、顧客固有のIP管理やIPレンジの一貫性確保が困難でした。本機能は、オンプレミスや他クラウドとのIPアドレス統合管理や、既存のIPベースのセキュリティポリシー適用を容易にします。実装は、Azure FirewallのパブリックIP設定に顧客所有のグローバルIPリソースを指定し、Virtual WANセキュアハブに紐付ける形で行います。これにより、IPアドレスの持ち込み（BYOIP）が可能となり、IP変更による運用影響を低減します。活用例としては、複数リージョンでのグローバルIP統一や、既存のIP制限を持つ外部サービスとの接続時に有効です。注意点として、顧客提供IPは事前にAzureに登録・承認が必要であり、IPの所有権証明や適切なルーティング設定が求められます。また、Azure Firewallのスケーリングや冗長構成時のIP管理に留意が必要です。関連サービスとしては、Virtual WANのハブ構成、Azure Firewallポリシー、IP管理のAzure Resource Manager連携が挙げられ、これらを組み合わせた一元的なネットワークセキュリティ運用が可能です。詳細は公式ドキュメント参照を推奨します。

---

### 3. Generally Available: Firmware analysis enabled by Azure Arc 

**公開日時**: 2025年10月09日 14:15:20 UTC
**リンク**: [Generally Available: Firmware analysis enabled by Azure Arc ](https://azure.microsoft.com/updates?id=512201)

**アップデートID**: 512201
**情報源**: Azure Updates API

**カテゴリ**: Launched, Hybrid + multicloud, Azure Arc, Features

**要約**:

- 何が更新されたか  
Azure Arcによるファームウェア分析機能が一般提供（GA）となりました。

- 主な変更点や新機能  
IoT/OTやネットワーク機器のファームウェアを詳細に解析し、従来ブラックボックス化していたソフトウェアのセキュリティ状態を可視化可能に。

- 影響を受ける対象  
Azure Arcで管理されるIoT/OTデバイスやネットワーク機器の運用・セキュリティ担当者。

- 注意点  
ファームウェア分析にはAzure Arcの導入が前提となり、対応デバイスの確認が必要です。

**詳細**:

Azure Arc対応のファームウェア分析機能が一般提供（GA）となりました。本機能はIoT/OTやネットワーク機器のファームウェアを詳細に解析し、従来「ブラックボックス化」しがちなデバイスのソフトウェア構成や脆弱性を可視化します。Azure Arcによりオンプレミスやマルチクラウド環境のデバイスを一元管理し、Azure Security Centerと連携してファームウェアのセキュリティ評価を実現します。解析はAzure Arcエージェントを通じて対象デバイスのファームウェアイメージを収集し、クラウド上の分析エンジンでマルウェア検出や脆弱性スキャンを行います。活用例としては製造業のOT機器監視やネットワーク機器のセキュリティ強化が挙げられ、既存のAzure SentinelやAzure Defenderと統合することで包括的なセキュリティ運用が可能です。制限としては対応デバイスの種類やファームウェア形式に依存し、全てのIoT/OT機器に対応しているわけではありません。導入時はAzure Arcのセットアップとエージェント展開が前提となり、ネットワーク帯域やプライバシー保護にも留意が必要です。

---

### 4. Retirement: Azure AI Health Insights and related models

**公開日時**: 2025年10月09日 12:45:35 UTC
**リンク**: [Retirement: Azure AI Health Insights and related models](https://azure.microsoft.com/updates?id=502049)

**アップデートID**: 502049
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

- 何が更新されたか  
Azure AI Health InsightsサービスおよびClinical Trials Matcher、Radiology Insightsモデルの廃止が発表されました。

- 主な変更点や新機能  
これらのサービス・モデルは2025年12月31日をもって提供終了となり、新規利用や統合ができなくなります。

- 影響を受ける対象  
これらのサービスを利用中の開発者や医療関連アプリケーションが影響を受けます。

- 注意点  
廃止までに代替サービスへの移行計画を立てる必要があります。

**詳細**:

本アップデートは、AzureのAIポートフォリオ戦略見直しの一環として、Azure AI Health InsightsサービスおよびClinical Trials Matcher、Radiology Insightsモデルの2025年12月31日付けでの廃止を通知するものです。これらのサービスは医療データ解析や臨床試験マッチング、画像診断支援を目的としたAIモデル群であり、廃止後はAPI呼び出しや統合が不可となります。技術的には、これらのモデルはAzure Cognitive Servicesの一部として提供され、REST API経由で医療関連データの解析や推論を行っていました。活用シナリオとしては、医療機関での患者データ解析や臨床試験候補者の特定、放射線画像の自動診断支援が挙げられます。廃止に伴い、これらの機能を利用したアプリケーションは代替サービスへの移行が必須であり、データ連携やAPI仕様の変更に注意が必要です。関連サービスとしてはAzure Health Data ServicesやAzure Machine Learningがあり、これらを活用したカスタムモデル開発やデータ統合による代替策が推奨されます。移行計画を早期に策定し、影響範囲の特定と対応を進めることが重要です。詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=502049）を参照してください。

---


*このレポートは自動生成されました - 2025-10-10 12:01:38 JST*