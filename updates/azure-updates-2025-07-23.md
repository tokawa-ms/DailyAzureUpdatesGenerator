# 2025年07月23日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年07月23日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Public Preview: Web Application Firewall (WAF) running on Application Gateway for Containers

**公開日時**: 2025年07月22日 16:00:45 UTC
**リンク**: [Public Preview: Web Application Firewall (WAF) running on Application Gateway for Containers](https://azure.microsoft.com/updates?id=498272)

**アップデートID**: 498272
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS), Web Application Firewall, Features, Services

**要約**:

- 何が更新されたか  
Application Gateway for ContainersでWeb Application Firewall（WAF）がパブリックプレビューとして利用可能に。

- 主な変更点や新機能  
Kubernetesクラスター上のコンテナワークロード向けに、レイヤ7負荷分散と動的トラフィック管理に加え、WAFによるセキュリティ保護が追加。

- 影響を受ける対象  
AKSや他のKubernetes環境でApplication Gateway for Containersを利用する開発者・運用者。

- 注意点があれば記載  
プレビュー版のため、本番環境での利用は慎重に。設定やパフォーマンスの検証が必要。

**詳細**:

本アップデートは、Kubernetes上で稼働するコンテナワークロード向けに提供されるApplication Gateway for ContainersにWeb Application Firewall（WAF）機能を追加し、セキュリティ強化とトラフィック管理の一元化を目的としています。Application Gateway for Containersはレイヤー7のロードバランサーで、動的なトラフィックルーティングを実現しますが、今回のパブリックプレビューにより、OWASPコアルールセットに基づくWAFが統合され、SQLインジェクションやクロスサイトスクリプティングなどの攻撃からアプリケーションを保護可能です。技術的には、Application GatewayのWAFモジュールがKubernetes Ingressコントローラーと連携し、Ingressリソースを通じてWAFポリシーを適用します。これにより、マイクロサービス環境下でのセキュリティポリシー管理が容易になります。利用シナリオとしては、AKSクラスタ上の複数コンテナサービスに対し、統一したセキュリティルールを適用しつつ、負荷分散を行うケースが挙げられます。注意点としては、現時点でパブリックプレビューのため、SLAs非適用や一部機能制限が存在し、商用環境での利用は慎重に検討が必要です。また、Azure MonitorやAzure Security Centerと連携することで、ログ収集やセキュリティアラートの統合管理が可能です。詳細は公式ドキュメントを参照し、環境に応じたWAFルールのカスタマイズを推奨します。

---


*このレポートは自動生成されました - 2025-07-23 12:00:59 JST*