# 2025年10月24日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年10月24日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Retirement: Azure Computer Vision – Image Analysis will be retired on September 25, 2028 

**公開日時**: 2025年10月23日 14:15:03 UTC
**リンク**: [Retirement: Azure Computer Vision – Image Analysis will be retired on September 25, 2028 ](https://azure.microsoft.com/updates?id=502909)

**アップデートID**: 502909
**情報源**: Azure Updates API

**カテゴリ**: AI + machine learning, Azure AI Foundry, Retirements

**要約**:

- 何が更新されたか  
Azure Computer VisionのImage Analysisサービスが2028年9月25日に廃止予定と発表されました。  

- 主な変更点や新機能  
新機能はなく、既存サービスのサポート終了予定の通知です。  

- 影響を受ける対象  
Image Analysis APIを利用している全ユーザーが対象です。  

- 注意点  
2028年9月25日まではサポート継続しますが、それ以降は利用不可となるため、代替サービスへの移行準備が必要です。

**詳細**:

本アップデートは、Azure Computer VisionのImage Analysis機能が2028年9月25日をもって段階的に廃止されることを告知するものです。背景には、より高度で統合的なビジョンサービスへの移行促進と、最新AIモデルへの対応強化が挙げられます。Image Analysisは画像のタグ付け、物体検出、テキスト抽出などをREST API経由で提供してきましたが、今後はAzure Cognitive ServicesのVision APIやCustom Visionなど、より柔軟かつ拡張性の高いサービスへの移行が推奨されます。技術的には既存APIのサポートは2028年まで継続されるものの、新規機能追加は停止されるため、長期運用を想定する場合は移行計画を早期に策定すべきです。活用シナリオとしては、画像分類やメタデータ生成、コンテンツモデレーションなどが主であり、Azure Blob StorageやLogic Apps、Power Automateとの連携による自動化も可能です。注意点として、廃止後はAPI呼び出しが停止し、サービスが利用不可となるため、依存するシステムの影響評価と代替サービスへの切替が必須です。関連サービスとの連携では、Computer Visionの新バージョンやCustom Vision、Form Recognizerとの組み合わせで高度な画像認識・解析ワークフローを構築可能です。詳細は公式ドキュメントを参照し、計画的な移行を推奨します。

---


*このレポートは自動生成されました - 2025-10-24 12:01:17 JST*