# 2026年04月28日 - Azure Updates 要約レポート (詳細モード)

**生成日時**: 2026年04月28日
**対象期間**: 過去 24 時間以内
**処理モード**: 詳細モード
**更新件数**: 2 件

## 更新一覧

### 1. Generally Available: Bring your own AI Gateway in Foundry Agent Service 

**公開日時**: 2026年04月27日 18:00:52 UTC
**リンク**: [Generally Available: Bring your own AI Gateway in Foundry Agent Service ](https://azure.microsoft.com/updates?id=561002)

**アップデートID**: 561002
**情報源**: Azure Updates API

**カテゴリ**: Launched, AI + machine learning, Microsoft Foundry, Features

**要約**:

【Azure Update要約】

■何が更新されたか  
Foundry Agent Serviceが「Bring Your Own AI Gateway」機能の一般提供（GA）を開始しました。

■主な変更点や新機能  
これにより、Foundry Agent Serviceは外部でデプロイ・管理されているAIモデルを利用できるようになりました。具体的には、Azure API ManagementなどのエンタープライズAIゲートウェイ経由でホストされているモデルをエージェントが呼び出せます。これにより、Foundry外部の独自AIモデルや既存のAIサービスを柔軟に統合可能です。

■影響を受ける対象  
Foundry Agent Serviceを利用している組織や開発者が対象です。特に、独自のAIモデルや社内AIゲートウェイを運用している企業にとって、既存資産の活用やセキュリティ管理が容易になります。

■注意点  
外部AIモデルの統合時には、API管理や認証、セキュリティ設定などの運用面に注意が必要です。また、モデルのパフォーマンスや可用性は、Foundry外部の環境に依存します。

**詳細**:

本アップデートは、Foundry Agent Serviceにおいて「Bring your own AI Gateway」機能が一般提供（GA）となったことを示しています。これにより、Foundry外部でデプロイおよび管理されているAIモデルを、Foundry Agent Serviceのエージェントが利用できるようになりました。特に、Azure API ManagementなどのエンタープライズAIゲートウェイの背後にホストされているモデルも対象となります。

この機能追加の背景には、企業が独自に管理するAIモデルや、セキュリティやガバナンス要件により外部公開できないAIサービスを活用したいというニーズがあります。従来、Foundry Agent ServiceはFoundry内で管理されているAIモデルに限定してエージェントの構築や運用が可能でしたが、今回のアップデートにより、既存のエンタープライズAIインフラストラクチャを活かしつつ、Foundryエージェントの機能拡張が実現します。

技術的には、Foundry Agent Serviceが外部AIモデルへのアクセスをサポートすることで、エージェントがAzure API Managementなどのゲートウェイ経由でAI推論リクエストを送信し、レスポンスを受け取ることが可能となります。これにより、企業は自社のAPI管理ポリシーや認証・認可機構を維持しつつ、Foundryエージェントサービスの自動化やインテリジェンス機能を利用できます。実装においては、エージェント構成時に外部AIモデルのエンドポイント情報や認証情報を指定することで、Foundryから透過的に外部AIサービスを呼び出せるようになります。

活用シナリオとしては、企業が独自にトレーニングしたAIモデルや、社内規定によりクラウド外部に公開できないAIサービスをFoundryエージェントに組み込む場合が想定されます。たとえば、社内の機密データを用いた自然言語処理モデルや、独自の画像認識モデルなどを、Azure API ManagementでAPI化し、Foundryエージェントサービスから利用することが可能です。

注意点としては、外部AIモデルの可用性やパフォーマンス、セキュリティ設定はFoundryの管理外となるため、十分な監視や運用設計が必要です。また、APIゲートウェイの認証方式やスロットリング設定など、既存のエンタープライズAPI管理ポリシーに準拠する必要があります。

関連するAzureサービスとしては、Azure API Managementが代表的ですが、他のAPIゲートウェイや外部AIモデルホスティングサービスとも連携可能です。これにより、Azure上の既存AI資産を最大限に活用しつつ、Foundryエージェントサービスの柔軟な拡張が実現します。

---

### 2. Retirement: Prompt Flow in Azure ML and Foundry

**公開日時**: 2026年04月27日 16:15:55 UTC
**リンク**: [Retirement: Prompt Flow in Azure ML and Foundry](https://azure.microsoft.com/updates?id=502936)

**アップデートID**: 502936
**情報源**: Azure Updates API

**カテゴリ**: Retirements

**要約**:

【何が更新されたか】  
Azure Machine LearningおよびMicrosoft Foundryで提供されているPrompt Flowが、2027年4月20日に廃止されることが発表されました。

【主な変更点や新機能】  
Prompt Flowの廃止後は、Microsoft Agent Frameworkという新しいオーケストレーションプラットフォームに統合されます。これにより、より現代的で統一された開発環境が提供され、将来の機能拡張や運用の効率化が期待できます。

【影響を受ける対象】  
Azure Machine LearningやFoundry上でPrompt Flowを利用している技術者や開発者が対象となります。既存のPrompt Flowワークフローやプロジェクトは、今後Microsoft Agent Frameworkへの移行が必要になります。

【注意点】  
Prompt Flowのサポートは2027年4月20日までとなるため、それ以降は新規作成や保守ができなくなります。早めにMicrosoft Agent Frameworkへの移行計画を立てることを推奨します。移行方法や詳細は今後公式ドキュメント等で案内される予定です。

**詳細**:

2027年4月20日をもって、Microsoft FoundryおよびAzure Machine LearningにおけるPrompt Flowの提供が終了し、これに代わりMicrosoft Agent Frameworkが導入されます。本アップデートの背景には、複数のオーケストレーションプラットフォームを統合し、よりモダンで拡張性の高い環境を提供するという目的があります。これにより、従来Prompt Flowで実現されていた機能やワークフローは、Microsoft Agent Frameworkに一本化され、将来的な拡張性や一貫したユーザー体験が期待できます。

具体的な変更内容としては、Prompt Flowの機能が廃止され、今後はMicrosoft Agent Frameworkを利用する必要がある点が挙げられます。Prompt Flowは、主に機械学習モデルのプロンプト設計やフロー管理を支援する機能を提供していましたが、これらの機能は新しいフレームワークに統合されます。これにより、ユーザーは複数のツールを使い分ける必要がなくなり、統一されたオーケストレーション基盤上での開発・運用が可能となります。

技術的な仕組みや実装方法については、詳細な情報は提供されていませんが、今後はMicrosoft Agent Frameworkを中心としたオーケストレーションが求められるため、既存のPrompt Flowで構築されたワークフローやプロジェクトは、移行計画を立てる必要があります。移行にあたっては、Microsoftが提供するドキュメントやサポート情報を参照し、計画的に作業を進めることが重要です。

活用シナリオとしては、これまでPrompt Flowを利用していた機械学習モデルのプロンプト設計やワークフロー自動化、パイプライン管理などの用途が、今後はMicrosoft Agent Frameworkを通じて実現されることになります。これにより、より一貫性のある開発・運用プロセスが期待できます。

注意点として、Prompt Flowは2027年4月20日以降利用できなくなるため、それまでにすべてのワークフローやプロジェクトを新しいフレームワークに移行する必要があります。また、移行作業に伴う互換性や機能差分については、事前に十分な検証と準備が求められます。

関連するAzureサービスとの連携については、Azure Machine LearningやFoundryとの統合が引き続き提供される見込みですが、今後はMicrosoft Agent Frameworkを介した連携が中心となります。これにより、Azure上での機械学習やAIワークフローの構築・運用が、より効率的かつ統合的に行えるようになります。

---


*このレポートは自動生成されました - 2026-04-28 12:00:48 JST*