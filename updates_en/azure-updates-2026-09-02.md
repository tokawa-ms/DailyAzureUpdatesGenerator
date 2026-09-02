# September 02, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 02, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 9 items

## Update List

### 1. Generally Available: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)

**Published**: September 01, 2026 22:34:43 UTC
**Link**: [Generally Available: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)](https://azure.microsoft.com/updates?id=570282)

**Update ID**: 570282
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Container Apps, Feature

**Summary**:

- What was updated  
Microsoft Defender for Cloud now provides general availability support for Azure Container Apps within its Serverless Containers Posture management experience.

- Key changes or new features  
Security teams can now onboard Azure Container Apps environments into Microsoft Defender for Cloud. This integration enables unified security posture management for serverless containers alongside other container services. The update allows for consistent security policy enforcement, threat detection, and compliance monitoring across a broader range of containerized workloads from a single workflow.

- Target audience affected  
This update is relevant to security teams, IT professionals, and developers managing containerized workloads on Azure, especially those leveraging Azure Container Apps and responsible for cloud security posture management.

- Important notes if any  
Organizations can now extend their security and compliance coverage to Azure Container Apps without separate tools or workflows. This helps centralize visibility and management of container security risks. Existing Defender for Cloud customers can start onboarding Azure Container Apps environments immediately. For more details, refer to the official documentation and onboarding guidance.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)  
**Link:** [Microsoft Azure Update](https://azure.microsoft.com/updates?id=570282)

---

**Background and Purpose of the Update**  
Microsoft Defender for Cloud is a comprehensive security management solution for Azure resources, providing posture management, threat protection, and compliance monitoring. Azure Container Apps is a serverless container platform that enables developers to deploy microservices and containerized applications without managing infrastructure. Previously, Defender for Cloud’s serverless containers posture management did not natively support Azure Container Apps environments, limiting visibility and security controls for organizations using this service. The purpose of this update is to extend Defender for Cloud’s posture management capabilities to Azure Container Apps, allowing security teams to monitor and manage security across a broader container estate from a unified workflow.

**Specific Features and Detailed Changes**  
With this update, Azure Container Apps environments can now be onboarded into Microsoft Defender for Cloud’s Serverless Containers Posture experience. Key features include:
- **Unified Posture Management:** Security teams can assess, monitor, and manage the security posture of Azure Container Apps alongside other container resources from a single interface within Defender for Cloud.
- **Expanded Coverage:** The update increases the scope of Defender for Cloud’s container security, ensuring that serverless container workloads are included in posture assessments.
- **Workflow Integration:** The onboarding process and ongoing posture management are seamlessly integrated into Defender for Cloud’s existing workflows, reducing operational complexity.

**Technical Mechanisms and Implementation Methods**  
The integration leverages Defender for Cloud’s existing posture management framework, which includes continuous assessment of resource configurations, compliance checks, and security recommendations. Azure Container Apps environments are now recognized as supported resource types within this framework. Security teams can onboard Container Apps environments via the Defender for Cloud portal, enabling automated posture assessments and recommendations. The technical implementation relies on Azure-native APIs and resource management capabilities, ensuring that posture management is consistent with other container services supported by Defender for Cloud.

**Use Cases and Application Scenarios**  
- **Enterprise Security Posture Management:** Organizations deploying microservices or serverless container workloads using Azure Container Apps can now include these environments in their overall security posture assessments.
- **Compliance Monitoring:** Security teams can ensure that Azure Container Apps adhere to organizational and regulatory compliance requirements, leveraging Defender for Cloud’s compliance reporting features.
- **Centralized Security Operations:** IT professionals can manage security policies, detect misconfigurations, and receive actionable recommendations for Azure Container Apps without switching between multiple tools.

**Important Considerations and Limitations**  
- **Scope:** The update specifically targets Azure Container Apps environments; other container services may require separate onboarding or configuration.
- **Workflow Dependency:** Posture management for Container Apps is integrated into Defender for Cloud’s serverless containers workflow. Teams must ensure that their workflows are updated to include these new resource types.
- **Resource Visibility:** Only environments onboarded into Defender for Cloud will be included in posture assessments; manual onboarding may be required for existing Container Apps.

**Integration with Related Azure Services**  
- **Azure Container Apps:** Direct integration enables posture management for serverless container workloads.
- **Microsoft Defender for Cloud:** Provides the central platform for security posture management, threat detection, and compliance monitoring.
- **Azure Resource Management:** Utilizes Azure-native APIs for resource discovery and configuration assessment.
- **Compliance and Reporting Tools:** Defender for Cloud’s compliance features extend to Azure Container Apps, supporting regulatory and organizational requirements.

---

**Summary Sentence:**  
Microsoft Defender for Cloud now generally supports Azure Container Apps within its Serverless Containers Posture experience, enabling security teams to centrally manage and assess the security posture of serverless container workloads alongside other container resources from a unified workflow.

---

### 2. Generally Available: Windows Server 2025 on AKS

**Published**: September 01, 2026 22:31:50 UTC
**Link**: [Generally Available: Windows Server 2025 on AKS](https://azure.microsoft.com/updates?id=570090)

**Update ID**: 570090
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**Summary**:

- What was updated  
Windows Server 2025 is now generally available (GA) as a supported node pool operating system in Azure Kubernetes Service (AKS).

- Key changes or new features  
AKS users can now deploy and manage Windows Server 2025 node pools alongside existing Linux and Windows node pools. This enables support for the latest Windows container features, improved security, and lifecycle management. Windows Server 2025 images are fully integrated with AKS, supporting seamless upgrades and scaling operations.

- Target audience affected  
Developers and IT professionals managing Windows-based workloads on AKS, especially those planning migrations from older Windows Server versions (e.g., 2019, 2022) or looking to modernize their container infrastructure.

- Important notes if any  
Organizations should consider upgrading to Windows Server 2025 on AKS to stay ahead of end-of-support timelines for previous Windows Server versions. This update ensures continued security, compliance, and access to the latest Windows container innovations. Review compatibility of your applications with Windows Server 2025 before upgrading. For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=570090

**Details**:

**Azure Update Report: Generally Available – Windows Server 2025 on AKS**

**Background and Purpose of the Update**  
Organizations leveraging Azure Kubernetes Service (AKS) for Windows-based workloads are facing increasing urgency to modernize their infrastructure as support for older Windows Server versions nears retirement. This update addresses the need for continuity and modernization by making Windows Server 2025 support generally available (GA) on AKS. The purpose is to enable customers to transition their Windows container workloads to a supported, up-to-date platform, ensuring ongoing security, compliance, and performance.

**Specific Features and Detailed Changes**  
With this update, AKS now supports Windows Server 2025 node pools in production environments. This allows customers to create and manage AKS clusters with Windows Server 2025 as the underlying OS for their Windows container workloads. Key features include:

- Full lifecycle management of Windows Server 2025 node pools within AKS.
- Compatibility with Windows-based containers, leveraging the latest Windows Server 2025 features and improvements.
- Seamless integration of Windows Server 2025 nodes alongside Linux nodes in hybrid AKS clusters.

**Technical Mechanisms and Implementation Methods**  
AKS utilizes Azure’s managed Kubernetes platform to orchestrate containerized applications. With Windows Server 2025 GA support, AKS provisions VM-based node pools running Windows Server 2025 images. Customers can specify Windows Server 2025 as the OS version when creating or updating node pools via Azure CLI, ARM templates, or the Azure portal. The AKS control plane manages scheduling, scaling, and health monitoring for Windows Server 2025 nodes, ensuring consistent operation with Kubernetes standards.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations running legacy or modern Windows applications in containers, such as:

- Migrating legacy .NET Framework applications to AKS for improved scalability and management.
- Deploying enterprise workloads that require Windows-specific features, libraries, or APIs.
- Building hybrid clusters with both Linux and Windows workloads, optimizing resource utilization and operational efficiency.
- Preparing for end-of-support scenarios by moving workloads from older Windows Server versions to Windows Server 2025.

**Important Considerations and Limitations**  
Technical professionals should note the following:

- Only Windows container workloads are supported on Windows Server 2025 node pools; Linux containers must run on Linux node pools.
- Customers must ensure their container images are compatible with Windows Server 2025.
- There may be limitations in feature parity between Windows and Linux node pools, such as networking, storage, or certain Kubernetes features.
- Organizations should review AKS documentation for supported Kubernetes versions and Windows Server 2025 image availability in their region.

**Integration with Related Azure Services**  
Windows Server 2025 node pools on AKS integrate seamlessly with other Azure services, including:

- Azure Monitor for container health and performance metrics.
- Azure Policy for governance and compliance.
- Azure DevOps and GitHub Actions for CI/CD pipelines targeting Windows containers.
- Azure Active Directory for authentication and access control.

**Summary Sentence**  
Windows Server 2025 is now generally available for Azure Kubernetes Service, enabling organizations to modernize and secure their Windows container workloads with full support for production deployments.

---

### 3. Generally Available: Artifact Streaming on AKS

**Published**: September 01, 2026 22:30:59 UTC
**Link**: [Generally Available: Artifact Streaming on AKS](https://azure.microsoft.com/updates?id=570095)

**Update ID**: 570095
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Feature

**Summary**:

- What was updated  
Artifact Streaming is now generally available on Azure Kubernetes Service (AKS) when using Azure Container Registry (ACR).

- Key changes or new features  
Artifact Streaming enables container images to start running on AKS before the full image is pulled from ACR. This reduces startup latency for containerized workloads, allowing faster scaling and deployment. The feature optimizes image pull times, especially for large images, by streaming only the necessary layers on demand.

- Target audience affected  
Developers and IT professionals managing containerized applications on AKS, especially those deploying large or frequently updated container images from Azure Container Registry.

- Important notes if any  
To leverage Artifact Streaming, ensure your AKS clusters are configured to use ACR and that your workloads are compatible with streaming. This feature can significantly improve application startup times and cluster scaling performance. Review your security and compliance requirements, as image streaming changes the way images are delivered to nodes.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=570095)

**Details**:

**Azure Update Report: Artifact Streaming on AKS (Generally Available)**

**Background and Purpose of the Update**  
Azure Kubernetes Service (AKS) is widely used for orchestrating containerized workloads, and Azure Container Registry (ACR) serves as a secure repository for container images. Traditionally, when deploying containers to AKS, the full image must be pulled from ACR before the workload can start. This process can introduce latency, especially with large images or during rapid scaling events. The purpose of this update is to address these bottlenecks by introducing Artifact Streaming, enabling faster and more efficient workload startup and scaling.

**Specific Features and Detailed Changes**  
Artifact Streaming is now generally available for AKS when using ACR. This feature allows container images to be streamed directly to AKS nodes, enabling workloads to start before the entire image is downloaded. The primary change is the ability to begin container execution as soon as the essential layers are available, rather than waiting for the complete image pull. This accelerates deployment times and improves the responsiveness of scaling operations.

**Technical Mechanisms and Implementation Methods**  
Artifact Streaming leverages a layer-by-layer streaming mechanism. When a container is scheduled on AKS, the node begins pulling image layers from ACR. As soon as the initial layers required for container startup are available, the container runtime (such as containerd) initiates the container, while remaining layers continue to download in the background. This is achieved by integrating ACR’s streaming capabilities with AKS’s container runtime, optimizing the image pull process and reducing startup latency.

**Use Cases and Application Scenarios**  
- **Rapid Scaling:** Artifact Streaming is particularly beneficial in scenarios where workloads need to scale quickly, such as during sudden traffic spikes or batch processing jobs.  
- **Large Images:** Applications with large container images (e.g., machine learning workloads or applications with extensive dependencies) can start faster, improving overall system responsiveness.  
- **CI/CD Pipelines:** Artifact Streaming enhances deployment speed in continuous integration and continuous deployment workflows, allowing for faster testing and production rollouts.

**Important Considerations and Limitations**  
- Artifact Streaming is available only when using AKS in conjunction with ACR; other container registries are not supported for this feature.  
- The streaming process depends on the container runtime’s compatibility and the image’s layer structure.  
- While streaming accelerates startup, workloads that require layers not yet downloaded may experience delays if those layers are accessed during execution.  
- Proper image design (e.g., placing essential startup files in early layers) can maximize the benefits of streaming.

**Integration with Related Azure Services**  
Artifact Streaming is tightly integrated with Azure Container Registry and Azure Kubernetes Service. It enhances the workflow between these services by optimizing image delivery. This update does not require changes to existing AKS or ACR configurations, but users should ensure their AKS clusters are updated to the latest supported versions to leverage streaming. It complements other Azure DevOps and CI/CD tools by reducing deployment times and improving scalability.

**Summary Sentence**  
Artifact Streaming on AKS is now generally available, enabling faster container startup and improved scalability by allowing workloads to begin execution before full image downloads from Azure Container Registry are complete.

---

### 4. Generally Available: Confidential VMs for Azure Linux

**Published**: September 01, 2026 22:30:18 UTC
**Link**: [Generally Available: Confidential VMs for Azure Linux](https://azure.microsoft.com/updates?id=570100)

**Update ID**: 570100
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Feature

**Summary**:

- What was updated  
Confidential Virtual Machines (CVM) for Azure Linux in Azure Kubernetes Service (AKS) are now generally available.

- Key changes or new features  
Azure Linux node pools in AKS can now be deployed as Confidential VMs. This enables enhanced security and confidentiality for containerized workloads by leveraging hardware-based trusted execution environments. Developers and IT teams can migrate highly sensitive workloads to AKS with improved isolation and protection against unauthorized access, including from Azure operators.

- Target audience affected  
This update is relevant for developers, DevOps engineers, and IT professionals managing sensitive or regulated container workloads on AKS, especially those with compliance or data privacy requirements.

- Important notes if any  
Confidential VM support is specific to Azure Linux node pools in AKS. Workloads running on these nodes benefit from hardware-enforced isolation and memory encryption. Organizations can now confidently run confidential workloads in AKS, facilitating compliance with strict security standards. Review documentation for supported VM sizes and configuration steps before migration.  

Data source: Using API data  
Link: [Azure Update](https://azure.microsoft.com/updates?id=570100)

**Details**:

**Azure Update Report: Confidential VMs for Azure Linux Now Generally Available**

**Background and Purpose of the Update**  
This update announces the general availability of Confidential Virtual Machines (CVMs) for Azure Linux within Azure Kubernetes Service (AKS). The primary purpose is to provide enhanced security and confidentiality for tenants running highly sensitive container workloads. By enabling CVMs in AKS node pools, organizations can migrate sensitive workloads to AKS with increased assurance of data protection.

**Specific Features and Detailed Changes**  
- CVMs for Azure Linux are now generally available, moving from preview to production-ready status.
- AKS node pools can be configured to use CVMs, allowing containerized workloads to run on hardware-backed confidential computing environments.
- This feature specifically targets the migration of highly sensitive workloads, providing a secure execution environment for containers.

**Technical Mechanisms and Implementation Methods**  
- Confidential VMs leverage hardware-based Trusted Execution Environments (TEEs), such as AMD SEV-SNP or Intel SGX, to isolate workloads and protect data in use.
- In AKS, node pools can be provisioned with CVM-enabled VM sizes, ensuring that all containers in those node pools benefit from confidential computing protections.
- The implementation ensures that data is encrypted not only at rest and in transit, but also during processing, mitigating risks from unauthorized access, including from Azure operators.

**Use Cases and Application Scenarios**  
- Migration of workloads containing sensitive data, such as financial, healthcare, or regulated industry applications, to AKS.
- Running containerized workloads that require compliance with strict confidentiality and privacy requirements.
- Scenarios where organizations must ensure that data remains protected from access by cloud providers or other tenants.

**Important Considerations and Limitations**  
- Only node pools configured with CVMs will provide confidential computing protections; workloads running on standard VMs do not benefit from these enhancements.
- The update is specific to Azure Linux-based CVMs in AKS; other operating systems or environments may not be covered.
- Performance and compatibility considerations may apply when running workloads on CVMs, and organizations should validate their applications accordingly.
- The migration process should account for potential limitations in supported VM sizes and features when using CVMs.

**Integration with Related Azure Services**  
- CVMs for Azure Linux are integrated with AKS, allowing seamless orchestration and management of confidential workloads alongside standard workloads.
- Organizations can leverage Azure’s broader confidential computing ecosystem, including confidential containers and related security services, to build end-to-end secure solutions.
- The update enhances AKS’s capabilities for secure workload deployment, complementing existing Azure security features such as encryption, identity management, and compliance tools.

**Summary Sentence**  
Confidential Virtual Machines for Azure Linux in AKS are now generally available, enabling secure node pools for highly sensitive container workloads and providing robust confidentiality protections for organizations migrating critical applications to Azure Kubernetes Service.

---

### 5. Generally Available: Purchase order mapping available in Microsoft Marketplace 

**Published**: September 01, 2026 18:40:59 UTC
**Link**: [Generally Available: Purchase order mapping available in Microsoft Marketplace ](https://azure.microsoft.com/updates?id=569700)

**Update ID**: 569700
**Data source**: Azure Updates API

**Categories**: Launched, Feature

**Summary**:

- What was updated  
Purchase order mapping is now generally available for Microsoft Marketplace purchases.

- Key changes or new features  
Organizations can now map purchase orders (POs) to their Microsoft Marketplace transactions. This feature enables businesses to align their Marketplace purchases with internal accounting processes, making it easier to allocate and reconcile cloud and AI spending on Microsoft invoices. The update provides supplemental PO information on invoices, improving transparency and financial tracking.

- Target audience affected  
This update is relevant for IT professionals, finance teams, procurement departments, and developers who manage or track cloud spending via Microsoft Marketplace.

- Important notes if any  
Organizations can now streamline invoice reconciliation by associating Marketplace purchases with specific purchase orders. This helps ensure compliance with internal procurement policies and simplifies financial reporting. No additional configuration is required for existing Marketplace users; the feature is available immediately. For more details, refer to the official documentation.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Purchase order mapping available in Microsoft Marketplace  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=569700)

---

**Background and Purpose of the Update**  
This update introduces purchase order mapping functionality for Microsoft Marketplace transactions, now generally available. The primary purpose is to streamline the alignment of Marketplace purchases with organizational accounting requirements. By enabling purchase order mapping, IT and finance teams can more efficiently allocate Microsoft invoices—including those generated from Marketplace purchases—facilitating improved reconciliation of cloud and AI expenditures.

**Specific Features and Detailed Changes**  
The key feature of this update is the ability to map purchase orders (POs) directly to Marketplace purchases. This enhancement allows users to associate specific purchase orders with their Microsoft invoices, which include Marketplace transactions. The mapping process ensures that each Marketplace purchase is linked to the relevant PO, providing granular visibility and traceability for financial reporting and auditing purposes. The update supplements existing invoice management capabilities, offering additional metadata for each transaction.

**Technical Mechanisms and Implementation Methods**  
Purchase order mapping is implemented within the Microsoft Marketplace purchasing workflow. When making a purchase, users can input or select a purchase order number to associate with the transaction. This PO information is then captured and reflected in the resulting Microsoft invoice. The mapping data is stored and accessible through the invoice management interface, allowing for automated or manual reconciliation processes. Integration with backend accounting systems is facilitated by the inclusion of PO metadata in invoice exports, supporting downstream processing and reporting.

**Use Cases and Application Scenarios**  
- **Enterprise Financial Reconciliation:** Organizations can allocate cloud and AI Marketplace spend to specific cost centers or projects by mapping purchases to corresponding POs, simplifying reconciliation and budget tracking.
- **Audit and Compliance:** The ability to trace each Marketplace purchase to a purchase order enhances auditability and compliance with internal and external financial controls.
- **Procurement Workflow Integration:** IT and procurement teams can enforce PO requirements for Marketplace purchases, ensuring adherence to procurement policies and reducing manual tracking.
- **Multi-department Cloud Spend Management:** Businesses with multiple departments or teams can use PO mapping to attribute Marketplace purchases accurately, supporting chargeback and internal billing processes.

**Important Considerations and Limitations**  
- **Invoice Scope:** PO mapping applies specifically to Microsoft invoices that include Marketplace purchases; it may not extend to other types of Azure billing or third-party invoices.
- **Data Entry:** Accurate PO mapping depends on correct input during the purchase process; errors or omissions may impact reconciliation.
- **Integration:** While PO metadata is included in invoices, further integration with external accounting systems may require custom development or configuration.
- **Supplemental Information:** The update provides supplemental data for invoice allocation but does not alter the underlying billing or payment mechanisms.

**Integration with Related Azure Services**  
Purchase order mapping is tightly integrated with Microsoft Marketplace and Azure billing services. It enhances invoice management capabilities, supporting Azure Cost Management and Billing workflows. The mapped PO data can be leveraged in reporting tools and exported for integration with financial systems, complementing existing Azure spend tracking and management features.

---

**Summary Sentence:**  
Purchase order mapping for Microsoft Marketplace purchases is now generally available, enabling organizations to align cloud and AI spend with their accounting needs by associating purchase orders with invoices for improved reconciliation and financial reporting.

---

### 6. Generally Available: Azure Firewall auto-learn SNAT routes 

**Published**: September 01, 2026 17:10:38 UTC
**Link**: [Generally Available: Azure Firewall auto-learn SNAT routes ](https://azure.microsoft.com/updates?id=570474)

**Update ID**: 570474
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure Firewall, Features

**Summary**:

- What was updated  
Azure Firewall’s auto-learn SNAT routes feature is now generally available.

- Key changes or new features  
Azure Firewall can now automatically discover and learn registered and private destination prefixes on a periodic basis. These learned prefixes are automatically applied as No-SNAT ranges, which means the firewall will preserve the original source IP addresses for traffic to these destinations. This automation reduces the need for manual configuration of SNAT (Source Network Address Translation) rules and simplifies SNAT management.

- Target audience affected  
This update is relevant for network and security administrators, IT professionals managing Azure Firewall deployments, and developers responsible for network architecture in Azure environments.

- Important notes if any  
The auto-learn SNAT routes feature helps prevent unnecessary source IP translation for traffic destined to known private or registered prefixes, improving traceability and simplifying troubleshooting. It also reduces operational overhead by minimizing manual updates to SNAT configuration as network environments evolve. For more information and implementation details, refer to the official Azure Update documentation: https://azure.microsoft.com/updates?id=570474

**Details**:

**Azure Update Report: Azure Firewall Auto-Learn SNAT Routes (General Availability)**

**Background and Purpose of the Update:**  
Azure Firewall traditionally uses Source Network Address Translation (SNAT) to manage outbound connectivity, translating private IP addresses to public IPs. However, managing SNAT ranges—especially to preserve original source IPs for certain destinations—has required manual configuration. The purpose of this update is to automate the learning and application of SNAT routes, reducing administrative overhead and improving accuracy in SNAT management.

**Specific Features and Detailed Changes:**  
With this update, Azure Firewall now periodically and automatically learns both registered and private destination prefixes. These learned prefixes are then applied as No-SNAT ranges. This means that traffic destined for these prefixes will bypass SNAT, preserving the original source IP address. The feature eliminates the need for manual configuration of No-SNAT ranges, ensuring that the firewall dynamically adapts to changes in destination prefixes.

**Technical Mechanisms and Implementation Methods:**  
The auto-learn mechanism operates by scanning and identifying registered and private destination prefixes within the network environment. Azure Firewall updates its internal configuration to include these prefixes as No-SNAT ranges. The process is periodic, ensuring that any changes in network topology or new prefixes are automatically incorporated. The implementation leverages Azure’s native route discovery and management capabilities, integrating seamlessly with the firewall’s SNAT logic. When outbound traffic matches a learned prefix, the firewall applies No-SNAT, allowing the original source IP to be retained.

**Use Cases and Application Scenarios:**  
This feature is particularly beneficial in scenarios where the original source IP must be preserved for compliance, auditing, or application requirements. For example:
- Communication with internal Azure resources or private endpoints where source IP preservation is necessary for access control or logging.
- Hybrid cloud environments where on-premises systems require visibility of Azure VM source IPs.
- Multi-tier applications where backend systems rely on source IP for session management or security policies.

**Important Considerations and Limitations:**  
IT professionals should note that the auto-learn feature is limited to registered and private destination prefixes. Public IP destinations will continue to use SNAT as usual. The periodic learning process may introduce a slight delay in updating No-SNAT ranges when new prefixes are added. Administrators should monitor and verify that critical prefixes are correctly identified and included in No-SNAT ranges. Additionally, reliance on auto-learn does not eliminate the need for occasional manual review, especially in complex network environments.

**Integration with Related Azure Services:**  
Azure Firewall’s auto-learn SNAT routes feature integrates with Azure’s networking stack, including Virtual Networks, Private Endpoints, and Route Tables. It enhances interoperability with services that require source IP preservation, such as Azure Private Link, Azure Bastion, and custom internal applications. The feature works transparently with other Azure Firewall capabilities, such as threat intelligence and logging, ensuring consistent operation across the security perimeter.

**Summary Sentence:**  
Azure Firewall’s auto-learn SNAT routes feature, now generally available, automates the identification and application of No-SNAT ranges for registered and private destination prefixes, streamlining SNAT management and preserving original source IPs for improved operational efficiency and compliance.

---

### 7. Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans

**Published**: September 01, 2026 16:31:14 UTC
**Link**: [Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans](https://azure.microsoft.com/updates?id=570250)

**Update ID**: 570250
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Azure Copilot, Feature

**Summary**:

- What was updated  
Azure Copilot Observability Agent in Azure Monitor is now generally available with support for Log Analytics data in Basic and Auxiliary table plans.

- Key changes or new features  
The agent now enables interactive analysis and deep investigations of telemetry stored in both Basic and Auxiliary tables. This allows teams to use Azure Copilot’s AI-powered operational capabilities across a broader range of Log Analytics data, including high-volume, cost-optimized telemetry that is typically stored outside standard tables.

- Target audience affected  
Developers, IT professionals, and operations teams using Azure Monitor and Log Analytics, especially those managing large-scale telemetry and cost-sensitive data retention strategies.

- Important notes if any  
This update allows organizations to leverage Azure Copilot’s advanced troubleshooting and analysis features on more cost-effective storage options (Basic and Auxiliary tables), improving coverage and reducing costs for high-volume telemetry scenarios. Teams can now perform AI-assisted investigations on data that was previously less accessible, streamlining root cause analysis and operational insights. No changes are required to existing data pipelines; the agent automatically supports these table types.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure Copilot Observability Agent supports Basic and Auxiliary table plans

**Background and Purpose of the Update:**  
Azure Monitor is a comprehensive platform for collecting, analyzing, and acting on telemetry from cloud and on-premises environments. The Azure Copilot Observability Agent is an AI-powered operational companion designed to enhance Azure Monitor’s capabilities, particularly in terms of interactive analysis and deep investigations. This update addresses the need for broader data coverage by enabling support for Log Analytics data stored in Basic and Auxiliary table plans, which are commonly used for high-volume telemetry and cost-effective data retention.

**Specific Features and Detailed Changes:**  
With this update, the Azure Copilot Observability Agent now supports Log Analytics data in both Basic and Auxiliary table plans. Previously, Copilot’s observability features may have been limited to standard tables, but now teams can leverage Copilot’s AI-driven insights and operational assistance across a wider range of data storage options. This includes the ability to analyze and investigate telemetry data that is stored in Basic tables (optimized for cost and high-volume ingestion) and Auxiliary tables (used for storing supplementary data such as diagnostic logs or custom telemetry).

**Technical Mechanisms and Implementation Methods:**  
The Copilot Observability Agent integrates directly with Azure Monitor’s Log Analytics workspace. It utilizes AI models to interpret and analyze telemetry data, providing interactive analysis and deep investigation capabilities. With this update, the agent’s data ingestion and processing pipeline has been extended to recognize and work with Basic and Auxiliary table schemas. This ensures that queries, anomaly detection, and operational recommendations can now be applied to data stored in these table plans, without requiring migration to standard tables.

**Use Cases and Application Scenarios:**  
- **High-Volume Telemetry Analysis:** Teams ingesting large volumes of telemetry (such as application logs, infrastructure metrics, or diagnostic data) into Basic tables can now use Copilot to perform interactive analysis and investigations, benefiting from AI-powered insights without incurring higher storage costs.
- **Cost-Optimized Monitoring:** Organizations utilizing Auxiliary tables for supplementary or archival telemetry can leverage Copilot for operational troubleshooting and root cause analysis, even on data that is not stored in premium table plans.
- **Incident Response and Deep Investigation:** During incidents, engineers can use Copilot to rapidly analyze both primary and auxiliary telemetry sources, improving response times and diagnostic accuracy.

**Important Considerations and Limitations:**  
- The update specifically covers Log Analytics data in Basic and Auxiliary table plans; it does not mention support for other data types or storage mechanisms.
- Teams should ensure that their Log Analytics workspace is configured to utilize Basic and Auxiliary tables as intended, and that data retention policies align with operational requirements.
- The AI-powered features of Copilot may be subject to limitations based on the schema and data quality in Basic and Auxiliary tables.

**Integration with Related Azure Services:**  
The Copilot Observability Agent is tightly integrated with Azure Monitor and Log Analytics. It enhances the operational value of telemetry data stored in Basic and Auxiliary tables by providing AI-driven analysis. This update allows seamless use of Copilot’s features alongside other Azure Monitor tools, such as alerting, dashboards, and workbooks, ensuring a unified observability experience across diverse data storage plans.

**Summary Sentence:**  
Azure Copilot Observability Agent is now generally available with support for Log Analytics data in Basic and Auxiliary table plans, enabling AI-powered interactive analysis and deep investigations for high-volume and cost-optimized telemetry within Azure Monitor.

---

### 8. Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions

**Published**: September 01, 2026 16:29:24 UTC
**Link**: [Generally Available: Azure Monitor Auxiliary Logs Plan in Azure Government and China regions](https://azure.microsoft.com/updates?id=569899)

**Update ID**: 569899
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Features

**Summary**:

- What was updated  
Azure Monitor Auxiliary Logs Plan is now generally available in Azure Government (Fairfax) and China regions.

- Key changes or new features  
The Auxiliary table plan in Azure Monitor Logs offers a cost-effective solution for ingesting and retaining high-volume, verbose logs, particularly for compliance and auditing purposes. This plan is now fully supported in sovereign cloud environments, enabling organizations in these regions to leverage the same scalable log management capabilities previously available in public Azure.

- Target audience affected  
This update is relevant to IT professionals, security teams, and developers managing workloads in Azure Government and China regions, especially those with compliance, auditing, or regulatory requirements that generate large volumes of log data.

- Important notes if any  
Organizations operating in Azure Government (Fairfax) and China can now use the Auxiliary Logs plan to optimize log storage costs and meet compliance needs. The plan is designed for logs that are high in volume but low in query frequency, making it suitable for audit and compliance scenarios. Review your log ingestion and retention strategies to take advantage of potential cost savings.  

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=569899

**Details**:

**Azure Update Report: Generally Available – Azure Monitor Auxiliary Logs Plan in Azure Government and China Regions**

**Background and Purpose of the Update**  
Azure Monitor Logs is a core component of Azure’s observability stack, enabling organizations to collect, analyze, and act on telemetry data from their cloud resources. High-volume, verbose logs—often required for compliance and auditing—can lead to substantial ingestion and retention costs. The Auxiliary table plan was introduced as a cost-effective solution for managing such logs. This update announces the general availability (GA) of the Auxiliary Logs plan in sovereign cloud environments: Azure Government (Fairfax) and China regions, extending this cost optimization capability to customers with strict compliance and data residency requirements.

**Specific Features and Detailed Changes**  
- **Auxiliary Table Plan Availability**: The Auxiliary Logs plan is now generally available in Azure Government (Fairfax) and China regions.
- **Cost Optimization**: The plan is specifically designed for high-volume, verbose logs, offering a more economical ingestion and retention model compared to standard Log Analytics tables.
- **Compliance and Auditing Focus**: The plan targets logs that are primarily used for compliance and auditing purposes, which typically require long-term retention but are infrequently queried.

**Technical Mechanisms and Implementation Methods**  
- **Table Plan Structure**: The Auxiliary table plan operates as a distinct log ingestion and storage tier within Azure Monitor Logs. Data ingested into auxiliary tables is subject to different pricing and retention policies, optimized for large volumes and lower query frequencies.
- **Ingestion and Retention**: Organizations can configure specific log sources to route data into auxiliary tables, ensuring that verbose logs do not impact the cost structure of more frequently queried operational data.
- **Access and Querying**: While the data is retained for compliance, it remains accessible for auditing and investigation, albeit with potential differences in query performance or features compared to standard tables.

**Use Cases and Application Scenarios**  
- **Regulatory Compliance**: Organizations in regulated industries (e.g., government, finance, healthcare) can use the Auxiliary Logs plan to store logs required for legal or regulatory retention periods.
- **Audit Trail Maintenance**: IT departments can route verbose diagnostic or audit logs into auxiliary tables, ensuring long-term availability for investigations or compliance checks.
- **Cost Management**: Enterprises with large-scale deployments generating significant log volumes can leverage the plan to control costs without sacrificing retention.

**Important Considerations and Limitations**  
- **Region Availability**: The plan is currently GA only in Azure Government (Fairfax) and China regions; it may not be available in all sovereign or commercial Azure regions.
- **Intended Use**: The Auxiliary Logs plan is optimized for logs that are infrequently queried but require long-term retention. It may not be suitable for operational logs that require frequent analysis or real-time monitoring.
- **Pricing and Performance**: While cost-effective for storage, there may be differences in query performance or feature set compared to standard Log Analytics tables. Users should review Azure documentation for detailed pricing and technical constraints.

**Integration with Related Azure Services**  
- **Azure Monitor**: The Auxiliary Logs plan is fully integrated with Azure Monitor, allowing seamless data ingestion and management alongside other monitoring and observability data.
- **Compliance Solutions**: The plan supports integration with compliance and auditing workflows, enabling organizations to meet regulatory requirements within the Azure ecosystem.
- **Log Analytics**: Data in auxiliary tables can be queried using familiar Log Analytics tools and interfaces, supporting unified monitoring and investigation workflows.

**Summary Sentence**  
The Azure Monitor Auxiliary Logs plan is now generally available in Azure Government (Fairfax) and China regions, providing a cost-effective solution for ingesting and retaining high-volume, verbose logs required for compliance and auditing in sovereign cloud environments.

---

### 9. Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching

**Published**: September 01, 2026 16:25:33 UTC
**Link**: [Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching](https://azure.microsoft.com/updates?id=569904)

**Update ID**: 569904
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Features

**Summary**:

- **What was updated:**  
Azure Monitor Auxiliary Logs Plan now supports Azure tables and allows plan switching, both features are generally available.

- **Key changes or new features:**  
  - You can now use the Auxiliary Logs Plan with Azure Monitor Logs tables, providing a cost-effective option for storing high-volume, verbose logs (e.g., compliance and auditing data) that are rarely queried.
  - Plan switching is supported: you can move existing tables between the Auxiliary plan and other available plans as your requirements change, without data loss or service interruption.

- **Target audience affected:**  
  - Developers and IT professionals managing Azure Monitor Logs, especially those handling large volumes of log data for compliance, auditing, or regulatory purposes.
  - Organizations seeking to optimize log storage costs while maintaining required data retention.

- **Important notes:**  
  - The Auxiliary plan is designed for logs that require long-term retention but are infrequently queried, offering a lower-cost alternative to standard log ingestion and retention.
  - Plan switching provides flexibility to adjust storage and cost strategies as log usage patterns evolve.
  - Review your current log tables and consider migrating suitable tables to the Auxiliary plan to reduce costs.

[More details](https://azure.microsoft.com/updates?id=569904)

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure Monitor Auxiliary Logs Plan support for Azure tables and plan switching  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=569904)

---

**Background and Purpose of the Update**  
Azure Monitor Logs is a core component in Azure for collecting, analyzing, and retaining log data from various resources. Many organizations generate high-volume, verbose logs—such as audit and compliance logs—that are infrequently queried but must be retained for regulatory purposes. The Auxiliary table plan was introduced to address the need for cost-effective log ingestion and retention for such scenarios. This update responds to customer demand for expanded support and flexibility in managing these logs.

**Specific Features and Detailed Changes**  
This update introduces two generally available capabilities:

1. **Azure Tables Support:** The Auxiliary table plan now supports Azure tables, enabling customers to ingest and retain logs within Azure Monitor using the cost-effective Auxiliary plan. This is particularly useful for logs that are stored in Azure tables and require long-term retention but are rarely accessed.
   
2. **Plan Switching:** Customers can now switch between log ingestion plans for their tables in Azure Monitor. This means that organizations can move their log tables between standard and auxiliary plans as their requirements change, providing greater flexibility in cost management and log retention strategies.

**Technical Mechanisms and Implementation Methods**  
- **Auxiliary Table Plan:** The Auxiliary plan is designed for tables with high ingestion volumes and low query frequency. It optimizes storage costs by reducing the price for ingesting and retaining logs, while limiting query performance and frequency.
- **Plan Switching:** Administrators can now change the ingestion plan for a given table directly within Azure Monitor. This is managed through the Azure Portal or via Azure Resource Manager APIs, allowing for seamless transitions between plans without data loss or manual migration.

**Use Cases and Application Scenarios**  
- **Compliance and Auditing:** Organizations required to retain logs for compliance can use the Auxiliary plan for audit trails, security logs, or access logs that are rarely queried but must be stored for extended periods.
- **Cost Optimization:** IT teams managing large volumes of diagnostic or verbose logs can leverage the Auxiliary plan to reduce storage and ingestion costs, especially for logs that are not actively used for operational monitoring.
- **Dynamic Retention Management:** The ability to switch plans allows teams to adapt their log management strategies as needs evolve, such as moving logs to the Auxiliary plan after their operational relevance decreases.

**Important Considerations and Limitations**  
- **Query Performance:** The Auxiliary plan is optimized for retention and ingestion, not for frequent querying. Logs stored under this plan may have reduced query performance and may not be suitable for operational analytics.
- **Plan Switching Impact:** Switching plans may affect cost, retention policies, and query availability. IT professionals should review the implications before migrating tables between plans.
- **Supported Tables:** Only Azure tables are supported for these features; other log types may not be eligible for the Auxiliary plan or plan switching.

**Integration with Related Azure Services**  
- **Azure Monitor:** The Auxiliary plan and plan switching are integrated within Azure Monitor’s log management framework, enabling seamless use alongside standard log analytics and monitoring features.
- **Azure Resource Manager:** Plan switching can be automated or managed programmatically using Azure Resource Manager APIs, supporting integration with infrastructure-as-code workflows.

---

**Summary Sentence:**  
Azure Monitor now generally supports the Auxiliary Logs Plan for Azure tables and enables plan switching, providing IT professionals with cost-effective log retention options and flexible management for high-volume, compliance-focused logs.

---


*This report was automatically generated - 2026-09-02 03:06:02 UTC*