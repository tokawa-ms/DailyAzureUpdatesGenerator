# 2025年07月30日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年07月30日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Generally Available: Customer-controlled maintenance

**公開日時**: 2025年07月29日 17:00:48 UTC
**リンク**: [Generally Available: Customer-controlled maintenance](https://azure.microsoft.com/updates?id=499396)

**アップデートID**: 499396
**情報源**: Azure Updates API

**カテゴリ**: Launched, Hybrid + multicloud, Networking, Security, Azure ExpressRoute, Virtual WAN, VPN Gateway, Features, Management, Services

**要約**:

- 何が更新されたか  
Point-to-Site VPN Gateway（P2S VPN）を含むVirtual WANサービスで、顧客がメンテナンス時間を設定できる「顧客制御メンテナンス」が一般提供開始。

- 主な変更点や新機能  
P2S VPN Gatewayのメンテナンスを任意の時間帯にスケジュール可能となり、運用影響を最小化できる。

- 影響を受ける対象  
Virtual WANのP2S VPN Gatewayを利用している顧客。

- 注意点があれば記載  
メンテナンスウィンドウの設定は適切に行い、業務時間外を選択するなど影響を考慮する必要がある。

**詳細**:

本アップデートは、Azure Virtual WANのPoint-to-Site VPN（P2S VPN）ゲートウェイにおけるメンテナンス時間を顧客が制御可能にする機能の一般提供開始を示します。従来、ゲートウェイのメンテナンスはAzure側で自動的に実施され、予期せぬダウンタイムが発生する可能性がありました。本機能により、顧客はメンテナンスウィンドウを設定し、業務影響を最小化しつつ計画的なメンテナンスを実施可能です。

具体的には、Azure PortalやAzure CLI、REST APIを通じてP2S VPNゲートウェイのメンテナンスウィンドウを設定できます。設定可能な時間帯は週単位で指定可能で、ゲートウェイの再起動やアップデートはその期間内に実施されます。これにより、VPN接続の切断タイミングを制御し、業務継続性を確保できます。

技術的には、Virtual WANの管理プレーンが顧客指定のメンテナンス時間を認識し、その期間内にゲートウェイのメンテナンス作業をスケジューリングします。設定はAzure Resource Managerテンプレートやスクリプトで自動化可能で、運用効率向上に寄与します。

活用シナリオとしては、グローバルに分散した拠点間VPN接続を持つ企業が、業務時間外にメンテナンスを集中させることで通信断を最小化するケースが挙げられます。また、複数ゲートウェイのメンテナンスを段階的に実施し、冗長性を維持しながらアップデートを行う運用も可能です。

注意点として、メンテナンスウィンドウは最大72時間まで設定可能ですが、ウィンドウ外での緊急メンテナンスはAzure側で実施される場合があります。また、P2S VPNゲートウェイのSKUによっては本機能が利用できない場合があるため、事前にSKU対応状況を確認する必要があります。

関連サービスとしては、Virtual WANのハブVPNゲートウェイ全般に適用されるため、Site-to-Site VPNやExpressRouteとの組み合わせ運用時にもメンテナンス計画の一環として活用可能です。Azure Monitorと連携し、メンテナンス時のログやアラートを取得することで運用監視を強化できます。

---

### 2. Retirement: Azure Front Door (classic) and Azure CDN from Microsoft Classic SKU ending CNAME based domain validation and new domain/profile creations by August 15, 2025

**公開日時**: 2025年07月29日 14:30:43 UTC
**リンク**: [Retirement: Azure Front Door (classic) and Azure CDN from Microsoft Classic SKU ending CNAME based domain validation and new domain/profile creations by August 15, 2025](https://azure.microsoft.com/updates?id=498522)

**アップデートID**: 498522
**情報源**: Azure Updates API

**カテゴリ**: Networking, Security, Media, Web, Azure Front Door, Content Delivery Network, Features, Retirements, Services

**要約**:

- 何が更新されたか  
Azure Front Door (classic)およびAzure CDN from Microsoft Classic SKUで、新規ドメインの追加やプロファイル作成が2025年8月15日以降できなくなります。  

- 主な変更点や新機能  
DigiCertによるCNAMEベースのドメイン検証（DCV）が廃止されるため、これらのサービスでの新規ドメイン検証がサポート終了します。  

- 影響を受ける対象  
Azure Front Door (classic)およびAzure CDN Classic SKUを利用中のユーザー。  

- 注意点  
既存のドメインやプロファイルは引き続き利用可能ですが、新規作成は不可。移行計画の検討が必要です。

**詳細**:

本アップデートは、Azure Front Door (classic)およびAzure CDN from Microsoft Classic SKUにおける新規ドメインの追加および新規プロファイル作成のサポート終了を2025年8月15日付で実施するものです。背景には、DigiCertによるCNAMEベースのドメインコントロール検証（DCV）の廃止があり、これに伴いClassic SKUの検証方式が非対応となるため、セキュリティ強化と運用効率化を目的としています。具体的には、Classic SKUではCNAMEレコードを用いたDCVが利用できなくなり、新規ドメイン登録時の検証が不可能となるため、新規プロファイル作成も停止されます。既存のドメインやプロファイルは引き続き利用可能ですが、将来的な機能拡張やセキュリティ更新は推奨されません。技術的には、Azure Front Door Standard/PremiumやAzure CDN Standard/Premium SKUへの移行が推奨され、これらはCNAME以外のDNS検証方式やより高度なセキュリティ機能をサポートします。移行に際しては、既存のCNAMEレコード設定を見直し、新SKUの検証手順に従う必要があります。Azure Front DoorやCDNを用いたグローバル配信や負荷分散のシナリオでは、最新SKUへの切り替えによりTLS証明書管理の自動化やパフォーマンス向上が期待できます。注意点として、Classic SKUの新規利用停止に伴い、運用中のサービスは計画的な移行を行わないと将来的なサポート切れリスクがあるため、早期対応が必須です。関連サービスとの連携では、Azure DNSやAzure Key Vaultを活用した証明書管理の統合が推奨されます。詳細は公式アップデート（https://azure.microsoft.com/updates?id=498522）を参照してください。

---


*このレポートは自動生成されました - 2025-07-30 12:01:10 JST*