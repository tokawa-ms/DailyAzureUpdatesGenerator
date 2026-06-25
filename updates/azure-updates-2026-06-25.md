# 2026年06月25日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年06月25日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Public Preview: Application Gateway for Containers – Inference gateway

**公開日時**: 2026年06月24日 19:00:43 UTC
**リンク**: [Public Preview: Application Gateway for Containers – Inference gateway](https://azure.microsoft.com/updates?id=566516)

**アップデートID**: 566516
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS), Features, Services

**要約**:

- 何が更新されたか  
Application Gateway for Containersに「Inference gateway」機能が追加され、パブリックプレビューとして提供開始されました。

- 主な変更点や新機能  
Kubernetes Gateway API Inference ExtensionがApplication Gateway for Containersに統合され、AI推論ワークロード向けのゲートウェイ機能が利用可能になりました。これにより、Kubernetes環境でAI推論サービスへのトラフィック管理やルーティングが容易になります。

- 影響を受ける対象  
Kubernetes上でAI推論ワークロードを運用している技術者や、Application Gateway for Containersを利用しているユーザーが主な対象です。AI推論サービスの運用効率向上や、トラフィック制御の高度化が期待できます。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用は慎重に検討してください。正式リリース前のため、仕様変更や制限が発生する可能性があります。

**詳細**:

Azure Update「Public Preview: Application Gateway for Containers – Inference gateway」について説明します。

本アップデートは、Application Gateway for ContainersのIngress Gateway機能セットを拡張し、新たにAI Gateway機能を追加するものです。具体的には、Inference Gateway機能が導入され、Kubernetes Gateway API Inference ExtensionをApplication Gateway for Containers上で利用可能となります。これにより、Kubernetes環境において、AI推論ワークロードのゲートウェイ管理が容易になります。

Application Gateway for Containersは、Azure上でコンテナ化されたアプリケーションのトラフィック管理を行うサービスです。今回のアップデートでは、Inference Gateway機能が追加され、Kubernetes Gateway APIのInference Extensionと連携することで、AI推論サービスへのトラフィックルーティングや管理が効率化されます。これにより、AIモデルの推論リクエストを適切なバックエンドサービスへルーティングすることが可能となります。

技術的な仕組みとしては、Kubernetes Gateway APIのInference Extensionを利用し、Application Gateway for ContainersがAI推論リクエストの受信、ルーティング、管理を行います。これにより、Kubernetesクラスタ内のAI推論サービスを外部から安全かつ効率的に公開することができます。実装方法としては、Kubernetes Gateway APIの定義に従い、Inference Gatewayを構成し、Application Gateway for Containersと連携させることで、AI推論ワークロードのIngress管理が実現されます。

活用シナリオとしては、Azure Kubernetes Service（AKS）上でAI推論サービスを運用する場合に、Inference Gatewayを利用することで、推論リクエストのスケーラブルな受信やルーティング、セキュアな公開が可能となります。例えば、画像認識や自然言語処理などのAIモデルをAKS上でデプロイし、外部からの推論リクエストをApplication Gateway for Containers経由で効率的に処理することができます。

注意点や制限事項としては、本機能はパブリックプレビュー段階であり、本番環境での利用には慎重な検証が必要です。また、Inference Gateway機能の詳細な設定や制約については、公式ドキュメントやアップデートページを参照する必要があります。

関連するAzureサービスとしては、Azure Kubernetes Service（AKS）、Application Gateway for Containers、Kubernetes Gateway APIなどが挙げられます。これらのサービスと連携することで、AI推論ワークロードの管理と公開が効率化されます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=566516）をご参照ください。

---


*このレポートは自動生成されました - 2026-06-25 12:01:02 JST*