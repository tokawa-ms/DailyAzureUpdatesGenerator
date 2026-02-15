# 2026年02月09日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年02月09日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Public Preview: Application Gateway for Containers - AKS managed add-on 

**公開日時**: 2026年02月09日 19:45:45 UTC
**リンク**: [Public Preview: Application Gateway for Containers - AKS managed add-on ](https://azure.microsoft.com/updates?id=555603)

**アップデートID**: 555603
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Application Gateway, Features

**要約**:

- 何が更新されたか  
Application Gateway for ContainersのAKSマネージドアドオンがパブリックプレビューで提供開始。

- 主な変更点や新機能  
AKSクラスター上でApplication Gateway for ContainersとALB Controllerの導入・管理が容易になり、アドオンとして有効化可能。

- 影響を受ける対象  
AKS（Azure Kubernetes Service）を利用する開発者・運用者。

- 注意点  
現在はパブリックプレビューのため、本番環境での利用は慎重に検討が必要です。

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）向けに「Application Gateway for Containers」のマネージドアドオンのパブリックプレビュー提供を開始したものです。これにより、従来手動で行っていたApplication Gateway for ContainersおよびALB Controllerのデプロイやライフサイクル管理が、AKSのアドオンとして簡素化されます。具体的には、Azure CLIやPortalからアドオンを有効化するだけで、必要なリソースのプロビジョニングや設定が自動化され、運用負荷が大幅に軽減されます。内部的には、AKSクラスターにALB Controllerが自動デプロイされ、Kubernetes Ingressリソースと連携してL7ロードバランシング機能を提供します。WebアプリやAPIの公開、マルチテナント環境でのトラフィック制御などに活用可能です。現時点ではプレビューのため、本番環境での利用は推奨されず、機能制限や将来的な仕様変更の可能性があります。Azure MonitorやAzure Policyなど他のAzureサービスとの統合も可能です。

---


*このレポートは自動生成されました - 2026-02-16 01:55:49 JST*