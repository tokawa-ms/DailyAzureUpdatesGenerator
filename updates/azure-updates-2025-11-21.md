# 2025年11月21日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年11月21日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 12 件

## 更新一覧

### 1. Public Preview: Container network metrics filtering in Advanced Container Networking Services for (ACNS) for AKS 

**公開日時**: 2025年11月20日 20:00:10 UTC
**リンク**: [Public Preview: Container network metrics filtering in Advanced Container Networking Services for (ACNS) for AKS ](https://azure.microsoft.com/updates?id=523076)

**アップデートID**: 523076
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）のAdvanced Container Networking Services（ACNS）で、コンテナネットワークメトリクスのフィルタリング機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
不要なネットワークメトリクスの収集を制御でき、ストレージコスト削減やダッシュボードの見やすさ向上が可能に。

- 影響を受ける対象  
AKS上でACNSを利用しているコンテナ環境の運用技術者。

- 注意点があれば記載  
プレビュー機能のため、本番環境での利用は慎重に検討し、最新のドキュメントを確認すること。

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）上のAdvanced Container Networking Services（ACNS）において、コンテナネットワークメトリクスのフィルタリング機能をパブリックプレビューで提供開始したものです。従来、コンテナ環境では大量のネットワークメトリクスが収集され、ストレージコストの増大や監視ダッシュボードの視認性低下を招いていました。本機能により、収集対象のメトリクスを細かく選別可能となり、必要な指標のみを効率的に取得できます。技術的には、ACNSのメトリクス収集パイプラインにフィルタリングルールを設定し、PrometheusやAzure Monitorなどへの送信前に不要なデータを除外します。これにより、監視コスト削減とパフォーマンス最適化が実現可能です。活用例としては、特定のネットワークトラフィック指標のみを抽出し、トラブルシューティングやリソース最適化に集中するケースが挙げられます。注意点としては、プレビュー段階のため一部機能制限や将来的な仕様変更の可能性がある点、またフィルタ設定ミスによる重要メトリクスの取りこぼしに注意が必要です。Azure Monitor、Log Analytics、Prometheusとの連携が強化されており、既存の監視基盤に柔軟に組み込めます。詳細は公式ドキュメントを参照してください。

---

### 2. Generally Available: MCP support for AI toolchain operator add-on in AKS

**公開日時**: 2025年11月20日 18:45:04 UTC
**リンク**: [Generally Available: MCP support for AI toolchain operator add-on in AKS](https://azure.microsoft.com/updates?id=523152)

**アップデートID**: 523152
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
AKSのAI Toolchain OperatorアドオンでModel Context Protocol（MCP）対応がGA（一般提供）となりました。

- 主な変更点や新機能  
KAITO推論ワークスペースとの統合が強化され、動的モデル管理やツール呼び出しが容易に。AIワークフローの自動化と拡張性が向上。

- 影響を受ける対象  
AKS上でAI推論基盤を構築・運用する開発者やデータサイエンティスト。

- 注意点  
既存環境でのMCP対応には設定変更が必要な場合があるため、アップデート前にドキュメント確認を推奨。

**詳細**:

本アップデートにより、Azure Kubernetes Service（AKS）上のAI Toolchain OperatorアドオンがModel Context Protocol（MCP）を用いたKAITO推論ワークスペースを正式サポートし、一般提供（GA）となりました。背景には、AIモデルの動的管理や複雑な推論パイプラインの効率化ニーズがあり、MCPによるモデルコンテキストの統一的管理とツール呼び出しの統合が目的です。具体的には、AI Toolchain OperatorがKAITO推論環境内で複数のAIツールやモデルを連携させ、動的にモデルコンテキストを共有・更新可能としました。技術的には、MCPプロトコルを介してモデルのメタデータや状態情報を標準化し、Operatorがこれを管理・同期することで、推論処理の一貫性と拡張性を確保します。活用例としては、複数AIモデルを組み合わせたマルチモーダル推論や、リアルタイムでモデル更新が必要なサービスに適しています。注意点として、MCP対応ツールやKAITO環境のバージョン整合性が必要であり、Operatorの設定ミスが推論結果に影響を与える可能性があります。関連サービスとしては、AKSのコンテナ管理機能、Azure Machine Learningのモデル管理機能と連携し、CI/CDパイプライン構築やスケーラブルな推論基盤の構築に寄与します。

---

### 3. Generally Available: Cluster-wide Cilium network policy with Azure CNI powered by Cilium for AKS 

**公開日時**: 2025年11月20日 18:30:02 UTC
**リンク**: [Generally Available: Cluster-wide Cilium network policy with Azure CNI powered by Cilium for AKS ](https://azure.microsoft.com/updates?id=523120)

**アップデートID**: 523120
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
AKSでAzure CNIを利用したCiliumによるクラスタ全体のネットワークポリシー管理機能がGA（一般提供）となりました。

- 主な変更点や新機能  
名前空間を跨いだ一貫性のあるネットワークポリシーをクラスタ全体で適用可能になり、マルチテナント環境での運用管理が容易に。

- 影響を受ける対象  
AKSクラスタをAzure CNIかつCiliumネットワークポリシーで運用するプラットフォームチームやセキュリティ担当者。

- 注意点  
既存のネットワークポリシーとの互換性や移行計画を事前に検討する必要があります。

**詳細**:

本アップデートは、Azure Kubernetes Service (AKS) におけるAzure CNIベースのCiliumネットワークプラグインで、クラスタ全体に適用可能なCiliumネットワークポリシーがGA（一般提供）となったことを示します。従来、Kubernetesの名前空間単位でのネットワークポリシー管理は複雑で、多テナント環境での一貫性確保が困難でした。本機能は、クラスタ全体を横断する統一的なネットワークポリシー適用を可能にし、セキュリティ強化と運用効率の向上を実現します。

具体的には、Azure CNIのIP管理機能を維持しつつ、Ciliumの高度なL3-L7レベルのポリシー制御を統合。CiliumのeBPFベースの高速パケット処理により、低レイテンシかつ柔軟なネットワーク制御が可能です。実装は、AKSクラスタにCiliumをAzure CNIの上にデプロイし、クラスタ全体ポリシーをCRD（CustomResourceDefinition）で定義・管理します。

活用シナリオとしては、マルチテナント環境でのセグメント分離、サービス間通信の細粒度制御、コンプライアンス遵守のための一元的なポリシー管理が挙げられます。注意点として、既存のネットワークポリシーとの競合回避や、Ciliumのバージョン互換性確認が必要です。また、Azure MonitorやAzure Policyと連携し、ポリシー適用状況の可視化やガバナンス強化が可能です。

本機能により、AKS上でのセキュアかつスケーラブルなネットワーク管理が実現し、運用負荷の軽減とセキュリティレベルの向上に寄与します。詳細は公式ドキュメントおよびアップデートページを参照ください。

---

### 4. Generally Available: Local redirect policy in Azure CNI powered by Cilium for AKS 

**公開日時**: 2025年11月20日 18:30:02 UTC
**リンク**: [Generally Available: Local redirect policy in Azure CNI powered by Cilium for AKS ](https://azure.microsoft.com/updates?id=523081)

**アップデートID**: 523081
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
Azure CNI powered by Cilium for AKSにおいて、Local redirect policyが一般提供(GA)となりました。

- 主な変更点や新機能  
クロスノードトラフィックによる遅延や性能ボトルネックを解消するため、同一ノード内でのトラフィックをローカルリダイレクトし、パフォーマンス向上を実現します。

- 影響を受ける対象  
高スケールなAKSクラスターでのネットワークパフォーマンス改善を求めるユーザー。

- 注意点があれば記載  
既存のネットワーク構成やポリシーとの整合性を確認し、適用前に検証を推奨します。

**詳細**:

Azure CNI powered by Cilium for AKSにおけるLocal Redirect Policyが一般提供開始されました。本アップデートは、高スケールなAKSクラスターで発生しやすいノード間トラフィックによるレイテンシやパフォーマンス低下を解消することを目的としています。Local Redirect Policyは、同一ノード内のPod間通信をローカルで完結させることで、不要なノード間ルーティングを排除し、通信遅延を削減します。技術的には、CiliumのBPF（Berkeley Packet Filter）ベースのデータプレーンがトラフィックの送信先を動的に判別し、ローカルネットワークパスへリダイレクトする仕組みを採用しています。これにより、ネットワークパフォーマンスが向上し、特にマイクロサービス間通信が頻繁な大規模分散アプリケーションに効果的です。導入はAKSクラスターのCilium CNI設定でLocal Redirectを有効化するだけで、既存のAzure MonitorやNetwork Watcherと連携しつつ運用可能です。ただし、ノード間通信が必要なケースや特定のネットワークポリシーとの互換性に注意が必要です。本機能は高パフォーマンスを求めるAKSユーザーに推奨されます。詳細は公式ドキュメントを参照してください。

---

### 5. Generally Available: Layer 7 policy with Advanced Container Networking Services (ACNS) for AKS

**公開日時**: 2025年11月20日 18:15:25 UTC
**リンク**: [Generally Available: Layer 7 policy with Advanced Container Networking Services (ACNS) for AKS](https://azure.microsoft.com/updates?id=523115)

**アップデートID**: 523115
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）向けのAdvanced Container Networking Services（ACNS）で、Layer 7ポリシーが一般提供（GA）となりました。

- 主な変更点や新機能  
マイクロサービス間のトラフィックをHTTP/HTTPSレベルで細かく制御可能になり、サービス間通信のセキュリティと管理性が向上します。

- 影響を受ける対象  
AKSを利用し、ACNSでネットワークポリシーを適用している開発者や運用チーム。

- 注意点があれば記載  
既存のLayer 3/4ポリシーとの併用や設定変更時は動作確認を推奨します。

**詳細**:

本アップデートは、マイクロサービス環境におけるトラフィック制御の高度化ニーズに対応し、Azure Kubernetes Service（AKS）向けのAdvanced Container Networking Services（ACNS）にLayer 7ポリシー機能をGA（一般提供）として追加したものです。Layer 7ポリシーにより、HTTP/HTTPSレベルでの細粒度なトラフィック制御が可能となり、パス、ヘッダー、メソッド単位でのルーティングやアクセス制御が実現します。実装はACNSのネットワークプラグインを通じて行われ、KubernetesのNetworkPolicy拡張として適用可能です。これにより、マイクロサービス間通信のセキュリティ強化やトラフィック分離、A/Bテストやカナリアリリースの精緻化が可能です。利用にあたっては、ACNS対応のAKSクラスターが必要であり、Layer 7ポリシーはHTTP/HTTPSトラフィックに限定される点に注意が必要です。また、Azure Application GatewayやAzure Front Doorとの連携により、エンドツーエンドのトラフィック管理が強化されます。開発・運用チームは、Kubernetesマニフェストでポリシー定義を管理し、CI/CDパイプラインに組み込むことで効率的な運用が可能です。

---

### 6. Generally Available: Azure NetApp Files single file restore from backup 

**公開日時**: 2025年11月20日 18:15:25 UTC
**リンク**: [Generally Available: Azure NetApp Files single file restore from backup ](https://azure.microsoft.com/updates?id=522077)

**アップデートID**: 522077
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure NetApp Files

**要約**:

- 何が更新されたか  
Azure NetApp Filesのバックアップから単一ファイル復元機能がGA（一般提供）となりました。

- 主な変更点や新機能  
ボリューム全体を復元せずに、必要なファイルだけをバックアップから直接復元可能。復元時間とコストを削減できます。

- 影響を受ける対象  
Azure NetApp Filesを利用し、バックアップ運用を行う技術者や運用チーム。

- 注意点があれば記載  
単一ファイル復元はバックアップが有効な環境でのみ利用可能です。復元対象ファイルの整合性確認が必要です。

**詳細**:

Azure NetApp Filesのバックアップから単一ファイルを復元可能となる機能がGA（一般提供）されました。本アップデートは、従来のボリューム単位の復元に比べ、必要なファイルのみを迅速かつ効率的に復元できることを目的としています。これにより、復元時間とコストの大幅な削減が可能です。技術的には、Azure NetApp Filesのバックアップボールト内のスナップショットから対象ファイルを選択し、元のボリュームにマウントせずに直接復元します。実装はAzure PortalやCLI、REST APIを通じて操作でき、細粒度の復元を実現します。活用シナリオとしては、誤削除やファイル破損時の迅速な復旧、特定ファイルのみのリカバリが求められる環境に適しています。注意点としては、復元可能なファイル形式やサイズ制限、バックアップポリシーの適用範囲を事前に確認する必要があります。また、Azure BackupやAzure Monitorと連携することで、バックアップ状態の監視や復元操作の自動化が可能です。本機能により、Azure NetApp Filesの運用効率とデータ保護レベルが向上します。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 7. Generally Available: DNS security policy Threat Intelligence feed

**公開日時**: 2025年11月20日 17:00:13 UTC
**リンク**: [Generally Available: DNS security policy Threat Intelligence feed](https://azure.microsoft.com/updates?id=530183)

**アップデートID**: 530183
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Azure DNS

**要約**:

- 何が更新されたか  
Azure DNSセキュリティポリシーにMicrosoft管理のThreat Intelligenceフィードが一般提供開始。

- 主な変更点や新機能  
既知の悪意あるドメインへのDNSクエリをリアルタイムで検知・ブロックし、攻撃の初動を防止可能に。

- 影響を受ける対象  
Azure DNSを利用するネットワーク環境およびセキュリティ運用担当者。

- 注意点があれば記載  
フィードの有効化により誤検知の可能性があるため、ポリシー設定時は検証を推奨。

**詳細**:

AzureのDNSセキュリティポリシーにおけるThreat Intelligenceフィードが一般提供（GA）されました。本機能はMicrosoftが管理する脅威インテリジェンスデータを活用し、既知の悪意あるドメインへのDNSクエリをリアルタイムで検知・ブロックすることで、初期段階の攻撃を未然に防止します。DNSはほぼ全ての攻撃の起点となるため、DNSレベルでの防御強化が目的です。実装はAzure DNS FirewallのセキュリティポリシーにThreat Intelligenceフィードを組み込む形で行い、管理ポータルやAzure CLIから有効化可能です。これにより、マルウェア通信やフィッシングサイトへのアクセスを自動的に遮断し、セキュリティ運用の負荷軽減と迅速な対応を実現します。活用シナリオとしては、企業内ネットワークのDNSクエリ監視や、クラウド環境でのマルウェア感染拡大防止が挙げられます。注意点として、フィードはMicrosoft管理のためカスタマイズ不可であり、誤検知時の例外設定が必要な場合があります。また、Azure FirewallやAzure Sentinelとの連携により、検知ログの一元管理や高度な分析が可能です。詳細は公式ドキュメントを参照してください。  
https://azure.microsoft.com/updates?id=530183

---

### 8. Generally Available: Azure Sphere OS version 25.10 is now available

**公開日時**: 2025年11月20日 16:00:12 UTC
**リンク**: [Generally Available: Azure Sphere OS version 25.10 is now available](https://azure.microsoft.com/updates?id=522390)

**アップデートID**: 522390
**情報源**: Azure Updates API

**カテゴリ**: Launched, Internet of Things, Azure Sphere

**要約**:

- 何が更新されたか  
Azure Sphere OSのバージョン25.10がRetailフィードで一般提供開始。

- 主な変更点や新機能  
OSのアップデートのみで、SDKの更新は含まれていない。セキュリティや安定性の改善が中心。

- 影響を受ける対象  
インターネット接続されたAzure Sphereデバイスが自動的に最新OSを受信。

- 注意点  
SDKは更新されていないため、開発環境の変更は不要。ネット接続が必須。

**詳細**:

Azure Sphere OSバージョン25.10がRetailフィードにて一般提供開始されました。本アップデートはOSのみに適用され、SDKの更新は含まれていません。Azure Sphere OSはセキュアなIoTデバイス向けの組み込みOSであり、本バージョンではセキュリティ強化や安定性向上が主な目的です。インターネット接続されたデバイスはクラウド経由で自動的に最新OSを受信し、OTA（Over-The-Air）アップデートにより安全かつシームレスに適用されます。具体的な変更点としては、カーネルの脆弱性修正、通信プロトコルの最適化、及びデバイス管理機能の改善が含まれます。これにより、製造業やスマートホームなどのIoT環境での長期的な運用信頼性が向上します。注意点として、SDKが更新されていないため、新機能の開発には別途SDKのアップデートを待つ必要があります。また、ネットワーク接続が不安定な環境ではアップデートの遅延が発生する可能性があります。Azure Sphere OSはAzure IoT HubやAzure Security Centerと連携し、デバイスの状態監視やセキュリティポリシー適用を強化するため、本OSアップデートはこれらサービスの運用効率向上にも寄与します。詳細は公式リンクを参照してください。

---

### 9. Generally Available: Trusted Launch is now supported for Arm64 Marketplace Images 

**公開日時**: 2025年11月20日 15:00:59 UTC
**リンク**: [Generally Available: Trusted Launch is now supported for Arm64 Marketplace Images ](https://azure.microsoft.com/updates?id=529797)

**アップデートID**: 529797
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Virtual Machines

**要約**:

- 何が更新されたか  
Azure MarketplaceでTrusted Launch対応のArm64イメージが一般提供開始。

- 主な変更点や新機能  
Arm64 VMのコスト・性能効率に加え、Trusted Launchによる強化されたセキュリティが利用可能に。

- 影響を受ける対象  
Arm64ベースのVMを利用する開発者や運用者。

- 注意点があれば記載  
Trusted Launchのセキュリティ機能を有効活用するため、対応イメージの選択が必要。

**詳細**:

本アップデートは、Azure MarketplaceでTrusted Launch対応のArm64イメージが一般提供（GA）されたことを発表しています。背景には、Arm64アーキテクチャが提供するコスト効率と高性能を、Trusted Launchの強固なセキュリティ機能と組み合わせるニーズの高まりがあります。Trusted Launchは、セキュアブート、コード整合性検証、仮想TPM（vTPM）を活用し、VMの起動時からランタイムまでのセキュリティを強化します。今回の対応により、Arm64ベースのVMでもこれらのセキュリティ機能が利用可能となり、信頼性の高いクラウド環境構築が可能です。実装はAzure MarketplaceのArm64イメージにTrusted Launchオプションが追加され、ARM64 VM作成時に有効化できます。活用例としては、コスト削減が求められる大規模分散処理やセキュリティ要件の厳しいエッジコンピューティング環境が挙げられます。注意点として、Trusted Launchは一部のカスタムイメージや特定の拡張機能と互換性が制限される場合があり、対応OSやドライバの確認が必要です。関連サービスとしてAzure Security CenterやAzure Policyと連携し、セキュリティポリシーの一元管理やコンプライアンス監視が可能です。詳細は公式リンクを参照してください。

---

### 10. Public Preview: Azure NetApp Files migration assistant (portal support) 

**公開日時**: 2025年11月20日 13:45:47 UTC
**リンク**: [Public Preview: Azure NetApp Files migration assistant (portal support) ](https://azure.microsoft.com/updates?id=525620)

**アップデートID**: 525620
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure NetApp Files

**要約**:

- 何が更新されたか  
Azure NetApp Filesのデータ移行支援ツール「migration assistant」がパブリックプレビューでポータル対応を開始。

- 主な変更点や新機能  
ONTAPのSnapMirrorを利用した効率的かつ低コストなデータレプリケーションによるオンプレやCVO、他クラウドからANFへのシームレス移行が可能に。

- 影響を受ける対象  
Azure NetApp Filesを利用するユーザー、特に既存環境からのデータ移行を検討している技術者。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討し、最新ドキュメントを参照すること。

**詳細**:

本アップデートは、Azure NetApp Files（ANF）へのデータ移行を効率化するため、SnapMirrorを活用した「Azure NetApp Files migration assistant」のポータル対応版をパブリックプレビューとして提供開始したものです。従来はCLIやスクリプトベースでの操作が主流だった移行支援ツールに対し、Azureポータル上でGUI操作が可能となり、操作性と可視性が大幅に向上しました。SnapMirrorはNetApp ONTAPのネイティブなレプリケーション機能であり、オンプレミスやCloud Volumes ONTAP（CVO）、他クラウド環境からANFへデータを高速かつコスト効率良く複製可能です。移行アシスタントはレプリケーションの設定、進捗管理、フェイルオーバー操作をポータル上で一元管理でき、移行作業の自動化とリスク低減に寄与します。活用シナリオとしては、オンプレミスのファイルサーバーやCVO環境からの大容量データ移行、クラウド間のデータ移行、災害復旧環境の構築などが挙げられます。制限事項としては、SnapMirror対応のONTAPバージョン要件やネットワーク帯域の確保が必要であり、移行中のデータ整合性確保に注意が必要です。また、Azure MonitorやAzure Policyと連携することで、移行プロセスの監視やガバナンス強化が可能です。本機能により、ANFへの移行作業がよりシンプルかつ信頼性高く実施できるため、クラウド移行プロジェクトの効率化に貢献します。詳細は公式ドキュメントおよびポータルのヘルプを参照してください。

---

### 11. Public Preview: Azure NetApp Files cache volumes    

**公開日時**: 2025年11月20日 13:45:47 UTC
**リンク**: [Public Preview: Azure NetApp Files cache volumes    ](https://azure.microsoft.com/updates?id=523917)

**アップデートID**: 523917
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure NetApp Files

**要約**:

- 何が更新されたか  
Azure NetApp Filesにキャッシュボリューム機能がパブリックプレビューで提供開始。

- 主な変更点や新機能  
ONTAPのFlexCache技術を活用し、ONTAPベースのストレージ上のデータに対してAzure内で永続的かつ高性能なキャッシュを実現。

- 影響を受ける対象  
Azure NetApp Filesを利用するストレージパフォーマンス向上を求めるエンタープライズユーザーやアプリケーション。

- 注意点  
パブリックプレビュー段階のため、商用利用前に機能の制限やサポート状況を確認する必要あり。

**詳細**:

Azure NetApp Filesのキャッシュボリューム機能がパブリックプレビューで提供開始されました。本機能はNetAppのONTAP FlexCache技術を基盤とし、ONTAPベースのストレージ上のデータに対してAzure内で永続的かつ高性能なキャッシュを実現します。これにより、リモートの主要ストレージからの読み取り遅延を大幅に削減し、アプリケーションの応答性を向上させることが可能です。キャッシュボリュームはONTAPのFlexCacheボリュームとして設定され、元データの変更をリアルタイムに反映しつつローカルアクセスを高速化します。主な活用シナリオは、地理的に分散した拠点間での大容量データ共有や、分析ワークロードの高速化、災害復旧環境での効率的なデータアクセスです。注意点としては、プレビュー段階のためサポート範囲やリージョンが限定されること、キャッシュの整合性管理にONTAPの設定が必要なことが挙げられます。Azure NetApp FilesはAzure Virtual MachinesやAzure Kubernetes Serviceと連携可能で、これらの環境での高速ストレージアクセスを支援します。詳細は公式ドキュメントで最新情報を確認してください。

---

### 12. Public Preview: Azure Monitor for Azure Arc-enabled Kubernetes with OpenShift and Azure Red Hat OpenShift

**公開日時**: 2025年11月20日 08:00:32 UTC
**リンク**: [Public Preview: Azure Monitor for Azure Arc-enabled Kubernetes with OpenShift and Azure Red Hat OpenShift](https://azure.microsoft.com/updates?id=530174)

**アップデートID**: 530174
**情報源**: Azure Updates API

**カテゴリ**: In preview, Hybrid + multicloud, Compute, Containers, DevOps, Management and governance, Azure Arc, Azure Kubernetes Service (AKS), Azure Monitor

**要約**:

- 何が更新されたか  
Azure MonitorがAzure Arc対応のOpenShiftおよびAzure Red Hat OpenShift環境の監視をパブリックプレビューでサポート開始。

- 主な変更点や新機能  
Kubernetesインフラ層とアプリケーションの健全性・パフォーマンスを包括的に監視可能に。

- 影響を受ける対象  
Azure Arc対応のOpenShift環境を運用する技術者やDevOpsチーム。

- 注意点  
パブリックプレビューのため、本番環境での利用は慎重に検討が必要。

**詳細**:

本アップデートは、Azure MonitorがAzure Arc対応のKubernetesクラスター上で稼働するOpenShiftおよびAzure Red Hat OpenShift（ARO）を監視可能にしたことを示す。背景には、オンプレミスやマルチクラウド環境に分散するKubernetes基盤の統合監視ニーズの高まりがある。具体的には、Azure Monitorのコンテナインサイト機能がOpenShiftクラスターに対応し、クラスターヘルス、ノード・ポッドのパフォーマンス、ログ収集、メトリクス分析を一元管理可能となった。技術的には、Azure ArcエージェントをOpenShiftクラスターにデプロイし、Azure Monitorエージェントを介してデータを収集、Azure Monitorワークスペースへ送信する形で実装される。活用例としては、ハイブリッド環境でのOpenShift運用監視や、ARO上のアプリケーションパフォーマンス最適化が挙げられる。注意点としては、Azure Arc対応のOpenShiftクラスターであること、対応バージョンの確認、及びAzure Monitorの設定における権限管理が必要である。関連サービスとしては、Log Analytics、Azure Metrics Explorer、Alerts、Workbooksと連携し、包括的な監視・分析環境を構築可能である。

---


*このレポートは自動生成されました - 2025-11-21 12:03:32 JST*