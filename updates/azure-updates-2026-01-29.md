# 2026年01月29日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年01月29日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Retirement: Support for Python 3.10 ends on October 1, 2026 – upgrade your Azure Functions apps to Python 3.13 

**公開日時**: 2026年01月28日 23:15:47 UTC
**リンク**: [Retirement: Support for Python 3.10 ends on October 1, 2026 – upgrade your Azure Functions apps to Python 3.13 ](https://azure.microsoft.com/updates?id=545771)

**アップデートID**: 545771
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, Internet of Things, Azure Functions

**要約**:

- 何が更新されたか  
Python 3.10のAzure Functionsサポートが2026年10月1日に終了します。

- 主な変更点や新機能  
以降はPython 3.10向けのセキュリティ更新やパフォーマンス改善が提供されません。Python 3.13へのアップグレードが推奨されます。

- 影響を受ける対象  
Python 3.10でAzure Functionsを運用している開発者・運用者。

- 注意点があれば記載  
サポート終了後もアプリは動作しますが、セキュリティリスクが高まるため早期のバージョンアップが必要です。

**詳細**:

本アップデートは、PythonコミュニティによるPython 3.10のサポート終了に伴い、Azure FunctionsにおけるPython 3.10のサポートも2026年10月1日をもって終了することを通知するものです。これにより、Python 3.10で構築されたAzure Functionsアプリは引き続き稼働しますが、セキュリティパッチやパフォーマンス改善の提供が停止されるため、脆弱性リスクや最適化不足が懸念されます。推奨される対応は、Python 3.13へのアップグレードであり、Azure Functionsのランタイム設定でPythonバージョンを明示的に指定し、ローカル環境やCI/CDパイプラインでの依存関係更新を行う必要があります。Python 3.13は最新の言語機能とパフォーマンス向上を備えており、Azure Functionsのイベント駆動型サーバーレスアーキテクチャにおいて、HTTPトリガーやタイマートリガーなど多様なシナリオで安定かつ効率的な動作を実現します。注意点として、Pythonバージョン変更に伴う依存パッケージの互換性検証や、Azure Functionsの拡張機能との整合性確認が必須です。さらに、Azure MonitorやApplication Insightsと連携し、アップグレード後の動作監視を強化することが望まれます。詳細は公式ドキュメントおよびアップデートページ（https://azure.microsoft.com/updates?id=545771）を参照してください。

---

### 2. Generally Available: Azure AMD Turin Dasv7, Easv7, and Fasv7-series Virtual Machines    

**公開日時**: 2026年01月28日 19:15:24 UTC
**リンク**: [Generally Available: Azure AMD Turin Dasv7, Easv7, and Fasv7-series Virtual Machines    ](https://azure.microsoft.com/updates?id=552318)

**アップデートID**: 552318
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Virtual Machines

**要約**:

- 何が更新されたか  
AzureのAMDベースTurinシリーズ（Dasv7、Dalsv7、Easv7、Fasv7など）の仮想マシンがGA（一般提供）となりました。

- 主な変更点や新機能  
汎用、メモリ最適化、コンピュート最適化の各VMがローカルディスクの有無で利用可能。性能向上とコスト効率が期待できます。

- 影響を受ける対象  
AMDプロセッサ搭載VMを利用するクラウド技術者やシステム設計者。

- 注意点があれば記載  
現時点で利用可能なリージョンはオーストラリア東部など限定的です。展開前に対応リージョンを確認してください。

**詳細**:

本アップデートにより、AMDベースのTurin世代Dasv7、Dalsv7（汎用）、Easv7（メモリ最適化）、Fasv7、Falsv7、Famsv7（コンピュート最適化）シリーズのAzure仮想マシンが一般提供（GA）されました。これらVMはローカルディスクの有無を選択可能で、オーストラリア東部や中央米国など複数リージョンで利用可能です。TurinシリーズはAMD EPYC 7003プロセッサを搭載し、高いコア数とメモリ帯域を提供、コストパフォーマンスに優れています。VMサイズはワークロードに応じて汎用からメモリ・コンピュート最適化まで幅広く選択可能で、オンプレミスからの移行やスケールアウトに適しています。ローカルディスク付きVMは一時ストレージとして高速I/Oを実現し、キャッシュやテンポラリデータ処理に有効です。Azure MonitorやAzure Backupとの連携も可能で運用管理が容易です。注意点として、ローカルディスクは永続ストレージではないため、重要データはAzure Managed DisksやAzure Filesに保存する必要があります。また、リージョン展開状況を事前確認し、VMサイズのSKU在庫制限に留意してください。これらVMは高性能かつコスト効率の良いAMDプラットフォームを活用したクラウド基盤構築に最適です。

---

### 3. Generally Available: Azure Databricks Agent Bricks Knowledge Assistant

**公開日時**: 2026年01月28日 18:45:08 UTC
**リンク**: [Generally Available: Azure Databricks Agent Bricks Knowledge Assistant](https://azure.microsoft.com/updates?id=542455)

**アップデートID**: 542455
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Analytics, Azure Databricks

**要約**:

- 何が更新されたか  
Azure Databricks上でAIエージェントを作成・展開・管理できる「Agent Bricks Knowledge Assistant」が一般提供開始。

- 主な変更点や新機能  
統合データとAI機能を活用し、事前構築されたコンポーネントでエージェント開発を簡素化。

- 影響を受ける対象  
Azure Databricksを利用するデータエンジニアやAI開発者。

- 注意点があれば記載  
既存のDatabricks環境に統合する際は、権限設定やリソース管理を適切に行う必要あり。

**詳細**:

本アップデート「Azure Databricks Agent Bricks Knowledge Assistant」は、Azure Databricks上でAIエージェントの作成・展開・管理を一元化し、データとAI機能を統合的に活用可能にすることを目的としています。これにより、従来複雑だったエージェント開発を簡素化し、事前構築されたコンポーネント（Bricks）を利用して迅速にAIエージェントを構築できます。技術的には、Databricksのノートブック環境にエージェント管理用のAPIとUIを統合し、Sparkベースの大規模データ処理とAzure Cognitive ServicesなどのAIモデルを連携させる仕組みです。具体的には、自然言語処理や対話型AIを活用したカスタマーサポートチャットボットやデータ分析支援エージェントの構築が可能です。利用時は、Databricksワークスペースの適切な権限設定やAIモデルのトレーニングデータ管理に注意が必要で、現時点では一部のリージョン限定で提供されています。Azure Cognitive Services、Azure Machine Learning、Azure Synapse Analyticsとの連携により、データ収集からモデル運用までのエンドツーエンドのAIワークフローを実現します。詳細は公式ドキュメントおよびリンク先を参照してください。

---

### 4. Generally Available: Latest PostgreSQL minor versions supported by Azure Database for PostgreSQL – Flexible Server  

**公開日時**: 2026年01月28日 17:00:53 UTC
**リンク**: [Generally Available: Latest PostgreSQL minor versions supported by Azure Database for PostgreSQL – Flexible Server  ](https://azure.microsoft.com/updates?id=550164)

**アップデートID**: 550164
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL – Flexible ServerでPostgreSQLの最新マイナーバージョン（18.1、17.7、16.11、15.15、14.20、13.23）がGA対応。

- 主な変更点や新機能  
これらのマイナーバージョンアップデートは、Azureの月次計画メンテナンス時に自動適用される。

- 影響を受ける対象  
Azure Database for PostgreSQL – Flexible Serverを利用中のユーザー。

- 注意点があれば記載  
自動アップデートにより互換性や動作確認が必要な場合は事前検証を推奨。

**詳細**:

本アップデートにより、Azure Database for PostgreSQL – Flexible ServerはPostgreSQLのマイナーバージョン18.1、17.7、16.11、15.15、14.20、13.23を正式サポートします。これらのマイナーバージョンはバグ修正やセキュリティパッチを含み、安定性とセキュリティの向上を目的としています。アップグレードはAzureの月次計画メンテナンス時に自動適用され、ユーザーの手動介入を不要とし、運用負荷を軽減します。技術的には、Flexible Serverのローリングアップデート機能を活用し、サービス停止時間を最小化しつつ安全に適用されます。活用シナリオとしては、既存のPostgreSQLワークロードの信頼性向上や最新のセキュリティ基準準拠が挙げられます。注意点として、マイナーバージョンアップは機能追加を伴わず、互換性は保たれますが、事前にテスト環境での動作確認を推奨します。関連サービスではAzure Monitorによるパフォーマンス監視やAzure Backupとの連携でデータ保護を強化可能です。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2026-01-29 12:01:34 JST*