# 2025年09月17日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月17日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 6 件

## 更新一覧

### 1. Generally Available: At-cost data transfer between Azure and an external endpoint

**公開日時**: 2025年09月16日 21:30:32 UTC
**リンク**: [Generally Available: At-cost data transfer between Azure and an external endpoint](https://azure.microsoft.com/updates?id=501915)

**アップデートID**: 501915
**情報源**: Azure Updates API

**カテゴリ**: Launched, Pricing & Offerings, Management

**要約**:

- 何が更新されたか  
Azureと外部エンドポイント間のデータ転送が「実コストベース」で提供開始されました。

- 主な変更点や新機能  
ヨーロッパ地域の顧客およびCSPパートナー向けに、Azureとインターネット経由で外部環境間のデータ転送料金が実コストで適用されます。

- 影響を受ける対象  
AzureユーザーおよびCSPパートナーで、Azure外部とのデータ転送を行う方。

- 注意点  
現時点ではヨーロッパ地域限定の提供であり、他地域への展開状況は今後の発表を確認してください。

**詳細**:

本アップデートは、Azureと外部環境間のデータ転送において、顧客およびCSPパートナーが欧州内でインターネット経由のデータ転送を「実コスト」で利用可能とするものです。従来、Azureのアウトバウンドデータ転送料金は一定のマージンが含まれていましたが、本機能により転送料金が実際の通信コストに近づき、コスト最適化が図れます。技術的には、Azureのネットワーク課金モデルにおいて、対象となるリージョン間のインターネット経由トラフィックを特定し、従量課金を実コストベースで適用します。実装はAzureポータルやAPIを通じて設定可能で、特別なネットワーク構成変更は不要です。活用例としては、オンプレミスや他クラウドとのハイブリッド環境での大量データ移行やバックアップ、CSPによる顧客環境への効率的なデータ配信が挙げられます。注意点としては、現状欧州リージョン限定であること、また転送先がインターネット経由の外部エンドポイントである必要がある点です。関連サービスとしては、Azure ExpressRouteやVPN Gatewayと異なり、インターネット経由の通信に適用されるため、これらのサービスと併用する際は課金体系の違いに留意してください。

---

### 2. Retirement: Azure Kubernetes Service on VMware will be retired on March 16, 2026 - Replace with Azure Kubernetes Service on Azure Local 

**公開日時**: 2025年09月16日 19:45:51 UTC
**リンク**: [Retirement: Azure Kubernetes Service on VMware will be retired on March 16, 2026 - Replace with Azure Kubernetes Service on Azure Local ](https://azure.microsoft.com/updates?id=500294)

**アップデートID**: 500294
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

- 何が更新されたか  
Azure Kubernetes Service on VMware (プレビュー)が2026年3月16日に廃止されることが発表されました。

- 主な変更点や新機能  
廃止に伴い、Azure Kubernetes Service on Azure Localへの移行が推奨されています。

- 影響を受ける対象  
AKS on VMwareを利用しているユーザー。

- 注意点  
2026年3月16日までにAzure Local版への移行を完了する必要があります。早めの移行計画が重要です。

情報源: https://azure.microsoft.com/updates?id=500294

**詳細**:

本アップデートは、Azure Kubernetes Service (AKS) on VMware（プレビュー版）の2026年3月16日をもって提供終了（リタイア）を告知するものです。背景には、オンプレミス環境向けの統合的かつサポート体制の強化を目的とし、より安定した運用が可能なAzure Local環境上のAKSへの移行促進があります。AKS on VMwareはVMware仮想化基盤上でKubernetesクラスターを構築・管理するプレビューサービスでしたが、今後はAzure Localの物理的またはハイブリッド環境でのAKS展開に一本化されます。技術的には、AKS on Azure LocalはAzureの管理プレーンと統合され、より高度な自動化・セキュリティ機能を提供し、オンプレミスやエッジ環境での低遅延運用を実現します。移行にあたっては、既存のVMware上のKubernetesリソースをAzure Localのクラスターに再デプロイし、ネットワーク設定やストレージ構成の調整が必要です。活用シナリオとしては、オンプレミスの厳密なデータ管理要件やエッジコンピューティング環境でのコンテナ運用に適しています。注意点として、プレビュー版のため一部機能が限定的であったこと、移行時のダウンタイムや設定差異に留意が必要です。関連サービスとしては、Azure Arcによるハイブリッド管理、Azure Monitorによる監視、Azure Policyによるガバナンスが連携可能で、包括的な運用管理が可能です。詳細は公式ドキュメントとアップデートページを参照してください。

---

### 3. Generally Available: Azure File Sync in Poland Central and Spain Central

**公開日時**: 2025年09月16日 17:45:04 UTC
**リンク**: [Generally Available: Azure File Sync in Poland Central and Spain Central](https://azure.microsoft.com/updates?id=503421)

**アップデートID**: 503421
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Storage, Cloud Services, Storage Accounts, Features

**要約**:

- 何が更新されたか  
Azure File SyncがPoland CentralおよびSpain Centralリージョンで一般提供（GA）開始。

- 主な変更点や新機能  
オンプレWindowsサーバーのデータをAzure Filesへシームレスに階層化し、ハイブリッド運用や移行を簡素化。オンプレのファイルサーバー性能と互換性を活かせる。

- 影響を受ける対象  
これらリージョンでAzure File Syncを利用する企業や技術者。

- 注意点があれば記載  
既存のAzure File Sync環境と同様にネットワーク帯域や同期ポリシーの最適化が必要。

**詳細**:

本アップデートにより、Azure File Syncがポーランド中央およびスペイン中央リージョンで一般提供（GA）となりました。Azure File SyncはオンプレミスのWindowsサーバーとAzure Files間でファイルデータの階層化（ティアリング）を実現し、ハイブリッド環境でのデータ管理や移行を簡素化します。具体的には、頻繁にアクセスされるファイルはローカルに保持し、アクセス頻度の低いファイルはクラウドに自動的に移動、ストレージ効率とパフォーマンスを最適化します。実装はWindows Server上にAzure File Syncエージェントをインストールし、Azure File Syncサービスと同期グループを構成することで行います。活用例としては、分散拠点のファイルサーバー統合や災害復旧のためのクラウドバックアップ、オンプレミス容量不足の解消が挙げられます。注意点として、ファイルサイズ制限（最大1TB）、サポートされるWindows Serverのバージョン、ネットワーク帯域の確保が必要です。また、Azure Monitorによる同期状態の監視やAzure Backupとの連携でデータ保護を強化可能です。本アップデートにより、ポーランド中央・スペイン中央リージョンのユーザーも低遅延かつ高可用なハイブリッドファイル共有環境を構築でき、地域要件に応じたデータ主権対応が促進されます。

---

### 4. Public Preview: Azure HBv5-series VMs

**公開日時**: 2025年09月16日 17:45:04 UTC
**リンク**: [Public Preview: Azure HBv5-series VMs](https://azure.microsoft.com/updates?id=503129)

**アップデートID**: 503129
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Linux Virtual Machines, Virtual Machines, Windows Virtual Machines, Services

**要約**:

- 何が更新されたか  
Azure HBv5シリーズVMがパブリックプレビューとして南米中部リージョンで利用可能に。

- 主な変更点や新機能  
メモリ帯域幅に最適化されたHPC向けVMで、CFDや自動車・航空宇宙シミュレーション、気象モデリングなどに適する。

- 影響を受ける対象  
高性能計算を行うエンジニアや研究者、HPCワークロードをAzureで実行する技術者。

- 注意点があれば記載  
現時点はプレビュー版のため、商用利用前に性能検証やリージョン対応を確認する必要あり。

**詳細**:

Azure HBv5シリーズVMは、メモリ帯域幅を重視したHPC（高性能計算）用途向けに設計された仮想マシンで、現在Azure South Central USリージョンでパブリックプレビュー提供中です。背景には、流体力学や自動車・航空宇宙シミュレーション、気象モデリングなどメモリ集約型計算の需要増加があり、これらに最適化された高帯域幅メモリと高性能CPU（AMD EPYC 7003シリーズ）を搭載しています。HBv5は最大448GiBのRAMと最大120のCPUコアを提供し、RDMA対応の高速ネットワーク（InfiniBand）を備え、低遅延かつ高スループットのクラスタ構築が可能です。実装にはAzure HPCクラスター管理ツールと連携し、SlurmやAzure CycleCloudなどのジョブスケジューラと統合可能です。活用例としては大規模流体解析や複雑な物理シミュレーションが挙げられ、Azure Blob StorageやAzure NetApp Filesと組み合わせて大容量データの高速入出力を実現します。注意点としては現時点で利用可能リージョンが限定的であり、プレビュー段階のためSLAが正式リリース時と異なる可能性があります。さらに、InfiniBandネットワークを活用するためには対応OSやドライバの適切な設定が必要です。これらの特性を踏まえ、HBv5シリーズはメモリ帯域幅重視のHPCワークロードに最適な選択肢となります。

---

### 5. Generally Available: AKS Automatic 

**公開日時**: 2025年09月16日 17:30:21 UTC
**リンク**: [Generally Available: AKS Automatic ](https://azure.microsoft.com/updates?id=503235)

**アップデートID**: 503235
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSの自動管理機能が一般提供（GA）となりました。

- 主な変更点や新機能  
クラスタの運用負荷を軽減するため、アップグレードやパッチ適用、スケーリングなどの自動化が可能に。セキュリティや信頼性のリスク軽減も支援します。

- 影響を受ける対象  
AKSを利用する開発者・運用チーム。

- 注意点があれば記載  
自動化設定の理解と適切なポリシー設定が必要です。既存環境への影響を事前に検証してください。

**詳細**:

Azure Kubernetes Service (AKS)の「Automatic」機能が一般提供(GA)となりました。本アップデートは、Kubernetes運用の複雑さと学習コストを軽減し、開発チームがクラスタ管理やインフラ調整、セキュリティ・信頼性問題のトラブルシューティングに費やす時間を削減することを目的としています。具体的には、AKSクラスタの自動アップグレード、自動スケーリング、セキュリティパッチ適用などの運用タスクを自動化し、安定稼働を支援します。技術的には、Azure MonitorやAzure Policyと連携し、クラスタ状態の継続的監視とポリシーベースの管理を実現。自動化されたアップデートはノードプール単位で段階的に適用され、ダウンタイムを最小化します。活用シナリオとしては、頻繁なKubernetesバージョンアップ対応が必要な大規模環境や、運用リソースが限られる開発チームに最適です。注意点としては、自動アップデートによる予期せぬ互換性問題やカスタム設定の影響を考慮し、事前にステージング環境で検証することが推奨されます。Azure DevOpsやGitOpsツールとの連携により、CI/CDパイプライン内での運用自動化も強化可能です。詳細は公式ドキュメントを参照ください。

---

### 6. Generally Available: Azure Container Storage v2.0.0 now with NVMe performance boost, open source, and no service fees

**公開日時**: 2025年09月16日 14:30:41 UTC
**リンク**: [Generally Available: Azure Container Storage v2.0.0 now with NVMe performance boost, open source, and no service fees](https://azure.microsoft.com/updates?id=502853)

**アップデートID**: 502853
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Compute, Azure Container Storage, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure Container Storage (ACStor) v2.0.0がGAリリースされました。

- 主な変更点や新機能  
ローカルNVMe対応によりIOPSが最大7倍、レイテンシが4分の1に改善。オープンソース化され、サービス利用料も無料に。

- 影響を受ける対象  
Azure Kubernetes Service（AKS）で高速ストレージを求める開発者・運用者。

- 注意点があれば記載  
既存v1.3.1からの移行時は性能特性の違いを考慮してください。

**詳細**:

Azure Container Storage (ACStor) v2.0.0が一般提供開始されました。本バージョンはローカルNVMeストレージの活用により、前バージョンv1.3.1比で最大7倍のIOPS向上と4分の1のレイテンシ低減を実現し、Azure Kubernetes Service (AKS)向けのストレージとして最高速性能を提供します。オープンソース化によりカスタマイズや拡張が容易となり、サービス利用料が不要となったため、コスト効率も向上しています。技術的には、NVMeデバイスを直接マウントし、コンテナ内から低レイテンシかつ高スループットでアクセス可能なストレージ層を構築。これにより、ステートフルなコンテナアプリケーションのI/O性能が大幅に改善されます。主な活用シナリオは、高負荷のデータベース、リアルタイム分析、キャッシュ層など、低遅延・高IOPSを必要とするワークロードです。注意点としては、NVMe対応のノードが必要であり、リージョンやSKUによる対応状況を事前確認する必要があります。AKSとの連携が強化されており、Kubernetes CSIドライバーを通じてシームレスにストレージをプロビジョニング可能です。詳細は公式ドキュメントおよびGitHubリポジトリを参照してください。

---


*このレポートは自動生成されました - 2025-09-17 12:01:54 JST*