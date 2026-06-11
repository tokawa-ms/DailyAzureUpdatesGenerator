# 2026年06月11日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年06月11日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Generally Available: Microsoft Entra server principals on Azure SQL Database 

**公開日時**: 2026年06月10日 20:45:26 UTC
**リンク**: [Generally Available: Microsoft Entra server principals on Azure SQL Database ](https://azure.microsoft.com/updates?id=565154)

**アップデートID**: 565154
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**要約**:

【何が更新されたか】  
Microsoft Entra server principals（ログイン）がAzure SQL Databaseで一般提供（GA）されました。

【主な変更点や新機能】  
Azure SQL Databaseの仮想マスターデータベースで「CREATE LOGIN ... FROM EXTERNAL PROVIDER」を使用できるようになりました。これにより、Microsoft Entra ID（旧Azure AD）を利用したログイン管理がSQLログインと同等の扱いとなり、認証やアクセス管理の一元化が可能です。

【影響を受ける対象】  
Azure SQL Databaseを利用している技術者や管理者、特にMicrosoft Entra IDによる認証を導入している環境が対象です。セキュリティや認証管理の強化を求めるシステムに有効です。

【注意点】  
新機能を利用するには、仮想マスターデータベースで適切な権限が必要です。既存のSQLログインとの違いや、Entra IDの設定・管理方法について事前に確認してください。既存の認証方式から移行する場合は、十分なテストを推奨します。

**詳細**:

本アップデートは、Azure SQL DatabaseにおいてMicrosoft Entra server principals（ログイン）が一般提供（GA）となったことを示しています。これにより、仮想マスターデータベース上で「CREATE LOGIN ... FROM EXTERNAL PROVIDER」コマンドを利用し、Microsoft Entra ID（旧Azure Active Directory）に基づくログインを作成できるようになりました。従来、Azure SQL DatabaseではSQL認証や一部のEntra ID認証がサポートされていましたが、今回のアップデートにより、オンプレミスのSQL Serverと同様にEntra IDベースのログイン管理が可能となり、認証方式の一貫性と運用の柔軟性が向上しています。

具体的には、仮想マスターデータベースで「CREATE LOGIN [ユーザー名] FROM EXTERNAL PROVIDER」と実行することで、Microsoft Entra IDに登録されたユーザーやサービスプリンシパルをサーバーレベルのログインとして登録できます。これにより、個々のデータベースごとにユーザーを作成する必要がなくなり、サーバーレベルで一元的なアクセス管理が実現します。Entra IDと連携することで、多要素認証や条件付きアクセスなどの高度なセキュリティ機能も活用可能です。

技術的な仕組みとしては、Azure SQL Databaseの仮想マスターデータベースがEntra IDと連携し、外部プロバイダーとしてEntra IDを認識します。これにより、Entra IDの認証情報を利用したサーバーレベルのログイン管理が可能となります。従来のSQLログインと同様の構文で管理できるため、既存の運用フローや自動化スクリプトへの組み込みも容易です。

活用シナリオとしては、企業内でEntra IDをアイデンティティ基盤として統合管理している場合、Azure SQL Databaseへのアクセス制御をEntra IDに集約できます。これにより、ユーザーやアプリケーションのアクセス権限管理、監査、セキュリティポリシーの適用が一元化され、運用効率とセキュリティが向上します。また、サービスプリンシパルを利用したアプリケーションからの安全な接続や、条件付きアクセスポリシーの適用も可能です。

注意点としては、Entra IDとの連携設定や必要な権限の付与、既存のSQLログインとの共存に関する設計が必要です。また、Entra IDの認証基盤に依存するため、ID管理や認証の可用性にも留意する必要があります。さらに、Azure SQL Databaseの一部エディションやリージョンでのサポート状況については、公式ドキュメントでの確認が推奨されます。

本機能は、Microsoft Entra ID、Azure SQL Database、Azure Active DirectoryなどのAzureサービスと密接に連携して動作します。これにより、クラウドネイティブなアイデンティティ管理とデータベースセキュリティの強化が実現されます。

---

### 2. Retirement: Azure Synapse Link for Azure Cosmos DB NoSQL

**公開日時**: 2026年06月10日 17:00:06 UTC
**リンク**: [Retirement: Azure Synapse Link for Azure Cosmos DB NoSQL](https://azure.microsoft.com/updates?id=558560)

**アップデートID**: 558560
**情報源**: Azure Updates API

**カテゴリ**: Databases, Internet of Things, Analytics, Azure Cosmos DB, Azure Synapse Analytics, Retirements, Services

**要約**:

- 何が更新されたか  
Azure Cosmos DB NoSQL向けのAzure Synapse Linkがリタイア（提供終了）となることが発表されました。

- 主な変更点や新機能  
2026年3月31日以降、新規のAzure Cosmos DB NoSQLアカウントではAzure Synapse Linkを有効化できなくなります。既存の利用者については2029年3月31日までサポートが継続されますが、それ以降は完全にサービスが終了します。

- 影響を受ける対象  
Azure Cosmos DB NoSQLでAzure Synapse Linkを利用している、または今後利用を検討しているすべてのユーザーが対象です。特に新規導入を検討中のプロジェクトは注意が必要です。

- 注意点  
既存ユーザーは2029年3月31日まで引き続きサポートされますが、今後の新規導入はできません。マイクロソフトは代替ソリューションへの移行を推奨しています。サービス終了に伴い、データ分析や連携機能の見直しが必要となるため、早めの移行計画策定をおすすめします。

**詳細**:

2026年3月31日をもって、新規のAzure Cosmos DB NoSQLアカウントではAzure Synapse Linkの有効化ができなくなります。既存の顧客については2029年3月31日までAzure Synapse Linkのサポートが継続されますが、その後はサービスの提供が終了します。このアップデートの背景には、Azureプラットフォーム全体のサービス統合や機能刷新、もしくは将来的な新サービスへの移行促進といった目的が考えられますが、公式にはサービス終了のアナウンスのみが示されています。

Azure Synapse Link for Azure Cosmos DB NoSQLは、トランザクションワークロードと分析ワークロードを分離し、リアルタイム分析を可能にする機能です。これにより、Cosmos DBに格納されたNoSQLデータをETL処理なしでAzure Synapse Analyticsなどの分析サービスに連携し、ほぼリアルタイムでデータ分析を実施できる仕組みを提供していました。技術的には、Cosmos DBの変更フィード(Change Feed)を活用し、データをHTAP(ハイブリッドトランザクション/分析処理)ストアに同期することで、運用データベースへの影響を最小限に抑えつつ分析処理を実現していました。

この機能は、たとえばeコマースサイトのユーザー行動分析やIoTデバイスからの時系列データのリアルタイム分析など、運用データベースと分析基盤のシームレスな連携が求められるシナリオで広く活用されてきました。ETLバッチ処理を介さず、データの即時分析が可能な点が大きな利点でした。

今回のアップデートにより、2026年3月31日以降は新規のNoSQLアカウントでAzure Synapse Linkを利用できなくなるため、新規プロジェクトでの採用は推奨されません。既存アカウントについても、2029年3月31日をもってサービスが完全終了するため、今後の運用計画やアーキテクチャ設計においては、代替手段の検討やデータ連携方法の見直しが必要となります。特に、Azure Synapse AnalyticsやPower BIなど、他のAzure分析サービスとの連携を行っている場合は、今後のサポート終了を見据えた移行計画を早期に策定することが重要です。

関連するAzureサービスとしては、Azure Data FactoryやAzure Databricks、Event Hubsなどが挙げられます。これらのサービスを活用したデータ連携や分析基盤の構築が今後の代替案となる可能性があります。サービス終了に伴い、既存のワークロードやデータフローに影響が及ぶため、十分な検証と計画的な移行が必要です。

詳細は公式アナウンス（https://azure.microsoft.com/updates?id=558560）を参照し、最新情報を確認してください。

---

### 3. Retirement: Azure VPN Client for Linux (Preview) will be retired on August 31, 2026 

**公開日時**: 2026年06月10日 16:15:16 UTC
**リンク**: [Retirement: Azure VPN Client for Linux (Preview) will be retired on August 31, 2026 ](https://azure.microsoft.com/updates?id=565393)

**アップデートID**: 565393
**情報源**: Azure Updates API

**カテゴリ**: Networking, Security, Virtual WAN, VPN Gateway, Retirements

**要約**:

- 何が更新されたか  
Azure VPN Client for Linux（プレビュー版）が2026年8月31日をもってリタイア（提供終了）されることが発表されました。

- 主な変更点や新機能  
本アップデートでは新機能の追加や変更はありません。Azure VPN Client for Linux（プレビュー版）の提供終了が主な内容です。

- 影響を受ける対象  
現在Azure VPN Client for Linux（プレビュー版）を利用しているユーザーおよびシステムが対象となります。今後このクライアントを利用したVPN接続はサポートされなくなります。

- 注意点があれば記載  
2026年8月31日以降、Azure VPN Client for Linux（プレビュー版）は利用できなくなります。今後もVPN接続が必要な場合は、他のサポートされているVPNクライアントや代替手段への移行を検討してください。プレビュー版のため、正式なサポートやセキュリティアップデートも提供されていません。早めの対応を推奨します。

**詳細**:

Azure VPN Client for Linux (Preview)は、パブリックプレビューとして提供されてきましたが、一般提供（GA）への移行計画がないまま、2026年8月31日をもってリタイアされることが発表されました。本アップデートの背景には、Azureネットワークサービス全体のセキュリティおよび信頼性基準への整合性を図るという目的があります。これにより、プレビュー版として提供されていたLinux向けAzure VPNクライアントのサポートが終了し、今後は他の正式サポートされているソリューションへの移行が求められます。

Azure VPN Client for Linux (Preview)は、Azure Virtual Network Gatewayを利用したPoint-to-Site（P2S）VPN接続をLinux環境から確立するためのクライアントアプリケーションです。これにより、Linux端末からAzure上の仮想ネットワークに安全にアクセスすることが可能となっていました。技術的には、OpenVPNやIKEv2などのプロトコルを利用し、Azure側で構成されたVPN Gatewayとの間で暗号化されたトンネルを確立する仕組みです。クライアント証明書やAzure Active Directory認証など、複数の認証方式に対応している点が特徴でした。

主な活用シナリオとしては、開発者や運用担当者がLinuxベースの端末からAzure上のリソース（仮想マシン、データベース、ストレージなど）にセキュアにアクセスする場合や、ハイブリッドネットワーク構成においてオンプレミスのLinuxサーバーからAzureリソースへの安全な通信経路を確保する場合が挙げられます。

今回のリタイアにより、Linux環境でAzure VPNクライアント（Preview）の利用を継続することはできなくなります。今後は、正式サポートされている他のVPNクライアント（たとえばOpenVPNクライアントやStrongSwanなど）を用いて、Azure Virtual Network Gatewayとの接続を構成する必要があります。Azure側のVPN Gatewayは、引き続きOpenVPNやIKEv2プロトコルに対応しているため、これらの標準的なクライアントを活用することで同等の接続性を維持できます。

注意点として、プレビュー版であるため、これまでのAzure VPN Client for Linuxは本番環境での利用が推奨されていませんでしたが、リタイア後は完全にサポートが終了し、セキュリティアップデートや技術的なサポートも提供されなくなります。したがって、早期に代替ソリューションへの移行計画を策定することが重要です。

関連するAzureサービスとしては、Azure Virtual Network GatewayやAzure Active Directoryなどが挙げられます。これらのサービスと連携し、引き続き安全なリモートアクセス環境を維持するためには、公式ドキュメントに従い、サポートされているクライアントでの接続設定を行う必要があります。

---


*このレポートは自動生成されました - 2026-06-11 12:01:16 JST*