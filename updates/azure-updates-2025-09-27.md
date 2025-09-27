# 2025年09月27日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月27日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Azure VMware Solution AV36 Node Retirement on June 30, 2028

**公開日時**: 2025年09月27日 00:30:39 UTC
**リンク**: [Azure VMware Solution AV36 Node Retirement on June 30, 2028](https://azure.microsoft.com/updates?id=503883)

**アップデートID**: 503883
**情報源**: Azure Updates API

**カテゴリ**: Compute, Azure VMware Solution, Retirements

**要約**:

- 何が更新されたか  
Azure VMware SolutionのAV36ノードタイプが2028年6月30日に廃止予定と発表されました。

- 主な変更点や新機能  
AV36ノードの提供が終了し、新規利用はできなくなります。

- 影響を受ける対象  
AV36ノードを利用中のユーザーおよびAV36のReserved Instance契約者。

- 注意点があれば記載  
既存のAV36 Reserved Instance契約には影響ありませんが、契約満了時期を確認し、移行計画を立てることを推奨します。

**詳細**:

本アップデートは、Azure VMware Solution（AVS）におけるAV36ノードタイプの2028年6月30日をもっての退役を告知するものです。AV36ノードはAVSの基盤となる仮想化リソースの一種であり、今回の退役により新規のAV36ノード導入は不可となりますが、既存のAV36リザーブドインスタンス（RI）契約には影響がありません。技術者は現在のRIの有効期限を確認し、退役までのリソース計画を見直す必要があります。AV36ノードの退役に伴い、AVS環境はより新しいノードタイプへ移行が推奨され、これによりパフォーマンスやセキュリティの最新基準を維持可能です。実装面では、既存のAV36ベースのクラスタから新ノードタイプへの移行計画を策定し、VMのライブマイグレーションやバックアップを活用したダウンタイム最小化が求められます。注意点として、AV36ノードの退役後はサポートが終了し、障害対応やアップデート提供が停止するため、早期の移行準備が重要です。AVSはAzureのネットワークやストレージサービスと密接に連携しており、移行時にはAzure Virtual NetworkやAzure Backupとの整合性を確保することが推奨されます。詳細は公式リンクを参照し、計画的なリソース更新を推進してください。

---

### 2. Retirement: Entity Linking from Azure AI Language

**公開日時**: 2025年09月26日 22:00:37 UTC
**リンク**: [Retirement: Entity Linking from Azure AI Language](https://azure.microsoft.com/updates?id=499851)

**アップデートID**: 499851
**情報源**: Azure Updates API

**カテゴリ**: AI + machine learning, Azure AI Language, Retirements, Services

**要約**:

- 何が更新されたか  
Azure AI LanguageのEntity Linking機能が廃止予定となりました。

- 主な変更点や新機能  
代替として、同じくAzure AI LanguageのNamed Entity Recognition（NER）機能を利用し、エンティティ識別を行うことが推奨されています。

- 影響を受ける対象  
Entity Linking APIを利用している開発者やシステム。

- 注意点があれば記載  
廃止に伴い早めの移行検討が必要で、Microsoftはサポートを継続提供予定です。

**詳細**:

MicrosoftはAzure AI LanguageのEntity Linking機能を段階的に廃止します。背景には、より統合的かつ高精度なエンティティ認識を実現するため、Named Entity Recognition（NER）機能への移行を促す狙いがあります。Entity Linkingはテキスト内のエンティティを外部知識ベースのIDに紐付ける機能でしたが、今後はNERがエンティティ抽出と識別を担い、よりシンプルなAPIで提供されます。技術的には、NERは機械学習モデルを用いてテキストから固有表現を抽出し、カテゴリ分類を行います。実装はAzure Cognitive ServicesのLanguageリソース経由でREST APIまたはSDKを利用可能です。活用例としては、文書解析やチャットボットの意図理解、メタデータ生成などが挙げられます。注意点として、Entity Linking特有の外部知識ベースとの連携機能はNERに直接含まれないため、必要に応じてカスタム実装や他サービスとの組み合わせが必要です。Azure Cognitive SearchやKnowledge Miningと連携することで、抽出したエンティティ情報を検索や分析に活用可能です。移行期間中は両機能の併用が推奨されます。詳細は公式ドキュメントを参照してください。

---

### 3. Retirement: The Linux Consumption hosting plan of Azure Functions will be retired on September 30, 2028. Migrate to Flex Consumption.

**公開日時**: 2025年09月26日 16:30:29 UTC
**リンク**: [Retirement: The Linux Consumption hosting plan of Azure Functions will be retired on September 30, 2028. Migrate to Flex Consumption.](https://azure.microsoft.com/updates?id=499451)

**アップデートID**: 499451
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, Internet of Things, Azure Functions, Retirements, Pricing & Offerings

**要約**:

- 何が更新されたか  
Azure FunctionsのLinux Consumptionプランが2028年9月30日に廃止されます。

- 主な変更点や新機能  
代替としてFlex Consumptionプランへの移行が推奨され、これにより高速スケーリング、高度なネットワーク機能、コールドスタートの軽減、同時実行制御が利用可能です。

- 影響を受ける対象  
Linux Consumptionプランを利用中のAzure Functionsユーザー。

- 注意点  
早めの移行計画が必要で、影響リソースの特定とテストを推奨します。

**詳細**:

本アップデートは、Azure FunctionsのLinux Consumptionプランの2028年9月30日廃止に伴い、より高性能なFlex Consumptionプランへの移行を促すものです。Linux Consumptionプランはシンプルなサーバーレス実行環境を提供していましたが、スケーリング速度やネットワーク機能、コールドスタート対策、同時実行制御に制約がありました。Flex Consumptionプランはこれらを改善し、コンテナベースの柔軟なホスティングを実現。具体的には、迅速なスケールアウト/イン、VNet統合による高度なネットワーク設定、コールドスタート時間の短縮、同時実行数の細かな制御が可能です。移行はAzure PortalやAzure CLIで対象リソースを特定し、プラン変更を行います。シナリオとしては、トラフィック変動が激しいAPIバックエンドやイベント駆動型処理でのパフォーマンス向上が期待されます。注意点として、Flex ConsumptionはLinux Consumptionと異なり、料金体系やリソース制限が異なるため事前検証が必要です。Azure MonitorやApplication Insightsとの連携でパフォーマンス監視も強化可能です。

---

### 4. Retirement: Upgrade BlobFuse v1 to latest version of Blobfuse v2 

**公開日時**: 2025年09月26日 16:00:55 UTC
**リンク**: [Retirement: Upgrade BlobFuse v1 to latest version of Blobfuse v2 ](https://azure.microsoft.com/updates?id=498563)

**アップデートID**: 498563
**情報源**: Azure Updates API

**カテゴリ**: Storage, Azure Blob Storage, Retirements

**要約**:

- 何が更新されたか  
BlobFuse v1のサポート終了とBlobFuse v2への移行推奨が発表されました。

- 主な変更点や新機能  
今後のAzure Blob Storageのファイルシステムアクセス関連の機能強化はBlobFuse v2に集中します。v2はパフォーマンスや安定性が向上しています。

- 影響を受ける対象  
BlobFuse v1を利用しているユーザーやシステム。

- 注意点があれば記載  
BlobFuse v1はサポートが終了するため、早急にv2へアップグレードする必要があります。  

情報源: https://azure.microsoft.com/updates?id=498563

**詳細**:

Azure Blob Storageのファイルシステムアクセスを実現するBlobFuseは、v1のサポート終了に伴い、最新のBlobFuse v2へのアップグレードが推奨されています。BlobFuse v2は、v1に比べてパフォーマンス向上、安定性強化、ネイティブなFUSEインターフェースの最適化を実現し、Azure Blob Storageとの連携を効率化します。具体的には、キャッシュ管理の改善やメタデータ処理の高速化、エラー復旧機能の強化が含まれ、Linux環境でのマウント操作がより堅牢になります。実装はFUSEベースのファイルシステムドライバとして動作し、Blob Storageのオブジェクトをローカルファイルのように扱うことが可能です。典型的な活用シナリオは、コンテナや仮想マシン上での大容量データアクセスや、ビッグデータ処理パイプラインにおけるストレージマウントです。注意点として、v1からv2への移行時には設定ファイルやマウントオプションの見直しが必要であり、v1のサポート終了に伴いセキュリティアップデートもv2に限定されます。BlobFuse v2はAzure Blob Storageのほか、Azure AD認証やManaged Identityと連携し、セキュアなアクセス制御を実現します。詳細は公式ドキュメントとアップデート情報を参照してください。

---

### 5. Retirement: Azure App Service on Azure Arc enabled Kubernetes

**公開日時**: 2025年09月26日 11:45:02 UTC
**リンク**: [Retirement: Azure App Service on Azure Arc enabled Kubernetes](https://azure.microsoft.com/updates?id=500016)

**アップデートID**: 500016
**情報源**: Azure Updates API

**カテゴリ**: Compute, Mobile, Web, App Service, Retirements, Features

**要約**:

- 何が更新されたか  
Azure Arc対応Kubernetes上のAzure App Serviceが2025年9月30日をもって廃止されます。

- 主な変更点や新機能  
新規インストールができなくなり、既存環境も廃止予定です。

- 影響を受ける対象  
Azure Arc対応Kubernetes上でApp Serviceを利用中のユーザー。

- 注意点  
廃止までに他のホスティングソリューションへアプリケーションを移行する必要があります。

**詳細**:

本アップデートは、2025年9月30日をもって「Azure App Service on Azure Arc enabled Kubernetes」の提供終了（リタイアメント）を告知するものです。これにより、同サービスの拡張機能の新規インストールが停止されます。背景には、オンプレミスやマルチクラウド環境でのKubernetes管理に対するAzure Arcの進化と、より統合的かつ効率的なアプリケーションホスティング環境への移行促進があります。Azure App Service on Azure Arc enabled Kubernetesは、Azure Arc対応Kubernetesクラスタ上でApp ServiceのPaaS機能を利用可能にし、開発者がクラウドと同様の環境でWebアプリやAPIを展開できる仕組みでした。具体的には、AzureポータルやCLIからArcクラスタにApp Service拡張をインストールし、App Serviceプランやアプリを管理する形態でした。今後は、Azure Kubernetes Service (AKS)やAzure Container Apps、Azure Functionsなど、よりネイティブなクラウドサービスへの移行が推奨されます。移行時は、アプリケーションの依存関係やネットワーク構成、認証・監視設定の見直しが必要です。なお、Azure Arcは引き続きKubernetesクラスタの管理やポリシー適用に利用可能であり、これらサービスとの連携強化が期待されます。利用者は早期に代替ソリューションの検討と移行計画を策定することが重要です。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2025-09-27 12:01:37 JST*