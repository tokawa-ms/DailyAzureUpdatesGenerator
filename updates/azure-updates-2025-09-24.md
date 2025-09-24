# 2025年09月24日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月24日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Generally Available: Azure Site Recovery Support for Virtual Machines with Premium SSD v2 disks

**公開日時**: 2025年09月23日 17:30:13 UTC
**リンク**: [Generally Available: Azure Site Recovery Support for Virtual Machines with Premium SSD v2 disks](https://azure.microsoft.com/updates?id=502998)

**アップデートID**: 502998
**情報源**: Azure Updates API

**カテゴリ**: Launched, Management and governance, Migration, Azure Site Recovery, Features, Management

**要約**:

- 何が更新されたか  
Azure Site Recovery（ASR）がPremium SSD v2ディスクを搭載した仮想マシンのサポートを一般提供開始。

- 主な変更点や新機能  
Premium SSD v2ディスクのVMに対しても、リージョン間およびオンプレミスからAzureへのシームレスなディザスタリカバリが可能に。

- 影響を受ける対象  
Premium SSD v2ディスクを利用するAzure VMの運用・バックアップ担当者。

- 注意点があれば記載  
既存のASR構成にPremium SSD v2対応が追加されたため、ディスク性能やコスト面の影響を考慮して設定を見直すことを推奨。

**詳細**:

本アップデートは、Azure Site Recovery（ASR）がPremium SSD v2ディスクを搭載した仮想マシン（VM）に対してGA（一般提供）となったことを発表しています。背景として、Premium SSD v2は従来のPremium SSDより高いIOPSとスループットを提供し、より高性能なストレージニーズに対応しています。これに伴い、ASRがPremium SSD v2対応を実現することで、これら高性能VMの災害復旧（DR）シナリオをネイティブにサポート可能となりました。

具体的には、ASRはAzureリージョン間およびオンプレミスからAzureへのレプリケーションにおいて、Premium SSD v2ディスクを持つVMのデータ整合性を保ちつつ、効率的なフェールオーバーとフェールバックを実現します。技術的には、ASRのレプリケーションエンジンがPremium SSD v2のストレージAPIに対応し、ディスクのスナップショット取得や変更ブロックの追跡を最適化しています。これにより、レプリケーション遅延の低減と復旧ポイント目標（RPO）の改善が期待できます。

活用シナリオとしては、ミッションクリティカルなアプリケーションを稼働させる高性能VMのDR対策が挙げられます。例えば、金融や製造業などで高IO性能を要求するワークロードの継続的な可用性確保に有効です。注意点としては、ASRのサポート対象リージョンやVMサイズ、OSの互換性を事前に確認する必要があります。また、Premium SSD v2の特性を活かすため、ネットワーク帯域やストレージアカウントの構成も最適化が求められます。

関連サービスとしては、Azure Monitorによるレプリケーション状態の監視、Azure Automationを用いたDR手順の自動化、Azure Backupとの併用による多層的なデータ保護が推奨されます。これにより、運用効率と復旧信頼性を高めることが可能です。詳細は公式ドキュメントおよびアップデートページ（https://azure.microsoft.com/updates?id=502998）を参照してください。

---

### 2. Retirement: NVv3-series Azure Virtual Machines will be retired on September 30 ,2026

**公開日時**: 2025年09月23日 16:00:30 UTC
**リンク**: [Retirement: NVv3-series Azure Virtual Machines will be retired on September 30 ,2026](https://azure.microsoft.com/updates?id=500573)

**アップデートID**: 500573
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

- 何が更新されたか  
NVv3シリーズの一部VM（Standard_NV12s_v3など）が2026年9月30日に廃止予定と発表。

- 主な変更点や新機能  
該当VMは利用不可となり、移行が必要。

- 影響を受ける対象  
NVv3シリーズの指定VMを使用中のユーザー。

- 注意点があれば記載  
廃止前に代替VMへの移行計画を立て、サービス停止を回避してください。

**詳細**:

本アップデートは、NVv3シリーズのGPU搭載仮想マシン（Standard_NV12s_v3、NV12hs_v3、NV24s_v3、NV24ms_v3、NV32ms_v3、NV48s_v3）が2026年9月30日に廃止されることを通知するものです。背景には、より高性能かつ効率的なGPU VMシリーズ（例：NVv4やNDシリーズ）への移行促進と、古いハードウェアのサポート終了による運用コスト削減があります。NVv3シリーズはNVIDIA Tesla M60 GPUを搭載し、主にリモートデスクトップ、グラフィックスレンダリング、機械学習推論などに利用されてきましたが、廃止に伴いこれらのワークロードは後継のGPU VMへ移行が推奨されます。移行時はGPUアーキテクチャやドライバ互換性、VMサイズのパフォーマンス差を考慮し、Azure CLIやPowerShellでのVM再デプロイやイメージ更新が必要です。なお、NVv3シリーズの廃止により、これらVMに依存するAzure BatchやAzure Machine LearningのGPUクラスター構成も見直しが必要です。移行計画を早期に策定し、サービス停止やパフォーマンス低下を回避してください。詳細は公式ドキュメントを参照のこと。

---

### 3. Generally Available: GitHub Copilot app modernization capabilities for Java and .NET are now available

**公開日時**: 2025年09月23日 15:00:40 UTC
**リンク**: [Generally Available: GitHub Copilot app modernization capabilities for Java and .NET are now available](https://azure.microsoft.com/updates?id=503603)

**アップデートID**: 503603
**情報源**: Azure Updates API

**カテゴリ**: Launched, Features

**要約**:

- 何が更新されたか  
GitHub CopilotのJavaおよび.NET向けアプリモダナイゼーション機能が一般提供（GA）となりました。

- 主な変更点や新機能  
コードのリファクタリングやモダン化を自動支援し、開発者の作業負荷を軽減。セキュリティやスケーラビリティ向上を促進します。

- 影響を受ける対象  
Java/.NET開発者やエンタープライズのアプリケーションモダナイゼーション担当者。

- 注意点があれば記載  
既存コードの特性により自動変換の精度が異なるため、結果の検証が必要です。

**詳細**:

本アップデートは、Javaおよび.NETアプリケーションのモダナイゼーションを支援するGitHub Copilotの機能が一般提供（GA）されたものです。従来、アプリケーションのモダナイゼーションはセキュリティ強化やスケーラビリティ確保のために不可欠ながら、複雑かつ冗長な作業が多く技術者の負担となっていました。GitHub CopilotはAIを活用し、コードのリファクタリングやクラウドネイティブ化に必要な変更提案をリアルタイムで提示することで、開発者の生産性向上と品質維持を実現します。

具体的には、レガシーコードの解析からマイクロサービス化、API設計の最適化、クラウド対応コードへの変換支援を行い、AzureのApp ServiceやAzure Functionsなどへの移行を容易にします。技術的にはGitHub CopilotのAIモデルがコードベースを理解し、Azure SDKやベストプラクティスに基づくコードスニペットを生成する仕組みです。IDE統合によりVisual StudioやVS Code上で直接利用可能です。

活用シナリオとしては、既存のオンプレミスJava/.NETアプリをAzure環境に移行する際のコード改修、クラウドネイティブ設計へのリファクタリング、セキュリティ強化のためのコード改善などが挙げられます。制限事項としては、AI提案が必ずしも最適解ではないため、専門家によるレビューが必要であり、複雑なビジネスロジックの完全自動化にはまだ課題があります。

Azure DevOpsやGitHub Actionsと連携することでCI/CDパイプラインに組み込み、モダナイゼーションの自動化や品質管理を強化可能です。これにより、継続的な改善と迅速なデプロイが促進され、企業のクラウド移行戦略を加速します。

---


*このレポートは自動生成されました - 2025-09-24 12:01:22 JST*