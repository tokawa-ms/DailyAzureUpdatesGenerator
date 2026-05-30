# 2026年05月30日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年05月30日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Retirement: AI Services Metrics Advisor is retired as of May 18, 2026

**公開日時**: 2026年05月29日 19:00:24 UTC
**リンク**: [Retirement: AI Services Metrics Advisor is retired as of May 18, 2026](https://azure.microsoft.com/updates?id=ai-services-metrics-advisor-will-be-retired-on-1-october-2026)

**アップデートID**: ai-services-metrics-advisor-will-be-retired-on-1-october-2026
**情報源**: Azure Updates API

**カテゴリ**: Services, Retirements

**要約**:

- 何が更新されたか  
Azure AI Metrics Advisorが2026年5月18日をもってリタイア（提供終了）となりました。

- 主な変更点や新機能  
Metrics Advisorのサービス提供が終了し、今後は利用できなくなります。代替サービスとして、Azure Monitorが推奨されています。Azure Monitorでは、異常検知や分析機能が複数のインターフェースを通じて提供されています。

- 影響を受ける対象  
現在Metrics Advisorを利用している全てのユーザーおよびシステムが影響を受けます。既存のワークロードやアプリケーションでMetrics Advisorを利用している場合、サービス終了までに移行対応が必要です。

- 注意点があれば記載  
Metrics Advisorのリタイア後はサービスが利用できなくなるため、早急にAzure Monitorなどの代替サービスへの移行計画を立ててください。移行に際しては、異常検知や分析要件に応じてAzure Monitorの機能を検討することを推奨します。

**詳細**:

2026年5月18日をもって、Azure AI Metrics Advisorは正式にリタイアされました。本サービスは、時系列データに対する異常検知や分析機能を提供していたAIサービスであり、特に運用監視やビジネスインテリジェンスの分野で利用されてきました。今回のリタイアに伴い、Microsoftは代替手段としてAzure Monitorの利用を推奨しています。

Azure Monitorは、Azureプラットフォーム全体の監視および可観測性を提供するサービスであり、Metrics Advisorが担っていた異常検知や分析機能も、複数のインターフェースを通じて実現可能です。これにより、既存のMetrics Advisorユーザーは、Azure MonitorのAPIやポータルを活用して、メトリクスデータの収集、可視化、アラート設定、異常検知などの運用を継続できます。

技術的には、Azure MonitorはLog AnalyticsやApplication Insightsと連携し、収集したデータに対してクエリや分析を実施できます。また、異常検知機能についても、組み込みの分析アルゴリズムやカスタムルールを用いて柔軟に設定が可能です。これにより、システムやアプリケーションのパフォーマンス監視、障害の早期検知、運用自動化などのシナリオに対応できます。

注意点として、Metrics Advisor固有の機能やAPIを利用していた場合は、Azure Monitorへの移行に際して実装の変更や再設計が必要となる場合があります。また、サービスリタイア後はMetrics Advisorへの新規アクセスやサポートが提供されなくなるため、早期の移行計画策定が重要です。

Azure Monitorは他のAzureサービスとも密接に連携しており、たとえばAzure Logic AppsやAzure Functionsと組み合わせることで、異常検知をトリガーとした自動化ワークフローの構築も可能です。今後はAzure Monitorを中心とした監視・分析基盤への移行が推奨されます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=ai-services-metrics-advisor-will-be-retired-on-1-october-2026）を参照してください。

---

### 2. Public Preview: Azure Site Recovery Support for Performance Plus Managed Disks

**公開日時**: 2026年05月29日 15:15:43 UTC
**リンク**: [Public Preview: Azure Site Recovery Support for Performance Plus Managed Disks](https://azure.microsoft.com/updates?id=564644)

**アップデートID**: 564644
**情報源**: Azure Updates API

**カテゴリ**: In preview, Management and governance, Migration, Azure Site Recovery, Features, Management

**要約**:

- 何が更新されたか  
Azure Site Recovery（ASR）が、Performance Plus機能を有効にしたマネージドディスクを利用する仮想マシンのレプリケーションをサポートするようになりました。今回のアップデートはパブリックプレビュー段階です。

- 主な変更点や新機能  
Premium SSD、Standard SSD、Standard HDDの各種マネージドディスクでPerformance Plus機能を有効化している場合でも、ASRによるディザスタリカバリーのためのVMレプリケーションが可能になりました。これにより、より高いディスクパフォーマンスを維持しつつ、可用性向上や災害対策が実現できます。

- 影響を受ける対象  
Performance Plusが有効なマネージドディスクを利用している仮想マシンをASRで保護したいユーザーや、既存のASR環境で高性能ディスクを活用したい技術者が対象です。

- 注意点があれば記載  
本機能はパブリックプレビュー段階のため、本番環境での利用には十分な検証が推奨されます。また、サポート対象のディスク種別やリージョンなど、詳細は公式ドキュメントの確認が必要です。

**詳細**:

Azure Site Recovery（ASR）は、Azure上の仮想マシンのディザスターリカバリーを実現するためのサービスです。今回のアップデートでは、ASRがPerformance Plus機能を有効にしたマネージドディスクを利用する仮想マシンのレプリケーションをサポートするようになりました。Performance Plusは、Premium SSD、Standard SSD、Standard HDDといった各種マネージドディスクに対して追加のパフォーマンスを提供する機能です。このアップデートにより、これらのディスクタイプでPerformance Plusが有効化されている仮想マシンも、ASRによるレプリケーションおよびフェールオーバーの対象となります。

具体的な機能としては、Performance Plus対応ディスクを持つ仮想マシンのデータを、ASRの標準的なレプリケーションプロセスを用いて別リージョンやセカンダリサイトに複製することが可能となります。これにより、ディスクのパフォーマンス要件が高いワークロードでも、従来通りASRを利用したBCP（事業継続計画）やDR（災害復旧）対策が実現できます。技術的には、ASRのレプリケーションエージェントがPerformance PlusディスクのI/O特性や拡張パフォーマンスを認識し、データ転送や整合性維持を行う仕組みとなっています。

活用シナリオとしては、ミッションクリティカルなアプリケーションや高トランザクションなデータベースなど、ディスクI/O性能が重要なシステムのディザスターリカバリー設計で有効です。たとえば、Premium SSD Performance Plusを利用したSQL Server仮想マシンのDR対策や、Standard SSD Performance Plusを用いたWebサーバーの可用性向上などが挙げられます。

注意点としては、現時点ではパブリックプレビューでの提供となっているため、本番環境での利用には慎重な検証が必要です。また、Performance Plus機能を有効にしたディスクのASRレプリケーションには、通常のディスクと同様にAzureのリージョン間レプリケーションやストレージアカウントの制限事項が適用される場合があります。詳細な制限事項やサポート範囲については、公式ドキュメントやサポート情報を参照することが推奨されます。

関連するAzureサービスとしては、Azure BackupやAzure Virtual Machinesが挙げられます。ASRはこれらのサービスと連携し、包括的なデータ保護および可用性ソリューションを構築する際の重要なコンポーネントとなります。今回のアップデートにより、より高性能なディスク環境でもASRを活用した堅牢なディザスターリカバリー設計が可能となりました。

---


*このレポートは自動生成されました - 2026-05-30 12:00:48 JST*