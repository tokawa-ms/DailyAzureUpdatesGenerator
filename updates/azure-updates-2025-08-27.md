# 2025年08月27日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年08月27日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Generally Available: Entra ID and RBAC support for GetAccountInfo and other supplemental APIs for Azure Storage

**公開日時**: 2025年08月26日 17:45:29 UTC
**リンク**: [Generally Available: Entra ID and RBAC support for GetAccountInfo and other supplemental APIs for Azure Storage](https://azure.microsoft.com/updates?id=496287)

**アップデートID**: 496287
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Blob Storage, Security

**要約**:

- 何が更新されたか  
Azure StorageのGetAccountInfoなど補助APIに対し、Entra IDとRBAC認可がGA（一般提供）されました。

- 主な変更点や新機能  
Get/Set Container、Queue、TableのACL操作がEntra ID認証とロールベースアクセス制御で管理可能に。

- 影響を受ける対象  
Azure Storageの管理APIを利用する開発者や運用担当者。

- 注意点があれば記載  
既存の認証方式からEntra IDとRBACへの移行計画を検討し、権限設定を適切に行う必要があります。

**詳細**:

本アップデートは、Azure Storageのセキュリティ強化を目的に、Entra ID（旧Azure AD）およびロールベースアクセス制御（RBAC）による認証・認可を「GetAccountInfo」などの補助API群に対して一般提供開始したものです。対象APIは、アカウント情報取得（GetAccountInfo）、コンテナ・キュー・テーブルのACL取得・設定API（Get/Set Container ACL、Get/Set Queue ACL、Get/Set Table ACL）で、これらが従来の共有キー認証からEntra ID認証に対応しました。これにより、Azure Storageリソースへのアクセス管理をAzure RBACポリシーで一元化可能となり、最小権限の原則に基づくセキュアな運用が実現します。技術的には、Azure Storage SDKやREST API呼び出し時にOAuth 2.0トークンを用いてEntra ID認証を行い、RBACロール割当てに基づきアクセス権限を検証します。活用例としては、複数ユーザーやサービス間での細かなアクセス制御、監査ログの一元管理、セキュリティポリシー準拠の強化が挙げられます。注意点として、RBAC対応API利用時は適切なロール割当てが必須であり、旧来の共有キー認証との併用時は権限管理の混在に留意が必要です。関連サービスとしては、Azure RBAC、Entra ID、Azure Monitor（監査ログ）、およびAzure Storage SDKが連携し、統合的なアクセス管理と監査を支援します。詳細は公式ドキュメントおよびリンク先を参照してください。

---

### 2. Public Preview: Custom block response code and body for Application Gateway WAF 

**公開日時**: 2025年08月26日 17:00:18 UTC
**リンク**: [Public Preview: Custom block response code and body for Application Gateway WAF ](https://azure.microsoft.com/updates?id=501323)

**アップデートID**: 501323
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Application Gateway, Web Application Firewall, Features

**要約**:

- 何が更新されたか  
Application Gateway統合WAFでブロック時のレスポンスコードとボディをカスタマイズ可能に（パブリックプレビュー開始）。

- 主な変更点や新機能  
ブロック応答のHTTPステータスコードやレスポンス内容を自由に設定でき、運用やユーザー通知の柔軟性が向上。

- 影響を受ける対象  
Application Gateway WAFを利用するAzureユーザー、特にセキュリティポリシーの応答制御が必要な技術者。

- 注意点  
プレビュー機能のため本番環境での利用は慎重に。設定ミスによる誤動作に注意。  

情報源: https://azure.microsoft.com/updates?id=501323

**詳細**:

Azure Application Gatewayに統合されたWAF（Web Application Firewall）において、ブロックされたリクエストに対するレスポンスのHTTPステータスコードおよびレスポンスボディをカスタマイズ可能とする機能がパブリックプレビューとして提供開始されました。本アップデートの背景には、標準のWAFブロックレスポンスが固定的であり、ユーザー体験やセキュリティ運用の柔軟性に制約があった点があります。これにより、攻撃検知時の応答を自社ポリシーやブランドに合わせて調整可能となり、セキュリティ通知やトラブルシューティングの効率化が期待されます。

具体的には、WAFポリシーの設定でブロック時のHTTPステータスコード（例：403、429など）を任意に指定でき、さらにカスタムHTMLやJSON形式のレスポンスボディを定義可能です。設定はAzure Portal、Azure CLI、ARMテンプレート、またはREST APIを通じて行います。技術的には、Application GatewayのWAFモジュールがブロック判定後に指定されたレスポンス情報を返す仕組みで、既存のWAFルールセットやポリシー管理とシームレスに連携します。

活用シナリオとしては、APIゲートウェイでのレート制限超過時に特定のJSONエラーメッセージを返す、あるいはWebアプリケーションでカスタムエラーページを表示するケースが挙げられます。これにより、ユーザーやクライアントアプリケーションに対してより明確な情報提供が可能となり、運用負荷の軽減にも寄与します。

注意点としては、プレビュー機能であるため本番環境での利用は慎重に行う必要があり、カスタムレスポンスのサイズや形式に制限がある点に留意してください。また、WAFの検知ロジック自体は変更されないため、誤検知時のレスポンスカスタマイズは根本的な問題解決にはならないことを理解する必要があります。

関連サービスとしては、Azure Front DoorやAzure Firewallなどのセキュリティ製品と組み合わせることで、多層防御戦略の一環として活用可能です。特に、Application Gatewayを通じたトラフィック管理とWAFの柔軟な応答設定により、より高度なセキュリティポリシーの実装が実現します。詳細は公式ドキュメントおよびAzureアップデートページ（https://azure.microsoft.com/updates?id=501323）を参照してください。

---

### 3. Generally Available: CNI Overlay for Application Gateway for Containers and AGIC

**公開日時**: 2025年08月26日 16:00:15 UTC
**リンク**: [Generally Available: CNI Overlay for Application Gateway for Containers and AGIC](https://azure.microsoft.com/updates?id=500991)

**アップデートID**: 500991
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Application Gateway, Services, Features

**要約**:

- 何が更新されたか  
Azure CNI OverlayがApplication Gateway for Containers（AGIC）対応で一般提供開始。

- 主な変更点や新機能  
AKSクラスタでポッドIPを別CIDRから割り当て可能にし、VNetのIP空間節約とマルチクラスタ運用を簡素化。

- 影響を受ける対象  
AKSでAGICを利用するコンテナアプリケーションのネットワーク設計担当者。

- 注意点があれば記載  
既存環境への適用時はIPアドレス管理とルーティング設定の見直しが必要。  

https://azure.microsoft.com/updates?id=500991

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）におけるネットワーク管理の効率化とスケーラビリティ向上を目的に、Application Gateway for Containers（AGIC）と連携可能なAzure CNI Overlay機能を一般提供開始したものです。Azure CNI Overlayは、PodのIPアドレスを既存VNetとは別のCIDRプールから割り当てることで、VNetのIPアドレス枯渇問題を緩和し、複数AKSクラスター間でのIPアドレス管理を簡素化します。技術的には、Overlayネットワークを用いてPod間通信を実現しつつ、AGICがApplication Gatewayを介してトラフィックを制御する構成をサポート。これにより、セキュアかつ柔軟なIngress管理が可能となります。活用例としては、大規模マルチクラスター環境でのIPアドレス重複回避や、マイクロサービス間のトラフィック最適化が挙げられます。注意点として、Overlayネットワークの設定には既存VNet構成との整合性確認が必要であり、一部古いAKSバージョンでは非対応です。関連サービスとしては、Azure Application Gateway、AGIC、Azure Monitorが連携し、トラフィック監視やセキュリティ強化に寄与します。詳細は公式ドキュメント参照推奨。

---

### 4. Public Preview: Azure NetApp Files short-term clones 

**公開日時**: 2025年08月26日 16:00:15 UTC
**リンク**: [Public Preview: Azure NetApp Files short-term clones ](https://azure.microsoft.com/updates?id=500914)

**アップデートID**: 500914
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure NetApp Files, Features, Services, SDK and Tools

**要約**:

- 何が更新されたか  
Azure NetApp Filesに短期クローン機能がパブリックプレビューで追加されました。

- 主な変更点や新機能  
既存のボリュームスナップショットから即時に薄型クローンを作成可能。フルコピー不要で容量節約と高速な読み書きアクセスを実現します。

- 影響を受ける対象  
開発・テスト環境や一時的なデータ利用を行うソフトウェア開発者や運用担当者。

- 注意点があれば記載  
現時点はパブリックプレビューのため、本番環境での利用は慎重に検討してください。

**詳細**:

Azure NetApp Filesの新機能「short-term clones」は、既存のボリュームスナップショットから一時的な薄型クローンを即座に作成し、読み書きアクセスを可能にするパブリックプレビュー機能です。従来のフルコピーを行わずに容量を大幅に節約できるため、開発・テスト環境やCI/CDパイプラインでの高速なデータ複製に最適です。技術的には、スナップショットの差分データを参照しつつ、変更部分のみを新規ストレージに書き込むコピーオンライト方式を採用。これにより、クローン作成が数秒で完了し、ストレージ消費を抑制します。利用時は短期間の使用を想定しており、長期間の保持には向かない点に注意が必要です。Azure NetApp FilesはAzure VMやKubernetesなどと連携しやすく、特にコンテナ環境での状態管理やマルチテナント開発環境の効率化に寄与します。管理はAzureポータルやCLIから可能で、既存のNetApp Filesボリュームに対して追加設定なく利用可能です。

---


*このレポートは自動生成されました - 2025-08-27 12:01:29 JST*