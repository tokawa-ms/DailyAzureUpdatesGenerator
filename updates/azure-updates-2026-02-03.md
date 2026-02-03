# 2026年02月03日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年02月03日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Retirement: Azure Front Door and Azure CDN profiles will end support for DHE cipher suites on April 1, 2026

**公開日時**: 2026年02月02日 18:15:39 UTC
**リンク**: [Retirement: Azure Front Door and Azure CDN profiles will end support for DHE cipher suites on April 1, 2026](https://azure.microsoft.com/updates?id=553527)

**アップデートID**: 553527
**情報源**: Azure Updates API

**カテゴリ**: Networking, Security, Azure Front Door

**要約**:

- 何が更新されたか  
Azure Front Door（Standard, Premium, Classic）およびAzure CDN（Classic）でDHE暗号スイートのサポート終了が発表されました。

- 主な変更点や新機能  
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384およびTLS_DHE_RSA_WITH_AES_128_GCM_SHA384の暗号スイートが2026年4月1日以降利用不可になります。

- 影響を受ける対象  
これらのサービスを利用し、該当DHE暗号スイートを使用している通信環境。

- 注意点  
移行期間を考慮し、強力な暗号スイートへの切替えを早めに検討してください。

**詳細**:

本アップデートは、Azure Front Door（Standard、Premium、Classic）およびAzure CDN（Classic）がTLS暗号スイートのセキュリティ強化を目的に、DHE（Diffie-Hellman Ephemeral）ベースの弱い暗号スイート「TLS_DHE_RSA_WITH_AES_256_GCM_SHA384」「TLS_DHE_RSA_WITH_AES_128_GCM_SHA384」のサポートを2026年4月1日付で終了するものです。DHE暗号スイートは過去に安全性が懸念されており、より安全なECDHE（Elliptic Curve Diffie-Hellman Ephemeral）暗号スイートへの移行が推奨されています。これにより、TLSハンドシェイク時の鍵交換方式がDHEからECDHEに限定され、通信の耐量子性や中間者攻撃耐性が向上します。技術的には、AzureのエッジノードでTLS設定が更新され、該当暗号スイートを無効化します。利用者はクライアント側のTLS設定を確認し、ECDHE対応の最新ブラウザやライブラリを使用する必要があります。特に古いクライアントやIoTデバイスでは接続障害が発生する可能性があるため、事前検証が重要です。Azure Front DoorやCDNを介したWebアプリケーションやAPIのセキュリティ強化に寄与し、Azure Application GatewayやAzure Firewallなど他のネットワークセキュリティサービスと連携する際も一貫したTLSポリシー運用が可能です。詳細は公式ドキュメントを参照し、2026年4月までに環境のTLS対応状況を見直すことを推奨します。

---

### 2. Generally Available: Serverless workspaces in Azure Databricks

**公開日時**: 2026年02月02日 18:15:39 UTC
**リンク**: [Generally Available: Serverless workspaces in Azure Databricks](https://azure.microsoft.com/updates?id=550845)

**アップデートID**: 550845
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Analytics, Azure Databricks

**要約**:

- 何が更新されたか  
Azure Databricksのサーバーレスワークスペースが一般提供（GA）となりました。

- 主な変更点や新機能  
サーバーレスコンピュートとデフォルトストレージを事前構成した完全マネージド型ワークスペースを提供し、インフラ管理不要のSaaS体験を実現。

- 影響を受ける対象  
Azure Databricks利用者、特にインフラ管理の負担を軽減したいデータエンジニアやデータサイエンティスト。

- 注意点  
既存のクラスター管理型ワークスペースとは異なる運用モデルのため、移行時は設定やコストモデルを確認する必要あり。

**詳細**:

Azure DatabricksのServerless Workspacesが一般提供（GA）となりました。本アップデートは、インフラ管理を不要とし、迅速な分析環境構築を目的に開発されました。Serverless Workspacesは、サーバーレスコンピュートとデフォルトストレージをあらかじめ構成済みの完全マネージド型ワークスペースで、ユーザーはクラスタ管理やスケーリングを意識せずに利用可能です。技術的には、Azureのサーバーレスコンピューティング基盤上でDatabricksランタイムが動作し、ジョブ実行時に自動的にリソースが割り当てられ、利用後は自動解放されます。活用例としては、データサイエンスやETL処理の迅速なプロトタイピング、スパイク的な分析処理に最適です。注意点としては、カスタムクラスタ設定や高度なネットワーク構成は制限されるため、複雑なワークロードには従来型ワークスペースが推奨されます。Azure Blob StorageやAzure Data Lake Storageとの連携が標準で組み込まれており、データの永続化や共有が容易です。これにより、運用負荷を大幅に軽減しつつ、スケーラブルな分析基盤を迅速に展開可能です。詳細は公式リンク参照。

---

### 3. Generally Available: Default Ruleset 2.2 in WAF for Azure Application Gateway

**公開日時**: 2026年02月02日 17:45:01 UTC
**リンク**: [Generally Available: Default Ruleset 2.2 in WAF for Azure Application Gateway](https://azure.microsoft.com/updates?id=553532)

**アップデートID**: 553532
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Application Gateway, Web Application Firewall

**要約**:

- 何が更新されたか  
Azure Application GatewayのWAFで、Default Rule Set (DRS) 2.2がGA（一般提供）となりました。

- 主な変更点や新機能  
DRS 2.2は最新のOWASPルールセットに基づき、既知の脆弱性や攻撃パターンに対する保護を強化。Microsoft Threat Intelligenceも統合し、検出精度が向上しています。

- 影響を受ける対象  
Azure Application GatewayのWAFを利用している全ユーザー。

- 注意点  
既存のカスタムルールとの競合や誤検知の可能性があるため、適用前にテスト環境での検証を推奨します。

**詳細**:

Azure Application GatewayのWeb Application Firewall（WAF）において、Default Rule Set (DRS) 2.2が一般提供（GA）されました。DRS 2.2は、OWASP Core Rule SetをベースにMicrosoftが独自に強化したルール群で、SQLインジェクションやクロスサイトスクリプティング（XSS）などの一般的なWeb攻撃に対する防御を強化しています。今回のアップデートでは、新たな脆弱性パターンの検出精度向上や誤検知の低減が図られており、Azureが管理するルールセットの自動更新により運用負荷が軽減されます。技術的には、Application GatewayのWAFポリシーにDRS 2.2を適用するだけで即座に最新の防御機能が利用可能で、カスタムルールとの併用も可能です。活用シナリオとしては、パブリックWebアプリケーションのセキュリティ強化や、DevSecOps環境での自動セキュリティ適用が挙げられます。注意点として、DRSの更新により一部トラフィックで誤検知が発生する可能性があるため、ログ監視とチューニングが推奨されます。さらに、Azure SentinelやAzure Monitorと連携することで、検知イベントの可視化や自動対応が可能となり、包括的なセキュリティ運用が実現します。

---


*このレポートは自動生成されました - 2026-02-03 12:01:30 JST*