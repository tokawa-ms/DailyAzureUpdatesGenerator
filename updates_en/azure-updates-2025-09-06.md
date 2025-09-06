# September 06, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 06, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Generally Available: Azure Red Hat OpenShift Now Available in UAE Central and US Gov Texas 

**Published**: September 05, 2025 21:15:48 UTC
**Link**: [Generally Available: Azure Red Hat OpenShift Now Available in UAE Central and US Gov Texas ](https://azure.microsoft.com/updates?id=500520)

**Update ID**: 500520
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Red Hat OpenShift, Features, Security

**Summary**:

- What was updated  
Azure Red Hat OpenShift (ARO) is now generally available in two additional Azure regions: UAE Central and US Gov Texas.

- Key changes or new features  
This expansion delivers fully managed, enterprise-grade OpenShift clusters closer to customers in the Middle East and the southwestern United States. It enables organizations to deploy containerized applications with integrated Kubernetes and Red Hat OpenShift services locally, improving latency, compliance, and data residency. The availability in US Gov Texas also supports government customers requiring sovereign cloud environments.

- Target audience affected  
Developers and IT professionals working with containerized applications, Kubernetes, and hybrid cloud deployments in the Middle East and US government sectors will benefit. Enterprises needing compliant, managed OpenShift services in these regions can now leverage ARO with local data residency and support.

- Important notes if any  
Customers should consider regional compliance and latency improvements when planning deployments. The US Gov Texas region availability addresses specific government compliance and security requirements. Existing ARO features and integrations remain consistent with other regions, ensuring a seamless experience.

**Details**:

The recent general availability of Azure Red Hat OpenShift (ARO) in the UAE Central and US Gov Texas regions marks a significant expansion of Microsoft’s managed Kubernetes service tailored for enterprise OpenShift workloads, enabling customers in the Middle East and US government sectors to deploy containerized applications with enhanced compliance, performance, and regional data residency.

**Background and Purpose**  
Azure Red Hat OpenShift is a jointly managed service by Microsoft and Red Hat that delivers a fully managed OpenShift container platform on Azure. OpenShift itself is a Kubernetes distribution optimized for developer productivity and enterprise security. The purpose of this update is to extend ARO’s regional footprint to UAE Central and US Gov Texas, addressing critical needs for data sovereignty, low latency, and regulatory compliance in these geographies. This expansion supports customers in government, defense, and regulated industries who require cloud services within specific sovereign boundaries.

**Specific Features and Detailed Changes**  
With ARO now generally available in these two regions, customers gain access to the same enterprise-grade features as in other Azure regions, including:  
- Fully managed OpenShift clusters with automated patching, upgrades, and monitoring.  
- Integrated Red Hat Enterprise Linux CoreOS nodes optimized for container workloads.  
- Native Kubernetes API compatibility with OpenShift’s developer and operational tools.  
- Enterprise security features such as role-based access control (RBAC), network policies, and integrated identity management via Azure Active Directory (AAD).  
- Support for hybrid and multi-cloud scenarios through OpenShift’s operators and Azure Arc integration.  

The key change is the physical availability of these services within the new regions, ensuring data residency and compliance with local regulations such as UAE’s data protection laws and US government FedRAMP and DoD requirements.

**Technical Mechanisms and Implementation Methods**  
ARO clusters in these regions are deployed on Azure infrastructure that meets regional compliance standards, including isolated network zones and government-grade security controls in US Gov Texas. The service automates cluster lifecycle management using Azure Resource Manager (ARM) templates and APIs, enabling declarative provisioning of OpenShift clusters with customizable node pools and networking configurations. Integration with Azure Monitor and Log Analytics provides observability, while Azure Policy can enforce governance controls. The underlying OpenShift control plane is managed by Microsoft and Red Hat, abstracting operational complexity from customers.

**Use Cases and Application Scenarios**  
- Government agencies in the US can deploy secure, compliant containerized applications with guaranteed data residency in US Gov Texas, supporting mission-critical workloads with stringent security requirements.  
- Enterprises in the Middle East can leverage ARO in UAE Central to reduce latency for regional users and comply with local data sovereignty laws, facilitating digital transformation initiatives such as smart city applications, financial services modernization, and IoT deployments.  
- ISVs and developers targeting regulated industries can build and deploy cloud-native applications on a consistent OpenShift platform across global and sovereign clouds.  

**Important Considerations and Limitations**  
- Customers must ensure that their workloads and data comply with the specific regulatory requirements of each region.  
- Some Azure services and third-party integrations may have limited availability or require additional configuration in sovereign or government clouds.  
- Pricing and SLA terms may differ slightly in these regions due to the specialized infrastructure and compliance overhead.  
- Network latency and throughput should be evaluated when integrating with other Azure services outside the region.  

**Integration with Related Azure Services**  
ARO seamlessly integrates with Azure services such as Azure Active Directory for identity and access management, Azure Monitor for observability, Azure DevOps and GitHub Actions for CI/CD pipelines, and Azure Container Registry for container image storage. In US Gov Texas, ARO supports integration with Azure Government services, ensuring compliance with FedRAMP High and DoD SRG requirements. Additionally, customers can use Azure Arc to extend management and governance of OpenShift clusters across hybrid environments.

In summary, the general availability of Azure Red Hat OpenShift in UAE Central and US Gov Texas empowers organizations in these regions to deploy secure, compliant, and fully

---

### 2. Generally Available: Azure NetApp Files migration assistant

**Published**: September 05, 2025 16:45:57 UTC
**Link**: [Generally Available: Azure NetApp Files migration assistant](https://azure.microsoft.com/updates?id=502607)

**Update ID**: 502607
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure NetApp Files, Features

**Summary**:

- What was updated  
Azure NetApp Files (ANF) migration assistant is now generally available, enabling streamlined data migration to ANF using SnapMirror replication technology.

- Key changes or new features  
The migration assistant leverages NetApp ONTAP’s native SnapMirror engine to provide efficient, reliable, and cost-effective data replication from on-premises ONTAP systems, Cloud Volumes ONTAP (CVO), or other cloud providers directly into Azure NetApp Files. This facilitates near-zero downtime migrations and simplifies the transition process by automating replication setup and monitoring.

- Target audience affected  
Developers, IT administrators, and cloud architects responsible for migrating enterprise file workloads to Azure NetApp Files will benefit from this tool. It is especially relevant for those managing large-scale data migrations requiring high availability and minimal disruption.

- Important notes if any  
Users should ensure compatibility of their source ONTAP versions with SnapMirror replication and plan network bandwidth accordingly to optimize migration speed. This tool enhances migration efficiency but requires familiarity with ONTAP management and Azure NetApp Files configurations. For detailed guidance, refer to the official Azure update link.

**Details**:

The Azure NetApp Files migration assistant, now generally available, leverages NetApp ONTAP’s native SnapMirror replication technology to enable efficient, reliable, and cost-effective data migration from on-premises NetApp storage systems, Cloud Volumes ONTAP (CVO), or other cloud providers directly into Azure NetApp Files (ANF). This update addresses the critical need for enterprises to seamlessly transition large-scale file-based workloads to Azure while minimizing downtime and operational complexity.

**Background and Purpose:**  
Enterprises increasingly adopt Azure NetApp Files for its high-performance, enterprise-grade file storage capabilities integrated natively within Azure. However, migrating existing data from on-premises NetApp arrays or other cloud environments to ANF has traditionally involved complex, manual, and time-consuming processes. The migration assistant simplifies this by automating and orchestrating data replication using SnapMirror, NetApp’s proven asynchronous replication technology, ensuring data consistency and integrity during migration.

**Specific Features and Changes:**  
- **SnapMirror-based Replication:** The core feature is the use of SnapMirror to replicate data snapshots incrementally from source ONTAP systems to ANF volumes, reducing bandwidth usage and migration windows.  
- **Support for Multiple Sources:** Supports migration from on-premises NetApp ONTAP systems, Cloud Volumes ONTAP (NetApp’s software-defined storage in the cloud), and other cloud providers that run ONTAP.  
- **Automated Migration Workflow:** The assistant provides a guided, automated workflow to configure replication relationships, monitor progress, and perform cutover with minimal manual intervention.  
- **Cost Efficiency:** By leveraging incremental replication and snapshot technology, the solution minimizes data transfer costs and reduces the need for extended dual-write periods.  
- **Seamless Cutover:** Enables near-zero downtime cutover by synchronizing data until the final switchover, ensuring application continuity.

**Technical Mechanisms and Implementation:**  
The migration assistant configures SnapMirror relationships between the source ONTAP system and the target ANF volumes. SnapMirror uses snapshot-based incremental replication, initially transferring a baseline snapshot and subsequently replicating only changed data blocks. The process involves:  
1. Establishing network connectivity and authentication between source and ANF.  
2. Creating destination volumes in ANF matching source volume configurations.  
3. Initiating baseline snapshot transfer followed by incremental updates.  
4. Monitoring replication health and progress via the assistant’s interface.  
5. Performing a final synchronization and cutover to switch production workloads to ANF.  

This approach leverages ONTAP’s native data management capabilities, ensuring data consistency and reducing manual scripting or third-party tool dependencies.

**Use Cases and Application Scenarios:**  
- **Data Center Migration:** Enterprises moving file shares from on-premises NetApp arrays to Azure to modernize infrastructure or retire legacy data centers.  
- **Cloud Migration:** Organizations transitioning workloads from other cloud providers’ ONTAP-based storage to Azure for consolidation or cost optimization.  
- **Disaster Recovery Setup:** Establishing ANF as a DR target with initial data seeding via SnapMirror.  
- **Hybrid Cloud Workflows:** Incrementally migrating data while maintaining dual access during phased cloud adoption.

**Important Considerations and Limitations:**  
- **Source System Requirements:** Source storage must be ONTAP-based (physical or Cloud Volumes ONTAP) to support SnapMirror replication. Non-ONTAP systems are not supported.  
- **Network Configuration:** Requires appropriate network connectivity and firewall configurations between source and Azure environments to enable SnapMirror traffic.  
- **Volume Compatibility:** Destination ANF volumes must be sized and configured to match source volumes, including protocol support (NFS/SMB).  
- **Migration Window:** While incremental replication reduces downtime, a final cutover window is still required for synchronization and switching workloads.  
- **Cost Implications:** Data transfer and ANF consumption costs apply; planning for bandwidth and storage sizing is necessary.

**

---

### 3. Retirement: Azure CDN will be retired on December 1 2025 in China

**Published**: September 05, 2025 15:45:50 UTC
**Link**: [Retirement: Azure CDN will be retired on December 1 2025 in China](https://azure.microsoft.com/updates?id=501678)

**Update ID**: 501678
**Data source**: Azure Updates API

**Categories**: Media, Networking, Web, Content Delivery Network, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of Azure CDN services in China, effective December 1, 2025.

- Key changes or new features  
Azure CDN in China will no longer be available after the retirement date. Customers currently using Azure CDN in China must migrate their content delivery workloads to Azure Front Door or alternative solutions before the deadline to ensure uninterrupted service.

- Target audience affected  
Developers and IT professionals managing content delivery and web performance optimization for applications hosted in China using Azure CDN.

- Important notes if any  
Microsoft emphasizes proactive migration to avoid service disruption. Support and guidance will be provided during the transition period. It is critical to plan and execute migration well ahead of the December 1, 2025 deadline to maintain service continuity. For detailed migration guidance, refer to official Azure documentation and support channels.

**Details**:

The announced retirement of Azure CDN in China, effective December 1, 2025, reflects Microsoft’s strategic shift to consolidate and enhance content delivery capabilities within the region by encouraging migration to Azure Front Door, ensuring improved performance, security, and unified management for customers operating in China.

**Background and Purpose of the Update:**  
Azure CDN has historically provided content delivery network services to accelerate web content and media delivery by caching data at edge locations closer to end users. However, due to evolving network infrastructure, regulatory requirements, and the need for more integrated security and application acceleration features, Microsoft is retiring Azure CDN in China. This move aims to streamline offerings and direct customers toward Azure Front Door, which offers a more comprehensive, modern, and globally consistent application delivery platform with advanced Layer 7 routing, web application firewall (WAF), and DDoS protection capabilities.

**Specific Features and Detailed Changes:**  
The retirement means that after December 1, 2025, Azure CDN endpoints in China will no longer be supported or available. Customers must migrate their CDN workloads to Azure Front Door for China regions. Azure Front Door provides global HTTP/HTTPS load balancing, SSL offloading, URL-based routing, session affinity, and integrated security features. Unlike Azure CDN, which primarily focuses on caching and content acceleration, Azure Front Door combines CDN capabilities with application layer routing and security, offering a unified platform.

**Technical Mechanisms and Implementation Methods:**  
Migration involves reconfiguring your content delivery endpoints from Azure CDN to Azure Front Door. This includes:  
- Creating Azure Front Door profiles and endpoints in the China region.  
- Configuring backend pools pointing to your origin servers or storage accounts.  
- Setting routing rules to manage traffic distribution and caching policies.  
- Implementing WAF policies if applicable for enhanced security.  
- Updating DNS records to point to the new Azure Front Door endpoint.  

Azure Front Door uses Anycast IP addresses and edge POPs distributed globally, including China, to deliver low-latency content delivery and application acceleration. It supports HTTP/2, TLS 1.3, and integrates with Azure Monitor for diagnostics and analytics.

**Use Cases and Application Scenarios:**  
Typical use cases include:  
- Accelerating static and dynamic web content delivery for websites and applications serving users in China.  
- Protecting web applications with integrated WAF and DDoS protection.  
- Load balancing traffic across multiple backend services or regions within China.  
- Implementing URL-based routing for microservices architectures or multi-tenant applications.  
- Enabling SSL offloading and session affinity for secure and performant user experiences.  

Organizations with compliance requirements in China benefit from Azure Front Door’s regional presence and compliance certifications.

**Important Considerations and Limitations:**  
- Migration requires careful planning to avoid downtime; DNS TTL values should be lowered in advance.  
- Azure Front Door pricing differs from Azure CDN; cost implications should be evaluated.  
- Some CDN-specific features may not have direct equivalents in Azure Front Door; review feature parity.  
- Azure Front Door’s configuration and management differ from Azure CDN; teams may need training.  
- Ensure compliance with China-specific regulatory requirements when configuring endpoints and data routing.  
- Legacy CDN custom rules or third-party integrations may require re-implementation.  

**Integration with Related Azure Services:**  
Azure Front Door integrates seamlessly with Azure Monitor for telemetry, Azure Security Center for threat detection, Azure Active Directory for identity-based access controls, and Azure Traffic Manager for global traffic distribution. It also works well with Azure Blob Storage, Azure App Service, and Azure Kubernetes Service as backend origins, enabling comprehensive application delivery and security solutions.

In summary, the retirement of Azure CDN in China by December 1, 2025, mandates migration to Azure Front Door, which offers a more advanced, secure, and integrated platform for content delivery and application acceleration tailored for the China region. IT professionals should plan their migration strategy carefully, leveraging Azure Front Door’s rich feature

---

### 4. Public Preview: Azure Functions support for Python 3.13 

**Published**: September 05, 2025 15:15:38 UTC
**Link**: [Public Preview: Azure Functions support for Python 3.13 ](https://azure.microsoft.com/updates?id=501970)

**Update ID**: 501970
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Features

**Summary**:

- What was updated  
Azure Functions now supports Python 3.13 in public preview, enabling developers to build and deploy functions using the latest Python runtime.

- Key changes or new features  
1. Python 3.13 runtime support for Azure Functions, allowing use of new language features and improvements.  
2. Introduction of runtime version control for Python functions—a new opt-in feature that lets developers specify and target exact Python runtime versions within Azure Functions, improving compatibility and deployment consistency.

- Target audience affected  
Developers building serverless applications with Azure Functions using Python, and IT professionals managing Azure Functions environments who need precise runtime versioning and compatibility control.

- Important notes if any  
This feature is currently in public preview, so it should be used with caution in production environments. Developers must opt-in to enable runtime version control. Local development environments should be updated to Python 3.13 to ensure compatibility before deployment.  

For more details, visit: https://azure.microsoft.com/updates?id=501970

**Details**:

The recent Azure Functions update introduces public preview support for Python 3.13, enabling developers to build and deploy serverless functions using the latest Python runtime locally and in Azure. This update also debuts runtime version control for Python functions, an opt-in feature allowing precise targeting of specific Python runtime versions within the Azure Functions environment.

**Background and Purpose:**  
Azure Functions has long supported Python as a first-class language for serverless computing, but rapid Python language evolution necessitates timely runtime updates to leverage new language features, performance improvements, and security patches. Python 3.13, being the latest stable release, brings enhancements that developers want to utilize in their cloud functions. The update aims to keep Azure Functions aligned with Python’s release cadence, improve developer experience, and provide greater control over runtime environments to reduce compatibility issues.

**Specific Features and Detailed Changes:**  
- **Python 3.13 Runtime Support:** Developers can now author Azure Functions locally using Python 3.13, test them end-to-end, and deploy seamlessly to Azure. This ensures access to new language features such as pattern matching enhancements, performance optimizations, and standard library updates.  
- **Runtime Version Control (Opt-in):** This new feature allows specifying the exact Python runtime version for Azure Functions, mitigating risks of unexpected breaking changes from automatic runtime upgrades. Developers can pin their functions to Python 3.13.x or other supported versions, ensuring consistent behavior across development, testing, and production environments.  
- **Local Development Tooling:** Azure Functions Core Tools and the Azure Functions extension for Visual Studio Code have been updated to support Python 3.13, enabling local debugging and deployment workflows with the new runtime.

**Technical Mechanisms and Implementation Methods:**  
Azure Functions runtime now includes container images and language workers compatible with Python 3.13. When runtime version control is enabled, the Functions host uses the specified Python interpreter version to initialize the Python worker process. This is managed via configuration settings in the function app’s application settings (e.g., `FUNCTIONS_PYTHON_VERSION` or a similar environment variable). The runtime isolates Python dependencies using virtual environments or container layers, ensuring that the selected Python version and packages coexist without conflict. Local development environments must have Python 3.13 installed to fully leverage the new runtime.

**Use Cases and Application Scenarios:**  
- **Modern Python Features:** Applications requiring Python 3.13 features such as improved error messages, new syntax constructs, or updated standard libraries can now migrate their Azure Functions workloads without waiting for general availability.  
- **Performance-Sensitive Serverless Apps:** Python 3.13 includes optimizations that can reduce cold start times and execution latency, benefiting event-driven microservices, data processing pipelines, and real-time APIs.  
- **Version-Sensitive Deployments:** Enterprises with strict compliance or testing requirements can lock function apps to a specific Python runtime version, avoiding unexpected runtime changes during critical operations.  
- **Hybrid Development Environments:** Teams developing locally on Python 3.13 can maintain parity with cloud runtimes, simplifying CI/CD pipelines and reducing “works on my machine” issues.

**Important Considerations and Limitations:**  
- **Preview Status:** As a public preview, Python 3.13 support and runtime version control may have limited SLA guarantees and could undergo breaking changes before GA. Production workloads should evaluate stability carefully.  
- **Dependency Compatibility:** Some third-party Python packages may not yet fully support Python 3.13, requiring thorough testing of function dependencies.  
- **Runtime Version Control Opt-in:** This feature is not enabled by default; developers must explicitly configure their function apps to use it.  
- **Local Environment Requirements:** Developers must install Python 3.13 locally to develop and test functions using this runtime version.  
- **Azure Regions:** Availability of Python 3.13 runtime may initially be limited to select Azure regions.

**Integration with Related Azure Services:**  
- **Azure Functions Core Tools & VS Code

---

### 5. Public Preview: .NET 10 Preview Now Available on Azure App Service

**Published**: September 05, 2025 14:15:34 UTC
**Link**: [Public Preview: .NET 10 Preview Now Available on Azure App Service](https://azure.microsoft.com/updates?id=501896)

**Update ID**: 501896
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Mobile, Web, App Service, Features, Services

**Summary**:

- What was updated  
Azure App Service now supports the public preview of .NET 10 on both Windows and Linux environments.

- Key changes or new features  
Developers can deploy and run applications built with the latest .NET 10 preview, including modern ASP.NET web apps, Blazor projects, and Minimal APIs. This enables early testing and experimentation with new .NET 10 features directly on a fully managed platform. The update simplifies the development workflow by integrating cutting-edge .NET capabilities without manual environment setup.

- Target audience affected  
.NET developers building web applications, Blazor developers, and IT professionals managing Azure App Service environments who want to evaluate or adopt .NET 10 features early.

- Important notes if any  
This is a public preview release, so it is recommended for testing and development purposes rather than production workloads. Users should monitor for updates and potential breaking changes as .NET 10 evolves. For more details and to get started, visit the official Azure update page.

**Details**:

The recent Azure update announces the public preview availability of .NET 10 Preview on Azure App Service for both Windows and Linux environments, enabling developers to build, test, and deploy applications using the latest .NET runtime and SDK enhancements within a fully managed platform-as-a-service (PaaS) environment.

**Background and Purpose:**  
.NET 10 represents the latest evolution of the .NET platform, introducing performance improvements, new language features, and expanded APIs that streamline modern application development. By integrating .NET 10 Preview into Azure App Service, Microsoft aims to provide developers early access to cutting-edge .NET capabilities in a scalable, secure, and production-ready hosting environment. This update facilitates rapid innovation cycles and helps organizations prepare their applications for the upcoming stable release, reducing migration friction and accelerating cloud modernization efforts.

**Specific Features and Detailed Changes:**  
- **Support for .NET 10 Preview Runtime and SDK:** Azure App Service now supports running applications targeting .NET 10 Preview, including ASP.NET Core 10, Blazor 10, and Minimal APIs, allowing developers to leverage new language constructs, improved performance, and enhanced APIs.  
- **Cross-Platform Availability:** Both Windows and Linux App Service plans can host .NET 10 Preview apps, ensuring broad compatibility and flexibility in deployment choices.  
- **Updated Build and Deployment Pipelines:** Integration with Azure DevOps and GitHub Actions supports building and deploying .NET 10 Preview applications seamlessly, including containerized workloads.  
- **Enhanced Diagnostics and Monitoring:** Azure App Service’s existing monitoring tools (Application Insights, Log Stream) are compatible with .NET 10 Preview apps, enabling performance tracking and troubleshooting.

**Technical Mechanisms and Implementation Methods:**  
Azure App Service provisions the .NET 10 Preview runtime as part of its underlying platform images. When a web app is configured to use .NET 10 Preview, the platform automatically selects the appropriate runtime environment during deployment and runtime. Developers can specify the target framework in their project files (e.g., `<TargetFramework>net10.0</TargetFramework>`) and deploy via standard methods such as ZIP deploy, Git, or container images. For Linux-based App Service plans, custom container images can be built with the .NET 10 Preview SDK pre-installed, or the built-in runtime stacks can be selected. The platform manages runtime updates and security patches during the preview period.

**Use Cases and Application Scenarios:**  
- **Modern Web Applications:** Developers building ASP.NET Core 10 web apps can test new features such as improved minimal APIs and enhanced routing.  
- **Blazor Applications:** Frontend developers can experiment with the latest Blazor 10 capabilities for building interactive web UIs with C#.  
- **Microservices and APIs:** Teams developing lightweight microservices or APIs can leverage the performance and simplicity improvements in .NET 10.  
- **Cloud-Native Development:** Organizations adopting cloud-native patterns can validate their applications against the upcoming .NET runtime to ensure compatibility and performance in Azure environments.

**Important Considerations and Limitations:**  
- **Preview Status:** As a public preview, .NET 10 on Azure App Service is not recommended for production workloads due to potential instability or breaking changes before the final release.  
- **Runtime Updates:** Preview runtimes may receive frequent updates; developers should monitor release notes and test their applications accordingly.  
- **Compatibility:** Some third-party libraries or dependencies may not yet support .NET 10 Preview, requiring validation and potential code adjustments.  
- **Scaling and Performance:** While Azure App Service provides scaling capabilities, performance characteristics of .NET 10 Preview apps should be benchmarked under expected loads.

**Integration with Related Azure Services:**  
- **Azure DevOps and GitHub Actions:** Continuous integration and deployment pipelines can be configured to build and deploy .NET 10 Preview applications automatically.  
- **Azure Monitor and Application Insights:** These services provide telemetry and diagnostics for .NET 10 apps, enabling proactive monitoring.  
-

---


*This report was automatically generated - 2025-09-06 03:02:32 UTC*