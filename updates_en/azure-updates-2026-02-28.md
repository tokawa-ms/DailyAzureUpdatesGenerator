# February 28, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: February 28, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Generally available: Azure Premium SSD v2 Disk Storage is now available in a third Availability Zone in New Zealan North

**Published**: February 27, 2026 23:15:13 UTC
**Link**: [Generally available: Azure Premium SSD v2 Disk Storage is now available in a third Availability Zone in New Zealan North](https://azure.microsoft.com/updates?id=558078)

**Update ID**: 558078
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Disk Storage, Features, Services

**Summary**:

- What was updated  
Azure Premium SSD v2 Disk Storage is now generally available in a third Availability Zone in the New Zealand North region.

- Key changes or new features  
Premium SSD v2 is a next-generation, general-purpose block storage solution for Azure Virtual Machines (VMs). It delivers sub-millisecond latencies and improved price-performance compared to previous disk offerings. The expansion to a third Availability Zone enhances high availability and disaster recovery options for workloads requiring zone-redundant architectures.

- Target audience affected  
Developers and IT professionals deploying or managing Azure VMs in the New Zealand North region, especially those requiring high-performance, low-latency storage and improved availability for mission-critical applications.

- Important notes if any  
With Premium SSD v2 now available in a third Availability Zone, customers can architect solutions with greater fault tolerance and resilience. Consider updating deployment templates or infrastructure-as-code scripts to leverage the new zone for enhanced availability. Review regional pricing and supported VM sizes to optimize cost and performance.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=558078

**Details**:

**Azure Update Technical Report**

**Title:** Generally available: Azure Premium SSD v2 Disk Storage is now available in a third Availability Zone in New Zealand North  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=558078)

---

**Background and Purpose of the Update**  
This update announces the general availability of Azure Premium SSD v2 disk storage in a third Availability Zone within the New Zealand North region. The purpose of this update is to enhance regional resilience and availability for customers deploying workloads in New Zealand North, by providing access to advanced block storage capabilities across an additional Availability Zone. This expansion supports high-availability architectures and disaster recovery strategies by enabling customers to distribute resources across three distinct fault domains.

**Specific Features and Detailed Changes**  
Azure Premium SSD v2 is a next-generation general-purpose block storage option for Azure Virtual Machines (VMs). The key features highlighted include:
- **Sub-millisecond latencies:** Premium SSD v2 disks deliver extremely low latency, which is critical for performance-sensitive workloads.
- **Exceptional price:** The offering is positioned as cost-effective, providing improved performance at a competitive price point.
- **Availability in a third zone:** Previously, Premium SSD v2 was available in fewer zones within New Zealand North; this update extends support to a third Availability Zone, enabling more robust multi-zone deployments.

**Technical Mechanisms and Implementation Methods**  
Premium SSD v2 disks are provisioned as managed disks within Azure and are attached to Azure VMs as block storage. The sub-millisecond latency is achieved through advanced storage hardware and optimized data paths within Azure’s infrastructure. By making Premium SSD v2 available in a third Availability Zone, Azure ensures that customers can architect solutions that span multiple zones, leveraging zone-redundant storage patterns. This is particularly important for workloads requiring high availability, as resources can be distributed to minimize the impact of zone-level failures.

**Use Cases and Application Scenarios**  
- **High-availability applications:** Customers can deploy mission-critical applications across three Availability Zones, using Premium SSD v2 disks for fast, reliable storage.
- **Disaster recovery:** Multi-zone support enables robust disaster recovery strategies, allowing for quick failover and minimal downtime.
- **Performance-sensitive workloads:** Databases, transactional systems, and analytics workloads benefit from the sub-millisecond latency and consistent performance of Premium SSD v2.
- **Cost optimization:** The price-performance ratio makes Premium SSD v2 suitable for organizations seeking to optimize storage costs without sacrificing speed.

**Important Considerations and Limitations**  
- **Regional scope:** This update is specific to the New Zealand North region and its third Availability Zone; customers in other regions or zones should verify Premium SSD v2 availability.
- **Zone selection:** When architecting solutions, engineers must ensure proper zone selection to maximize availability and resilience.
- **Disk compatibility:** Premium SSD v2 disks are designed for Azure VMs; compatibility with other Azure services should be confirmed based on workload requirements.

**Integration with Related Azure Services**  
Premium SSD v2 disks integrate seamlessly with Azure Virtual Machines, supporting both Windows and Linux workloads. They can be used in conjunction with Azure Availability Sets and Azure Availability Zones to achieve high availability. Additionally, these disks are managed through Azure Resource Manager, enabling automated deployment, scaling, and management via ARM templates, Azure CLI, and PowerShell.

---

**Summary Sentence:**  
Azure Premium SSD v2 disk storage is now generally available in a third Availability Zone in New Zealand North, offering sub-millisecond latency and cost-effective performance for Azure Virtual Machines, thereby enabling enhanced high-availability and disaster recovery architectures in this region.

---

### 2. Generally Available: DCesv6, DCedsv6, ECesv6, and ECedsv6 confidential VMs

**Published**: February 27, 2026 23:15:13 UTC
**Link**: [Generally Available: DCesv6, DCedsv6, ECesv6, and ECedsv6 confidential VMs](https://azure.microsoft.com/updates?id=558051)

**Update ID**: 558051
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines, Features, Services

**Summary**:

- What was updated  
The DCesv6, DCedsv6, ECesv6, and ECedsv6 series confidential Virtual Machines (VMs) are now generally available in Azure.

- Key changes or new features  
These new VM series are built on 5th Gen Intel® Xeon® processors and leverage Intel® Trust Domain Extensions (TDX) to provide advanced confidential computing capabilities. They enable hardware-based isolation of VM memory, protecting data in use from cloud operators and other tenants. The VMs support a range of workloads, including those requiring secure data processing and enhanced privacy. They also offer improved performance and scalability compared to previous generations.

- Target audience affected  
Developers and IT professionals building or managing applications with strict data privacy, compliance, or security requirements—such as those in finance, healthcare, or regulated industries—will benefit most. Organizations looking to adopt confidential computing for sensitive workloads are the primary audience.

- Important notes if any  
These VMs support confidential workloads out-of-the-box with minimal code changes, making it easier to migrate existing applications. Integration with Azure security and management tools is supported. Review regional availability and pricing before deployment, as not all VM sizes may be available in every region.

**Details**:

**Azure Update Report: Generally Available – DCesv6, DCedsv6, ECesv6, and ECedsv6 Confidential VMs**

**Background and Purpose of the Update**  
Azure has announced the general availability of its next-generation confidential Virtual Machines (VMs): DCesv6, DCedsv6, ECesv6, and ECedsv6. These VM series are built on 5th Gen Intel® Xeon® processors, leveraging Intel® Trust Domain Extensions (Intel® TDX). The purpose of this update is to enhance the security and confidentiality of workloads running in Azure by providing advanced hardware-based isolation and protection mechanisms.

**Specific Features and Detailed Changes**  
The new VM series introduces several key features:
- **Confidential Computing:** These VMs are designed to protect data in use by isolating workloads from the cloud infrastructure and other tenants.
- **Intel® TDX Support:** Intel® TDX enables hardware-enforced trust domains, providing stronger isolation for VM memory and state.
- **VM Series Differentiation:**  
  - **DCesv6 and DCedsv6:** Optimized for confidential workloads with enhanced security features.
  - **ECesv6 and ECedsv6:** Targeted for larger, memory-intensive confidential workloads.
- **5th Gen Intel® Xeon® Processors:** Improved performance and security capabilities compared to previous generations.

**Technical Mechanisms and Implementation Methods**  
The implementation relies on Intel® TDX, which establishes trust domains at the hardware level. This mechanism ensures that VM memory and execution context are encrypted and isolated from the hypervisor, other VMs, and Azure operators. The VMs are provisioned through standard Azure deployment methods, and the confidential computing features are enabled by default for these series. The underlying hardware enforces isolation, preventing unauthorized access to VM data during runtime.

**Use Cases and Application Scenarios**  
These confidential VMs are suitable for:
- **Sensitive Workloads:** Applications handling regulated or highly confidential data, such as financial services, healthcare, and government workloads.
- **Multi-tenant Environments:** Scenarios where isolation between tenants is critical.
- **Data Protection Compliance:** Workloads requiring compliance with strict data protection standards and regulations.
- **Confidential AI and Analytics:** Secure processing of sensitive datasets for machine learning and analytics.

**Important Considerations and Limitations**  
- **Hardware Dependency:** The confidential features are only available on VMs provisioned on 5th Gen Intel® Xeon® processors with Intel® TDX.
- **Performance Overhead:** There may be some performance impact due to hardware-based encryption and isolation.
- **Supported Operating Systems and Applications:** Not all OS and application types may be compatible with confidential computing features; validation is recommended.
- **Resource Availability:** These VM series may be limited to specific Azure regions and availability zones.

**Integration with Related Azure Services**  
The confidential VM series integrates with Azure’s broader confidential computing portfolio, including:
- **Azure Key Vault:** For secure key management and attestation.
- **Azure Security Center:** For monitoring and compliance.
- **Azure Policy:** For enforcing deployment and configuration standards.
- **Azure VM Management Tools:** Standard tools for provisioning, monitoring, and scaling are supported.

**Summary Sentence**  
Azure’s DCesv6, DCedsv6, ECesv6, and ECedsv6 confidential VMs are now generally available, offering enhanced hardware-based isolation and protection for sensitive workloads through Intel® TDX on 5th Gen Intel® Xeon® processors.

---

### 3. Retirement: Managed NGINX Ingress with Application Routing Add-on Retiring November 2026

**Published**: February 27, 2026 21:45:03 UTC
**Link**: [Retirement: Managed NGINX Ingress with Application Routing Add-on Retiring November 2026](https://azure.microsoft.com/updates?id=555839)

**Update ID**: 555839
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements, Open Source

**Summary**:

- What was updated  
The Managed NGINX Ingress option within the Application Routing Add-on for Azure Kubernetes Service (AKS) is being retired. Support will end on November 30, 2026.

- Key changes or new features  
The upstream Ingress-NGINX project is being deprecated and will stop receiving updates after March 2026. Microsoft will continue to provide critical security patches for the Managed NGINX Ingress until November 30, 2026. After this date, the NGINX ingress controller will no longer be supported or maintained in AKS.

- Target audience affected  
Developers and IT professionals using AKS clusters with the Application Routing Add-on configured for Managed NGINX Ingress.

- Important notes if any  
Users must plan to migrate workloads from Managed NGINX Ingress to alternative ingress solutions before November 30, 2026, to ensure continued security and support. Consider evaluating Azure’s recommended ingress controllers or other supported solutions. Failure to migrate may expose workloads to unpatched vulnerabilities and unsupported configurations. Early planning and testing of migration paths are strongly advised.  

For more details, see the official update: https://azure.microsoft.com/updates?id=555839

**Details**:

**Azure Update Report**

**Title:** Retirement: Managed NGINX Ingress with Application Routing Add-on Retiring November 2026  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=555839)

---

**Background and Purpose of the Update:**  
The upstream Ingress-NGINX project, which serves as the foundation for the Managed NGINX Ingress with Application Routing Add-on in Azure Kubernetes Service (AKS), is being deprecated. The project will cease receiving updates after March 2026. As a result, Microsoft has announced the retirement of its managed NGINX ingress controller solution, with critical security patch support continuing until November 30, 2026. This update is intended to inform users of the planned retirement and to encourage migration planning.

**Specific Features and Detailed Changes:**  
- The Managed NGINX Ingress controller, provided as part of the Application Routing Add-on for AKS, will no longer be supported after November 30, 2026.
- Microsoft will continue to deliver critical security patches for the managed NGINX ingress controller until the retirement date.
- After November 2026, no further updates, bug fixes, or security patches will be provided for the NGINX ingress controller within the Application Routing Add-on.

**Technical Mechanisms and Implementation Methods:**  
- The Managed NGINX Ingress controller is deployed as an add-on in AKS clusters, enabling users to manage HTTP(S) routing to Kubernetes workloads via NGINX.
- The add-on leverages the upstream Ingress-NGINX project for core ingress functionality, including routing, TLS termination, and path-based routing.
- Security patching will be handled by Microsoft until the specified retirement date, ensuring continued protection against critical vulnerabilities during the transition period.

**Use Cases and Application Scenarios:**  
- The Managed NGINX Ingress controller is commonly used in AKS environments to expose Kubernetes services externally, manage ingress traffic, and provide advanced routing features.
- Typical scenarios include deploying web applications, APIs, and microservices that require secure, scalable ingress management.
- Organizations relying on the Application Routing Add-on for ingress should begin evaluating alternative solutions, such as Azure Application Gateway Ingress Controller or other supported ingress controllers, for future deployments.

**Important Considerations and Limitations:**  
- After November 30, 2026, the NGINX ingress controller in the Application Routing Add-on will become unsupported, exposing clusters to potential security and compliance risks.
- Users must plan for migration to alternative ingress solutions before the retirement date to ensure continued support and security.
- Existing workloads using the managed NGINX ingress controller will not receive updates or patches post-retirement, increasing operational risk.

**Integration with Related Azure Services:**  
- The Managed NGINX Ingress controller integrates directly with AKS, providing native ingress management for Kubernetes workloads.
- Users may consider transitioning to Azure Application Gateway Ingress Controller, which offers deep integration with Azure networking and security services.
- Migration planning should include evaluation of ingress controller compatibility, feature parity, and integration with Azure-native services such as Azure Front Door, Azure Load Balancer, and Azure Monitor.

---

**Summary Sentence:**  
Microsoft will retire the Managed NGINX Ingress with Application Routing Add-on for AKS in November 2026, continuing critical security patch support until then, and recommends users begin migration planning to alternative ingress solutions to maintain security and support.

---

### 4. Generally Available: Azure Red Hat OpenShift is now available in Malaysia West, New Zealand North, and Mexico Central

**Published**: February 27, 2026 17:30:41 UTC
**Link**: [Generally Available: Azure Red Hat OpenShift is now available in Malaysia West, New Zealand North, and Mexico Central](https://azure.microsoft.com/updates?id=557897)

**Update ID**: 557897
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Red Hat OpenShift, Features, Open Source, Regions & Datacenters

**Summary**:

- What was updated  
Azure Red Hat OpenShift is now generally available in three new Azure regions: Malaysia West, New Zealand North, and Mexico Central.

- Key changes or new features  
This update expands the geographic availability of Azure Red Hat OpenShift, allowing customers to deploy and manage OpenShift clusters in these additional regions. It supports the same enterprise-grade Kubernetes features, integration with Azure services, and Red Hat support as in other regions.

- Target audience affected  
Developers and IT professionals who are building, deploying, or managing containerized applications using Azure Red Hat OpenShift, particularly those with workloads or compliance requirements in Malaysia, New Zealand, or Mexico.

- Important notes if any  
This regional expansion helps organizations meet data residency, latency, and regulatory requirements by enabling local deployments. Customers can now leverage Azure Red Hat OpenShift’s managed Kubernetes platform closer to their users and data sources in Asia Pacific and Latin America. No changes to pricing or service features have been announced with this update.

Data source: Using API data  
More information: [Azure Update link](https://azure.microsoft.com/updates?id=557897)

**Details**:

**Azure Update Report**

**Title:** Generally Available: Azure Red Hat OpenShift is now available in Malaysia West, New Zealand North, and Mexico Central  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=557897)

---

**Background and Purpose of the Update**  
Azure Red Hat OpenShift (ARO) is a managed Kubernetes platform jointly engineered, operated, and supported by Microsoft and Red Hat. The purpose of this update is to extend the general availability of ARO to three new Azure regions: Malaysia West, New Zealand North, and Mexico Central. This regional expansion aims to strengthen ARO’s presence in the Asia Pacific and Latin America, enabling customers in these geographies to deploy OpenShift clusters closer to their users and data, thereby improving performance, compliance, and disaster recovery options.

**Specific Features and Detailed Changes**  
With this update, ARO is now generally available in the aforementioned regions. Customers can provision fully managed OpenShift clusters in Malaysia West, New Zealand North, and Mexico Central using the Azure portal, CLI, or ARM templates. The service includes automated cluster deployment, integrated security, built-in monitoring, and enterprise support. All features previously available in other regions, such as integrated CI/CD pipelines, developer self-service, and seamless scaling, are now accessible in these new regions.

**Technical Mechanisms and Implementation Methods**  
ARO leverages Azure’s infrastructure to provide a managed OpenShift environment. The technical implementation involves provisioning Red Hat OpenShift clusters on Azure virtual machines, with Azure handling the underlying compute, networking, and storage. The service automates cluster lifecycle management, including installation, upgrades, patching, and scaling. Integration with Azure Active Directory, Azure Monitor, and Azure Policy is available, enabling centralized identity management, monitoring, and governance. Customers can deploy clusters via the Azure portal, Azure CLI, or ARM templates, specifying the desired region as Malaysia West, New Zealand North, or Mexico Central.

**Use Cases and Application Scenarios**  
Typical use cases include:  
- Enterprises running containerized applications requiring high availability and scalability.  
- Organizations needing compliance with local data residency regulations in Malaysia, New Zealand, or Mexico.  
- Development teams seeking a managed Kubernetes platform with integrated DevOps tooling.  
- Businesses implementing hybrid cloud or multi-region architectures for disaster recovery and latency optimization.  
- ISVs and SaaS providers deploying applications closer to customers in Asia Pacific and Latin America.

**Important Considerations and Limitations**  
- Service availability is limited to Malaysia West, New Zealand North, and Mexico Central, in addition to previously supported regions.  
- Customers must ensure their Azure subscriptions have sufficient quota in these regions for required resources.  
- Network latency, regional pricing, and compliance requirements should be evaluated before deployment.  
- Not all Azure services may be available in these regions; integration points should be verified.  
- Existing clusters in other regions cannot be migrated directly; new clusters must be provisioned in the expanded regions.

**Integration with Related Azure Services**  
ARO integrates seamlessly with Azure services such as Azure Active Directory for identity and access management, Azure Monitor for logging and metrics, and Azure Policy for governance. It also supports integration with Azure DevOps, Azure Container Registry, and other Azure-native services, enabling end-to-end application lifecycle management and security.

---

**Summary Sentence:**  
Azure Red Hat OpenShift is now generally available in Malaysia West, New Zealand North, and Mexico Central, enabling customers in these regions to deploy fully managed OpenShift clusters with integrated Azure services for enhanced performance, compliance, and operational efficiency.

---


*This report was automatically generated - 2026-02-28 03:02:37 UTC*