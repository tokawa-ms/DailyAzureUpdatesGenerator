# 2025年09月03日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年09月03日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 6 件

## 更新一覧

### 1. Retirement: Confidential VM SKUs DCesv5, DCedsv5, ECesv5, ECedsv5 SKUs

**公開日時**: 2025年09月02日 18:45:30 UTC
**リンク**: [Retirement: Confidential VM SKUs DCesv5, DCedsv5, ECesv5, ECedsv5 SKUs](https://azure.microsoft.com/updates?id=502039)

**アップデートID**: 502039
**情報源**: Azure Updates API

**カテゴリ**: Compute, Virtual Machines, Retirements, Services

**要約**:

- 何が更新されたか  
Confidential VMの旧SKU（DCesv5、DCedsv5、ECesv5、ECedsv5）が廃止されます。

- 主な変更点や新機能  
後継として性能向上した次世代SKU「DCesv6」「ECesv6」が公開プレビュー中です。

- 影響を受ける対象  
これら旧SKUを利用中のユーザーは、新SKUへの移行を検討する必要があります。

- 注意点があれば記載  
廃止に伴い旧SKUのサポート終了が予定されているため、早めの移行計画が推奨されます。

**詳細**:

本アップデートは、AzureのConfidential VM（機密コンピューティング対応仮想マシン）SKUであるDCesv5、DCedsv5、ECesv5、ECedsv5の廃止を告知し、後継のDCesv6およびECesv6 SKUへ移行を促すものです。背景には、次世代のIntel SGX対応プロセッサ搭載により、セキュリティ性能とパフォーマンスが向上した新SKUの提供があり、より高度な機密データ保護と効率的な処理を実現します。DCesv6/ECesv6はIntel SGX第3世代を採用し、より大容量の保護メモリを提供、暗号化処理の高速化や信頼できる実行環境（TEE）を強化しています。実装は既存のConfidential VM展開手順に準拠し、Azure PortalやCLIで新SKUを指定するだけで利用可能です。活用例としては、金融・医療分野での機密データ解析やマルチテナント環境での安全なコード実行が挙げられます。注意点として、旧SKUは廃止に伴いサポート終了が予定されており、移行計画が必要です。また、DCesv6/ECesv6は対応リージョンが限定されるため事前確認が必須です。Azure Key Vaultとの連携により、機密鍵の安全管理とTEE内でのシームレスな暗号処理が可能であり、Azure Attestationサービスを用いた信頼性検証も強化されています。これにより、クラウド上での高度なセキュリティ要件を満たす機密コンピューティング環境を構築できます。

---

### 2. Retirement: Azure CDN – Migrate to Azure Front Door on December 1, 2025 

**公開日時**: 2025年09月02日 18:00:44 UTC
**リンク**: [Retirement: Azure CDN – Migrate to Azure Front Door on December 1, 2025 ](https://azure.microsoft.com/updates?id=501174)

**アップデートID**: 501174
**情報源**: Azure Updates API

**カテゴリ**: Networking, Security, Azure Front Door, Retirements

**要約**:

- 何が更新されたか  
Azure Chinaで提供されているAzure CDNサービスが2025年12月1日に廃止されます。  

- 主な変更点や新機能  
Azure CDNはローカルCDNプロバイダーのPOP上に構築されていますが、今後はAzure Front Doorへの移行が推奨されます。  

- 影響を受ける対象  
Azure ChinaでAzure CDNを利用中の全顧客が対象です。  

- 注意点  
廃止日までにAzure Front Doorへの移行計画を立て、サービス停止を回避してください。  

情報源: https://azure.microsoft.com/updates?id=501174

**詳細**:

本アップデートは、Microsoft Azureが中国市場向けに提供しているAzure CDN（21Vianet運営版）を2025年12月1日付で廃止し、代替としてAzure Front Doorへの移行を促すものです。背景には、より高度なセキュリティ機能やグローバルなパフォーマンス最適化を実現するため、Azure Front Doorの利用促進があります。Azure CDNは中国国内のローカルCDNプロバイダーのPOPを活用して配信していましたが、Azure Front DoorはエッジルーティングやWAF、TLS終端などの機能を統合し、より柔軟かつ安全なコンテンツ配信を可能にします。移行にあたっては、既存のCDNエンドポイント設定をAzure Front Doorのフロントエンドホストやバックエンドプールに置き換え、ルーティングルールやキャッシュ設定を再構築する必要があります。活用シナリオとしては、Webアプリケーションの高速化、DDoS対策強化、グローバル負荷分散などが挙げられます。注意点として、中国特有のネットワーク規制や21Vianet運営環境固有の制約があるため、移行前に詳細な検証とテストが必須です。また、Azure Front DoorはAzure MonitorやAzure Security Centerと連携し、運用監視やセキュリティ管理が強化可能です。移行計画は早期に策定し、2025年末までの完全移行を推奨します。

---

### 3. Generally Available: Playwright Workspaces in Azure App Testing

**公開日時**: 2025年09月02日 17:00:13 UTC
**リンク**: [Generally Available: Playwright Workspaces in Azure App Testing](https://azure.microsoft.com/updates?id=501953)

**アップデートID**: 501953
**情報源**: Azure Updates API

**カテゴリ**: Launched, Developer tools, DevOps, Azure Load Testing, Features

**要約**:

- 何が更新されたか  
Azure App TestingのPlaywright Workspaces機能が一般提供（GA）となりました。

- 主な変更点や新機能  
複数ブラウザ・デバイスでの高並列エンドツーエンドテストが可能になり、アプリの機能検証が効率化されます。

- 影響を受ける対象  
Azure上でのアプリケーションテストを行う開発者・テストエンジニア。

- 注意点があれば記載  
既存のPlaywrightテスト環境との統合や並列実行時のリソース管理に注意が必要です。

**詳細**:

Azure App TestingにおけるPlaywright Workspaces機能がGA（一般提供）となりました。本機能は、Playwrightを用いたエンドツーエンドテストの大規模並列実行を可能にし、多様なブラウザやデバイス環境でのアプリケーション検証を効率化します。具体的には、複数のテストスイートを同時に実行し、クロスブラウザテストを自動化。Azure App Testingのクラウド基盤を活用し、スケーラブルかつ高速にテストを完了させる設計です。実装は、PlaywrightのテストコードをAzureにデプロイし、Workspaces上で管理。CI/CDパイプラインと連携することで、継続的テストの自動化が容易になります。活用例としては、Webアプリの多環境対応検証やリリース前の回帰テストが挙げられます。注意点として、テスト実行時のリソース制限やブラウザバージョンのサポート範囲を確認する必要があります。また、Azure DevOpsやGitHub Actionsとの連携により、テスト結果の可視化や通知機能を活用可能です。これにより、品質保証プロセスの効率化と信頼性向上が期待されます。

---

### 4. Generally Available: Azure Ultra Disk Price Reduction in UK South

**公開日時**: 2025年09月02日 17:00:13 UTC
**リンク**: [Generally Available: Azure Ultra Disk Price Reduction in UK South](https://azure.microsoft.com/updates?id=499411)

**アップデートID**: 499411
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Disk Storage, Features, Pricing & Offerings

**要約**:

- 何が更新されたか  
Azure Ultra Diskの価格がUK Southリージョンで値下げされました。

- 主な変更点や新機能  
Ultra Diskはサブミリ秒の低レイテンシと高性能を持つブロックストレージで、コスト削減によりより利用しやすくなりました。

- 影響を受ける対象  
UK SouthリージョンでUltra Diskを利用するAzure VMユーザー。

- 注意点があれば記載  
価格変更はUK South限定のため、他リージョンの価格は影響ありません。性能要件に応じてコスト最適化を検討してください。

**詳細**:

本アップデートは、Azure Ultra DiskのUK Southリージョンにおける価格削減を正式リリースしたものです。Ultra Diskは、サブミリ秒の一貫した低レイテンシと高IOPSを実現する高性能ブロックストレージで、ミッションクリティカルなエンタープライズアプリケーション向けに最適化されています。今回の価格改定により、コスト効率が向上し、より多くのワークロードでの採用が促進されます。技術的には、Ultra Diskは動的にIOPSとスループットを調整可能で、VMのパフォーマンス要件に応じて柔軟に設定可能です。活用シナリオとしては、トランザクション処理システム、リアルタイム分析、データベースサーバーなど高頻度アクセスが求められる環境が挙げられます。注意点として、Ultra Diskは特定のVMシリーズのみ対応し、リージョンによって提供状況が異なるため事前確認が必要です。また、スナップショットやバックアップは別途管理が必要です。Azure VM、Azure Backup、Azure Monitorとの連携により、パフォーマンス監視やデータ保護が容易になります。今回の価格改定は、UK SouthリージョンでのUltra Disk利用のコストパフォーマンスを大幅に改善し、高性能ストレージの導入障壁を下げる重要なアップデートです。

---

### 5. Generally Available: Azure Ultra Disk Price Reduction in Central US

**公開日時**: 2025年09月02日 17:00:13 UTC
**リンク**: [Generally Available: Azure Ultra Disk Price Reduction in Central US](https://azure.microsoft.com/updates?id=499406)

**アップデートID**: 499406
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Disk Storage, Features, Pricing & Offerings

**要約**:

- 何が更新されたか  
Central USリージョンでAzure Ultra Diskの価格が引き下げられ、一般提供（GA）となりました。  

- 主な変更点や新機能  
Ultra Diskはサブミリ秒の低レイテンシと高性能を持つブロックストレージで、価格が下がることでコスト効率が向上しました。  

- 影響を受ける対象  
高性能ストレージを必要とするAzure VMユーザー、特にエンタープライズ向けのワークロード。  

- 注意点があれば記載  
価格変更はCentral USリージョン限定のため、他リージョンの利用者は影響なし。性能要件に応じて選択を検討してください。

**詳細**:

本アップデートは、Azure Ultra DiskのCentral USリージョンにおける価格改定を通じて、コスト効率の向上を目的としています。Ultra Diskは、サブミリ秒の一貫した低レイテンシと高IOPSを実現するブロックストレージであり、ミッションクリティカルなエンタープライズアプリケーションに最適です。今回の価格引き下げにより、高性能ストレージをより経済的に利用可能となりました。技術的には、Ultra Diskは動的にパフォーマンスを調整可能で、VMのワークロードに応じてIOPSやスループットを柔軟に設定可能です。活用例としては、大規模データベースやトランザクション処理、高頻度の読み書きを要する分析ワークロードが挙げられます。注意点として、Ultra DiskはCentral USリージョン限定の価格改定であり、リージョン間の価格差に留意が必要です。また、VMサイズやOSによっては利用制限があるため、事前に対応状況を確認することが推奨されます。Azure VMやAzure Backup、Azure Site Recoveryとの連携により、高可用性やデータ保護を強化可能です。詳細は公式アップデートページ（https://azure.microsoft.com/updates?id=499406）を参照してください。

---

### 6. Generally Available: Azure Ultra Disk Price Reduction in West US 2

**公開日時**: 2025年09月02日 17:00:13 UTC
**リンク**: [Generally Available: Azure Ultra Disk Price Reduction in West US 2](https://azure.microsoft.com/updates?id=499401)

**アップデートID**: 499401
**情報源**: Azure Updates API

**カテゴリ**: Launched, Storage, Azure Disk Storage, Pricing & Offerings, Features

**要約**:

- 何が更新されたか  
Azure Ultra Diskの価格がWest US 2リージョンで正式に値下げされました。

- 主な変更点や新機能  
Ultra Diskはサブミリ秒の低レイテンシと高性能を持つブロックストレージで、コスト削減によりより利用しやすくなりました。

- 影響を受ける対象  
West US 2リージョンでUltra Diskを利用している、または検討しているAzure VMユーザー。

- 注意点があれば記載  
価格変更はWest US 2限定のため、他リージョンの価格は影響ありません。性能要件に応じてコスト最適化を検討してください。

**詳細**:

本アップデートは、Azure Ultra DiskのWest US 2リージョンにおける価格削減を正式リリースしたものです。Ultra Diskは、サブミリ秒の一貫した低レイテンシと高IOPSを実現するAzureの最高性能ブロックストレージであり、ミッションクリティカルなエンタープライズアプリケーション向けに最適化されています。今回の価格改定により、コスト効率が向上し、より幅広いワークロードでの採用が促進されます。Ultra Diskは動的にIOPSとスループットを調整可能で、VMのパフォーマンス要件に柔軟に対応可能です。実装はAzureポータルやCLI、ARMテンプレートで設定可能で、VMのOSディスクやデータディスクとして利用できます。主な活用シナリオは、大規模データベース、高頻度トランザクション処理、リアルタイム分析など高性能ストレージを必要とする環境です。注意点として、Ultra Diskは現在一部リージョン限定で提供され、スナップショットやバックアップの対応状況を確認する必要があります。Azure VM、Azure Backup、Azure Monitorとの連携により、運用管理やパフォーマンス監視が容易になります。今回の価格改定はWest US 2リージョン限定のため、他リージョン利用時は価格差に留意してください。

---


*このレポートは自動生成されました - 2025-09-03 12:01:46 JST*