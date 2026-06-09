# 2026年06月09日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年06月09日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 7 件

## 更新一覧

### 1. Update: Minimum billable object size for cooler storage tiers

**公開日時**: 2026年06月08日 23:45:02 UTC
**リンク**: [Update: Minimum billable object size for cooler storage tiers](https://azure.microsoft.com/updates?id=559756)

**アップデートID**: 559756
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Analytics, Azure Blob Storage, Azure Data Lake Storage, Pricing & Offerings

**要約**:

【何が更新されたか】  
Azure Storageのクーラー（Cool）、コールド（Cold）、アーカイブ（Archive）アクセスティアにおける「最小課金オブジェクトサイズ」の導入が一時停止されました。

【主な変更点や新機能】  
2026年7月1日から予定されていた、各アクセスティアでの最小課金オブジェクトサイズの新しい課金方式は導入されません。これにより、現行の課金方法が継続されます。

【影響を受ける対象】  
Cool、Cold、Archiveアクセスティアを利用している新規および既存のAzure Storageアカウントが対象です。これらのストレージ利用者は、2026年7月1日以降も課金方法の変更による影響を受けません。

【注意点】  
今後の課金方式に関する最新情報は、Microsoftから改めて通知される予定です。ストレージ利用者は公式アップデートを随時確認してください。現時点では、課金方法の変更や追加対応は不要です。

**詳細**:

今回のAzure Updateは、「cool」「cold」「archive」アクセスティアにおける最小課金オブジェクトサイズの導入についての変更に関するものです。これまで、Azure Storageの低頻度アクセスティア（cool、cold、archive）に対して、最小課金オブジェクトサイズの導入が予定されていましたが、今回のアップデートにより、その導入が一時停止されることとなりました。これにより、2026年7月1日以降も新規および既存のストレージアカウントにおいて、課金の挙動は変更されません。

このアップデートの背景には、ストレージ利用者のコスト管理や課金体系の透明性を維持する目的があると考えられます。Azure Storageのcool、cold、archiveティアは、主にアクセス頻度が低いデータの保存に適しており、コスト効率を重視するシナリオで活用されています。最小課金オブジェクトサイズの導入は、極小サイズのオブジェクトを大量に保存する場合の課金最適化や、ストレージインフラの運用効率向上を目的として検討されていましたが、今回の一時停止により、現行の課金方式が継続されることとなります。

具体的な変更内容としては、2026年7月1日以降も、cool、cold、archiveティアに保存されるオブジェクトに対して、最小課金サイズの制約が適用されない点が挙げられます。これにより、例えば数KBの小さなファイルを大量に保存する場合でも、実際のオブジェクトサイズに基づいた課金が継続されます。技術的な仕組みとしては、Azure Storageの課金ロジックが現状維持され、ストレージアカウントの設定やAPIの利用方法にも変更はありません。

活用シナリオとしては、ログファイルやIoTデバイスからの小規模データ、アーカイブ用途の画像やドキュメントなど、アクセス頻度が低く、かつオブジェクトサイズが小さいデータを大量に保存する場合に、今回のアップデートによる課金方式の維持がコスト面で有利となります。注意点としては、今後のアップデートで課金方式が変更される可能性があるため、公式情報の継続的な確認が必要です。

関連するAzureサービスとしては、Azure Blob Storageが主に対象となり、Data Lake StorageやBackup、Archive Storageなどのサービスとも密接に連携しています。今回のアップデートは、これらのサービスを利用する際のコスト計算やストレージ設計に直接影響する内容となっています。今後の公式アップデートにより、課金体系やストレージ運用方針が変更される場合は、速やかに対応することが求められます。

---

### 2. Generally Available: Azure NC RTX PRO 6000 Blackwell Server Edition v6 Series Virtual Machines

**公開日時**: 2026年06月08日 18:15:14 UTC
**リンク**: [Generally Available: Azure NC RTX PRO 6000 Blackwell Server Edition v6 Series Virtual Machines](https://azure.microsoft.com/updates?id=565271)

**アップデートID**: 565271
**情報源**: Azure Updates API

**カテゴリ**: Launched, Features

**要約**:

- 何が更新されたか  
Azure NCv6シリーズ仮想マシン（VM）が、Southeast AsiaおよびWest US 2リージョンで一般提供（GA）されました。

- 主な変更点や新機能  
NCv6シリーズVMは、NVIDIA RTX PRO 6000 Blackwell Server Edition GPUを搭載しています。各GPUは96GBのメモリを持ち、高度なグラフィックス処理やAI/機械学習ワークロードに最適化されています。

- 影響を受ける対象  
GPUを活用した高性能コンピューティングが必要な技術者や開発者、特にディープラーニング、3Dレンダリング、シミュレーションなどの用途でAzureを利用するユーザーが対象です。

- 注意点があれば記載  
利用可能なリージョンはSoutheast AsiaとWest US 2に限定されています。その他のリージョンでは利用できませんので、リージョン選択にご注意ください。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=565271）をご参照ください。

**詳細**:

Azure NCv6シリーズ仮想マシン（VM）が、東南アジアおよび米国西部2リージョンで一般提供（GA）となりました。本アップデートの背景には、GPUを活用した高度な計算処理やグラフィックス処理に対する需要の高まりがあり、これに応える形で最新のNVIDIA RTX PRO 6000 Blackwell Server Edition GPUを搭載したNCv6シリーズが提供開始されました。これにより、Azure上でより高性能なGPUリソースを必要とするワークロードを実行できる環境が整備されます。

NCv6シリーズVMは、各インスタンスにNVIDIA RTX PRO 6000 Blackwell Server Edition GPUを搭載しており、各GPUは96GBの大容量メモリを備えています。これにより、従来の世代よりも大規模なデータセットや複雑な計算処理を効率的に実行することが可能です。主な変更点は、最新世代GPUの採用による計算能力とメモリ容量の大幅な向上にあります。

技術的な仕組みとしては、Azureの仮想化基盤上で物理GPUリソースをVMに割り当てることで、高度な並列処理やグラフィックス処理を実現しています。これにより、機械学習モデルのトレーニングや推論、3Dレンダリング、科学技術計算、ビジュアルシミュレーションなど、GPUアクセラレーションが求められるさまざまな用途に対応できます。

活用シナリオとしては、ディープラーニングやAIワークロードの大規模なトレーニング、複雑なビジュアルエフェクトの生成、CADやCAEなどのエンジニアリング用途、リアルタイムのデータ解析やシミュレーションなどが挙げられます。特に、GPUメモリ容量が96GBと大きいため、メモリ消費の激しいモデルやアプリケーションにも適しています。

注意点としては、現時点で一般提供されているリージョンが東南アジアおよび米国西部2に限定されているため、他リージョンでは利用できない点に留意が必要です。また、GPUリソースは需要が高く、利用状況によってはリソースの確保が難しい場合があります。

関連するAzureサービスとしては、Azure Machine LearningやAzure BatchなどのGPU対応サービスと組み合わせることで、スケーラブルなAI/MLワークロードやバッチ処理を効率的に実行できます。これにより、クラウド上でのGPU活用の幅がさらに広がります。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=565271）を参照してください。

---

### 3. Generally Available: Premium SSD v2 disks now support non-zonal Azure Virtual Machines 

**公開日時**: 2026年06月08日 18:00:23 UTC
**リンク**: [Generally Available: Premium SSD v2 disks now support non-zonal Azure Virtual Machines ](https://azure.microsoft.com/updates?id=565359)

**アップデートID**: 565359
**情報源**: Azure Updates API

**カテゴリ**: Launched, Features

**要約**:

- 何が更新されたか  
Azure Premium SSD v2ディスクが、Availability Zones（AZs）を持つ一部のAzureリージョンにおいて、ゾーン指定なし（non-zonal）の単一インスタンス仮想マシン（VM）でも利用可能になりました。

- 主な変更点や新機能  
これまでPremium SSD v2ディスクは、主にゾーン指定（zonal）VMでの利用が前提でしたが、今回のアップデートにより、Availability Zoneを指定しないnon-zonal VMでもPremium SSD v2ディスクをアタッチして利用できるようになりました。これにより、VMのデプロイ時にゾーン指定が不要となり、柔軟な構成が可能です。

- 影響を受ける対象  
Availability Zonesを持つリージョンで、Premium SSD v2ディスクを利用したいnon-zonal VMを運用している、または今後利用予定のあるユーザーやシステムが対象です。

- 注意点  
本機能は一部のAZ対応リージョンでのみ利用可能です。利用可能なリージョンについては公式ドキュメントで確認する必要があります。既存のzonal VMや他のディスクタイプには影響しません。

**詳細**:

本アップデートは、Azure Premium SSD v2ディスクが、これまでサポート対象外であった非ゾーン（non-zonal）、単一インスタンスのAzure仮想マシン（VM）に対しても利用可能となったことを示しています。対象となるのは、アベイラビリティゾーン（Availability Zones, AZs）が提供されている一部のAzureリージョンです。これにより、従来はPremium SSD v2を利用する際に必須であったアベイラビリティゾーンの選択が不要となり、非ゾーン仮想マシンでもPremium SSD v2の高性能ストレージを利用できるようになりました。

この変更の背景には、Premium SSD v2が持つ高いIOPS、スループット、低レイテンシといった特長を、より幅広いワークロードやシナリオで活用したいというニーズがあります。従来、Premium SSD v2はゾーン指定VMでのみ利用可能であったため、可用性ゾーンを利用しないシンプルな構成や、単一インスタンス運用のワークロードでは選択肢が限られていました。今回のアップデートにより、これらのシナリオでもPremium SSD v2の恩恵を受けることが可能となります。

技術的には、Premium SSD v2ディスクのプロビジョニング時に、従来はゾーン指定が必須でしたが、今回のアップデートによってゾーン指定なし（non-zonal）でのディスク作成およびアタッチがサポートされます。これにより、非ゾーンVMのデプロイ時にもPremium SSD v2を選択でき、既存のストレージ構成を変更することなく、より高性能なディスクを利用することができます。

活用シナリオとしては、可用性ゾーンを利用しない単一インスタンスのアプリケーションサーバーや、テスト・開発環境など、シンプルな構成で高いストレージ性能が求められるケースが挙げられます。また、既存の非ゾーンVM環境でストレージ性能を向上させたい場合にも有効です。

注意点として、Premium SSD v2のnon-zonalサポートは、アベイラビリティゾーンが提供されている一部リージョンに限定されているため、利用可能なリージョンを事前に確認する必要があります。また、ゾーン冗長性や高可用性が求められる場合は、引き続きゾーン指定VMの利用が推奨されます。

関連するAzureサービスとの連携については、仮想マシンのストレージとしてPremium SSD v2を利用できる点が主なポイントとなります。これにより、Azure Virtual Machinesのパフォーマンス要件に応じた柔軟なストレージ選択が可能となり、コストと性能の最適化が図れます。

以上のように、本アップデートはPremium SSD v2の利用範囲を拡大し、非ゾーン仮想マシンでも高性能ストレージを活用したい技術者にとって有用な変更となっています。

---

### 4. Public Preview: Microsoft Foundry agent security capabilities in Microsoft Defender for Cloud are transitioning to a Microsoft Agent 365 license

**公開日時**: 2026年06月08日 17:15:43 UTC
**リンク**: [Public Preview: Microsoft Foundry agent security capabilities in Microsoft Defender for Cloud are transitioning to a Microsoft Agent 365 license](https://azure.microsoft.com/updates?id=565171)

**アップデートID**: 565171
**情報源**: Azure Updates API

**カテゴリ**: In preview, Hybrid + multicloud, Security, Microsoft Defender for Cloud, Features, Pricing & Offerings, Feature

**要約**:

- 何が更新されたか  
Microsoft Defender for Cloudで提供されていたMicrosoft Foundryエージェントのセキュリティ機能が、2026年7月1日よりMicrosoft Agent 365ライセンスへ移行されることが発表されました。

- 主な変更点や新機能  
これまでDefender for Cloudで利用できたFoundryエージェントのセキュリティ機能は、今後はMicrosoft Agent 365ライセンスの一部として提供されます。また、Defenderでのエージェント保護は、Agent 365のオブザーバビリティログを活用して実現されるようになります。

- 影響を受ける対象  
現在、Microsoft Defender for CloudでFoundryエージェントのセキュリティ機能を利用している組織やユーザーが対象となります。今後はMicrosoft Agent 365ライセンスが必要となります。

- 注意点があれば記載  
2026年7月1日以降、従来のDefender for Cloud経由でのFoundryエージェントセキュリティ機能は利用できなくなります。該当機能を継続利用する場合は、Microsoft Agent 365ライセンスへの移行準備が必要です。移行計画やライセンス要件の確認を早めに行うことを推奨します。

**詳細**:

2026年7月1日より、Microsoft Defender for Cloudで提供されていたMicrosoft Foundryエージェントのセキュリティ機能は、Microsoft Agent 365ライセンスに移行されます。本アップデートの背景には、セキュリティ機能の提供方法を見直し、より一貫性のあるライセンス体系と運用管理を実現する目的があります。これにより、従来Defender for Cloudを通じて利用していたFoundryエージェントの保護機能は、今後はMicrosoft Agent 365ライセンスを通じて提供されることになります。

具体的な変更点としては、Defender for Cloud内でのエージェント保護が、Agent 365のオブザーバビリティログを活用して実現される点が挙げられます。これにより、セキュリティイベントや運用データの収集・分析がAgent 365の仕組みに統合され、より高度な監視やインシデント対応が可能となります。技術的には、エージェントが生成するログデータがAgent 365のインフラストラクチャに送信され、そこで分析・可視化される形となります。これにより、セキュリティ運用担当者は統合されたダッシュボードやアラート機能を利用して、脅威の検出や対応を効率的に行うことができます。

利用シナリオとしては、従来Defender for Cloud上でFoundryエージェントを用いて仮想マシンやクラウドリソースのセキュリティ監視を行っていた環境において、今後はAgent 365ライセンスを取得し、同様の監視・保護機能を継続利用することが想定されます。これにより、既存のセキュリティ運用フローを大きく変更することなく、最新の監視基盤を活用することが可能です。

注意点としては、2026年7月1日以降はFoundryエージェントのセキュリティ機能がDefender for Cloud単体では利用できなくなり、Agent 365ライセンスが必須となる点です。移行期間中にライセンスの取得や設定変更を計画的に進める必要があります。また、Agent 365のオブザーバビリティログの仕様や運用方法についても事前に確認しておくことが重要です。

関連するAzureサービスとしては、Microsoft Defender for Cloudが引き続きセキュリティ管理の中核を担いますが、今後はAgent 365との連携が不可欠となります。これにより、Azure上のセキュリティ監視やインシデント対応の自動化、可視化機能がより強化されることが期待されます。詳細については、公式アップデート情報（https://azure.microsoft.com/updates?id=565171）を参照してください。

---

### 5. Public Preview: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers.

**公開日時**: 2026年06月08日 17:15:43 UTC
**リンク**: [Public Preview: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers.](https://azure.microsoft.com/updates?id=565103)

**アップデートID**: 565103
**情報源**: Azure Updates API

**カテゴリ**: In preview, Management and governance, Migration, Azure Site Recovery, Management, Feature

**要約**:

【何が更新されたか】  
Azure Site Recoveryが、NVMeディスクコントローラーを搭載したLinux Azure仮想マシン（VM）のレプリケーションと災害復旧をサポートするパブリックプレビューを開始しました。

【主な変更点や新機能】  
これまでサポートされていなかったNVMe対応のGeneration 2 VMファミリー（例：Da/Ea/Fa v6シリーズ、Ebsv5/Ebdsv5）に対して、Azure-to-Azureシナリオでのレプリケーションとフェールオーバーが可能になりました。これにより、最新世代のVMで高性能なストレージ構成を利用している環境でも、Site Recoveryによる保護が利用できます。

【影響を受ける対象】  
NVMeディスクコントローラーを搭載したLinux Azure VMを利用している技術者や、災害復旧対策を検討しているAzureユーザーが対象です。特に、Da/Ea/Fa v6シリーズやEbsv5/Ebdsv5などのGeneration 2 VMファミリーを利用している場合に恩恵があります。

【注意点】  
本機能はパブリックプレビュー段階であり、正式リリース前のため運用環境での利用には注意が必要です。また、サポートはAzure-to-Azureシナリオに限定されているため、他のレプリケーションシナリオでは利用できません。詳細や制限事項は公式ドキュメントを参照してください。

**詳細**:

本アップデートは、Azure Site Recovery（ASR）がLinuxベースのAzure仮想マシン（VM）に対して、NVMeディスクコントローラーを搭載したGeneration 2 VMファミリー、具体的にはDa/Ea/Fa v6シリーズおよびEbsv5/Ebdsv5シリーズにおけるレプリケーションおよびディザスターリカバリー機能のサポートをパブリックプレビューとして開始したことを示しています。これにより、これまでサポートされていなかったNVMe対応の最新世代VMに対しても、Azure-to-Azure環境内での災害対策が可能となります。

今回の機能追加により、NVMeディスクコントローラーを利用することで高いI/Oパフォーマンスを必要とするワークロードを運用しているLinux VMに対しても、ASRによる継続的なデータレプリケーションやフェールオーバー、フェールバックといったディザスターリカバリー機能を適用できます。従来はSCSIやSATAコントローラーを利用したVMが主な対象でしたが、NVMeコントローラーを持つGeneration 2 VMファミリーへの対応が進んだことで、より幅広いシナリオに対応できるようになりました。

技術的な仕組みとしては、ASRはAzure内で稼働するLinux VMのディスクデータを継続的に別リージョンのAzureストレージにレプリケーションします。NVMeディスクコントローラーを搭載したVMでも、ASRのレプリケーションエージェントがディスクI/Oをキャプチャし、増分データを転送することで、障害発生時には迅速なフェールオーバーを実現します。これにより、業務継続性の確保や災害発生時のダウンタイム最小化が可能となります。

活用シナリオとしては、金融や製造業など高いパフォーマンスと可用性が求められるLinuxワークロードの災害対策、またはNVMeディスクを活用したデータベースや分析基盤のBCP（事業継続計画）対策が挙げられます。ASRを利用することで、これらのワークロードを別リージョンに自動的にレプリケートし、障害時には迅速にサービスを再開できます。

注意点としては、本サポートはAzure-to-Azureシナリオに限定されている点が挙げられます。オンプレミスからAzure、またはAzureからオンプレミスへのレプリケーションには本アップデートは適用されません。また、パブリックプレビュー段階であるため、運用環境での利用には十分な検証が推奨されます。

関連サービスとしては、Azure BackupやAzure Monitorなどと連携することで、より包括的なデータ保護や監視体制を構築することが可能です。ASRの新機能を活用することで、最新のNVMe対応Linux VMに対しても、Azureプラットフォーム上で高度なディザスターリカバリー戦略を実現できます。

---

### 6. Generally Available: Maintenance control for Azure Database for PostgreSQL - reschedule, apply on demand, view and download

**公開日時**: 2026年06月08日 17:15:43 UTC
**リンク**: [Generally Available: Maintenance control for Azure Database for PostgreSQL - reschedule, apply on demand, view and download](https://azure.microsoft.com/updates?id=563756)

**アップデートID**: 563756
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Build, Feature

**要約**:

- 何が更新されたか  
Azure Database for PostgreSQL Flexible Serverにおいて、メンテナンス制御機能が一般提供（GA）されました。

- 主な変更点や新機能  
今回のアップデートにより、プラットフォームメンテナンスのスケジュール変更（リスケジュール）、オンデマンドでの適用、メンテナンスイベントの閲覧およびダウンロードが可能になりました。これにより、メンテナンスによるシステムへの影響を最小限に抑えつつ、運用計画に合わせた柔軟な対応が可能です。

- 影響を受ける対象  
Azure Database for PostgreSQL Flexible Serverを利用している全てのユーザーおよび管理者が対象です。

- 注意点があれば記載  
本機能を活用することで、メンテナンスによる予期せぬダウンタイムやサービス影響を回避しやすくなりますが、メンテナンス適用のタイミング管理には十分ご注意ください。詳細な操作方法や制約事項については公式ドキュメントを参照してください。

**詳細**:

本アップデートは、Azure Database for PostgreSQL Flexible Serverに対するメンテナンスコントロール機能の一般提供（GA）を発表するものです。従来、Azure Database for PostgreSQL Flexible Serverのプラットフォームメンテナンスは、Azure側で自動的にスケジュール・適用されるため、ユーザー側で制御できる範囲が限定されていました。今回のアップデートにより、ユーザーはメンテナンスイベントに対してより高い可視性と柔軟性を持って管理できるようになります。これにより、計画外のサービス中断や業務影響を最小限に抑えることが可能となります。

具体的な機能としては、メンテナンスイベントの再スケジュール、オンデマンドでの適用、イベントの詳細情報の閲覧およびダウンロードが可能となっています。これらの機能により、管理者は自身のシステムや業務プロセスに合わせてメンテナンスのタイミングを調整でき、事前に影響範囲を把握した上で適切な対応を取ることができます。特に、イベント情報のダウンロード機能は、監査やレポート作成、社内共有などの用途に有用です。

技術的には、Azure PortalやAzure CLI、REST APIなどを通じてこれらのメンテナンスコントロール機能が提供されます。管理者は対象のFlexible Serverインスタンスに対して、メンテナンスウィンドウの確認や変更、イベントの適用指示、イベント履歴の取得などを実施できます。これにより、DevOpsやSREチームはCI/CDパイプラインや運用自動化スクリプトと連携させることも可能です。

活用シナリオとしては、業務のピーク時間帯を避けてメンテナンスを実施したい場合や、複数の関連システムと連携している環境で事前に調整を行いたい場合などが挙げられます。また、障害対応訓練やアップグレード検証のタイミングに合わせてメンテナンスを適用することで、システムの安定運用に寄与します。

注意点としては、すべてのメンテナンスイベントがユーザーによる完全な制御下に置かれるわけではなく、Azureプラットフォームの健全性維持のために強制的に適用される場合がある点です。また、メンテナンスコントロール機能の利用には、対象インスタンスがFlexible Serverである必要があります。

関連するAzureサービスとの連携においては、Azure MonitorやAzure Event Gridなどと組み合わせることで、メンテナンスイベントの通知や自動化処理を強化することができます。これにより、システム全体の可用性や運用効率の向上が期待できます。

---

### 7. Public Preview: Azure Managed Redis now supports Entra ID based RBAC for data management 

**公開日時**: 2026年06月08日 16:15:40 UTC
**リンク**: [Public Preview: Azure Managed Redis now supports Entra ID based RBAC for data management ](https://azure.microsoft.com/updates?id=564873)

**アップデートID**: 564873
**情報源**: Azure Updates API

**カテゴリ**: In preview, Azure Managed Redis, Features, Microsoft Build

**要約**:

- 何が更新されたか  
Azure Managed Redisで、Microsoft Entra ID（旧Azure AD）を利用したRBAC（ロールベースアクセス制御）によるデータ管理機能がパブリックプレビューとして提供開始されました。

- 主な変更点や新機能  
これまでの共有キーによるアクセス制御に加え、Entra IDを用いたきめ細かなRBACが利用可能になりました。これにより、ユーザーやグループごとに「読み取り」「書き込み」「管理」などの権限を柔軟に設定できます。本機能はRedis ACL（Access Control Lists）を基盤としています。

- 影響を受ける対象  
Azure Managed Redisを利用している組織や開発者、特にセキュリティ要件が高く、アクセス権限の厳格な管理が求められる環境が対象となります。

- 注意点  
本機能は現時点でパブリックプレビューのため、本番環境での利用には十分な検証が推奨されます。また、既存の共有キー方式との互換性や移行手順についても事前に確認が必要です。

**詳細**:

今回のアップデートは、Azure Managed RedisにおいてMicrosoft Entra IDを用いたロールベースアクセス制御（RBAC）がデータ管理に対してパブリックプレビューとしてサポートされたことを示しています。これまでAzure Managed Redisのデータアクセス管理は主に共有キーに依存していましたが、本アップデートにより、より細粒度かつセキュアなアクセス制御が可能となります。背景としては、企業や組織におけるセキュリティ要件の高まりや、アクセス権限の厳格な管理ニーズへの対応が挙げられます。

具体的な機能としては、Microsoft Entra ID（旧称Azure Active Directory）を用いて、ユーザーやグループごとに「読み取り」「書き込み」「管理」などの権限を割り当てることができます。これにより、従来のような共有キーを配布する必要がなくなり、アクセス権限の管理や監査が容易になります。RBACはRedisのAccess Control Lists（ACL）機能の上に実装されており、Azureの認証基盤と連携することで、認証と認可のプロセスを統合的に管理できます。

技術的な仕組みとしては、Azure Managed RedisがEntra IDと連携し、ユーザーやサービスプリンシパルに対してRBACポリシーを適用します。これにより、Redisインスタンスへのアクセス時にEntra IDによる認証が行われ、RBACの設定に基づいてアクセス権限が付与されます。管理者はAzure PortalやCLI、ARMテンプレートなどを用いて、RBACの設定や権限の付与・変更を行うことができます。

活用シナリオとしては、複数のアプリケーションやチームが同一のRedisインスタンスを利用する場合に、各チームやアプリケーションごとに適切なアクセス権限を割り当てることで、不要なデータアクセスや操作を防ぐことが可能です。また、監査ログやアクセス履歴の管理が容易になるため、コンプライアンス要件への対応やセキュリティ強化にも寄与します。

注意点としては、パブリックプレビュー段階であるため、機能や仕様が今後変更される可能性があること、また一部の機能や制限事項が存在する場合があります。運用環境での利用に際しては、公式ドキュメントやサポート情報を十分に確認する必要があります。

関連するAzureサービスとの連携については、Entra IDを認証基盤として利用することで、Azure全体のID管理やセキュリティポリシーとRedisのアクセス制御を統合できます。これにより、Azure Managed Redisを他のAzureサービスと組み合わせたシステム構成においても、一貫したアクセス管理を実現することができます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=564873）をご参照ください。

---


*このレポートは自動生成されました - 2026-06-09 12:01:52 JST*