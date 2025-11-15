# 2025年11月15日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年11月15日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Retirement: Support for Python 3.10 ends on October 1st, 2026

**公開日時**: 2025年11月14日 21:15:14 UTC
**リンク**: [Retirement: Support for Python 3.10 ends on October 1st, 2026](https://azure.microsoft.com/updates?id=509686)

**アップデートID**: 509686
**情報源**: Azure Updates API

**カテゴリ**: Compute, Mobile, Web, App Service, Retirements

**要約**:

- 何が更新されたか  
Python 3.10のサポート終了が2026年10月1日に予定されていることが発表されました。

- 主な変更点や新機能  
同日以降、App Service上のPython 3.10アプリは引き続き動作しますが、セキュリティアップデートやカスタマーサポートは提供されません。

- 影響を受ける対象  
Azure App ServiceでPython 3.10を利用している開発者および運用チーム。

- 注意点  
期限までにPythonのバージョンアップを検討し、セキュリティリスクを回避してください。  

詳細：https://azure.microsoft.com/updates?id=509686

**詳細**:

本アップデートは、Azure App ServiceにおけるPython 3.10の拡張サポート終了（2026年10月1日）を告知するものです。背景には、Pythonコミュニティの公式サポート終了に伴い、Azure側でもセキュリティ更新やカスタマーサポートの提供を停止することで、最新かつ安全なランタイム環境への移行を促進する目的があります。これにより、Python 3.10を利用するApp Service上のアプリは引き続き稼働しますが、セキュリティパッチが提供されず、脆弱性リスクが増大するため、Python 3.11以降へのアップグレードが推奨されます。技術的には、App Serviceのランタイムイメージ更新が停止し、Python 3.10環境は固定されるため、新機能やバグ修正は適用されません。移行時は、requirements.txtやpipenvなどの依存管理ツールを用いてPythonバージョンを指定し、Azure DevOpsやGitHub Actionsを活用したCI/CDパイプラインで検証・デプロイを行うことが効果的です。注意点として、Python 3.10固有のライブラリやフレームワークの互換性を事前に検証し、App Serviceの設定（例えばWEBSITE_PYTHON_VERSION）を更新する必要があります。関連サービスとして、Azure FunctionsやAzure Container AppsでもPythonランタイムのバージョン管理が重要であり、統一的なバージョンアップ計画が求められます。詳細は公式ドキュメント（https://azure.microsoft.com/updates?id=509686）を参照してください。

---

### 2. Retirement: Windows Server 2022 on Azure Kubernetes Service enabled by Azure Arc

**公開日時**: 2025年11月14日 18:00:13 UTC
**リンク**: [Retirement: Windows Server 2022 on Azure Kubernetes Service enabled by Azure Arc](https://azure.microsoft.com/updates?id=499906)

**アップデートID**: 499906
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

- 何が更新されたか  
Windows Server 2022をAzure Arc対応のAzure Kubernetes Service（AKS）上で利用する機能が2026年10月に廃止予定と発表。

- 主な変更点や新機能  
廃止により、Windows Server 2022ベースのAKSクラスターは新規展開やサポートが終了。

- 影響を受ける対象  
Azure Arc経由でWindows Server 2022をAKSで運用しているユーザーや組織。

- 注意点  
廃止までに移行計画を立て、代替のOSバージョンやサービスへの切り替えを検討する必要がある。

**詳細**:

本アップデートは、Azure Arc対応のAzure Kubernetes Service（AKS）上で提供されていたWindows Server 2022コンテナサポートの2026年10月廃止を告知するものです。背景には、Windows Server 2022ベースのAKSクラスターの運用負荷軽減と最新のコンテナ基盤への移行促進があります。具体的には、Azure Arcによりオンプレミスやマルチクラウド環境でAKSを展開可能でしたが、Windows Server 2022ノードのサポート終了に伴い、新規クラスター作成や既存クラスターのアップグレードが停止されます。技術的には、WindowsコンテナのホストOSとしてWindows Server 2022が利用されており、Azure ArcはKubernetes管理プレーンをAzure上で一元管理する仕組みを提供していました。活用シナリオとしては、ハイブリッド環境でWindowsコンテナをAKSで運用するケースが想定されますが、廃止によりWindows Server 2019やLinuxベースのAKSへの移行が推奨されます。注意点として、廃止後はWindows Server 2022ノードのセキュリティアップデートやサポートが受けられなくなるため、早期の移行計画が必要です。関連サービスとしてAzure ArcのKubernetes管理機能、AKSのLinuxコンテナサポート、Azure Monitorによる運用監視が連携しており、これらを活用した運用設計の見直しが求められます。

---

### 3. Public Preview: Pod CIDR expansion in Azure CNI Overlay for AKS

**公開日時**: 2025年11月14日 16:30:37 UTC
**リンク**: [Public Preview: Pod CIDR expansion in Azure CNI Overlay for AKS](https://azure.microsoft.com/updates?id=523086)

**アップデートID**: 523086
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）のAzure CNI Overlayネットワークで、Pod CIDRの拡張機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
既存クラスターのPod CIDRを動的に拡張可能となり、大規模・動的なKubernetesワークロードに対応しやすくなった。

- 影響を受ける対象  
Azure CNI Overlayを利用するAKSクラスターの管理者や運用担当者。

- 注意点があれば記載  
プレビュー機能のため、商用環境での利用は慎重に。事前にドキュメントを確認し、影響範囲を把握すること。

**詳細**:

Azure Kubernetes Service（AKS）におけるAzure CNI OverlayのPod CIDR拡張機能がパブリックプレビューで提供開始されました。背景として、動的かつ大規模なKubernetesワークロードの増加に伴い、既存のPod CIDR割り当てではIPアドレス枯渇やスケール制限が課題となっていました。本機能は、既存クラスターのPod CIDR範囲を動的に拡張可能とし、IPアドレス不足を解消します。技術的には、Azure CNI Overlayネットワークモデルを利用し、追加のCIDRブロックをクラスターネットワークに統合、PodのIP割り当て範囲を拡大します。実装はaz aksコマンドやAzure Portalからの設定変更で対応可能です。活用例として、大規模なマルチテナント環境や急激なスケールアップが必要なサービスに適しています。注意点として、プレビュー段階のため一部リージョン限定や既存ネットワーク構成との互換性確認が必要です。関連サービスではAzure Virtual Networkとの連携が重要で、CIDR拡張時のVNet設定調整が求められます。詳細は公式ドキュメント参照を推奨します。

---

### 4. Public Preview: eBPF host routing in Advanced Container Networking Services (ACNS) for AKS

**公開日時**: 2025年11月14日 16:00:47 UTC
**リンク**: [Public Preview: eBPF host routing in Advanced Container Networking Services (ACNS) for AKS](https://azure.microsoft.com/updates?id=523100)

**アップデートID**: 523100
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**要約**:

- 何が更新されたか  
AKSのAdvanced Container Networking Services (ACNS)でeBPFを用いたホストルーティング機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
eBPFによるホストレベルのルーティングでネットワーク遅延を低減し、スループット向上を実現。従来のネットワーク方式より効率的なパケット処理が可能。

- 影響を受ける対象  
AKS上でACNSを利用するコンテナ化アプリケーションのネットワークパフォーマンスを改善したい技術者や運用者。

- 注意点  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討し、Azureのドキュメントやサポート情報を確認すること。

**詳細**:

本アップデートは、AKSのAdvanced Container Networking Services（ACNS）においてeBPFベースのホストルーティング機能をパブリックプレビューで提供開始したものです。従来のネットワークスタックでは、分散環境下でのコンテナ間通信においてカーネル空間とユーザ空間のコンテキストスイッチが多発し、レイテンシ増大やスループット低下を招いていました。eBPF（extended Berkeley Packet Filter）を活用することで、カーネル内で効率的にパケット処理を行い、ホストレベルでのルーティングを最適化します。これにより、ネットワークパフォーマンスが向上し、大規模なAKSクラスターでのコンテナ通信が高速化されます。実装はAzure CNIの拡張としてeBPFプログラムをホストOSにロードし、パケットのフィルタリング・ルーティングを行う形態です。典型的な活用シナリオは、マイクロサービス間の高頻度通信やマルチノード間の低レイテンシ通信が求められる環境です。現時点ではパブリックプレビューのため、一部のカーネルバージョンやノード構成に制限があり、正式リリース前のフィードバック収集段階です。Azure MonitorやAzure Network Watcherと連携可能で、ネットワークトラフィックの可視化・トラブルシューティングに役立ちます。詳細は公式ドキュメントとプレビューガイドを参照してください。

---


*このレポートは自動生成されました - 2025-11-15 12:01:39 JST*