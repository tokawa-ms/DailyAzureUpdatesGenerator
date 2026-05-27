# 2026年05月27日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年05月27日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Public Preview: Azure Virtual Network Manager integration with Virtual WAN 

**公開日時**: 2026年05月26日 18:00:01 UTC
**リンク**: [Public Preview: Azure Virtual Network Manager integration with Virtual WAN ](https://azure.microsoft.com/updates?id=564478)

**アップデートID**: 564478
**情報源**: Azure Updates API

**カテゴリ**: In preview, Networking, Virtual WAN, Azure Virtual Network Manager, Features, Management, Security, Services

**要約**:

【何が更新されたか】  
Azure Virtual Network Manager（VNM）がAzure Virtual WANとの統合に対応し、パブリックプレビューとして提供開始されました。

【主な変更点や新機能】  
今回のアップデートにより、Azure Virtual Network Managerのハブアンドスポーク構成において、Azure Virtual WANハブをハブとして利用できるようになりました。これにより、Virtual Network ManagerとVirtual WANの機能を組み合わせて、ネットワーク管理や接続性の設計が柔軟かつ効率的になります。

【影響を受ける対象】  
Azure Virtual Network ManagerおよびAzure Virtual WANを利用している技術者や、複数の仮想ネットワークをハブアンドスポーク構成で管理しているユーザーが対象です。特に、広域ネットワークや複雑なネットワーク構成を必要とする企業環境で恩恵を受けます。

【注意点】  
本機能はパブリックプレビュー段階のため、本番環境での利用には注意が必要です。サポートや機能の安定性については、今後の正式リリースまで確認が必要です。

詳細は公式アップデートページをご参照ください。

**詳細**:

Azure Virtual Network ManagerとAzure Virtual WANの統合がパブリックプレビューとして公開されました。このアップデートの背景には、Azure上で複雑なネットワーク構成を効率的に管理し、拡張性と柔軟性を高めるニーズがあります。従来、Virtual Network Managerによるハブアンドスポーク型の接続構成では、専用の仮想ネットワークハブを用いる必要がありましたが、今回のアップデートによりAzure Virtual WANハブをハブとして利用できるようになりました。これにより、Virtual WANのグローバルな接続性やセキュリティ機能を活用しつつ、Virtual Network Managerの一元管理機能を組み合わせることが可能となります。

具体的な機能変更としては、Virtual Network Managerのハブアンドスポーク構成において、Azure Virtual WANハブを選択できるようになった点が挙げられます。これにより、複数のスポークネットワークをVirtual WANハブに接続し、広域ネットワーク管理やルーティングの最適化を実現できます。技術的な仕組みとしては、Virtual Network ManagerがVirtual WANハブのリソースを認識し、スポークネットワークとの接続設定やポリシー適用を行う形となります。管理者はAzureポータルやAPIを通じて、ハブアンドスポーク構成の作成や変更を一元的に操作できます。

活用シナリオとしては、グローバルに分散した拠点や複数のリージョンにまたがるネットワーク構成を持つ企業が、Virtual WANの広域接続性を活用しつつ、Virtual Network Managerによるネットワーク管理やセキュリティポリシーの適用を効率化するケースが想定されます。また、複数のサブネットや仮想ネットワークを一元的に管理し、ルーティングやアクセス制御を統合する用途にも適しています。

注意点としては、現在パブリックプレビュー段階であるため、本番環境での利用は推奨されません。また、機能や制限事項については今後正式リリース時に変更される可能性があります。関連するAzureサービスとしては、Azure Virtual WAN、Azure Virtual Network Manager、Azureポータル、APIなどが挙げられます。これらのサービスとの連携により、広域ネットワークの構成管理やセキュリティ強化が実現できます。

詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=564478）をご参照ください。

---

### 2. Generally Available: Virtual network flow logs connector with Microsoft Sentinel

**公開日時**: 2026年05月26日 16:45:10 UTC
**リンク**: [Generally Available: Virtual network flow logs connector with Microsoft Sentinel](https://azure.microsoft.com/updates?id=564689)

**アップデートID**: 564689
**情報源**: Azure Updates API

**カテゴリ**: Launched, Management and governance, Networking, Network Watcher, Features

**要約**:

- 何が更新されたか  
Azure Virtual Network Flow Logs ConnectorがMicrosoft Sentinelと統合され、一般提供（GA）となりました。

- 主な変更点や新機能  
このアップデートにより、Virtual Network Flow LogsをMicrosoft Sentinelにシームレスにエクスポートし、ネットワークトラフィックデータをセキュリティ運用ワークフロー内で分析できるようになりました。これにより、ネットワークの可視化や脅威検出、インシデント対応が強化されます。

- 影響を受ける対象  
Azure Virtual Networkを利用している環境でネットワークフローの監視・分析を行っているセキュリティ担当者や運用管理者が主な対象です。Microsoft Sentinelを活用している組織にとって、ネットワークログの統合分析が可能になります。

- 注意点があれば記載  
本機能を利用するには、Virtual Network Flow Logsの設定とMicrosoft Sentinel環境の構築が必要です。ログのエクスポートや分析に伴うストレージやコスト管理にも注意してください。

**詳細**:

Azure Virtual Network Flow Logs Connector with Microsoft Sentinelが一般提供（GA）となりました。このアップデートの背景には、ネットワークトラフィックデータの可視化とセキュリティ運用の強化というニーズがあります。従来、Azure Virtual Networkのフローログはネットワークの可視化やトラブルシューティング、セキュリティ監査などに利用されてきましたが、これらのログデータをセキュリティ運用ワークフローにシームレスに統合することは容易ではありませんでした。今回のコネクターの一般提供により、これらの課題が解決され、ネットワークトラフィックデータをMicrosoft Sentinelに直接エクスポートし、統合的に分析できるようになりました。

具体的な機能としては、Azure Virtual NetworkのフローログをMicrosoft Sentinelに連携し、ネットワークトラフィックデータをセキュリティイベントとして取り込むことが可能です。これにより、Sentinel上での高度なクエリ、アラート生成、脅威ハンティング、インシデント対応などの一連のセキュリティ運用プロセスにネットワークデータを活用できます。変更内容としては、フローログのデータソースとしてSentinelがサポートされ、エクスポートや分析が一元化された点が挙げられます。

技術的な仕組みとしては、Azure Virtual NetworkのフローログがAzure Monitor経由で収集され、コネクターを介してMicrosoft SentinelのLog Analyticsワークスペースにデータが転送されます。これにより、SentinelのKusto Query Language（KQL）を用いた詳細な分析や、カスタムアラートルールの作成が可能となります。実装方法としては、Azureポータル上でコネクターの設定を行い、必要な権限とデータフローを構成することで連携が完了します。

活用シナリオとしては、ネットワーク上の異常な通信パターンの検出や、未承認の通信経路の監視、セキュリティインシデント発生時のトラフィック解析などが考えられます。例えば、特定のIPアドレスからの不審なアクセスや、通常とは異なるポートの利用状況をリアルタイムで検知し、即座にアラートを発報することが可能です。また、過去のトラフィックデータを用いたフォレンジック調査にも有効です。

注意点としては、フローログの収集・転送には追加のストレージやログ保持コストが発生する場合があるため、コスト管理が必要です。また、フローログの粒度や保持期間、サポートされるネットワーク構成などについては、公式ドキュメントでの確認が推奨されます。さらに、ログの転送や分析に伴う遅延や、対応するリージョンの制限なども考慮する必要があります。

本コネクターは、Microsoft SentinelとAzure Virtual Networkだけでなく、Azure MonitorやLog Analyticsなどの関連サービスとも連携して動作します。これにより、Azure上のさまざまなリソースからのセキュリティデータを統合し、包括的なセキュリティ監視基盤を構築することが可能となります。

---


*このレポートは自動生成されました - 2026-05-27 12:00:44 JST*