# February 06, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: February 06, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Private Preview: Vaulted Backups for Azure Disk 

**Published**: February 06, 2026 23:00:02 UTC
**Link**: [Private Preview: Vaulted Backups for Azure Disk ](https://azure.microsoft.com/updates?id=555184)

**Update ID**: 555184
**Data source**: Azure Updates API

**Categories**: In development, Management and governance, Storage, Azure Backup, Features

**Summary**:

- What was updated  
Azure has announced the Private Preview of Vaulted Backups for Azure Disk.

- Key changes or new features  
Vaulted Backups introduce a new backup tier for Azure Disks, enabling backups to be stored in an Azure Backup vault, separate from the source subscription and resource group. This is in addition to the existing Operational Tier, which stores crash-consistent snapshots in the same subscription. Vaulted Backups provide enhanced data protection, long-term retention, and improved security by isolating backup data from the source environment.

- Target audience affected  
Developers and IT professionals responsible for managing Azure Disk data protection, backup, and disaster recovery strategies.

- Important notes if any  
Vaulted Backups are currently available in Private Preview and require registration for access. This feature is particularly relevant for organizations with strict compliance, security, or retention requirements, as it enables offsite, isolated backup storage. Existing backup workflows using the Operational Tier remain unchanged; Vaulted Backups are an additional option for enhanced protection. For more details and to request access, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=555184).

**Details**:

**Comprehensive Technical Explanation: Private Preview – Vaulted Backups for Azure Disk**

**Background and Purpose of the Update**  
Azure Disk Backup currently offers protection for Azure Managed Disks by creating regular, crash-consistent snapshots. These snapshots are stored within the same subscription and tenant, in a resource group known as the Operational Tier. While this approach provides fast, local recovery, it does not address scenarios requiring long-term retention, offsite protection, or compliance with regulatory requirements for data immutability and isolation. The introduction of "Vaulted Backups for Azure Disk" in Private Preview aims to bridge this gap by enabling the backup of Azure Disks to Azure Recovery Services Vaults, thus providing an additional layer of data protection and retention capabilities.

**Specific Features and Detailed Changes**  
- **Vaulted Backup Capability:** Azure Disks can now be backed up to Recovery Services Vaults, moving beyond just local snapshots. This enables long-term retention, offsite storage, and enhanced data durability.
- **Policy-Based Backup Management:** IT professionals can define backup policies for Azure Disks, specifying backup frequency and retention periods, similar to how VM or SQL backups are managed in Azure Backup.
- **Immutable Backups:** Vaulted backups support immutability, preventing accidental or malicious deletion or modification of backup data.
- **Centralized Management:** All disk backups can be managed and monitored centrally from the Recovery Services Vault, streamlining operations and compliance reporting.

**Technical Mechanisms and Implementation Methods**  
- **Snapshot to Vault Workflow:** The backup process first creates a crash-consistent snapshot of the Azure Disk (Operational Tier). This snapshot is then transferred to the Recovery Services Vault (Vaulted Tier), leveraging Azure Backup’s secure and scalable infrastructure.
- **Data Movement and Storage:** Data is stored in the Recovery Services Vault, which is geo-redundant by default, ensuring offsite protection. The vault abstracts the underlying storage, providing a secure, managed backup repository.
- **Backup and Restore Operations:** Backups can be triggered on-demand or scheduled via policies. Restores can be performed by selecting the desired recovery point from the vault, which then rehydrates the disk to a specified state.

**Use Cases and Application Scenarios**  
- **Long-Term Retention:** Organizations needing to retain disk backups for months or years for compliance or archival purposes.
- **Disaster Recovery:** Vaulted backups provide an additional layer of protection against accidental deletion, ransomware, or regional outages.
- **Regulatory Compliance:** Industries with strict data retention and immutability requirements (e.g., finance, healthcare) can leverage this feature for audit-ready backup management.
- **Operational Recovery:** Enables recovery of disks to a previous state in case of logical corruption or application errors.

**Important Considerations and Limitations**  
- **Private Preview:** The feature is currently in Private Preview, which may limit availability and support for certain regions or disk types.
- **Supported Disk Types:** Initially, only specific disk types and sizes may be supported; check the official documentation for up-to-date compatibility.
- **Cost Implications:** Vaulted backups incur additional storage and operation costs compared to standard snapshots. Review Azure Backup pricing for Recovery Services Vaults.
- **Backup and Restore Performance:** Vaulted backups may have higher latency for backup and restore operations compared to local snapshots, due to data movement to/from the vault.

**Integration with Related Azure Services**  
- **Azure Backup:** Deep integration with Azure Backup and Recovery Services Vaults, leveraging existing policy, monitoring, and security features.
- **Azure Policy and RBAC:** Supports integration with Azure Policy for compliance enforcement and Azure Role-Based Access Control (RBAC) for granular access management.
- **Monitoring and Alerts:** Backup jobs, health, and alerts can be monitored through Azure Monitor and the Backup center.

**Summary Sentence:**  
Vaulted Backups for Azure Disk, now in Private Preview, extends Azure Disk Backup capabilities by enabling policy-driven, immutable, long-term

---

### 2. Public Preview: Azure Monitor pipeline transformations 

**Published**: February 06, 2026 22:45:47 UTC
**Link**: [Public Preview: Azure Monitor pipeline transformations ](https://azure.microsoft.com/updates?id=555488)

**Update ID**: 555488
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor, Security, Features

**Summary**:

- What was updated  
Azure Monitor pipeline transformations feature is now in Public Preview.

- Key changes or new features  
This new feature allows users to transform and filter telemetry data before it is ingested into Azure Monitor. Users can shape incoming data using transformation rules, which helps reduce unnecessary data ingestion, control associated costs, improve data quality, and streamline analytics workflows. Transformations can be applied to telemetry from sources such as Application Insights and Log Analytics.

- Target audience affected  
Developers and IT professionals who manage telemetry data collection, monitoring, and analytics in Azure environments. This includes teams responsible for application monitoring, cost management, and operational analytics.

- Important notes if any  
Using pipeline transformations can significantly reduce ingestion costs by filtering out unneeded data before it reaches Azure Monitor. It also enables better data governance and can simplify downstream analytics by ensuring only relevant, high-quality data is stored. The feature is currently in Public Preview, so it may not yet be suitable for production workloads. Review the official documentation for limitations and best practices during the preview phase.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=555488

**Details**:

**Azure Monitor Pipeline Transformations Public Preview – Technical Explanation**

**Background and Purpose of the Update:**  
Azure Monitor is a comprehensive platform for collecting, analyzing, and acting on telemetry from cloud and on-premises environments. As organizations scale their cloud workloads, the volume of telemetry data (logs, metrics, traces) grows rapidly, leading to increased ingestion costs and challenges in managing data quality and relevance. Previously, all telemetry sent to Azure Monitor was ingested as-is, requiring post-ingestion processing and sometimes resulting in unnecessary data storage and costs. The new pipeline transformations feature addresses these challenges by allowing users to preprocess and shape telemetry data before it is ingested, optimizing both cost and operational efficiency.

**Specific Features and Detailed Changes:**  
The pipeline transformations feature introduces the ability to define transformation rules for telemetry streams as they flow into Azure Monitor. Key capabilities include:
- **Data Shaping:** Users can filter, enrich, or modify telemetry records based on custom logic.
- **Pre-Ingestion Processing:** Transformations are applied before data is stored, enabling cost savings by reducing unnecessary data ingestion.
- **Rule-Based Configuration:** Transformations are defined declaratively using configuration files or the Azure portal, specifying which data streams and conditions to apply.
- **Preview Scope:** The feature is currently in Public Preview, meaning it is available for testing and feedback but not yet recommended for production-critical workloads.

**Technical Mechanisms and Implementation Methods:**  
Pipeline transformations leverage a rules engine that operates on telemetry streams (such as logs, metrics, or traces) as they are sent to Azure Monitor. The transformation logic is typically expressed in a domain-specific language (DSL) or configuration syntax, allowing users to:
- **Filter:** Drop records that do not meet specified criteria (e.g., severity, source, or custom attributes).
- **Enrich:** Add or modify fields in telemetry records, such as tagging with environment or application metadata.
- **Aggregate or Mask:** Summarize data or redact sensitive information before ingestion.
Transformations are applied at the data collection pipeline level, ensuring only relevant and compliant data is ingested.

**Use Cases and Application Scenarios:**  
- **Cost Optimization:** Exclude verbose or low-value logs (e.g., debug-level traces) from ingestion to reduce Azure Monitor costs.
- **Data Quality Improvement:** Standardize telemetry formats or enrich records with additional context for more effective querying and alerting.
- **Compliance and Security:** Remove or mask sensitive information (e.g., PII) before data is stored in Azure Monitor.
- **Operational Efficiency:** Simplify downstream analytics by ensuring only relevant and well-structured data is available.

**Important Considerations and Limitations:**  
- **Preview Limitations:** As a Public Preview feature, pipeline transformations may not support all data types or integration scenarios and are not covered by Azure SLAs.
- **Performance Impact:** Complex transformation logic may introduce latency in data processing.
- **Rule Management:** Careful management of transformation rules is required to avoid unintentional data loss or compliance issues.
- **Monitoring and Auditing:** Users should monitor transformation outcomes to ensure data integrity and compliance with organizational policies.

**Integration with Related Azure Services:**  
Pipeline transformations are designed to work seamlessly with Azure Monitor and its associated data sources, including Azure Log Analytics, Application Insights, and custom telemetry pipelines. They can be configured alongside data collection rules (DCRs) and integrated with Azure Policy for governance. This feature complements other data management tools such as Azure Data Explorer and Azure Sentinel, enabling more efficient and secure telemetry workflows across the Azure ecosystem.

**Summary:**  
The Azure Monitor pipeline transformations feature (Public Preview) empowers organizations to preprocess and optimize telemetry data before ingestion, enabling cost control, improved data quality, and streamlined analytics within Azure Monitor.

---

### 3. ​Generally Available: Claude Opus 4.6 now available on Azure Databricks

**Published**: February 06, 2026 19:00:01 UTC
**Link**: [​Generally Available: Claude Opus 4.6 now available on Azure Databricks](https://azure.microsoft.com/updates?id=555981)

**Update ID**: 555981
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Analytics, Azure Databricks, Features

**Summary**:

- What was updated  
Claude Opus 4.6, Anthropic’s most advanced large language model, is now generally available on Azure Databricks via Mosaic AI Model Serving.

- Key changes or new features  
Azure Databricks users can now access and deploy Claude Opus 4.6 for their AI workloads. This model offers state-of-the-art capabilities in agentic coding, complex reasoning, and advanced knowledge work. Integration with Mosaic AI Model Serving enables seamless API-based access, allowing developers to incorporate Claude Opus 4.6 into data pipelines, applications, and analytics workflows.

- Target audience affected  
This update is relevant for data scientists, machine learning engineers, AI developers, and IT professionals using Azure Databricks who require advanced generative AI models for coding assistance, reasoning tasks, or knowledge-intensive applications.

- Important notes if any  
To leverage Claude Opus 4.6, ensure your Databricks workspace is configured for Mosaic AI Model Serving. Review Anthropic’s usage guidelines and pricing. The model’s advanced capabilities may require updated prompt engineering strategies for optimal results. For more information, refer to the official Azure update: https://azure.microsoft.com/updates?id=555981

**Details**:

**Generally Available: Claude Opus 4.6 now available on Azure Databricks**

**Background and Purpose of the Update:**  
This update introduces Anthropic’s Claude Opus 4.6, the latest and most advanced large language model (LLM) from Anthropic, to Azure Databricks via Mosaic AI Model Serving. The purpose is to provide Azure Databricks users with access to state-of-the-art generative AI capabilities, enabling advanced agentic coding, complex reasoning, and sophisticated knowledge work directly within their data and AI workflows. This aligns with the growing demand for enterprise-grade, secure, and scalable AI model integration within cloud-based analytics and machine learning platforms.

**Specific Features and Detailed Changes:**  
- **Model Availability:** Claude Opus 4.6 is now generally available as a managed endpoint in Azure Databricks through Mosaic AI Model Serving.
- **Performance:** The model offers leading performance in tasks such as code generation, multi-step reasoning, summarization, and question answering.
- **Integration:** Users can invoke Claude Opus 4.6 directly from Databricks notebooks, jobs, and workflows, leveraging the familiar Databricks environment.
- **Security and Compliance:** The model is served within the Azure Databricks environment, ensuring enterprise-grade security, compliance, and data privacy.

**Technical Mechanisms and Implementation Methods:**  
- **Mosaic AI Model Serving:** Azure Databricks uses Mosaic AI Model Serving to host and manage the Claude Opus 4.6 model. This service abstracts the complexities of model deployment, scaling, and endpoint management.
- **API Access:** Users interact with the model via RESTful API endpoints, which can be called from Python, Scala, or SQL within Databricks notebooks or jobs.
- **Authentication and Access Control:** Access to the model is governed by Azure Active Directory (AAD) and Databricks’ workspace-level permissions, ensuring secure and auditable usage.
- **Resource Management:** The underlying infrastructure automatically scales based on request volume, optimizing cost and performance.

**Use Cases and Application Scenarios:**  
- **Agentic Coding:** Automate code generation, code review, and refactoring tasks, accelerating software development lifecycles.
- **Complex Reasoning:** Enable advanced analytics, hypothesis generation, and decision support in domains such as finance, healthcare, and research.
- **Knowledge Work:** Enhance productivity in summarization, report generation, and knowledge extraction from large unstructured datasets.
- **Conversational AI:** Build intelligent chatbots and virtual assistants that require nuanced understanding and context retention.

**Important Considerations and Limitations:**  
- **Model Costs:** Usage of Claude Opus 4.6 may incur additional costs based on the number of tokens processed and the compute resources consumed.
- **Data Residency:** While the model is served within Azure, ensure that your data residency and compliance requirements are met.
- **Model Limitations:** As with all LLMs, outputs may occasionally be inaccurate or hallucinated; human oversight is recommended for critical tasks.
- **Versioning:** The update specifically refers to Claude Opus 4.6; future versions may require separate enablement or migration.

**Integration with Related Azure Services:**  
- **Azure Databricks:** Seamless integration with Databricks notebooks, workflows, and ML pipelines.
- **Azure Data Lake and Storage:** Process and analyze data stored in Azure Data Lake or Blob Storage, using Claude Opus 4.6 for enrichment or summarization.
- **Azure Machine Learning:** Combine with Azure ML for custom model orchestration, evaluation, and deployment.
- **Azure Security and Monitoring:** Leverage Azure Monitor and Defender for monitoring, logging, and securing AI workloads.

**Summary:**  
Claude Opus 4.6 is now generally available on Azure Databricks, offering advanced generative AI capabilities through Mosaic AI Model Serving for secure, scalable, and enterprise-ready integration into data and AI workflows.

---

### 4. Private Preview: New planned datacenter region in Thailand (Thailand South)

**Published**: February 06, 2026 19:00:01 UTC
**Link**: [Private Preview: New planned datacenter region in Thailand (Thailand South)](https://azure.microsoft.com/updates?id=553999)

**Update ID**: 553999
**Data source**: Azure Updates API

**Categories**: In development, Regions & Datacenters

**Summary**:

- What was updated  
Microsoft announced the planned establishment of a new Azure datacenter region in Thailand (Thailand South), currently in private preview.

- Key changes or new features  
The new region will provide access to Microsoft’s hyperscale cloud services, enhancing local availability, enterprise-grade reliability, and performance for customers in Thailand. This expansion supports data residency, compliance, and disaster recovery requirements, and will enable customers to deploy Azure services closer to their users and data sources.

- Target audience affected  
Developers, IT professionals, and organizations operating in or serving customers in Thailand, especially those with strict data residency, compliance, or latency requirements.

- Important notes if any  
The Thailand South region is in private preview; general availability timelines have not been announced. Interested customers should monitor Azure updates for further details on access and service availability. Early engagement may be possible for select customers with specific needs. This expansion aligns with Microsoft’s ongoing investment in global cloud infrastructure and regional compliance.

**Details**:

**Azure Update Technical Explanation: Private Preview – New Planned Datacenter Region in Thailand (Thailand South)**

---

**Background and Purpose of the Update**

Microsoft has announced its intent to establish a new Azure datacenter region in Thailand, specifically named "Thailand South." This initiative is part of Microsoft’s ongoing global expansion strategy to enhance the reach of its hyperscale cloud infrastructure. The primary purpose is to address the growing demand for cloud services in Southeast Asia, enabling local organizations to leverage Azure’s enterprise-grade reliability, performance, and compliance capabilities. This move supports digital transformation, data residency requirements, and regulatory compliance for businesses operating in or serving the Thai market.

---

**Specific Features and Detailed Changes**

- **New Regional Presence:** The Thailand South region will provide a local Azure presence, reducing latency for customers and partners in Thailand.
- **Service Availability:** Upon launch, the region is expected to offer core Azure services such as compute (VMs, App Services), storage, networking, and databases, with additional services rolled out over time.
- **Data Residency:** Customers will have the option to store data within Thailand, addressing data sovereignty and compliance needs.
- **High Availability:** The region will be designed with multiple Availability Zones, supporting high availability and disaster recovery scenarios.

---

**Technical Mechanisms and Implementation Methods**

- **Hyperscale Architecture:** The new region will utilize Microsoft’s hyperscale datacenter design, featuring modular infrastructure, advanced cooling, and energy efficiency.
- **Networking:** Integration with Microsoft’s global backbone network will ensure secure, high-speed connectivity between Thailand South and other Azure regions.
- **Compliance and Security:** The region will adhere to Microsoft’s global security and compliance standards, including ISO, SOC, and GDPR frameworks, with additional local certifications as required.
- **Resource Management:** IT professionals will be able to select "Thailand South" as a deployment region in the Azure Portal, CLI, and ARM templates once the region is generally available.

---

**Use Cases and Application Scenarios**

- **Regulated Industries:** Financial services, healthcare, and government organizations can deploy workloads in-country to meet regulatory and data residency requirements.
- **Low-Latency Applications:** Enterprises and ISVs can deliver latency-sensitive applications (e.g., real-time analytics, IoT, gaming) to end-users in Thailand.
- **Business Continuity:** Organizations can architect multi-region solutions for disaster recovery, leveraging Thailand South alongside other Asia-Pacific regions.
- **Hybrid and Multicloud:** Customers using Azure Arc or hybrid cloud architectures can extend their on-premises environments to the new region for greater flexibility.

---

**Important Considerations and Limitations**

- **Private Preview Status:** The region is currently in private preview; access is limited and subject to Microsoft’s invitation and approval process.
- **Service Rollout:** Not all Azure services will be available at launch; customers should verify service availability for their workloads.
- **Pricing and SLAs:** Regional pricing and service-level agreements (SLAs) will be published closer to general availability.
- **Migration Planning:** Existing customers planning to migrate workloads should assess network connectivity, data transfer costs, and compliance impacts.

---

**Integration with Related Azure Services**

- **Azure Active Directory:** Seamless integration for identity and access management across global and regional resources.
- **Azure ExpressRoute:** Customers can establish private, high-speed connections to the new region for hybrid scenarios.
- **Azure Site Recovery and Backup:** Enhanced disaster recovery and backup options within Thailand for business continuity.
- **Azure Monitor and Security Center:** Unified monitoring, security, and compliance management across the new and existing regions.

---

**Summary:**  
Microsoft’s planned Thailand South datacenter region will provide local access to Azure’s hyperscale cloud services, supporting data residency, regulatory compliance, and low-latency application delivery for organizations in Thailand.

---

### 5. Generally Available: AMD v6 confidential VMs in new regions for January 2026

**Published**: February 06, 2026 01:00:02 UTC
**Link**: [Generally Available: AMD v6 confidential VMs in new regions for January 2026](https://azure.microsoft.com/updates?id=553966)

**Update ID**: 553966
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines, Regions & Datacenters

**Summary**:

- What was updated  
The AMD-based DCa/ECa v6 confidential virtual machines (VMs) are now generally available in 11 additional Azure regions as of January 2026.

- Key changes or new features  
The DCa/ECa v6 series VMs, which leverage AMD hardware-based confidential computing, are now available in the following regions: Canada Central, Canada East, Norway East, Norway West, Italy North, Germany North, France South, Australia East, West US, West US 3, and Germany West Central. These VMs provide enhanced data protection using hardware-enforced isolation for sensitive workloads.

- Target audience affected  
This update is relevant for developers and IT professionals who require confidential computing capabilities for their applications, especially those handling sensitive data or operating in regulated industries. Organizations with compliance requirements or those deploying workloads across multiple regions will benefit from the expanded regional availability.

- Important notes if any  
The expansion allows for greater flexibility in deploying confidential workloads closer to end-users or within specific compliance boundaries. Developers should review regional availability when planning deployments. For optimal use, ensure applications are designed to leverage confidential computing features. Existing pricing and VM size options apply in the new regions. For more details, refer to the official Azure documentation.

**Details**:

**Azure Update Report: General Availability of AMD v6 Confidential VMs in New Regions (January 2026)**

**Background and Purpose of the Update**  
Confidential computing is a critical requirement for organizations handling sensitive data, as it provides hardware-based protection for data in use. Azure’s DCa/ECa v6 series confidential virtual machines (VMs), powered by AMD EPYC™ processors with Secure Encrypted Virtualization-Secure Nested Paging (SEV-SNP), enable customers to run workloads with enhanced security and privacy. The expansion of these VM series to 11 new regions (Canada Central, Canada East, Norway East, Norway West, Italy North, Germany North, France South, Australia East, West US, West US 3, Germany West Central) addresses growing customer demand for confidential computing capabilities closer to their data residency and compliance requirements.

**Specific Features and Detailed Changes**  
- **VM Series**: The DCa/ECa v6 series are based on AMD EPYC™ 3rd Gen processors, supporting confidential computing.
- **Confidential Computing**: These VMs provide memory encryption using AMD SEV-SNP, isolating VM memory from the hypervisor and other VMs.
- **Regional Expansion**: Previously limited to select regions, these VMs are now generally available in 11 additional Azure regions, improving global coverage and enabling more customers to deploy confidential workloads in compliance with local regulations.

**Technical Mechanisms and Implementation Methods**  
- **AMD SEV-SNP**: This hardware feature encrypts VM memory with unique keys managed by the AMD Secure Processor, ensuring that data is protected even from Azure operators and the hypervisor.
- **Attestation**: Azure provides attestation services to verify the integrity of the VM and the underlying hardware before sensitive workloads are executed.
- **Integration with Azure Resource Manager**: These VMs can be provisioned and managed using standard Azure tools (ARM templates, CLI, PowerShell), with confidential computing features enabled via VM configuration settings.

**Use Cases and Application Scenarios**  
- **Regulated Industries**: Financial services, healthcare, and government organizations can process sensitive data in the cloud while maintaining compliance with strict regulatory requirements.
- **Multi-Party Computation**: Scenarios where multiple organizations need to collaborate on data analysis without exposing raw data to each other.
- **Intellectual Property Protection**: Running proprietary algorithms and code in a confidential VM ensures that intellectual property remains protected from cloud operators and other tenants.

**Important Considerations and Limitations**  
- **Supported OS and Workloads**: Not all operating systems and workloads are compatible with confidential VMs. Customers should verify application compatibility and test workloads before production deployment.
- **Performance Overhead**: Memory encryption and attestation may introduce some performance overhead compared to standard VMs.
- **Feature Parity**: Certain Azure features (e.g., nested virtualization, GPU acceleration) may not be available or may have limited support in confidential VMs.
- **Pricing**: Confidential VMs may have different pricing compared to standard VM series due to the additional security features.

**Integration with Related Azure Services**  
- **Azure Key Vault**: Can be used to manage and control access to cryptographic keys and secrets used by applications running in confidential VMs.
- **Azure Attestation**: Provides remote attestation capabilities to verify the trustworthiness of the VM environment.
- **Azure Policy and Security Center**: Integration allows organizations to enforce and monitor compliance with confidential computing requirements across their Azure estate.

**Summary Sentence**  
The general availability of AMD v6 confidential VMs in 11 new Azure regions enables organizations to deploy highly secure, hardware-encrypted workloads globally, supporting compliance and data residency needs for sensitive and regulated applications.

---


*This report was automatically generated - 2026-02-15 16:58:11 UTC*