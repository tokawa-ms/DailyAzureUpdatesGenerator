# August 19, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 19, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Generally Available: Azure Blob Storage Archive Tier Now in Malaysia West

**Published**: August 18, 2025 15:00:19 UTC
**Link**: [Generally Available: Azure Blob Storage Archive Tier Now in Malaysia West](https://azure.microsoft.com/updates?id=500630)

**Update ID**: 500630
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Archive Storage, Azure Blob Storage, Storage Accounts, Features, Services

**Summary**:

- What was updated  
The Azure Blob Storage Archive access tier is now generally available in the Malaysia West region.

- Key changes or new features  
Customers in Malaysia West can now leverage the Archive tier to store infrequently accessed data at a lower cost. This expansion enables local data residency compliance while optimizing storage expenses for long-term retention and archival scenarios.

- Target audience affected  
Developers and IT professionals managing data storage and compliance in Malaysia, especially those handling large volumes of infrequently accessed or archival data.

- Important notes if any  
Using the Archive tier requires understanding of retrieval latency and costs, as data retrieval from Archive can take hours. Ensure applications and workflows accommodate these access patterns. This update enhances regional availability, reducing latency and improving compliance with local data residency requirements.

**Details**:

The Azure update announces the general availability of the Azure Blob Storage Archive access tier in the Malaysia West region, enabling customers in that geography to leverage the cost-effective, long-term storage option for infrequently accessed data while ensuring data residency compliance.

**Background and Purpose**  
Azure Blob Storage offers multiple access tiers—Hot, Cool, and Archive—to optimize storage costs based on data access patterns. The Archive tier is designed for data that is rarely accessed and can tolerate retrieval latency, providing the lowest storage cost. Previously, the Archive tier was not available in all Azure regions, limiting customers’ ability to store archival data locally. This update expands the Archive tier availability to Malaysia West, addressing regional data residency requirements and reducing latency for local customers, while enabling cost savings on long-term storage.

**Specific Features and Detailed Changes**  
- **Archive Tier Availability:** Customers can now set blobs to the Archive tier in Malaysia West, allowing them to store data at the lowest cost tier within that region.  
- **Seamless Tiering:** Blobs can be transitioned between Hot, Cool, and Archive tiers programmatically or via lifecycle management policies.  
- **Data Residency:** Data stored in the Archive tier remains within Malaysia West, supporting compliance with local regulations.  
- **General Availability (GA):** The feature is fully supported with SLA and production-grade reliability.

**Technical Mechanisms and Implementation Methods**  
- **Blob Tiering:** Using Azure Storage REST APIs, SDKs, or Azure Portal, users can set the access tier of a blob to Archive. This action changes the blob’s storage state but does not delete or move the data physically; instead, it changes the billing and access characteristics.  
- **Data Retrieval:** Retrieving data from the Archive tier requires rehydration, which can take several hours (typically 6-12 hours) because the data is stored offline on lower-cost media. Rehydration is initiated by changing the blob’s tier back to Hot or Cool.  
- **Lifecycle Management:** Azure Blob Storage lifecycle management policies can automate tier transitions based on rules such as last modified date or access patterns, enabling automated archival of cold data.  
- **Access Protocols:** Archive tier blobs support all standard Blob Storage protocols (REST, NFS, SMB via Azure Files Sync for certain scenarios), but direct read access is not possible without rehydration.

**Use Cases and Application Scenarios**  
- **Regulatory Compliance:** Organizations in Malaysia requiring data to remain within national boundaries can archive data locally.  
- **Cost Optimization:** Enterprises with large volumes of infrequently accessed data (e.g., backups, logs, compliance records) can reduce storage costs by archiving data in-region.  
- **Disaster Recovery and Backup:** Archive tier can serve as a long-term retention layer for backup data that is rarely accessed but must be retained for compliance or recovery.  
- **Media and Content Archiving:** Media companies can archive raw footage or completed projects that need to be preserved but not accessed frequently.

**Important Considerations and Limitations**  
- **Rehydration Latency:** Data retrieval from Archive tier is not instantaneous; planning for retrieval delays is essential.  
- **Data Immutability:** While blobs in Archive tier can be deleted or tier-changed, Azure Blob Storage supports immutable storage policies which can be combined with tiering for compliance.  
- **Cost Implications:** While storage costs are lowest in Archive, retrieval and early deletion fees may apply.  
- **API and SDK Support:** Ensure applications use the latest Azure Storage SDKs that support tiering operations in the Malaysia West region.  
- **Availability Zones:** Verify if Malaysia West supports zone-redundant storage (ZRS) for Archive tier blobs if higher durability is required.

**Integration with Related Azure Services**  
- **Azure Data Factory:** Can orchestrate data movement and tiering as part of ETL workflows.  
- **Azure Backup:** May leverage Blob Storage Archive tier for

---


*This report was automatically generated - 2025-08-19 03:01:13 UTC*