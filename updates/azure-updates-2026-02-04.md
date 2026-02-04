# 2026年02月04日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年02月04日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Public Preview: X-Forwarded-For (XFF) grouping for rate limiting on Application Gateway WAF v2

**公開日時**: 2026年02月03日 20:30:31 UTC
**リンク**: [Public Preview: X-Forwarded-For (XFF) grouping for rate limiting on Application Gateway WAF v2](https://azure.microsoft.com/updates?id=555205)

**アップデートID**: 555205
**情報源**: Azure Updates API

**カテゴリ**: In development, Networking, Security, Web Application Firewall

**要約**:

- 何が更新されたか  
Application Gateway WAF v2で、X-Forwarded-For（XFF）ヘッダーを用いたレート制限のグルーピング機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
プロキシやCDN背後の環境でも、XFFヘッダーを基にしたIP単位でのレート制限が可能になり、より正確なトラフィック制御が実現します。

- 影響を受ける対象  
Application Gateway WAF v2を利用し、プロキシやCDN経由でトラフィックを受けている環境の技術者。

- 注意点  
パブリックプレビュー機能のため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure Application Gateway WAF v2の新機能として、X-Forwarded-For（XFF）ヘッダーを用いたレート制限のグルーピングがパブリックプレビューで提供開始されました。従来、WAFのレート制限はクライアントIP単位で行われていましたが、プロキシやCDNを経由する環境では実際のクライアントIPが隠蔽されるため、正確な制御が困難でした。本アップデートにより、XFFヘッダー内の実クライアントIPを基にグルーピング可能となり、より精緻なレート制限が実現します。実装はWAFポリシーのRateLimit設定でGroupByオプションに「X-Forwarded-For」を指定する形で行い、複数のXFF値がある場合は最左のIPを優先的に使用します。これにより、例えばAzure Front Doorや他のCDN経由でApplication Gatewayを運用する際、真のクライアント単位での攻撃検知やトラフィック制御が可能です。注意点として、XFFヘッダーはクライアント側で改ざんされる可能性があるため、信頼できるプロキシ経由のトラフィックに限定して利用すべきです。また、XFFを用いたレート制限はWAF v2のみ対応し、v1では非対応です。Azure Front DoorやAzure CDNとの連携で効果的に活用でき、セキュリティ強化とサービスの安定運用に寄与します。詳細は公式ドキュメントで最新情報を確認してください。

---

### 2. Generally Available: Azure Container Storage v2.1.0 now with Elastic SAN integration and on demand installation

**公開日時**: 2026年02月03日 20:30:31 UTC
**リンク**: [Generally Available: Azure Container Storage v2.1.0 now with Elastic SAN integration and on demand installation](https://azure.microsoft.com/updates?id=553917)

**アップデートID**: 553917
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Compute, Azure Container Storage, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
Azure Container Storage v2.1.0がGAリリースされました。

- 主な変更点や新機能  
Elastic SANのネイティブサポートを追加し、軽量でオンデマンドのインストールモデルを導入。Kubernetes環境での展開と運用が簡素化されます。

- 影響を受ける対象  
Azure上でKubernetesを利用し、コンテナストレージを管理する技術者や運用チーム。

- 注意点があれば記載  
既存環境への移行時はElastic SAN対応状況とインストール方法の変更点を確認してください。

**詳細**:

Azure Container Storage（ACS）v2.1.0が一般提供（GA）となり、Elastic SANのネイティブサポートとオンデマンドインストール機能が追加されました。本アップデートは、Kubernetes上のストレージ管理を簡素化し、スケーラブルかつ柔軟なストレージ利用を促進することを目的としています。Elastic SAN統合により、ACSは高性能かつ低レイテンシのブロックストレージを提供し、動的な容量拡張やIOPS調整が可能です。オンデマンドインストールは軽量なコンポーネント構成で、必要時にのみインストールできるため、運用負荷を軽減します。技術的には、CSI（Container Storage Interface）ドライバーを通じてElastic SANと連携し、KubernetesのPersistentVolumeとして利用可能です。活用シナリオとしては、ステートフルなアプリケーションやデータベースコンテナの高可用性ストレージ基盤として最適です。注意点としては、Elastic SANのリージョン対応状況や容量上限、パフォーマンス要件の事前検証が必要です。ACSはAzure Kubernetes Service（AKS）と密接に連携し、Azure MonitorやAzure Policyと組み合わせて運用管理の自動化も可能です。詳細は公式ドキュメントを参照してください。

---

### 3. Public Preview: Azure Kubernetes Fleet Manager namespace-scoped resource placement 

**公開日時**: 2026年02月03日 20:30:31 UTC
**リンク**: [Public Preview: Azure Kubernetes Fleet Manager namespace-scoped resource placement ](https://azure.microsoft.com/updates?id=548198)

**アップデートID**: 548198
**情報源**: Azure Updates API

**カテゴリ**: In preview, Containers, Azure Kubernetes Fleet Manager

**要約**:

- 何が更新されたか  
Azure Kubernetes Fleet Managerで、namespace単位のリソース配置機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
複数クラスタ間で特定のnamespaceリソースを細かく選択・同期可能に。リソース管理の柔軟性が向上。

- 影響を受ける対象  
複数Kubernetesクラスタを管理し、namespace単位でリソース制御を行う技術者や運用チーム。

- 注意点があれば記載  
プレビュー機能のため、本番環境での利用は慎重に。今後のアップデートで仕様変更の可能性あり。

**詳細**:

Azure Kubernetes Fleet Managerのパブリックプレビューで提供開始された「namespace-scoped resource placement」は、複数クラスタ間で個別のネームスペース単位リソースの選択と伝播を細かく制御可能にする機能です。従来はクラスタ単位でのリソース管理が主流でしたが、本機能によりネームスペース単位でのリソース配置が可能となり、マルチクラスタ環境での運用柔軟性が大幅に向上します。技術的には、Fleet Managerが管理する複数のKubernetesクラスタに対し、指定ネームスペースのConfigMapやSecretなどのリソースを選択的に同期・配置する仕組みを提供。実装はCRD（カスタムリソース定義）を用いたポリシーベースの管理で、対象ネームスペースのリソースを明示的に指定し、Fleet Managerが自動的に複数クラスタへ反映します。活用例としては、複数環境にまたがるアプリケーションの設定情報や認証情報をネームスペース単位で一元管理しつつ、必要なクラスタにのみ配布するケースが挙げられます。注意点としては、プレビュー段階のため機能制限やAPIの変更可能性があり、運用前に十分な検証が必要です。また、Azure Arc対応クラスタとの連携により、オンプレや他クラウドのKubernetes環境も含めた統合管理が可能です。本機能はマルチクラスタ運用の効率化とセキュリティ向上に寄与し、Azure Kubernetes Fleet Managerの管理範囲をより細分化・最適化する重要なアップデートです。

---


*このレポートは自動生成されました - 2026-02-04 12:01:30 JST*