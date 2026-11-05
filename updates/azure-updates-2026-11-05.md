# 2026年11月05日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年11月05日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Generally Available: Azure Database for PostgreSQL stable REST API version 2026-10-01

**公開日時**: 2026年11月04日 18:42:12 UTC
**リンク**: [Generally Available: Azure Database for PostgreSQL stable REST API version 2026-10-01](https://azure.microsoft.com/updates?id=579300)

**アップデートID**: 579300
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Feature

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible ServerのREST APIバージョン「2026-10-01」が一般提供（GA）されました。

- 主な変更点や新機能  
この安定版APIでは、メンテナンス管理機能の拡張、イミュータブル（変更不可）バックアップのサポート、マルチテナント暗号化（クロステナントカスタム暗号化キー対応）などの新機能が追加されています。

- 影響を受ける対象  
Azure Database for PostgreSQL Flexible Serverを利用している技術者や、REST APIを活用して管理・運用を行っている開発者が対象となります。

- 注意点があれば記載  
新APIバージョンを利用する際は、既存のAPIバージョンとの互換性や、追加された機能の利用条件を事前に確認してください。また、APIの仕様変更により、既存の運用フローや自動化スクリプトへの影響がないか検証することを推奨します。

**詳細**:

Azure Database for PostgreSQL Flexible Server REST APIのバージョン2026-10-01が一般提供（GA）となりました。本アップデートは、APIの安定版リリースとして位置付けられており、主にメンテナンス管理機能の拡張、イミュータブルバックアップ、マルチテナント暗号化（クロステナントカスタム暗号化）などの新機能が導入されています。これにより、運用管理の効率化やセキュリティ強化、バックアップ運用の堅牢化などが実現されます。

メンテナンス管理機能の拡張では、APIを通じて柔軟なメンテナンススケジュール設定や管理が可能となり、サービスの可用性を維持しつつ計画的なアップデートやパッチ適用が実施できるようになります。イミュータブルバックアップ機能は、バックアップデータの改ざん防止を目的としており、API経由でバックアップの取得や管理を行う際に、データの整合性と保護を強化します。マルチテナント暗号化については、複数テナント環境においてクロステナントカスタム暗号化がサポートされることで、より高度なセキュリティ要件に対応できるようになります。

技術的な仕組みとしては、REST APIを利用した操作が中心となります。APIエンドポイントを介して、サーバーの設定変更やバックアップ管理、暗号化設定などをプログラムから直接制御することが可能です。これにより、インフラ自動化やDevOpsのワークフローに組み込むことができ、運用の効率化が図れます。

活用シナリオとしては、企業のデータベース運用管理者が定期的なメンテナンスやバックアップ運用を自動化する場合や、セキュリティ要件の高いマルチテナント環境で暗号化設定を厳格に管理するケースが想定されます。また、APIを活用することで、Azure DevOpsやAzure Logic Appsなどの他のAzureサービスと連携し、複雑な運用フローを構築することも可能です。

注意点としては、APIバージョンの互換性やサポート期間、既存システムとの統合時の仕様確認が必要です。また、イミュータブルバックアップやクロステナント暗号化機能を利用する際には、各機能の制限事項やAzureポータル上での設定要件を事前に確認することが重要です。

本APIは、Azure Database for PostgreSQL Flexible Serverの運用管理を高度化するための重要なアップデートであり、他のAzureサービスとの連携によるシステム全体の自動化やセキュリティ強化にも寄与します。詳細については公式アップデートページ（https://azure.microsoft.com/updates?id=579300）を参照してください。

---

### 2. Generally Available: Route maps for Azure Route Server

**公開日時**: 2026年11月04日 18:39:41 UTC
**リンク**: [Generally Available: Route maps for Azure Route Server](https://azure.microsoft.com/updates?id=578966)

**アップデートID**: 578966
**情報源**: Azure Updates API

**カテゴリ**: Networking, Azure Route Server, Features

**要約**:

- 何が更新されたか  
Azure Route Serverにおいて、Route maps機能が一般提供（GA）されました。

- 主な変更点や新機能  
Route mapsを利用することで、Azure Route Serverを介したハイブリッド接続におけるインバウンドおよびアウトバウンドのルーティング制御がより細かく行えるようになりました。これにより、Azure Route Serverに対して広告されるルートや、Azure Route Serverから広告されるルートを柔軟に管理できます。

- 影響を受ける対象  
Azure Route Serverを利用しているユーザーや、オンプレミスとAzure間でBGPピアリングを構成しているネットワーク管理者が主な対象です。

- 注意点があれば記載  
本機能はAzureパブリッククラウドで利用可能です。Route mapsの設定や運用にあたっては、既存のルーティングポリシーとの整合性や影響範囲を十分に確認することを推奨します。

**詳細**:

Azure Route ServerにおけるRoute mapsの一般提供が開始されました。本アップデートの背景には、ハイブリッド接続環境におけるルーティング制御の高度化ニーズがあります。従来、Azure Route Serverを利用した場合、オンプレミスネットワークや仮想ネットワーク間のルート交換は自動的に行われていましたが、ルートの選択や制御が限定的でした。今回のRoute mapsの提供により、Azure Route Serverを介したルートの広告や受信に対して、きめ細やかな制御が可能となります。

具体的な機能として、Route mapsはAzure Route Serverに接続されたBGPピアとの間で、インバウンドおよびアウトバウンドのルートに対して条件付きの操作を設定できます。これにより、特定のルートの許可や拒否、ルート属性の変更（例：AS Pathの追加や削除、コミュニティ値の付与など）が実現できます。Route mapsは、ルートのマッチ条件とアクションを組み合わせて定義され、複数のステートメントを順次評価することで柔軟なルーティングポリシーを構築できます。

技術的な仕組みとしては、Azure Route Server上でRoute mapsを設定することで、BGPセッションを通じて交換されるルートのフィルタリングや属性操作が自動的に適用されます。設定はAzure Resource Manager（ARM）テンプレートやAzure Portal、CLIなどを用いて実施できます。Route mapsは、Azure Route Serverリソースのプロパティとして管理され、変更は即座にBGPピアに反映されます。

活用シナリオとしては、例えばオンプレミスからAzureへのルート広告の制限や、特定のサブネットへのトラフィック誘導、複数拠点間の優先ルート設定などが挙げられます。また、マルチクラウドや複雑なハイブリッド環境において、ルートの選択や冗長性確保、セキュリティ要件に応じたルート制御が可能となります。

注意点としては、Route mapsの設定ミスによるルート遮断や意図しないトラフィック経路変更が発生する可能性があるため、事前の設計と検証が重要です。また、Route mapsの適用範囲や構文、Azure Route Serverのバージョンによる機能差異については公式ドキュメントを参照し、最新の仕様を確認する必要があります。

関連するAzureサービスとしては、Azure Virtual Network、ExpressRoute、VPN Gatewayなどが挙げられます。これらのサービスとAzure Route Serverを組み合わせることで、ハイブリッドネットワーク全体のルーティングポリシーを統合的に管理できます。Route mapsの導入により、Azure上のネットワーク設計や運用の柔軟性が大幅に向上します。

---

### 3. Public Preview: Azure Firewall IPv6 now supports application rules

**公開日時**: 2026年11月04日 18:09:43 UTC
**リンク**: [Public Preview: Azure Firewall IPv6 now supports application rules](https://azure.microsoft.com/updates?id=579507)

**アップデートID**: 579507
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Azure Firewall, Features

**要約**:

【何が更新されたか】  
Azure FirewallでIPv6環境におけるアプリケーションルールのサポートがパブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
今回のアップデートにより、Azure FirewallはIPv6およびデュアルスタック構成でHTTP/HTTPSトラフィックに対するレイヤ7（アプリケーション層）フィルタリングが可能となりました。これにより、アプリケーションレベルでのアクセス制御やセキュリティポリシーの適用がIPv6通信にも対応します。

【影響を受ける対象】  
IPv6またはデュアルスタック環境でAzure Firewallを利用しているユーザーが対象です。特に、アプリケーションルールによる詳細なトラフィック制御やセキュリティ強化を必要とするシステムに影響します。

【注意点】  
本機能はパブリックプレビュー段階のため、商用利用時にはサポートや安定性に注意が必要です。正式リリース前のため、運用環境での利用は慎重に検討してください。また、既存のIPv4ルールとの整合性や設定方法についても事前に確認することを推奨します。

**詳細**:

Azure FirewallにおけるIPv6対応のアプリケーションルールがパブリックプレビューとして提供開始されました。本アップデートの背景には、クラウド環境におけるIPv6の普及と、セキュリティ制御の高度化へのニーズがあります。従来、Azure FirewallはIPv4トラフィックに対してアプリケーションルールによるレイヤ7（アプリケーション層）でのHTTP/HTTPSフィルタリングを提供していましたが、今回のアップデートによりIPv6トラフィックにも同様の制御が適用可能となりました。これにより、IPv6単独の環境やIPv4/IPv6のデュアルスタック構成においても、一貫したアプリケーションレベルのセキュリティポリシーを実装できるようになります。

具体的な機能としては、Azure FirewallのアプリケーションルールがIPv6アドレスを対象としたHTTPおよびHTTPSトラフィックのフィルタリングをサポートします。これにより、ドメイン名やURLベースでのアクセス制御がIPv6環境でも可能となり、従来のネットワークルール（IPアドレスやポート単位の制御）に加えて、より細粒度なセキュリティ管理が実現します。実装方法としては、Azure Firewallの設定画面やARMテンプレート、Azure CLIなどを用いて、アプリケーションルールの対象IPバージョンとしてIPv6を指定することで、ルールの適用範囲を拡張できます。

活用シナリオとしては、企業や組織がAzure上でIPv6対応のWebサービスを展開する際、HTTP/HTTPSトラフィックに対してアクセス制御や監視を行いたい場合に有効です。また、デュアルスタック環境においても、IPv4とIPv6双方のトラフィックに対して同一のセキュリティポリシーを適用できるため、運用管理の一貫性が保たれます。例えば、特定のWebサイトへのアクセスをIPv6経由でも制限したり、許可したりするケースにおいて、アプリケーションルールを活用することができます。

注意点としては、本機能はパブリックプレビュー段階であり、商用利用に際してはサポートや機能の安定性に関して十分な検証が必要です。また、IPv6トラフィックに対するアプリケーションルールの適用範囲はHTTP/HTTPSに限定されており、他のプロトコルやアプリケーション層の制御については対応状況を確認する必要があります。

関連するAzureサービスとしては、Azure Virtual Network、Azure Application Gateway、Azure Monitorなどとの連携が考えられます。特に、Azure Firewallをネットワーク境界に配置し、アプリケーションルールによるフィルタリングとログ監視を組み合わせることで、セキュアなIPv6対応クラウド環境を構築することが可能です。

---

### 4. Retirement: Transition to Entra ID (formerly known as Azure AD) to query data from Azure Monitor application insights by March 31, 2027

**公開日時**: 2026年11月04日 17:40:28 UTC
**リンク**: [Retirement: Transition to Entra ID (formerly known as Azure AD) to query data from Azure Monitor application insights by March 31, 2027](https://azure.microsoft.com/updates?id=transition-to-azure-ad-to-query-data-from-azure-monitor-application-insights-by-31-march-2026)

**アップデートID**: transition-to-azure-ad-to-query-data-from-azure-monitor-application-insights-by-31-march-2026
**情報源**: Azure Updates API

**カテゴリ**: DevOps, Management and governance, Application Insights, Azure Monitor, Retirements

**要約**:

【何が更新されたか】  
Azure Monitor Application Insightsのデータクエリに使用されているAPIキーの廃止日が2027年3月31日に延長されました。

【主な変更点や新機能】  
2027年3月31日以降、APIキーによるデータクエリが利用できなくなり、Microsoft Entra ID（旧Azure AD）を用いた認証方式に移行する必要があります。Entra IDは従来の機能をすべて提供し、よりセキュアな認証・アクセス管理を実現します。

【影響を受ける対象】  
Application InsightsのデータクエリでAPIキーを使用しているシステムやアプリケーションが対象です。これらのシステムはEntra IDへの認証方式変更が必要となります。

【注意点】  
移行期限までにAPIキー認証からEntra ID認証への切り替えを行わない場合、データクエリが実行できなくなります。移行作業にはアプリケーションの認証方式やアクセス権限の見直しが必要となるため、計画的な対応を推奨します。

**詳細**:

本アップデートは、Azure Monitor Application Insightsのデータクエリに使用されているAPIキーの廃止と、Microsoft Entra ID（旧称Azure Active Directory）への移行について告知するものです。APIキーによるデータクエリは2027年3月31日をもって廃止される予定であり、以降はEntra IDを利用した認証方式に完全移行する必要があります。今回のリタイアメントの背景には、セキュリティ強化と統合認証基盤の推進があります。APIキーはシンプルな認証手段ですが、漏洩リスクやアクセス制御の柔軟性に課題があり、Entra IDへの移行によって、より高度な認証・認可機能を活用できるようになります。

具体的な変更内容としては、従来Application Insightsのデータ取得に利用されていたAPIキーが利用できなくなり、今後はEntra IDを用いたOAuth 2.0ベースの認証フローに切り替わります。これにより、ユーザーやサービスプリンシパル単位で細かいアクセス権限管理が可能となり、監査やコンプライアンス要件にも対応しやすくなります。技術的な実装方法としては、Azure Monitor Application InsightsのAPIを利用する際、Entra IDで認証されたアクセストークンを取得し、そのトークンをAPIリクエストに付与する形となります。これには、Azure ADアプリ登録や必要なAPIアクセス権限の付与、トークン取得のための認証フロー（例：クライアントクレデンシャルフローや認証コードフロー）などが必要です。

活用シナリオとしては、従来APIキーで自動化されていた監視データの取得や分析処理を、Entra ID認証に置き換えることで、より安全かつ柔軟な運用が可能となります。例えば、CI/CDパイプラインや外部分析ツールからApplication Insightsのデータを取得する場合、サービスプリンシパルを用いた認証でアクセス権限を限定しつつ、必要なデータのみを安全に取得できます。

注意点としては、APIキー廃止後は既存の自動化スクリプトやツールが動作しなくなるため、早期にEntra ID認証への移行対応が必要です。また、Entra ID認証にはアプリ登録や権限設定など追加の構成作業が発生します。関連するAzureサービスとしては、Azure Monitor、Azure AD（Entra ID）、Application Insightsが密接に連携します。これらのサービス間で認証・認可の統合が進むことで、全体のセキュリティと運用効率が向上します。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=transition-to-azure-ad-to-query-data-from-azure-monitor-application-insights-by-31-march-2026）を参照してください。

---

### 5. Public Preview: Multi-disk crash-consistent VM restore points for Premium SSD v2 and Ultra Disks on VMs with SCSI disk controller

**公開日時**: 2026年11月04日 17:13:51 UTC
**リンク**: [Public Preview: Multi-disk crash-consistent VM restore points for Premium SSD v2 and Ultra Disks on VMs with SCSI disk controller](https://azure.microsoft.com/updates?id=579162)

**アップデートID**: 579162
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Compute, Azure Disk Storage, Virtual Machines, Compliance, Management, Feature

**要約**:

【何が更新されたか】  
Azure仮想マシン（VM）において、Premium SSD v2およびUltra Diskを搭載したVM（SCSIディスクコントローラー利用）向けに、マルチディスクのクラッシュ一貫性リストアポイントがパブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
VM内の複数ディスクに対して、エージェントレスでクラッシュ一貫性を持つリストアポイントを取得できるようになりました。これにより、バックアップやリストア時にディスク間の整合性を確保しやすくなります。

【影響を受ける対象】  
Premium SSD v2およびUltra Diskを使用し、SCSIディスクコントローラーを搭載したAzure VMが対象です。これらのVMを利用している技術者や管理者にとって、バックアップ運用の柔軟性と信頼性が向上します。

【注意点】  
本機能はパブリックプレビュー段階のため、本番環境での利用には慎重な検証が必要です。また、対応ディスクタイプやコントローラーに制限があるため、既存環境との互換性を事前に確認してください。

**詳細**:

今回のAzure Updateは、「Premium SSD v2」と「Ultra Disk」を搭載した仮想マシン（VM）において、SCSIディスクコントローラーを利用している場合に、複数ディスクのクラッシュ整合性を持つVMリストアポイントを取得できる機能がパブリックプレビューとして提供開始されたものです。これまで、複数ディスクを持つVMでクラッシュ整合性のあるリストアポイントを取得することは、特定のディスクタイプやコントローラー構成に制限がありましたが、本アップデートにより、Premium SSD v2やUltra Diskを利用する高性能なストレージ構成のVMでも、SCSIディスクコントローラーを用いている場合に限り、クラッシュ整合性のあるリストアポイントを取得できるようになりました。

この機能の主な目的は、VMのバックアップやリストア作業時に、複数ディスク間の整合性を保った状態で復元ポイントを取得することです。従来のスナップショットやバックアップ機能では、ディスクごとに個別にスナップショットを取得するため、複数ディスク間で整合性が保証されない場合がありました。今回のアップデートでは、VM全体のクラッシュ整合性を担保したリストアポイントを、エージェントレスで取得できる点が特徴です。これにより、バックアップエージェントのインストールや管理が不要となり、運用負荷の軽減が期待できます。

技術的な仕組みとしては、Azure側でVMの複数ディスクに対して同時にクラッシュ整合性のあるスナップショットを取得し、それをリストアポイントとして管理します。SCSIディスクコントローラーを利用しているVMに限定されているため、VM構成の要件を満たす必要があります。また、Premium SSD v2やUltra Diskは高性能なストレージを提供するため、データベースやトランザクション処理を伴うアプリケーションのバックアップ・リストア用途に適しています。

活用シナリオとしては、ミッションクリティカルなアプリケーションを運用しているVMで、複数ディスク構成を採用している場合に、障害発生時の迅速な復旧や、定期的なバックアップ運用に利用できます。特に、データベースやファイルストレージなど、複数ディスクにまたがるデータを扱うワークロードで、クラッシュ整合性を確保したリストアポイントは重要な役割を果たします。

注意点としては、本機能はパブリックプレビュー段階であり、商用利用や大規模運用時にはAzureの公式ドキュメントやサポート情報を確認し、制限事項や既知の問題点を把握しておく必要があります。また、SCSIディスクコントローラーを利用していないVMや、Premium SSD v2・Ultra Disk以外のディスクタイプでは本機能は利用できません。

関連するAzureサービスとしては、Azure BackupやAzure Site Recoveryなどのバックアップ・復旧サービスと連携することで、より高度なデータ保護や災害復旧シナリオを構築できます。今回のアップデートは、ストレージの高性能化と運用効率の向上を両立する新しいバックアップ手法として、今後の運用設計において重要な選択肢となります。

---


*このレポートは自動生成されました - 2026-11-05 12:01:56 JST*