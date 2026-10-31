# 2026年10月31日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年10月31日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL 

**公開日時**: 2026年10月30日 17:16:27 UTC
**リンク**: [Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL ](https://azure.microsoft.com/updates?id=577491)

**アップデートID**: 577491
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**要約**:

【何が更新されたか】  
Azure SQL Databaseにおいて、データベース単位で管理されたID（Managed Identity）のサポートがパブリックプレビューとして提供されました。これにより、Create Database Scoped Credential T-SQLでユーザー割り当て型のManaged Identity（FICを含む）が利用可能になりました。

【主な変更点や新機能】  
各データベースごとにユーザー割り当て型Managed Identityを設定できるようになり、外部テーブルやOPENROWSETを使用してAzure Blob StorageやAzure Data Lake Storage Gen2のファイルにアクセスする際の認証方法が強化されました。これにより、より細かい権限管理とセキュアなデータ連携が可能になります。

【影響を受ける対象】  
Azure SQL Databaseを利用して外部ストレージと連携するアプリケーションや、データベースごとに異なる認証設定が必要なシステムが対象となります。特に、データ連携やデータ分析の用途で外部データソースを利用する技術者にとって重要なアップデートです。

【注意点】  
本機能はパブリックプレビュー段階のため、本番環境での利用には慎重な検討が必要です。今後の正式リリースに向けて仕様変更や制限が発生する可能性がありますので、最新情報の確認を推奨します。

**詳細**:

今回のAzure Updateは、「Create Database Scoped Credential T-SQL」において、Azure SQL Databaseのデータベース単位でマネージドID（特にユーザー割り当て型マネージドIDおよびFIC：Federated Identity Credential）をサポートする機能のパブリックプレビュー開始に関するものです。従来、Azure SQL Databaseで外部ストレージ（Azure Blob StorageやAzure Data Lake Storage Gen2）と連携する際には、サーバーレベルのマネージドIDやストレージアカウントのアクセスキーなどを利用して認証を行う必要がありました。しかし今回のアップデートにより、各データベースごとにユーザー割り当て型マネージドIDを設定し、T-SQLの「CREATE DATABASE SCOPED CREDENTIAL」コマンドを通じて認証情報を管理できるようになりました。

この機能の主な目的は、データベースごとに異なるマネージドIDを割り当てることで、より細粒度なアクセス制御とセキュリティ向上を実現することにあります。例えば、複数のデータベースが同一SQLサーバー上に存在する場合、それぞれのデータベースが異なるストレージリソースにアクセスする際に、個別のマネージドIDを利用することで、不要な権限の付与や情報漏洩リスクを低減できます。

技術的な仕組みとしては、Azure Active Directory上でユーザー割り当て型マネージドIDを作成し、そのIDに対してストレージリソースへのアクセス権限（RBACなど）を付与します。データベース側では、「CREATE DATABASE SCOPED CREDENTIAL」コマンドを用いて、そのマネージドIDを認証情報として登録します。これにより、外部テーブルや「OPENROWSET」などのT-SQL機能を使ってストレージ上のファイルを直接クエリする際に、データベース単位で設定されたマネージドIDを用いて認証が行われます。

活用シナリオとしては、データウェアハウスやデータレイク連携を行う際に、各データベースごとに異なるストレージアカウントやコンテナへのアクセスを制御したい場合や、マルチテナント環境でテナントごとに認証情報を分離したい場合などが挙げられます。また、Federated Identity Credential（FIC）にも対応しているため、より柔軟な認証方式の採用が可能です。

注意点としては、パブリックプレビュー段階であるため、商用環境での利用には慎重な検証が必要です。また、マネージドIDの設定や権限付与はAzure Active Directoryおよびストレージ側で適切に行う必要があります。関連するAzureサービスとしては、Azure Blob Storage、Azure Data Lake Storage Gen2、Azure Active Directory、RBAC（ロールベースアクセス制御）、およびSQL Databaseが密接に連携します。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=577491）をご参照ください。

---


*このレポートは自動生成されました - 2026-10-31 12:00:51 JST*