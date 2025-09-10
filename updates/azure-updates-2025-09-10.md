# 2025年09月10日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月10日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Private Preview: Azure AMD-based Dasv7, Easv7, and Fasv7-series Virtual Machines

**公開日時**: 2025年09月09日 20:45:15 UTC
**リンク**: [Private Preview: Azure AMD-based Dasv7, Easv7, and Fasv7-series Virtual Machines](https://azure.microsoft.com/updates?id=500175)

**アップデートID**: 500175
**情報源**: Azure Updates API

**カテゴリ**: In development, Compute, Linux Virtual Machines, Windows Virtual Machines, Pricing & Offerings, Services

**要約**:

- 何が更新されたか  
AzureのAMDベースのDasv7、Easv7、Fasv7シリーズVMがプライベートプレビューで提供開始。

- 主な変更点や新機能  
一般用途（Dasv7/Dalsv7）、メモリ最適化（Easv7）、計算最適化（Fasv7系）VMがローカルディスク有無で利用可能に。  

- 影響を受ける対象  
Azure VMを利用する開発者・運用者で、AMDベースの新VMを検討する技術者。  

- 注意点があれば記載  
現時点はプライベートプレビューのため、利用には申請が必要。対応リージョンはEast US 2、North Europe、West US 3に限定。

**詳細**:

本アップデートは、AMDベースの新世代VMシリーズ（Dasv7/Dalsv7：汎用、Easv7：メモリ最適化、Fasv7/Falsv7/Famsv7：コンピュート最適化）をプライベートプレビューとして提供開始したものです。これらVMは、従来のIntelベースVMに比べコストパフォーマンスに優れ、最新のAMD EPYCプロセッサを搭載し、高いCPU性能と効率的なメモリ帯域を実現します。ローカルディスクの有無を選択可能で、ストレージ要件に柔軟に対応可能です。対応リージョンはEast US 2、North Europe、West US 3です。VMの展開はAzureポータルやARMテンプレート、CLIから可能で、既存のVMスケールセットやAzure Monitor等と連携しやすい設計です。活用例としては、コスト重視のWebサーバー、メモリ集約型のデータ処理、CPU負荷の高いバッチ処理など多様なワークロードに適しています。注意点としては、現時点でプレビューのため、リージョンとSKUが限定されており、SLAやサポート範囲が正式リリース時と異なる可能性があります。Azure Disk Storageやネットワーク機能との互換性は既存VMと同等で、Azure BackupやAzure Security Centerなどの管理サービスも利用可能です。

---

### 2. Generally Available: Multitenant Managed Logging in Container Insights

**公開日時**: 2025年09月09日 16:30:49 UTC
**リンク**: [Generally Available: Multitenant Managed Logging in Container Insights](https://azure.microsoft.com/updates?id=502561)

**アップデートID**: 502561
**情報源**: Azure Updates API

**カテゴリ**: Launched, DevOps, Management and governance, Azure Monitor, Features, Management

**要約**:

- 何が更新されたか  
Container Insightsのマルチテナント管理ログ機能がGA（一般提供）となりました。

- 主な変更点や新機能  
共有AKSクラスター内でチームごとにコンテナログを分離・管理可能になり、各チームが独立してログの閲覧・運用が行えます。

- 影響を受ける対象  
複数チームで共有AKSクラスターを運用する組織やSaaS事業者。

- 注意点があれば記載  
ログ分離設定の適切な権限管理が必要です。  

https://azure.microsoft.com/updates?id=502561

**詳細**:

Azure Container Insightsの「Multitenant Managed Logging」機能がGA（一般提供）となりました。本機能は、共有AKSクラスター環境で複数チームが同一クラスターを利用する際に、コンテナログをチーム単位で分離・管理可能にするものです。具体的には、ログデータをチームごとに論理的に分割し、アクセス制御や管理を独立して行えるため、運用効率とセキュリティが向上します。技術的には、Azure MonitorのLog Analyticsワークスペースに対し、チーム別のスコープやフィルターを設定し、ログ収集時にタグ付けやラベル付けを行うことで実現しています。これにより、チームごとに専用のクエリやアラート設定が可能です。活用例としては、大規模組織で複数開発チームが同一AKSクラスターを利用しつつ、ログの混在を防ぎつつ個別分析やトラブルシューティングを行うケースが挙げられます。注意点としては、適切なRBAC設定とタグ管理が必須であり、誤設定によるログの漏洩や管理混乱を防ぐ必要があります。また、Log Analyticsの料金体系やデータ保持ポリシーも考慮が必要です。関連サービスとしては、Azure Monitor、Azure RBAC、Azure Policyと連携し、統合的な監視・管理体制を構築可能です。

---

### 3. Retirement: Microsoft Playwright Testing (Preview) will be retired on March 8, 2026

**公開日時**: 2025年09月09日 11:15:09 UTC
**リンク**: [Retirement: Microsoft Playwright Testing (Preview) will be retired on March 8, 2026](https://azure.microsoft.com/updates?id=499860)

**アップデートID**: 499860
**情報源**: Azure Updates API

**カテゴリ**: Developer tools, DevOps, Web, Microsoft Playwright Testing, Retirements

**要約**:

- 何が更新されたか  
Microsoft Playwright Testing (Preview) が2026年3月8日に廃止予定と発表されました。

- 主な変更点や新機能  
Azure App TestingとしてAzure Load TestingとPlaywright Testingを統合していましたが、Playwright Testing部分のサポート終了です。

- 影響を受ける対象  
Playwright Testingを利用している開発者やQAチーム。

- 注意点があれば記載  
廃止までに代替手段の検討と移行計画を推奨します。

**詳細**:

本アップデートは、Microsoft Playwright Testing（プレビュー版）が2026年3月8日に廃止されることを通知するものです。背景には、2023年8月に発表されたAzure App Testingの統合方針があり、Azure Load TestingとPlaywright Testingの機能を一元化して開発・QAチームの大規模な機能・性能テストを効率化する狙いがあります。Playwright Testingはブラウザ自動操作によるエンドツーエンドテストを提供していましたが、Azure App Testingに統合されることで、より包括的なテスト管理が可能となります。技術的には、Playwrightのスクリプト作成・実行環境がAzure App Testingに移行し、APIやUIも統合されるため、既存のPlaywrightテストは移行計画に沿ってAzure App Testingへ移行が推奨されます。活用シナリオとしては、Webアプリケーションのクロスブラウザ検証や負荷テストの組み合わせによる品質保証が挙げられます。注意点として、廃止後はPlaywright Testing単体のサービス利用ができなくなるため、移行期間中にテスト資産の移行と動作検証を行う必要があります。関連サービスとしてAzure DevOpsやGitHub Actionsと連携し、CI/CDパイプライン内での自動テスト実行が可能です。詳細は公式ドキュメントおよび移行ガイドを参照してください。

---


*このレポートは自動生成されました - 2025-09-10 12:01:20 JST*