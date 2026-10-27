# 2026年10月27日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年10月27日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Generally Available: Network Watcher VNet flow logs filtering

**公開日時**: 2026年10月26日 16:02:05 UTC
**リンク**: [Generally Available: Network Watcher VNet flow logs filtering](https://azure.microsoft.com/updates?id=577782)

**アップデートID**: 577782
**情報源**: Azure Updates API

**カテゴリ**: Launched, Management and governance, Networking, Network Watcher, Features

**要約**:

【何が更新されたか】  
Azure Network WatcherのVNetフロー ログのフィルタリング機能が一般提供（GA）されました。

【主な変更点や新機能】  
これまでVNetフロー ログは全てのネットワークトラフィックを記録していましたが、今回のアップデートにより、IPアドレス、ポート、プロトコル、暗号化状態、フロー状態、トラフィック方向などの特定の条件に基づいてログをフィルタリングできるようになりました。これにより、不要なログを削減し、必要なトラフィックのみを効率的に監視・分析できます。

【影響を受ける対象】  
Azure Network Watcherを利用してVNetフロー ログを管理している技術者やネットワーク管理者が対象です。特に大量のトラフィックを扱う環境や、セキュリティ監視・トラブルシューティングを行う現場で有効です。

【注意点】  
フィルタリング条件の設定ミスにより、必要なトラフィックログが記録されない可能性があります。導入時はフィルタ条件を十分に検討し、監視要件に合致するよう設定してください。

**詳細**:

Azure Network Watcher VNet flow logs filtering is now generally available, enabling you to control which
network traffic flows are logged based on specific criteria such as IP
addresses, ports, protocols, encryption state, flow state, and traffic directio

---


*このレポートは自動生成されました - 2026-10-27 12:01:13 JST*