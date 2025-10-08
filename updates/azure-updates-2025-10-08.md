# 2025年10月08日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年10月08日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 5 件

## 更新一覧

### 1. Retirement: Azure Network Policy Manager (NPM) for Windows nodes on AKS to Be Retired by September 30, 2026

**公開日時**: 2025年10月07日 21:30:21 UTC
**リンク**: [Retirement: Azure Network Policy Manager (NPM) for Windows nodes on AKS to Be Retired by September 30, 2026](https://azure.microsoft.com/updates?id=500273)

**アップデートID**: 500273
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）上のWindowsノード向けAzure Network Policy Manager（NPM）のサポートが2026年9月30日で終了予定。

- 主な変更点や新機能  
WindowsノードのNPMは廃止され、代替のネットワークポリシー管理手段の検討が推奨される。

- 影響を受ける対象  
AKSのWindowsノードでNPMを利用しているユーザー。

- 注意点  
サポート終了後はセキュリティ更新や互換性が保証されないため、早めに代替ソリューションへの移行を検討する必要がある。

**詳細**:

本アップデートは、2026年9月30日をもってAKSのWindowsノードにおけるAzure Network Policy Manager（NPM）のサポートを終了することを通知するものです。背景には、Windowsノード向けNPMのメンテナンス負荷やセキュリティ対応の複雑化があり、より安定的かつ効率的なネットワークポリシー管理手法への移行を促す目的があります。NPMはKubernetesのネットワークポリシーをWindows環境で実現するためのコンポーネントであり、Windowsノード上でのポッド間通信制御を担ってきましたが、今後は代替としてCalicoなどの他のネットワークプラグインの利用が推奨されます。技術的には、NPMはWindows Filtering Platform（WFP）を活用し、ポリシーをWindowsカーネルレベルで適用していましたが、サポート終了後はこれが利用できなくなるため、Windowsノードのネットワークポリシー管理は別の方法に切り替える必要があります。活用シナリオとしては、WindowsベースのAKSクラスターでのセキュアなポッド間通信制御が挙げられますが、今後はCalicoのWindows対応版などを検討し、移行計画を早期に策定することが重要です。注意点として、サポート終了後はNPM利用環境でのセキュリティ更新やバグ修正が提供されなくなり、運用リスクが増大します。関連サービスとしては、AKS自体のネットワークプラグイン設定やAzure Policyによるガバナンス管理と連携し、包括的なセキュリティ対策を講じることが推奨されます。詳細は公式アップデート（https://azure.microsoft.com/updates?id=500273）を参照してください。

---

### 2. Generally Available: Azure Firewall Updates - IP Group limit increased to 600 per Firewall Policy 

**公開日時**: 2025年10月07日 16:30:20 UTC
**リンク**: [Generally Available: Azure Firewall Updates - IP Group limit increased to 600 per Firewall Policy ](https://azure.microsoft.com/updates?id=511722)

**アップデートID**: 511722
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Azure Firewall, Features

**要約**:

- 何が更新されたか  
Azure Firewall PolicyのIPグループ数制限が200から600に拡大されました。

- 主な変更点や新機能  
1ポリシーあたり最大600のIPグループを管理可能となり、長いIPリストを整理しルールの複雑さを軽減できます。

- 影響を受ける対象  
Azure Firewallを利用し、大規模なIPベースのアクセス制御を行うネットワーク管理者。

- 注意点があれば記載  
増加したIPグループ数に伴い、ポリシー設計時のパフォーマンスや管理負荷を考慮してください。

**詳細**:

本アップデートにより、Azure Firewall Policyで管理可能なIPグループ数が従来の200から600に大幅に拡張されました。背景には、大規模環境でのIPアドレス管理の複雑化があり、IPリストをIPグループに集約することでルールセットの可読性と保守性を向上させる目的があります。具体的には、Firewall Policy内で定義可能なIPグループ数が3倍に増加し、より細分化・階層化されたアクセス制御が可能となりました。技術的には、IPグループはCIDRや単一IPをまとめて管理し、ポリシーのルールで参照する形で適用されます。これにより、冗長なルール記述を削減し、ポリシーのパフォーマンス最適化にも寄与します。活用例としては、多数の拠点やサービスごとに異なるIP範囲をグルーピングし、柔軟かつスケーラブルなアクセス制御を実現可能です。注意点としては、IPグループ数増加に伴うポリシーの複雑化や管理負荷の増大に留意し、適切な命名規則やドキュメント管理が推奨されます。また、Azure FirewallはAzure MonitorやAzure Sentinelと連携し、IPグループ単位でのログ分析やセキュリティ監視が強化可能です。本アップデートは大規模ネットワーク環境でのセキュリティポリシー管理効率化に貢献します。

---

### 3. Generally Avaialbe: Azure NetApp Files short-term clones 

**公開日時**: 2025年10月07日 14:30:18 UTC
**リンク**: [Generally Avaialbe: Azure NetApp Files short-term clones ](https://azure.microsoft.com/updates?id=503836)

**アップデートID**: 503836
**情報源**: Azure Updates API

**カテゴリ**: Launched, Features

**要約**:

- 何が更新されたか  
Azure NetApp Filesの短期クローン機能が一般提供（GA）開始。

- 主な変更点や新機能  
既存ボリュームのスナップショットから即時に薄型クローンを作成可能。フルコピー不要で容量節約と高速な読み書きアクセスを実現。

- 影響を受ける対象  
Azure NetApp Filesを利用する開発者や運用担当者、特にテスト環境やソフトウェア開発でのデータ複製が必要なケース。

- 注意点  
短期クローンは一時的な利用を想定しており、長期保存には適さないため運用設計に注意が必要。

情報源: https://azure.microsoft.com/updates?id=503836

**詳細**:

Azure NetApp Filesのshort-term clones機能は、既存のボリュームスナップショットから一時的かつ薄型のクローンを即座に作成し、読み書きアクセスを可能にする技術です。これにより、従来のフルコピーを必要とせず、ストレージ容量の大幅な節約が実現します。主にソフトウェア開発やテスト環境での迅速なデータ複製に最適化されています。技術的には、スナップショットの差分データを参照しながらクローンを生成し、書き込み時のみ差分を保存するコピーオンライト方式を採用しています。これにより、クローン作成は数秒で完了し、ストレージ消費も最小限に抑えられます。活用例としては、開発者が本番データのスナップショットから短期間のテスト環境を即座に構築し、検証後にクローンを削除するケースが挙げられます。注意点として、short-term clonesは最大30日間の利用に適しており、長期保存には向きません。また、クローン数やサイズに制限があるため、運用前にAzure NetApp Filesの容量プランとポリシーを確認する必要があります。Azure Kubernetes Service (AKS)やAzure DevOpsと連携することで、CI/CDパイプライン内での高速な環境複製が可能となり、開発効率の向上に寄与します。詳細は公式ドキュメントおよび管理ポータルでの設定手順を参照してください。

---

### 4. Retirement: Legacy Authentication in Azure Monitor - Container Insights will be retired on September 30, 2026.

**公開日時**: 2025年10月07日 13:00:16 UTC
**リンク**: [Retirement: Legacy Authentication in Azure Monitor - Container Insights will be retired on September 30, 2026.](https://azure.microsoft.com/updates?id=500853)

**アップデートID**: 500853
**情報源**: Azure Updates API

**カテゴリ**: DevOps, Management and governance, Azure Monitor, Retirements

**要約**:

- 何が更新されたか  
Azure MonitorのContainer InsightsにおけるLegacy Authenticationが2026年9月30日に廃止されます。

- 主な変更点や新機能  
より安全なManaged Identity認証方式へ完全移行が必要となります。Managed Identity利用によりセキュリティ強化とアクセス管理が向上します。

- 影響を受ける対象  
Container InsightsでLegacy Authenticationを利用しているユーザーやシステム。

- 注意点  
廃止までにManaged Identity認証への移行を完了させないと監視機能に支障が出るため、早めの対応が推奨されます。

**詳細**:

本アップデートは、Azure MonitorのContainer Insightsにおけるレガシー認証方式の廃止を告知するものです。2026年9月30日をもって、従来のレガシー認証が廃止され、より安全なManaged Identity認証へ完全移行が求められます。レガシー認証は主にアクセスキーや資格情報の手動管理を伴い、セキュリティリスクが高いため、Azure ADのManaged Identityを用いた自動認証方式に置き換えられています。Managed IdentityはAzureリソースに対して自動的にトークンを発行し、キー管理不要で安全なアクセスを実現します。移行にあたっては、Container Insightsの設定を見直し、Azure AD認証を有効化する必要があります。これにより、Kubernetesクラスターやコンテナの監視データ収集時の認証が強化され、Azure MonitorやLog Analyticsとの連携がより安全かつ効率的になります。注意点として、移行前に既存の認証設定を確認し、Managed Identityが適切に割り当てられているか検証することが重要です。また、オンプレミスや他クラウド環境からのアクセスには別途認証構成が必要となる場合があります。関連サービスとしては、Azure Kubernetes Service（AKS）、Log Analytics、Azure Active Directoryが密接に連携し、統合監視とセキュアな認証基盤を提供します。

---

### 5. Generally Available: AI toolchain operator add-on (KAITO) for AKS 

**公開日時**: 2025年10月07日 12:00:49 UTC
**リンク**: [Generally Available: AI toolchain operator add-on (KAITO) for AKS ](https://azure.microsoft.com/updates?id=503263)

**アップデートID**: 503263
**情報源**: Azure Updates API

**カテゴリ**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**要約**:

- 何が更新されたか  
AKS向けAIツールチェーンオペレーターアドオン（KAITO）が一般提供開始。

- 主な変更点や新機能  
vLLMをデフォルト推論エンジンに採用し、オープンソースAIフレームワークを用いた推論・ファインチューニングのデプロイを簡素化。

- 影響を受ける対象  
AKS上でAI推論・モデル調整を行う開発者・運用者。

- 注意点があれば記載  
vLLMの特性理解とAKS環境でのリソース管理が重要。

**詳細**:

Azure Kubernetes Service（AKS）向けAIツールチェーンオペレーターアドオン「KAITO」がGA（一般提供）となりました。本アドオンは、vLLMをデフォルトの推論エンジンとして採用し、オープンソースのAIフレームワークを用いた推論およびファインチューニングのワークフローを自動化・簡素化します。具体的には、モデルのデプロイメント、スケーリング、バージョン管理をKubernetesネイティブに統合し、運用負荷を大幅に軽減。HelmチャートやCRD（カスタムリソース定義）を通じて設定可能で、CI/CDパイプラインとの連携も容易です。活用例としては、リアルタイム推論サービスやカスタムモデルの継続的学習環境構築が挙げられます。一方、vLLMはGPUリソースを多用するため、クラスターのリソース管理に注意が必要です。Azure Machine LearningやAzure Monitorと連携することで、モデルのパフォーマンス監視やログ収集が可能となり、運用効率をさらに向上させます。詳細は公式ドキュメントおよびアップデートページを参照してください。

---


*このレポートは自動生成されました - 2025-10-08 12:01:51 JST*