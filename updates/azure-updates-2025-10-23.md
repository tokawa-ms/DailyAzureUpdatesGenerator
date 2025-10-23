# 2025年10月23日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2025年10月23日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 3 件

## 更新一覧

### 1. Public Preview: VM vCore customization features disabling simultaneous multi-threading (SMT/HT) and constrained cores

**公開日時**: 2025年10月22日 17:15:22 UTC
**リンク**: [Public Preview: VM vCore customization features disabling simultaneous multi-threading (SMT/HT) and constrained cores](https://azure.microsoft.com/updates?id=516990)

**アップデートID**: 516990
**情報源**: Azure Updates API

**カテゴリ**: In preview, Features

**要約**:

- 何が更新されたか  
Azure VMのvCoreカスタマイズ機能がパブリックプレビューで提供開始。

- 主な変更点や新機能  
同時マルチスレッディング（SMT/HT）無効化とコア数制限の設定が可能に。性能最適化やライセンスコスト削減に寄与。

- 影響を受ける対象  
仮想マシンのCPU構成を細かく制御したいエンタープライズユーザーや開発者。

- 注意点があれば記載  
プレビュー機能のため本番環境利用は慎重に。対応VMサイズやリージョンを確認のこと。

**詳細**:

本アップデートは、Azure仮想マシン（VM）におけるvCoreカスタマイズ機能のパブリックプレビュー開始を告知するもので、仮想CPU構成の柔軟な制御を可能にし、性能最適化とライセンスコスト削減を目的としています。主な新機能は「同時マルチスレッディング（SMT/HT）の無効化」と「制約コア（constrained cores）」の設定です。SMT無効化により、物理コア単位でのCPU割当てが可能となり、特定のワークロードでの性能安定化やセキュリティ強化に寄与します。制約コア機能は、VMに割り当てるvCore数を物理コア数より少なく制限し、ライセンスコストを抑制しつつ必要な性能を確保する用途に適しています。実装はAzure CLIやARMテンプレートでのvCPU設定パラメータ追加により行い、既存VMの再作成やサイズ変更時に適用可能です。活用例としては、SQL Serverなどコアライセンス課金が発生するDBサーバーでのコスト最適化や、セキュリティ要件の高い環境でのSMT無効化が挙げられます。制限事項として、対応VMシリーズが限定的であり、SMT無効化は一部のハードウェアでのみサポートされる点に注意が必要です。また、Azure MonitorやAzure Policyと連携し、カスタマイズ設定の監視・管理が可能です。これにより、パフォーマンス要件とコスト効率のバランスを高度に調整できる新たなVM運用が実現します。

---

### 2. Generally Available: Azure SQL updates for mid-October 2025   

**公開日時**: 2025年10月22日 16:30:07 UTC
**リンク**: [Generally Available: Azure SQL updates for mid-October 2025   ](https://azure.microsoft.com/updates?id=513240)

**アップデートID**: 513240
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance, Features

**要約**:

- 何が更新されたか  
Azure SQLのリダイレクト接続方式の改善と、Azure SQL DatabaseのHyperscaleへの変換機能追加。

- 主な変更点や新機能  
リダイレクト接続がポート1433のみで動作するようになり、これがデフォルトに。既存のジオレプリケーションを維持したまま、Azure SQL DatabaseをHyperscaleへ変換可能に。

- 影響を受ける対象  
Azure SQL Database利用者、特にネットワーク設定やスケールアップを検討している技術者。

- 注意点  
リダイレクト接続のポート制限により、ファイアウォール設定の見直しが必要。Hyperscale変換は既存のジオレプリケーション環境での動作確認を推奨。

**詳細**:

2025年10月中旬にAzure SQLに実施されたアップデートでは、主に接続方式の改善とデータベースのスケールアップ機能が強化されました。まず、リダイレクト接続タイプが改良され、従来複数ポートを必要としていた接続がポート1433のみで完結可能となり、これをデフォルト設定に昇格させました。これによりファイアウォール設定の簡素化と接続安定性の向上が実現します。技術的には、クライアント接続時のトラフィックが単一ポートに集約され、ネットワーク構成の複雑さを軽減します。次に、既存のAzure SQL Databaseを地理的冗長性を維持したままHyperscaleへ変換可能となり、大規模データのスケーラビリティとパフォーマンスを向上させます。変換はAzureポータルやPowerShell、CLIから実行可能で、ダウンタイムを最小限に抑えつつスムーズに移行可能です。活用例としては、グローバル展開するアプリケーションのデータベース負荷分散や大容量データ処理に最適です。注意点として、Hyperscale変換時は一部の機能制限や互換性確認が必要であり、事前検証が推奨されます。また、Azure SQL Managed InstanceやAzure Arcとの連携により、ハイブリッド環境での一貫した管理が可能です。詳細は公式ドキュメント（https://azure.microsoft.com/updates?id=513240）を参照してください。

---

### 3. Generally Available: Near-zero downtime scaling for HA-enabled Azure Database for PostgreSQL servers 

**公開日時**: 2025年10月22日 16:00:32 UTC
**リンク**: [Generally Available: Near-zero downtime scaling for HA-enabled Azure Database for PostgreSQL servers ](https://azure.microsoft.com/updates?id=502004)

**アップデートID**: 502004
**情報源**: Azure Updates API

**カテゴリ**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**要約**:

- 何が更新されたか  
HA対応のAzure Database for PostgreSQLサーバーで、ほぼダウンタイムなしのスケーリングが一般提供開始。

- 主な変更点や新機能  
スケーリング時間が従来の2～10分から30秒未満に大幅短縮され、ユーザー影響を最小化。

- 影響を受ける対象  
高可用性構成のAzure Database for PostgreSQLを利用する技術者や運用チーム。

- 注意点があれば記載  
従来のスケーリング方法と比較し、HA構成でのみ適用可能な点に注意。

**詳細**:

本アップデートは、高可用性（HA）構成のAzure Database for PostgreSQLサーバーにおけるスケーリング時のダウンタイムを従来の数分から30秒未満へ大幅に短縮することを目的としています。これにより、業務継続性を維持しつつリソース調整が可能となります。具体的には、プライマリとレプリカ間の同期処理を最適化し、スケール操作中のフェイルオーバー時間を短縮する仕組みを導入しました。実装は、HA構成のレプリケーションとフェイルオーバー制御を高度に連携させることで実現しています。活用シナリオとしては、トラフィック急増時のCPUやメモリ増強、メンテナンス時のリソース調整が挙げられます。注意点として、スケール操作中に一時的な接続遅延や再接続が発生する可能性があり、アプリケーション側でのリトライ対応が推奨されます。また、シングルインスタンス構成や非HA構成では本機能は適用されません。Azure MonitorやAzure Automationと連携することで、スケールイベントの監視・自動化が可能です。詳細は公式ドキュメントを参照してください。

---


*このレポートは自動生成されました - 2025-10-23 12:01:41 JST*