# June 12, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 12, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Retirement: Av2-series, F-series, Fs-series, Fsv2-series, G-series, Gs-series, and Lsv2-series Virtual Machines for Azure Batch pools

**Published**: June 11, 2026 19:00:41 UTC
**Link**: [Retirement: Av2-series, F-series, Fs-series, Fsv2-series, G-series, Gs-series, and Lsv2-series Virtual Machines for Azure Batch pools](https://azure.microsoft.com/updates?id=564774)

**Update ID**: 564774
**Data source**: Azure Updates API

**Categories**: Compute, Batch, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of several Virtual Machine (VM) series for Azure Batch pools: Av2-series, F-series, Fs-series, Fsv2-series, G-series, Gs-series, and Lsv2-series. The retirement date is November 15, 2028.

- Key changes or new features  
After November 15, 2028, you will no longer be able to create new Azure Batch pools using these VM series. Existing Batch pools using these VM sizes will also no longer be supported and may not function as expected. No new features are being introduced; this is a deprecation notice.

- Target audience affected  
This update impacts developers and IT professionals managing Azure Batch workloads that currently use any of the retiring VM series. Any automated deployments, scripts, or infrastructure-as-code templates referencing these VM sizes will require updates.

- Important notes if any  
Microsoft recommends migrating existing Batch pools to supported VM series before the retirement date to avoid service disruptions. Review your current Batch pool configurations and update them to use supported VM sizes. Early migration and testing are advised to ensure compatibility and performance. For more information and migration guidance, refer to the official Azure documentation.

Link: https://azure.microsoft.com/updates?id=564774

**Details**:

**Comprehensive Technical Explanation:**

**Background and Purpose of the Update:**  
Azure Compute has announced the retirement of several Virtual Machine (VM) series—specifically, Av2-series, F-series, Fs-series, Fsv2-series, G-series, Gs-series, and Lsv2-series—for use in Azure Batch pools, effective November 15, 2028. The primary purpose of this update is to inform customers that these VM series will no longer be available for provisioning new Azure Batch pools after the retirement date. This action is part of Azure’s ongoing efforts to phase out older VM families in favor of newer, more performant, and secure VM offerings.

**Specific Features and Detailed Changes:**  
- The retirement affects the following VM series: Av2, F, Fs, Fsv2, G, Gs, and Lsv2.
- After November 15, 2028, it will not be possible to create new Azure Batch pools using any of these VM series.
- Existing Batch pools that utilize these VM series may also be impacted, though the update specifically highlights the restriction on creating new pools.
- The update is specific to Azure Batch, a service designed to run large-scale parallel and high-performance computing (HPC) workloads in the cloud.

**Technical Mechanisms and Implementation Methods:**  
- Azure will enforce the retirement by disabling the option to select the affected VM series when configuring new Batch pools after the specified date.
- Existing APIs, ARM templates, and Azure Portal interfaces will no longer allow the selection or provisioning of these VM sizes for new Batch pools.
- The underlying infrastructure supporting these VM series will be deprecated, and support for these SKUs will be removed from the Batch service’s configuration options.

**Use Cases and Application Scenarios:**  
- The VM series being retired are commonly used for a variety of compute-intensive workloads, including batch processing, rendering, simulations, and other parallelizable tasks managed via Azure Batch.
- Organizations leveraging these VM series for cost-effective compute or specific hardware features (such as high memory or local SSD) in their Batch jobs will need to plan migration to supported VM series.
- Scenarios involving automated scaling, job scheduling, and resource optimization in Batch pools will need to be reviewed to ensure compatibility with supported VM types post-retirement.

**Important Considerations and Limitations:**  
- Customers must review their existing Azure Batch pools and job templates to identify dependencies on the retiring VM series.
- Migration planning is essential to avoid service disruption; this may involve testing workloads on alternative VM series and updating automation scripts and infrastructure-as-code templates.
- There may be differences in performance, pricing, and hardware capabilities between the retiring and replacement VM series, requiring workload validation and potential tuning.
- The update does not specify whether existing pools using these VM series will continue to function after the retirement date, so proactive migration is recommended.

**Integration with Related Azure Services:**  
- Azure Batch integrates with other Azure services such as Azure Storage, Azure Virtual Network, and Azure Active Directory for job management, data access, and security.
- The retirement of these VM series may impact integrations where specific VM capabilities are required (e.g., local SSD in Lsv2-series).
- Customers should ensure that their end-to-end workflows, including data ingress/egress and security configurations, are compatible with the new VM series selected for Batch pools.

**Calm and Detailed Summary Sentence:**  
Azure Compute will retire the Av2, F, Fs, Fsv2, G, Gs, and Lsv2 VM series for Azure Batch pools on November 15, 2028, requiring customers to transition to supported VM series for new pool creation and to review existing workloads for continued compatibility.

---

### 2. Retirement: D-series, Ds-series, Dv2-series, Dsv2-series, and Ls-series Virtual Machines for Azure Batch pools

**Published**: June 11, 2026 19:00:41 UTC
**Link**: [Retirement: D-series, Ds-series, Dv2-series, Dsv2-series, and Ls-series Virtual Machines for Azure Batch pools](https://azure.microsoft.com/updates?id=564772)

**Update ID**: 564772
**Data source**: Azure Updates API

**Categories**: Compute, Batch, Retirements

**Summary**:

- What was updated  
Azure Compute announced the retirement of several Virtual Machine (VM) series—D-series, Ds-series, Dv2-series, Dsv2-series, and Ls-series—for use in Azure Batch pools.

- Key changes or new features  
These VM series will be retired on May 1, 2028. After this date, you will no longer be able to create new Azure Batch pools using these VM sizes. Existing Batch pools that use these VM series will also be impacted and will need to migrate to supported VM series.

- Target audience affected  
This update affects developers, IT professionals, and administrators who manage or deploy Azure Batch workloads using the D-series, Ds-series, Dv2-series, Dsv2-series, or Ls-series VMs.

- Important notes if any  
To avoid service disruption, review your current Azure Batch pools and plan migration to supported VM series before the retirement date. Microsoft recommends updating scripts, templates, and automation workflows to use newer VM sizes. For more information and migration guidance, refer to the official Azure documentation.

Link: [Azure Update Announcement](https://azure.microsoft.com/updates?id=564772)

**Details**:

**Azure Update Technical Report**

**Title:** Retirement: D-series, Ds-series, Dv2-series, Dsv2-series, and Ls-series Virtual Machines for Azure Batch pools  
**Source:** [Azure Update Link](https://azure.microsoft.com/updates?id=564772)  
**Retirement Date:** May 1, 2028

---

**Background and Purpose of the Update**  
Azure Compute is announcing the retirement of several legacy Virtual Machine (VM) series—specifically D-series, Ds-series, Dv2-series, Dsv2-series, and Ls-series—within Azure Batch pools. The primary purpose of this update is to phase out older VM families that may no longer meet current performance, scalability, or security standards, and to encourage migration to newer VM series that offer improved capabilities and support.

**Specific Features and Detailed Changes**  
After May 1, 2028, the following changes will take effect:
- **Creation of New Batch Pools:** It will no longer be possible to create new Azure Batch pools using any of the retired VM series (D-series, Ds-series, Dv2-series, Dsv2-series, and Ls-series).
- **Existing Batch Pools:** The update specifies the impact on new pool creation; details regarding the operation of existing pools using these VM series are not provided in the announcement.

**Technical Mechanisms and Implementation Methods**  
Azure Batch pools are logical groupings of compute resources used to run parallel workloads. Each pool is configured with a specific VM series, which determines the underlying hardware and performance characteristics. The retirement will be enforced at the Azure API and portal level, preventing selection of the retired VM series when configuring new Batch pools. This mechanism ensures that new deployments are aligned with supported VM families, reducing operational risks associated with legacy hardware.

**Use Cases and Application Scenarios**  
Azure Batch is commonly used for large-scale parallel processing workloads such as:
- High-performance computing (HPC)
- Data processing pipelines
- Rendering tasks
- Scientific simulations

Organizations currently utilizing the D-series, Ds-series, Dv2-series, Dsv2-series, or Ls-series VMs for these workloads must plan to migrate to supported VM series before the retirement date to ensure continuity and optimal performance.

**Important Considerations and Limitations**  
- **Migration Planning:** IT professionals should identify all Batch pools using the affected VM series and develop a migration strategy to newer VM families, such as Dv3, Dv4, or other recommended series.
- **Compatibility:** Review application and workload requirements to ensure compatibility with newer VM series, as performance characteristics and available features may differ.
- **Automation and Scripts:** Update any automation, deployment scripts, or templates that reference the retired VM series to prevent deployment failures post-retirement.
- **Resource Availability:** The update does not specify whether existing pools will continue to operate or if there will be further restrictions; monitor future Azure communications for additional guidance.

**Integration with Related Azure Services**  
Azure Batch integrates with various Azure services, including Azure Storage, Azure Networking, and Azure Monitoring. When migrating Batch pools to newer VM series, ensure that integration points and dependencies are validated for compatibility and performance. Additionally, leverage Azure Resource Manager (ARM) templates and Azure Policy to enforce the use of supported VM series across deployments.

---

**Summary Sentence:**  
Azure Compute will retire D-series, Ds-series, Dv2-series, Dsv2-series, and Ls-series Virtual Machines for Azure Batch pools on May 1, 2028, after which new Batch pools using these VM series cannot be created, requiring IT professionals to migrate workloads to supported VM families to ensure ongoing operational continuity.

---

### 3. Retirement: GPv1 and Legacy Blob storage account creation

**Published**: June 11, 2026 19:00:41 UTC
**Link**: [Retirement: GPv1 and Legacy Blob storage account creation](https://azure.microsoft.com/updates?id=564441)

**Update ID**: 564441
**Data source**: Azure Updates API

**Categories**: Storage, Storage Accounts, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of General Purpose v1 (GPv1) storage accounts, including legacy Blob storage account creation.

- Key changes or new features  
Creation of new GPv1 and legacy Blob storage accounts will no longer be supported. Existing GPv1 and legacy Blob accounts will continue to function for now, but users are encouraged to migrate to General Purpose v2 (GPv2) storage accounts, which offer improved performance, scalability, and cost efficiency.

- Target audience affected  
Developers and IT professionals managing Azure Storage accounts, especially those using GPv1 or legacy Blob storage for applications, data storage, or backup solutions.

- Important notes if any  
No new GPv1 or legacy Blob storage accounts can be created after the retirement date. Existing accounts are not immediately affected, but migration to GPv2 is strongly recommended to benefit from the latest features and to ensure long-term support. Review your storage account inventory and plan migrations to avoid service disruption. For migration guidance, refer to official Azure documentation.

Link: https://azure.microsoft.com/updates?id=564441

**Details**:

**Azure Update Report: Retirement of GPv1 and Legacy Blob Storage Account Creation**

**Background and Purpose of the Update**  
Microsoft Azure is retiring the creation of General Purpose v1 (GPv1) storage accounts, including legacy blob storage accounts. This decision is part of a broader initiative to streamline the Azure Storage portfolio, aiming to deliver improved performance, scalability, and cost efficiency. By focusing on more modern storage account types, Azure intends to simplify storage management and encourage adoption of newer, more capable offerings.

**Specific Features and Detailed Changes**  
The update specifically targets the discontinuation of the ability to create new GPv1 storage accounts and legacy blob storage accounts. GPv1 accounts were originally designed to provide basic storage functionality for blobs, files, queues, and tables. However, they lack many advanced features available in later versions, such as General Purpose v2 (GPv2) and Blob Storage accounts. The retirement means that after the designated date, users will no longer be able to provision these account types via the Azure Portal, CLI, PowerShell, or ARM templates.

**Technical Mechanisms and Implementation Methods**  
The retirement will be enforced at the platform level. Azure Resource Manager (ARM) APIs, portal interfaces, and scripting tools will be updated to remove GPv1 and legacy blob storage account options from account creation workflows. Existing GPv1 accounts will not be affected by this change; only the creation of new accounts is impacted. Azure will continue to support existing GPv1 storage accounts for the time being, but users are encouraged to migrate to GPv2 or Blob Storage accounts to benefit from enhanced features and ongoing support.

**Use Cases and Application Scenarios**  
GPv1 storage accounts have historically been used for legacy applications and workloads requiring basic storage capabilities. Typical scenarios include archival storage, simple file sharing, and basic blob storage. With the retirement, new projects and workloads should utilize GPv2 or Blob Storage accounts, which offer improved performance, advanced security features, tiered storage options, and better integration with Azure services.

**Important Considerations and Limitations**  
- **Migration Planning:** Existing GPv1 accounts are not immediately impacted, but organizations should plan to migrate to GPv2 or Blob Storage accounts to future-proof their storage infrastructure.
- **Feature Parity:** GPv2 accounts provide all features of GPv1, plus additional enhancements such as support for hot, cool, and archive tiers, improved analytics, and better integration with Azure Data Lake Storage.
- **Cost Efficiency:** GPv2 accounts offer more granular pricing and cost management options, which can result in lower storage costs for many workloads.
- **API Compatibility:** Applications using GPv1 APIs may require updates to ensure compatibility with GPv2 or Blob Storage APIs.

**Integration with Related Azure Services**  
GPv2 and Blob Storage accounts integrate seamlessly with Azure services such as Azure Data Lake Storage, Azure Backup, Azure Site Recovery, and Azure Synapse Analytics. They support advanced features like Azure Active Directory authentication, managed identities, and network security controls, enabling more robust and secure solutions.

**Summary Sentence**  
Azure is retiring the creation of GPv1 and legacy blob storage accounts to streamline its storage portfolio, enhance performance and scalability, and encourage migration to modern storage account types with advanced features and improved cost efficiency.

---

### 4. Generally Available: SQL MCP Server

**Published**: June 11, 2026 18:45:02 UTC
**Link**: [Generally Available: SQL MCP Server](https://azure.microsoft.com/updates?id=564734)

**Update ID**: 564734
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
SQL MCP Server is now generally available on Azure.

- Key changes or new features  
SQL MCP Server offers a secure, high-performance platform for building agentic solutions with controlled access to production data. It is designed for SQL workloads and is compatible with PostgreSQL and Azure Cosmos DB. The server enables dynamic data access management, allowing developers to build solutions that require granular control over data exposure and usage. This release focuses on enhanced security, performance, and compatibility across multiple database types.

- Target audience affected  
Developers building data-driven or agentic applications, database administrators, and IT professionals responsible for managing secure data access in production environments.

- Important notes if any  
SQL MCP Server supports integration with existing SQL, PostgreSQL, and Cosmos DB environments, making it easier to adopt without significant changes to current infrastructure. The general availability release ensures enterprise-grade support and reliability. Organizations can now leverage SQL MCP Server for secure, controlled, and high-performance data access in their production workloads.

**Details**:

**Azure Update Report: General Availability of SQL MCP Server**

**Background and Purpose of the Update**  
The general availability (GA) of SQL MCP Server marks a significant milestone in Azure’s data platform offerings. The primary purpose of this release is to provide customers with a secure and high-performance solution for building agentic (autonomous or semi-autonomous) applications that require controlled access to production data. This addresses the growing demand for robust data access mechanisms that maintain strict security and compliance, especially in environments where sensitive or mission-critical data is involved.

**Specific Features and Detailed Changes**  
SQL MCP Server introduces several key features:
- **Secure Data Access:** It enables controlled access to production data, ensuring that only authorized agents or applications can interact with sensitive datasets.
- **High Performance:** The server is optimized for performance, supporting demanding workloads and minimizing latency for data operations.
- **Multi-Database Compatibility:** SQL MCP Server is designed for SQL workloads and is compatible with both PostgreSQL and Azure Cosmos DB, broadening its applicability across different database engines.
- **Agentic Solution Support:** The server is purpose-built to facilitate agentic solutions, which may involve automated processes or intelligent agents interacting with data in a managed and secure manner.

**Technical Mechanisms and Implementation Methods**  
While the detailed technical architecture is not specified in the provided content, SQL MCP Server operates as a dynamic data access layer that enforces security and performance best practices. Its compatibility with SQL, PostgreSQL, and Azure Cosmos DB suggests that it abstracts database interactions, providing a unified interface for agentic applications. Controlled access is likely implemented via robust authentication and authorization mechanisms, ensuring that only permitted entities can query or manipulate production data.

**Use Cases and Application Scenarios**  
Typical scenarios for SQL MCP Server include:
- **Autonomous Data Processing:** Enabling automated agents to securely access and process production data for analytics, monitoring, or operational tasks.
- **AI and Machine Learning Pipelines:** Facilitating controlled data access for AI models or ML pipelines that require real-time or batch data from production databases.
- **Multi-Database Applications:** Supporting applications that need to interact with both SQL-based and NoSQL (Cosmos DB) data stores through a consistent and secure interface.
- **Compliance-Driven Environments:** Ensuring that data access in regulated industries (e.g., finance, healthcare) adheres to strict security and audit requirements.

**Important Considerations and Limitations**  
- **Security Configuration:** Proper configuration of access controls is critical to prevent unauthorized data access.
- **Database Compatibility:** While SQL MCP Server supports SQL, PostgreSQL, and Cosmos DB, compatibility with other database engines is not indicated.
- **Performance Tuning:** High-performance claims may require tuning based on workload characteristics and underlying infrastructure.
- **Feature Scope:** The update does not specify advanced features such as data transformation, caching, or auditing—these should be evaluated separately.

**Integration with Related Azure Services**  
SQL MCP Server is positioned to integrate seamlessly with Azure’s data ecosystem:
- **Azure SQL Database and Managed Instances:** Direct compatibility for SQL workloads.
- **Azure Database for PostgreSQL:** Enables agentic solutions on PostgreSQL databases.
- **Azure Cosmos DB:** Extends agentic data access to globally distributed NoSQL data.
- **Azure Security and Compliance Services:** Likely to be used in conjunction with Azure Active Directory, Azure Policy, and Azure Monitor for end-to-end security and governance.

**Summary Sentence**  
SQL MCP Server is now generally available, providing a secure, high-performance, and multi-database-compatible solution for building agentic applications with controlled access to production data across SQL, PostgreSQL, and Azure Cosmos DB environments.

---

### 5. Retirement: Azure Load Balancer Inbound NAT rule version 1 for Azure VMSS (aka Inbound NAT Pools)

**Published**: June 11, 2026 16:15:07 UTC
**Link**: [Retirement: Azure Load Balancer Inbound NAT rule version 1 for Azure VMSS (aka Inbound NAT Pools)](https://azure.microsoft.com/updates?id=565482)

**Update ID**: 565482
**Data source**: Azure Updates API

**Categories**: Retirements, Services, Feature

**Summary**:

- What was updated  
Azure has updated the retirement scope for Inbound NAT rule version 1 resources on Azure Load Balancer, specifically for Azure Virtual Machine Scale Sets (VMSS). Previously, all version 1 Inbound NAT rules (including single-VM rules and NAT pools) were set for retirement. The scope is now narrowed.

- Key changes or new features  
Only Inbound NAT Pools (used with VMSS) are being retired. Single-VM Inbound NAT rules are no longer affected by this retirement. Customers using Inbound NAT Pools for VMSS must migrate to the newer Inbound NAT rule version 2 resources.

- Target audience affected  
This update impacts IT professionals and developers managing Azure VMSS deployments that utilize Azure Load Balancer Inbound NAT Pools (version 1). Single-VM deployments using Inbound NAT rules are not affected.

- Important notes if any  
Action is required for customers using Inbound NAT Pools with VMSS: migrate to Inbound NAT rule version 2 before the retirement date to avoid service disruption. Review your Azure Load Balancer configurations and update any VMSS deployments using version 1 NAT Pools. For migration guidance, refer to the official Azure documentation.  
[Azure Update Link](https://azure.microsoft.com/updates?id=565482)

**Details**:

**Azure Update Technical Explanation**

**Title:** Retirement: Azure Load Balancer Inbound NAT rule version 1 for Azure VMSS (aka Inbound NAT Pools)

**Background and Purpose of the Update:**
Microsoft Azure has announced a revision to its earlier communication regarding the retirement of Inbound NAT rule version 1 resources in Azure Load Balancer. Originally, the retirement encompassed both single-VM NAT rules and NAT pools for Virtual Machine Scale Sets (VMSS). The latest update narrows the scope of this retirement specifically to Inbound NAT Pools for VMSS. This change is intended to streamline resource management and encourage the adoption of newer, more robust NAT rule implementations.

**Specific Features and Detailed Changes:**
- The retirement now targets only Inbound NAT Pools associated with VMSS, which are version 1 NAT rules.
- Single-VM NAT rules are no longer included in the retirement scope.
- Inbound NAT Pools allow mapping of a range of frontend ports on the Load Balancer to a range of backend ports on VMSS instances, facilitating remote access (e.g., RDP, SSH) to individual VMs within a scale set.
- After retirement, creation and management of version 1 NAT Pools for VMSS will be deprecated and unsupported.

**Technical Mechanisms and Implementation Methods:**
- Inbound NAT Pools (version 1) are configured on Azure Load Balancer to provide port-based access to VMSS instances.
- The mechanism involves assigning a unique frontend port for each VMSS instance, which is then mapped to a specific backend port (such as 3389 for RDP or 22 for SSH).
- This is typically used to enable remote management of VMs in a scale set without exposing all instances directly to the internet.
- With the retirement, customers must transition to newer NAT rule implementations (version 2 or later), which offer improved functionality, security, and manageability.

**Use Cases and Application Scenarios:**
- Inbound NAT Pools are commonly used in scenarios where administrators need to access individual VMs within a VMSS for maintenance, troubleshooting, or configuration.
- Typical applications include remote desktop access to Windows VMSS instances or SSH access to Linux VMSS instances via unique ports mapped through the Load Balancer.
- Organizations using automation scripts or orchestration tools that rely on NAT Pool configurations for VMSS will need to update their workflows to accommodate the retirement.

**Important Considerations and Limitations:**
- Existing deployments using Inbound NAT Pools (version 1) for VMSS must plan for migration to supported NAT rule versions to avoid service disruption.
- The retirement does not affect single-VM NAT rules, so those configurations remain supported.
- Customers should review their VMSS Load Balancer configurations and update any dependencies on version 1 NAT Pools.
- It is critical to ensure that migration plans include updating access methods, firewall rules, and automation scripts to align with the new NAT rule versions.

**Integration with Related Azure Services:**
- Azure Load Balancer is tightly integrated with VMSS, providing network traffic distribution and remote access capabilities.
- Transitioning to newer NAT rule versions may require updates to Azure Resource Manager (ARM) templates, Azure CLI scripts, and integration with Azure Automation or DevOps pipelines.
- Customers should verify compatibility with other Azure services such as Azure Bastion, which can provide secure remote access alternatives to NAT Pools.

**Summary Sentence:**  
The scope of retirement for Azure Load Balancer Inbound NAT rule version 1 resources has been narrowed to affect only Inbound NAT Pools for Virtual Machine Scale Sets, requiring customers to transition to newer NAT rule implementations for continued support and functionality.

---


*This report was automatically generated - 2026-06-12 03:02:44 UTC*