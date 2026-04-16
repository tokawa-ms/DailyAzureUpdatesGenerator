# 2026年04月16日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年04月16日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Retirement: End of lift reminder of HBv2/HC-Series/NP-Series Azure Virtual Machine in Azure Batch Pool

**公開日時**: 2026年04月15日 17:30:33 UTC
**リンク**: [Retirement: End of lift reminder of HBv2/HC-Series/NP-Series Azure Virtual Machine in Azure Batch Pool](https://azure.microsoft.com/updates?id=559751)

**アップデートID**: 559751
**情報源**: Azure Updates API

**カテゴリ**: Compute, Batch, Retirements

**要約**:

- 何が更新されたか  
Microsoft Azureは、Azure Batchプールで利用可能なHBv2シリーズ、HCシリーズ、NPシリーズ仮想マシン（VM）のサポートを2027年5月31日に終了することを発表しました。

- 主な変更点や新機能  
今回のアップデートは、上記3シリーズ（HBv2: 120 AMD EPYC 7V12 vCPU/480GB RAM/200Gbps HDR InfiniBand、HC: 44 Intel Xeon Platinum 8168など）のVMがAzure Batchプールで利用できなくなる点が主な変更点です。新機能の追加はありません。

- 影響を受ける対象  
Azure BatchサービスでHBv2シリーズ、HCシリーズ、NPシリーズのVMを利用しているユーザーやシステムが影響を受けます。これらのVMを活用したHPC（ハイパフォーマンスコンピューティング）ワークロードを運用している環境が該当します。

- 注意点  
2027年5月31日以降、該当VMシリーズはAzure Batchプールで利用できなくなります。対象VMを利用している場合は、サポート終了前に他のVMシリーズへの移行計画を立てる必要があります。移行に伴うアプリケーションやワークフローの動作検証も早めに実施することを推奨します。

**詳細**:

本アップデートは、Microsoft Azureが2027年5月31日をもってAzure BatchプールにおけるHBv2シリーズ、HCシリーズ、NPシリーズ仮想マシン（VM）のサポートを終了することを通知するものです。これらのVMシリーズは、主に高性能コンピューティング（HPC）用途に特化した構成であり、HBv2シリーズは120コアのAMD EPYC 7V12 vCPU、480GB RAM、200Gb/s HDR InfiniBandインターコネクトを搭載し、HCシリーズは44コアのIntel Xeon Platinum 8168プロセッサを特徴としています。NPシリーズについても同様にHPCや特殊なワークロード向けに設計されています。

Azure Batchは、大規模な並列処理やバッチ処理を自動的にスケーリングし、管理するためのサービスであり、これらのHPC向けVMシリーズを利用することで、科学技術計算、CAE、レンダリング、機械学習などの高負荷な計算処理を効率的に実行することが可能でした。サポート終了により、2027年5月31日以降はAzure BatchプールにこれらのVMシリーズを新規に追加することができなくなり、既存のプールにおいてもこれらのVMを利用したジョブの実行や管理ができなくなります。

技術的には、Azure Batchのプール作成時に指定するVMサイズとして、HBv2、HC、NPシリーズが選択できなくなることを意味します。これにより、これらのシリーズを前提としたジョブスケジューリングやリソース管理の自動化フローも見直しが必要となります。既存の活用シナリオとしては、分子動力学シミュレーション、流体解析、ディープラーニングの分散学習などが挙げられますが、今後はAzureが提供する他のHPC対応VMシリーズやサービスへの移行を検討する必要があります。

注意点として、サポート終了日以降はこれらのVMシリーズを利用したAzure Batchプールの新規作成や既存プールの拡張ができなくなるため、運用中のシステムやワークフローに影響が及ぶ可能性があります。関連するAzureサービスとしては、Azure CycleCloudやAzure Machine Learningなどがあり、これらのサービスと連携してHPCワークロードを管理している場合、早期に移行計画を策定することが重要です。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=559751）を参照してください。

---

### 2. Generally Available: Encrypt Premium SSD v2 and Ultra Disks with Cross Tenant Customer Managed Keys

**公開日時**: 2026年04月15日 17:15:38 UTC
**リンク**: [Generally Available: Encrypt Premium SSD v2 and Ultra Disks with Cross Tenant Customer Managed Keys](https://azure.microsoft.com/updates?id=559761)

**アップデートID**: 559761
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Disk Storage, Compliance, Security

**要約**:

- 何が更新されたか  
Premium SSD v2およびUltra Disksに対して、クロステナントでのカスタマーマネージドキー（CMK）による暗号化が一般提供（GA）されました。

- 主な変更点や新機能  
これまで同一テナント内のAzure Key Vaultに保存されたCMKのみ利用可能でしたが、今回のアップデートにより、異なるMicrosoft Entraテナントに存在するAzure Key VaultのCMKを使用して、Premium SSD v2およびUltra Disksを暗号化できるようになりました。

- 影響を受ける対象  
複数のAzureテナントを運用している企業や、セキュリティ要件によりキー管理を分離したい組織が対象です。特に、ストレージリソースとキー管理を別テナントで運用するケースで有用です。

- 注意点があれば記載  
クロステナントCMKを利用する場合は、適切なアクセス許可設定やKey Vaultの構成が必要です。また、運用前に公式ドキュメントでサポート条件や制限事項を確認することを推奨します。

**詳細**:

本アップデートは、「Premium SSD v2」および「Ultra Disks」に対して、クロステナントでのカスタマーマネージドキー（CMK）による暗号化が一般提供（GA）されたことを示しています。従来、Azure Managed Disksの暗号化には、同一テナント内のAzure Key Vaultに格納されたカスタマーマネージドキーを利用する必要がありましたが、今回のアップデートにより、異なるMicrosoft Entraテナント（旧Azure ADテナント）に存在するKey Vaultに保存されたCMKを利用して、Premium SSD v2およびUltra Disksの暗号化が可能となりました。

この機能の主な目的は、マルチテナント環境や複数組織間でのセキュリティポリシーやコンプライアンス要件に柔軟に対応することです。たとえば、ディスクを利用するリソースグループやサブスクリプションがAテナントに存在し、暗号化キーのみをBテナントで一元管理したい場合などに有効です。これにより、キー管理の分離や、組織間のセキュリティ境界を維持しつつ、ディスクの暗号化を実現できます。

技術的には、Azure Managed Disksの暗号化プロセスにおいて、ディスクリソースが参照するKey VaultのテナントIDを指定し、クロステナントアクセスを許可する必要があります。Key Vault側では、アクセス制御（アクセスポリシーまたはRBAC）を適切に設定し、ディスクの管理者が必要なキー操作（ラップ・アンラップ等）を実行できるようにします。また、Key Vaultとディスク間の通信はAzureのセキュアなチャネルを介して行われ、キーの漏洩リスクを低減しています。

活用シナリオとしては、グループ企業間でのリソース分離、委託先と委託元でのセキュリティ責任分担、またはグローバル企業における地域ごとのキー管理ポリシーの適用などが考えられます。たとえば、親会社がすべての暗号化キーを管理し、子会社ごとにAzure環境を分離運用する場合に、クロステナントCMK機能が役立ちます。

注意点としては、Key Vaultとディスク間のクロステナントアクセス権限の設定ミスによるアクセス障害や、キーのローテーション・削除時の影響範囲の把握が重要です。また、クロステナント構成においては、Azure Key Vaultの可用性やネットワーク設計にも留意する必要があります。

本機能は、Azure Key Vault、Microsoft Entra ID（旧Azure AD）、Azure Managed Disksなどのサービス連携を前提としています。これにより、Azure全体のセキュリティアーキテクチャに柔軟性と拡張性をもたらします。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=559761）を参照してください。

---


*このレポートは自動生成されました - 2026-04-16 12:01:55 JST*