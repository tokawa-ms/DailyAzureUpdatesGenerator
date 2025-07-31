# 2025年07月31日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年07月31日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 6 件

## 更新一覧

### 1. Public Preview: New SQL Server database migration in Azure Arc

**公開日時**: 2025年07月30日 17:00:36 UTC
**リンク**: [Public Preview: New SQL Server database migration in Azure Arc](https://azure.microsoft.com/updates?id=498948)

**アップデートID**: 498948
**情報源**: Azure Updates API

**カテゴリ**: In preview, Features

**要約**:

- 何が更新されたか  
Azure Arc上でのSQL Serverデータベース移行がパブリックプレビューで提供開始。

- 主な変更点や新機能  
評価からプロビジョニング、カットオーバーまで一連の移行作業をAzureポータル内で一元管理可能に。Azure Database Migration Serviceが統合され、移行プロセスが簡素化。

- 影響を受ける対象  
Azure Arcを利用してオンプレや他クラウドのSQL ServerをAzureへ移行する技術者や運用チーム。

- 注意点  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討が必要。最新のドキュメントを参照し、制限事項を確認すること。

**詳細**:

本アップデートは、Azure Arc対応環境におけるSQL Serverデータベースの移行プロセスを一元化し、効率化することを目的としています。従来は評価、プロビジョニング、カットオーバーが分散していた作業を、Azureポータル上の単一インターフェースで完結可能にしました。新たに統合されたAzure Database Migration Service（DMS）を活用し、オンプレミスや他クラウド上のSQL ServerからAzure Arc管理下のサーバーへの移行をシームレスに実行できます。技術的には、Azure Arcエージェントを対象サーバーに導入し、DMSが移行評価レポートを生成、移行ジョブの管理・監視をAzureポータルから行います。活用シナリオとしては、ハイブリッド環境やマルチクラウド環境でのSQL Server移行、既存インフラのクラウド統合が挙げられます。注意点としては、現時点でプレビュー段階のため、対応するSQL Serverのバージョンや機能に制限があり、商用環境での利用は慎重を要します。Azure MonitorやAzure Policyと連携することで、移行後の運用監視やガバナンス強化も可能です。詳細は公式ドキュメントを参照し、環境に応じた検証を推奨します。

---

### 2. Generally Available: Azure SQL updates for late-July 2025

**公開日時**: 2025年07月30日 17:00:36 UTC
**リンク**: [Generally Available: Azure SQL updates for late-July 2025](https://azure.microsoft.com/updates?id=498943)

**アップデートID**: 498943
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

- 何が更新されたか  
Azure SQLでUnicode文字列リテラルをUnicodeコード値で定義可能なUNISTR関数と、ANSI SQL標準の連結演算子「||」が利用可能に。

- 主な変更点や新機能  
Unicode文字列操作の柔軟性向上と、ANSI SQL準拠の文字列連結がサポートされた。

- 影響を受ける対象  
Azure SQLを利用する開発者およびDB管理者。

- 注意点があれば記載  
既存の文字列連結処理との互換性確認を推奨。

**詳細**:

2025年7月下旬にAzure SQLで提供開始されたアップデートでは、Unicode文字列リテラルの定義にUNISTR関数を利用可能となり、Unicodeエンコード値を直接文字列内で指定できるようになりました。これにより、多言語対応や特殊文字の扱いが容易になり、従来の文字列リテラルの制約を解消します。また、ANSI SQL標準の連結演算子「||」がサポートされ、文字列結合の記述が標準準拠かつ簡潔に行えるようになりました。これらの機能は、T-SQLクエリ内での文字列操作をより柔軟かつ互換性高く実装可能にし、国際化対応アプリケーションや標準SQLベースの移行プロジェクトに有効です。実装は既存のクエリにUNISTR('…')や「||」演算子を適用するだけで利用可能で、追加設定は不要です。ただし、UNISTRはUnicodeコードポイント指定に特化しているため、文字コードの正確な理解が必要であり、誤ったコード指定は意図しない文字表示を招く可能性があります。Azure SQL DatabaseおよびManaged Instanceで利用可能で、Azure Data FactoryやAzure Synapse Analyticsとの連携時にもUnicode文字列処理の一貫性向上に寄与します。

---

### 3. Public Preview: Azure Database for PostgreSQL cascading read replica 

**公開日時**: 2025年07月30日 17:00:36 UTC
**リンク**: [Public Preview: Azure Database for PostgreSQL cascading read replica ](https://azure.microsoft.com/updates?id=498938)

**アップデートID**: 498938
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverで、カスケード型のリードレプリカがPublic Previewで利用可能になりました。

- 主な変更点や新機能  
既存のリードレプリカからさらにリードレプリカを作成できるため、読み取り負荷の分散やスケーラビリティが向上します。

- 影響を受ける対象  
PostgreSQL Flexible Serverを利用し、リードレプリカを活用している開発者や運用担当者。

- 注意点があれば記載  
Public Preview機能のため、本番環境での利用は慎重に検討し、最新のドキュメントを確認してください。

**詳細**:

Azure Database for PostgreSQL Flexible Serverにおいて、Public Previewとして「カスケード型リードレプリカ」機能が提供開始されました。本機能は、既存のリードレプリカからさらに別のリードレプリカを作成可能とし、読み取り負荷の分散や地理的分散を強化することを目的としています。従来はマスターサーバーから直接リードレプリカを作成していましたが、カスケード型ではリードレプリカが新たなレプリカのソースとなるため、マスターの負荷軽減やネットワーク帯域の最適化が可能です。実装はPostgreSQLのストリーミングレプリケーションを基盤とし、Flexible Serverの管理コンソールやCLIから既存レプリカを指定して新規レプリカ作成を行います。活用例としては、グローバル展開時の読み取りレプリカの階層的配置や、開発・検証環境へのデータ同期が挙げられます。注意点として、カスケード型レプリカの遅延や障害時のフェイルオーバー挙動を理解し、監視設定を適切に行う必要があります。また、Azure MonitorやAzure Arcと連携することで運用管理の効率化が図れます。今後の本機能のGAに向けて、パフォーマンス検証や運用設計に活用可能な重要アップデートです。

---

### 4. Generally Available: Accelerated logs now available for General Purpose tier in Azure Database for MySQL - Flexible Server

**公開日時**: 2025年07月30日 17:00:36 UTC
**リンク**: [Generally Available: Accelerated logs now available for General Purpose tier in Azure Database for MySQL - Flexible Server](https://azure.microsoft.com/updates?id=498933)

**アップデートID**: 498933
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Azure Database for MySQL, Features

**要約**:

- 何が更新されたか  
Azure Database for MySQL - Flexible ServerのGeneral Purpose層でAccelerated LogsがGA（一般提供）開始。

- 主な変更点や新機能  
これまでBusiness Critical層のみで利用可能だったAccelerated Logsにより、ログ書き込み性能が向上し、トランザクション処理が高速化。

- 影響を受ける対象  
General Purpose層を利用するMySQL Flexible Serverユーザー。

- 注意点があれば記載  
パフォーマンス向上の恩恵を受けるためには、Accelerated Logsの有効化が必要。既存環境での動作検証を推奨。

**詳細**:

本アップデートは、Azure Database for MySQL - Flexible ServerのGeneral Purpose（GP）層に対し、従来Business Critical（BC）層のみで利用可能だった「Accelerated logs」機能を提供開始したものです。Accelerated logsは、トランザクションログの書き込み処理を高速化し、I/O待ち時間を削減することで、データベースの書き込み性能と全体的なスループットを向上させます。具体的には、ログ書き込みを専用の高速ストレージにオフロードし、遅延を抑制する仕組みで、GP層でもBC層に近いパフォーマンスを実現可能です。実装はAzureの分散ストレージとキャッシュ技術を活用し、ログの耐久性と整合性を保ちながら高速化を達成しています。活用シナリオとしては、書き込み負荷の高いWebアプリケーションやトランザクション処理が多い業務系システムで効果的です。注意点としては、Accelerated logsはGP層の追加オプションとして有効化が必要で、コスト増加や一部リージョン非対応の可能性があります。また、バックアップやレプリケーション機能との整合性も考慮が必要です。関連サービスとしては、Azure Monitorでログパフォーマンスの監視、Azure Backupとの連携によるデータ保護が推奨されます。今回の拡張により、GP層ユーザーもBC層に匹敵するログ性能を享受でき、コストパフォーマンスの高い運用が可能となりました。

---

### 5. Generally Available: Configure backup interval for Azure Database for MySQL automated backups 

**公開日時**: 2025年07月30日 17:00:36 UTC
**リンク**: [Generally Available: Configure backup interval for Azure Database for MySQL automated backups ](https://azure.microsoft.com/updates?id=498928)

**アップデートID**: 498928
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Azure Database for MySQL, Features

**要約**:

- 何が更新されたか  
Azure Database for MySQLの自動バックアップで、バックアップ間隔を設定可能に。

- 主な変更点や新機能  
より頻繁なスナップショット取得により、復元速度が向上。バックアップ間隔をカスタマイズできるため、運用要件に応じた最適化が可能。

- 影響を受ける対象  
Azure Database for MySQLを利用するユーザーで、自動バックアップの復元性能を重視する技術者。

- 注意点  
バックアップ頻度の増加はストレージ使用量やコストに影響するため、適切な間隔設定が必要。

**詳細**:

Azure Database for MySQLの自動バックアップにおいて、バックアップ間隔をユーザーが設定可能となり、リストア速度の向上を実現しました。従来はシステムが固定間隔でスナップショットを取得していましたが、本アップデートによりより頻繁なスナップショット取得が可能となり、復旧ポイントの粒度が細かくなります。設定はAzureポータルやCLI、ARMテンプレートで行え、バックアップ間隔を短縮することで障害発生時のデータ損失を最小化し、復旧時間を短縮可能です。具体的には、例えば5分間隔など細かい設定が可能で、トランザクション量の多いシステムでの利用に適しています。注意点として、バックアップ頻度を上げるとストレージ消費量とバックアップ処理負荷が増加するため、コストとパフォーマンスのバランスを考慮する必要があります。Azure BackupやAzure Monitorとの連携により、バックアップ状況の監視やアラート設定も可能で、運用管理の効率化に寄与します。

---

### 6. Generally Available: Azure Database for PostgreSQL Entra authentication for Power BI Desktop

**公開日時**: 2025年07月30日 16:00:44 UTC
**リンク**: [Generally Available: Azure Database for PostgreSQL Entra authentication for Power BI Desktop](https://azure.microsoft.com/updates?id=498175)

**アップデートID**: 498175
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Power BI DesktopからAzure Database for PostgreSQLへの接続にMicrosoft Entra ID認証が正式対応。

- 主な変更点や新機能  
Entra IDを用いた認証によりアクセス管理が簡素化され、セキュリティが強化。組織のEntra認証基盤との統合が容易に。

- 影響を受ける対象  
Power BI DesktopでAzure Database for PostgreSQLを利用する技術者や組織。

- 注意点  
既存の接続設定からEntra認証への移行時は設定変更が必要。対応バージョンのPower BI Desktopを利用すること。

**詳細**:

本アップデートにより、Power BI DesktopからAzure Database for PostgreSQLへの接続時にMicrosoft Entra ID（旧Azure AD）認証が正式サポートされました。これにより、従来のSQL認証に代わり、組織のEntra IDベースの認証ポリシーを適用可能となり、アクセス管理の一元化とセキュリティ強化が実現します。技術的には、Power BI Desktopのデータソース設定で「Microsoft Entra ID認証」を選択し、ユーザーのEntra ID資格情報を用いてOAuth 2.0トークンを取得、PostgreSQLサーバーの接続に利用します。これにより、パスワード管理の負荷軽減や多要素認証の適用が容易になります。活用例としては、組織のPower BIレポート作成者が自分のEntra IDで安全にデータベースへアクセスし、リアルタイム分析を行うシナリオが挙げられます。注意点として、Entra ID認証を利用するには、PostgreSQLサーバー側でEntra ID統合が事前に構成されている必要があり、旧バージョンのPower BI Desktopでは未対応です。また、接続時のネットワーク要件や適切なロール割当も重要です。関連サービスとしては、Microsoft Entra IDのID管理機能、Azure RBACによるアクセス制御、さらにPower BIのデータゲートウェイを介したオンプレミス連携も併用可能です。これにより、組織全体で統合された認証基盤を活用した安全なデータ分析環境の構築が促進されます。

---


*このレポートは自動生成されました - 2025-07-31 12:01:35 JST*