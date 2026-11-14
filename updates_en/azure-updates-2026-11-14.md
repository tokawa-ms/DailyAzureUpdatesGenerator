# November 14, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 14, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Retirement: Azure Data Share will be retired on November 12, 2029 

**Published**: November 13, 2026 19:54:45 UTC
**Link**: [Retirement: Azure Data Share will be retired on November 12, 2029 ](https://azure.microsoft.com/updates?id=578818)

**Update ID**: 578818
**Data source**: Azure Updates API

**Categories**: Analytics, Storage, Azure Data Share, Retirements

**Summary**:

- What was updated  
Azure Data Share will be retired on November 12, 2029.

- Key changes or new features  
Azure Data Share, the service for sharing data across Azure tenants and subscriptions, will no longer be available after November 12, 2029. Microsoft recommends transitioning to Microsoft Fabric for data sharing needs. Microsoft Fabric provides features such as External data sharing, Cross-tenant delegated shortcuts, and IQ share. Alternatively, you may use other data-source-specific sharing solutions as appropriate.

- Target audience affected  
Developers and IT professionals currently using Azure Data Share for automated or managed data sharing between Azure tenants, subscriptions, or organizations.

- Important notes if any  
All Azure Data Share workloads must be migrated to Microsoft Fabric or another suitable solution before the retirement date to avoid service disruption. Begin planning your migration strategy well in advance to ensure a smooth transition. Review Microsoft Fabric’s capabilities to determine the best fit for your data sharing scenarios. No new features or updates will be added to Azure Data Share before retirement.  
[More details](https://azure.microsoft.com/updates?id=578818)

**Details**:

**Azure Update Report: Retirement of Azure Data Share on November 12, 2029**

**Background and Purpose of the Update**  
Azure Data Share, a service designed to facilitate secure and scalable data sharing across Azure tenants and subscriptions, will be officially retired on November 12, 2029. This update aims to inform IT professionals and organizations relying on Azure Data Share to begin planning a migration strategy. The retirement is part of Microsoft’s ongoing efforts to consolidate and enhance data sharing capabilities within its ecosystem, specifically by transitioning workloads to Microsoft Fabric.

**Specific Features and Detailed Changes**  
The primary change is the discontinuation of Azure Data Share as a supported service. Users will need to migrate their existing data sharing workloads to Microsoft Fabric, which now offers advanced sharing features such as:
- **External Data Sharing:** Enables secure data exchange across organizational boundaries.
- **Cross Tenant Delegated Shortcuts:** Facilitates seamless access to shared data between Azure tenants.
- **IQ Share:** Provides improved mechanisms for sharing data efficiently and securely.

The update also suggests considering data-source-specific sharing solutions where appropriate, depending on the nature of the data and integration requirements.

**Technical Mechanisms and Implementation Methods**  
Azure Data Share currently utilizes snapshot-based and in-place sharing mechanisms, allowing users to share datasets from Azure storage accounts, data lakes, and other supported sources. With the retirement, these mechanisms will no longer be available. Microsoft Fabric’s data sharing features leverage modern data governance, access control, and integration capabilities, providing enhanced security and scalability. Migration will involve:
- Assessing current Azure Data Share workloads.
- Mapping shared datasets to Microsoft Fabric’s sharing constructs.
- Reconfiguring access policies and permissions within Microsoft Fabric.
- Testing and validating data sharing workflows to ensure continuity.

**Use Cases and Application Scenarios**  
Azure Data Share is commonly used for:
- Sharing data between business units within an organization.
- Exchanging datasets with external partners or customers.
- Enabling cross-tenant analytics and reporting.
Post-retirement, these scenarios should be transitioned to Microsoft Fabric, which supports similar and expanded use cases, including more granular access control and improved cross-tenant collaboration.

**Important Considerations and Limitations**  
- **Timeline:** Azure Data Share will be fully retired on November 12, 2029. After this date, the service will be unavailable, and existing shares will cease to function.
- **Migration Planning:** Organizations must plan and execute migration well before the retirement date to avoid service disruption.
- **Feature Parity:** While Microsoft Fabric offers enhanced sharing features, IT professionals should verify that all required functionalities are supported and test migration thoroughly.
- **Data Governance:** Review and update data governance policies to align with Microsoft Fabric’s mechanisms.

**Integration with Related Azure Services**  
Azure Data Share integrates with Azure Storage, Azure Data Lake, and other data services. Microsoft Fabric is designed to interoperate with these services and provides additional integration points, enabling more robust data sharing and analytics capabilities. IT professionals should review integration requirements and update workflows to leverage Microsoft Fabric’s features.

**Summary Sentence**  
Azure Data Share will be retired on November 12, 2029; organizations should transition their data sharing workloads to Microsoft Fabric, which offers enhanced sharing features and integration options, ensuring continuity and improved data governance.

---


*This report was automatically generated - 2026-11-14 03:01:17 UTC*