# 2026年08月07日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年08月07日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Announcing:  Azure Databricks Genie One and Genie Agents Free Usage Extended Through January 31, 2027 

**公開日時**: 2026年08月06日 19:41:52 UTC
**リンク**: [Announcing:  Azure Databricks Genie One and Genie Agents Free Usage Extended Through January 31, 2027 ](https://azure.microsoft.com/updates?id=568964)

**アップデートID**: 568964
**情報源**: Azure Updates API

**カテゴリ**: AI + machine learning, Analytics, Azure Databricks, Announcement

**要約**:

【Azure Update要約】

- 何が更新されたか  
Azure Databricksの「Genie One」と「Genie Agents」の無料利用期間が延長されました。

- 主な変更点や新機能  
これまで2026年7月31日までだった無料利用期間が、2027年1月31日まで延長されました。プロモーション期間中は、これらの製品に対してAzureの予算管理（Budget controls）が適用されません。

- 影響を受ける対象  
Azure Databricks上で「Genie One」および「Genie Agents」を利用している技術者や組織が対象です。これらのサービスを活用しているユーザーは、追加コストを気にせず利用を継続できます。

- 注意点  
プロモーション期間中は予算管理機能が適用されないため、利用状況の把握やコスト管理はユーザー自身で行う必要があります。無料期間終了後は通常の課金が再開されるため、運用計画の見直しが必要です。

詳細は公式アップデートページをご参照ください。

**詳細**:

本アップデートは、Azure DatabricksにおけるGenie OneおよびGenie Agentsの無料利用期間が、従来の2026年7月31日から2027年1月31日まで延長されたことを発表するものです。これにより、Azure Databricksユーザーは、これらの機能を追加コストなしでより長期間にわたり利用できるようになります。今回の延長は、Genie OneおよびGenie Agentsの利用促進と、ユーザーによる機能評価や導入の加速を目的としています。

具体的な変更内容としては、無料利用期間の延長に加え、プロモーション期間中は予算コントロール（Budget controls）がこれらの製品には適用されない点が挙げられます。つまり、Azureポータルで設定されている予算制限に関わらず、対象期間中はGenie OneおよびGenie Agentsの利用に対して課金が発生しません。

技術的な仕組みとしては、Azure Databricksのサービス上でGenie OneおよびGenie Agentsを有効化することで、ユーザーは追加設定や特別なデプロイ作業を行うことなく、これらの機能を利用できます。利用状況はAzureポータルやDatabricksの管理画面から確認可能ですが、プロモーション期間中は課金レポートにこれらのサービスの利用料が反映されない点に注意が必要です。

活用シナリオとしては、データエンジニアやデータサイエンティストがAzure Databricks上でのデータ処理やAIワークロードの自動化、運用効率化のためにGenie OneおよびGenie Agentsを試験的に導入するケースが想定されます。無料期間を活用することで、PoC（概念実証）や本番導入前の検証をコストを気にせず実施できるメリットがあります。

注意点として、プロモーション期間中は予算コントロールが適用されないため、組織のコスト管理ポリシーに基づく利用制限が効かないことを理解しておく必要があります。また、無料利用期間終了後は通常の課金体系に戻るため、継続利用を検討する場合は事前にコスト見積もりや予算調整が求められます。

関連するAzureサービスとの連携については、Azure DatabricksがAzureの各種データサービス（Azure Data Lake Storage、Azure Synapse Analyticsなど）とシームレスに連携できるため、Genie OneおよびGenie Agentsの活用範囲も広がります。これにより、エンドツーエンドのデータ分析基盤やAIワークフローの構築において、Azureエコシステム全体の利便性を高めることが可能です。

---

### 2. Public Preview: Migrate from AWS FSx for Windows File Server to Azure Files with Azure Storage Mover

**公開日時**: 2026年08月06日 16:40:19 UTC
**リンク**: [Public Preview: Migrate from AWS FSx for Windows File Server to Azure Files with Azure Storage Mover](https://azure.microsoft.com/updates?id=567979)

**アップデートID**: 567979
**情報源**: Azure Updates API

**カテゴリ**: In preview, Migration, Storage, Azure Storage Mover, Feature

**要約**:

【要約】

■何が更新されたか  
Azure Storage Moverが、AWS FSx for Windows File Server（SMB）からAzure Files（SMB）へのクラウド間移行を、エージェントレスでサポートするパブリックプレビューが開始されました。

■主な変更点や新機能  
従来は移行のためにエージェントの導入や管理が必要でしたが、今回のアップデートにより、エージェントレスでAWS FSxからAzure FilesへWindowsファイル共有を直接移行できるようになりました。これにより、移行作業の手間や運用負荷が大幅に軽減されます。

■影響を受ける対象  
AWS FSx for Windows File Server（SMB）を利用しているユーザーで、Azure Files（SMB）への移行を検討している技術者や管理者が主な対象です。クラウド間でファイルサーバーを移行したい場合に有効です。

■注意点  
現在はパブリックプレビュー段階のため、本番環境での利用は慎重に検討してください。機能やサポート内容が正式リリース時に変更される可能性があります。移行前には事前検証やバックアップを推奨します。

**詳細**:

今回のAzure Updateは、「Azure Storage MoverによるAWS FSx for Windows File ServerからAzure Filesへのエージェントレス・クラウド間移行」のパブリックプレビュー開始に関するものです。背景として、企業や組織がクラウドストレージの選択肢を広げる中、AWS FSx for Windows File Server（SMBプロトコル対応）からAzure Files（同じくSMB対応）への移行ニーズが高まっています。従来は、移行の際に専用のエージェントや追加のインフラ構築、複雑な管理作業が必要でしたが、Azure Storage Moverの新機能により、これらの負担が大幅に軽減されます。

具体的な機能として、Azure Storage MoverはAWS FSx for Windows File Server上のWindowsファイル共有を、Azure Filesへ直接移行できるようになりました。エージェントレスであるため、移行元・移行先双方に追加のソフトウェアや管理用エージェントを導入する必要がありません。クラウド間でのデータ転送は、Azure Storage Moverのサービスが自動的に管理し、ユーザーは移行ジョブの設定や進捗管理のみを行うことで、効率的かつ安全にファイル共有の移行が可能です。

技術的な仕組みとしては、Azure Storage MoverがAWS FSx for Windows File ServerとAzure Filesの双方に対してSMBプロトコルを用いてアクセスし、クラウド間でファイルデータを転送します。これにより、ファイルの属性やアクセス権限などの情報も保持したまま移行できることが特徴です。移行プロセスはAzure Storage Moverの管理ポータルから制御でき、移行ジョブの作成、進捗確認、エラー管理などが一元的に行えます。

活用シナリオとしては、AWS上で運用しているWindowsファイル共有をAzure環境へ統合したい場合や、Azure Filesの高可用性やセキュリティ機能を活用するためにストレージ基盤を移行したい場合に有効です。また、複数拠点や部門で分散管理されているファイル共有の集約や、クラウド間のストレージ最適化にも利用できます。

注意点として、現時点ではパブリックプレビューであるため、本番環境での利用は推奨されません。また、移行対象や移行方式に制限がある場合があります。SMBプロトコルによるファイル共有のみが対象であり、その他のプロトコルや特殊なファイル属性、カスタム権限などについては事前に検証が必要です。移行の際には、データ整合性やアクセス権限の維持、移行後のアプリケーション互換性などにも注意が必要です。

関連するAzureサービスとしては、Azure Filesが移行先となり、Azure Storage Moverが移行プロセスを管理します。これらのサービスはAzureポータルから一元的に操作でき、既存のAzureストレージ管理やセキュリティ機能と連携して運用することが可能です。

以上が、AWS FSx for Windows File ServerからAzure Filesへのクラウド間移行を実現するAzure Storage Moverのアップデート内容の詳細です。

---


*このレポートは自動生成されました - 2026-08-07 12:01:21 JST*