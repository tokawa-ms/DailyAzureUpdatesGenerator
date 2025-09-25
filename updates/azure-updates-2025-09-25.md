# 2025年09月25日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月25日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Public Preview: Discover and assess PostgreSQL in Azure Migrate 

**公開日時**: 2025年09月24日 17:00:24 UTC
**リンク**: [Public Preview: Discover and assess PostgreSQL in Azure Migrate ](https://azure.microsoft.com/updates?id=503641)

**アップデートID**: 503641
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Azure MigrateがPostgreSQLの検出と評価をパブリックプレビューでサポート開始。

- 主な変更点や新機能  
VMware、Hyper-V、物理サーバー、他クラウド環境のPostgreSQLリソースを一元的に発見・評価可能に。

- 影響を受ける対象  
AzureへのPostgreSQL移行を検討するインフラ・DB管理者やクラウドエンジニア。

- 注意点があれば記載  
パブリックプレビューのため、商用利用前に機能制限やサポート状況を確認推奨。

**詳細**:

本アップデートは、Azure MigrateにおけるPostgreSQLワークロードの発見・評価機能をパブリックプレビューで提供開始したものです。従来は仮想マシンや物理サーバーの移行評価が中心でしたが、PostgreSQLリソースの包括的な検出と評価を可能にし、移行計画の精度向上と工数削減を目的としています。具体的には、VMware、Hyper-V、物理サーバー、他クラウド環境上のPostgreSQLインスタンスを自動検出し、パフォーマンスデータや構成情報を収集。Azure Database for PostgreSQLへの移行適性を評価するレポートを生成します。技術的には、エージェントレスまたはエージェントベースのアプローチでリソースをスキャンし、Azure Migrateの統合ダッシュボードに情報を集約。これにより、移行候補の優先順位付けやリスク分析が可能です。活用シナリオとしては、オンプレや他クラウドのPostgreSQLをAzureに移行する際の事前調査やコスト見積もり、パフォーマンス最適化が挙げられます。制限事項としては、現時点で対応するPostgreSQLのバージョンや環境に制約があり、詳細はドキュメント参照が必要です。関連サービスとして、Azure Database Migration Serviceとの連携により、評価結果を基にシームレスな移行作業が実現可能です。

---

### 2. Generally Available: Delete on-demand backup in Azure DB for MySQL - Flexible Server 

**公開日時**: 2025年09月24日 17:00:24 UTC
**リンク**: [Generally Available: Delete on-demand backup in Azure DB for MySQL - Flexible Server ](https://azure.microsoft.com/updates?id=503622)

**アップデートID**: 503622
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Azure Database for MySQL, Features

**要約**:

- 何が更新されたか  
Azure DB for MySQL - Flexible Serverでオンデマンドバックアップの削除機能がGAリリースされました。

- 主な変更点や新機能  
これまで手動で作成したオンデマンドバックアップは削除できませんでしたが、2025年8月以降は不要なバックアップを手動で削除可能になります。

- 影響を受ける対象  
Azure DB for MySQL - Flexible Serverを利用し、オンデマンドバックアップを活用している技術者や運用担当者。

- 注意点があれば記載  
削除操作は復元不可のため、誤削除に注意が必要です。自動バックアップには影響ありません。

**詳細**:

Azure Database for MySQL - Flexible Serverにおいて、オンデマンドバックアップの削除機能がGA（一般提供）されました。本アップデートは、従来の自動バックアップに加え、手動でトリガーしたバックアップの管理性向上を目的としています。これにより、不要になったオンデマンドバックアップをユーザーが明示的に削除可能となり、ストレージコストの最適化やバックアップポリシーの柔軟な運用が可能です。技術的には、Azureポータル、CLI、REST API経由でオンデマンドバックアップの作成・削除操作が行え、バックアップはFlexible Serverのストレージに保存されます。活用例としては、重要な変更前後の手動バックアップ取得後、不要になったバックアップを削除し、運用コストを抑制するケースが挙げられます。注意点として、削除したバックアップは復元不可となるため、誤削除防止の運用ルール策定が必要です。また、Azure BackupやAzure Monitorと連携し、バックアップの監視やアラート設定を行うことで運用効率を高められます。今回の機能拡張により、MySQL Flexible Serverのバックアップ管理がより柔軟かつ効率的になります。

---

### 3. Retirement: Azure Disk Encryption

**公開日時**: 2025年09月24日 11:45:14 UTC
**リンク**: [Retirement: Azure Disk Encryption](https://azure.microsoft.com/updates?id=493779)

**アップデートID**: 493779
**情報源**: Azure Updates API

**カテゴリ**: Compute, Virtual Machine Scale Sets, Virtual Machines, Retirements

**要約**:

- 何が更新されたか  
Azure Disk Encryptionが2028年9月15日に廃止予定と発表されました。

- 主な変更点や新機能  
代替としてEncryption at HostやCVM OSディスク暗号化の利用が推奨され、これらはより広範なOSサポートを提供します。

- 影響を受ける対象  
Azure Disk Encryptionを利用中のVMおよびストレージ管理者。

- 注意点  
廃止までにEncryption at Hostへの移行を計画し、互換性や運用影響を事前に検証してください。

情報源: https://azure.microsoft.com/updates?id=493779

**詳細**:

本アップデートは、Azure Disk Encryption (ADE) の2028年9月15日での廃止を告知し、より新しい暗号化技術であるEncryption at Host (EaH) への移行を推奨しています。ADEはVMのOSおよびデータディスクをBitLocker（Windows）やDM-Crypt（Linux）で暗号化する方式ですが、管理負荷やパフォーマンス面での課題がありました。一方、EaHはホストレベルでディスクI/Oを暗号化し、OSやアプリケーションに依存しないため、より広範なOSサポートとシームレスな暗号化を実現します。実装はAzureポータルやCLIでVMの暗号化設定を切り替えるだけで完了し、既存のキー管理はAzure Key Vaultと連携可能です。活用シナリオとしては、規制準拠やデータ保護強化を目的に、運用中VMの暗号化を簡素化しつつパフォーマンス低下を抑えたいケースが挙げられます。注意点として、EaHは一部の古いVMシリーズで非対応のため事前検証が必要であり、ADE廃止後はセキュリティ更新が提供されません。関連サービスとしてAzure Key Vaultによるキー管理、Azure Security Centerによる暗号化状態の監視が連携可能で、包括的なセキュリティ運用を支援します。

---


*このレポートは自動生成されました - 2025-09-25 12:01:27 JST*