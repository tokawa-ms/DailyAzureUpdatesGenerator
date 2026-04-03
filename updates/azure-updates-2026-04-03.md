# 2026年04月03日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年04月03日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Retirement: Python support for Azure App Service and Azure Functions on Windows will be retired on March 31, 2027 

**公開日時**: 2026年04月02日 16:45:52 UTC
**リンク**: [Retirement: Python support for Azure App Service and Azure Functions on Windows will be retired on March 31, 2027 ](https://azure.microsoft.com/updates?id=558027)

**アップデートID**: 558027
**情報源**: Azure Updates API

**カテゴリ**: Compute, Mobile, Web, App Service, Retirements

**要約**:

- 何が更新されたか  
Azure App ServiceおよびAzure Functions（いずれもWindows環境）におけるPythonサポートが、2027年3月31日をもって廃止されることが発表されました。

- 主な変更点や新機能  
2027年3月31日以降、Windows上で動作するAzure App ServiceおよびAzure FunctionsでのPythonアプリケーションは実行できなくなります。アプリケーションの構成やコンテンツ自体は保持されますが、アプリは稼働しなくなります。

- 影響を受ける対象  
WindowsベースのAzure App ServiceおよびAzure FunctionsでPythonを利用している全てのアプリケーションが対象です。Linuxベースのサービスや他の言語には影響はありません。

- 注意点があれば記載  
該当するPythonアプリケーションを運用している場合は、2027年3月31日までにLinuxベースのApp ServiceやFunctionsへの移行、または他の対応策を検討する必要があります。移行作業には十分な準備期間を設けてください。

**詳細**:

本アップデートは、「Azure App Service on Windows」および「Azure Functions on Windows」におけるPythonサポートの提供終了に関するものです。2027年3月31日をもって、これらのサービス上でホストされているPythonアプリケーションは実行できなくなります。この変更の背景には、Azureプラットフォームにおけるサービスの進化や、より最新の技術スタックへの移行促進があると考えられますが、公式には詳細な目的は明示されていません。

具体的な変更内容としては、2027年3月31日以降、WindowsベースのAzure App ServiceおよびAzure Functions上で稼働しているPythonアプリケーションは停止し、実行されなくなります。ただし、アプリケーションの構成やコンテンツ自体は削除されず、そのまま保持されます。つまり、アプリケーションのファイルや設定情報は残りますが、サービスとしての実行はできなくなります。

技術的な仕組みとして、Azure App ServiceおよびAzure Functionsは、Windows環境上でPythonランタイムを提供してきました。これにより、開発者はPythonで記述したWebアプリケーションやサーバーレス関数をWindowsベースのインフラストラクチャ上でデプロイ・実行することが可能でした。しかし、今回のアップデートにより、このWindowsプラットフォーム上でのPythonランタイムのサポートが終了することになります。

活用シナリオとしては、従来、Pythonで開発されたWeb APIやバッチ処理、イベントドリブンな関数アプリケーションなどを、WindowsベースのApp ServiceやFunctionsでホストするケースが多く見られました。今後は、これらのアプリケーションを引き続きAzure上で運用する場合、LinuxベースのApp ServiceやFunctions、あるいは他のAzureサービスへの移行を検討する必要があります。

注意点として、サポート終了後はアプリケーションが自動的に停止し、サービスとしての提供ができなくなるため、事前の移行計画が必須です。また、アプリケーションの構成やデータは残るものの、実行環境が失われるため、業務継続の観点からも早期の対応が求められます。

関連するAzureサービスとしては、LinuxベースのAzure App ServiceやAzure Functionsが挙げられます。これらは引き続きPythonをサポートしており、既存のアプリケーションを比較的容易に移行できる選択肢となります。移行に際しては、OS依存のライブラリや設定の違いに注意し、十分なテストを行うことが推奨されます。

詳細は公式発表ページ（https://azure.microsoft.com/updates?id=558027）を参照してください。

---

### 2. Retirement: AzureDnsEndpoints for Azure storage accounts will be retired March 2027

**公開日時**: 2026年04月02日 16:30:09 UTC
**リンク**: [Retirement: AzureDnsEndpoints for Azure storage accounts will be retired March 2027](https://azure.microsoft.com/updates?id=558276)

**アップデートID**: 558276
**情報源**: Azure Updates API

**カテゴリ**: Storage, Azure Blob Storage, Retirements

**要約**:

- 何が更新されたか  
Azure Blob Storageアカウントで利用されているAzureDnsZoneエンドポイント（プレビュー版）が、2027年3月に廃止されることが発表されました。

- 主な変更点や新機能  
AzureDnsZoneエンドポイント（プレビュー版）の提供が終了し、今後はStandardエンドポイントへの移行が推奨されます。新規および既存のBlob Storageアカウントに対して、Standardエンドポイントの利用が必要となります。

- 影響を受ける対象  
現在AzureDnsZoneエンドポイント（プレビュー版）を利用しているBlob Storageアカウントが対象となります。これらのアカウントは、廃止までにStandardエンドポイントへ移行する必要があります。

- 注意点があれば記載  
2027年3月以降、AzureDnsZoneエンドポイント（プレビュー版）は利用できなくなるため、早めにStandardエンドポイントへの移行計画を立ててください。移行に伴う設定変更やアプリケーション側の対応が必要となる場合がありますので、事前に影響範囲を確認してください。

**詳細**:

Azureは、Azure Blob Storageアカウント向けに提供されているAzureDnsZoneエンドポイント（プレビュー機能）を2027年3月に廃止することを発表しました。このアップデートの背景には、より標準化されたエンドポイント運用への移行と、プレビュー機能の正式サポート終了があります。AzureDnsZoneエンドポイントは、Blob Storageアカウントに対してカスタムDNSゾーンを利用したアクセスを可能にする機能であり、特定のネットワーク構成や名前解決要件に対応するために利用されてきました。

今回の変更により、現在AzureDnsZoneエンドポイント（プレビュー）を利用しているユーザーは、今後すべての新規および既存のBlob Storageアカウントに対して、標準エンドポイントへの移行が求められます。標準エンドポイントは、Azure Storageアカウントがデフォルトで提供する「<accountname>.blob.core.windows.net」形式のエンドポイントであり、Microsoftが公式にサポートする安定したアクセス方法です。これにより、今後は標準エンドポイントを利用した運用が推奨され、AzureDnsZoneエンドポイントの新規作成や既存利用はサポート対象外となります。

技術的な仕組みとして、AzureDnsZoneエンドポイントはカスタムDNSゾーンをAzure DNSで管理し、Blob Storageへのアクセスを独自のドメイン名で提供するものです。これに対し、標準エンドポイントはAzureが提供するグローバルDNSインフラストラクチャを利用し、可用性やセキュリティ、パフォーマンス面で最適化されています。移行に際しては、既存のアプリケーションやサービスが標準エンドポイントを参照するように設定変更が必要となります。

活用シナリオとしては、従来AzureDnsZoneエンドポイントを利用していた環境では、ネットワーク分離や独自の名前解決要件が存在したケースが多いですが、今後はこれらの要件を標準エンドポイントで満たす必要があります。たとえば、仮想ネットワークサービスエンドポイントやプライベートエンドポイントと組み合わせて、セキュアなアクセスを実現することが推奨されます。

注意点として、2027年3月以降はAzureDnsZoneエンドポイント（プレビュー）のサポートが完全に終了するため、移行計画を早期に策定し、アプリケーションや運用プロセスへの影響を最小限に抑えることが重要です。また、関連するAzureサービス、特にAzure DNSや仮想ネットワーク、プライベートリンクなどとの連携についても、標準エンドポイントを前提とした設計への見直しが必要となります。

詳細は公式発表（https://azure.microsoft.com/updates?id=558276）を参照し、最新情報を確認してください。

---


*このレポートは自動生成されました - 2026-04-03 12:01:37 JST*