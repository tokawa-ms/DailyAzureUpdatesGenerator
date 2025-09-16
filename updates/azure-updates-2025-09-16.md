# 2025年09月16日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月16日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 6 件

## 更新一覧

### 1. Retirement: Azure Databricks Standard tier will retire by October 2026

**公開日時**: 2025年09月16日 00:15:32 UTC
**リンク**: [Retirement: Azure Databricks Standard tier will retire by October 2026](https://azure.microsoft.com/updates?id=502623)

**アップデートID**: 502623
**情報源**: Azure Updates API

**カテゴリ**: AI + machine learning, Analytics, Azure Databricks, Retirements

**要約**:

- 何が更新されたか  
Azure DatabricksのStandardティアが2026年10月に廃止されることが発表されました。

- 主な変更点や新機能  
2026年4月1日以降、新規にStandardティアのワークスペース作成が不可となり、同年10月1日以降は既存のStandardティアワークスペースも利用できなくなります。

- 影響を受ける対象  
Azure Databricks Standardティアを利用中のユーザーおよび新規作成を検討している技術者。

- 注意点があれば記載  
移行計画を早めに立て、PremiumやEnterpriseティアへの切り替えを検討してください。

**詳細**:

本アップデートは、Azure DatabricksのStandardティア廃止を告知するもので、2026年4月1日以降は新規Standardティアのワークスペース作成が不可となり、同年10月1日には既存Standardティアワークスペースのサポートが終了します。背景には、Databricksの機能強化とセキュリティ・パフォーマンス向上を目的としたPremiumおよびEnterpriseティアへの移行促進があります。Standardティアは基本的なデータ分析機能を提供していましたが、今後はより高度なアクセス制御や監査機能を備えた上位ティアを利用することが推奨されます。技術的には、ワークスペース作成APIやAzureポータルからの選択肢が削除され、既存Standardティアのワークスペースは移行計画を立てる必要があります。移行時は、ノートブックやジョブ設定のエクスポート・インポート、クラスター構成の再設定が必要です。活用シナリオとしては、データエンジニアリングや機械学習パイプライン構築で、Premium以上のティアで提供されるセキュリティ機能や統合監査ログが重要となります。注意点として、Standardティア廃止に伴い、互換性のないAPIや機能制限が発生する可能性があるため、事前検証が必須です。Azure Data FactoryやAzure Synapse Analyticsとの連携は引き続き可能ですが、接続設定の見直しや認証方式の更新が必要になる場合があります。詳細は公式ドキュメントと移行ガイドを参照し、早期の移行計画策定を推奨します。

---

### 2. Retirement: hsmPlatform 1 Keys in Azure Key Vault

**公開日時**: 2025年09月15日 21:30:04 UTC
**リンク**: [Retirement: hsmPlatform 1 Keys in Azure Key Vault](https://azure.microsoft.com/updates?id=494676)

**アップデートID**: 494676
**情報源**: Azure Updates API

**カテゴリ**: Security, Key Vault, Retirements

**要約**:

- 何が更新されたか  
Azure Key VaultでhsmPlatform 1キーのサポートが2028年9月15日をもって終了予定。

- 主な変更点や新機能  
hsmPlatform 1キーは廃止され、より安全で性能向上した新しいキータイプへの移行が推奨される。

- 影響を受ける対象  
hsmPlatform 1キーを利用しているAzure Key Vaultユーザー。

- 注意点  
期限までにキーの移行を完了しないと、キーの利用が停止されるため早めの対応が必要。

**詳細**:

本アップデートは、Azure Key VaultにおけるhsmPlatform 1キーのサポート終了を2028年9月15日付で実施するものです。背景には、セキュリティ強化およびパフォーマンス最適化の継続的な取り組みがあり、旧世代のハードウェアセキュリティモジュール（HSM）プラットフォーム1の鍵管理機能を段階的に廃止します。具体的には、hsmPlatform 1キーで生成・管理された鍵は以降の操作が不可となり、新規および既存の鍵はhsmPlatform 2以降への移行が推奨されます。技術的には、Azure Key Vaultのキー管理APIがhsmPlatform 1キーの呼び出しを拒否し、移行ツールやスクリプトを用いて鍵のエクスポート・再生成を行う必要があります。活用シナリオとしては、既存の暗号化・署名処理に使用しているhsmPlatform 1キーを安全にhsmPlatform 2キーに切り替えることで、最新の暗号化アルゴリズムやパフォーマンス改善を享受可能です。注意点として、移行期間中に鍵の互換性や依存するアプリケーションの動作確認を必ず行い、鍵の失効やサービス停止を防ぐことが重要です。関連サービスとしては、Azure Key Vaultと連携するAzure FunctionsやAzure App Service、Azure Storageの暗号化機能が影響を受けるため、これらのサービス設定も併せて見直す必要があります。詳細は公式ドキュメントを参照し、計画的な移行を推奨します。

---

### 3. Generally Available: Enabling dedicated connections to backends in Azure Application Gateway

**公開日時**: 2025年09月15日 16:45:57 UTC
**リンク**: [Generally Available: Enabling dedicated connections to backends in Azure Application Gateway](https://azure.microsoft.com/updates?id=503398)

**アップデートID**: 503398
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Application Gateway, Services, Features, Management

**要約**:

- 何が更新されたか  
Azure Application Gateway V2で、バックエンドへの専用接続を有効化可能に。

- 主な変更点や新機能  
従来はアイドル状態のバックエンド接続を再利用していたが、専用接続を設定することで各リクエストに専用TCP接続を割り当て可能に。

- 影響を受ける対象  
Application Gatewayを利用し、バックエンドとの接続管理を細かく制御したい技術者や運用チーム。

- 注意点  
専用接続を有効にするとTCP接続数が増加し、リソース消費が増える可能性があるため、負荷やコストを考慮して設定する必要あり。

**詳細**:

Azure Application Gateway V2の新機能として、バックエンドサーバーへの専用接続（Dedicated Connections）が一般提供（GA）されました。従来はアイドル状態のTCP接続を再利用することでリソース効率を最適化していましたが、本機能により特定のバックエンドとの接続を専用化し、接続の安定性やパフォーマンスを向上させることが可能です。専用接続は、特に長時間持続するセッションや高頻度通信が必要なアプリケーションに適しており、TCP接続の競合や遅延を低減します。設定はApplication Gatewayのバックエンドプール設定で有効化でき、既存のロードバランシング機能やWAF（Web Application Firewall）と併用可能です。ただし、専用接続を多用するとTCPコネクション数が増加し、リソース消費が高まるため、バックエンドサーバーのキャパシティとトラフィックパターンを考慮する必要があります。Azure MonitorやNetwork Watcherと連携することで接続状態の監視やトラブルシューティングが容易になります。専用接続機能は、Azure Kubernetes Service（AKS）やApp Serviceなどのバックエンドに対しても効果的に利用可能で、マイクロサービス間通信の安定化やレイテンシ削減に寄与します。

---

### 4. Generally Available: Backend TLS validation controls in Azure Application Gateway

**公開日時**: 2025年09月15日 16:30:18 UTC
**リンク**: [Generally Available: Backend TLS validation controls in Azure Application Gateway](https://azure.microsoft.com/updates?id=503393)

**アップデートID**: 503393
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Application Gateway, Services, Features, Management

**要約**:

- 何が更新されたか  
Azure Application Gateway V2で、バックエンドTLS検証のカスタマイズ機能がGA（一般提供）になりました。

- 主な変更点や新機能  
HTTPSバックエンド設定時に、TLSハンドシェイクの検証項目をユーザーが制御可能に。証明書の検証強化や柔軟な設定が可能です。

- 影響を受ける対象  
Azure Application Gatewayを利用し、HTTPSバックエンド通信を行う技術者や運用者。

- 注意点があれば記載  
設定変更によりTLS検証の挙動が変わるため、既存環境への影響を事前に検証することを推奨します。

**詳細**:

Azure Application Gateway V2のバックエンドTLS検証制御機能がGA（一般提供）となりました。本アップデートは、バックエンドとのHTTPS通信におけるTLS証明書検証を顧客が細かく制御可能にすることを目的としています。従来はバックエンド設定でHTTPSを選択すると、Application Gatewayが自動的に証明書の有効期限、発行者、ホスト名検証などを行っていましたが、本機能によりこれらの検証項目を個別に有効・無効化できます。技術的には、バックエンドHTTP設定の「Backend TLS validation」オプションで、証明書の検証ポリシー（例：CN/SANのホスト名検証、証明書チェーンの検証、失効チェックなど）を設定可能です。これにより、自己署名証明書や内部CA証明書を用いる環境でも柔軟に対応でき、開発・テスト環境やハイブリッド構成での運用性が向上します。活用例としては、オンプレミスやプライベートVNet内のバックエンドサーバーに対し、特定のTLS検証のみを行い通信を確立するケースが挙げられます。注意点として、検証を緩和するとセキュリティリスクが増大するため、運用ポリシーに基づいた設定が必要です。また、Azure Key VaultやAzure Monitorと連携し、証明書管理やログ監視を強化することが推奨されます。詳細は公式ドキュメントおよびアップデートページ（https://azure.microsoft.com/updates?id=503393）を参照してください。

---

### 5. Generally Available: Azure SQL hub experience in Azure portal 

**公開日時**: 2025年09月15日 16:30:18 UTC
**リンク**: [Generally Available: Azure SQL hub experience in Azure portal ](https://azure.microsoft.com/updates?id=502014)

**アップデートID**: 502014
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Azure SQL, Features

**要約**:

- 何が更新されたか  
Azureポータルに「Azure SQLハブ」が一般提供開始されました。

- 主な変更点や新機能  
Azure SQL関連サービスを一元管理できる新しいダッシュボードを提供し、サービス選択や管理が容易に。

- 影響を受ける対象  
Azure SQLを利用する開発者や運用担当者。

- 注意点があれば記載  
既存の個別サービス管理画面と併用可能で、移行は任意です。

**詳細**:

本アップデートは、Azure SQLサービス選択の複雑さを解消するため、Azureポータル内に「Azure SQLハブ」を一般提供（GA）したものです。Azure SQLハブは、Azure SQL Database、Managed Instance、SQL Edgeなど全Azure SQLリソースを一元管理できる統合ダッシュボードを提供し、リソース作成・監視・管理を効率化します。技術的には、ポータルの拡張機能として実装され、リソースタイプ横断のフィルタリングやクイックアクションをサポート。例えば、新規データベース作成時に最適なサービス選択をガイドし、パフォーマンスやセキュリティ設定も一画面で確認可能です。活用シナリオとしては、複数Azure SQLリソースの運用管理やコスト最適化、トラブルシューティングの迅速化が挙げられます。制限として、既存の個別リソース管理画面と併用する必要があり、全機能がハブに集約されているわけではありません。Azure MonitorやAzure Security Centerとの連携により、監視・セキュリティ強化も容易です。技術者はハブを活用し、Azure SQL環境の統合的な運用管理を推進できます。

---

### 6. Retirement: Azure Linux 2.0 on AKS 

**公開日時**: 2025年09月15日 13:45:52 UTC
**リンク**: [Retirement: Azure Linux 2.0 on AKS ](https://azure.microsoft.com/updates?id=500645)

**アップデートID**: 500645
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）上のAzure Linux 2.0が2025年11月30日にサポート終了となります。

- 主な変更点や新機能  
Azure Linux 2.0はAzure Linux 3.0に置き換えられ、より新しくサポートされたOSバージョンに移行が必要です。

- 影響を受ける対象  
AKSでAzure Linux 2.0を利用しているユーザー。

- 注意点  
2025年11月30日までにAzure Linux 3.0へ移行しないとサポートが受けられなくなるため、早めの対応を推奨します。

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）上で提供されているAzure Linux 2.0のサポート終了（2025年11月30日）に伴い、最新のAzure Linux 3.0への移行を促すものです。Azure Linux 3.0はセキュリティ強化、最新カーネル対応、パフォーマンス最適化が施されており、長期的な安定運用を実現します。技術的には、AKSクラスターのノードイメージをAzure Linux 3.0ベースに更新することで移行可能で、Azure CLIやARMテンプレートを用いたノードプールの再作成やアップグレードが推奨されます。移行により、最新のセキュリティパッチ適用やコンテナランタイムの改善が利用可能となり、特にセキュリティ要件の高い環境や最新機能を活用するシナリオで効果的です。注意点として、移行前にアプリケーションの互換性検証やバックアップを行い、ノードプールの一括切り替え時のダウンタイムを考慮する必要があります。また、Azure MonitorやAzure Policyなどの連携サービスは引き続き利用可能で、最新OS対応の監視・管理が可能です。移行計画を早期に策定し、2025年11月までに確実なアップデートを推奨します。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2025-09-16 12:01:48 JST*