# 2025年08月01日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年08月01日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Generally Available: Live Resize for Premium SSD v2 and Ultra NVMe Disks

**公開日時**: 2025年07月31日 17:15:08 UTC
**リンク**: [Generally Available: Live Resize for Premium SSD v2 and Ultra NVMe Disks](https://azure.microsoft.com/updates?id=495106)

**アップデートID**: 495106
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Disk Storage, Features

**要約**:

- 何が更新されたか  
Premium SSD v2およびUltra NVMeディスクのライブリサイズ機能がGA（一般提供）となりました。

- 主な変更点や新機能  
稼働中のディスク容量をアプリケーション停止なしで動的に拡張可能。コスト最適化に寄与します。

- 影響を受ける対象  
Premium SSD v2およびUltra NVMeディスクを利用するAzureユーザー。

- 注意点があれば記載  
リサイズ時は容量拡張のみ対応し、縮小はサポートされていません。アプリケーションの対応も確認が必要です。

**詳細**:

本アップデートは、Premium SSD v2（Pv2）およびUltra NVMeディスクに対する「ライブリサイズ」機能の一般提供開始を発表するものです。これにより、稼働中の仮想マシンに対してディスク容量をオンラインで拡張可能となり、アプリケーションの停止や再起動を伴わずにストレージ増強が行えます。技術的には、Azureのストレージ基盤が動的にディスクサイズ変更を反映し、OS側のパーティション拡張はユーザー側で実施可能です。Pv2およびUltra NVMeは高性能ストレージであり、ライブリサイズによりコスト最適化と柔軟なリソース管理が可能です。主な活用例としては、データベースの容量増加やログ収集環境の拡張が挙げられます。注意点として、縮小はサポートされず、拡張後のパフォーマンス特性やIOPS上限にも留意が必要です。また、Azure VMの種類やOSによっては追加の設定や再スキャン操作が必要となる場合があります。Azure MonitorやAzure Automationと連携し、容量監視や自動拡張運用も実現可能です。詳細は公式ドキュメントを参照してください。

---

### 2. Generally Available: Azure Virtual Network Manager in Azure US Government Cloud

**公開日時**: 2025年07月31日 17:00:19 UTC
**リンク**: [Generally Available: Azure Virtual Network Manager in Azure US Government Cloud](https://azure.microsoft.com/updates?id=499387)

**アップデートID**: 499387
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Azure Virtual Network Manager, Regions & Datacenters, Security, Services, Pricing & Offerings, Management, Features

**要約**:

- 何が更新されたか  
Azure Virtual Network ManagerがAzure US Government Cloudで一般提供開始。

- 主な変更点や新機能  
サブスクリプションやリージョン、テナントを跨いだネットワーク接続、セキュリティ、ルーティングの一元管理と自動化が可能に。

- 影響を受ける対象  
政府機関向けAzure環境で大規模ネットワーク管理を行う技術者。

- 注意点があれば記載  
ポリシーの一貫性維持により運用ミスを低減できるが、初期設定の設計が重要。

**詳細**:

Azure Virtual Network Manager（VNet Manager）がAzure US Government Cloudで一般提供（GA）となりました。本サービスは、複数サブスクリプションやリージョン、テナントにまたがるネットワーク接続、セキュリティ、ルーティングの一元管理を実現します。従来、個別設定が必要だったVNet間のポリシーやルート設定を自動化・統一し、構成の一貫性と運用効率を向上させることが目的です。技術的には、管理グループ単位でのポリシー適用や、セキュリティグループ、ルートテーブルの集中管理が可能で、Azure Resource Manager（ARM）テンプレートやAPIを用いた自動化もサポートします。活用シナリオとしては、政府機関の複数部門間でのセキュリティポリシー統一や、広域ネットワークのルーティング最適化が挙げられます。制限事項としては、対応リージョンやサービスの一部機能がUS Government Cloudに限定される点に注意が必要です。Azure FirewallやAzure Bastionなどのネットワークセキュリティサービスと連携し、包括的なネットワーク管理が可能です。詳細は公式ドキュメント参照を推奨します。

---

### 3. Public Preview: New tagging features in Azure confidential ledger

**公開日時**: 2025年07月31日 17:00:19 UTC
**リンク**: [Public Preview: New tagging features in Azure confidential ledger](https://azure.microsoft.com/updates?id=499382)

**アップデートID**: 499382
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Security, Storage, Azure confidential ledger, Features

**要約**:

- 何が更新されたか  
Azure Confidential Ledgerに新たにタグ機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
トランザクションごとに最大5つのタグを設定可能となり、データの分類・検索が容易に。タグはセカンダリキーとして機能し、コレクション内のデータ整理を強化します。

- 影響を受ける対象  
Confidential Ledgerを利用する開発者や運用担当者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に。タグの管理方法やパフォーマンス影響を事前に検証推奨。

**詳細**:

Azure Confidential Ledgerにおける新しいタグ機能は、データ管理の効率化を目的としてパブリックプレビューで提供開始されました。本機能は、各トランザクションに最大5つのタグを付与可能とし、これによりコレクション内のデータを二次的なキーで分類・検索しやすくします。技術的には、タグはトランザクションメタデータとして保存され、Confidential Ledgerの改ざん防止特性を維持しつつ高速なフィルタリングを実現します。実装はAzure SDKやREST APIを通じてタグの追加・検索が可能で、トランザクションの整合性を損なわずに運用できます。活用例としては、監査ログの種類別管理やマルチテナント環境でのトランザクション分類が挙げられ、運用負荷軽減に寄与します。一方、タグ数は最大5つに制限され、タグの内容は文字列でサイズ制限があるため設計時に注意が必要です。さらに、Azure Key VaultやAzure Monitorと連携することで、セキュアな鍵管理やログ監視と組み合わせた高度な運用が可能です。

---

### 4. Generally Available: Log or block shared access signature (SAS) tokens for Azure Storage based on expiration policy

**公開日時**: 2025年07月31日 17:00:19 UTC
**リンク**: [Generally Available: Log or block shared access signature (SAS) tokens for Azure Storage based on expiration policy](https://azure.microsoft.com/updates?id=498759)

**アップデートID**: 498759
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Storage Accounts, Security

**要約**:

- 何が更新されたか  
Azure StorageのSASトークンに対し、有効期限ポリシーに基づきトークンのログ記録またはブロックがGA（一般提供）された。

- 主な変更点や新機能  
管理者はSASトークンの最大有効期間を設定でき、期限切れトークンの使用をログまたはブロック可能に。セキュリティ強化と監査が容易に。

- 影響を受ける対象  
Azure Storageを利用し、SASトークン管理を行う運用者やセキュリティ担当者。

- 注意点  
既存のSASポリシー設定の見直しが必要で、適切な期限設定とポリシー運用が求められる。

**詳細**:

本アップデートは、Azure Storageの共有アクセス署名（SAS）トークンに対し、有効期限の上限を設定し、その期限切れに基づいてトークンのログ記録またはブロックを可能にする機能のGA提供を示します。従来、SASトークンの有効期間はポリシーで制御可能でしたが、期限切れトークンの利用監視や不正アクセス防止は限定的でした。本機能により、管理者はSAS有効期限ポリシーを設定し、期限超過のトークン使用を検知・拒否できるため、セキュリティ強化とコンプライアンス対応が容易になります。技術的には、ストレージアカウントのSAS expiration policyを設定し、期限切れトークンのアクセス試行時にログをAzure MonitorやAzure Storageの診断ログに記録、またはアクセスをブロックする仕組みです。活用例としては、長期間有効なSASトークンの誤用防止や、期限管理の自動化による運用負荷軽減が挙げられます。注意点として、既存のSASトークンはポリシー適用前に発行されたものは影響を受けず、ポリシー適用後の新規トークンに対してのみ有効です。また、Azure Blob、File、Queue、Tableストレージ全般で利用可能で、Azure MonitorやAzure Policyと連携し監査・運用管理を強化できます。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2025-08-01 12:01:24 JST*