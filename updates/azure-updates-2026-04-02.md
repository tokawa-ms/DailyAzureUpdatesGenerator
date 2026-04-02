# 2026年04月02日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年04月02日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 7 件

## 更新一覧

### 1. Retirement: Service Fabric support for Windows Server 2022 ends on March 31, 2027 - upgrade to Windows Server 2025

**公開日時**: 2026年04月01日 21:00:19 UTC
**リンク**: [Retirement: Service Fabric support for Windows Server 2022 ends on March 31, 2027 - upgrade to Windows Server 2025](https://azure.microsoft.com/updates?id=558247)

**アップデートID**: 558247
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, Azure Service Fabric, Retirements

**要約**:

- 何が更新されたか  
Azure Service FabricのWindows Server 2022サポートが2027年3月31日で終了することが発表されました。

- 主な変更点や新機能  
Windows Server 2022上で稼働しているService Fabricクラスタのサポートが終了し、今後はWindows Server 2025へのアップグレードが必要となります。これにより、Service FabricのWindows OSイメージサポートポリシーが最新OSバージョンに合わせて更新されます。

- 影響を受ける対象  
現在Windows Server 2022上でService Fabricクラスタを運用している全てのユーザーや組織が対象です。

- 注意点があれば記載  
2027年3月31日以降、Windows Server 2022上のService Fabricクラスタはサポート対象外となります。引き続きサポートを受けるためには、事前にWindows Server 2025へのアップグレードを計画・実施する必要があります。サポート切れの環境ではセキュリティリスクや障害時の対応が受けられなくなるため、早めの対応を推奨します。

**詳細**:

Azure Service Fabricは、分散型アプリケーションの構築と管理を支援するプラットフォームとして多くの企業で利用されています。今回のアップデートでは、Service FabricがWindows Server 2022上で稼働するクラスタのサポートを2027年3月31日で終了することが発表されました。これにより、Windows Server 2022を基盤としたService Fabricクラスタを運用しているユーザーは、サポート終了日までにWindows Server 2025へアップグレードする必要があります。この変更は、Service FabricのWindows OSイメージサポートモードと整合性を持たせるために実施されるものです。

具体的な変更内容としては、2027年3月31日以降、Windows Server 2022上で稼働するService Fabricクラスタは公式サポートの対象外となります。これにより、セキュリティパッチやバグフィックス、技術的な問い合わせ対応などが受けられなくなります。サポート継続のためには、クラスタのOSをWindows Server 2025に移行することが必須となります。技術的な仕組みとしては、Service Fabricクラスタのノードを新しいOSイメージに置き換える形でアップグレードを実施する必要があります。通常、クラスタのローリングアップグレードを活用し、ダウンタイムを最小限に抑えながらノードごとにOSを更新することが推奨されます。

Service Fabricはマイクロサービスアーキテクチャの実装や、ステートフル／ステートレスサービスの運用、アプリケーションの自動スケーリングなど、幅広いシナリオで利用されています。今回のアップデートにより、これらのシステムをWindows Server 2022上で運用している場合は、計画的なOSアップグレードが求められます。アップグレード作業時には、クラスタの構成やアプリケーションの互換性、バックアップ体制などを事前に確認し、障害発生時のリカバリ手順を整備しておくことが重要です。

注意点として、サポート終了日以降はWindows Server 2022上のService Fabricクラスタに対する公式サポートが完全に停止されるため、運用リスクが高まります。また、OSアップグレード時にはクラスタの安定性やアプリケーションの動作検証を十分に行う必要があります。関連するAzureサービスとしては、Azure Virtual MachinesやAzure Monitor、Azure Backupなどが挙げられます。これらのサービスと連携し、クラスタの監視やバックアップ、障害対応を強化することが推奨されます。

以上の内容から、Service FabricクラスタをWindows Server 2022上で運用している技術者は、2027年3月31日までにWindows Server 2025へのアップグレード計画を立て、安定した運用を継続できるよう準備を進める必要があります。

---

### 2. Retirement: Service Fabric support for Windows Server 2019 ends on March 31, 2027 - upgrade to Windows Server 2025

**公開日時**: 2026年04月01日 20:30:41 UTC
**リンク**: [Retirement: Service Fabric support for Windows Server 2019 ends on March 31, 2027 - upgrade to Windows Server 2025](https://azure.microsoft.com/updates?id=558246)

**アップデートID**: 558246
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, Azure Service Fabric, Retirements

**要約**:

- 何が更新されたか  
Azure Service Fabricが、Windows Server 2019上で稼働する全てのクラスターのサポートを2027年3月31日で終了すると発表されました。

- 主な変更点や新機能  
Windows Server 2019のサポート終了に伴い、Service Fabricクラスターのサポート対象OSがWindows Server 2025に移行します。これにより、今後はWindows Server 2025上での運用が必要となります。

- 影響を受ける対象  
現在、Windows Server 2019上でService Fabricクラスターを運用している全てのユーザーおよび組織が対象です。これらの環境は、2027年3月31日以降はサポート対象外となります。

- 注意点  
サポート終了日までにWindows Server 2025へのアップグレードを実施しない場合、セキュリティアップデートや技術サポートが受けられなくなります。運用中のService Fabricクラスターは、計画的にOSのアップグレードを進める必要があります。  
詳細は公式情報（https://azure.microsoft.com/updates?id=558246）をご確認ください。

**詳細**:

本アップデートは、Azure Service FabricにおけるWindows Server 2019のサポート終了に関する重要な通知です。2027年3月31日をもって、Windows Server 2019上で稼働しているすべてのService Fabricクラスターのサポートが終了します。これに伴い、サポートを継続するためには、同日までにWindows Server 2025へのアップグレードが必要となります。この変更は、Service FabricのWindows OSイメージサポートポリシーに準拠したものであり、最新のOSバージョンに対する継続的なサポートとセキュリティ確保を目的としています。

具体的な変更内容としては、Windows Server 2019を基盤としたService Fabricクラスターの新規作成や既存クラスターの運用に対する公式サポートが終了する点が挙げられます。これにより、2027年3月31日以降は、セキュリティアップデートやバグフィックス、技術サポートを受けることができなくなります。したがって、現在Windows Server 2019上でService Fabricクラスターを運用している場合は、計画的にWindows Server 2025への移行作業を進める必要があります。

技術的な実装方法としては、既存のService FabricクラスターをWindows Server 2025ベースのノードに移行することが求められます。移行にあたっては、クラスターのバックアップ、アプリケーションの互換性検証、段階的なノードの置き換えなどが必要となります。Service Fabricのアップグレード手順やベストプラクティスに従い、ダウンタイムの最小化やサービスの継続性を確保しながら移行を実施することが推奨されます。

Service Fabricは、マイクロサービスアーキテクチャを採用した分散アプリケーションの構築や運用に広く利用されています。たとえば、ミッションクリティカルな業務システムや大規模なWebサービス、IoTバックエンドなど、多様なシナリオで活用されています。今回のアップデートにより、これらのシステムを最新のOS基盤で安全かつ安定的に運用し続けるためには、早期の移行対応が不可欠です。

注意点として、サポート終了後にWindows Server 2019上で稼働し続ける場合、セキュリティリスクや障害発生時のサポートが受けられない点に留意する必要があります。また、移行作業に伴うアプリケーションやミドルウェアの互換性検証も重要です。関連するAzureサービスとしては、Azure Resource Managerによるインフラ管理や、Azure Monitorによる監視機能などがService Fabricクラスターと連携可能です。移行後もこれらのサービスを活用することで、運用管理の効率化や可用性向上が期待できます。

以上のように、今回のアップデートはService Fabricクラスターの運用基盤を最新のWindows Serverバージョンへ移行することを促すものであり、安定したサービス提供とセキュリティ確保の観点からも早期対応が求められます。

---

### 3. Public Preview: Unlock Client-Side Configuration at Scale with Azure App Configuration and Azure Front Door

**公開日時**: 2026年04月01日 19:00:05 UTC
**リンク**: [Public Preview: Unlock Client-Side Configuration at Scale with Azure App Configuration and Azure Front Door](https://azure.microsoft.com/updates?id=537234)

**アップデートID**: 537234
**情報源**: Azure Updates API

**カテゴリ**: In preview, Containers, Developer tools, Mobile, Security, Web, App Configuration, Features, Microsoft Ignite

**要約**:

- 何が更新されたか  
Azure App ConfigurationとAzure Front Doorの統合により、クライアントサイドアプリケーション向けの動的な構成配信がパブリックプレビューとして提供開始されました。

- 主な変更点や新機能  
Azure App Configurationで管理しているアプリケーション設定を、Azure Front DoorのCDNスケールでクライアントサイドアプリケーションに安全に配信できるようになりました。これにより、設定の即時反映やグローバルなスケーラビリティ、セキュアな構成管理が実現します。

- 影響を受ける対象  
フロントエンド（クライアントサイド）アプリケーションをAzure上で運用している開発者や運用担当者が主な対象です。特に、グローバルに分散したユーザー向けに設定を迅速かつ安全に配信したい場合に有効です。

- 注意点があれば記載  
本機能はパブリックプレビュー段階であり、本番環境での利用には十分な検証が必要です。また、セキュリティ設定やアクセス制御の構成に注意してください。

**詳細**:

本アップデートは、Azure App ConfigurationとAzure Front Doorの統合による新機能のパブリックプレビュー提供を目的としています。これにより、動的な構成情報をクライアントサイドアプリケーションへ直接、安全かつCDNスケールで配信できるようになりました。従来、アプリケーション構成は主にサーバーサイドで管理されていましたが、今回のアップデートにより、クライアントサイドでも柔軟かつリアルタイムに構成情報を取得・反映できるようになり、モダンなアプリケーション開発における重要な機能が解放されます。

具体的な機能としては、Azure App Configurationに保存された設定データをAzure Front Door経由で配信することで、グローバルな分散環境でも高速かつセキュアな構成情報の提供が可能となります。Azure Front DoorはCDN機能を持つため、世界中のエンドユーザーに対して低遅延で構成情報を届けることができます。また、App Configurationの管理機能により、設定値のバージョン管理やロールベースのアクセス制御も適用されるため、セキュアな運用が担保されます。

技術的な仕組みとしては、Azure App ConfigurationのエンドポイントがAzure Front Doorに統合され、クライアントアプリケーションはFront Door経由で構成情報を取得します。これにより、App Configurationへの直接アクセスを避けつつ、Front Doorのキャッシュやセキュリティ機能を活用したスケーラブルな配信が実現します。実装方法としては、クライアントアプリケーション側でFront Doorのエンドポイントを参照し、必要な構成情報をリクエストする形となります。

活用シナリオとしては、SPA（Single Page Application）やモバイルアプリケーションなど、クライアントサイドで動的に設定値を変更する必要があるケースに有効です。例えば、機能フラグやUI構成、APIエンドポイントの切り替えなど、運用中のアプリケーションに対して即時に設定変更を反映させたい場合に利用できます。また、グローバル展開されているサービスにおいて、地域ごとに異なる設定値を配信する用途にも適しています。

注意点としては、パブリックプレビュー段階であるため、商用環境での利用には慎重な検証が必要です。また、Front Doorのキャッシュ設定やApp Configurationのアクセス制御を適切に構成しないと、意図しない設定値の配信やセキュリティリスクが発生する可能性があります。

関連するAzureサービスとしては、Azure App Configurationが構成管理の中心となり、Azure Front Doorが配信経路として機能します。他にも、Azure Active Directoryによる認証や、Azure Monitorによる監視機能と組み合わせることで、より高度な運用が可能です。

以上が本アップデートの技術者向け詳細説明となります。

---

### 4. Generally Available: Azure Data Box enhances compliance with automatic Secure Erasure Certificates

**公開日時**: 2026年04月01日 18:30:16 UTC
**リンク**: [Generally Available: Azure Data Box enhances compliance with automatic Secure Erasure Certificates](https://azure.microsoft.com/updates?id=559772)

**アップデートID**: 559772
**情報源**: Azure Updates API

**カテゴリ**: Launched, Migration, Storage, Azure Data Box, Features

**要約**:

【何が更新されたか】  
Azure Data Boxが、デバイス内のデータ消去完了後に自動で「Secure Erasure Certificate（安全消去証明書）」を生成・ダウンロードできる機能を正式リリースしました。

【主な変更点や新機能】  
これまで手動対応だった消去証明書の発行が自動化され、各注文ごとに証明書が提供されます。証明書は、NIST 800-88 Revision 2の基準に準拠した安全なデータ消去を証明します。

【影響を受ける対象】  
Azure Data Boxを利用してデータ移行やバックアップを行う企業や技術者が対象です。特にコンプライアンス要件や監査対応が必要な組織にとって、証明書の自動発行は重要な機能となります。

【注意点】  
証明書は消去完了後にダウンロード可能です。NIST 800-88 Revision 2準拠の証明書が必要な場合は、必ず消去完了後に証明書を取得・保管してください。証明書の取得方法や管理については公式ドキュメントを参照することを推奨します。

**詳細**:

本アップデートは、Azure Data Boxにおいて自動的にSecure Erasure Certificate（セキュア消去証明書）が生成され、各注文完了時にダウンロード可能となったことを示しています。これにより、デバイス上のすべてのデータがNIST 800-88 Revision 2規格に準拠して安全に消去されたことを証明する手段が提供されます。アップデートの背景には、データ消去の証跡管理やコンプライアンス要件への対応強化という目的があります。特に、厳格な情報管理や監査対応が求められる業界において、データ消去の確実性を第三者に証明するニーズが高まっていることが背景にあります。

具体的な機能としては、Azure Data Boxの注文が完了し、デバイスの返却およびデータ消去プロセスが終了した際に、ユーザーはAzureポータルなどからSecure Erasure Certificateをダウンロードできるようになります。この証明書には、消去がNIST 800-88 Revision 2に準拠して実施されたことが明記されており、監査や社内外のコンプライアンス報告に利用できます。

技術的な仕組みとしては、Azure Data Boxのデータ消去プロセスが完了した際に、Azure側で自動的に証明書が生成されるフローとなっています。証明書の発行は各注文ごとに行われ、ユーザーはこれを自身の管理システムや監査資料として保存・活用できます。

活用シナリオとしては、例えば金融機関や医療機関など、厳格なデータガバナンスが求められる現場でのデータ移行やバックアップ作業後、確実なデータ消去とその証明が必要な場合に有効です。また、外部委託先や監査法人への証跡提出が求められるケースでも、証明書を活用することでスムーズな対応が可能となります。

注意点としては、証明書のダウンロードが各注文ごとであるため、複数デバイスや複数回の利用時にはそれぞれの証明書を適切に管理する必要があります。また、証明書の内容やフォーマットについてはAzureの仕様に準拠するため、独自の記載事項追加などはできません。

関連するAzureサービスとの連携については、Azure Data Boxを利用したデータ移行やバックアップ、リストアのワークフローにおいて、データ消去証明書の取得・管理が追加される形となります。これにより、Azure上でのデータライフサイクル管理やコンプライアンス対応がより強化されます。

詳細は公式アップデート情報（https://azure.microsoft.com/updates?id=559772）を参照してください。

---

### 5. Generally Available: Azure Data Box now supports Azure Files Provisioned v2

**公開日時**: 2026年04月01日 18:15:44 UTC
**リンク**: [Generally Available: Azure Data Box now supports Azure Files Provisioned v2](https://azure.microsoft.com/updates?id=559767)

**アップデートID**: 559767
**情報源**: Azure Updates API

**カテゴリ**: Launched, Migration, Storage, Azure Data Box, Features

**要約**:

- 何が更新されたか  
Azure Data Boxが、Azure Files Provisioned v2ストレージアカウントへのデータインジェスト（データ取り込み）をサポートするようになりました。

- 主な変更点や新機能  
これまでAzure Data Boxは従来のAzure Filesストレージアカウントへのデータ移行に対応していましたが、今回から新しい課金モデルであるAzure Files Provisioned v2にも対応しました。Provisioned v2では、容量、IOPS、スループットをユーザーが指定してプロビジョニングし、それに応じた課金が行われるため、より柔軟なリソース管理が可能です。

- 影響を受ける対象  
Azure Data Boxを利用して大量データをAzure Filesに移行しているユーザーや、今後Provisioned v2ストレージアカウントを利用予定の組織・技術者が対象となります。

- 注意点があれば記載  
今回のアップデートはデータ移行の柔軟性向上に寄与しますが、Provisioned v2特有の課金体系やパフォーマンス要件については事前に確認することを推奨します。既存のData Boxワークフローに影響がないかも合わせてご確認ください。

**詳細**:

本アップデートは、Azure Data BoxがAzure Files Provisioned v2ストレージアカウントへのデータインジェスト（取り込み）をサポートするようになったことを示しています。これにより、オンプレミス環境などから大容量データを物理デバイス経由でAzure Files Provisioned v2に効率的に移行できるようになります。

Azure Files Provisioned v2は、従来のAzure Filesと異なり、ユーザーが必要な容量、IOPS（Input/Output Operations Per Second）、およびスループット（帯域幅）を事前にプロビジョニングし、そのリソースに対して課金される新しい課金モデルです。これにより、ワークロードに応じて柔軟にリソースを調整できるため、パフォーマンス要件が厳しいシナリオや予測可能なコスト管理が求められるケースに適しています。

今回のアップデートにより、Azure Data Boxデバイスを利用して、Azure Files Provisioned v2ストレージアカウントに直接データを取り込むことが可能になりました。技術的には、Data Boxデバイスにデータをコピーした後、Azure側でデータがAzure Files Provisioned v2アカウントに自動的にアップロードされます。これにより、従来のネットワーク経由の転送に比べて、ネットワーク帯域の制約や転送時間の問題を回避しつつ、安全かつ大容量のデータ移行が実現できます。

この機能は、例えばオンプレミスのファイルサーバーからクラウドへの大規模なデータ移行、データセンター統合、災害復旧のためのデータバックアップなど、さまざまなシナリオで活用できます。また、Azure Files Provisioned v2のプロビジョニングモデルを利用することで、移行後のストレージパフォーマンスやコストの最適化も図れます。

注意点としては、Azure Data BoxおよびAzure Files Provisioned v2の各サービスが提供されているリージョンや、サポートされるファイルサイズ・ファイル数、プロビジョニング可能なリソース上限など、各サービス固有の制限事項を事前に確認する必要があります。また、Data Boxの利用には事前の申請やデバイスの配送・返却などのプロセスが含まれるため、スケジュール管理も重要です。

Azure Data Boxは、Azure Blob Storageや他のストレージサービスとも連携可能であり、今回のアップデートによりAzure Files Provisioned v2との連携が強化されました。これにより、クラウドストレージの選択肢が広がり、より多様なデータ移行シナリオに対応できるようになっています。

---

### 6. Public Preview: Azure NetApp Files storage with cool access enhancement 

**公開日時**: 2026年04月01日 18:15:44 UTC
**リンク**: [Public Preview: Azure NetApp Files storage with cool access enhancement ](https://azure.microsoft.com/updates?id=559504)

**アップデートID**: 559504
**情報源**: Azure Updates API

**カテゴリ**: In development, Storage, Azure NetApp Files, Features

**要約**:

【何が更新されたか】  
Azure NetApp Filesにおいて、PremiumおよびUltraサービスレベルで「cool access」機能がパブリックプレビューとして追加されました。

【主な変更点や新機能】  
QoS（Quality of Service）が「cool access」対応にアップデートされ、ホットデータとクールデータの混在ワークロードにおいて、パフォーマンスとコストのバランスが向上します。データがクールストレージに移動すると、スループットが自動的に調整され、ホットティアのパフォーマンスを維持しつつ、コスト効率を高めることが可能です。

【影響を受ける対象】  
PremiumおよびUltraサービスレベルのAzure NetApp Filesを利用しているユーザーが対象です。特に、ホットデータとクールデータが混在する環境でストレージコストとパフォーマンス最適化を求める技術者にとって有用な機能です。

【注意点】  
本機能はパブリックプレビュー段階のため、商用利用や本番環境での導入時には十分な検証が必要です。また、スループットの自動調整による挙動や、クールアクセスの適用範囲について事前に確認することを推奨します。

**詳細**:

本アップデートは、「Azure NetApp Files」において、PremiumおよびUltraサービスレベルで「cool access」が有効化された場合のQoS（Quality of Service）機能の強化を目的としています。これにより、Azure NetApp Filesはホットデータとクールデータが混在するワークロードに対して、パフォーマンスとコストのバランスをより効率的に最適化できるようになります。

具体的には、cool accessが有効な状態でPremiumまたはUltraサービスレベルを利用する際、データがクールストレージに移動するとスループット（スループット性能）が自動的に調整されます。この自動調整により、データがホットティアに存在する場合の高いパフォーマンスを維持しつつ、クールティアに移行したデータについてはコスト効率を重視したリソース配分が行われます。これにより、ホットデータへのアクセス時には従来通りの高いI/O性能が確保され、クールデータへのアクセス時にはコスト最適化が図られます。

技術的な仕組みとしては、Azure NetApp FilesのQoS制御がデータのアクセス頻度やストレージティアの状態に応じて、スループットの割り当てを動的に変更します。これにより、ユーザーはワークロードの特性に応じて自動的に最適なパフォーマンスとコストのバランスを享受することが可能です。実装面では、ユーザーが明示的にスループットの調整を行う必要はなく、システム側で自動的に最適化処理が行われます。

活用シナリオとしては、アクセス頻度が高いホットデータと、長期保存やアクセス頻度が低いクールデータが混在するエンタープライズ環境や、データライフサイクル管理を重視するシステムで有効です。たとえば、分析基盤やバックアップ用途、アーカイブデータの管理など、データアクセスパターンが多様な環境でコストとパフォーマンスの最適化が求められる場合に適しています。

注意点としては、本機能はPremiumおよびUltraサービスレベルでのみ利用可能であり、cool accessが有効化されている必要があります。また、詳細な制限事項や設定方法については、公式ドキュメントの確認が推奨されます。

関連するAzureサービスとしては、Azure NetApp Files自体がAzureの他のストレージサービスやデータ分析基盤と連携して利用されるケースが多く、今回のQoSアップデートにより、より柔軟かつコスト効率の高いストレージ運用が可能となります。

---

### 7. Retirement: Select Azure AI Language Features 

**公開日時**: 2026年04月01日 18:00:10 UTC
**リンク**: [Retirement: Select Azure AI Language Features ](https://azure.microsoft.com/updates?id=557394)

**アップデートID**: 557394
**情報源**: Azure Updates API

**カテゴリ**: AI + machine learning, Azure AI Language, Retirements

**要約**:

【何が更新されたか】  
Microsoftは2027年3月20日に、Azure AI Languageの8つの機能を廃止することを発表しました。

【主な変更点や新機能】  
今回のアップデートでは、以下の機能が廃止対象となります：  
- Key Phrase Extraction  
- Sentiment Analysis and Opinion Mining  
- Custom Text Classification  
- Conversational Language Understanding (CLU)  
- Custom Question Answering (CQA)  
- Orchestrator  
（残り2つの機能についてはリンク先でご確認ください）

【影響を受ける対象】  
これらの機能を利用しているアプリケーションやサービスは、2027年3月20日以降利用できなくなります。該当APIやサービスを組み込んでいるシステムの開発者や運用担当者が影響を受けます。

【注意点】  
廃止対象機能を利用している場合は、今後の移行計画や代替機能の検討が必要です。Microsoftからの追加情報や移行ガイドを随時確認し、早めに対応を進めることを推奨します。

**詳細**:

2027年3月20日をもって、MicrosoftはAzure AI Languageの8つの機能を廃止することを発表しました。対象となる機能は、Key Phrase Extraction、Sentiment Analysis and Opinion Mining、Custom Text Classification、Conversational Language Understanding (CLU)、Custom Question Answering (CQA)、およびOrchestrなどです。このアップデートの背景には、AIサービスの進化や機能統合、あるいは新たなサービスへの移行が考えられますが、詳細な目的については公式情報に記載されていません。

廃止される各機能は、自然言語処理（NLP）分野で広く利用されてきました。たとえばKey Phrase Extractionはテキストから重要なキーワードを自動抽出する機能であり、Sentiment Analysis and Opinion Miningは文章の感情や意見を判定するために利用されてきました。Custom Text Classificationはユーザー独自の分類モデルを作成し、特定の業務要件に合わせたテキスト分類を実現していました。また、Conversational Language Understanding (CLU)は会話型AIの構築に不可欠な発話理解を担い、Custom Question Answering (CQA)はFAQやドキュメントからの自動応答システムの実装に用いられてきました。Orchestrは複数の言語機能を統合的に制御する役割を果たしていました。

これらの機能は、Azure AI LanguageサービスのREST APIやSDKを通じて実装されており、アプリケーションや業務システムへの組み込みが容易でした。たとえば、カスタマーサポートの自動化、SNS分析、ドキュメント分類、チャットボットの会話理解など、さまざまな業務シナリオで活用されてきました。

今回のリタイアメントにより、2027年3月20日以降はこれらの機能が利用できなくなります。既存システムでこれらの機能を利用している場合は、代替手段の検討や移行計画が必要です。特に、APIのエンドポイントやSDKの依存関係がある場合は、早期に対応策を講じることが推奨されます。

Azure AI Languageの他の機能や、関連するAzure Cognitive Servicesとの連携も考慮する必要があります。廃止対象の機能を利用しているワークフローやアプリケーションについては、今後のサポート状況や代替サービスの情報を随時確認し、適切な移行を進めてください。

詳細については、公式アップデートページ（https://azure.microsoft.com/updates?id=557394）を参照し、最新情報を確認することが重要です。

---


*このレポートは自動生成されました - 2026-04-02 12:02:56 JST*