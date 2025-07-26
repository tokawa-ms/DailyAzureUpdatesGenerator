# 2025年07月26日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年07月26日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Generally Available: ExpressRoute - Auto-assigned Public IP for ExpressRoute Gateways

**公開日時**: 2025年07月25日 10:45:12 UTC
**リンク**: [Generally Available: ExpressRoute - Auto-assigned Public IP for ExpressRoute Gateways](https://azure.microsoft.com/updates?id=498361)

**アップデートID**: 498361
**情報源**: Azure Updates API

**カテゴリ**: Launched, Hybrid + multicloud, Networking, Azure ExpressRoute, Features, Security

**要約**:

- 何が更新されたか  
ExpressRouteのVirtual Network Gatewayで、自動割り当てのパブリックIPがGA（一般提供）となりました。

- 主な変更点や新機能  
新規作成時にパブリックIPの手動割り当てが不要となり、ゲートウェイ構成が簡素化されます。

- 影響を受ける対象  
新規にExpressRouteゲートウェイをデプロイする技術者や運用者。

- 注意点があれば記載  
既存ゲートウェイには影響なく、手動割り当ても引き続き可能です。自動割り当てIPの管理方法を理解しておく必要があります。

**詳細**:

本アップデートは、ExpressRoute仮想ネットワークゲートウェイのパブリックIPアドレス割り当てを自動化することで、構成の簡素化と展開効率の向上を目的としています。従来はゲートウェイ作成時にユーザーが明示的にパブリックIPを用意し割り当てる必要がありましたが、新規作成されるExpressRouteゲートウェイはAzure側で自動的にパブリックIPが割り当てられます。これにより、IP管理の手間が削減され、デプロイメントの自動化やIaC（Infrastructure as Code）運用が容易になります。技術的には、ゲートウェイ作成APIやARMテンプレートでパブリックIP指定を省略可能となり、Azure内部で動的にIPプールから割当てが行われます。利用シナリオとしては、ExpressRoute接続の迅速なセットアップやスケールアウト時のIP管理負荷軽減が挙げられます。一方、IPアドレスの固定化が必要な場合は従来通り手動割当も可能であり、IPアドレスの変更リスクを考慮する必要があります。関連サービスとしては、Azure Virtual Network、ExpressRoute回線、Azure MonitorによるIP変更の監視連携が有効です。今回の自動割当機能は新規ゲートウェイに適用され、既存ゲートウェイには影響しません。

---

### 2. Public Preview: Modernizing Azure Resource Manager Throttling for Sovereign Clouds

**公開日時**: 2025年07月25日 10:30:26 UTC
**リンク**: [Public Preview: Modernizing Azure Resource Manager Throttling for Sovereign Clouds](https://azure.microsoft.com/updates?id=498893)

**アップデートID**: 498893
**情報源**: Azure Updates API

**カテゴリ**: Launched, Management and governance, Azure Resource Manager, Features, Management

**要約**:

- 何が更新されたか  
Azure Resource Manager（ARM）のスロットリング制御が、パブリッククラウドとソブリン（政府・特定地域）クラウド間で統一されるモダナイズ計画のパブリックプレビューを開始。

- 主な変更点や新機能  
2026年末までに両環境で同一のスロットリングポリシーを適用し、一貫したAPI制限管理を実現。

- 影響を受ける対象  
ソブリンクラウドを利用するAzure管理者や開発者。API呼び出しの制限挙動がパブリッククラウドと同様になる。

- 注意点があれば記載  
現状のソブリンクラウド特有のスロットリング挙動が変わるため、運用や自動化スクリプトの影響を事前に検証することが推奨される。

**詳細**:

本アップデートは、Azure Resource Manager（ARM）のスロットリング制御をパブリッククラウドとソブリン（主権）クラウド間で統一し、2026年末までに機能の均一化を図るものです。背景には、ソブリンクラウド環境でのAPIリクエスト制限がパブリッククラウドと異なり、運用効率や開発者体験に差異が生じていた点があります。具体的には、API呼び出しのスロットリングポリシーを共通化し、リクエストのレート制限やバースト制御のアルゴリズムを統一。これにより、ソブリンクラウドでもパブリッククラウドと同様のスロットリング挙動が得られ、アプリケーションの移植性と予測可能性が向上します。技術的には、ARMのスロットリングロジックを共通コードベースに統合し、クラウド環境ごとのパラメータ調整を可能にする設計が採用されています。活用例としては、グローバルに展開するマルチクラウドアプリケーションが、環境差異を意識せずにAPI呼び出しを最適化できる点が挙げられます。注意点としては、現行のソブリンクラウド固有のスロットリング挙動が変更されるため、既存運用ルールや自動化スクリプトの見直しが必要になる場合があります。関連サービスとしては、Azure MonitorやAzure Advisorと連携し、スロットリング発生時のログ収集や推奨設定の提示が強化される予定です。詳細は公式ドキュメントを参照してください。

---

### 3. Generally Available: Search Job Enhancements in Log Analytics 

**公開日時**: 2025年07月25日 10:30:26 UTC
**リンク**: [Generally Available: Search Job Enhancements in Log Analytics ](https://azure.microsoft.com/updates?id=498462)

**アップデートID**: 498462
**情報源**: Azure Updates API

**カテゴリ**: Launched, DevOps, Management and governance, Azure Monitor, Features

**要約**:

- 何が更新されたか  
Log AnalyticsのSearch Job機能がGA（一般提供）となり、非同期クエリの実行が安定提供開始。

- 主な変更点や新機能  
長期保持データを含む任意のデータに対し非同期クエリが可能に。結果は新しいAnalyticsテーブルとしてワークスペース内に保存され、後続クエリで活用可能。

- 影響を受ける対象  
Log Analyticsを利用し大規模・長期データ分析を行う技術者や運用チーム。

- 注意点があれば記載  
非同期処理のためクエリ完了まで待機が必要。結果のテーブル管理に注意が必要。  

情報源: https://azure.microsoft.com/updates?id=498462

**詳細**:

Azure Log Analyticsの「Search Job」機能がGA（一般提供）となりました。Search Jobは、Log Analyticsワークスペース内のデータ全体（長期保持データを含む）に対して非同期クエリを実行し、その結果を新たなAnalyticsテーブルとして保存可能にする機能です。これにより、大量データの長期分析や複雑なクエリの分割実行が容易になります。実装は非同期ジョブとしてバックグラウンドで処理され、完了後に結果テーブルが生成されるため、後続のクエリで効率的に再利用可能です。活用例としては、セキュリティインシデントの長期トレンド分析や、複数期間のログ比較分析が挙げられます。注意点として、Search Jobの実行にはリソース制限や実行時間制限が存在し、結果テーブルの管理も必要です。また、Azure MonitorやAzure Sentinelと連携することで、検出ルールやアラートの高度化に寄与します。これにより、運用効率の向上と高度な分析基盤の構築が可能となります。

---


*このレポートは自動生成されました - 2025-07-26 12:01:15 JST*