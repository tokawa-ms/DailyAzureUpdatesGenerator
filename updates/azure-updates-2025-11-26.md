# 2025年11月26日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年11月26日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Generally Available: Model Context Protocol support in Azure API Management and Azure API Center 

**公開日時**: 2025年11月25日 20:30:17 UTC
**リンク**: [Generally Available: Model Context Protocol support in Azure API Management and Azure API Center ](https://azure.microsoft.com/updates?id=491990)

**アップデートID**: 491990
**情報源**: Azure Updates API

**カテゴリ**: In preview, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build, Features

**要約**:

- 何が更新されたか  
Azure API ManagementとAzure API CenterでModel Context Protocol（MCP）が一般提供開始（GA）されました。

- 主な変更点や新機能  
MCP対応により、既存APIを動的かつエージェント対応可能なツールに変換可能。APIのセキュリティ強化と運用の簡素化が実現します。

- 影響を受ける対象  
API管理や統合を行うエンタープライズの開発者・運用者。

- 注意点があれば記載  
プレビューからGAへの移行に伴い、安定性とサポートが向上していますが、既存環境での動作検証を推奨します。

**詳細**:

本アップデートは、Azure API Management（APIM）およびAzure API CenterにModel Context Protocol（MCP）サポートをGA（一般提供）したものです。MCPはAPIとAIモデル間の連携を標準化し、既存APIを動的かつエージェント対応可能なインターフェースへと進化させます。これにより、API呼び出し時にモデルコンテキスト情報を付与し、AIベースの解析や応答生成が容易になります。技術的には、APIMがMCPメッセージ形式を解釈し、APIリクエストにモデル関連メタデータを注入、Azure API CenterはAPIカタログ管理にMCP対応を組み込みます。活用例としては、チャットボットやインテリジェントエージェントがAPI経由でリアルタイムにモデル情報を取得し、精度の高い応答を生成するケースが挙げられます。注意点として、MCP対応APIは対応クライアントが必要であり、既存APIの設計変更やセキュリティポリシー調整が求められる場合があります。Azure Cognitive ServicesやAzure OpenAI Serviceとの連携により、モデルの高度な活用が可能です。詳細は公式ドキュメント参照を推奨します。

---

### 2. Public Preview: Managed Identity support in Network Watcher VNET flow log, traffic analytics and packet capture

**公開日時**: 2025年11月25日 16:45:50 UTC
**リンク**: [Public Preview: Managed Identity support in Network Watcher VNET flow log, traffic analytics and packet capture](https://azure.microsoft.com/updates?id=534482)

**アップデートID**: 534482
**情報源**: Azure Updates API

**カテゴリ**: In preview, Management and governance, Networking, Network Watcher

**要約**:

- 何が更新されたか  
Network WatcherのVNETフローログ、Traffic Analytics、パケットキャプチャでマネージドIDがパブリックプレビュー対応。

- 主な変更点や新機能  
これにより、Azure Storageへのログ保存やTraffic Analyticsのデータ収集時にマネージドIDを使った認証が可能となり、セキュリティと運用管理が簡素化。

- 影響を受ける対象  
VNETフローログやTraffic Analytics、パケットキャプチャを利用しているネットワーク管理者やセキュリティエンジニア。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に。マネージドIDの設定が必須。

**詳細**:

本アップデートは、Network WatcherのVNETフローログ、Traffic Analytics、パケットキャプチャ機能に対してマネージドID（Managed Identity）による認証サポートをパブリックプレビューで提供開始したものです。従来はストレージアカウントへのアクセスにサービスプリンシパルやキー管理が必要でしたが、マネージドIDを利用することで認証管理が簡素化され、セキュリティと運用効率が向上します。VNETフローログはVNET、サブネット、NIC間のIPトラフィックをキャプチャし、Azure Storageに保存。Traffic Analyticsはこれらのログを集約・解析し、ネットワークのパフォーマンス監視や異常検知に活用します。マネージドIDはAzure ADと連携し、Network Watcherリソースに割り当てられたIDがストレージアカウントのアクセス権限を取得する仕組みです。設定はAzureポータルやCLIでNetwork Watcherの設定時にマネージドIDを有効化し、ストレージアカウントのアクセス制御（IAM）で適切なロール割当を行います。活用例としては、運用チームがキー管理不要で安全にフローログを収集・分析し、ネットワーク障害の迅速な特定やセキュリティ監査を実現可能です。注意点としては、マネージドID利用時は対応リージョンやストレージアカウントの種類に制限がある場合があるため、事前確認が必要です。また、既存の認証方式との併用は可能ですが、切り替え時の権限設定に注意が必要です。本機能はNetwork Watcher、Azure Storage、Azure AD、Traffic Analyticsと密接に連携し、より安全かつ効率的なネットワーク監視基盤の構築を支援します。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2025-11-26 12:01:24 JST*