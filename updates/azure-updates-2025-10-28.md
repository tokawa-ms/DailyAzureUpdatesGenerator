# 2025年10月28日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年10月28日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Generally Available: Azure Storage Mover support for NFS source to Azure File Share (NFS 4.1) target

**公開日時**: 2025年10月27日 18:45:01 UTC
**リンク**: [Generally Available: Azure Storage Mover support for NFS source to Azure File Share (NFS 4.1) target](https://azure.microsoft.com/updates?id=514658)

**アップデートID**: 514658
**情報源**: Azure Updates API

**カテゴリ**: Launched, Services, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure Storage MoverがNFSソースからAzure File Share（NFS 4.1対応）への移行を正式サポート開始。

- 主な変更点や新機能  
オンプレのNFSファイル共有をAzure File Share（NFS 4.1）へダウンタイムを最小化して移行可能に。

- 影響を受ける対象  
NFSベースのファイル共有をAzureへ移行したいエンタープライズユーザーやシステム管理者。

- 注意点があれば記載  
移行先はAzure File ShareのNFS 4.1のみ対応。既存のStorage Mover利用環境で設定確認が必要。

**詳細**:

本アップデートにより、Azure Storage MoverはNFSファイル共有（NFS 4.1）をソースとして、Azure File Share（NFS 4.1対応）へのデータ移行を正式サポートします。Storage MoverはオンプレミスのファイルやフォルダをAzure Storageへダウンタイムを最小化しつつ移行可能なフルマネージドサービスであり、今回の対応でNFSベースのワークロード移行が容易になります。技術的には、Storage MoverエージェントがオンプレミスのNFSマウントポイントからデータを読み取り、Azure File ShareのNFS 4.1対応ストレージに効率的に転送します。移行中は差分同期や整合性チェックを行い、業務継続を支援します。典型的な活用例として、既存のNFSストレージからAzure Filesへクラウド移行しつつ、アプリケーションのダウンタイムを抑制するケースが挙げられます。制限事項としては、対象NFSバージョンが4.1に限定される点や、オンプレミス環境のネットワーク帯域やパーミッション設定に注意が必要です。関連サービスとしては、Azure File SyncやAzure Monitorと連携し、移行状況の監視やパフォーマンス最適化が可能です。これにより、NFSワークロードのクラウド移行戦略が一層強化されます。

---

### 2. Generally Available: PgBouncer 1.23.1 support in Azure Database for PostgreSQL – Flexible Server 

**公開日時**: 2025年10月27日 18:30:05 UTC
**リンク**: [Generally Available: PgBouncer 1.23.1 support in Azure Database for PostgreSQL – Flexible Server ](https://azure.microsoft.com/updates?id=513254)

**アップデートID**: 513254
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL – Flexible ServerでPgBouncer 1.23.1がGAリリースされました。

- 主な変更点や新機能  
組み込みの接続プーリング機能として、アイドル接続や短時間接続を効率的に管理し、数千の接続を低オーバーヘッドでスケール可能にします。

- 影響を受ける対象  
PostgreSQL Flexible Serverを利用するアプリケーションで大量接続を扱う技術者。

- 注意点があれば記載  
既存の接続プール設定との互換性やパフォーマンスチューニングが必要になる場合があります。

**詳細**:

Azure Database for PostgreSQL – Flexible Serverにおいて、PgBouncer 1.23.1が一般提供（GA）されました。PgBouncerは軽量な接続プーリングツールで、多数のクライアント接続を効率的に管理し、サーバー負荷を低減する目的で導入されました。今回のアップデートでは、最新の1.23.1バージョンを組み込み、接続のアイドル管理や短時間接続の最適化が強化されています。技術的には、PgBouncerがFlexible Server内でネイティブに統合され、ユーザーは設定画面から簡単に有効化・設定可能です。これにより、数千の同時接続でもリソース消費を抑えつつスケーラブルな運用が可能となります。典型的な活用例は、Webアプリケーションやマイクロサービス環境での大量同時接続処理や、短命なトランザクションが多発するケースです。ただし、PgBouncerはトランザクションプーリングモードの制約や、一部の拡張機能非対応など制限があるため、事前に動作検証が推奨されます。Azure MonitorやAzure Advisorと連携し、接続プールのパフォーマンス監視や最適化も可能です。詳細は公式ドキュメントを参照してください。

---

### 3. Generally Available: RHEL Software Reservations Now Available on Azure with Updated Pricing

**公開日時**: 2025年10月27日 16:45:57 UTC
**リンク**: [Generally Available: RHEL Software Reservations Now Available on Azure with Updated Pricing](https://azure.microsoft.com/updates?id=519526)

**アップデートID**: 519526
**情報源**: Azure Updates API

**カテゴリ**: Launched, Containers, Azure Red Hat OpenShift, Features

**要約**:

- 何が更新されたか  
Azure上でRed Hat Enterprise Linux（RHEL）のソフトウェア予約購入が再開され、課金メーターと価格体系が更新されました。

- 主な変更点や新機能  
従来の課金メーターの問題を解消し、Red Hatの新価格に準拠した料金設定が適用されます。

- 影響を受ける対象  
Azure上でRHELを利用する企業や技術者、特に予約購入を検討しているユーザー。

- 注意点があれば記載  
価格変更によりコスト計算が変わるため、既存の利用計画や予算を見直す必要があります。

**詳細**:

本アップデートは、Azure上でのRed Hat Enterprise Linux（RHEL）ソフトウェア予約購入が再開されたもので、従来の課金メーターの不整合を解消し、Red Hatの新価格体系に対応することを目的としています。具体的には、RHELの利用に対する課金メーターが改訂され、予約購入時の価格が最新のRed Hatライセンスモデルに準拠する形で更新されました。技術的には、Azureの課金システムがRHELのサブスクリプションライセンス情報と連携し、予約購入時に適切な課金単位を適用する仕組みとなっています。これにより、RHELをAzure仮想マシン上で長期的に安定的かつコスト効率良く利用可能です。活用シナリオとしては、ミッションクリティカルなエンタープライズアプリケーションの運用や、DevOps環境での一貫したRHEL環境構築が挙げられます。注意点としては、予約購入は特定のリージョンとSKUに限定される場合があるため、事前に対応状況を確認する必要があります。また、Azure Hybrid Benefitとの併用可否も確認が必要です。関連サービスとしては、Azure Cost Managementで予約の利用状況とコスト分析が可能であり、Azure MarketplaceからのRHELイメージ選択時に予約適用が自動で反映されます。

---


*このレポートは自動生成されました - 2025-10-28 12:01:36 JST*