# 2026年07月07日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年07月07日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Generally Available: Microsoft Entra ID-based access for Azure Blob Storage SFTP

**公開日時**: 2026年07月06日 15:54:08 UTC
**リンク**: [Generally Available: Microsoft Entra ID-based access for Azure Blob Storage SFTP](https://azure.microsoft.com/updates?id=567085)

**アップデートID**: 567085
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Blob Storage, Features

**要約**:

【何が更新されたか】  
Azure Blob StorageのSFTP接続において、Microsoft Entra ID（旧Azure AD）ベースのアクセスが全リージョンで一般提供（GA）されました。

【主な変更点や新機能】  
従来のローカルユーザー管理に加え、Entra IDのユーザー（ゲストユーザーを含むEntra External Identities）を利用して、SFTP経由でAzure Blob Storageへ安全にアクセスできるようになりました。これにより、ID管理や認証の一元化、セキュリティ強化が可能です。

【影響を受ける対象】  
Azure Blob StorageをSFTPで利用する組織や技術者、特にEntra IDによるユーザー管理を実施している環境が対象となります。ゲストユーザーや外部ユーザーとの連携が必要なケースにも有効です。

【注意点】  
Entra IDベースのアクセスを利用する際は、既存のローカルユーザー管理との違いや、Entra External Identitiesの設定・権限管理に注意が必要です。詳細な設定や運用方法は公式ドキュメントを参照してください。

**詳細**:

Microsoft Entra ID-based access for Azure Blob Storage SFTPが全リージョンで一般提供となりました。本アップデートの背景には、Azure Blob Storageに対するSFTP（Secure File Transfer Protocol）接続時の認証方式の強化と柔軟性向上があります。従来、SFTP接続にはローカルユーザーやストレージアカウントキーなどの認証方式が主に用いられていましたが、今回のアップデートにより、Microsoft Entra ID（旧Azure Active Directory）を用いた認証が可能となりました。これにより、組織内ユーザーのみならず、Entra External Identitiesを活用したゲストユーザーも含め、よりセキュアかつ統合的なアクセス管理が実現します。

具体的な機能としては、Azure Blob StorageのSFTPエンドポイントに対して、Entra IDのアイデンティティを用いた認証がサポートされます。これにより、ユーザー管理やアクセス制御をEntra ID側で一元化でき、既存のID管理ポリシーや多要素認証、条件付きアクセスなどのセキュリティ機能を活用することが可能です。また、ゲストユーザーのアクセスもEntra External Identitiesを通じて許可できるため、外部パートナーや委託先とのファイル共有シナリオにも対応します。

技術的な仕組みとしては、Azure Blob StorageのSFTP機能とEntra IDの認証基盤が連携し、SFTP接続時にEntra IDによる認証プロセスが実行されます。ユーザーはEntra IDの資格情報を用いてSFTPクライアントから接続し、認証後にBlob Storage上のデータにアクセスできます。これにより、従来のローカルユーザー管理に比べて、組織全体のID管理ポリシーと連動したアクセス制御が可能となります。

活用シナリオとしては、企業内のファイル転送や外部との安全なデータ共有、システム間連携などが挙げられます。特に、外部ゲストユーザーを含めたアクセス管理が求められる場合や、Entra IDによる統合認証を活用したセキュリティ強化を図りたい場合に有効です。

注意点としては、Entra ID認証を利用するためには、Blob Storage側でSFTP機能とEntra ID連携の設定が必要です。また、Entra IDベースのアクセス制御を適切に設計しないと、不要なアクセス権限が付与されるリスクがあります。既存のローカルユーザー認証との併用や移行時には、アクセス権限の整理やポリシーの見直しが重要です。

関連するAzureサービスとしては、Microsoft Entra ID（旧Azure Active Directory）、Azure Blob Storage、Entra External Identitiesが挙げられます。これらのサービスを組み合わせることで、クラウド上でのファイル転送やデータ共有のセキュリティと管理性を大幅に向上させることができます。

---

### 2. Generally Available: Support 5x churn in Azure Site Recovery

**公開日時**: 2026年07月06日 15:00:33 UTC
**リンク**: [Generally Available: Support 5x churn in Azure Site Recovery](https://azure.microsoft.com/updates?id=566966)

**アップデートID**: 566966
**情報源**: Azure Updates API

**カテゴリ**: Launched, Management and governance, Migration, Azure Site Recovery, Features, Compliance, Management

**要約**:

【Azure Update要約】

- 何が更新されたか  
Azure Site Recoveryが、1仮想マシン（VM）あたり最大5倍のデータ変更量（churn）、すなわち500MB/sまでのデータ転送をサポートするようになりました。

- 主な変更点や新機能  
これまでより高いI/O負荷のワークロードに対応できるようになり、高速で大量のデータ変更が発生するアプリケーションでも、Azure Site Recoveryによる災害復旧が可能となりました。これにより、ミッションクリティカルなシステムや高IOPSが求められる業務アプリケーションの保護範囲が大幅に拡大します。

- 影響を受ける対象  
高I/Oワークロードを持つ仮想マシンをAzure Site Recoveryで保護しているユーザーや、今後導入を検討している技術者が主な対象です。特に、金融、製造、医療など大量データ処理が必要な業種で恩恵を受けます。

- 注意点があれば記載  
新しいchurn上限（500MB/s/VM）を活用する際は、ネットワーク帯域やストレージ性能などインフラ要件を事前に確認してください。また、既存環境での設定変更やパフォーマンス影響についても十分に検証することを推奨します。

**詳細**:

Azure Site Recoveryは、災害復旧（DR）ソリューションとして広く利用されているサービスですが、今回のアップデートにより、1仮想マシン（VM）あたり最大5倍のデータチャーン、すなわち500MB/sのチャーンレートをサポートするようになりました。このアップデートの背景には、企業のITインフラにおいて高IOPS（Input/Output Operations Per Second）を要求するワークロードが増加していることが挙げられます。従来のチャーンレート制限では、高負荷なアプリケーションやデータベースの災害復旧に十分な性能を提供できない場面がありましたが、今回の拡張により、より多くのデータ変更が発生するシステムにも対応可能となりました。

具体的な機能変更としては、Azure Site Recoveryが1VMあたり最大500MB/sのチャーンレートをサポートする点が挙げられます。これにより、データの変更量が多いアプリケーションや、リアルタイム性が求められるシステムのレプリケーションが可能となり、より堅牢な災害復旧体制を構築できます。技術的には、Azure Site RecoveryはVMのデータ変更を継続的にキャプチャし、Azure上のレプリカに転送することで、障害発生時の迅速な復旧を実現しています。今回のアップデートでは、このデータ転送の最大速度が大幅に向上したため、レプリケーションの遅延が減少し、復旧ポイントの精度も高まります。

活用シナリオとしては、高IOPSを必要とするデータベースサーバーや、トランザクション量が多い業務システム、リアルタイム分析基盤などが挙げられます。これらのシステムでは、短時間で大量のデータ変更が発生するため、従来のチャーンレート制限では十分な災害復旧対策が困難でしたが、今回のアップデートにより、より広範なワークロードに対してAzure Site Recoveryを適用できるようになりました。

注意点としては、チャーンレートの増加に伴い、ネットワーク帯域やストレージ性能、レプリケーション先のAzure環境のリソース設計が重要となります。高チャーンレートを活用する場合は、十分な帯域幅とストレージIOPSを確保する必要があります。また、レプリケーションの設定や監視、障害発生時の復旧手順についても事前に検証しておくことが推奨されます。

関連するAzureサービスとしては、Azure BackupやAzure Storage、Azure Virtual Machinesなどが挙げられます。これらのサービスと組み合わせることで、バックアップと災害復旧の二重の保護体制を構築することが可能です。今回のアップデートにより、Azure Site Recoveryはより多様なシステムに対して高性能なDRソリューションを提供できるようになりました。

---


*このレポートは自動生成されました - 2026-07-07 12:01:11 JST*