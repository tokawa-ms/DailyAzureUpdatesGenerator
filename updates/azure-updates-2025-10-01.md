# 2025年10月01日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年10月01日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Public Preview: Soft Delete feature in Azure Compute Gallery

**公開日時**: 2025年09月30日 19:30:35 UTC
**リンク**: [Public Preview: Soft Delete feature in Azure Compute Gallery](https://azure.microsoft.com/updates?id=506886)

**アップデートID**: 506886
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Azure VM Image Builder, Virtual Machine Scale Sets, Virtual Machines, Gallery, Features, Services

**要約**:

- 何が更新されたか  
Azure Compute GalleryにSoft Delete機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
誤って削除したイメージを7日間の保持期間内に復元可能となり、誤削除による影響を軽減します。

- 影響を受ける対象  
Azure Compute Galleryを利用してイメージ管理を行う技術者や運用チーム。

- 注意点があれば記載  
保持期間は7日間であり、それ以降は復元不可のため削除操作には注意が必要です。

**詳細**:

Azure Compute GalleryのSoft Delete機能は、誤って削除したイメージを7日間の保持期間内に復元可能にする機能で、パブリックプレビューとして提供開始されました。背景には、運用ミスによる重要なカスタムイメージの削除リスク軽減と、復旧作業の迅速化が挙げられます。具体的には、削除されたイメージは即時完全削除されずに「ソフト削除」状態となり、AzureポータルやCLI、PowerShellから復元操作が可能です。技術的には、イメージのメタデータとストレージ情報を保持したまま非表示状態にし、保持期間経過後に完全削除される仕組みです。活用シナリオとしては、CI/CDパイプラインでの誤操作防止や、複数環境で共有するイメージの誤削除時の復旧が挙げられます。注意点として、保持期間は固定の7日間で延長不可、保持中のイメージは新規展開不可であること、ストレージコストが発生する点があります。Azure VMやManaged Diskと連携し、Compute Gallery経由でのイメージ管理の信頼性向上に寄与します。詳細は公式ドキュメントを参照してください。

---

### 2. Retirement: Support for Service Connector (preview) on Azure Container Apps will end on March 30th, 2026

**公開日時**: 2025年09月30日 17:30:02 UTC
**リンク**: [Retirement: Support for Service Connector (preview) on Azure Container Apps will end on March 30th, 2026](https://azure.microsoft.com/updates?id=501528)

**アップデートID**: 501528
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

- 何が更新されたか  
Azure Container AppsのService Connector（プレビュー版）のサポート終了が2026年3月30日に決定。

- 主な変更点や新機能  
プレビュー機能のサポートが終了し、以降は利用不可となる。

- 影響を受ける対象  
Azure Container AppsでService Connector（プレビュー）を利用しているユーザー。

- 注意点  
サポート終了後はService Connector（プレビュー）を使った接続が動作しなくなるため、代替手段の検討や移行が必要。  

情報源: https://azure.microsoft.com/updates?id=501528

**詳細**:

本アップデートは、Azure Container Apps上のService Connector（プレビュー版）サポートが2026年3月30日をもって終了することを通知するものです。Service Connectorは、Azure Container Appsから他のAzureサービス（例：Azure SQL、Cosmos DB、Event Hubsなど）への接続設定を簡素化する機能で、プレビュー期間中に利用されてきました。今回のサポート終了により、Azure Portalで作成されたService Connector経由の接続は以降サポートされなくなり、既存の接続は移行や再構築が必要になります。技術的には、Service ConnectorはAzure Resource ManagerテンプレートやマネージドIDを活用し、セキュアな接続情報の自動管理を実現していました。活用シナリオとしては、マイクロサービス間の安全な通信や外部データベース接続の簡易化が挙げられますが、今後は代替手段としてAzure Managed Identityや直接のネットワーク設定、Azure SDKによる接続管理を検討すべきです。注意点として、サポート終了後は接続の自動更新や認証管理が無効となるため、運用影響を最小化するため早期の移行計画が必須です。関連サービスとの連携は引き続き可能ですが、Service Connectorを介さない形での接続設定が求められます。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 3. Retirement: NVv4-series Azure Virtual Machines will be retired on September 30, 2026

**公開日時**: 2025年09月30日 17:15:32 UTC
**リンク**: [Retirement: NVv4-series Azure Virtual Machines will be retired on September 30, 2026](https://azure.microsoft.com/updates?id=500578)

**アップデートID**: 500578
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

- 何が更新されたか  
NVv4シリーズのAzure仮想マシン（Standard_NV4as_v4など）が2026年9月30日に廃止予定。

- 主な変更点や新機能  
該当VMは利用不可となり、新規作成やサポートが終了。

- 影響を受ける対象  
NVv4シリーズを利用中のユーザーやシステム。

- 注意点があれば記載  
廃止前に代替VMへの移行計画を立て、サービス停止を避ける必要がある。

**詳細**:

本アップデートは、NVv4シリーズのAzure仮想マシン（Standard_NV4as_v4～Standard_NV32ahs_v4）が2026年9月30日に退役することを通知するものです。NVv4シリーズはAMD EPYCプロセッサとNVIDIA GPUを組み合わせ、グラフィックス集約型ワークロードや仮想デスクトップ環境に最適化されていました。退役の背景には、より高性能かつ効率的なGPU搭載VMの提供やハードウェアの陳腐化が挙げられます。技術的には、これらVMはGPUリソースを仮想化し、リモートグラフィックス処理を実現していましたが、今後はNVシリーズの後継モデルやNDシリーズなどへの移行が推奨されます。利用シナリオとしては、CAD、3Dレンダリング、AI推論などGPU依存の処理が中心です。注意点として、退役後はこれらVMの作成・再起動が不可となり、移行計画が必須です。また、Azure MonitorやAzure Backupなどのサービスは引き続き利用可能ですが、VMのSKU非対応に伴う制約が発生します。関連サービスとの連携では、Azure Virtual DesktopやNVIDIA GPUドライバの最新対応状況を確認し、移行時の互換性確保が重要です。詳細は公式リンクを参照ください。

---

### 4. Retirement: Spark Native Connector for Semantic Link 

**公開日時**: 2025年09月30日 13:45:49 UTC
**リンク**: [Retirement: Spark Native Connector for Semantic Link ](https://azure.microsoft.com/updates?id=502602)

**アップデートID**: 502602
**情報源**: Azure Updates API

**カテゴリ**: Analytics, Microsoft Fabric, Retirements

**要約**:

- 何が更新されたか  
Spark Native Connector for Semantic Linkが2025年10月1日をもって廃止されることが発表されました。

- 主な変更点や新機能  
使用率の低さと高い保守コスト、セキュリティリスクを理由にサポート終了となります。代替手段の利用が推奨されます。

- 影響を受ける対象  
Semantic LinkのSparkコネクタを利用している開発者や運用チーム。

- 注意点があれば記載  
廃止までに移行計画を立て、他の接続方法への切り替えを検討してください。

**詳細**:

本アップデートは、2025年10月1日をもってSpark Native Connector for Semantic Linkの提供を終了することを発表しています。背景には、利用率の低さ、運用コストの高さ、ならびに潜在的なセキュリティリスクが挙げられています。Spark Native Connectorは、Apache Spark環境からSemantic Linkサービスへネイティブに接続し、高速なデータ連携を実現するためのコンポーネントでした。具体的には、Sparkジョブ内でSemantic Linkのメタデータやリンク情報を直接参照・操作可能とし、データ統合や知識グラフ構築に活用されていました。実装はSparkのDataSource APIを利用し、分散処理環境での効率的なI/Oを実現していました。活用シナリオとしては、大規模データセットの意味的結合やリアルタイム分析が挙げられますが、今後は代替手段としてREST APIやAzure Synapse Analyticsなどのサービス連携を推奨します。注意点として、Connectorの廃止に伴いSparkジョブの修正や移行計画が必要であり、セキュリティ面ではAPIキー管理や認証方式の見直しが求められます。関連サービスではAzure Synapse、Azure Data Factoryとの統合が今後の中心となるため、これらを活用したデータパイプライン設計が推奨されます。

---


*このレポートは自動生成されました - 2025-10-01 12:01:33 JST*