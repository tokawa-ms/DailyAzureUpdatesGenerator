# 2025年09月11日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月11日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 8 件

## 更新一覧

### 1. Generally Available: Azure Databricks automatic identity management

**公開日時**: 2025年09月10日 21:30:10 UTC
**リンク**: [Generally Available: Azure Databricks automatic identity management](https://azure.microsoft.com/updates?id=502633)

**アップデートID**: 502633
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Analytics, Azure Databricks, Features

**要約**:

- 何が更新されたか  
Azure Databricksの自動アイデンティティ管理機能がGA（一般提供）となりました。

- 主な変更点や新機能  
Microsoft Entraとネイティブ統合し、ユーザーのプロビジョニング・デプロビジョニングを自動化可能に。

- 影響を受ける対象  
Azure Databricksを利用し、ユーザー管理を効率化したい企業や技術者。

- 注意点があれば記載  
既存の手動管理から移行する際は、権限設定や同期設定の確認が必要です。

**詳細**:

Azure Databricksの自動アイデンティティ管理機能がGA（一般提供）となり、Microsoft Entra（旧Azure AD）とのネイティブ統合によりユーザーのプロビジョニング・デプロビジョニングを自動化可能となった。本機能は、ユーザーのライフサイクル管理を効率化し、手動設定ミスや運用負荷を低減することを目的としている。具体的には、Microsoft Entraのグループやユーザー情報を基に、Databricksワークスペースへのアクセス権を自動付与・削除する仕組みで、SCIM（System for Cross-domain Identity Management）プロトコルを活用している。実装はAzureポータルやMicrosoft Entra管理画面から連携設定を行い、ポリシーに基づくアクセス制御を一元管理できる。活用例としては、組織の人事異動や退職に伴うDatabricksアクセス権の即時反映が挙げられ、セキュリティ強化と運用効率化に寄与する。注意点としては、SCIM対応のユーザー属性やグループ構成の整備が必要であり、既存のカスタムロールやアクセス制御との整合性確認が求められる。関連サービスとしてMicrosoft Entra ID、Azure RBAC、Azure Monitorと連携し、監査ログやアクセス権管理の統合運用が可能である。

---

### 2. Generally Available: Azure Database for PostgreSQL flexible server in Austria East and Chile Central 

**公開日時**: 2025年09月10日 21:30:10 UTC
**リンク**: [Generally Available: Azure Database for PostgreSQL flexible server in Austria East and Chile Central ](https://azure.microsoft.com/updates?id=502009)

**アップデートID**: 502009
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible ServerがAustria EastおよびChile Centralリージョンで一般提供（GA）開始。

- 主な変更点や新機能  
これらの新リージョンで柔軟なサーバー展開が可能となり、リージョン選択肢が拡大。

- 影響を受ける対象  
これら地域での低遅延やデータ主権を重視する開発者・運用者。

- 注意点があれば記載  
既存リージョンとの機能差異は特に記載なし。リージョン特有のネットワーク設定に注意。

**詳細**:

本アップデートにより、Azure Database for PostgreSQL Flexible Serverがオーストリア東部（Austria East）およびチリ中部（Chile Central）リージョンで一般提供（GA）開始されました。背景には、グローバルなデータ主権要件や低遅延アクセスのニーズに応えるため、地域拡大を図る目的があります。Flexible Serverは高可用性構成、スケーラブルなコンピューティングリソース、カスタマイズ可能なメンテナンスウィンドウを特徴とし、これらが新リージョンでも利用可能となりました。導入はAzureポータル、CLI、ARMテンプレートを通じて行え、VNet統合によるセキュアなネットワーク構成もサポートされます。活用例としては、欧州および南米の顧客向けアプリケーションでのデータベース遅延削減や、地域ごとのコンプライアンス遵守が挙げられます。注意点としては、リージョン固有のサービス制限や価格差、バックアップ保持期間の上限などを確認する必要があります。関連サービスとしては、Azure Monitorによるパフォーマンス監視、Azure Private Linkによるプライベート接続、Azure Active Directory連携による認証強化が可能で、これらと組み合わせることで運用効率とセキュリティを高められます。

---

### 3. Public Preview: Azure MySQL Self Heal

**公開日時**: 2025年09月10日 21:30:10 UTC
**リンク**: [Public Preview: Azure MySQL Self Heal](https://azure.microsoft.com/updates?id=501999)

**アップデートID**: 501999
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Azure Database for MySQL, Features

**要約**:

- 何が更新されたか  
Azure Database for MySQL – Flexible Serverに自己修復機能（Self-Heal）がパブリックプレビューで追加されました。

- 主な変更点や新機能  
サーバーの応答停止など一般的な問題をサポートケースを開かずに自動で検知・修復可能です。

- 影響を受ける対象  
Azure Database for MySQL – Flexible Server利用者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

本アップデートは、Azure Database for MySQL – Flexible Serverにおける運用効率向上を目的とし、サーバーの一般的な障害をユーザー自身で迅速に解決可能とするSelf-Heal機能をPublic Previewで提供開始しました。従来はサポートケースを開く必要があったサーバーの応答停止や接続異常などの問題を、ポータルやCLIからの操作で自動診断・修復できる点が特徴です。技術的には、サーバーの状態監視とトラブルシューティング用の診断ロジックを組み込み、問題発生時に再起動や構成リセットなどの修復アクションを自動または手動で実行可能にしています。活用例としては、運用監視で検知した応答遅延時に即座にSelf-Healを適用し、ダウンタイムを最小化するケースが想定されます。注意点としては、現時点で対応可能な障害種別が限定的であり、根本的な問題解決には専門的な調査が必要な場合もあること、またプレビュー機能のため本番環境での利用は慎重を要します。Azure MonitorやLog Analyticsと連携することで、Self-Healの適用状況や効果を可視化し、運用自動化の一環として活用可能です。詳細は公式ドキュメントとアップデートページを参照してください。

---

### 4. Generally Available: Azure MySQL Extended Support 

**公開日時**: 2025年09月10日 21:30:10 UTC
**リンク**: [Generally Available: Azure MySQL Extended Support ](https://azure.microsoft.com/updates?id=501994)

**アップデートID**: 501994
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Azure Database for MySQL, Features

**要約**:

- 何が更新されたか  
Azure Database for MySQL – Flexible Serverに対し、MySQLのExtended Support（延長サポート）が2026年春より一般提供開始。

- 主な変更点や新機能  
MySQLのサポート終了バージョンでも、延長サポート期間中はセキュリティ更新や重要なバグ修正が提供され、アップグレードスケジュールの柔軟性が向上。

- 影響を受ける対象  
MySQLのサポート終了バージョンを利用中のAzure Database for MySQL Flexible Serverユーザー。

- 注意点  
延長サポートは期限付きであり、長期的には最新バージョンへのアップグレードが推奨される。

**詳細**:

Azure Database for MySQL – Flexible Serverに対する「Extended Support」が2026年春より一般提供開始されます。本アップデートは、MySQLのバージョンアップグレード計画に柔軟性を持たせることを目的とし、MySQLの公式サポート終了後もセキュリティパッチや重要なバグ修正をAzure側で継続提供します。これにより、既存のMySQLバージョンを長期間安全に運用可能となり、アップグレードのタイミングを業務要件に合わせて調整できます。技術的には、Azureが独自にパッチ適用や脆弱性対応を行い、ユーザーはバージョン変更なしにセキュリティを維持可能です。活用シナリオとしては、レガシーアプリケーションの安定稼働や移行計画の延期が挙げられます。注意点として、Extended Supportは全MySQLバージョンに適用されるわけではなく、対象バージョンや期間は限定的です。また、パフォーマンス改善や新機能追加は含まれません。Azure MonitorやAzure Security Centerと連携し、運用監視とセキュリティ管理を強化することが推奨されます。詳細は公式ドキュメントで対象バージョンとサポート内容を確認してください。

---

### 5. Generally Available: Azure Database for MySQL 8.4 

**公開日時**: 2025年09月10日 21:30:10 UTC
**リンク**: [Generally Available: Azure Database for MySQL 8.4 ](https://azure.microsoft.com/updates?id=501989)

**アップデートID**: 501989
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Azure Database for MySQL, Features

**要約**:

- 何が更新されたか  
Azure Database for MySQL – Flexible Serverのバージョン8.4が一般提供開始。

- 主な変更点や新機能  
MySQL 8.4の最新機能や性能改善が利用可能に。新規サーバー作成時に選択可能。

- 影響を受ける対象  
MySQLをAzure上で運用する開発者・運用者。特に新規構築やバージョンアップ検討者。

- 注意点があれば記載  
既存サーバーの自動アップグレードはなく、新規作成または手動移行が必要。詳細は公式ドキュメント参照。

**詳細**:

Azure Database for MySQL Flexible Serverのバージョン8.4が一般提供（GA）されました。本アップデートはMySQL 8.4の最新機能とパフォーマンス改善をAzure上で利用可能にし、プロダクション環境での安定運用を目的としています。主な変更点は、MySQL 8.4の新機能対応（例えばJSON機能強化、パフォーマンススキーマの拡張）、Flexible Serverの高可用性オプションの改善、スケーラビリティ向上です。実装はAzureのマネージドサービスとして提供され、ユーザーはポータルやCLIで簡単にサーバー作成・管理が可能です。活用シナリオとしては、トランザクション処理や分析を含むWebアプリケーションのバックエンド、コンテナ化環境との連携が挙げられます。注意点としては、既存のMySQLバージョンからの直接アップグレードはサポートされず、新規作成が必要であること、また一部拡張機能の互換性確認が推奨されます。Azure FunctionsやApp Service、Azure Kubernetes Service（AKS）との連携により、スケーラブルなクラウドネイティブアプリケーション構築が容易になります。詳細は公式ドキュメント参照が推奨されます。

---

### 6. Generally Available: Azure Cosmos DB for MongoDB (vCore) encryption with customer-managed key 

**公開日時**: 2025年09月10日 21:30:10 UTC
**リンク**: [Generally Available: Azure Cosmos DB for MongoDB (vCore) encryption with customer-managed key ](https://azure.microsoft.com/updates?id=501980)

**アップデートID**: 501980
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Internet of Things, Azure Cosmos DB, Features

**要約**:

- 何が更新されたか  
Azure Cosmos DB for MongoDB (vCore)で、顧客管理キー（CMK）による暗号化がGAリリースされました。

- 主な変更点や新機能  
従来のMicrosoft管理キーに加え、顧客が管理するキーでデータ暗号化が可能となり、セキュリティとコンプライアンス要件を強化。

- 影響を受ける対象  
Azure Cosmos DB for MongoDB (vCore)を利用する企業や技術者。

- 注意点があれば記載  
CMK利用時はキー管理とローテーションの責任が顧客にあるため、適切な運用が必要です。

**詳細**:

本アップデートは、Azure Cosmos DB for MongoDB (vCore)におけるデータ暗号化の強化を目的とし、従来のMicrosoft管理キーによる自動暗号化（SMK）に加え、顧客管理キー（CMK）による暗号化をGA提供開始しました。これにより、顧客はAzure Key Vaultで管理する独自のキーを用いてデータの暗号化を制御可能となり、セキュリティポリシーやコンプライアンス要件に柔軟に対応できます。技術的には、CMKはAzure Key Vaultと連携し、キーの生成・ローテーション・アクセス制御を顧客側で管理しつつ、Cosmos DBのストレージ層で透過的に暗号化処理が行われます。導入はAzureポータルやCLIでCMKを指定し、既存クラスターへの適用も可能です。活用例としては、金融や医療など厳格なデータ保護が求められる業界での利用が想定されます。注意点として、CMK利用時はKey Vaultのアクセス許可設定やネットワーク構成を適切に管理する必要があり、キーの削除や無効化はデータアクセスに影響を及ぼすため慎重な運用が求められます。また、Azure MonitorやAzure Policyと連携し、暗号化状態の監査やガバナンス強化が可能です。

---

### 7. Public Preview: File share centric management model (Microsoft.FileShares) for Azure Files

**公開日時**: 2025年09月10日 19:30:42 UTC
**リンク**: [Public Preview: File share centric management model (Microsoft.FileShares) for Azure Files](https://azure.microsoft.com/updates?id=503096)

**アップデートID**: 503096
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure Files, Features

**要約**:

- 何が更新されたか  
Azure Filesでファイル共有の管理モデルに「Microsoft.FileShares」リソースプロバイダーがパブリックプレビューとして追加されました。

- 主な変更点や新機能  
ファイル共有がトップレベルリソースとなり、作成・管理がより直感的かつ効率的に行えるようになります。

- 影響を受ける対象  
Azure Filesを利用しファイル共有を管理する開発者や運用担当者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。API仕様の変更に注意が必要です。

**詳細**:

本アップデートは、Azure Filesのファイル共有管理を簡素化するため、Microsoft.FileSharesリソースプロバイダーによるファイル共有中心の管理モデルをパブリックプレビューで提供開始したものです。従来はストレージアカウント配下のサブリソースとして管理されていたファイル共有が、独立したトップレベルリソースとして扱えるようになり、ARMテンプレートやAzure CLI、PowerShellでの操作性が向上します。これにより、ファイル共有の作成・更新・削除が直接的かつ効率的に行え、リソース管理の柔軟性が増します。実装面では、Microsoft.FileSharesプロバイダーを登録し、ファイル共有リソースを明示的に定義する形でARMテンプレートを記述します。活用例としては、大規模なファイル共有のライフサイクル管理や、複数環境での一括デプロイが挙げられます。注意点としては現時点でプレビュー機能のため、全リージョン対応や一部APIの互換性に制限がある点に留意が必要です。Azure StorageやAzure RBACとの連携により、アクセス制御や監査も一元管理可能であり、DevOpsパイプラインへの組み込みも容易です。

---

### 8. Generally Available: Azure D192 Sizes in the Azure Dsv6 and Ddsv6-series VM Families

**公開日時**: 2025年09月10日 15:15:43 UTC
**リンク**: [Generally Available: Azure D192 Sizes in the Azure Dsv6 and Ddsv6-series VM Families](https://azure.microsoft.com/updates?id=503049)

**アップデートID**: 503049
**情報源**: Azure Updates API

**カテゴリ**: Launched, Services

**要約**:

- 何が更新されたか  
Azure Dsv6およびDdsv6シリーズVMに新たにD192サイズがGA（一般提供）開始。

- 主な変更点や新機能  
5世代Intel Xeon Platinum 8573C（Emerald Rapids）搭載で、大規模ワークロード向けに192 vCPUを提供。Dsv6はAzureマネージドディスク専用。

- 影響を受ける対象  
大規模コンピューティングリソースを必要とするエンタープライズユーザーやクラウド技術者。

- 注意点  
Dsv6シリーズはマネージドディスクのみ対応のため、既存のストレージ構成との整合性確認が必要。

**詳細**:

本アップデートでは、AzureのDsv6およびDdsv6シリーズ仮想マシンに新たにD192サイズがGA（一般提供）されました。これらは第5世代Intel Xeon Platinum 8573C（Emerald Rapids）プロセッサを搭載し、高い計算性能と効率性を実現します。Dsv6シリーズはAzureマネージドディスク専用で、Ddsv6シリーズは一部ローカルSSDも利用可能です。D192は192 vCPU、768 GiBメモリを備え、大規模なデータ処理や高負荷の分析ワークロードに適しています。実装はAzureポータルやCLI、ARMテンプレートでサイズ指定するだけで利用可能で、既存のDsv6/Ddsv6環境にシームレスに統合できます。活用例としては、大規模な機械学習モデルのトレーニングやビッグデータ分析、HPCジョブの高速化が挙げられます。注意点として、D192は高リソース消費に伴いコストが増加するため、用途に応じた適切なサイズ選定が必要です。また、リージョンによっては提供状況が異なるため事前確認が推奨されます。Azure MonitorやAzure Autoscaleとの連携により、パフォーマンス監視や負荷に応じた自動スケーリングも可能です。詳細は公式ドキュメントおよびアップデートページを参照してください。

---


*このレポートは自動生成されました - 2025-09-11 12:01:53 JST*