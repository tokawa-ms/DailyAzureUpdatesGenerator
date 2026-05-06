# 2026年05月06日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年05月06日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Retirement: Azure Reserved Virtual Machines Instances for select VM series

**公開日時**: 2026年05月05日 20:00:13 UTC
**リンク**: [Retirement: Azure Reserved Virtual Machines Instances for select VM series](https://azure.microsoft.com/updates?id=560948)

**アップデートID**: 560948
**情報源**: Azure Updates API

**カテゴリ**: Compute, Virtual Machines, Retirements, Pricing & Offerings

**要約**:

- 何が更新されたか  
2026年7月1日より、特定のAzure仮想マシン（VM）シリーズに対するAzure Reserved VM Instances（一年予約インスタンス）の新規購入および更新ができなくなります。

- 主な変更点や新機能  
Av2、Amv2、Bv1、D、Ds、Dv2、Dsv2、F、Fs、Fsv2、G、Gs、Ls、Lsv2といったVMシリーズが対象で、これらのシリーズでは一年予約インスタンスの購入・更新が終了します。また、これらのシリーズに対する一部の予約インスタンス（1年・3年）の提供も終了します。

- 影響を受ける対象  
上記VMシリーズのAzure Reserved VM Instances（一年予約インスタンス）を利用中、または今後利用予定のユーザーや組織が影響を受けます。

- 注意点  
既存の予約インスタンスは有効期限まで利用可能ですが、2026年7月1日以降は新規購入や更新ができなくなります。コスト最適化や運用計画を見直す必要があります。今後は他のVMシリーズや従量課金制への移行を検討してください。詳細は公式ドキュメントを参照してください。

**詳細**:

2026年7月1日より、Azureは特定の仮想マシン（VM）シリーズに対する1年間のAzure Reserved Virtual Machines Instances（予約インスタンス）の新規購入および更新を終了します。対象となるVMシリーズは、Av2、Amv2、Bv1、D、Ds、Dv2、Dsv2、F、Fs、Fsv2、G、Gs、Ls、Lsv2です。また、これらのシリーズに対しては、1年および3年の予約インスタンスの提供も終了となります。

このアップデートの背景には、Azureがサービスやインフラストラクチャの最適化を進める中で、特定のVMシリーズの提供形態を見直す方針があると考えられます。予約インスタンスは、特定のVMサイズとリージョンに対して長期間の利用を前提に割引価格を提供する仕組みであり、コスト最適化を目的とした多くの企業で利用されています。しかし、今回の変更により、上記シリーズのVMについては、今後は従量課金制（Pay-As-You-Go）や他の割引プランへの移行が必要となります。

技術的には、予約インスタンスはAzure Resource Manager（ARM）ベースで管理され、購入時に指定したVMサイズやリージョンに対して割引が適用される仕組みです。今回の変更により、対象VMシリーズの予約インスタンスの新規購入や既存予約の更新ができなくなるため、これらのVMを長期運用しているシステムではコスト構造の見直しが必要です。

活用シナリオとしては、これまでコスト削減のために予約インスタンスを利用していたワークロードや、長期間安定して稼働させる必要がある業務システムなどが挙げられます。今後は、他のVMシリーズへの移行や、従量課金制での運用、またはAzure Savings Plans for Computeなどの他のコスト最適化手法の検討が求められます。

注意点として、既存の予約インスタンスについては、契約期間満了までは引き続き利用可能ですが、期間終了後の更新や新規購入はできません。また、対象VMシリーズを利用している場合は、早めに今後の運用方針を検討し、必要に応じて他のVMシリーズへの移行計画を立てることが重要です。

関連するAzureサービスとの連携としては、Azure Cost ManagementやAzure Advisorを活用することで、コスト最適化の提案や移行先の選定を効率的に行うことができます。今回のアップデートにより、コスト管理やリソース運用の見直しが必要となるため、これらのツールを積極的に利用することが推奨されます。

---

### 2. Public Preview: Application Gateway for Containers managed add-on + AKS Automatic 

**公開日時**: 2026年05月05日 17:30:03 UTC
**リンク**: [Public Preview: Application Gateway for Containers managed add-on + AKS Automatic ](https://azure.microsoft.com/updates?id=558403)

**アップデートID**: 558403
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
Application Gateway for ContainersのAKSマネージドアドオンおよびAKS自動管理機能がパブリックプレビューとして提供開始されました。

- 主な変更点や新機能  
これまでApplication Gateway for ContainersはAKSクラスタへの自動デプロイや管理ができませんでしたが、今回のアップデートでAKSアドオンとして統合され、自動的にプロビジョニング・管理が可能になりました。これにより、Kubernetesクラスタ上でのL7ロードバランシングやアプリケーションゲートウェイの運用が簡素化されます。

- 影響を受ける対象  
Azure Kubernetes Service（AKS）を利用しているユーザーや、Kubernetes環境でL7トラフィック管理・セキュリティ強化を行いたい技術者が対象です。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用は推奨されません。サポート範囲や制限事項については公式ドキュメントを確認してください。

**詳細**:

本アップデートは、「Application Gateway for Containers managed add-on」と「AKS Automatic」に関するパブリックプレビューの提供開始についてのものです。これまでAzure Kubernetes Service（AKS）向けに「Application Gateway for Containers」およびそのAKSアドオンが発表されていましたが、当時は「Application Gateway for Containers」が自動的に管理される形でAKSに統合されることができないという制限がありました。今回のアップデートでは、この制限が解消され、AKS環境において「Application Gateway for Containers managed add-on」が自動的に利用できるようになったことが主な変更点です。

具体的な機能として、「Application Gateway for Containers managed add-on」は、AKSクラスターに対して容易に導入できる形で提供されます。これにより、コンテナ化されたアプリケーションのトラフィック管理やロードバランシング、セキュアな通信の終端などを、Azure Application Gatewayの機能を活用しながら実現できます。従来は手動で構成や管理が必要だった部分が、AKSのアドオンとして自動的に管理されるため、運用負荷の軽減や構成ミスの防止につながります。

技術的な仕組みとしては、AKSクラスターにアドオンとして「Application Gateway for Containers」を追加することで、KubernetesのサービスやIngressリソースと連携し、アプリケーションへの外部アクセスのルーティングやTLS終端、WAF（Web Application Firewall）などの高度な機能を提供します。Azureの管理基盤と統合されているため、リソースの作成や更新、スケーリングなどもAzureポータルやCLIから一括して管理できます。

活用シナリオとしては、複数のコンテナアプリケーションをAKS上で運用する際に、外部からのアクセスをセキュアかつ効率的に制御したい場合や、アプリケーションごとに異なるルーティングや認証・認可を実装したい場合に有効です。また、Azure Application GatewayのWAF機能を活用することで、セキュリティ要件の高いシステムにも対応可能です。

注意点としては、パブリックプレビュー段階であるため、本番環境での利用には慎重な検討が必要です。機能やパフォーマンス、サポート範囲については今後変更される可能性があるため、最新のドキュメントや公式情報を確認しながら導入を進めることが推奨されます。

関連するAzureサービスとしては、AKS、Application Gateway、Azure Monitorなどが挙げられます。これらのサービスと連携することで、運用監視やセキュリティ対策、スケーリングなどのクラウドネイティブな運用が実現できます。今回のアップデートにより、AKS環境でのネットワーク管理がよりシームレスかつ効率的に行えるようになりました。

---

### 3. Generally Available: Azure Elastic SAN support for AVS Gen2 Private Cloud  

**公開日時**: 2026年05月05日 16:00:38 UTC
**リンク**: [Generally Available: Azure Elastic SAN support for AVS Gen2 Private Cloud  ](https://azure.microsoft.com/updates?id=560909)

**アップデートID**: 560909
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Elastic SAN, Features

**要約**:

- 何が更新されたか  
Azure Elastic SANが、Azure VMware Solution（AVS）Gen2 Private Cloudで一般提供（GA）となりました。

- 主な変更点や新機能  
Elastic SANデータストアをAVS Gen2 Private Cloudで利用できるようになり、接続性とパフォーマンスが向上しました。従来必要だったExpressRoute Gatewayが不要となり、シンプルな接続構成が可能です。また、構成には単一のPrivate Endpointのみで十分となりました。

- 影響を受ける対象  
AVS Gen2 Private Cloud環境でストレージ拡張やパフォーマンス向上を求める技術者、およびElastic SANを活用したいユーザーが対象です。

- 注意点があれば記載  
ExpressRoute Gatewayが不要になったことでネットワーク設計が簡素化されますが、Private Endpointの設定やセキュリティに関するベストプラクティスの遵守が引き続き重要です。詳細な要件や制限事項については公式ドキュメントを参照してください。

**詳細**:

今回のAzure Updateは、「Azure Elastic SAN support for AVS Gen2 Private Cloud」が一般提供（GA）されたことに関するものです。背景として、Azure VMware Solution（AVS）Gen2 Private Cloud環境において、ストレージの接続性やパフォーマンスの向上が求められていました。従来、AVS環境で外部ストレージを利用する場合、複雑なネットワーク構成やExpressRoute Gatewayの設定が必要でしたが、今回のアップデートにより、Elastic SANデータストアの利用が大幅に簡素化されました。

具体的な変更内容として、Elastic SANデータストアをAVS Gen2 Private Cloudで利用する際、ExpressRoute Gatewayの構築が不要となり、ネットワーク構成や管理の負担が軽減されます。また、接続設定においては、単一のPrivate Endpointを用いるだけでElastic SANデータストアの構成が可能となりました。これにより、セキュリティとシンプルな接続性を両立しつつ、従来よりも迅速かつ効率的なストレージの導入が実現します。

技術的な仕組みとしては、Elastic SANはAzure上で提供されるスケーラブルなストレージサービスであり、Private Endpointを通じてAVS環境と安全に接続されます。ExpressRoute Gatewayを介さずに直接Private Endpointで接続することで、ネットワークの複雑さが排除され、構成作業が容易になります。これにより、AVS Gen2 Private Cloud上の仮想マシンやワークロードがElastic SANの高性能ストレージを利用できるようになります。

活用シナリオとしては、AVS Gen2 Private Cloud上で大容量かつ高性能なストレージが必要な場合や、ストレージ管理の簡素化を求める企業にとって有効です。例えば、データベースやファイルサーバーなど、ストレージI/Oが重要なワークロードをElastic SANに配置することで、パフォーマンス向上と管理効率化を図ることができます。

注意点としては、今回のアップデートはAVS Gen2 Private Cloud環境に限定されていること、またElastic SANデータストアの利用にはAzureのPrivate Endpoint設定が必要となるため、ネットワークセキュリティやアクセス制御の設計が重要です。さらに、ExpressRoute Gatewayを利用しない構成となるため、既存のネットワーク設計との整合性を確認する必要があります。

関連するAzureサービスとしては、Elastic SAN自体の管理や監視にはAzure MonitorやAzure Security Centerなどのサービスと連携することが可能です。AVS環境とElastic SANの組み合わせにより、クラウド上でVMwareワークロードのストレージ拡張が柔軟に行えるようになりました。

---

### 4. Generally Available: Single Volume Snapshots on Azure Elastic SAN

**公開日時**: 2026年05月05日 16:00:38 UTC
**リンク**: [Generally Available: Single Volume Snapshots on Azure Elastic SAN](https://azure.microsoft.com/updates?id=560899)

**アップデートID**: 560899
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Elastic SAN, Features

**要約**:

【何が更新されたか】  
Azure Elastic SANで「単一ボリュームスナップショット」機能が一般提供（GA）されました。

【主な変更点や新機能】  
これまでElastic SAN全体のスナップショットのみが利用可能でしたが、今回のアップデートにより、個々のSANボリューム単位で増分型のポイントインタイムスナップショットを取得できるようになりました。スナップショットは前回からの変更分のみを保存し、Elastic SAN内部に格納されます。これにより、バックアップや新規ボリュームの迅速なデプロイが可能となります。

【影響を受ける対象】  
Azure Elastic SANを利用しているユーザーや、SANボリューム単位でバックアップやリストアを行いたい技術者が対象です。

【注意点】  
スナップショットはElastic SAN内に保存されるため、ストレージ容量や管理方法に注意が必要です。また、スナップショットの取得や復元操作はAzureポータルやAPIを通じて行う必要があります。

**詳細**:

Azure Elastic SANにおいて、シングルボリュームスナップショット機能が一般提供（GA）となりました。このアップデートの背景には、エンタープライズ環境でのストレージ管理の柔軟性向上と、データ保護・バックアップ運用の効率化が求められていたことがあります。従来のElastic SANでは、ボリューム単位でのバックアップやリストアが容易ではなく、全体のスナップショットや外部バックアップソリューションに依存するケースが多くありました。今回のアップデートにより、個々のSANボリュームごとに増分型のポイントインタイムスナップショットを取得できるようになり、より細粒度なデータ保護が可能となっています。

具体的な機能としては、Azure Elastic SAN内の各ボリュームに対してスナップショットを作成することができ、スナップショットは前回取得したスナップショット以降の変更分のみを保存します。これにより、ストレージ消費量を最小限に抑えつつ、迅速なバックアップとリストアが実現できます。スナップショットはElastic SAN内に保持されるため、外部ストレージへの転送や管理の手間が不要です。また、スナップショットから新規ボリュームを迅速にデプロイすることも可能であり、テスト環境の複製や障害時のリカバリにも活用できます。

技術的な仕組みとしては、Azure Elastic SANの内部でスナップショット管理が行われ、増分スナップショット方式により、変更ブロックのみを記録します。これにより、従来のフルバックアップと比較してストレージ効率が大幅に向上します。スナップショットはSAN内に格納されるため、ネットワーク帯域や外部ストレージの容量を消費しません。

活用シナリオとしては、定期的なバックアップ運用、障害発生時の迅速なリストア、開発・テスト環境の複製、データ保護ポリシーの実装などが挙げられます。特に、ミッションクリティカルなシステムや大規模データベースの運用において、ポイントインタイムでのリカバリや環境複製が求められる場合に有効です。

注意点としては、スナップショットがElastic SAN内に保持されるため、SANのストレージ容量管理が重要となります。また、スナップショットの取得やリストア操作にはAzureポータルやAPIを利用する必要があります。スナップショットの保持期間や最大数などの制限事項については、公式ドキュメントを参照する必要があります。

関連するAzureサービスとしては、Azure BackupやAzure Site Recoveryなどがありますが、Elastic SANのスナップショット機能はこれらとは独立して動作します。Elastic SANを利用したストレージ環境において、より効率的かつ柔軟なデータ保護・運用が可能となるアップデートです。

---

### 5. Generally Available: AVS Support for AV64 SKU on Azure Elastic SAN

**公開日時**: 2026年05月05日 16:00:38 UTC
**リンク**: [Generally Available: AVS Support for AV64 SKU on Azure Elastic SAN](https://azure.microsoft.com/updates?id=560894)

**アップデートID**: 560894
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Elastic SAN, Features

**要約**:

- 何が更新されたか  
Azure Elastic SANのデータストアが、Azure VMware Solution（AVS）のAV64 SKUでサポートされるようになりました。

- 主な変更点や新機能  
今回のアップデートにより、AV64 SKUを利用したAVS環境でElastic SANをストレージとして利用できるようになりました。これにより、より大規模かつ高性能なストレージオプションが利用可能となります。

- 影響を受ける対象  
Azure VMware Solution（AVS）をAV64 SKUで利用している、もしくは今後利用を検討しているユーザーや管理者が対象です。特に、拡張性やパフォーマンス向上を求めるシナリオで恩恵があります。

- 注意点があれば記載  
Elastic SANの利用には別途設定やコストが発生する場合があります。既存のAVSデプロイメントでAV64 SKUへの変更を検討する際は、互換性や運用面の影響を事前に確認することを推奨します。

**詳細**:

本アップデートは、Azure Elastic SANデータストアがAV64 SKUに対応したことを示しています。これにより、Azure VMware Solution（AVS）環境において、より大規模かつ高性能なストレージオプションの利用が可能となりました。背景としては、AVSの導入が進む中で、仮想化基盤のストレージ要件が増大し、従来のストレージ構成では対応しきれないケースが増えていたことが挙げられます。Elastic SANは、Azure上でスケーラブルかつ高可用性のSANストレージを提供するサービスであり、AV64 SKUはその中でも高いスペックを持つ仮想マシンサイズです。今回のアップデートでは、AV64 SKUを利用するAVS環境でElastic SANデータストアを直接利用できるようになりました。

具体的な変更内容としては、AV64 SKUの仮想マシン上でElastic SANデータストアのマウントと利用がサポートされるようになった点です。これにより、AVS環境の仮想マシンがElastic SANのストレージリソースを効率的に利用できるようになります。技術的な仕組みとしては、Azure VMware Solutionのクラスタ内からElastic SANに接続し、データストアとして利用することで、従来のAzure Diskや他のストレージサービスよりも高いスケーラビリティとパフォーマンスを実現しています。

活用シナリオとしては、エンタープライズ規模の仮想化環境や、大量のデータを高速に処理する必要があるワークロードにおいて、AV64 SKUとElastic SANの組み合わせが有効です。たとえば、ミッションクリティカルなアプリケーションや大規模なデータベース、VDI環境などで、ストレージ性能や容量がボトルネックとなる場合に、今回のアップデートによって解決策を提供できます。

注意点としては、Elastic SANの利用にあたっては、対応するSKUやAzure VMware Solutionのバージョン、ネットワーク構成など、事前に要件を確認する必要があります。また、Elastic SANの料金体系や管理方法についても理解しておくことが重要です。制限事項については、AV64 SKU以外の仮想マシンサイズでのElastic SANデータストア利用がサポートされているかどうか、公式ドキュメントで確認する必要があります。

関連するAzureサービスとの連携としては、Azure VMware SolutionとElastic SANの組み合わせにより、仮想化基盤のストレージ拡張が容易になり、Azure上の他のストレージサービスやバックアップサービスと連携した運用が可能となります。今回のアップデートは、AVS環境の拡張性とパフォーマンス向上を実現する重要な機能追加です。

---


*このレポートは自動生成されました - 2026-05-06 12:01:27 JST*