# October 01, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 01, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Public Preview: Soft Delete feature in Azure Compute Gallery

**Published**: September 30, 2025 19:30:35 UTC
**Link**: [Public Preview: Soft Delete feature in Azure Compute Gallery](https://azure.microsoft.com/updates?id=506886)

**Update ID**: 506886
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Azure VM Image Builder, Virtual Machine Scale Sets, Virtual Machines, Gallery, Features, Services

**Summary**:

- What was updated  
Azure Compute Gallery now supports a Soft Delete feature, currently in public preview.

- Key changes or new features  
The Soft Delete feature enables recovery of accidentally deleted images within a 7-day retention window. When an image is deleted, it is retained in a recoverable state rather than being permanently removed immediately. Users can restore these images during this grace period, preventing data loss from unintended deletions.

- Target audience affected  
This update primarily benefits developers and IT professionals who manage VM images and versioning in Azure Compute Gallery, improving image lifecycle management and operational resilience.

- Important notes if any  
The feature is in public preview, so users should evaluate it in non-production environments before full adoption. The 7-day retention period is fixed, and after this period, deleted images will be permanently purged. Users should plan their image management workflows accordingly to leverage this recovery capability effectively.

For more details, visit: https://azure.microsoft.com/updates?id=506886

**Details**:

The newly introduced Soft Delete feature in Azure Compute Gallery, currently in public preview, addresses a critical operational risk by enabling the recovery of accidentally deleted images within a configurable retention window of 7 days. This enhancement is designed to improve image management resilience and operational continuity for IT professionals managing large-scale VM image repositories.

**Background and Purpose:**  
Azure Compute Gallery (formerly Shared Image Gallery) is a service that facilitates the management, sharing, and versioning of VM images across subscriptions and regions. Prior to this update, deletion of images was immediate and irreversible, posing a risk of data loss due to human error or automation faults. The Soft Delete feature was introduced to mitigate this risk by providing a safety net that allows administrators to recover deleted images, thereby reducing downtime and rework associated with image recreation.

**Specific Features and Detailed Changes:**  
- **Soft Delete Retention Period:** When an image or image version is deleted, it is not permanently removed but instead marked as “soft deleted” and retained for 7 days by default.  
- **Recovery Capability:** During this retention period, users can restore the soft deleted images to their original state without data loss.  
- **Automatic Purge:** After the 7-day retention window, the soft deleted images are permanently purged from the system.  
- **Scope:** The feature applies to both images and image versions within the Azure Compute Gallery.  
- **Preview Status:** Being in public preview, the feature is available for testing and feedback but may have limitations or changes before general availability.

**Technical Mechanisms and Implementation Methods:**  
Soft Delete is implemented as a state transition within the Azure Compute Gallery’s backend metadata store. Upon deletion, the image’s metadata is flagged as soft deleted, and the actual image blobs remain intact but inaccessible for provisioning. The system maintains a retention timer, after which a background process permanently deletes the image data. Recovery operations update the metadata state back to active, restoring normal access. This approach ensures minimal disruption to storage and indexing systems while providing a reversible deletion workflow.

**Use Cases and Application Scenarios:**  
- **Accidental Deletion Recovery:** Administrators can quickly restore images deleted by mistake, avoiding the need to rebuild or re-upload images.  
- **Automated Cleanup Safety:** Scripts or automation tools that manage image lifecycle can incorporate soft delete to prevent permanent loss from erroneous deletions.  
- **Compliance and Audit:** Organizations can leverage the retention period as a buffer to comply with internal change control and audit policies before permanent deletion.  
- **Multi-Region Image Management:** In scenarios where images are replicated across regions, soft delete ensures consistent recovery options across distributed environments.

**Important Considerations and Limitations:**  
- The retention period is fixed at 7 days during the preview and may be subject to change.  
- Soft deleted images do not incur additional storage costs beyond normal image storage.  
- Images in soft deleted state are not available for VM provisioning or replication.  
- The feature currently supports only images and image versions; other gallery artifacts like galleries or gallery applications are not covered.  
- As a preview feature, users should test thoroughly and monitor for any service updates or changes.

**Integration with Related Azure Services:**  
Soft Delete in Azure Compute Gallery complements Azure Backup and Azure Resource Manager’s (ARM) resource locks by providing a focused recovery mechanism for VM images. It integrates seamlessly with existing image versioning and replication capabilities, ensuring that soft delete states are respected across regional replications. Additionally, it aligns with Azure Policy and governance frameworks by enabling safer image lifecycle management within enterprise environments.

In summary, the Soft Delete feature in Azure Compute Gallery enhances image lifecycle management by introducing a recoverable deletion state with a 7-day retention window, thereby reducing operational risks associated with accidental deletions and improving overall service reliability for IT professionals managing VM images at scale.

---

### 2. Retirement: Support for Service Connector (preview) on Azure Container Apps will end on March 30th, 2026

**Published**: September 30, 2025 17:30:02 UTC
**Link**: [Retirement: Support for Service Connector (preview) on Azure Container Apps will end on March 30th, 2026](https://azure.microsoft.com/updates?id=501528)

**Update ID**: 501528
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Service Connector (preview) support on Azure Container Apps, effective March 30, 2026.

- Key changes or new features  
After March 30, 2026, Service Connector (preview) will no longer be supported or functional on Azure Container Apps. Users who have created service connections via the Azure Portal will need to plan for migration or alternative solutions before this date.

- Target audience affected  
Developers and IT professionals using Azure Container Apps with Service Connector (preview) to integrate and connect services will be impacted by this retirement.

- Important notes if any  
It is recommended to review existing service connections configured through the Azure Portal and begin transitioning to supported connectivity methods ahead of the retirement deadline to avoid disruption. No replacement or successor service connector feature was announced in this update. Users should monitor Azure updates for alternative integration options.

**Details**:

The announced retirement of support for Service Connector (preview) on Azure Container Apps, effective March 30, 2026, signifies Microsoft’s planned discontinuation of this feature to streamline and evolve the integration capabilities within Azure Container Apps. Service Connector (preview) was introduced to simplify the process of connecting Azure Container Apps to various Azure services by automating network and security configurations, thereby reducing manual setup complexity and accelerating development workflows.

**Background and Purpose:**  
Service Connector (preview) was designed as a low-code/no-code solution to enable seamless connectivity between containerized applications and Azure services such as Azure Database for PostgreSQL, Azure Cache for Redis, and Azure Event Hubs. The preview status indicated ongoing development and refinement based on user feedback. The retirement notice reflects Microsoft’s intent to phase out this preview feature, likely in favor of more robust, integrated, or evolved connectivity solutions within Azure Container Apps or other Azure networking services.

**Specific Features and Detailed Changes:**  
The key feature of Service Connector (preview) was its ability to automatically establish secure connections by configuring managed identities, virtual network integrations, and firewall rules without requiring extensive manual intervention. With the retirement, these automated connection capabilities via Service Connector (preview) will cease to be supported. Users who have created service connections through the Azure Portal using this feature will need to plan migration strategies before the cutoff date to avoid disruption.

**Technical Mechanisms and Implementation Methods:**  
Service Connector (preview) functioned by orchestrating underlying Azure resources and permissions: it leveraged Azure Managed Identities for authentication, configured virtual network service endpoints or private endpoints for secure connectivity, and adjusted firewall settings to permit traffic from Azure Container Apps to the target service. The implementation abstracted these complex configurations into a simplified UI-driven experience. Post-retirement, users will need to manually configure these components or use alternative automation mechanisms such as Azure CLI, ARM templates, or Terraform scripts to establish similar connectivity.

**Use Cases and Application Scenarios:**  
Typical use cases included microservices architectures deployed on Azure Container Apps that required secure, reliable access to backend services like databases, caches, or messaging systems. For example, a containerized web API connecting to Azure Database for PostgreSQL or an event-driven application consuming Azure Event Hubs would benefit from Service Connector’s automated setup. With the retirement, these scenarios remain valid but will require more hands-on configuration.

**Important Considerations and Limitations:**  
- Existing connections established via Service Connector (preview) will continue to function until March 30, 2026, but no new connections can be created post-retirement.  
- Users must audit their current container app deployments to identify dependencies on Service Connector (preview) and plan migration to supported connectivity methods well in advance.  
- Manual configuration of network security groups, private endpoints, and managed identities will be necessary to maintain secure and compliant connectivity.  
- The retirement does not affect Azure Container Apps as a service, only the preview Service Connector feature.

**Integration with Related Azure Services:**  
Service Connector (preview) tightly integrated with Azure networking constructs such as virtual networks, private endpoints, and Azure Active Directory managed identities. It also interfaced with Azure services like Azure Database for PostgreSQL, Azure Cache for Redis, Azure Event Hubs, and others to streamline connectivity. Post-retirement, users should leverage Azure Private Link, virtual network integration for Azure Container Apps, and Azure RBAC to manually replicate these integrations. Additionally, Azure DevOps or GitHub Actions can be used to automate deployment and configuration of these network and identity components.

In summary, the retirement of Service Connector (preview) on Azure Container Apps by March 30, 2026, requires IT professionals to transition from this automated preview feature to manual or alternative automated methods for securely connecting containerized applications to Azure services, ensuring continuity and security in their cloud-native architectures.

---

### 3. Retirement: NVv4-series Azure Virtual Machines will be retired on September 30, 2026

**Published**: September 30, 2025 17:15:32 UTC
**Link**: [Retirement: NVv4-series Azure Virtual Machines will be retired on September 30, 2026](https://azure.microsoft.com/updates?id=500578)

**Update ID**: 500578
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of the NVv4-series Azure Virtual Machines, effective September 30, 2026.

- Key changes or new features  
The following VM SKUs will be retired: Standard_NV4as_v4, Standard_NV4ahs_v4, Standard_NV8as_v4, Standard_NV8ahs_v4, Standard_NV16as_v4, Standard_NV16ahs_v4, Standard_NV32as_v4, and Standard_NV32ahs_v4. After the retirement date, these VM sizes will no longer be available for deployment or scaling.

- Target audience affected  
Developers and IT professionals currently using or planning to use NVv4-series VMs for GPU-accelerated workloads, including graphics-intensive applications, AI, and machine learning tasks, will be impacted.

- Important notes if any  
Users should plan to migrate workloads running on NVv4-series VMs to alternative VM families before the retirement date to avoid service disruption. Review current deployments and consider newer GPU-enabled VM options that offer improved performance and support. Microsoft recommends starting migration planning well in advance of September 2026. For more details, visit the official Azure update page: https://azure.microsoft.com/updates?id=500578

**Details**:

The NVv4-series Azure Virtual Machines, including Standard_NV4as_v4, Standard_NV4ahs_v4, Standard_NV8as_v4, Standard_NV8ahs_v4, Standard_NV16as_v4, Standard_NV16ahs_v4, Standard_NV32as_v4, and Standard_NV32ahs_v4, are scheduled for retirement on September 30, 2026. This planned decommissioning reflects Microsoft’s ongoing efforts to optimize its VM portfolio by phasing out older generation instances in favor of newer, more efficient, and higher-performing options.

**Background and Purpose**  
The NVv4-series VMs were introduced to provide GPU-accelerated compute capabilities tailored for graphics-intensive workloads, such as visualization, simulation, and remote workstation scenarios, leveraging AMD Radeon Instinct MI25 GPUs with AMD EPYC CPUs. Over time, advancements in GPU technology, VM architecture, and Azure infrastructure have led to the availability of newer VM series that offer improved performance, cost efficiency, and feature sets. The retirement aims to streamline the Azure VM offerings, reduce maintenance overhead, and encourage customers to migrate to more modern VM types that better meet current and future workload demands.

**Specific Features and Detailed Changes**  
The NVv4-series VMs uniquely combined AMD EPYC CPUs with AMD Radeon GPUs, supporting GPU partitioning via AMD’s Multiuser GPU (MxGPU) technology, enabling multiple users to share a single GPU securely and efficiently. These VMs supported a range of sizes from 4 to 32 vCPUs, with corresponding GPU resources, designed for workloads such as CAD, 3D rendering, and video editing.

With the retirement, these specific VM SKUs will no longer be available for provisioning or scaling after the cutoff date. Existing deployments must be migrated or decommissioned before September 30, 2026, to avoid service disruption.

**Technical Mechanisms and Implementation Methods**  
The NVv4-series leveraged AMD’s MxGPU technology implemented via SR-IOV (Single Root I/O Virtualization), allowing hardware-level GPU virtualization and secure multi-tenant GPU sharing. This differs from NVIDIA’s GRID technology used in other Azure GPU VMs. The retirement means that Azure’s backend infrastructure will cease support for these AMD GPU-based VMs, and the associated hardware will be phased out from Azure datacenters.

Migration paths typically involve moving workloads to newer GPU VM series, such as the NVv5-series or ND-series, which use NVIDIA GPUs and provide enhanced AI, HPC, and visualization capabilities. Migration may require application compatibility testing, driver updates, and possible reconfiguration of GPU-accelerated workloads.

**Use Cases and Application Scenarios**  
NVv4-series VMs were primarily used for remote visualization, virtual desktop infrastructure (VDI), engineering simulations, and graphics rendering workloads that benefit from GPU acceleration. Organizations running CAD applications, 3D modeling, or media processing pipelines leveraged these VMs for cost-effective GPU sharing.

Post-retirement, customers should evaluate newer VM families that align with their workload requirements, considering factors such as GPU architecture, driver support, performance benchmarks, and cost. For example, NVv5-series VMs provide AMD MI250 GPUs optimized for HPC and AI, while ND-series VMs focus on NVIDIA A100 GPUs for deep learning and HPC.

**Important Considerations and Limitations**  
- Customers must plan migration well in advance to avoid service interruptions.  
- Some legacy applications may require testing to ensure compatibility with newer GPU drivers and VM architectures.  
- Pricing and performance characteristics may differ significantly between NVv4-series and replacement VMs, necessitating cost-benefit analysis.  
- Azure does not support in-place upgrades between VM series; redeployment and data migration are required.  
- Backup and disaster recovery strategies should be updated to accommodate the new VM types.

**Integration with Related Azure Services**  
NVv4-series VMs integrate with Azure services such as Azure Virtual Desktop, Azure Batch, and

---

### 4. Retirement: Spark Native Connector for Semantic Link 

**Published**: September 30, 2025 13:45:49 UTC
**Link**: [Retirement: Spark Native Connector for Semantic Link ](https://azure.microsoft.com/updates?id=502602)

**Update ID**: 502602
**Data source**: Azure Updates API

**Categories**: Analytics, Microsoft Fabric, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of the Spark Native Connector for Semantic Link, effective October 1, 2025.

- Key changes or new features  
The connector will no longer be supported or maintained after the retirement date. This decision follows internal analysis showing low usage, high maintenance overhead, and potential security risks. Users are encouraged to transition to alternative integration methods or connectors that provide better support and security.

- Target audience affected  
Developers and IT professionals who currently use the Spark Native Connector for Semantic Link in their data processing or analytics workflows will be impacted. Those relying on this connector for integrating Spark workloads with Semantic Link services need to plan migration strategies.

- Important notes if any  
It is critical to begin evaluating and migrating existing workloads well before the retirement date to avoid disruptions. Microsoft recommends exploring other supported connectors or APIs that offer improved security and performance. Continued use of the retired connector beyond October 1, 2025, will not receive updates or security patches. For detailed migration guidance, refer to official Azure documentation and support channels.

**Details**:

The Azure update announces the official retirement of the Spark Native Connector for Semantic Link effective October 1, 2025. This decision follows an internal evaluation revealing minimal usage, disproportionate maintenance overhead, and identified security risks, prompting Microsoft to discontinue support and encourage migration to alternative solutions.

Background and Purpose:  
The Spark Native Connector for Semantic Link was designed to facilitate seamless integration between Apache Spark workloads and Semantic Link services, enabling data scientists and engineers to query and analyze semantic graph data directly within Spark environments. However, over time, usage metrics indicated that the connector did not achieve widespread adoption, while ongoing maintenance and security patching demands increased operational costs. The retirement aims to streamline Azure’s service portfolio, reduce security exposure, and focus resources on more robust and widely used integration methods.

Specific Features and Changes:  
The connector provided native Spark APIs and data source interfaces to connect Spark jobs with Semantic Link graph data stores, supporting read and write operations with optimized query translation. With retirement, the connector will no longer receive updates, bug fixes, or security patches after October 1, 2025, and will be formally deprecated before that date. Users will lose official support and should plan to transition workloads accordingly.

Technical Mechanisms and Implementation:  
The connector functioned as a Spark DataSource V2 implementation, translating Spark SQL queries into Semantic Link graph queries and managing data serialization/deserialization between Spark’s RDD/DataFrame abstractions and the Semantic Link graph format. It leveraged Spark’s Catalyst optimizer extensions to push down predicates and optimize query execution. Its retirement means these integration points will cease to be maintained, and users must adopt alternative integration methods such as REST APIs, SDKs, or custom connectors.

Use Cases and Application Scenarios:  
Primarily, the connector was used in scenarios where organizations performed large-scale semantic graph analytics within Spark clusters, such as knowledge graph enrichment, entity resolution, and relationship discovery in big data pipelines. It enabled data engineers to embed semantic querying directly into Spark ETL workflows. Post-retirement, these use cases will require re-architecting to use other integration approaches.

Important Considerations and Limitations:  
- Migration Planning: Organizations must audit existing workloads using the connector and plan migration well before the retirement date to avoid disruption.  
- Security: The retirement is partly driven by security vulnerabilities; continuing to use the connector beyond the support window poses risks.  
- Performance: Alternative integration methods may not match the native connector’s query pushdown optimizations, potentially impacting performance.  
- Compatibility: Future Spark versions may not support the connector, so compatibility issues will arise post-retirement.

Integration with Related Azure Services:  
Users are encouraged to leverage Azure-native alternatives such as Azure Synapse Analytics, Azure Data Factory, or Azure Cosmos DB’s graph APIs for semantic data processing. Additionally, integration via RESTful APIs or Azure SDKs can replace the connector’s functionality, providing more secure and maintainable access to Semantic Link data. Combining these services with Azure Databricks or HDInsight Spark clusters can replicate or enhance existing workflows without relying on the deprecated connector.

In summary, the retirement of the Spark Native Connector for Semantic Link reflects Microsoft’s strategic shift to optimize service offerings by discontinuing low-usage, high-maintenance components with security concerns. IT professionals should proactively assess and migrate their Spark-based semantic graph workloads to supported integration methods leveraging Azure’s broader data ecosystem to ensure continuity, security, and performance beyond October 2025.

---


*This report was automatically generated - 2025-10-01 03:02:25 UTC*