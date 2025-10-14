# 2025年10月14日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年10月14日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Public Preview: Environmental sustainability features in Azure API Management

**公開日時**: 2025年10月13日 16:30:27 UTC
**リンク**: [Public Preview: Environmental sustainability features in Azure API Management](https://azure.microsoft.com/updates?id=513074)

**アップデートID**: 513074
**情報源**: Azure Updates API

**カテゴリ**: In preview, Integration, Internet of Things, Mobile, Web, API Management, Features

**要約**:

- 何が更新されたか  
Azure API Managementに環境持続可能性機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
APIトラフィックやポリシーの動作をカーボンフットプリントを意識して最適化し、APIインフラのCO2排出削減を支援します。

- 影響を受ける対象  
API管理を行う開発者や運用チーム。

- 注意点があれば記載  
パブリックプレビュー段階のため、本番環境での利用は慎重に検討してください。

情報源: https://azure.microsoft.com/updates?id=513074

**詳細**:

Azure API Managementのパブリックプレビューで提供開始された環境持続可能性機能は、APIインフラのカーボンフットプリント削減を目的としています。具体的には、APIトラフィックやポリシーの動作をカーボン排出量に配慮した形で管理可能とし、環境負荷の可視化と最適化を支援します。技術的には、API呼び出しごとの推定CO2排出量を計測し、ポリシーでのルーティングやスロットリングに反映可能です。これにより、環境負荷の高いリージョンや時間帯のトラフィックを制御し、より低炭素な運用が実現します。活用例としては、グローバルAPI配信におけるリージョン選択最適化や、ピーク時の負荷分散調整による排出削減が挙げられます。注意点としては、現状はプレビュー段階のため、計測精度や対応リージョンに制限があり、運用前の検証が必要です。Azure MonitorやAzure Cost Managementと連携し、環境データの統合分析も可能で、持続可能性を考慮したAPI運用の基盤強化に寄与します。

---

### 2. Public Preview: PostgreSQL 18 on Azure Database for PostgreSQL – Flexible Server 

**公開日時**: 2025年10月13日 16:00:05 UTC
**リンク**: [Public Preview: PostgreSQL 18 on Azure Database for PostgreSQL – Flexible Server ](https://azure.microsoft.com/updates?id=508403)

**アップデートID**: 508403
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL – Flexible ServerでPostgreSQL 18がパブリックプレビュー提供開始。  

- 主な変更点や新機能  
性能向上、スケーラビリティ強化、開発者生産性の改善が含まれる最新機能を早期に利用可能。  

- 影響を受ける対象  
PostgreSQLを利用する開発者や運用担当者、特に最新機能を試したい技術者。  

- 注意点があれば記載  
プレビュー版のため本番環境での利用は慎重に。正式リリース前の機能変更や不具合の可能性あり。

**詳細**:

Azure Database for PostgreSQL – Flexible Serverにおいて、PostgreSQL 18がパブリックプレビューとして利用可能になりました。本アップデートは、最新のPostgreSQL 18の性能向上、スケーラビリティ強化、開発者生産性改善をAzure環境で早期に体験可能にすることを目的としています。主な機能としては、クエリ処理の最適化、新しい並列処理機能、拡張可能なインデックス構造の追加、JSON処理の高速化が含まれます。Flexible Serverのマネージド環境により、スケーリングやバックアップ、セキュリティ設定が容易に行え、PostgreSQL 18の新機能を活かしたアプリケーション開発が可能です。実装はAzure PortalやCLIからサーバー作成時にバージョン指定する形で行い、既存環境からの移行もサポートされています。活用シナリオとしては、高負荷トランザクション処理や複雑な分析クエリを伴うWebアプリケーション、IoTデータのリアルタイム集計などが挙げられます。注意点としては、プレビュー版のため一部機能が制限される可能性があり、本番環境での利用は慎重に検討が必要です。Azure MonitorやAzure Security Centerとの連携により、運用監視やセキュリティ強化も可能です。詳細は公式ドキュメントおよびアップデートページを参照してください。

---

### 3. Retirement: Azure Custom Vision will be retired on September 25, 2028 

**公開日時**: 2025年10月13日 16:00:05 UTC
**リンク**: [Retirement: Azure Custom Vision will be retired on September 25, 2028 ](https://azure.microsoft.com/updates?id=502914)

**アップデートID**: 502914
**情報源**: Azure Updates API

**カテゴリ**: AI + machine learning, Azure AI Custom Vision, Retirements

**要約**:

- 何が更新されたか  
Azure Custom Visionサービスの廃止予定が発表されました。

- 主な変更点や新機能  
2028年9月25日をもってサービスが正式に終了します。  

- 影響を受ける対象  
既存のAzure Custom Vision利用者全員。  

- 注意点があれば記載  
廃止までサポートは継続されますが、早めに代替サービスや移行計画の検討を推奨します。  

情報源: https://azure.microsoft.com/updates?id=502914

**詳細**:

Microsoftは、Azure Custom Visionサービスを2028年9月25日をもって段階的に廃止することを発表しました。本アップデートの背景には、AI・機械学習分野の技術進化に伴うサービス統合や新機能への移行促進があり、既存ユーザーには2028年まで完全サポートが提供されます。Azure Custom Visionは、画像分類や物体検出モデルをノーコードで作成・トレーニング可能なサービスで、REST APIやSDKを通じてカスタムモデルのデプロイや推論が行えます。主な活用例は製造業の欠陥検出や小売業の画像解析などです。廃止に伴い、新規開発は推奨されず、MicrosoftはAzure Cognitive ServicesのVision系APIやAzure Machine Learningへの移行を推奨しています。既存モデルのエクスポートやAPI移行計画を早期に策定することが重要です。なお、Azure Custom VisionはAzure Blob StorageやAzure Functionsと連携し、画像データの管理や自動処理が可能でしたが、今後はこれらの連携も新サービスに置き換える必要があります。移行期間中の運用継続には十分な計画とテストが求められます。詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=502914）を参照してください。

---

### 4. Public Preview: Azure Integrated HSM

**公開日時**: 2025年10月13日 15:30:40 UTC
**リンク**: [Public Preview: Azure Integrated HSM](https://azure.microsoft.com/updates?id=503325)

**アップデートID**: 503325
**情報源**: Azure Updates API

**カテゴリ**: In preview, Security, Features, Services

**要約**:

- 何が更新されたか  
Azure Integrated HSMのパブリックプレビューが開始されました。

- 主な変更点や新機能  
仮想マシン内で動作するHSMキャッシュと暗号アクセラレータを提供し、暗号処理のセキュリティ強化とパフォーマンス向上を実現します。

- 影響を受ける対象  
暗号処理を多用するAzure仮想マシン利用者。

- 注意点  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure Integrated HSMは、仮想マシン内での暗号処理性能とセキュリティを強化するためのハードウェアセキュリティモジュール（HSM）キャッシュ兼暗号アクセラレータです。背景には、クラウド上での暗号化処理負荷増大とセキュリティ強化ニーズの高まりがあり、ソフトウェアベースの暗号処理では性能や鍵管理の面で限界があった点があります。本サービスはVM内に専用のHSMキャッシュを統合し、暗号演算を高速化すると同時に鍵の安全な保管と管理を実現します。実装はAzureの仮想化基盤に組み込まれ、VMからの暗号API呼び出しをHSMキャッシュがオフロード処理。これによりレイテンシ低減とスループット向上を達成します。主な活用例は、TLS終端処理やデータベース暗号化、ブロックチェーンノードなど高頻度暗号処理を要するアプリケーションです。注意点としては、現時点でプレビュー版のため利用可能リージョンやVMサイズに制限があり、対応OSや暗号ライブラリとの互換性確認が必要です。Azure Key VaultやAzure Confidential Computingと連携し、鍵管理ポリシーの一元化や機密データ保護強化が可能です。詳細は公式ドキュメントを参照し、適切な設計・検証を推奨します。

---

### 5. Generally Available: Microsoft Entra ID token refresh code samples in Python and .NET 

**公開日時**: 2025年10月13日 15:00:46 UTC
**リンク**: [Generally Available: Microsoft Entra ID token refresh code samples in Python and .NET ](https://azure.microsoft.com/updates?id=508413)

**アップデートID**: 508413
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
Microsoft Entra IDのトークンリフレッシュ用コードサンプルがPythonと.NETで一般提供開始。

- 主な変更点や新機能  
Azure Database for PostgreSQL接続時にEntra ID認証トークンを安全に管理するサンプルコードを提供。

- 影響を受ける対象  
Azure Database for PostgreSQLをEntra ID認証で利用する開発者。

- 注意点があれば記載  
トークン管理の実装に役立つが、セキュリティベストプラクティスに従うことが重要。

**詳細**:

本アップデートは、Azure Database for PostgreSQLにおけるMicrosoft Entra ID（旧Azure AD）認証トークンのリフレッシュ処理をPythonおよび.NETで実装するためのコードサンプルを一般提供（GA）したものです。背景には、Entra ID認証を用いたPostgreSQL接続時にアクセストークンの有効期限管理が必要であり、トークンの自動更新を安全かつ効率的に行う実装例が求められていた点があります。提供されるコードサンプルは、OAuth 2.0のリフレッシュトークンフローを活用し、アクセストークンの取得・更新をプログラム的に行う方法を示しています。具体的には、MSALライブラリを用いてトークンキャッシュ管理やリフレッシュ処理を実装し、PostgreSQL接続文字列に最新トークンを組み込む形で認証を維持します。活用シナリオとしては、長時間稼働するアプリケーションやバッチ処理での継続的なデータベース接続が挙げられ、トークン期限切れによる接続断を防止可能です。注意点としては、リフレッシュトークンの適切な保護やMSALのバージョン管理、PostgreSQLサーバー側のEntra ID統合設定が前提となることが挙げられます。また、Azure Key Vaultとの連携でトークン管理のセキュリティ強化も推奨されます。これにより、AzureのID管理とデータベース認証の連携がより堅牢かつ自動化され、運用負荷の低減が期待できます。詳細は公式ドキュメントおよびサンプルコードリポジトリを参照してください。

---


*このレポートは自動生成されました - 2025-10-14 12:01:46 JST*