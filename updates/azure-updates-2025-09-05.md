# 2025年09月05日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月05日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Generally Available: Multiple address prefixes for subnets in Azure Virtual Networks

**公開日時**: 2025年09月04日 21:00:07 UTC
**リンク**: [Generally Available: Multiple address prefixes for subnets in Azure Virtual Networks](https://azure.microsoft.com/updates?id=502583)

**アップデートID**: 502583
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Virtual Network, Features

**要約**:

- 何が更新されたか  
Azure Virtual Networkのサブネットで複数のアドレスプレフィックスがサポートされ、GA（一般提供）となりました。

- 主な変更点や新機能  
従来はサブネットごとに単一のアドレスプレフィックスのみ対応でしたが、複数プレフィックスを割り当て可能になり、IPアドレス空間の拡張や柔軟なネットワーク設計が可能です。

- 影響を受ける対象  
大規模ネットワークや複雑なIPアドレス管理を行うAzure VNet利用者。

- 注意点があれば記載  
既存サブネットの設計変更時はIPアドレスの重複やルーティング設定に注意が必要です。

**詳細**:

Azure Virtual Network（VNet）のサブネットに複数のアドレスプレフィックスを割り当て可能となる機能がGA（一般提供）されました。従来、サブネットは単一のCIDRブロックのみ対応しており、アドレス空間の拡張や複雑なネットワーク設計に制約がありました。本アップデートにより、一つのサブネット内で複数の非連続または連続したIPv4/IPv6プレフィックスを設定可能となり、柔軟なIPアドレス管理が実現します。

技術的には、Azure Resource ManagerテンプレートやAzure CLI、PowerShellでsubnetのaddressPrefixesプロパティに複数のCIDRを指定可能です。これにより、既存サブネットの拡張や分割なしでIPアドレスの追加が可能となり、スケールアウトや複数サービスの共存に有効です。

活用例として、大規模なマルチテナント環境でのIPアドレス管理、オンプレミスとの複数IPレンジ統合、異なるアプリケーション層ごとのIP分割などが挙げられます。注意点として、サブネットの複数プレフィックスは同一VNet内で重複しないこと、NSGやルートテーブルの設定が複数プレフィックスに適用される点を考慮する必要があります。

本機能はAzure Firewall、Azure Load Balancer、VPN Gatewayなどのネットワークサービスと連携可能で、より高度なネットワーク設計やセキュリティ構成に寄与します。既存環境への適用は段階的に検証し、IPアドレスの重複やルーティングの整合性を十分に確認することが推奨されます。

---

### 2. Generally Available: Upgrade existing Azure Gen1 VMs to Gen2-Trusted launch

**公開日時**: 2025年09月04日 18:15:11 UTC
**リンク**: [Generally Available: Upgrade existing Azure Gen1 VMs to Gen2-Trusted launch](https://azure.microsoft.com/updates?id=499104)

**アップデートID**: 499104
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Virtual Machines, Compliance, Operating System, Security, Features

**要約**:

- 何が更新されたか  
既存のAzure Gen1 VMをGen2-Trusted Launch VMへアップグレードする機能が一般提供開始。

- 主な変更点や新機能  
Trusted Launchによるセキュリティ強化（セキュアブート、仮想TPM、コード整合性保護）がGen1 VMでも利用可能に。

- 影響を受ける対象  
既存のAzure Gen1 VMユーザーで、セキュリティ強化を図りたい技術者。

- 注意点があれば記載  
アップグレードにはVMの再起動が必要で、互換性やサポート状況を事前に確認すること。

**詳細**:

本アップデートは、既存のAzure Gen1仮想マシン（VM）をGen2 Trusted Launch対応VMへアップグレード可能にし、VMの基盤セキュリティを強化することを目的としています。Trusted Launchは、セキュアブート、仮想化ベースのセキュリティ（VBS）、コード整合性保護を組み合わせ、ブートプロセスの改ざん検知やマルウェア防止を実現します。従来はGen2 VM作成時のみ利用可能でしたが、本アップデートにより既存Gen1 VMを停止後にGen2 Trusted Launchへ変換可能となり、運用中VMのセキュリティ強化が容易になります。実装はAzure CLIやPowerShellの専用コマンドで行い、VMの世代変更とTrusted Launch有効化を同時に実施します。活用例としては、セキュリティ要件が厳しい金融機関や政府機関の既存VM保護強化が挙げられます。注意点としては、Gen1からGen2への変換はVM停止が必須であり、一部のOSやカスタムイメージは非対応の可能性があるため事前検証が必要です。さらに、Azure Security CenterやAzure Defenderと連携し、Trusted Launchの状態監視や脅威検出を統合的に実施可能です。詳細は公式ドキュメントとアップデートページを参照してください。

---

### 3. Generally Available: Near-zero-downtime maintenance in Azure Database for MySQL 

**公開日時**: 2025年09月04日 16:30:46 UTC
**リンク**: [Generally Available: Near-zero-downtime maintenance in Azure Database for MySQL ](https://azure.microsoft.com/updates?id=500765)

**アップデートID**: 500765
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Azure Database for MySQL, Features

**要約**:

- 何が更新されたか  
Azure Database for MySQL Flexible Serverの高可用性(HA)構成で、ほぼダウンタイムなしのメンテナンスが一般提供開始。

- 主な変更点や新機能  
専用のHAアーキテクチャを採用し、メンテナンス時のサービス停止を極小化。

- 影響を受ける対象  
Azure Database for MySQL Flexible ServerのHA有効化ユーザー。

- 注意点があれば記載  
HA構成が前提のため、シングルインスタンス利用時は対象外。メンテナンス計画時も影響を確認推奨。

**詳細**:

Azure Database for MySQL – Flexible Serverの高可用性(HA)構成において、ダウンタイムをほぼゼロに抑えたメンテナンスがGAとなりました。本アップデートは、従来のメンテナンス時に発生していたサービス停止を最小化し、業務継続性を向上させることを目的としています。新たに導入された専用のHAアーキテクチャは、プライマリとセカンダリノード間でのフェイルオーバーを迅速かつシームレスに実行可能にし、メンテナンス中もクライアント接続を維持します。具体的には、メンテナンス対象ノードを順次切り替えながら更新を行い、接続の切断や再接続を極力回避します。活用シナリオとしては、ミッションクリティカルなWebアプリケーションやリアルタイムデータ処理環境での継続的運用が挙げられます。注意点として、HA構成が必須であり、Flexible Serverのシングルサーバー構成では本機能は利用できません。また、メンテナンスの種類や規模によっては短時間の接続遅延が発生する可能性があります。関連サービスとしては、Azure Monitorによるメンテナンス状況の監視や、Azure Private Linkを用いたセキュアな接続構成と組み合わせることで、信頼性とセキュリティを強化可能です。詳細は公式ドキュメントおよびアップデートページを参照してください。

---


*このレポートは自動生成されました - 2025-09-05 12:01:25 JST*