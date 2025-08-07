# 2025年08月07日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年08月07日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 20 件

## 更新一覧

### 1. Generally Available: Azure Data Box Next Gen is now generally available in additional regions

**公開日時**: 2025年08月06日 16:00:45 UTC
**リンク**: [Generally Available: Azure Data Box Next Gen is now generally available in additional regions](https://azure.microsoft.com/updates?id=499945)

**アップデートID**: 499945
**情報源**: Azure Updates API

**カテゴリ**: Launched, Migration, Storage, Azure Data Box, Features

**要約**:

- 何が更新されたか  
Azure Data Box Next Genが新たにオーストラリア、日本、シンガポール、ブラジル、香港、UAE、スイス、ノルウェーで一般提供（GA）開始。

- 主な変更点や新機能  
120TBおよび525TBモデルの両方がこれらの地域で利用可能に。

- 影響を受ける対象  
大容量データのオフライン転送を必要とする企業や技術者。

- 注意点があれば記載  
地域拡大によりデータ移行計画の柔軟性が向上。利用前に対応リージョンを確認すること。

**詳細**:

本アップデートは、Azure Data Box Next Genの提供地域拡大を目的とし、オーストラリア、日本、シンガポール、ブラジル、香港、UAE、スイス、ノルウェーで一般提供（GA）を開始しました。これにより、120TBおよび525TBの2種類の大容量データ転送デバイスが複数リージョンで利用可能となり、オンプレミスからAzureへの大規模データ移行を高速かつ安全に実現します。Data Box Next Genは耐久性の高いハードウェアとAES 256ビット暗号化を備え、ネットワーク帯域に依存しない物理転送を可能にします。利用者はAzureポータルから注文し、デバイス到着後にデータをローカルに書き込み、返送することでAzure Blob StorageやData Lake Storage Gen2へ直接アップロードされます。主な活用シナリオは、ネットワーク制約下での大容量データ移行、災害復旧データの迅速なバックアップ、マルチリージョン間のデータ集約です。注意点としては、デバイスの輸送期間や地域ごとの輸送制限、データ消去ポリシーの遵守が必要です。また、Azure Data Box GatewayやAzure Storage Explorerとの連携により、ハイブリッド環境でのデータ管理が効率化されます。今回のリージョン拡大により、グローバルなデータ移行戦略の柔軟性が向上しました。

---

### 2. Public Preview: Azure Storage Discovery

**公開日時**: 2025年08月06日 15:00:18 UTC
**リンク**: [Public Preview: Azure Storage Discovery](https://azure.microsoft.com/updates?id=499143)

**アップデートID**: 499143
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Storage Accounts, Features, Management, Services

**要約**:

- 何が更新されたか  
Azure Storage Discoveryがパブリックプレビューで提供開始。

- 主な変更点や新機能  
エンタープライズ全体のAzure Storageデータ資産を可視化し、容量使用状況やアクティビティを詳細分析可能。コスト最適化やセキュリティ強化に役立つインサイトを提供。

- 影響を受ける対象  
Azure Storageを大規模に利用する企業や運用チーム。

- 注意点があれば記載  
プレビュー機能のため、商用利用前に機能制限や変更の可能性を確認すること。

**詳細**:

Azure Storage Discoveryは、企業全体のAzureストレージ資産を一元的に可視化し、従来得られなかった詳細な容量利用状況やアクセスアクティビティの分析を可能にするパブリックプレビュー機能です。これにより、ストレージコストの最適化、セキュリティ強化、運用効率の向上を実現します。主な機能は、ストレージアカウント単位での使用容量の詳細把握、アクセス頻度やパターンの分析、異常検知のためのセキュリティインサイト提供です。技術的には、Azure MonitorやAzure Resource Graphと連携し、ストレージメタデータとログを集約・解析する仕組みを持ちます。活用例としては、未使用データの特定によるコスト削減、アクセス権限の見直しによるセキュリティ強化、運用チームによる容量計画の精緻化が挙げられます。注意点としては、プレビュー段階のため一部機能が限定的であり、対応リージョンやストレージタイプに制約がある可能性があります。Azure Security CenterやAzure Cost Managementとの連携により、より包括的な管理が可能です。詳細は公式リンクを参照してください。

---

### 3. Generally Available: AKS support for Advanced Container Networking: L7 Policies

**公開日時**: 2025年08月06日 04:00:09 UTC
**リンク**: [Generally Available: AKS support for Advanced Container Networking: L7 Policies](https://azure.microsoft.com/updates?id=499274)

**アップデートID**: 499274
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSのAdvanced Container Networking ServicesとCiliumクラスターでL7（アプリケーション層）ネットワークポリシーがGA対応。

- 主な変更点や新機能  
アプリケーション層の属性に基づく細かなトラフィック制御が可能となり、セキュリティルールをより詳細に設定できる。

- 影響を受ける対象  
AKSでAdvanced Container NetworkingとCiliumを利用するユーザー。

- 注意点  
L7ポリシーの適用には対応クラスターの設定が必要で、既存のネットワーク構成との整合性を確認すること。

**詳細**:

本アップデートにより、Azure Kubernetes Service（AKS）はAdvanced Container Networking Services（ACNS）およびCiliumベースのクラスターにおいて、Layer 7（L7）ネットワークポリシーのサポートを一般提供（GA）しました。これにより、従来のL3/L4レベルの通信制御に加え、HTTPやgRPCなどのアプリケーション層属性に基づく細粒度なトラフィック制御が可能となります。具体的には、URIパス、HTTPメソッド、ヘッダー情報などを条件にしたアクセス制御ルールを定義でき、マイクロサービス間の通信セキュリティ強化やコンプライアンス対応が容易になります。実装はCiliumのeBPF技術を活用し、カーネルレベルでの高速かつ効率的なパケット処理を実現。ポリシーはKubernetesのCustomResourceDefinition（CRD）を通じて管理し、既存のKubernetesネットワークポリシーと連携可能です。活用例としては、APIゲートウェイの前段での細かなアクセス制御や、サービスメッシュを用いたトラフィック分離が挙げられます。一方、L7ポリシーはACNS+Cilium環境限定であり、他のネットワークプラグインでは非対応、また複雑なポリシー設定はパフォーマンスに影響を与える可能性があるため注意が必要です。Azure MonitorやAzure Policyとの連携により、ポリシー適用状況の可視化やガバナンス強化も可能です。詳細は公式ドキュメントを参照してください。

---

### 4. Private Preview: Agentic experience for AKS in the Azure CLI

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Private Preview: Agentic experience for AKS in the Azure CLI](https://azure.microsoft.com/updates?id=499377)

**アップデートID**: 499377
**情報源**: Azure Updates API

**カテゴリ**: In development, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure CLIに「az aks agent」コマンドがプライベートプレビューで追加され、AKS操作にAIエージェント機能が導入された。

- 主な変更点や新機能  
エージェントベースのAI推論により、AKSクラスター管理やトラブルシューティングをCLI上で効率化可能。

- 影響を受ける対象  
AKSを利用する開発者・運用者で、CLIからの高度な操作を求める技術者。

- 注意点があれば記載  
現時点はプライベートプレビューのため、利用には申請が必要で機能が限定的。

**詳細**:

Azure Kubernetes Service（AKS）における新たなエージェントAI駆動のCLI体験「az aks agent」がプライベートプレビューとして導入されました。本アップデートは、従来の手動操作に加え、エージェント的推論を活用して開発者や運用者の作業効率を向上させることを目的としています。具体的には、Azure CLI内でAIがコンテキストを理解し、複雑なクラスター管理タスクを自動化・支援します。技術的には、AIモデルがユーザーのコマンドや環境情報を解析し、最適な操作手順を提案・実行する仕組みで、CLIの「az aks agent」コマンドを通じて利用可能です。活用シナリオとしては、クラスターのスケーリング、トラブルシューティング、設定最適化などが挙げられ、特に運用自動化や迅速な問題解決に効果的です。注意点としては、現時点でプライベートプレビュー段階のため利用には申請が必要であり、AI推論の結果は必ずしも完璧ではないため人間の監督が推奨されます。また、Azure MonitorやAzure Policyなどの既存サービスと連携し、より高度な運用管理を実現可能です。本機能はAKS運用の効率化と高度化を目指す技術者にとって有用なツールとなります。

---

### 5. Public Preview: Managed Namespaces in AKS

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: Managed Namespaces in AKS](https://azure.microsoft.com/updates?id=499371)

**アップデートID**: 499371
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSでManaged Namespaces機能がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
サブスクリプション、リソースグループ、クラスター単位でアクセス可能な名前空間一覧を取得可能。該当名前空間へのデプロイ権限を持つ認証情報も取得できる。

- 影響を受ける対象  
AKSを利用し、複数名前空間の管理やアクセス制御を行う開発者・運用者。

- 注意点があれば記載  
プレビュー機能のため、本番環境での利用は慎重に。権限管理の設計に注意が必要。

**詳細**:

本アップデートは、AKS（Azure Kubernetes Service）におけるマネージドネームスペース機能のパブリックプレビュー提供開始を示します。従来、AKSクラスター内のネームスペース管理は個別に権限設定が必要で、スケールや運用負荷が課題でした。今回の機能は、サブスクリプション、リソースグループ、クラスター単位でユーザーがアクセス可能なネームスペース一覧を取得し、対応するデプロイ権限付きの認証情報を一元的に取得可能にします。これにより、複数ネームスペースへのアクセス管理とデプロイ作業の効率化が図れます。

技術的には、Azure RBACと統合し、ユーザーのアクセス許可に基づくネームスペースの列挙と、Kubernetesのkubeconfig生成を自動化します。APIやCLIを通じて対象ネームスペースの認証情報を取得し、kubectl等での操作を容易にします。実装にはAzure AD認証とAKSのネームスペース権限管理が連携し、セキュアなアクセス制御を実現しています。

活用例としては、マルチテナント環境での開発チームごとのネームスペース分離運用、CI/CDパイプラインでの権限管理自動化、複数クラスターに跨る一元的なアクセス管理が挙げられます。注意点としては、現時点でプレビュー機能のため、全てのリージョンで利用可能ではない点や、権限設定ミスによるアクセス漏れリスクに留意が必要です。

関連サービスとしては、Azure ADによる認証管理、Azure RBACによる権限付与、Azure CLIおよびAzure Portalでの操作サポートが挙げられ、これらと連携してセキュアかつ効率的なネームスペース管理を実現します。

---

### 6. Generally Available: AKS Security Dashboard

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Generally Available: AKS Security Dashboard](https://azure.microsoft.com/updates?id=499366)

**アップデートID**: 499366
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKS Security Dashboardが一般提供（GA）開始。

- 主な変更点や新機能  
Azureポータル上でAKSクラスターのセキュリティ状況を一元管理可能。ソフトウェア脆弱性、重大なセキュリティ問題、コンプライアンス違反、実行時の脅威を可視化。

- 影響を受ける対象  
AKSを利用するクラウド運用・セキュリティ担当者。

- 注意点  
ダッシュボード活用にはAzure Security Centerとの連携が必要。

**詳細**:

Azure Kubernetes Service（AKS）における「AKS Security Dashboard」の一般提供開始は、クラスタのセキュリティ管理を一元化し、運用負荷軽減と迅速な脅威対応を目的としています。本ダッシュボードはAzure Portal上で利用可能で、クラスタ内のソフトウェア脆弱性、重要なセキュリティ問題、コンプライアンス違反、実行時の脅威を可視化します。具体的には、Kubernetesノードやコンテナイメージの脆弱性スキャン結果、ネットワークポリシー違反、異常なプロセス検出などを統合表示し、問題の優先順位付けを支援します。技術的にはAzure Defender for Kubernetesのデータを基に、Azure MonitorおよびLog Analyticsと連携してリアルタイムのセキュリティ情報を収集・分析し、ダッシュボードに反映します。活用例としては、DevOpsチームがCI/CDパイプラインに組み込み、脆弱性修正やポリシー適用の迅速化が可能です。注意点としては、Azure Defenderの有効化が前提であり、追加コストが発生する点や、現状はAKSに限定されていることが挙げられます。関連サービスとしてAzure Security Center、Azure Monitor、Azure Policyと密接に連携し、包括的なセキュリティ管理を実現します。

---

### 7. Public Preview: Azure Virtual Network Verifier for AKS (VNV) for AKS

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: Azure Virtual Network Verifier for AKS (VNV) for AKS](https://azure.microsoft.com/updates?id=499361)

**アップデートID**: 499361
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure Virtual Network Verifier for AKS (VNV) がパブリックプレビューとしてAzureポータルで利用可能に。

- 主な変更点や新機能  
AKSクラスターのアウトバウンド接続問題を検出・トラブルシュートできるツールを提供。

- 影響を受ける対象  
AKSを利用する開発者・運用者。

- 注意点があれば記載  
プレビュー版のため、本番環境での利用は慎重に検討すること。

**詳細**:

本アップデートは、AKS（Azure Kubernetes Service）クラスターのアウトバウンド接続問題を迅速に検出・トラブルシュートするためのツール「Azure Virtual Network Verifier for AKS（VNV）」のパブリックプレビュー提供開始を示すものです。VNVはAzureポータルから利用可能で、AKSの仮想ネットワーク設定に起因する通信障害を自動的に診断します。具体的には、ネットワークセキュリティグループ（NSG）、ルートテーブル、ユーザーデファインドルート（UDR）などの設定を検証し、アウトバウンド通信経路の問題点を特定。診断結果は視覚的に表示され、問題箇所の詳細なログも取得可能です。技術的には、VNVはAKSクラスターのネットワーク構成情報を収集し、仮想ネットワーク内のパケットフローをシミュレーションすることで問題を検出します。活用シナリオとしては、外部APIやサービスへの接続障害発生時の原因調査や、ネットワーク設定変更後の検証が挙げられます。制限事項として、現時点で対応するAKSバージョンやリージョンに制限がある可能性があり、プレビュー機能のため本番環境での使用は慎重を要します。なお、Azure MonitorやNetwork Watcherと連携することで、より詳細なログ収集や監視が可能となり、包括的なネットワーク運用管理に寄与します。

---

### 8. Public Preview: Multiple Standard Load Balancers support in AKS

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: Multiple Standard Load Balancers support in AKS](https://azure.microsoft.com/updates?id=499356)

**アップデートID**: 499356
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSで複数のStandard Load Balancer（SLB）をクラスタ単位で利用可能に（パブリックプレビュー）。

- 主な変更点や新機能  
ノードNICあたりの300インバウンドルール制限を超えてスケール可能。異なるエージェントプールに別々のSLBを割り当ててトラフィックを分離可能。

- 影響を受ける対象  
大規模なAKSクラスタや複数のワークロードを分離したいユーザー。

- 注意点  
パブリックプレビューのため、本番環境での利用は慎重に。設定や運用に追加の考慮が必要。

**詳細**:

本アップデートは、AKSクラスターにおけるStandard Load Balancer（SLB）のインバウンドルール数制限（300ルール/ノードNIC）を超えてスケール可能にするため、複数SLBの利用をパブリックプレビューでサポート開始したものです。これにより、異なるエージェントプールに別々のSLBを割り当てることでトラフィックの分離が可能となり、大規模かつ複雑なネットワーク構成に対応できます。実装は、各エージェントプールに対し個別のStandard Load Balancerを関連付け、サービスのLoadBalancerタイプで特定のSLBを指定する形で行います。活用例としては、マルチテナント環境や異なるアプリケーションのトラフィック分離、または大規模なマイクロサービス群の負荷分散が挙げられます。注意点として、複数SLBの管理コスト増加やIPアドレス管理の複雑化があり、プレビュー段階のため一部機能制限やサポート範囲の確認が必要です。関連サービスでは、Azure MonitorによるSLBのヘルス監視やAzure Firewallとの組み合わせによるセキュリティ強化が推奨されます。詳細は公式ドキュメントを参照してください。

---

### 9. Generally Available: Static egress gateway public prefix support in AKS 

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Generally Available: Static egress gateway public prefix support in AKS ](https://azure.microsoft.com/updates?id=499351)

**アップデートID**: 499351
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSで静的なパブリックIPプレフィックスを使用した出口ゲートウェイ機能がGA（一般提供）となりました。

- 主な変更点や新機能  
専用のゲートウェイノードプールを作成し、特定のPodのアウトバウンド通信を/28～/31の静的パブリックIPプレフィックス経由でルーティング可能に。

- 影響を受ける対象  
AKSでアウトバウンド通信のIP固定化やセキュリティ要件を持つ開発者・運用者。

- 注意点  
IPプレフィックスのサイズ制限とノードプールの管理が必要です。

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）におけるアウトバウンドトラフィックのIPアドレス管理を強化するために導入されました。従来、AKSのアウトバウンド通信は動的に割り当てられたパブリックIPを経由していたため、IPアドレスの固定化が困難であり、ファイアウォールやネットワークポリシーの管理に課題がありました。今回の「Static egress gateway public prefix」機能のGAにより、専用のゲートウェイノードプールを作成し、注釈付きのPodからのアウトバウンドトラフィックを静的なパブリックIPプレフィックス（/28～/31）経由でルーティング可能となりました。

技術的には、専用ノードプールに割り当てられた静的パブリックIPプレフィックスを持つNATゲートウェイを構成し、Podに特定のアノテーションを付与することで、そのPodのアウトバウンド通信を該当ゲートウェイ経由に強制します。これにより、IPアドレスの固定化とトラフィックの分離が実現し、セキュリティポリシーの適用やトラフィック監視が容易になります。

活用シナリオとしては、外部サービスへのアクセス制御が厳格な環境でのIPホワイトリスト管理、複数のアプリケーションが混在するクラスターでのトラフィック分離、及びコンプライアンス要件に対応したネットワーク設計が挙げられます。

注意点として、静的IPプレフィックスのサイズは/28から/31までであり、割り当て可能なIP数に制限があるため、トラフィック量やPod数に応じた適切なプレフィックス選定が必要です。また、ゲートウェイノードプールの管理とスケーリングはユーザー側の責任となります。

関連サービスとしては、Azure NAT Gateway、Azure Virtual Network、及びAzure Firewallとの連携が考えられ、これらを組み合わせることで高度なネットワークセキュリティとトラフィック管理が可能です。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 10. Public Preview: Increase ingestion quota for Azure Managed Prometheus with an ARM API 

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: Increase ingestion quota for Azure Managed Prometheus with an ARM API ](https://azure.microsoft.com/updates?id=499346)

**アップデートID**: 499346
**情報源**: Azure Updates API

**カテゴリ**: In preview, DevOps, Management and governance, Azure Monitor, Features

**要約**:

- 何が更新されたか  
Azure Managed Prometheusのメトリクス取り込みクォータをARM API経由で増加申請可能に（パブリックプレビュー）。

- 主な変更点や新機能  
Azure Monitorワークスペースのデフォルト取り込み制限をAPIで柔軟に引き上げられるようになった。

- 影響を受ける対象  
Azure Managed Prometheusを利用し、大量メトリクスを監視している技術者や運用チーム。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に。API利用には適切な権限が必要。

**詳細**:

本アップデートは、Azure MonitorのManaged Prometheusにおけるメトリクスの取り込み（ingestion）上限をAPI経由で柔軟に引き上げ可能にするものです。従来、Azure Monitorワークスペースにはデフォルトの取り込みクォータが設定されており、大規模なPrometheusメトリクスの監視環境では制限によりデータ損失や監視遅延が発生するケースがありました。今回のPublic Previewでは、Azure Resource Manager（ARM）APIを用いて、Managed Prometheusの取り込みクォータ増加をリクエストできる機能が追加され、運用の柔軟性とスケーラビリティが向上します。

具体的には、ARM APIのエンドポイントに対してJSON形式で増加リクエストを送信し、審査を経てワークスペースの取り込み容量が拡張されます。これにより、CLIやIaCツールからプログラム的にクォータ管理が可能となり、自動化運用や大規模環境でのスムーズなスケールアップが実現します。実装時はAzure MonitorワークスペースのリソースIDを指定し、適切な権限（例：Contributor以上）が必要です。

活用シナリオとしては、大量のPrometheusメトリクスを収集するマイクロサービス群やIoTデバイス群の監視、またはピーク時の一時的な取り込み増加要求に対応可能です。注意点として、クォータ増加は即時反映ではなく審査プロセスを含むため、事前計画が重要です。また、増加上限には物理的な制約が存在し、無制限ではありません。関連サービスとしてAzure Monitor LogsやAzure Metricsと連携し、統合的な監視基盤構築が推奨されます。

---

### 11. Public Preview: LocalDNS for AKS

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: LocalDNS for AKS](https://azure.microsoft.com/updates?id=499341)

**アップデートID**: 499341
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure Kubernetes Service (AKS)において、LocalDNS機能がパブリックプレビューで利用可能になりました。

- 主な変更点や新機能  
各ノードにDNSプロキシを配置し、大規模クラスターでのDNSボトルネックを解消。DNSクエリのレイテンシを低減し、信頼性を向上させます。

- 影響を受ける対象  
大規模またはDNS負荷の高いAKSクラスターの運用者。

- 注意点  
プレビュー機能のため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure Kubernetes Service (AKS)のPublic Previewとして提供開始されたLocalDNSは、大規模クラスターにおけるDNS解決のパフォーマンス向上を目的とした機能です。従来、AKSではDNSクエリが集中し、特に大規模ノード数でレイテンシや信頼性の問題が発生していました。LocalDNSは各ノード上にDNSプロキシを配置し、ノード内でDNSキャッシュと解決を行うことで、クエリのボトルネックを解消し、応答時間を短縮します。

技術的には、LocalDNSはCoreDNSのプロキシとして動作し、ノードローカルにDNSキャッシュを保持。これによりDNSクエリがノード外のDNSサーバーに頻繁に到達することを防ぎ、ネットワーク負荷と遅延を低減します。実装はAKSのアドオンとして有効化可能で、既存のCoreDNS設定を変更せずに導入できます。

活用シナリオとしては、大規模なAKSクラスターでのマイクロサービス間通信や外部サービスへの名前解決が多発する環境で効果的です。特に、DNS解決の遅延がアプリケーション性能に影響を与えるケースで有用です。

注意点としては、現時点でプレビュー版のため、全てのリージョンやクラスター構成での動作保証がないこと、またLocalDNSのキャッシュによる名前解決の一時的な遅延反映が発生する可能性があります。アップデート適用前に十分な検証が推奨されます。

Azureの他サービスでは、Azure Monitorと連携しDNSクエリのパフォーマンス監視が可能であり、Azure PolicyでLocalDNSの有効化管理も行えます。これにより運用管理の効率化と安定稼働が期待されます。

---

### 12. Public Preview : Azure Bastion integration with AKS

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview : Azure Bastion integration with AKS](https://azure.microsoft.com/updates?id=499335)

**アップデートID**: 499335
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure BastionがAKS（Azure Kubernetes Service）と統合され、パブリックプレビューとして提供開始。

- 主な変更点や新機能  
Bastion経由でプライベートAKSクラスターへ継続的かつ安全にアクセス可能に。APIサーバーの許可IP範囲設定があるパブリックAKSクラスターにも対応。

- 影響を受ける対象  
AKSを利用する開発者・運用者で、セキュアなクラスターアクセスを求めるユーザー。

- 注意点  
プレビュー機能のため、商用環境での利用は慎重に。今後のアップデートに注意。

**詳細**:

本アップデートは、Azure BastionとAzure Kubernetes Service（AKS）の統合をパブリックプレビューで提供開始したものです。背景には、プライベートAKSクラスターへの安全かつ継続的なアクセスニーズの高まりがあり、従来のVPNやJumpboxに依存しないシームレスな接続を実現することが目的です。主な機能として、Azure Bastion経由でプライベートAKSクラスターのAPIサーバーに直接安全アクセス可能となり、さらにAPIサーバーの許可IP範囲設定があるパブリックAKSクラスターにも対応します。技術的には、Azure BastionがAKSのAPIサーバーのプライベートエンドポイントに中継接続を行い、TLSトンネルを介して管理トラフィックを保護します。実装はAzureポータルやCLIでBastionのAKS統合を有効化するだけで、追加のネットワーク構成やVPN設定は不要です。活用例としては、開発・運用チームがインターネット経由で安全にAKS管理を行うケースや、セキュリティポリシーでVPN利用が制限される環境での利用が挙げられます。注意点としては、現時点でプレビュー機能であるため、商用環境での利用は慎重に検討し、Bastionのサブネット要件やAKSのバージョン互換性を確認する必要があります。関連サービスとしては、Azure Active Directory連携による認証強化やAzure Monitorによるアクセスログ監査と組み合わせることで、より堅牢な運用が可能です。

---

### 13. Public Preview: AKS Model Context Protocol (MCP) server

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: AKS Model Context Protocol (MCP) server](https://azure.microsoft.com/updates?id=499326)

**アップデートID**: 499326
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKS向けのModel Context Protocol (MCP)サーバーがパブリックプレビューとしてオープンソースで公開されました。

- 主な変更点や新機能  
AIエージェントがAKSクラスターと連携可能な標準化されたインターフェースを提供し、クラスター管理を簡素化します。

- 影響を受ける対象  
AKSを利用し、AIエージェントや自動化ツールでクラスター管理を行う技術者。

- 注意点があれば記載  
現時点はプレビュー版のため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure Kubernetes Service (AKS)向けのModel Context Protocol (MCP)サーバーがパブリックプレビューとしてオープンソースで公開されました。本アップデートは、AIエージェントとAKSクラスター間の相互作用を標準化し、クラスター管理の自動化と効率化を目的としています。MCPサーバーは、AIモデルがクラスターの状態やリソース情報を取得・操作するための共通プロトコルを提供し、複雑なAPI呼び出しを抽象化します。技術的には、gRPCベースの通信を用い、拡張性の高いAPI設計によりカスタムリソースとの連携も可能です。活用例としては、AIによるクラスターの自動スケーリング、異常検知、運用タスクの自動化などが挙げられます。現時点ではプレビュー版のため、APIの安定性や機能追加に制限があり、運用環境での利用には注意が必要です。Azure MonitorやAzure Arcとの連携により、監視やハイブリッド環境管理との統合も期待できます。詳細は公式ドキュメントを参照してください。

---

### 14. Generally Available: Control Plane Improvements in AKS

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Generally Available: Control Plane Improvements in AKS](https://azure.microsoft.com/updates?id=499313)

**アップデートID**: 499313
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSのAPIサーバーの制御プレーンが強化され、リスト応答のストリーミングエンコーディングが一般提供開始。

- 主な変更点や新機能  
KEP 5116に基づき、大規模なLIST APIコール時のメモリ使用量を約10倍削減し、APIサーバーの耐障害性と効率が向上。

- 影響を受ける対象  
AKSを利用する開発者および運用チームで、大量リソース取得を行う環境。

- 注意点  
既存のAPI動作に大きな影響はないが、大規模環境でのパフォーマンス改善効果を確認可能。  

詳細：https://azure.microsoft.com/updates?id=499313

**詳細**:

本アップデートは、AKSのAPIサーバーの耐障害性向上を目的に、Kubernetes Enhancement Proposal (KEP) 5116「LISTレスポンスのストリーミングエンコーディング」を実装したものです。従来のLIST API呼び出しは大量データ取得時にAPIサーバーのメモリ使用量が増大し、パフォーマンス低下や障害リスクがありました。本改善により、LISTレスポンスを逐次的にエンコード・送信するストリーミング方式を採用し、メモリ使用量を約10分の1に削減します。これにより、大規模クラスターでのAPI応答性能が向上し、安定性が増します。実装はAPIサーバーのレスポンス処理層に組み込まれ、既存のクライアントは透過的に恩恵を受けられます。活用シナリオとしては、大量Podやリソースを管理する運用監視ツールやCI/CDパイプラインが挙げられます。注意点として、ストリーミング対応クライアントでない場合、互換性問題は発生しませんが、レスポンス処理の最適化は限定的です。AKSの他Azure MonitorやAzure Policyと連携し、大規模環境の安定運用に寄与します。詳細は公式リンク参照ください。

---

### 15. Public Preview: Web Application Firewall on Application Gateway for Containers 

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: Web Application Firewall on Application Gateway for Containers ](https://azure.microsoft.com/updates?id=499308)

**アップデートID**: 499308
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Application Gateway for ContainersでWeb Application Firewall（WAF）ポリシーがパブリックプレビュー対応。

- 主な変更点や新機能  
WAFのデフォルトルールセットを利用し、AKS上のコンテナワークロードを悪意ある攻撃から保護可能に。

- 影響を受ける対象  
AKS管理者および開発者で、コンテナ環境のセキュリティ強化を図るユーザー。

- 注意点があれば記載  
パブリックプレビューのため、本番環境での利用は慎重に検討し、最新のドキュメントを参照すること。

**詳細**:

本アップデートは、Azure Application Gateway for ContainersにWeb Application Firewall（WAF）ポリシーのサポートをパブリックプレビューとして追加したものです。背景には、AKS環境で稼働するコンテナ化アプリケーションのセキュリティ強化ニーズがあり、WAFの既存のDefault Rulesetを活用することで、SQLインジェクションやクロスサイトスクリプティングなどの一般的な攻撃から保護可能となります。技術的には、Application Gateway for ContainersにWAF機能を統合し、Ingressトラフィックを監視・検査する仕組みで、AKSクラスターのIngressコントローラーとして設定可能です。実装はAzure CLIやARMテンプレートでWAFポリシーを適用し、Application Gatewayの設定に組み込む形で行います。活用シナリオとしては、マイクロサービス構成のAKS上に展開したWebアプリケーションのセキュリティ強化が挙げられ、DevOpsパイプラインに組み込むことで自動化も可能です。注意点としては、パブリックプレビュー段階のためSLAsが適用されず、機能変更や制限が今後発生する可能性がある点、またWAFルールのチューニングが必要な場合があることに留意が必要です。関連サービスとしては、Azure Monitorによるログ収集、Azure Security Centerとの連携でセキュリティインシデントの可視化が可能です。詳細は公式ドキュメントとアップデートページを参照してください。

---

### 16. Generally Available: Deployment safeguards in AKS

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Generally Available: Deployment safeguards in AKS](https://azure.microsoft.com/updates?id=499299)

**アップデートID**: 499299
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure Kubernetes Service (AKS)でデプロイメントセーフガード機能が一般提供（GA）となりました。

- 主な変更点や新機能  
Kubernetesのベストプラクティスを強制し、設定ミスやデプロイ時の問題を未然に防止する仕組みを提供します。

- 影響を受ける対象  
AKSを利用する開発者・運用者で、安定したKubernetes環境構築を目指す技術者。

- 注意点があれば記載  
既存のデプロイメントに影響を与える可能性があるため、導入前に設定内容の確認が推奨されます。

**詳細**:

Azure Kubernetes Service (AKS)の「Deployment safeguards」機能がGA（一般提供）となりました。本機能は、Kubernetes開発時の設定ミスによるバグやデプロイ失敗を防止するため、ベストプラクティスの自動適用を目的としています。具体的には、Podセキュリティポリシーやリソース制限、ラベル付けなどのポリシーを事前に検証・強制し、誤った設定を検出・ブロックします。技術的には、Admission Controllerを活用し、デプロイ時にポリシー違反をリアルタイムで検知・拒否する仕組みです。これにより、CI/CDパイプライン内での品質担保が容易となり、運用コスト削減と安定稼働に寄与します。活用例としては、複数チームが共有するAKSクラスターでの一貫したセキュリティ基準維持や、リソース過剰消費防止が挙げられます。注意点としては、既存のカスタムAdmission Controllerとの競合や、ポリシー適用範囲の限定があるため事前検証が必要です。Azure PolicyやAzure Monitorと連携することで、ポリシー違反の監視・レポートも可能となり、包括的なガバナンス体制を構築できます。詳細は公式リンク参照。

---

### 17. Public Preview: Encryption in Transit for Azure Files NFS shares in AKS 

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: Encryption in Transit for Azure Files NFS shares in AKS ](https://azure.microsoft.com/updates?id=499294)

**アップデートID**: 499294
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSでAzure Files NFS v4.1ボリュームのEncryption in Transit（EiT）がパブリックプレビューで利用可能に。

- 主な変更点や新機能  
Azure File CSIドライバー経由でTLS 1.2による通信の暗号化が可能となり、データ転送のセキュリティが強化。

- 影響を受ける対象  
AKS上でAzure Files NFSを利用する開発者や運用者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討する必要あり。

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）におけるAzure Files NFS v4.1ボリュームの通信経路暗号化（Encryption in Transit：EiT）をPublic Previewとして提供開始したものです。背景には、クラウド環境でのデータ保護強化ニーズの高まりがあり、2023年6月にAzure Files NFS共有でTLS 1.2を用いたEiTがGAとなったことを踏まえ、AKS環境でも同様のセキュリティ強化を実現する目的があります。具体的には、Azure File CSIドライバーを通じてNFSマウント時にTLS 1.2による通信暗号化を有効化可能となり、AKS上のコンテナからAzure Files NFSボリュームへのデータ転送が安全に行われます。実装はCSIドライバーのパラメータ設定でEiTを有効化し、NFSクライアントとサーバ間のTLSハンドシェイクを介して暗号化通信を確立します。活用シナリオとしては、機密性の高いファイル共有やコンプライアンス要件を満たす必要があるAKSワークロードに適しています。注意点として、EiT対応はNFS v4.1に限定され、パフォーマンス影響やTLS証明書管理が発生するため事前検証が推奨されます。また、Azure Active Directory（AAD）やAzure Monitorとの連携により、認証強化や監査ログ取得が可能で、包括的なセキュリティ運用が実現します。

---

### 18. Generally Available: Confidential VMs for Ubuntu 24.04 in AKS 

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Generally Available: Confidential VMs for Ubuntu 24.04 in AKS ](https://azure.microsoft.com/updates?id=499289)

**アップデートID**: 499289
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSでUbuntu 24.04対応のConfidential VM（CVM）が一般提供開始。

- 主な変更点や新機能  
CVMにより、機密性の高いコンテナワークロードをハードウェアベースのセキュリティで保護しつつAKS上で実行可能に。

- 影響を受ける対象  
AKSで高いセキュリティ要件を持つコンテナを運用する開発者・運用者。

- 注意点があれば記載  
CVM対応ノードプールの構築時にUbuntu 24.04を選択する必要がある。対応リージョンや料金体系も確認推奨。

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）においてUbuntu 24.04ベースのConfidential Virtual Machines（CVM）が一般提供（GA）されたことを示す。CVMはハードウェアベースの信頼実行環境（Trusted Execution Environment）を活用し、メモリやCPUのデータを暗号化・隔離することで、テナントの機密性とセキュリティを強化する。今回のGAにより、AKSのノードプールでUbuntu 24.04を用いたCVMを選択可能となり、高度に機密性を要するコンテナワークロードのクラウド移行が容易になる。

技術的には、Intel SGXやAMD SEVなどのハードウェア機能を利用し、ホストOSや他のノードからの不正アクセスを防止。AKSのノードプール作成時にCVMイメージを指定し、Ubuntu 24.04の最新カーネルとセキュリティパッチを適用した環境を構築可能。これにより、コンテナ内のアプリケーションデータや処理内容が保護される。

活用シナリオとしては、金融・医療・政府機関など機密データを扱う業界でのコンテナ化されたアプリケーションの運用が想定される。特に、クラウド上でのデータ漏洩リスクを最小化しつつ、コンプライアンス要件を満たす用途に適合する。

注意点としては、CVM対応のVMサイズやリージョンに制限があり、全てのAKS機能が即時対応しているわけではない点。また、CVM利用時はパフォーマンスオーバーヘッドが発生する可能性があるため、ワークロード特性の検証が必要。

関連サービスとしては、Azure Confidential Computing、Azure Key Vaultとの連携により、機密情報の安全な管理と利用が可能。さらに、Azure PolicyでCVMノードプールの適用をガバナンス管理できるため、セキュリティポリシーの一元管理が実現する。

---

### 19. Public Preview: Confidential VMs for Azure Linux

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: Confidential VMs for Azure Linux](https://azure.microsoft.com/updates?id=499284)

**アップデートID**: 499284
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Azure Kubernetes Service (AKS)でLinux向けConfidential Virtual Machines (CVM)がパブリックプレビューとして提供開始。

- 主な変更点や新機能  
CVM対応のノードプールを作成可能となり、高度に機密性の高いコンテナワークロードをセキュアに実行可能。

- 影響を受ける対象  
AKS上で機密性の高いコンテナを運用する開発者や運用者。

- 注意点があれば記載  
プレビュー機能のため、本番環境での利用は慎重に。対応リージョンや制限事項を事前に確認推奨。

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）におけるLinuxノードプール向けのConfidential Virtual Machines（CVM）をパブリックプレビューとして提供開始したものです。背景には、機密性の高いコンテナワークロードをクラウド上で安全に運用したいニーズがあり、ハードウェアベースの信頼実行環境（Intel SGXやAMD SEV）を活用し、VM内部のメモリやデータを暗号化・保護することを目的としています。具体的には、AKSクラスター内でCVM対応ノードプールを作成可能となり、機密性保証された環境でLinuxコンテナを実行可能です。技術的には、AzureのConfidential Computing対応ハードウェア上で動作し、ホストOSや管理者からも隔離された安全な実行領域を提供。実装は、AKSのノードプール作成時にCVM SKUを指定する形で行います。活用シナリオとしては、金融・医療などの規制産業における機密データ処理や、機密アルゴリズムの保護が挙げられます。注意点として、現状はLinuxノードプールのみ対応であり、Windowsノードプールは非対応、また一部リージョン限定のため利用前に対応リージョンを確認する必要があります。さらに、CVMは通常のVMよりコストが高く、性能面での影響も考慮が必要です。関連サービスとしては、Azure Key Vaultとの連携で機密鍵管理を強化可能であり、Azure Monitorでの監視も対応しています。これにより、機密性と運用性を両立したAKS環境構築が可能となります。

---

### 20. Public Preview: Disable HTTP proxy

**公開日時**: 2025年08月06日 03:30:15 UTC
**リンク**: [Public Preview: Disable HTTP proxy](https://azure.microsoft.com/updates?id=499279)

**アップデートID**: 499279
**情報源**: Azure Updates API

**カテゴリ**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKSのHTTPプロキシ機能に「無効化」オプションがパブリックプレビューで追加されました。

- 主な変更点や新機能  
AKSノードとPodでHTTPプロキシ設定を無効化でき、プロキシ依存環境でのネットワーク制御が柔軟に行えます。

- 影響を受ける対象  
AKSクラスタをプロキシ環境で運用している技術者やネットワーク管理者。

- 注意点があれば記載  
プレビュー機能のため、本番環境での利用は慎重に検討してください。  

詳細：https://azure.microsoft.com/updates?id=499279

**詳細**:

本アップデートは、AKSクラスタにおけるHTTPプロキシ機能を無効化可能にするPublic Preview提供開始を示します。背景として、企業ネットワークでプロキシ経由の通信が必須となる環境下で、AKSノードおよびPodの通信をHTTPプロキシ経由に統一しセキュリティと管理性を向上させる目的でHTTPプロキシ機能が導入されました。今回のアップデートでは、この機能を環境に応じて柔軟に無効化できる設定が追加され、プロキシ不要な環境や特定通信の直接接続を求めるケースに対応可能となりました。

技術的には、AKSのクラスタ作成時または既存クラスタの設定変更でHTTP_PROXY環境変数をノードとPodに適用し、通信をプロキシ経由に設定します。今回の無効化オプションは、この環境変数の適用を制御し、HTTPプロキシ設定を解除する形で実装されています。設定はAzure CLIやARMテンプレート、Azure Portalから行えます。

活用シナリオとしては、企業のネットワークポリシーでプロキシ利用が必須な場合にAKS通信を統一的に管理可能な一方、開発やテスト環境でプロキシ不要な場合に機能をオフにして通信遅延や障害リスクを低減できます。注意点として、HTTPプロキシ無効化時はAKSの一部管理通信が直接インターネットに接続されるため、ネットワークセキュリティ設定の見直しが必要です。また、プロキシ設定を変更するとPodの再起動が必要になる場合があります。

関連サービスとしては、Azure MonitorやAzure Policyと連携し、プロキシ設定の監視・管理が可能です。さらに、Azure FirewallやAzure Application Gatewayと組み合わせることで、より高度なネットワーク制御が実現できます。今回のアップデートにより、AKSのネットワーク構成に柔軟性が増し、多様な企業ネットワーク環境に対応可能となりました。詳細は公式ドキュメントおよびアップデートページを参照してください。  
https://azure.microsoft.com/updates?id=499279

---


*このレポートは自動生成されました - 2025-08-07 12:03:33 JST*