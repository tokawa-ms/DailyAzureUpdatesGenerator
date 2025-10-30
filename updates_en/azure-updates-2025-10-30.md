# October 30, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 30, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Retirement: Remove dependency on these preview features before March 31, 2026 

**Published**: October 29, 2025 21:00:13 UTC
**Link**: [Retirement: Remove dependency on these preview features before March 31, 2026 ](https://azure.microsoft.com/updates?id=501663)

**Update ID**: 501663
**Data source**: Azure Updates API

**Categories**: AI + machine learning, Internet of Things, Azure Machine Learning, Retirements, Features

**Summary**:

- What was updated  
Microsoft announced the retirement of several Azure preview features effective March 31, 2026.

- Key changes or new features  
The following preview capabilities will be deprecated and no longer supported after the retirement date:  
• Grouping multiple pipeline steps as a single unit for better organization of complex pipelines  
• Comparing pipeline jobs to troubleshoot failures or unexpected behavior  
• Importing data into data labeling projects  
• Using v2 data versions  

- Target audience affected  
Developers and IT professionals who utilize Azure Pipelines for CI/CD workflows, data scientists and engineers working with Azure data labeling projects, and teams leveraging preview data features need to plan for this change.

- Important notes if any  
Users must remove dependencies on these preview features before March 31, 2026, to avoid disruption. It is recommended to transition to supported alternatives or stable feature releases well in advance. Review existing pipelines and data labeling workflows to identify usage of these features and update accordingly. No direct replacements were specified, so monitoring Azure updates for successor features is advised.

**Details**:

The Azure update titled "Retirement: Remove dependency on these preview features before March 31, 2026" announces the planned deprecation of several preview capabilities within Azure Machine Learning and related services, effective March 31, 2026. This advance notice serves to guide IT professionals and developers to transition away from these features to ensure uninterrupted workflows and compatibility with supported Azure offerings.

**Background and Purpose of the Update**  
Azure periodically introduces preview features to gather user feedback and validate new capabilities before general availability. The features listed in this update—grouping multiple pipeline steps, pipeline job comparison, data import into data labeling projects, and use of v2 data—were provided as previews to enhance pipeline management and data labeling workflows. The retirement notice signals that these preview features will no longer be supported or available after March 31, 2026, encouraging users to migrate to stable, fully supported alternatives. This helps Microsoft streamline the platform, improve reliability, and focus development efforts on mature features.

**Specific Features and Detailed Changes**  
1. **Group multiple steps as a whole to better organize complex pipelines:** This preview allowed users to encapsulate multiple pipeline steps into a single grouped entity for better organization and readability in complex ML pipelines.  
2. **Compare pipeline jobs to debug failures or unexpected issues:** This feature enabled side-by-side comparison of pipeline job runs to facilitate troubleshooting by highlighting differences in parameters, outputs, or execution details.  
3. **Import data into a data labeling project:** This preview supported importing external datasets directly into Azure Machine Learning data labeling projects to streamline annotation workflows.  
4. **Use v2 data:** This relates to the use of version 2 data formats or APIs in Azure ML, which may have been experimental or transitional.

Post-retirement, these preview features will be disabled, and users must avoid dependencies on them. Microsoft recommends adopting GA (Generally Available) features or alternative workflows that provide similar or improved functionality.

**Technical Mechanisms and Implementation Methods**  
- The grouping of pipeline steps was implemented as a UI and pipeline DSL (Domain Specific Language) enhancement, allowing nested pipeline constructs.  
- Pipeline job comparison leveraged metadata tracking and UI diff tools to compare job runs.  
- Data import to labeling projects involved connectors and data ingestion APIs integrated with Azure ML data labeling services.  
- The v2 data usage likely involved updated SDK methods and data schema versions.

Users should review their pipeline definitions, SDK usage, and data labeling configurations to identify and refactor any references to these preview features. This may involve rewriting pipeline YAML or Python SDK code, modifying data import scripts, or switching to supported data versioning methods.

**Use Cases and Application Scenarios**  
- Complex ML pipelines in production environments that used step grouping for clarity and modularity will need to reorganize pipelines without this feature.  
- Teams relying on pipeline job comparisons for debugging CI/CD pipelines must adopt alternative logging, monitoring, or manual comparison approaches.  
- Data scientists using data labeling projects with imported datasets must transition to supported data ingestion methods to maintain annotation workflows.  
- Projects using v2 data APIs or formats should migrate to the latest stable data handling mechanisms to ensure compatibility.

**Important Considerations and Limitations**  
- The retirement date is over two years away, providing ample time for migration planning and testing.  
- Preview features are inherently subject to change or removal; reliance on them in production is discouraged.  
- Users should audit existing pipelines and labeling projects to detect usage of these features.  
- Lack of direct 1:1 replacements for some preview features may require redesigning workflows or adopting third-party tools.  
- Documentation and SDK updates from Microsoft will provide guidance on migration paths.

**Integration with Related Azure Services**  
- Azure Machine Learning pipelines integrate with Azure DevOps, GitHub Actions, and Azure Data Factory; changes in pipeline step grouping and job comparison may affect CI/CD and orchestration workflows.  
- Data labeling projects are part of Azure ML’s data preparation

---


*This report was automatically generated - 2025-10-30 03:01:20 UTC*