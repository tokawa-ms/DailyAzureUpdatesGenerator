# 2025年09月19日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月19日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Retirement: Licensing changes for future Azure VMware Solution subscriptions starting October 16, 2025.

**公開日時**: 2025年09月18日 20:45:29 UTC
**リンク**: [Retirement: Licensing changes for future Azure VMware Solution subscriptions starting October 16, 2025.](https://azure.microsoft.com/updates?id=503878)

**アップデートID**: 503878
**情報源**: Azure Updates API

**カテゴリ**: Compute, Azure VMware Solution, Retirements

**要約**:

- 何が更新されたか  
2025年10月16日以降、Azure VMware Solution（AVS）の新規サブスクリプションに対し、BroadcomのVMwareライセンス方針が変更されます。

- 主な変更点や新機能  
新規顧客はハイパースケーラー環境で利用する際、自身でポータブルなVMware Cloud Foundation（VCF）サブスクリプションを用意する必要があります。

- 影響を受ける対象  
2025年10月16日以降にAVSを新規契約する顧客が対象。既存のAVS利用者は影響を受けません。

- 注意点  
既存顧客は継続利用可能ですが、新規契約時はライセンス調達の準備が必要です。ライセンスコストや運用管理に影響が出る可能性があります。

**詳細**:

本アップデートは、BroadcomによるVMwareライセンス方針変更に伴い、2025年10月16日以降に新規契約されるAzure VMware Solution（AVS）サブスクリプションに対し、顧客が自身でポータブルなVMware Cloud Foundation（VCF）サブスクリプションを持ち込む（BYOS）ことを必須化するものです。これにより、従来のAVSのライセンスモデルが改変され、新規顧客はBroadcom提供のVCFライセンスを別途購入し、Azure上で利用する形態となります。既存のAVS契約者は影響を受けず、従来通りの運用が可能です。技術的には、AVS環境構築時にVCFライセンスの登録・認証が必要となり、ライセンス管理が顧客側に移行します。これにより、ライセンスの柔軟性が向上する一方、ライセンス管理負荷が増加します。活用シナリオとしては、オンプレVMware環境からのクラウド移行やハイブリッド運用で、既存VCFライセンスを活用しコスト最適化が可能です。注意点として、ライセンス未準備の場合はAVSの新規利用が制限されるため、事前のライセンス調達と管理体制構築が必須です。AVSはAzureのネットワークやストレージサービスと連携し、Azure MonitorやAzure Security Centerによる統合管理も可能であり、ライセンス変更後もこれらの連携は継続されます。詳細は公式ドキュメントとBroadcomのライセンスガイドを参照してください。

---

### 2. Generally Available: DCa/ECa v6 series AMD based confidential virtual machines (VMs) 

**公開日時**: 2025年09月18日 19:00:07 UTC
**リンク**: [Generally Available: DCa/ECa v6 series AMD based confidential virtual machines (VMs) ](https://azure.microsoft.com/updates?id=502874)

**アップデートID**: 502874
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Virtual Machines, Features

**要約**:

- 何が更新されたか  
DCa/ECa v6シリーズのAMDベース機密仮想マシン（VM）が一般提供開始。

- 主な変更点や新機能  
第4世代AMD EPYCプロセッサ搭載で、機密コンピューティング対応。UAE北部、韓国中央、米国西中央、南アフリカ北部、スイス北部、英国南部リージョンで利用可能。

- 影響を受ける対象  
機密性の高いワークロードをAzureで運用する開発者・運用者。

- 注意点があれば記載  
対応リージョンが限定されているため、利用前にリージョン確認が必要。

**詳細**:

本アップデートは、AMD第4世代EPYCプロセッサを搭載したDCa/ECa v6シリーズの機密仮想マシン（Confidential VM）がUAE北部、韓国中央、西中央米国、南アフリカ北部、スイス北部、英国南部リージョンで一般提供開始されたことを示す。目的は、Azure Confidential Computingの強化であり、ハードウェアベースの信頼できる実行環境（TEE）を活用し、データの暗号化と処理中のデータ保護を両立することにある。DCa/ECa v6はAMD SEV-SNP（Secure Encrypted Virtualization – Secure Nested Paging）技術を採用し、ゲストOSレベルでのメモリ暗号化と改ざん防止を実現。これにより、クラウド上での機密性の高いワークロードを安全に実行可能となる。実装はAzureポータルやCLIから通常のVM作成手順にてサイズ指定するだけで利用可能。主な活用シナリオは、金融サービスや医療、政府機関など機密データを扱うアプリケーションの保護であり、特に規制遵守やデータプライバシー強化が求められる環境に適している。注意点として、現時点で対応OSやイメージが限定的であり、一部リージョンのみで提供されているため、事前確認が必要。また、Azure Key Vaultとの連携によりキー管理を強化でき、Azure Attestationサービスと組み合わせて信頼性の検証も可能。これらにより、エンドツーエンドのセキュリティ強化が図られる。

---

### 3. Public Preview: Azure Kubernetes Fleet Manager – update run approval gates

**公開日時**: 2025年09月18日 17:30:18 UTC
**リンク**: [Public Preview: Azure Kubernetes Fleet Manager – update run approval gates](https://azure.microsoft.com/updates?id=503245)

**アップデートID**: 503245
**情報源**: Azure Updates API

**カテゴリ**: In preview, Containers, Compute, Azure Kubernetes Fleet Manager, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure Kubernetes Fleet Managerのアップデート実行に承認ゲート機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
アップデート実行の前後に承認ゲートを設定可能となり、手動承認による更新制御が強化されました。

- 影響を受ける対象  
Azure Kubernetes Fleet Managerを利用し、複数クラスターの更新管理を行う技術者。

- 注意点があれば記載  
承認ゲートの運用設計が必要で、手動承認による更新遅延の可能性があります。

**詳細**:

Azure Kubernetes Fleet Managerのアップデート実行に対して承認ゲート機能がパブリックプレビューで提供開始されました。本機能は、複数のクラスターを一括管理する更新プロセスにおける制御性を強化することを目的としています。具体的には、更新グループやステージの前後に承認ゲートを設定可能とし、管理者が手動で更新の進行を承認・拒否できる仕組みを提供します。これにより、更新の自動化と安全性のバランスを取りつつ、段階的な展開や問題発生時の即時停止が可能となります。技術的には、更新ランのワークフローに承認待ち状態を挿入し、Azure PortalやCLIから承認操作を実施します。活用例としては、大規模な複数リージョンのAKSクラスター更新時に、重要なステージでの承認を挟むことでリスク管理を強化できます。注意点として、承認ゲートは現在パブリックプレビュー段階のため、SLAやサポート範囲に制限があり、運用前に十分な検証が推奨されます。また、Azure PolicyやAzure Monitorと連携し、承認状況の監視やポリシー適用によるガバナンス強化が可能です。

---

### 4. Generally Available: Distributed tracing for Durable Functions 

**公開日時**: 2025年09月18日 17:00:27 UTC
**リンク**: [Generally Available: Distributed tracing for Durable Functions ](https://azure.microsoft.com/updates?id=503139)

**アップデートID**: 503139
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features

**要約**:

- 何が更新されたか  
Durable Functions向けの分散トレーシング機能（V2）が一般提供開始されました。

- 主な変更点や新機能  
オーケストレーション、アクティビティ、耐久エンティティ間の操作を一元的に関連付け可能な高度なトレーシングモデルを導入。

- 影響を受ける対象  
Durable Functionsを利用する開発者や運用チーム。

- 注意点  
既存のトレーシング設定との互換性や設定変更が必要な場合があります。  

詳細：https://azure.microsoft.com/updates?id=503139

**詳細**:

Azure Durable Functions向けに提供されるDistributed tracing V2は、オーケストレーション、アクティビティ、耐久エンティティ間の操作を一元的に関連付ける高度なトレーシングモデルを実装したものです。背景として、複雑な分散ワークフローの可視化とデバッグ効率向上が求められており、従来のトレーシング機能の拡張が目的です。具体的には、分散トレースの相関IDを自動的に伝播し、Azure Application InsightsやOpenTelemetryと連携可能な形式で詳細な実行経路を記録します。技術的にはDurable Task Frameworkの内部でトレースコンテキストを管理し、各関数呼び出しに紐づくトレースデータを生成・送信します。活用例としては、複数のアクティビティが連携する長時間実行ワークフローのパフォーマンス分析や障害箇所の特定が挙げられます。注意点としては、トレースデータ量の増加によるコスト増や、トレースの有効化設定が必要な点があり、適切なサンプリング設定が推奨されます。関連サービスではAzure MonitorやApplication Insightsとの統合が強化されており、統合監視基盤の構築に有効です。

---


*このレポートは自動生成されました - 2025-09-19 12:01:34 JST*