# 2025年12月30日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年12月30日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Retirement: Deprecation of Custom Resource Providers

**公開日時**: 2025年12月29日 17:30:40 UTC
**リンク**: [Retirement: Deprecation of Custom Resource Providers](https://azure.microsoft.com/updates?id=513892)

**アップデートID**: 513892
**情報源**: Azure Updates API

**カテゴリ**: Management and governance, Azure Resource Manager, Retirements

**要約**:

- 何が更新されたか  
Azure Resource ManagerのCustom Resource Provider（CuRP）サービスが2026年10月31日に廃止予定。

- 主な変更点や新機能  
CuRPの新規作成は2026年7月31日で停止。2025年10月27日にスクリームテストを実施予定。

- 影響を受ける対象  
CuRPを利用しているリソース管理や拡張機能の開発者・運用者。

- 注意点  
廃止に伴い代替手段の検討が必要。スクリームテストで影響を事前確認推奨。

**詳細**:

本アップデートは、Azure Resource Manager（ARM）におけるCustom Resource Provider（CuRP）サービスの廃止を告知するものです。CuRPはユーザー独自のリソースタイプをARMに統合し、カスタムAPIを通じて管理可能にする機能でしたが、2026年10月31日をもって完全廃止されます。2025年10月27日にスクリームテスト（影響検証）が実施され、2026年7月31日以降は新規リソース作成が停止されます。CuRPはREST APIを用いてカスタムリソースのCRUD操作を実装し、AzureポータルやARMテンプレートから一元管理を可能にしていました。主にオンプレミスやサードパーティ製品のリソースをAzure管理下に置くシナリオで活用されていましたが、Azure ArcやAzure Managed Applicationsなどの代替技術への移行が推奨されます。廃止に伴い、CuRPに依存する自動化やデプロイメントは事前に移行計画を策定し、Azure PolicyやAzure Blueprintsなどの標準機能を活用する必要があります。関連サービスとしてはARM、Azure Arc、Azure Policyが挙げられ、これらを組み合わせることでカスタムリソース管理の代替手段を構築可能です。

---


*このレポートは自動生成されました - 2025-12-30 12:01:07 JST*