# 2025年08月22日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年08月22日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Generally Available: Application Gateway adds MaxSurge support for zero-capacity-impact upgrades

**公開日時**: 2025年08月21日 17:00:04 UTC
**リンク**: [Generally Available: Application Gateway adds MaxSurge support for zero-capacity-impact upgrades](https://azure.microsoft.com/updates?id=501017)

**アップデートID**: 501017
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Application Gateway, Features

**要約**:

- 何が更新されたか  
Azure Application GatewayがMaxSurgeをサポートし、ローリングアップグレード時に既存インスタンスを停止せずに新インスタンスを追加可能に。

- 主な変更点や新機能  
アップグレード中も容量低下なしで新バージョンへ移行可能となり、サービスの継続性と可用性が向上。

- 影響を受ける対象  
Application Gatewayを利用するシステム全般。

- 注意点があれば記載  
アップグレード時のリソース消費増加に注意し、適切なスケーリング設定を推奨。

**詳細**:

Azure Application GatewayがMaxSurge対応でゼロキャパシティ影響のローリングアップグレードを実現しました。本アップデートの背景は、従来のアップグレード時に既存インスタンスが一時的に停止し、サービスのスループット低下や接続障害が発生する課題を解消することにあります。MaxSurge機能により、新バージョンのインスタンスを既存の稼働インスタンスに加えて並行してプロビジョニングし、段階的にトラフィックを切り替えることで、アップグレード中も常に十分なキャパシティを維持可能です。技術的には、Azureのローリングデプロイメント機構を活用し、最大許容オーバーキャパシティ（MaxSurge）を設定することで、インスタンス数の一時的増加を許容しつつ段階的な入れ替えを実現しています。これにより、ミッションクリティカルなWebアプリケーションやAPIの継続稼働が求められる環境でのバージョンアップが容易になります。活用シナリオとしては、トラフィックが多い本番環境でのApplication Gatewayバージョンアップやセキュリティパッチ適用時に、サービス停止を伴わずに実施可能です。注意点としては、MaxSurge設定により一時的にインスタンス数が増加するため、リソースコストやスケーリング制限を考慮する必要があります。また、リージョンやSKUによって対応状況が異なる場合があるため、事前確認が推奨されます。関連サービスとしては、Azure Monitorでアップグレード状況やパフォーマンスを監視し、Azure DevOpsやAzure CLIを用いた自動化運用と組み合わせることで、効率的な運用が可能です。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 2. Generally, Available: Search Job in Log Analytics - Now Supporting Up to 100 Million Results

**公開日時**: 2025年08月21日 16:45:10 UTC
**リンク**: [Generally, Available: Search Job in Log Analytics - Now Supporting Up to 100 Million Results](https://azure.microsoft.com/updates?id=500879)

**アップデートID**: 500879
**情報源**: Azure Updates API

**カテゴリ**: Launched, DevOps, Management and governance, Azure Monitor, Features

**要約**:

- 何が更新されたか  
Log AnalyticsのSearch Job機能がGAとなり、最大1億件の結果取得をサポート開始。

- 主な変更点や新機能  
非同期クエリで長期保持データも含め全ワークスペースを検索可能に。結果は新しいAnalyticsテーブルで詳細分析可能。

- 影響を受ける対象  
大規模ログ分析を行うAzure Log Analyticsユーザー。

- 注意点  
大量データ取得時のパフォーマンスやコストに注意が必要。  

情報源: https://azure.microsoft.com/updates?id=500879

**詳細**:

Azure Log AnalyticsのSearch Job機能がGAとなり、最大1億件の結果取得をサポートしました。Search Jobは非同期クエリ実行を可能にし、ワークスペース内のリアルタイムデータだけでなく長期保存データも横断的に検索可能です。結果は新設のAnalyticsテーブルに格納され、Power BIやKustoクエリでの二次分析が容易になります。従来の同期クエリの制限（数百万件程度）を大幅に超え、大規模ログ解析やセキュリティ調査、運用監視に適しています。実装はAzure Monitorのバックエンドで非同期処理を行い、結果をテーブル形式で永続化する仕組みです。活用例としては、膨大なログから特定イベントの抽出や異常検知、長期間のトレンド分析が挙げられます。注意点としては、結果件数増加に伴うストレージコストやクエリ実行時間の増加があるため、適切なフィルタリング設計が必要です。Azure Data ExplorerやAzure Sentinelとの連携により、より高度な分析やセキュリティインシデント対応が可能となります。詳細は公式アップデート（https://azure.microsoft.com/updates?id=500879）を参照してください。

---

### 3. Generally Available: Azure NetApp Files file access logs

**公開日時**: 2025年08月21日 16:30:27 UTC
**リンク**: [Generally Available: Azure NetApp Files file access logs](https://azure.microsoft.com/updates?id=500760)

**アップデートID**: 500760
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure NetApp Files, Features, SDK and Tools, Regions & Datacenters, Services

**要約**:

- 何が更新されたか  
Azure NetApp Filesのファイルアクセスログ機能が一般提供（GA）となりました。

- 主な変更点や新機能  
SMB、NFSv4.1、デュアルプロトコルボリュームのファイル単位操作を詳細にログ取得可能となり、セキュリティ監査やトラブルシューティングが強化されます。

- 影響を受ける対象  
Azure NetApp Filesを利用する企業や技術者で、ファイルアクセスの可視化・監査を必要とする環境。

- 注意点  
ログの管理・保存に伴うコストやプライバシー保護の考慮が必要です。

**詳細**:

Azure NetApp Filesのファイルアクセスログ機能が一般提供（GA）となりました。本機能はSMB、NFSv4.1、及びデュアルプロトコルボリュームにおけるファイル単位の操作ログを取得可能とし、エンタープライズレベルの可視性を実現します。背景には、クラウド上のファイル共有に対するセキュリティ強化とコンプライアンス対応のニーズ増加があります。具体的には、ファイルの読み書き、削除、権限変更などの操作を詳細に記録し、ログはAzure MonitorやEvent Hubへ送信可能で、SIEMやカスタム分析ツールと連携できます。実装はAzure PortalやCLIからアクセスログの有効化を行い、ログ収集先を設定する形で簡便です。活用例としては、不正アクセス検知、操作履歴の監査、トラブルシューティングが挙げられます。注意点として、ログ収集はパフォーマンスに影響を与える可能性があるため、必要なボリュームに限定して有効化することが推奨されます。また、ログ保持期間やストレージコストも考慮が必要です。Azure Monitor、Event Hub、Log Analyticsとの連携により、統合的なセキュリティ運用や運用自動化が可能となります。

---

### 4. Generally Available: Azure Functions Flex Consumption plan now supports 512 MB instance size and diagnostic settings

**公開日時**: 2025年08月21日 15:30:02 UTC
**リンク**: [Generally Available: Azure Functions Flex Consumption plan now supports 512 MB instance size and diagnostic settings](https://azure.microsoft.com/updates?id=500369)

**アップデートID**: 500369
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features

**要約**:

- 何が更新されたか  
Azure Functions Flex Consumptionプランで、512MBメモリインスタンスサイズがGA対応し、診断設定もサポート開始。

- 主な変更点や新機能  
従来の2048MB・4096MBに加え、512MBを選択可能に。リソース消費が少ないアプリのコスト最適化とスケーリング効率向上が可能。

- 影響を受ける対象  
Flex Consumptionプランを利用するAzure Functions開発者。

- 注意点があれば記載  
小容量インスタンスはリソース制限が厳しいため、アプリの動作要件を確認の上選択を推奨。

**詳細**:

本アップデートにより、Azure FunctionsのFlex Consumptionプランで新たに512MBのメモリインスタンスサイズがGA（一般提供）されました。従来は2048MBおよび4096MBのみの選択肢でしたが、より軽量なワークロードに対してリソースを最適化し、コスト削減を図ることが可能となります。Flex Consumptionプランはコンテナベースでスケールし、メモリサイズの選択はアプリのパフォーマンスとコストに直結するため、512MBの追加は小規模な関数アプリに適しています。実装はAzure PortalやARMテンプレート、Azure CLIでメモリサイズパラメータを指定する形で行います。加えて、診断設定のサポートが強化され、ログやメトリクスの収集が容易になり、運用監視の効率化が期待されます。活用シナリオとしては、低負荷のイベント駆動型処理やバッチ処理、小規模APIのコスト効率化が挙げられます。注意点として、512MBインスタンスはリソース制約が厳しいため、メモリ使用量が多い関数には適しません。また、Flex ConsumptionプランはApp ServiceプランやPremiumプランとは異なるスケーリング特性を持つため、負荷変動を考慮した設計が必要です。関連サービスとしては、Azure Monitorとの連携で診断データの収集・分析が可能であり、Azure DevOpsやGitHub Actionsと組み合わせたCI/CDパイプライン構築時にも有効です。詳細は公式ドキュメントおよびアップデートページ（https://azure.microsoft.com/updates?id=500369）を参照してください。

---


*このレポートは自動生成されました - 2025-08-22 12:01:32 JST*