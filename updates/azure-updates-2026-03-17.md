# 2026年03月17日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年03月17日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Retirement: Support for Windows Server 2016 Marketplace images on Azure Batch pools will end on January 12, 2027

**公開日時**: 2026年03月16日 18:45:11 UTC
**リンク**: [Retirement: Support for Windows Server 2016 Marketplace images on Azure Batch pools will end on January 12, 2027](https://azure.microsoft.com/updates?id=549077)

**アップデートID**: 549077
**情報源**: Azure Updates API

**カテゴリ**: Compute, Batch, Retirements

**要約**:

- 何が更新されたか  
Azure BatchにおけるWindows Server 2016 Marketplaceイメージのサポートが、2027年1月12日をもって終了することが発表されました。

- 主な変更点や新機能  
今回の更新では、Windows Server 2016が延長サポート終了に伴い、Azure BatchプールでのMarketplaceイメージの利用が非推奨となります。新機能の追加はありません。

- 影響を受ける対象  
Azure Batch上でWindows Server 2016 Marketplaceイメージを利用しているユーザーやシステムが対象です。これには、既存のBatchプールや今後新規作成されるプールも含まれます。

- 注意点があれば記載  
2027年1月12日以降は、Windows Server 2016 Marketplaceイメージを使用したBatchプールの作成や管理ができなくなります。対象ユーザーは、Windows Server 2019や2022などサポート中のOSイメージへの移行を早めに検討してください。サポート終了後はセキュリティ更新や技術サポートも提供されませんのでご注意ください。

**詳細**:

Azure Batchは、クラウド上で大規模な並列計算やジョブ管理を効率的に行うサービスです。今回のアップデートは、Windows Server 2016のMarketplaceイメージを利用したAzure Batchプールのサポート終了に関するものです。背景として、MicrosoftはOSのライフサイクル管理を徹底しており、Windows Server 2016は2022年1月11日に通常サポートが終了し、2027年1月12日に延長サポートも終了する予定です。このため、Azure Batchでも同OSのMarketplaceイメージのサポートを段階的に終了する方針となっています。

具体的な変更内容として、2027年1月12日以降、Azure Marketplaceで提供されているWindows Server 2016イメージを利用したBatchプールの新規作成や既存プールの維持ができなくなります。これにより、Windows Server 2016イメージを指定したプールの運用やジョブ実行が不可となります。技術的には、Azure Batchのプール作成時にOSイメージとしてMarketplaceから提供されるWindows Server 2016を選択することができなくなり、既存プールもサポート対象外となるため、セキュリティパッチや更新が提供されなくなります。

Azure Batchの活用シナリオとしては、科学技術計算、画像処理、動画エンコード、データ分析など大量のジョブを分散実行する用途が一般的です。これらの処理でWindows Server 2016イメージを利用している場合、今後はサポート終了に伴い、より新しいOSイメージ（例：Windows Server 2019や2022）への移行が必要となります。移行時には、アプリケーションの互換性や依存ライブラリの対応状況を確認し、Batchプールの再構築やジョブスケジューラの設定変更が求められます。

注意点として、サポート終了後はセキュリティアップデートや技術的なサポートが提供されなくなるため、運用リスクが高まります。また、Azure Batch以外のサービスでも同様にOSイメージのサポート状況に注意が必要です。関連するAzureサービスとしては、Azure Virtual MachinesやAzure Compute Galleryなどが挙げられ、これらのサービスでもMarketplaceイメージのライフサイクル管理が行われています。

まとめとして、Windows Server 2016 Marketplaceイメージを利用したAzure Batchプールのサポートは2027年1月12日で終了します。技術者は、計画的な移行とアプリケーションの互換性確認を行い、最新のOSイメージを活用することで、安定したBatch運用とセキュリティ確保を実現する必要があります。

---

### 2. Retirement: Migration of Azure Batch Low-Priority VMs to Spot VMs in early March

**公開日時**: 2026年03月16日 18:45:11 UTC
**リンク**: [Retirement: Migration of Azure Batch Low-Priority VMs to Spot VMs in early March](https://azure.microsoft.com/updates?id=543279)

**アップデートID**: 543279
**情報源**: Azure Updates API

**カテゴリ**: Compute, Batch, Retirements

**要約**:

- 何が更新されたか  
Azure BatchのLow-Priority VMが2025年9月30日に廃止され、2026年3月1日よりシステム主導でSpot VMへの移行が開始されます。

- 主な変更点や新機能  
これまで利用されていたLow-Priority VMは廃止され、今後はSpot VMが代替として利用されます。これにより、Azure BatchはAzure全体のSpotインフラストラクチャと統一され、VMの提供形態が簡素化されます。

- 影響を受ける対象  
Azure BatchでLow-Priority VMを利用している全てのユーザーおよびシステムが対象です。既存のLow-Priority VMジョブやプールは、今後Spot VMへの移行が必要となります。

- 注意点  
2025年9月30日以降はLow-Priority VMが利用できなくなります。2026年3月1日からはAzureによる自動移行が始まるため、事前にSpot VMへの移行計画を立てておくことを推奨します。Spot VMの特性や制約についても十分に理解しておく必要があります。

**詳細**:

Azure Batchにおいて、Low-Priority VMの提供が2025年9月30日をもって終了し、2026年3月1日よりSpot VMへのシステム主導による移行が開始されます。このアップデートの背景には、Azure BatchのVMオファリングをより簡素化し、Azure全体のSpotインフラストラクチャと整合性を取る目的があります。これにより、Batchサービス利用者は今後、Low-Priority VMではなくSpot VMを選択することになります。

具体的な変更内容としては、従来Batchで利用されていたLow-Priority VMが廃止され、今後はSpot VMのみが選択可能となります。Spot VMは、未使用の計算リソースを割安な価格で利用できるVMですが、需要が高まった際には事前通知なく削除される可能性があるため、バッチ処理や一時的な計算タスクに適しています。システム主導の移行は、ユーザーが手動で設定を変更する必要なく、Batchアカウント内のLow-Priority VMジョブが自動的にSpot VMへ切り替えられる仕組みとなります。

技術的な実装方法としては、Azure Batchのジョブやプール定義において、Low-Priority VMの指定がSpot VMへと置き換えられます。Spot VMは、AzureのSpotインフラストラクチャと連携しており、VMの割り当てや削除のタイミングはAzureのリソース管理によって制御されます。これにより、BatchサービスのVM管理がAzure全体のリソース管理方針と統一され、運用の一貫性が向上します。

活用シナリオとしては、コスト効率を重視した大規模なバッチ処理や、並列計算を必要とするデータ分析、シミュレーションなどの用途でSpot VMが利用されます。Spot VMは、価格変動やVMの削除リスクを許容できるワークロードに適しており、Azure Batchのジョブスケジューリング機能と組み合わせることで、効率的なリソース活用が可能です。

注意点としては、Spot VMは需要に応じて事前通知なく削除されるため、ジョブの中断や再実行が発生する可能性があります。これに対処するためには、ジョブの再開やチェックポイント機能を活用し、耐障害性の高い設計を行う必要があります。また、Low-Priority VMからSpot VMへの移行に伴い、既存のBatchジョブやプール設定が影響を受けるため、事前に設定内容の確認と対応が求められます。

関連するAzureサービスとしては、Azure BatchとAzure Spot VMが密接に連携します。Batchサービスのジョブ管理やスケジューリング機能はそのまま利用でき、Spot VMの割り当てや管理はAzureのインフラストラクチャによって自動化されます。これにより、Batchユーザーは従来通りの運用を維持しつつ、より効率的なリソース利用が可能となります。

---

### 3. Public Preview: Entra ID-Based Access for Azure Blob Storage SFTP

**公開日時**: 2026年03月16日 18:30:34 UTC
**リンク**: [Public Preview: Entra ID-Based Access for Azure Blob Storage SFTP](https://azure.microsoft.com/updates?id=558662)

**アップデートID**: 558662
**情報源**: Azure Updates API

**カテゴリ**: In preview, Storage, Azure Blob Storage, Features

**要約**:

- 何が更新されたか  
Azure Blob StorageのSFTP接続において、Microsoft Entra ID（旧称Azure AD）ベースのアクセス制御がパブリックプレビューとして提供開始されました。

- 主な変更点や新機能  
これまでSFTP接続にはローカルユーザーやSSHキーが必要でしたが、今回のアップデートにより、Microsoft Entra IDのID（組織内ユーザーやEntra External Identities経由のゲストユーザーを含む）を利用して、SFTP経由でAzure Blob Storageへセキュアにアクセスできるようになりました。これにより、ID管理やアクセス制御が一元化され、セキュリティと運用効率が向上します。

- 影響を受ける対象  
Azure Blob StorageをSFTP経由で利用している組織や、Entra IDによる統合的なアクセス管理を求める企業が主な対象です。特に、外部ユーザーやゲストユーザーのアクセス管理を強化したい場合に有効です。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用には注意が必要です。正式リリース前のため、サポートや機能面で制限がある可能性があります。詳細や最新情報は公式ドキュメントを参照してください。

**詳細**:

本アップデートは、「Microsoft Entra ID-based access for Azure Blob Storage SFTP」がパブリックプレビューとして提供開始されたことを示しています。これにより、Azure Blob StorageのSFTP（SSH File Transfer Protocol）アクセスにおいて、Microsoft Entra IDのID管理基盤を利用した認証・認可が可能となります。従来、Azure Blob StorageのSFTPアクセスはローカルユーザーやストレージアカウントキーなどによる認証が主流でしたが、本機能の導入により、Microsoft Entra ID（旧称Azure Active Directory）に登録されたユーザーや、Entra External Identitiesを利用したゲストユーザーも含めたIDベースのセキュアなアクセス制御が実現されます。

具体的には、SFTPクライアントからAzure Blob Storageに接続する際、Microsoft Entra IDの認証情報を用いてアクセス権限を判定します。これにより、組織内のユーザー管理ポリシーや多要素認証（MFA）、条件付きアクセスなどのEntra IDのセキュリティ機能をSFTPアクセスにも適用できるようになります。また、ゲストユーザーにもアクセス権を付与できるため、外部パートナーとのファイル連携や共同作業のセキュリティを強化できます。

技術的な実装としては、Entra IDとAzure Blob Storage間で認証連携が行われ、SFTPアクセス時にユーザーのEntra IDトークンを検証することでアクセス制御が実現されます。これにより、従来のローカルユーザー管理の煩雑さを軽減し、IDライフサイクル管理やアクセス権限の一元管理が可能となります。

活用シナリオとしては、企業内外のユーザーがSFTPを通じて安全にBlob Storageへファイルをアップロード・ダウンロードするケースや、既存のEntra IDベースのセキュリティポリシーをそのままSFTPアクセスに適用したい場合が想定されます。特に、外部委託先やパートナー企業とのデータ連携において、ゲストユーザーのアクセス管理が容易になる点が大きな利点です。

注意点としては、本機能がパブリックプレビュー段階であるため、本番環境での利用には慎重な検証が必要です。また、既存のSFTPアクセス方式との互換性や、Entra IDの設定状況による影響範囲についても事前に確認することが推奨されます。

関連するAzureサービスとしては、Microsoft Entra ID自体のほか、Azure Blob StorageのSFTP機能、Entra External Identitiesによるゲストユーザー管理などが挙げられます。これらのサービスと連携することで、よりセキュアで柔軟なストレージアクセス基盤を構築できます。

---

### 4. Retirement: End of life reminder of NVv3 and NVv4-series Azure virtual machine in Azure Batch pools 

**公開日時**: 2026年03月16日 18:30:34 UTC
**リンク**: [Retirement: End of life reminder of NVv3 and NVv4-series Azure virtual machine in Azure Batch pools ](https://azure.microsoft.com/updates?id=516070)

**アップデートID**: 516070
**情報源**: Azure Updates API

**カテゴリ**: Compute, Batch, Features, Retirements

**要約**:

【何が更新されたか】  
Microsoft Azureは、NVv3およびNVv4シリーズの仮想マシン（VM）のAzure Batchプールにおけるサポートを2026年9月30日に終了することを発表しました。

【主な変更点や新機能】  
NVv3シリーズ（NVIDIA Tesla M60 GPU搭載：Standard_NV12s_v3、Standard_NV12hs_v3、Standard_NV24s_v3、Standard_NV24ms_v3、Standard_NV32ms_v3、Standard_NV48s_v3）およびNVv4シリーズのVMがAzure Batchプールで利用できなくなります。新機能の追加はありません。

【影響を受ける対象】  
Azure BatchでNVv3またはNVv4シリーズのVMを利用しているユーザーやシステムが対象です。GPUを活用したバッチ処理や計算タスクを実行している環境が影響を受けます。

【注意点】  
2026年9月30日以降、該当VMシリーズはAzure Batchプールで新規作成や既存プールの維持ができなくなります。今後の運用やシステム設計において、他のVMシリーズへの移行計画を早めに検討・実施する必要があります。該当VMを利用している場合は、サービス停止や業務影響を防ぐため、十分な移行準備を行ってください。

**詳細**:

本アップデートは、Microsoft AzureにおけるNVv3およびNVv4シリーズの仮想マシン（VM）のサポート終了に関する重要な案内です。2026年9月30日をもって、Azure Batchプール内で利用されているNVv3シリーズ（NVIDIA Tesla M60 GPU搭載：Standard_NV12s_v3、Standard_NV12hs_v3、Standard_NV24s_v3、Standard_NV24ms_v3、Standard_NV32ms_v3、Standard_NV48s_v3）およびNVv4シリーズの仮想マシンが正式にリタイアされます。

このアップデートの背景には、Azureプラットフォームにおけるハードウェアおよびサービスの最新化があり、より高性能かつ効率的な仮想マシンシリーズへの移行を促進する目的があります。NVv3およびNVv4シリーズは、GPUアクセラレーションを必要とするグラフィックス処理や機械学習、ビジュアライゼーションなどの用途で広く利用されてきましたが、今後は新しい世代のVMへの移行が求められます。

具体的な変更内容としては、上記日付以降、Azure BatchプールにおいてNVv3およびNVv4シリーズのVMを新規作成・スケールアウトすることができなくなります。既存のBatchプールでこれらのVMを利用している場合も、サポート終了日以降はサービスの継続利用ができなくなります。技術的には、Azure Batchのプール定義やスケーリング設定において、これらのVMサイズを指定してもプロビジョニングが失敗するようになります。

実装方法としては、Azure Batchのプール作成時にVMサイズを指定する必要がありますが、2026年9月30日以降はNVv3およびNVv4シリーズの選択肢が利用不可となるため、他のサポートされているGPU VMシリーズへの移行作業が必要です。移行に際しては、ワークロードのGPU要件や互換性を十分に検証し、必要に応じてアプリケーションの最適化や再構成を行う必要があります。

これらのVMシリーズは、主にCAD、3Dレンダリング、ビジュアルシミュレーション、リモートデスクトップなどのGPUリソースを集中的に利用するシナリオで活用されてきました。Azure Batchは大規模なバッチ処理や並列計算の自動化に適しているため、これらの用途でNVv3/NVv4シリーズを利用していた場合、今後は新しいGPU VMシリーズ（例：NC、ND、NVv5など）への移行計画が不可欠です。

注意点として、サポート終了日以降はこれらのVMを利用したBatchプールが正常に動作しなくなるため、早期の移行計画策定とテストが推奨されます。また、他のAzureサービス（例：Azure Machine Learning、Azure Virtual Desktop）と連携している場合も、同様にVMシリーズの互換性を確認し、必要な変更を実施してください。

本アップデートにより、Azure Batch環境でNVv3およびNVv4シリーズVMを利用している場合は、速やかに移行計画を立案し、最新のサポート対象VMシリーズへの移行を進めることが重要です。詳細は公式ドキュメントやアップデートページ（https://azure.microsoft.com/updates?id=516070）を参照してください。

---

### 5. Retirement: Flatcar Container Linux for AKS (preview) 

**公開日時**: 2026年03月16日 18:15:54 UTC
**リンク**: [Retirement: Flatcar Container Linux for AKS (preview) ](https://azure.microsoft.com/updates?id=557929)

**アップデートID**: 557929
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）におけるFlatcar Container Linux（プレビュー版）のサポートが、2026年6月8日をもって終了（リタイア）することが発表されました。

- 主な変更点や新機能  
新機能の追加はありません。今回のアップデートは、Flatcar Container Linux for AKS（プレビュー）のサポート終了に関する案内です。

- 影響を受ける対象  
現在AKSでFlatcar Container Linux（プレビュー）を利用しているユーザーおよびシステムが対象となります。これらのユーザーは、サポート終了日までに他のサポートされているノードイメージへの移行が必要です。

- 注意点があれば記載  
2026年6月7日までは引き続きFlatcar Container Linux for AKS（プレビュー）の利用が可能ですが、2026年6月8日以降はサポートが完全に終了します。運用中のクラスターやワークロードの安定稼働のため、早めに代替となるサポート対象のノードイメージへの移行計画を立てることを推奨します。

**詳細**:

本アップデートは、Azure Kubernetes Service（AKS）におけるFlatcar Container Linux（プレビュー版）のサポートが2026年6月8日をもって終了することを告知するものです。Flatcar Container Linuxは、コンテナワークロードの実行に特化した軽量なLinuxディストリビューションであり、AKS環境においても選択可能なノードOSとして提供されていました。今回のリタイアメントにより、2026年6月7日までは引き続きFlatcar Container Linux for AKS（プレビュー）を利用することができますが、それ以降はサポート対象外となります。

この変更の背景には、Flatcar Container Linux for AKS（プレビュー）が正式なGA（一般提供）に至らず、今後のAKSにおけるサポート体制やセキュリティアップデートの継続が困難となったことが挙げられます。Azureでは、サポート対象のOSイメージを利用することが推奨されており、リタイアメント日までに他のサポートされているノードOS（例：Ubuntu、Marinerなど）への移行が必要です。

技術的には、Flatcar Container Linux for AKS（プレビュー）は、AKSクラスターのノードプール作成時にOSオプションとして選択できる形で実装されていました。これにより、ユーザーはFlatcarの自動アップデート機能やイミュータブルなファイルシステム設計を活用し、セキュアかつ効率的なコンテナ基盤を構築できていました。しかし、プレビュー版であるため、正式なSLAや長期的なサポートが提供されていない点が制限事項となります。

主な活用シナリオとしては、セキュリティ要件が高い環境や、イミュータブルインフラストラクチャを志向するワークロードでFlatcar Container Linuxが選択されていました。また、AKSのマネージドサービスとしての利便性を享受しつつ、Flatcarの特徴を活かした運用が可能でした。

注意点として、Flatcar Container Linux for AKS（プレビュー）を利用しているクラスターは、2026年6月8日以降はAzureからのサポートやセキュリティパッチの提供が受けられなくなります。そのため、運用中のシステムにおいては計画的な移行が必須です。移行に際しては、ノードプールのOSをサポート対象のものに変更し、ワークロードの動作検証を行う必要があります。

関連するAzureサービスとの連携については、AKS自体がAzureの各種マネージドサービス（例：Azure Monitor、Azure Policy、Azure Active Directoryなど）と密接に連携しているため、ノードOSの変更による連携性への影響は限定的ですが、OS固有の設定や挙動に依存する部分については事前の検証が推奨されます。

以上の内容から、Flatcar Container Linux for AKS（プレビュー）を利用中の技術者は、リタイアメント日までにサポート対象のOSへの移行計画を策定し、Azureの最新のベストプラクティスに従った運用を行うことが求められます。

---


*このレポートは自動生成されました - 2026-03-17 12:02:32 JST*