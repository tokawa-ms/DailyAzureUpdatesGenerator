# August 23, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 23, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Azure Functions support for Node.js 22

**Published**: August 22, 2025 11:45:29 UTC
**Link**: [Generally Available: Azure Functions support for Node.js 22](https://azure.microsoft.com/updates?id=500438)

**Update ID**: 500438
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features

**Summary**:

- What was updated  
Azure Functions now generally supports Node.js 22 runtime.

- Key changes or new features  
Developers can build and run Azure Functions using Node.js 22 both locally and in the cloud. This support extends across all Azure Functions hosting plans on Linux and Windows environments, enabling access to the latest Node.js features and performance improvements.

- Target audience affected  
Developers building serverless applications with Azure Functions, and IT professionals managing Azure Functions deployments who want to leverage the newest Node.js runtime.

- Important notes if any  
Ensure your function app dependencies and code are compatible with Node.js 22 before upgrading. Testing locally with the updated runtime is recommended to avoid runtime issues. This update aligns Azure Functions with the latest Node.js LTS release, offering improved security and language features.  

Learn more: https://azure.microsoft.com/updates?id=500438

**Details**:

The recent Azure update announces the general availability of Azure Functions support for Node.js 22, enabling developers to build and deploy serverless functions using the latest Node.js runtime across all Azure Functions hosting plans on both Linux and Windows environments. This update reflects Microsoft’s commitment to providing up-to-date runtime support, ensuring developers can leverage the newest language features, performance improvements, and security enhancements inherent in Node.js 22 within their serverless applications.

**Background and Purpose:**  
Azure Functions is a widely used serverless compute service that allows developers to run event-driven code without managing infrastructure. Node.js has been a popular runtime choice due to its asynchronous, event-driven architecture and extensive package ecosystem. Node.js 22, as the latest LTS (Long-Term Support) version, introduces modern JavaScript features, improved diagnostics, and enhanced security. By supporting Node.js 22, Azure Functions ensures developers can utilize the latest language capabilities and maintain alignment with current Node.js ecosystem standards, improving application performance and security posture.

**Specific Features and Detailed Changes:**  
- **Runtime Support:** Azure Functions now fully supports Node.js 22 runtime, allowing function apps to be created, tested locally, and deployed seamlessly.  
- **Cross-Platform Availability:** Support extends to all Azure Functions hosting plans on both Linux and Windows, ensuring broad compatibility regardless of the underlying OS.  
- **Local Development:** Developers can use the Azure Functions Core Tools and Visual Studio Code extensions to develop and debug Node.js 22 functions locally before deployment.  
- **Improved Performance and Security:** Node.js 22 includes V8 engine upgrades, enhanced diagnostics, and stricter security defaults, all inherited by Azure Functions apps running on this runtime.

**Technical Mechanisms and Implementation Methods:**  
Azure Functions runtime abstracts the underlying Node.js version through its managed environment. When a function app is configured to use Node.js 22, the platform provisions containers or sandboxed environments with the Node.js 22 runtime pre-installed. Developers specify the runtime version in the function app’s configuration (e.g., via the `FUNCTIONS_WORKER_RUNTIME` and `WEBSITE_NODE_DEFAULT_VERSION` settings). The Azure Functions Core Tools support scaffolding projects targeting Node.js 22, and deployment pipelines (Azure DevOps, GitHub Actions) can be configured to build and deploy these apps seamlessly. The platform handles runtime updates, patching, and scaling transparently.

**Use Cases and Application Scenarios:**  
- **Modern Web APIs:** Building RESTful APIs using the latest ECMAScript features and async patterns.  
- **Event Processing:** Handling events from Azure Event Grid, Service Bus, or Blob Storage with improved runtime performance.  
- **Microservices:** Implementing lightweight, scalable microservices that benefit from Node.js 22’s performance optimizations.  
- **Automation and Integration:** Running serverless workflows that integrate with other Azure services, leveraging the latest Node.js libraries.  
- **Real-time Data Processing:** Utilizing updated diagnostics and performance tools for monitoring real-time data pipelines.

**Important Considerations and Limitations:**  
- **Compatibility:** While Node.js 22 is backward compatible with most Node.js 18 or 20 code, some deprecated APIs or behaviors might have changed; thorough testing is recommended.  
- **Third-Party Modules:** Ensure all npm dependencies are compatible with Node.js 22 to avoid runtime errors.  
- **Cold Start Impact:** Although Node.js 22 includes performance improvements, cold start times may still vary depending on app complexity and hosting plan.  
- **Runtime Configuration:** Correctly setting environment variables and runtime versions is critical to avoid deployment issues.  
- **Monitoring:** Utilize Azure Monitor and Application Insights to track function performance and diagnose issues specific to the new runtime.

**Integration with Related Azure Services:**  
Node.js 22 support in Azure Functions integrates smoothly with Azure’s event-driven ecosystem, including Event Grid, Service Bus, Cosmos DB, and Blob Storage triggers and bindings. It also complements Azure API Management for exposing

---

### 2. Generally Available: Azure Migrate now supports migration to disks with Zone-Redundant Storage (ZRS) redundancy 

**Published**: August 22, 2025 11:00:33 UTC
**Link**: [Generally Available: Azure Migrate now supports migration to disks with Zone-Redundant Storage (ZRS) redundancy ](https://azure.microsoft.com/updates?id=501233)

**Update ID**: 501233
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Migration, Azure Migrate, Features, Management

**Summary**:

- What was updated  
Azure Migrate now supports migration to disks configured with Zone-Redundant Storage (ZRS) redundancy.

- Key changes or new features  
During server migration workflows, users can select ZRS as the redundancy option for destination disks. This enables automatic provisioning of disks with ZRS, enhancing data durability and availability by replicating data synchronously across multiple availability zones within the same region.

- Target audience affected  
Developers and IT professionals involved in cloud migration, infrastructure modernization, and disaster recovery planning who use Azure Migrate for server and workload migration.

- Important notes if any  
Choosing ZRS can improve resilience against zone-level failures without requiring application-level changes. However, it may have cost implications compared to locally redundant storage (LRS). Users should evaluate their availability requirements and budget when selecting redundancy options during migration. This update streamlines adopting zone-redundant storage for migrated workloads, supporting higher availability SLAs in Azure.

**Details**:

The recent Azure Migrate update introduces support for migrating servers to managed disks configured with Zone-Redundant Storage (ZRS) redundancy, enabling users to select ZRS as the disk redundancy option during migration workflows. This enhancement addresses the growing need for higher availability and resilience in cloud storage by automatically provisioning disks with ZRS, which replicates data synchronously across multiple availability zones within the same Azure region.

**Background and Purpose:**  
Azure Migrate is a central hub for assessment and migration of on-premises workloads to Azure. Previously, while migrating servers, users could select storage redundancy options such as Locally Redundant Storage (LRS) or Geo-Redundant Storage (GRS) for managed disks. However, these options either provide replication within a single data center (LRS) or across regions (GRS), but not across multiple availability zones within the same region. With the increasing adoption of availability zones to improve fault tolerance against datacenter-level failures, there was a need to support Zone-Redundant Storage (ZRS) during migration. This update fulfills that requirement by enabling direct migration to ZRS disks, enhancing data durability and availability for migrated workloads.

**Specific Features and Detailed Changes:**  
- During the server migration process in Azure Migrate, users can now explicitly select ZRS as the redundancy option for managed disks attached to the migrated virtual machines.  
- The migration service automatically provisions new managed disks with ZRS enabled, ensuring data is synchronously replicated across three availability zones in the target Azure region.  
- This feature is generally available, indicating full support and SLA-backed reliability for production workloads.  
- The UI and APIs for Azure Migrate have been updated to include ZRS as a selectable redundancy option, streamlining the migration workflow without requiring manual post-migration disk configuration.

**Technical Mechanisms and Implementation Methods:**  
Zone-Redundant Storage achieves high availability by replicating data synchronously across three physically separated Azure availability zones within the same region. This means that if one zone experiences an outage, the data remains accessible from the other zones without interruption. Azure Migrate integrates with the Azure Compute and Storage services to provision managed disks with the ZRS SKU during the migration cutover phase. The migration orchestrator communicates the redundancy choice to the Azure Storage backend, which then handles the replication and durability guarantees transparently. This integration ensures that migrated VMs benefit from zone-level fault tolerance immediately upon provisioning.

**Use Cases and Application Scenarios:**  
- Enterprises migrating critical workloads that require high availability and resilience against zone failures can leverage this feature to improve their disaster recovery posture.  
- Applications with stringent uptime requirements, such as financial services, healthcare, and e-commerce platforms, benefit from ZRS disks to minimize downtime risks.  
- Workloads that are sensitive to regional outages but do not require geo-replication can use ZRS as a cost-effective alternative to GRS, balancing availability and cost.  
- Organizations adopting Azure Availability Zones as part of their architecture can now migrate workloads directly into zone-redundant storage configurations, simplifying infrastructure modernization.

**Important Considerations and Limitations:**  
- ZRS is supported only in Azure regions that have multiple availability zones; regions without zone support cannot leverage this feature.  
- While ZRS provides zone-level redundancy, it does not replace geo-redundancy; for disaster recovery across regions, GRS or RA-GRS remains necessary.  
- Migrated disks with ZRS may have different pricing compared to LRS or GRS; users should evaluate cost implications.  
- Existing migrated VMs can be converted to ZRS disks post-migration, but this update simplifies the process by enabling direct provisioning during migration.  
- Users should verify compatibility of their workloads and VM sizes with ZRS disks, as some specialized VM types or legacy configurations may have restrictions.

**Integration with Related Azure Services:**  
- Azure Migrate’s integration with Azure Compute and Storage services is enhanced to support ZRS provisioning seamlessly.  
-

---


*This report was automatically generated - 2025-08-23 03:01:28 UTC*