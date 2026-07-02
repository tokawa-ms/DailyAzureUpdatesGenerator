# 2026年07月02日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年07月02日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Generally Available: New Powershell module:  Az.PostgreSQLFlexibleServer  

**公開日時**: 2026年07月01日 17:19:25 UTC
**リンク**: [Generally Available: New Powershell module:  Az.PostgreSQLFlexibleServer  ](https://azure.microsoft.com/updates?id=566209)

**アップデートID**: 566209
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

【何が更新されたか】  
Azure Database for PostgreSQL Flexible Serverの管理を支援する新しいPowerShellモジュール「Az.PostgreSQLFlexibleServer」が一般提供（GA）されました。

【主な変更点や新機能】  
従来の「Az.PostgreSql」モジュールから名称が変更され、より柔軟なサーバー管理に特化した機能が提供されます。これにより、PowerShellを使ったAzure PostgreSQL Flexible Serverの操作がより効率的かつ直感的になります。

【影響を受ける対象】  
Azure Database for PostgreSQL Flexible ServerをPowerShellで管理している技術者や運用担当者が対象です。既存のスクリプトや運用フローで「Az.PostgreSql」モジュールを利用している場合、今後は新モジュールへの移行を検討する必要があります。

【注意点】  
新モジュールへの移行時には、コマンドレットやパラメータの違いに注意してください。既存のスクリプトが動作しなくなる可能性があるため、事前に動作確認を行うことを推奨します。

**詳細**:

本アップデートは、Azure Database for PostgreSQL Flexible Serverの管理をPowerShellからより効率的に行うための新しいPowerShellモジュール「Az.PostgreSQLFlexibleServer」の一般提供開始を告知するものです。従来の「Az.PostgreSql」モジュールの機能を基盤としつつ、名称を変更し、より柔軟で直感的な操作性を提供することを目的としています。これにより、Azure上で稼働するPostgreSQL Flexible Serverのリソース管理や運用自動化が、PowerShellを通じて一層容易になります。

新モジュール「Az.PostgreSQLFlexibleServer」では、サーバーの作成、構成変更、スケーリング、バックアップ、リストア、セキュリティ設定など、PostgreSQL Flexible Serverに関する主要な管理操作をPowerShellコマンドレットとして提供します。これにより、GUIではなくスクリプトベースでの一括管理や自動化が可能となり、DevOpsやインフラ自動化の現場での活用が期待されます。従来のモジュールからの移行に際しては、コマンドレット名やパラメーター体系が変更されている場合があるため、既存のスクリプトを利用する際には互換性に注意が必要です。

技術的には、Az PowerShellモジュールの一部として提供され、Azure Resource Manager（ARM）APIをバックエンドで利用してリソース操作を実現しています。これにより、Azure PortalやCLIと同等の操作がPowerShellから実行可能となります。実装方法としては、PowerShellギャラリーから「Az.PostgreSQLFlexibleServer」モジュールをインストールし、必要なコマンドレットを呼び出して操作を行います。

活用シナリオとしては、複数のPostgreSQL Flexible Serverインスタンスの一括デプロイ、定期的なバックアップやパラメーター設定の自動化、運用監視や障害対応の自動化などが挙げられます。たとえば、CI/CDパイプライン内でのデータベース環境の自動構築や、定期的なメンテナンス作業の自動化など、運用効率化に貢献します。

注意点としては、従来の「Az.PostgreSql」モジュールとの互換性や、サポートされるPowerShellバージョン、Azureアカウントの認証方式などに留意する必要があります。また、Flexible Server固有の機能や制限事項については、公式ドキュメントを参照し、モジュールのバージョンアップや機能追加に追従することが推奨されます。

本モジュールは、Azure Database for PostgreSQL Flexible Server専用となっており、他のAzure Databaseサービス（例：MySQL、SQL Database）とは異なるコマンドレット体系となっています。必要に応じて、他のAzモジュールと組み合わせて、より包括的なAzureリソース管理を実現することが可能です。詳細については、公式アップデートページやドキュメントを参照してください。

---

### 2. Public Preview: Document PII playground sample in Microsoft Foundry NextGen

**公開日時**: 2026年07月01日 17:04:40 UTC
**リンク**: [Public Preview: Document PII playground sample in Microsoft Foundry NextGen](https://azure.microsoft.com/updates?id=563331)

**アップデートID**: 563331
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry, Feature

**要約**:

- 何が更新されたか  
Azure AI LanguageのドキュメントベースPII（個人識別情報）検出機能が、Microsoft Foundry NextGenポータルでPublic Previewとして利用可能になりました。

- 主な変更点や新機能  
新たに「PII playground」サンプルが提供され、サンプルドキュメントを使ってPII検出機能を体験できるようになりました。ユーザーはドキュメントをアップロードし、PII検出の結果としてマスキングされた内容を確認できます。

- 影響を受ける対象  
Azure AI Languageを利用している技術者や、PII検出機能の評価・導入を検討している開発者が対象です。特に、ドキュメント単位でのPII検出を試したい場合に有用です。

- 注意点があれば記載  
本機能はPublic Preview段階のため、商用利用や本番環境での利用には注意が必要です。機能やUIが今後変更される可能性があります。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=563331）をご参照ください。

**詳細**:

今回のAzure Updateは、「Document-based PII detection in Azure AI Language」がMicrosoft Foundry NextGenポータルにて初期のプレイグラウンド体験として提供開始されたことを示しています。アップデートの背景としては、Azure AI Languageサービスにおける文書ベースのPII（Personally Identifiable Information、個人識別情報）検出機能の実用性向上と、ユーザーが容易に機能を試せる環境の提供が挙げられます。これにより、技術者はPII検出の挙動や精度を事前に確認し、実際の業務やシステム導入時の参考にすることが可能となります。

具体的な機能としては、Microsoft Foundry NextGenポータル内のプレイグラウンドで、あらかじめ用意されたサンプル文書をロードし、その文書をAzure AI Languageの文書ベースPII検出機能に通すことができます。処理後には、検出されたPII情報がマスキングされた状態の文書が表示されます。これにより、どの情報がPIIとして認識され、どのようにマスキングされるかを視覚的に確認することができます。

技術的な仕組みについては、Azure AI LanguageのPII検出機能が文書全体を解析し、個人識別情報を自動的に抽出・マスキングするアルゴリズムを用いています。プレイグラウンドでは、サンプル文書を入力として、バックエンドでPII検出APIが呼び出され、その結果がユーザーインターフェース上に表示される流れとなっています。Microsoft Foundry NextGenポータルは、Azureの各種AIサービスの実験的な機能を試せる環境として設計されており、今回のアップデートもその一環です。

活用シナリオとしては、技術者が自社の文書データにPII検出機能を導入する前に、サンプル文書を使って検出精度やマスキング方法を確認する用途が考えられます。また、開発者がAzure AI LanguageのPII検出APIの挙動を理解し、実際のシステム設計や運用に役立てることができます。

注意点や制限事項としては、現時点でプレイグラウンド体験が提供されているのはMicrosoft Foundry NextGenポータル内のみであり、利用できる文書は準備されたサンプルに限定されています。実際の業務データやカスタム文書での検証は、別途Azure AI Languageサービスの本番環境で行う必要があります。

関連するAzureサービスとしては、Azure AI Languageが中心となりますが、PII検出機能は他のAzure Cognitive Servicesやセキュリティ関連サービスと組み合わせて利用することも可能です。今回のアップデートは、Azure AI Languageの機能拡張やユーザー体験向上の一環として位置付けられています。

---

### 3. Generally Available: Document PII NextGen Playground in Azure AI Language

**公開日時**: 2026年07月01日 17:01:07 UTC
**リンク**: [Generally Available: Document PII NextGen Playground in Azure AI Language](https://azure.microsoft.com/updates?id=564382)

**アップデートID**: 564382
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry, Feature

**要約**:

【何が更新されたか】  
Azure AI Languageにおいて、「Document PII NextGen Playground」が一般提供（GA）されました。

【主な変更点や新機能】  
このアップデートにより、ドキュメント内の個人識別情報（PII）検出機能を評価するためのプレイグラウンドが刷新されました。新しいプレイグラウンドには、厳選されたサンプル入力と出力が用意されており、ユーザーはより迅速にPII検出の精度や動作を確認できます。

【影響を受ける対象】  
Azure AI LanguageのDocument PII機能を利用する開発者やデータエンジニア、セキュリティ担当者が主な対象です。特に、ドキュメント内の個人情報保護やコンプライアンス対応を求められるシステムの設計・運用に関わる技術者にとって有用です。

【注意点】  
一般提供となったことで、商用環境でも安心して利用できますが、サンプルデータの利用や実際のPII検出結果の精度については、公式ドキュメントを参照しながら検証を行うことを推奨します。

**詳細**:

Azure AI Languageにおいて、Document PII NextGen Playgroundが一般提供（GA）となりました。このアップデートは、ドキュメント内の個人識別情報（PII: Personally Identifiable Information）検出機能の評価を迅速かつ効率的に行える環境を提供することを目的としています。従来、PII検出の精度や挙動を確認するには、独自のサンプルデータを用意し、APIを組み込んで検証する必要がありましたが、今回のPlaygroundでは、あらかじめ厳選されたサンプル入力と出力が用意されており、ユーザーはこれらを利用して即座にPII検出の結果を確認できます。

具体的な機能として、Document PII Playgroundは、ドキュメント内に含まれる氏名、住所、電話番号、メールアドレスなどの個人情報を自動的に抽出・検出するAIモデルの評価環境を提供します。ユーザーはサンプルドキュメントを選択し、検出結果としてどの情報がPIIとして認識されたかを確認できます。これにより、実運用前の検証や、モデルの挙動理解、導入可否の判断が容易になります。

技術的な仕組みとしては、Azure AI LanguageのPII検出APIがバックエンドで動作しており、PlaygroundはそのAPIの呼び出し結果をインタラクティブに表示するWebベースのUIを提供しています。サンプルデータはMicrosoftによってキュレーションされており、実際のAPIレスポンスを即座に確認できるため、APIのパラメータやレスポンス形式の理解にも役立ちます。

活用シナリオとしては、企業の情報管理担当者や開発者が、自社ドキュメントのPII検出精度を事前に評価したい場合や、Azure AI Languageの導入を検討する際の技術検証に利用できます。また、既存システムへの組み込み前に、検出結果の妥当性や期待値を確認する用途にも適しています。

注意点として、Playgroundはサンプルデータによる評価環境であり、実際の運用データを直接アップロードして検証する機能については明記されていません。また、検出対象となるPIIの種類や言語対応範囲、モデルのバージョンなど詳細な制限事項は公式ドキュメントを参照する必要があります。

関連するAzureサービスとしては、Azure AI LanguageのDocument PII検出APIが中心となりますが、他のテキスト分析機能や、Azure Cognitive Servicesとの連携も想定されます。Playgroundはこれらのサービスの評価・導入支援ツールとして位置付けられています。

以上が、Azure AI LanguageのDocument PII NextGen Playground一般提供に関する技術者向け詳細説明です。

---

### 4. Public Preview: Instant Access via application consistent restore points

**公開日時**: 2026年07月01日 16:59:39 UTC
**リンク**: [Public Preview: Instant Access via application consistent restore points](https://azure.microsoft.com/updates?id=565758)

**アップデートID**: 565758
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Compute, Azure Disk Storage, Virtual Machines, Features, Feature

**要約**:

【何が更新されたか】  
Azure VM Restore Pointsに「Instant Access」機能がパブリックプレビューとして追加されました。

【主な変更点や新機能】  
これまでRestore Point作成後、ディスクの復元にはバックグラウンドでのデータレプリケーション完了を待つ必要がありましたが、Instant Accessにより、Restore Point作成直後からディスクを即時復元できるようになりました。これにより、RTO（復旧時間目標）が大幅に短縮され、迅速な障害対応やテストが可能になります。

【影響を受ける対象】  
Azure上で仮想マシンのバックアップやリストアを行う技術者、特にアプリケーション整合性を重視した復元作業を行う運用担当者が主な対象です。

【注意点】  
本機能は現在パブリックプレビュー段階です。商用環境での利用には十分な検証を推奨します。また、Instant Accessはアプリケーション整合性のあるRestore Pointに限定されているため、利用前に対応状況を確認してください。

**詳細**:

Azureは、仮想マシン（VM）のRestore Pointに対して「Instant Access」機能のパブリックプレビューを開始しました。このアップデートの背景には、従来のRestore Point作成後にディスク復元を行う際、バックグラウンドでのデータレプリケーション完了まで待つ必要があり、復旧時間（RTO: Recovery Time Objective）が長くなるという課題がありました。今回のアップデートは、Restore Point作成直後にディスクを即座に復元できるようになり、復旧プロセスの効率化と迅速化を目的としています。

具体的な機能としては、Restore Pointが作成されると同時に、バックグラウンドのデータレプリケーションを待たずに、ディスクの復元操作を開始できる点が最大の特徴です。これにより、障害発生時やテスト環境の迅速なリカバリーが求められる場面で、従来よりも大幅に短い時間で復元作業を完了することが可能となります。アプリケーション整合性のあるRestore Pointを利用することで、データの一貫性を担保しつつ、即時復元が実現できます。

技術的な仕組みとしては、Restore Point作成時に、復元対象ディスクのスナップショットが即座に利用可能となるため、ユーザーはバックグラウンド処理の進捗を待つことなく、復元操作を開始できます。これにより、従来のプロセスに比べて、復元までの待機時間が大幅に短縮されます。実装方法としては、Azure PortalやAPIを通じてRestore Point作成後、即座に復元ディスクの作成やアタッチが可能です。

活用シナリオとしては、ミッションクリティカルなシステムの障害復旧や、開発・テスト環境での迅速なロールバック、データ整合性を重視した復元作業などが挙げられます。特に、業務継続計画（BCP）やDR（ディザスタリカバリ）対策として、復旧時間の短縮が求められる場面で有効です。

注意点としては、パブリックプレビュー段階であるため、運用環境での利用には慎重な検証が必要です。また、Instant Access機能がサポートするVMやディスクの種類、リージョンなどに制限がある可能性があるため、事前に公式ドキュメントやサポート情報を確認することが重要です。

関連するAzureサービスとしては、Azure BackupやAzure Site Recoveryなどの復旧・バックアップサービスと連携することで、より高度なデータ保護や復元戦略を構築できます。Instant AccessによるRestore Pointの即時復元は、これらのサービスと組み合わせることで、全体の復旧プロセスを最適化することが可能です。

以上のように、AzureのInstant Access via application consistent restore pointsは、復旧時間の短縮とデータ整合性の担保を両立する新しい復元機能として、技術者にとって非常に実用的なアップデートです。

---

### 5. Public Preview: Azure Storage Mover now supports migration from Google Cloud Storage (GCS)

**公開日時**: 2026年07月01日 16:56:50 UTC
**リンク**: [Public Preview: Azure Storage Mover now supports migration from Google Cloud Storage (GCS)](https://azure.microsoft.com/updates?id=566948)

**アップデートID**: 566948
**情報源**: Azure Updates API

**カテゴリ**: Launched, Migration, Storage, Azure Storage Mover, Feature

**要約**:

- 何が更新されたか  
Azure Storage Moverが、Google Cloud Storage（GCS）からAzure Blob Storageへのクラウド間データ移行をサポートする機能がパブリックプレビューとして提供開始されました。

- 主な変更点や新機能  
今回のアップデートにより、S3互換インターフェースを利用して、GCSからAzure Blob Storageへのデータ移行が可能になりました。これにより、マルチクラウド環境からAzureへのデータ統合や移行作業がより簡単に実施できます。

- 影響を受ける対象  
Google Cloud StorageからAzure Blob Storageへのデータ移行を検討している企業や組織、またはマルチクラウド環境を運用している技術者が主な対象です。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用には十分な検証が推奨されます。また、S3互換インターフェースを利用するため、設定や互換性について事前に確認することが重要です。

**詳細**:

Azure Storage Moverの最新アップデートにより、Google Cloud Storage（GCS）からAzure Blob Storageへのクラウド間データ移行がパブリックプレビューとしてサポートされるようになりました。このアップデートの背景には、企業が複数のクラウド環境を利用する中で、データの統合や移行を効率的に行いたいというニーズがあります。特に、Google Cloud StorageからAzureへの移行を容易にすることで、Azureへのマルチクラウド統合を促進する目的があります。

今回のアップデートでは、Azure Storage MoverがS3互換インターフェースを利用してGCSからデータを取得し、Azure Blob Storageへ移行できる機能が追加されています。これにより、従来はオンプレミスや他のクラウドサービスからの移行に限定されていたStorage Moverの利用範囲が拡大し、Google Cloud Storageから直接Azure Blob Storageへのクラウド間移行が可能となりました。

技術的な仕組みとしては、Storage MoverがS3互換APIを通じてGCSのデータにアクセスし、データの転送を行います。ユーザーはStorage Moverのジョブ設定において、GCSのエンドポイントや認証情報を指定することで、移行プロセスを自動化できます。移行先としてAzure Blob Storageを指定することで、データの整合性を保ちながら効率的に移行が実施されます。

活用シナリオとしては、Google Cloud上に保存されている大量のデータをAzure環境へ統合したい場合や、マルチクラウド運用からAzureへの集約を検討している企業にとって有効です。また、既存のバックアップデータやアーカイブデータをAzure Blob Storageに移行することで、Azureの高度なセキュリティや管理機能を活用することができます。

注意点としては、パブリックプレビュー段階であるため、運用環境での利用には慎重な検証が必要です。また、S3互換インターフェースを利用するため、GCS側でのAPI設定や認証情報の管理が適切に行われていることが前提となります。移行対象データのサイズや構造によっては、転送速度やコスト面での考慮も必要です。

関連するAzureサービスとしては、Azure Blob Storageが移行先となり、移行後はAzureのデータ管理機能やセキュリティ機能と連携して運用することが可能です。さらに、Storage MoverはAzureの他のストレージサービスやデータ移行ツールとも併用できるため、総合的なデータ管理ソリューションの一部として活用できます。

以上のように、Azure Storage MoverのGCS対応は、マルチクラウド環境からAzureへのデータ移行を効率化し、企業のクラウド統合戦略を支援する重要なアップデートです。

---


*このレポートは自動生成されました - 2026-07-02 12:01:59 JST*