# 2026年09月12日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年09月12日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Retirement: Azure Linux with OS Guard in Azure Kubernetes Service

**公開日時**: 2026年09月11日 18:08:28 UTC
**リンク**: [Retirement: Azure Linux with OS Guard in Azure Kubernetes Service](https://azure.microsoft.com/updates?id=571257)

**アップデートID**: 571257
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）における「Azure Linux with OS Guard」のサポートが2026年12月10日に終了することが発表されました。

- 主な変更点や新機能  
2026年12月10日以降、「Azure Linux with OS Guard」を新規に作成することができなくなります。今後は「Azure Container Linux」が「Azure Linux with OS Guard（プレビュー）」の後継となります。

- 影響を受ける対象  
AKS環境で「Azure Linux with OS Guard」を利用しているユーザーが対象となります。既存のワークロードやクラスタでこのOSを使用している場合、今後の運用や移行計画を検討する必要があります。

- 注意点があれば記載  
サポート終了日以降は新規作成が不可となるため、既存環境の移行や後継OSである「Azure Container Linux」への切り替えを早めに検討してください。サポート終了に伴うセキュリティや運用上のリスクにも注意が必要です。

**詳細**:

2026年12月10日をもって、Azure Kubernetes Service（AKS）における「Azure Linux with OS Guard」のサポートが終了します。これは、MicrosoftがAKS上で提供していたAzure Linux with OS Guard（プレビュー版）の利用が今後できなくなることを意味します。サポート終了後は、新規にAzure Linux with OS Guardを用いたノードプールやクラスタの作成ができなくなります。代替として「Azure Container Linux」が提供されることが発表されています。

このアップデートの背景には、Azure Linux with OS Guardのプレビュー提供を終了し、より安定的かつセキュアなコンテナ向けOSであるAzure Container Linuxへの移行を促進する目的があります。OS Guardは、Azure Linux上でセキュリティ強化を目的とした機能であり、AKS環境においてホストOSの保護や攻撃耐性の向上を図っていました。今回の変更により、今後はAzure Container LinuxがAKSにおける標準的なLinux OSとなります。

技術的な仕組みとして、Azure Linux with OS GuardはAKSのノードプールにおいて選択可能なOSイメージとして提供されていました。OS Guardは、OSレベルでのセキュリティ機能（例えば、カーネルの強化や不要なサービスの無効化など）を実装し、コンテナワークロードの安全性を高めていました。AKSのクラスタ作成時やノードプール追加時に、Azure Linux with OS Guardを選択することで、これらのセキュリティ機能を活用することができました。

活用シナリオとしては、金融や医療など高いセキュリティ要件を求められる業界で、AKS上のワークロードをAzure Linux with OS Guardで運用することで、OSレベルの保護を強化していました。また、Azure上でクラウドネイティブなアプリケーションを展開する際、セキュリティを重視する技術者がこのOS Guard機能を活用していました。

注意点として、2026年12月10日以降はAzure Linux with OS Guardを新規に作成することができなくなります。既存のリソースについての扱いは明記されていませんが、今後の運用やアップグレード計画においてはAzure Container Linuxへの移行を検討する必要があります。また、Azure Container LinuxはAzure Linux with OS Guardの直接的な後継となるため、移行時には互換性や機能差異について十分な検証が必要です。

関連するAzureサービスとしては、AKSが中心となりますが、Azure Container Linuxは今後AKSのノードOSとして標準的に利用されることになります。AKSのクラスタ管理やノードプールの構成、セキュリティ設定などにおいて、Azure Container Linuxを選択することで、Microsoftが提供する最新のセキュアなコンテナ向けOS環境を活用できます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=571257）をご参照ください。

---

### 2. Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB)

**公開日時**: 2026年09月11日 15:58:56 UTC
**リンク**: [Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB)](https://azure.microsoft.com/updates?id=570910)

**アップデートID**: 570910
**情報源**: Azure Updates API

**カテゴリ**: In preview, Migration, Storage, Azure Storage Mover, Features

**要約**:

- 何が更新されたか  
Azure Storage Moverが、オンプレミスのSMBファイル共有からAzure Files（SMB）へのエージェントレス移行をパブリックプレビューでサポートしました。

- 主な変更点や新機能  
これまで必要だった移行エージェントの導入や管理が不要となり、Windows ServerやNAS上のSMBファイル共有から直接Azure Files（SMB）へデータを移行できるようになりました。これにより、移行作業の簡素化と運用負荷の軽減が実現します。

- 影響を受ける対象  
オンプレミスでSMBファイル共有を運用しており、Azure Filesへの移行を検討している技術者やシステム管理者が対象です。特にWindows ServerやNASを利用している環境に適しています。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用には注意が必要です。正式リリース前の機能であるため、サポート範囲や動作保証に制限がある可能性があります。

**詳細**:

今回のAzure Updateは、「Azure Storage MoverによるオンプレミスのSMBファイル共有からAzure Files（SMB）へのエージェントレス移行」がパブリックプレビューとして提供開始されたことを示しています。アップデートの背景として、従来オンプレミス環境のWindows ServerやNAS上のSMBファイル共有をAzure Filesへ移行する際には、移行エージェントの導入や管理が必要でした。これにより、移行プロセスの複雑化や運用負荷が増大する課題がありました。今回のアップデートは、これらの課題を解決し、より簡便かつ効率的な移行を実現することを目的としています。

具体的な機能として、Azure Storage MoverがエージェントレスでオンプレミスのSMBファイル共有からAzure Files（SMB）へのデータ移行をサポートします。エージェントレスとは、移行対象のサーバーやNASに専用の移行エージェントをインストール、登録、管理する必要がないことを意味します。これにより、移行作業の前準備や運用負荷が大幅に軽減されます。Azure Storage MoverはAzure上で管理されるサービスであり、移行元と移行先の情報を設定するだけで、ファイルデータの転送が可能となります。

技術的な仕組みとしては、Azure Storage Moverがクラウドサービスとして動作し、オンプレミスのSMBファイル共有からAzure Files（SMB）へのデータコピーを実施します。移行元はWindows ServerやNASのSMB共有であり、移行先はAzure Files（SMB）となります。ユーザーはAzureポータル上で移行ジョブを作成し、必要な接続情報や認証情報を設定することで、移行プロセスを開始できます。エージェントレスのため、移行元環境へのソフトウェア導入や追加設定は不要です。

活用シナリオとしては、企業のファイルサーバーやNASのデータをクラウドへ移行する際に、運用負荷やセキュリティリスクを最小限に抑えつつ、迅速にAzure Filesへ移行したい場合に有効です。例えば、オンプレミスのWindows Server上のSMBファイル共有をAzure Filesへ移行し、クラウドベースのファイルストレージへ統合することで、バックアップや災害対策、リモートアクセスの強化などが実現できます。

注意点や制限事項としては、現時点でパブリックプレビューであるため、商用利用や大規模移行の際には十分な検証が必要です。また、エージェントレス移行がサポートするSMB共有のバージョンや認証方式、移行可能なデータ量など、詳細な制約については公式ドキュメントを参照する必要があります。

関連するAzureサービスとしては、Azure Files（SMB）が移行先となり、Azure Storage Moverが移行プロセスを管理します。これらのサービスを組み合わせることで、オンプレミスからクラウドへのファイルデータ移行が効率的に実現できます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=570910）を参照してください。

---


*このレポートは自動生成されました - 2026-09-12 12:01:04 JST*