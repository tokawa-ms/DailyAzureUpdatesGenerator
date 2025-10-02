# 2025年10月02日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年10月02日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 4 件

## 更新一覧

### 1. Public Preview: MSSQL extension integration with Microsoft Fabric 

**公開日時**: 2025年10月01日 17:30:57 UTC
**リンク**: [Public Preview: MSSQL extension integration with Microsoft Fabric ](https://azure.microsoft.com/updates?id=503646)

**アップデートID**: 503646
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Analytics, Azure SQL Database, Microsoft Fabric, Features

**要約**:

- 何が更新されたか  
MSSQL拡張機能がVisual Studio CodeでMicrosoft FabricのSQLデータベースと統合され、パブリックプレビュー提供開始。

- 主な変更点や新機能  
接続ダイアログにFabric接続オプションが追加され、Microsoft Entra IDでサインイン可能。Fabric内のSQLデータベースを直接参照・操作できる。

- 影響を受ける対象  
VS CodeでMSSQL拡張を利用する開発者や、Microsoft Fabric上のデータベースを扱う技術者。

- 注意点  
現時点はパブリックプレビューのため、本番環境での利用は慎重に。Microsoft Entra IDの認証設定が必要。

**詳細**:

本アップデートは、Visual Studio CodeのMSSQL拡張機能にMicrosoft FabricのSQLデータベース接続を統合し、開発者の作業効率向上を目的としています。新たに追加された「Fabric接続オプション」では、接続ダイアログからMicrosoft Entra IDによる認証が可能となり、Fabric環境内のSQLデータベースを直接参照・操作できます。技術的には、OAuth 2.0ベースのEntra ID認証を経て、FabricのAPI経由でデータベースメタ情報を取得し、VS Code内でクエリ実行やスキーマ閲覧が可能です。これにより、ローカル開発環境からクラウド上のFabricリソースへのシームレスなアクセスが実現します。活用例としては、データパイプライン開発や分析クエリの迅速な検証が挙げられます。注意点としては、現時点でパブリックプレビューのため一部機能が限定的であり、Entra IDの適切な権限設定が必須です。関連サービスとしてAzure Synapse AnalyticsやAzure Data Factoryとの連携も想定され、Fabricを中心とした統合データ分析環境の構築に寄与します。

---

### 2. Retirement: Azure Machine Learning - Data labeling Deprecation

**公開日時**: 2025年10月01日 17:30:57 UTC
**リンク**: [Retirement: Azure Machine Learning - Data labeling Deprecation](https://azure.microsoft.com/updates?id=501692)

**アップデートID**: 501692
**情報源**: Azure Updates API

**カテゴリ**: AI + machine learning, Internet of Things, Azure Machine Learning, Retirements

**要約**:

- 何が更新されたか  
Azure Machine Learningのデータラベリング機能が2026年9月30日に廃止されることが発表されました。

- 主な変更点や新機能  
2026年9月30日以降、Azureのデータラベリングは利用できなくなり、サードパーティのデータラベリングサービスへの移行が必要です。

- 影響を受ける対象  
Azure Machine Learningのデータラベリング機能を利用している技術者や組織。

- 注意点  
2026年9月30日までは従来通り利用可能ですが、早めに代替サービスへの移行計画を立てることを推奨します。

**詳細**:

Azure Machine Learningのデータラベリング機能は、2026年9月30日をもって廃止されます。本アップデートの背景には、より専門的かつ多様なラベリングニーズに対応するため、サードパーティのデータラベリングサービスへの移行促進があります。廃止までの期間は既存機能が継続利用可能ですが、それ以降はAzure上でのネイティブなラベリングサポートが停止します。技術的には、Azure ML内のラベリングジョブ作成・管理UIやAPIが利用不可となり、代替としてLabelboxやScale AIなど外部サービスとの連携が推奨されます。実装面では、Azure MLのデータセットをエクスポートし、外部サービスでラベル付けを行い、結果を再インポートしてモデル学習に活用するワークフローが一般的です。活用シナリオは画像認識や自然言語処理の教師データ作成が中心で、ラベリング精度向上やコスト最適化が期待されます。注意点として、外部サービス利用時のデータセキュリティやAPI連携の互換性確認が必要です。また、Azure Cognitive ServicesやAzure Storageとの連携により、データ管理や前処理を効率化可能です。移行計画を早期に策定し、2026年9月末までにサードパーティサービスへの切り替えを完了することが推奨されます。詳細は公式ドキュメント（https://azure.microsoft.com/updates?id=501692）を参照してください。

---

### 3. Retirement: Azure Network Policy Manager (NPM) for Linux nodes on AKS to Be Retired by September 30, 2028

**公開日時**: 2025年10月01日 17:15:18 UTC
**リンク**: [Retirement: Azure Network Policy Manager (NPM) for Linux nodes on AKS to Be Retired by September 30, 2028](https://azure.microsoft.com/updates?id=500268)

**アップデートID**: 500268
**情報源**: Azure Updates API

**カテゴリ**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements

**要約**:

- 何が更新されたか  
Azure Kubernetes Service（AKS）上のLinuxノード向けAzure Network Policy Manager（NPM）が2028年9月30日にサポート終了。

- 主な変更点や新機能  
NPMからCilium Network Policyへの移行が推奨される。

- 影響を受ける対象  
AKSでLinuxノードを使用しNPMを利用しているユーザー。

- 注意点  
期限までにNPMからCiliumへ移行しないとネットワークポリシー管理に影響が出る可能性がある。  

詳細：https://azure.microsoft.com/updates?id=500268

**詳細**:

本アップデートは、2028年9月30日をもってAKS上のLinuxノードにおけるAzure Network Policy Manager（NPM）のサポートを終了することを通知するものです。背景には、より高性能かつ柔軟なネットワークポリシー管理を実現するCilium Network Policyへの移行促進があります。NPMはWindows Azure CNIベースで動作し、Kubernetesのネットワークポリシーを実装しますが、CiliumはeBPF技術を活用し、レイヤー3からレイヤー7までの高度なポリシー制御や可観測性を提供します。移行は、既存のAKSクラスターでNPMを無効化し、Ciliumをネットワークポリシーエンジンとして有効化する手順を踏みます。CiliumはKubernetesのNetworkPolicy APIに加え、独自のCiliumNetworkPolicy CRDを用いて詳細なトラフィック制御が可能です。活用例としては、マイクロサービス間のセキュアな通信制御や、サービスメッシュとの連携によるトラフィック管理が挙げられます。注意点として、移行期間中はポリシーの適用漏れや通信断を防ぐため、段階的なテストと検証が必須です。また、CiliumのeBPFはLinuxカーネルバージョンに依存するため、対応カーネルの確認が必要です。Azure MonitorやAzure Policyと連携することで、ポリシー適用状況の監視やガバナンス強化が可能です。詳細は公式ドキュメントを参照し、2028年までに計画的な移行を推奨します。  
https://azure.microsoft.com/updates?id=500268

---

### 4. Public Preview: Azure SQL updates for late September 2025 

**公開日時**: 2025年10月01日 16:00:52 UTC
**リンク**: [Public Preview: Azure SQL updates for late September 2025 ](https://azure.microsoft.com/updates?id=503612)

**アップデートID**: 503612
**情報源**: Azure Updates API

**カテゴリ**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**要約**:

- 何が更新されたか  
Azure SQLの長期保持（LTR）バックアップに対するランサムウェア攻撃防御機能が追加されました。

- 主な変更点や新機能  
LTRバックアップの不変性（immutability）をサポートし、バックアップの改ざんや削除を防止可能に。

- 影響を受ける対象  
Azure SQLを利用し、LTRバックアップを運用しているユーザー。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用は慎重に検討してください。

情報源：https://azure.microsoft.com/updates?id=503612

**詳細**:

2025年9月下旬、Azure SQLは長期保持（LTR）バックアップに対するランサムウェア攻撃防御機能として「イミュータビリティ（不変性）」をパブリックプレビューで提供開始しました。LTRバックアップは長期間のデータ保持を目的とし、重要データの復旧に不可欠ですが、ランサムウェアによる改ざんや削除リスクが課題でした。本アップデートでは、バックアップファイルに対して一定期間の変更・削除を禁止するイミュータビリティポリシーを適用可能とし、悪意ある操作から保護します。技術的にはAzure Blob Storageのイミュータブルストレージ機能を活用し、Azure SQLのバックアップ管理APIからポリシー設定を行います。活用例としては、金融や医療など規制遵守が求められる業界でのデータ保護強化が挙げられます。注意点として、イミュータビリティ期間中はバックアップの削除や変更が不可となるため、運用計画に反映が必要です。また、Azure BackupやAzure Security Centerと連携し、監査やアラート設定が可能です。詳細は公式ドキュメントおよび管理ポータルで確認推奨します。

---


*このレポートは自動生成されました - 2025-10-02 12:01:27 JST*