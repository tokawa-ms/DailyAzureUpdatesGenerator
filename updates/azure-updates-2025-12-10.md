# 2025年12月10日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年12月10日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 1 件

## 更新一覧

### 1. Generally Available: FIPS compliant mode for Application Gateway V2 SKUs 

**公開日時**: 2025年12月09日 13:15:11 UTC
**リンク**: [Generally Available: FIPS compliant mode for Application Gateway V2 SKUs ](https://azure.microsoft.com/updates?id=536712)

**アップデートID**: 536712
**情報源**: Azure Updates API

**カテゴリ**: Launched, Networking, Security, Application Gateway

**要約**:

- 何が更新されたか  
Azure Application Gateway V2 SKUでFIPS 140-2準拠モードが一般提供開始されました。

- 主な変更点や新機能  
暗号モジュールがFIPS 140-2のセキュリティ基準を満たすモードをサポートし、政府機関やセキュリティ要件の厳しい環境での利用が可能に。

- 影響を受ける対象  
高セキュリティ基準を求める政府機関や企業のAzure Application Gateway V2ユーザー。

- 注意点  
FIPSモード有効化により暗号化方式やパフォーマンスに影響が出る可能性があるため、事前検証を推奨。

**詳細**:

本アップデートは、米国政府の暗号モジュール標準であるFIPS 140-2準拠をAzure Application Gateway V2 SKUで正式サポートするものです。FIPS 140-2は暗号化モジュールのセキュリティ要件を定めており、政府機関や金融機関など高セキュリティ環境での利用が求められます。今回の対応により、Application GatewayのTLS通信や暗号処理がFIPS認証済みモジュールを用いて実行され、コンプライアンス要件を満たせます。実装はAzureポータルやARMテンプレートで「FIPSモード」を有効化することで適用可能で、暗号化アルゴリズムや証明書管理はFIPS準拠のものに限定されます。活用例としては、政府系クラウド環境や金融サービスのWebアプリケーションのフロントエンドに配置し、通信の暗号化強化と規制遵守を両立できます。注意点として、FIPSモード有効時は一部非対応の暗号スイートが利用不可となり、パフォーマンスに若干の影響が出る可能性があります。また、Application GatewayとAzure Key Vault連携時もFIPS準拠のキー管理が推奨されます。これにより、Azure全体のセキュリティ基盤と整合した運用が可能となります。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2025-12-10 12:01:06 JST*