# September 13, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 13, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Bring Your Own License (BYOL) Support for JBoss EAP on Azure App Service

**Published**: September 12, 2025 14:30:17 UTC
**Link**: [Generally Available: Bring Your Own License (BYOL) Support for JBoss EAP on Azure App Service](https://azure.microsoft.com/updates?id=501891)

**Update ID**: 501891
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Mobile, Web, App Service, Features, Pricing & Offerings

**Summary**:

- What was updated  
Azure App Service now supports Bring Your Own License (BYOL) for JBoss Enterprise Application Platform (EAP).

- Key changes or new features  
This update allows enterprise customers to deploy Java applications on Azure App Service using their existing JBoss EAP licenses. It provides greater flexibility in license management and can reduce costs by leveraging already purchased licenses rather than paying for new ones through Azure. Developers can now run JBoss EAP workloads in a fully managed PaaS environment while maintaining compliance with their licensing agreements.

- Target audience affected  
Java developers, DevOps engineers, and IT professionals managing enterprise Java applications on Azure who use or plan to use JBoss EAP. Enterprises looking to optimize licensing costs and streamline deployment of Java workloads on Azure App Service will benefit most.

- Important notes if any  
Customers must ensure compliance with Red Hat’s licensing terms when using BYOL. This feature enhances cost efficiency but requires proper license management. For detailed guidance, refer to Azure documentation and Red Hat licensing policies.

**Details**:

The recent Azure update announces the general availability of Bring Your Own License (BYOL) support for JBoss Enterprise Application Platform (EAP) on Azure App Service, enabling enterprise customers to deploy Java applications with enhanced flexibility and cost control. This update addresses the need for organizations to leverage existing JBoss EAP licenses while benefiting from the fully managed, scalable, and secure environment provided by Azure App Service.

**Background and Purpose:**  
JBoss EAP is a widely used Java EE application server favored by enterprises for its robustness and support for enterprise Java standards. Previously, deploying JBoss EAP on Azure App Service required using licenses bundled with the platform or purchasing new ones, which could increase costs and complicate license management. The BYOL capability allows organizations to utilize their existing JBoss EAP licenses, aligning with cost optimization strategies and compliance requirements. This update aims to simplify migration and modernization of Java workloads by combining license flexibility with Azure’s platform-as-a-service (PaaS) benefits.

**Specific Features and Detailed Changes:**  
- **BYOL Licensing Model:** Customers can now upload and apply their own JBoss EAP licenses when deploying Java applications on Azure App Service.  
- **Seamless Deployment:** The App Service environment supports JBoss EAP runtime with BYOL, enabling deployment of enterprise Java applications without vendor lock-in or additional license fees from Azure.  
- **Enhanced Cost Efficiency:** By reusing existing licenses, enterprises reduce total cost of ownership (TCO) for cloud migration and ongoing operations.  
- **Support for Standard JBoss EAP Versions:** The BYOL feature supports multiple JBoss EAP versions consistent with Red Hat’s licensing terms, ensuring compatibility and compliance.

**Technical Mechanisms and Implementation Methods:**  
- **License Upload and Management:** Customers upload their JBoss EAP license files (typically `.lic` files) through Azure portal, CLI, or ARM templates during the App Service creation or configuration phase.  
- **Custom Container or Built-in Runtime:** Azure App Service supports deploying JBoss EAP either via custom container images that include the BYOL license or through configuration settings that reference the uploaded license.  
- **Integration with App Service Runtime:** The platform integrates the license validation process within the startup scripts or container entry points, ensuring the JBoss server runs with the provided license.  
- **Security and Compliance:** License files are stored securely within the App Service environment, with access controls to prevent unauthorized use or leakage.

**Use Cases and Application Scenarios:**  
- **Enterprise Java Application Modernization:** Organizations migrating legacy JBoss EAP applications to Azure can maintain license compliance while leveraging PaaS benefits such as auto-scaling, patching, and integrated monitoring.  
- **Cost-Optimized Cloud Migration:** Enterprises with existing JBoss EAP investments can reduce licensing costs when moving workloads to Azure.  
- **Dev/Test Environments:** BYOL enables consistent licensing across development, testing, and production environments, facilitating streamlined DevOps workflows.  
- **Hybrid Deployments:** Customers running hybrid architectures can maintain license consistency across on-premises and cloud deployments.

**Important Considerations and Limitations:**  
- **License Compliance:** Customers must ensure their JBoss EAP licenses are valid for cloud deployment under Red Hat’s licensing terms. Azure does not provide licenses; customers are responsible for license procurement and compliance.  
- **Supported Versions:** Only specific JBoss EAP versions are supported for BYOL on Azure App Service; users should verify compatibility before deployment.  
- **License File Management:** Proper handling and secure storage of license files are critical to avoid service disruptions.  
- **No License Mobility Guarantee:** Unlike some Microsoft licenses, JBoss EAP licenses may have restrictions on mobility; customers should consult Red Hat licensing policies.  
- **Limited to Azure App Service:** BYOL support currently applies only to JBoss EAP on Azure App Service and not other Azure compute services like Azure Kubernetes Service or Virtual Machines.

**Integration with Related Azure

---

### 2. Generally Available: Azure Cosmos DB for MongoDB (vCore) same-region replica cluster 

**Published**: September 12, 2025 13:45:05 UTC
**Link**: [Generally Available: Azure Cosmos DB for MongoDB (vCore) same-region replica cluster ](https://azure.microsoft.com/updates?id=501975)

**Update ID**: 501975
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Features

**Summary**:

- What was updated  
Azure Cosmos DB for MongoDB (vCore) now supports creating same-region replica clusters.

- Key changes or new features  
Developers and IT professionals can deploy a read-only replica cluster within the same Azure region as the primary read-write cluster. This replica cluster is continuously synchronized with the primary, ensuring strong data consistency and low-latency read access. This feature enhances high availability and read scalability without cross-region latency or data transfer costs.

- Target audience affected  
This update primarily benefits developers and database administrators managing Azure Cosmos DB for MongoDB workloads who require improved read scalability, high availability, and disaster recovery options within a single region.

- Important notes if any  
The same-region replica cluster is designed for read operations only and maintains continuous synchronization with the primary cluster. This capability complements existing cross-region replication features by providing a low-latency, cost-effective solution for scaling reads and improving resilience within the same geographic location. Users should consider this when architecting their Cosmos DB deployments for optimized performance and availability.

For more details, visit: https://azure.microsoft.com/updates?id=501975

**Details**:

The recent Azure update announces the general availability of same-region replica clusters for Azure Cosmos DB for MongoDB (vCore), enabling users to create a secondary replica cluster within the same Azure region as the primary cluster. This enhancement is designed to improve data availability, read scalability, and operational flexibility while maintaining strong data consistency within a single geographic location.

**Background and Purpose:**  
Previously, Azure Cosmos DB for MongoDB (vCore) supported replica clusters primarily across different regions to provide geo-redundancy and disaster recovery. However, certain applications require high availability and read scalability without the latency or complexity introduced by cross-region replication. The introduction of same-region replica clusters addresses this need by allowing a read-only replica cluster to exist in the same Azure region as the primary read-write cluster, facilitating faster read operations and operational resilience within a single data center footprint.

**Specific Features and Detailed Changes:**  
- **Same-Region Replica Cluster Creation:** Users can now provision a replica cluster in the same Azure region as the primary cluster. This replica cluster is read-only and continuously synchronized with the primary cluster.  
- **Continuous Synchronization:** The replica cluster maintains near real-time data consistency with the primary cluster using Azure Cosmos DB’s internal replication mechanisms, ensuring that reads from the replica reflect the latest committed writes.  
- **Improved Read Scalability:** By directing read-heavy workloads to the replica cluster, applications can offload read operations from the primary cluster, improving overall throughput and reducing latency for read queries.  
- **Operational Flexibility:** Maintenance, backups, or schema changes can be performed on the replica cluster with minimal impact on the primary cluster’s write operations.

**Technical Mechanisms and Implementation Methods:**  
The same-region replica cluster leverages Azure Cosmos DB’s distributed architecture and its underlying replication protocol. The primary cluster acts as the authoritative source of truth, handling all write operations. Changes are asynchronously but rapidly propagated to the replica cluster within the same region, ensuring low-latency synchronization. The replica cluster exposes a MongoDB-compatible endpoint configured for read-only operations, allowing applications to connect and perform read queries without risking data inconsistency. This setup is managed through Azure Resource Manager templates or the Azure portal, where users specify the replica cluster configuration during deployment or scaling operations.

**Use Cases and Application Scenarios:**  
- **Read-Heavy Applications:** Applications with high read-to-write ratios, such as content delivery platforms, analytics dashboards, or catalog browsing systems, benefit from offloading reads to the replica cluster.  
- **Operational Maintenance:** Organizations can perform schema migrations, backups, or testing on the replica cluster without affecting the primary cluster’s write availability.  
- **Low-Latency Reads Within a Region:** Applications requiring minimal read latency within a region can leverage the replica cluster to reduce contention on the primary cluster.  
- **Disaster Recovery and High Availability:** While cross-region replication remains essential for disaster recovery, same-region replicas enhance availability and fault tolerance within the region.

**Important Considerations and Limitations:**  
- **Read-Only Replica:** The replica cluster does not support write operations; all writes must be directed to the primary cluster.  
- **Consistency Model:** The synchronization is designed to maintain strong consistency, but transient replication lag may occur; applications should handle eventual consistency scenarios accordingly.  
- **Cost Implications:** Running an additional replica cluster within the same region incurs extra compute and storage costs, which should be factored into capacity planning.  
- **Failover:** Automatic failover to the same-region replica cluster is not supported; it is primarily intended for read scaling and operational flexibility rather than high availability failover.

**Integration with Related Azure Services:**  
- **Azure Monitor and Azure Metrics:** Users can monitor replica cluster health, replication lag, and performance metrics through Azure Monitor and integrate alerts for operational insights.  
- **Azure Resource Manager (ARM):** Deployment and management of same-region replica clusters are integrated with ARM templates and Azure CLI for automation and infrastructure as code practices

---


*This report was automatically generated - 2025-09-13 03:01:38 UTC*