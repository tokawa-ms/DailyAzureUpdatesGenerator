# 2026年07月31日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年07月31日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Generally Available: Azure Database for PostgreSQL flexible server in India South Central 

**公開日時**: 2026年07月30日 19:14:44 UTC
**リンク**: [Generally Available: Azure Database for PostgreSQL flexible server in India South Central ](https://azure.microsoft.com/updates?id=568334)

**アップデートID**: 568334
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Feature

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverが、インド南中部（India South Central）リージョンで一般提供（GA）されました。

- 主な変更点や新機能  
これまで利用できなかったIndia South Centralリージョンで、PostgreSQL Flexible Serverのデプロイが可能になりました。これにより、リージョン固有の低レイテンシやデータ主権要件への対応が強化されます。

- 影響を受ける対象  
インド南中部リージョンでサービスを展開する企業や開発者、現地のデータ要件に対応したいユーザーが対象となります。既存のAzure Database for PostgreSQL Flexible Serverユーザーも、リージョン選択肢が増えることで、より柔軟なアーキテクチャ設計が可能です。

- 注意点があれば記載  
新たにリージョンが追加されたことで、リージョンごとのサービス仕様や料金体系、可用性ゾーンの有無などを事前に確認することをおすすめします。既存のデータベースからの移行やレプリケーションを検討する際は、リージョン間の制約にも注意が必要です。

**詳細**:

Azure Database for PostgreSQL Flexible ServerがIndia South Centralリージョンで一般提供されたことにより、インド南部地域のユーザーは、より近いリージョンで高可用性と柔軟性を備えたPostgreSQLデータベースサービスを利用できるようになりました。このアップデートの背景には、インド国内のデータレジデンシ要件や低レイテンシニーズへの対応、ならびに地域のクラウドインフラ拡充が挙げられます。これにより、現地の企業や開発者は、Azureのグローバルな信頼性とスケーラビリティを活用しつつ、データをインド国内に保持することが可能となります。

具体的な機能として、Azure Database for PostgreSQL Flexible Serverは、PostgreSQLのオープンソースデータベースをマネージドサービスとして提供し、サーバー構成の柔軟性、カスタムメンテナンスウィンドウ、スケールアップ・スケールダウン、バックアップ、フェイルオーバー、セキュリティ機能などを備えています。今回のアップデートでは、これらの機能がIndia South Centralリージョンでも利用可能となり、リージョン選択時にIndia South Centralを指定することでデプロイできます。

技術的な仕組みとしては、Flexible Serverは仮想マシンベースで構築されており、ユーザーはvCPU数やメモリサイズ、ストレージ容量などを細かく設定できます。また、単一可用性ゾーンや複数可用性ゾーンでの高可用性構成が選択でき、障害時の自動フェイルオーバーやバックアップからのリストアもサポートされています。さらに、ネットワーク構成ではパブリックアクセスとプライベートアクセス（VNet統合）が選択可能です。

活用シナリオとしては、インド南部地域の金融、医療、教育、政府機関など、データの地域内保存が求められる業種での利用が想定されます。また、低レイテンシが求められるWebアプリケーションやモバイルアプリのバックエンド、分析基盤、IoTデータストアなどにも適しています。Azure App ServiceやAzure Functions、Azure Logic Appsなどのサービスと連携することで、フルマネージドなアプリケーション基盤を構築できます。

注意点としては、リージョンごとに利用可能なSKUや機能、価格が異なる場合があるため、India South Centralリージョンの公式ドキュメントや価格ページを事前に確認する必要があります。また、リージョン間レプリケーションやバックアップの保存先など、リージョン固有の制限事項にも留意してください。

関連するAzureサービスとの連携としては、Azure Active Directoryによる認証統合、Azure Monitorによる監視、Azure Backupによるデータ保護、Azure Private Linkによるセキュアなネットワーク接続などが挙げられます。これらのサービスと組み合わせることで、セキュリティや運用管理の強化が可能です。

今回のアップデートにより、India South CentralリージョンでAzure Database for PostgreSQL Flexible Serverを利用することで、現地の要件に即したクラウドデータベース運用が実現できるようになりました。

---

### 2. Generally Available: Azure Automation supports PowerShell 7.6 runbooks and Runtime environment

**公開日時**: 2026年07月30日 19:10:35 UTC
**リンク**: [Generally Available: Azure Automation supports PowerShell 7.6 runbooks and Runtime environment](https://azure.microsoft.com/updates?id=568102)

**アップデートID**: 568102
**情報源**: Azure Updates API

**カテゴリ**: Launched, Management and governance, Automation, Feature

**要約**:

【何が更新されたか】  
Azure AutomationでPowerShell 7.6ランブックおよびランタイム環境が一般提供（GA）されました。

【主な変更点や新機能】  
これまでサポートされていなかったPowerShell 7.6を利用したランブックの作成・実行が可能になり、最新のスクリプトや機能を活用できるようになりました。また、Azure CLIコマンドのサポートも強化されています。

【影響を受ける対象】  
Azure Automationを利用している技術者や運用担当者が対象です。特に、従来のPowerShellバージョン（5.1など）で作成したランブックを新しいバージョンへ移行したい場合や、最新のPowerShell機能を活用したい場合に影響があります。

【注意点】  
既存のランブックをPowerShell 7.6へ移行する際は、互換性や動作確認が必要です。特に、モジュールやコマンドの仕様変更により動作が変わる場合があるため、事前にテストを行うことを推奨します。

**詳細**:

Azure Automationは、PowerShell 7.6ランブックおよび対応するランタイム環境の一般提供（GA）を発表しました。本アップデートの背景には、従来のPowerShellバージョンを利用したスクリプトの保守性やセキュリティ上の課題があり、最新かつサポート対象のランタイム環境への移行を促進することが目的です。これにより、ユーザーは既存の古いスクリプトをPowerShell 7.6対応のランブックへシームレスにアップグレードすることが可能となります。

具体的な変更内容としては、Azure AutomationでPowerShell 7.6ランブックが正式にサポートされるようになり、これに伴い新しいランタイム環境も利用できるようになりました。これにより、PowerShell 7.6の新機能やセキュリティ修正を活用したスクリプトの自動化が実現します。また、Azure CLIコマンドのサポートも強化されていますが、詳細は提供された情報内では明記されていません。

技術的な仕組みとしては、Azure Automationアカウント内でランブックの実行環境としてPowerShell 7.6を選択できるようになっています。これにより、従来のWindows PowerShell 5.1やPowerShell 7.2などのバージョンと並行して、PowerShell 7.6ランブックを運用することが可能です。既存のランブックを新しいランタイム環境に移行する場合は、スクリプトの互換性を確認し、必要に応じて修正を行う必要があります。

活用シナリオとしては、インフラストラクチャの自動構成、リソースのプロビジョニング、定期的なメンテナンスタスクの自動化などが挙げられます。特に、PowerShell 7.6の新機能やモジュールを活用した高度な自動化シナリオの実装が容易になります。

注意点としては、PowerShell 7.6ランブックに移行する際には、従来のバージョンで動作していたスクリプトとの互換性を十分に検証する必要があります。また、利用可能なモジュールやコマンドレットのバージョンにも注意が必要です。

関連するAzureサービスとの連携としては、Azure Automationが提供する各種Runbook、ハイブリッドワーカー、スケジュール機能、Azure Monitorなどと組み合わせて、より柔軟かつ拡張性の高い自動化環境を構築することが可能です。

詳細は公式アップデート情報（https://azure.microsoft.com/updates?id=568102）をご参照ください。

---

### 3. Announcing: Reservation exchanges for Azure services supported by savings plans will no longer be available starting February 1, 2027  

**公開日時**: 2026年07月30日 19:03:21 UTC
**リンク**: [Announcing: Reservation exchanges for Azure services supported by savings plans will no longer be available starting February 1, 2027  ](https://azure.microsoft.com/updates?id=568514)

**アップデートID**: 568514
**情報源**: Azure Updates API

**カテゴリ**: Announcement

**要約**:

- 何が更新されたか  
2027年2月1日より、Azureのセービングプラン（Savings Plans）でカバーされているサービスに対するリザベーション交換（Reservation Exchange）が利用できなくなることが発表されました。

- 主な変更点や新機能  
これまで可能だった、Azureリザベーションの交換（例：VMサイズやリージョンの変更）が、セービングプラン対象サービスでは2027年2月1日以降できなくなります。現時点では、Azure Virtual Machine（VM）などのコンピュートサービスが対象です。

- 影響を受ける対象  
Azureセービングプランの対象となるサービスでリザベーションを利用しているユーザーや組織が影響を受けます。特に、VMリザベーションの柔軟な運用を行っている技術者は注意が必要です。

- 注意点があれば記載  
2027年2月1日以降は、対象サービスのリザベーション交換ができなくなるため、今後のリザベーション購入や運用計画を見直す必要があります。既存のリザベーションの有効期限や運用方針を事前に確認し、必要に応じて早めに対応を検討してください。

**詳細**:

2027年2月1日より、AzureサービスのSavings Plan（セービングプラン）でカバーされているサービスに対して、Azure予約（Reservation）の交換（Exchange）機能が利用できなくなります。本アップデートは、Azureのコスト最適化機能における予約とセービングプランの役割の明確化を目的としています。現時点でこの変更の対象となるサービスは、Azure Virtual Machine（仮想マシン）などのコンピュートサービスの予約です。

Azure予約は、特定のサービスに対して一定期間（通常1年または3年）の利用を事前にコミットすることで、従量課金制よりも割引価格でリソースを利用できる仕組みです。従来、予約の交換機能を利用することで、既存の予約を他のSKUやリージョン、サイズなどに柔軟に変更することが可能でした。しかし、今回のアップデートにより、Savings Planでカバーされているサービスの予約については、この交換機能が廃止されます。これにより、Savings Planと予約の併用や移行の際の柔軟性が制限されることになります。

技術的には、AzureポータルやAPIを通じて予約の管理や交換操作が行われていましたが、2027年2月1日以降はSavings Plan対象サービスの予約交換操作が不可となります。予約の購入やキャンセルなど、他の管理操作については本アップデートの範囲外です。

実際の活用シナリオとしては、これまで仮想マシンの利用状況や要件変更に応じて予約を交換し、コスト最適化を図ることができましたが、今後はSavings Plan対象サービスの予約に関しては交換による柔軟な調整ができなくなります。例えば、仮想マシンのSKUやリージョン変更が必要になった場合、予約交換ではなく新規予約の購入や既存予約のキャンセルを検討する必要があります。

この変更により、Savings Planと予約の選択や運用方針を見直す必要があります。Savings Planは予約よりも柔軟性が高い一方、予約は特定のリソースに対してより高い割引率を提供する場合があります。両者の違いを理解し、今後のコスト管理戦略に反映させることが重要です。

関連するAzureサービスとしては、Azure Virtual Machine以外にも今後Savings Plan対象となるサービスが追加される可能性がありますが、現時点では仮想マシンが主な対象です。アップデートの詳細や最新情報については公式サイト（https://azure.microsoft.com/updates?id=568514）を参照してください。

---

### 4. Public Preview: Symmetric keys on Azure Key Vault Premium

**公開日時**: 2026年07月30日 18:57:18 UTC
**リンク**: [Public Preview: Symmetric keys on Azure Key Vault Premium](https://azure.microsoft.com/updates?id=566746)

**アップデートID**: 566746
**情報源**: Azure Updates API

**カテゴリ**: In preview, Security, Key Vault, Features

**要約**:

- 何が更新されたか  
Azure Key Vault Premiumで「対称鍵（symmetric keys）」の機能がパブリックプレビューとして利用可能になりました。

- 主な変更点や新機能  
新たにoct-HSMキータイプを用いた対称暗号化機能が追加され、AES（Advanced Encryption Standard）による暗号化・復号が可能となりました。これにより、Key Vault Premiumで対称鍵の管理や利用がサポートされます。

- 影響を受ける対象  
Azure Key Vault Premiumを利用している技術者や企業が対象です。特に、対称鍵による暗号化を必要とするアプリケーションやサービスの開発・運用に関わる方に影響があります。

- 注意点があれば記載  
現在はパブリックプレビュー段階のため、本番環境での利用は推奨されません。評価や検証目的で利用し、正式リリースまで運用環境での導入は慎重に検討してください。また、oct-HSMキータイプやAESの仕様に関する詳細は公式ドキュメントを参照してください。

**詳細**:

Azure Key Vault Premiumにおいて、対称鍵（Symmetric Keys）がパブリックプレビューとして提供開始されたことが発表されています。このアップデートの背景には、Azure Key Vaultを利用する企業やパートナーが、より高度な暗号化ニーズに対応するための機能拡張があります。従来のAzure Key Vaultでは主に非対称鍵（RSAやECDSAなど）による暗号化や署名が中心でしたが、今回のアップデートにより、対称鍵を用いた暗号化が可能となり、より幅広いセキュリティ要件に対応できるようになっています。

具体的な機能としては、oct-HSMキータイプと呼ばれる対称鍵がAzure Key Vault Premiumで利用可能となり、Advanced Encryption Standard（AES）を用いた暗号化処理が実施できるようになります。oct-HSMキータイプは、HSM（Hardware Security Module）によって保護される対称鍵であり、これにより鍵の安全な管理と高いセキュリティレベルを実現しています。ユーザーはAzure Key Vault PremiumのAPIやポータルを通じて、対称鍵の生成、管理、利用が可能です。

技術的な仕組みとしては、Azure Key Vault PremiumがHSMをバックエンドに持つことで、対称鍵の生成やストレージ、暗号化・復号処理を安全に実行します。対称鍵はoct-HSMキータイプとして定義され、AES暗号化アルゴリズムを利用したデータの暗号化・復号がサポートされます。APIを通じて暗号化・復号リクエストを送信することで、Azure Key Vault内で安全に処理が完結します。

活用シナリオとしては、アプリケーションやサービスが大量のデータを効率的に暗号化・復号する必要がある場合や、従来の非対称鍵ではパフォーマンスやコスト面で課題があったケースにおいて、対称鍵による暗号化が有効です。例えば、ストレージサービスやデータベースの暗号化、機密情報の一時的な保管など、AESによる高速な暗号化が求められる場面で活用できます。

注意点としては、本機能は現在パブリックプレビュー段階であり、商用利用や本番環境での利用には慎重な検証が必要です。また、oct-HSMキータイプやAES暗号化の利用にあたっては、Azure Key Vault Premiumの利用が前提となるため、Standard SKUでは利用できません。さらに、プレビュー段階では機能やAPIの仕様が変更される可能性があるため、最新のドキュメントやアップデート情報を随時確認する必要があります。

関連するAzureサービスとの連携については、Azure Key Vault Premiumで管理される対称鍵を、Azure StorageやAzure SQL Databaseなどのサービスと組み合わせて利用することで、データの暗号化やセキュリティ強化が実現できます。また、Azure Active Directoryによるアクセス制御や、監査ログの取得など、Key Vaultの既存機能と組み合わせることで、統合的なセキュリティ管理が可能です。

---

### 5. Public Preview: Support for SMB Opportunistic Locking (Oplocks) configuration 

**公開日時**: 2026年07月30日 16:38:15 UTC
**リンク**: [Public Preview: Support for SMB Opportunistic Locking (Oplocks) configuration ](https://azure.microsoft.com/updates?id=568396)

**アップデートID**: 568396
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure NetApp Files, Feature

**要約**:

【何が更新されたか】  
Azure NetApp Filesにおいて、SMB Opportunistic Locking（Oplocks）の設定がパブリックプレビューとして利用可能になりました。

【主な変更点や新機能】  
SMBおよびデュアルプロトコルボリュームに対して、Oplocksの有効・無効を設定できるようになりました。OplocksはSMBクライアントのキャッシュ性能を向上させる機能で、デフォルトで有効化されています。新規ボリューム作成時だけでなく、既存ボリュームに対してもOplocksの設定変更が可能です。

【影響を受ける対象】  
Azure NetApp Filesを利用しているSMBまたはデュアルプロトコルボリュームの管理者や技術者が対象となります。特に、SMBクライアントのキャッシュ動作やファイル共有のパフォーマンスを最適化したい場合に有用です。

【注意点】  
Oplocksはクライアント側のキャッシュを強化しますが、アプリケーションによっては競合やデータ整合性の問題が発生する場合があります。利用時はアプリケーションの動作要件や運用ポリシーに注意して設定を行ってください。

**詳細**:

Azure NetApp Filesにおいて、SMB Opportunistic Locking（Oplocks）の構成がサポートされる機能がパブリックプレビューとして提供開始されました。本アップデートの背景には、SMBプロトコルを利用するファイル共有環境において、クライアント側のキャッシュ効率を向上させ、ネットワークトラフィックの削減やパフォーマンス向上を図るニーズがあります。OplocksはSMBクライアントがファイルのロック状態を管理することで、ローカルキャッシュの利用を最適化し、ファイルアクセスの競合を減らす役割を担っています。

今回のアップデートにより、Azure NetApp FilesのSMBボリュームおよびデュアルプロトコルボリュームに対して、Oplocksの有効・無効を設定できるようになりました。Oplocksはデフォルトで有効化されていますが、ボリューム作成時や既存ボリュームの設定変更時に管理者が任意に構成することが可能です。これにより、アプリケーションやワークロードの要件に応じて、柔軟にSMBファイル共有の動作を調整できます。

技術的な仕組みとしては、SMB Oplocksはクライアントがファイルを開く際にロックを取得し、他のクライアントからのアクセスが発生した場合にロックを解除することで、キャッシュの整合性を保ちます。Azure NetApp Filesでは、SMBプロトコルの標準機能としてOplocksをサポートし、管理者はAzureポータルやAPIを通じて設定を変更できます。

活用シナリオとしては、例えばCADデータや大容量ファイルを複数ユーザーが共有する環境、あるいは頻繁なファイル更新が発生するアプリケーションにおいて、Oplocksを有効化することでクライアント側のキャッシュ性能を最大化し、ネットワーク負荷を軽減できます。一方で、ファイルの同時編集や競合が多い環境ではOplocksを無効化することで、データ整合性の確保を優先することも可能です。

注意点として、Oplocksの設定はボリューム単位で行われるため、アプリケーションの特性や利用ユーザーの動作に応じて適切な構成を選択する必要があります。また、Oplocksの有効化・無効化は既存ボリュームにも適用可能ですが、設定変更時にはファイルアクセス中のクライアント動作に影響を与える場合があるため、事前に影響範囲を確認することが推奨されます。

本機能はAzure NetApp FilesのSMBおよびデュアルプロトコルボリュームに限定されており、他のAzureストレージサービス（例：Azure Files等）とは直接の連携や影響はありません。Azure NetApp Filesを利用した高性能ファイル共有環境において、SMB Oplocksの柔軟な構成が可能となることで、より多様なワークロードに対応できるようになりました。

---


*このレポートは自動生成されました - 2026-07-31 12:02:06 JST*