# August 19, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 19, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Retirement: Azure VMware Solution License-included service will be retired August 30, 2027

**Published**: August 18, 2026 19:52:06 UTC
**Link**: [Retirement: Azure VMware Solution License-included service will be retired August 30, 2027](https://azure.microsoft.com/updates?id=569535)

**Update ID**: 569535
**Data source**: Azure Updates API

**Categories**: Compute, Azure VMware Solution, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of the Azure VMware Solution License-included service, effective August 30, 2027.

- Key changes or new features  
Due to Broadcom's updated VMware licensing policies, customers will no longer be able to use the license-included option for Azure VMware Solution after the retirement date. Instead, customers must bring their own portable VMware Cloud Foundation (VCF) license (“BYOL”) to continue using Azure VMware Solution.

- Target audience affected  
This update impacts developers, IT professionals, and organizations currently using or planning to use Azure VMware Solution with license-included services. It is especially relevant for those managing VMware workloads in Azure.

- Important notes if any  
Existing license-included deployments will be supported until August 30, 2027. After this date, customers must transition to the BYOL model to avoid service disruption. Planning for license acquisition and migration is recommended well in advance. No immediate action is required, but review your VMware licensing strategy for Azure workloads to ensure compliance and continuity.

**Details**:

**Azure Update Report: Retirement of Azure VMware Solution License-Included Service (Effective August 30, 2027)**  
[Reference: Azure Update Link](https://azure.microsoft.com/updates?id=569535)

---

**Background and Purpose of the Update**  
Broadcom, following its acquisition of VMware, revised VMware licensing policies for hyperscaler platforms in November last year. The new policy mandates customers to utilize “bring your own” portable licenses for VMware Cloud Foundation (VCF), discontinuing license-included offerings. As a direct result, Microsoft Azure will retire the Azure VMware Solution (AVS) license-included service on August 30, 2027. This update aligns Azure’s VMware offerings with Broadcom’s licensing requirements and prepares customers for the transition to a BYOL (Bring Your Own License) model.

---

**Specific Features and Detailed Changes**  
- **Retirement Date:** The license-included AVS service will be retired on August 30, 2027.
- **Service Impact:** After this date, Azure will no longer provide VMware licenses as part of AVS. Customers must supply their own portable VMware Cloud Foundation licenses to continue using AVS.
- **Transition Requirement:** Existing AVS customers using the license-included model must migrate to the BYOL model before the retirement date to avoid service disruption.

---

**Technical Mechanisms and Implementation Methods**  
- **Current Model:** The license-included AVS service bundles VMware software licenses (vSphere, vSAN, NSX, etc.) with Azure infrastructure, simplifying procurement and deployment.
- **Post-Retirement Model:** Customers will be required to obtain portable VMware Cloud Foundation licenses directly from Broadcom or authorized partners. These licenses must be applied to AVS deployments in Azure.
- **Migration Process:** Technical migration will involve:
  - Decommissioning license-included AVS clusters.
  - Provisioning new AVS clusters using BYOL.
  - Applying customer-owned VMware licenses to the new clusters.
  - Ensuring compliance with Broadcom’s licensing terms for hyperscaler platforms.

---

**Use Cases and Application Scenarios**  
- **Current Use Cases:** AVS is used for lift-and-shift migrations, hybrid cloud deployments, disaster recovery, and extending on-premises VMware environments into Azure with minimal re-architecture.
- **Future Use Cases:** These scenarios remain valid, but customers must manage VMware licensing independently. Organizations with existing VMware Cloud Foundation licenses can leverage AVS as part of their hybrid or multi-cloud strategies, ensuring license portability and compliance.

---

**Important Considerations and Limitations**  
- **Licensing Responsibility:** Customers are responsible for procuring and managing portable VMware Cloud Foundation licenses.
- **Compliance:** Only portable licenses are valid for AVS post-retirement; non-portable licenses or legacy license types will not be accepted.
- **Transition Timeline:** Customers must plan and execute migration before August 30, 2027, to avoid service interruption.
- **Cost Implications:** The shift to BYOL may impact budgeting and procurement processes, as license costs are no longer bundled with Azure infrastructure.

---

**Integration with Related Azure Services**  
- **AVS Integration:** AVS continues to integrate with Azure services such as Azure Active Directory, Azure Backup, Azure Site Recovery, and Azure networking features.
- **Licensing Integration:** The BYOL model requires coordination between Azure resource management and VMware license management, ensuring seamless operation and compliance.

---

**Summary Sentence**  
Azure VMware Solution’s license-included service will be retired on August 30, 2027, requiring customers to transition to a bring-your-own-license model for VMware Cloud Foundation in alignment with Broadcom’s updated licensing policies.

---

### 2. Generally Available: Managed Instance on Azure App Service

**Published**: August 18, 2026 17:26:25 UTC
**Link**: [Generally Available: Managed Instance on Azure App Service](https://azure.microsoft.com/updates?id=568952)

**Update ID**: 568952
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Mobile, Web, App Service, Services, Feature

**Summary**:

- What was updated  
Managed Instance on Azure App Service is now generally available.

- Key changes or new features  
Managed Instance enables organizations to migrate web applications from on-premises or virtual machines to Azure App Service with minimal configuration and no code changes. This feature provides enhanced compatibility for applications that require specific dependencies, custom configurations, or legacy frameworks. Managed Instance offers isolated hosting environments, improved security, and easier management of web apps, supporting seamless lift-and-shift scenarios.

- Target audience affected  
Developers and IT professionals responsible for migrating, managing, or deploying web applications, especially those with complex dependencies or legacy architectures.

- Important notes  
Managed Instance simplifies migration to Azure App Service by reducing the need for code modifications and extensive reconfiguration. It is ideal for organizations seeking to modernize their web hosting infrastructure without disrupting existing application functionality. Consider using Managed Instance for web apps that cannot be easily refactored for standard App Service environments.

**Details**:

**Azure Update Report: Managed Instance on Azure App Service (General Availability)**

**Background and Purpose of the Update:**  
The general availability of Managed Instance on Azure App Service addresses the need for organizations to migrate web applications from on-premises environments or virtual machines to Azure App Service with minimal disruption. The primary purpose is to streamline migration processes by reducing configuration requirements and eliminating the necessity for code changes, thereby accelerating cloud adoption and minimizing operational overhead.

**Specific Features and Detailed Changes:**  
Managed Instance introduces a new deployment option within Azure App Service, enabling organizations to host web applications in a managed environment that closely replicates their existing infrastructure. The key feature is the ability to migrate applications with minimal configuration, supporting seamless transition from on-premises or VM-based hosting to Azure App Service. This update removes the requirement for code modifications, simplifying the migration workflow and reducing potential compatibility issues.

**Technical Mechanisms and Implementation Methods:**  
The Managed Instance leverages Azure App Service’s platform capabilities to provide a managed hosting environment. It abstracts underlying infrastructure management, offering automated scaling, patching, and monitoring. Applications are migrated by configuring the Managed Instance to match the original environment, ensuring compatibility and operational consistency. The implementation focuses on preserving application settings, dependencies, and runtime configurations, allowing for a lift-and-shift migration approach without code refactoring.

**Use Cases and Application Scenarios:**  
Typical use cases include organizations seeking to modernize legacy web applications, migrate workloads from on-premises data centers, or consolidate VM-hosted applications into Azure’s PaaS offerings. Managed Instance is particularly beneficial for scenarios where application code cannot be easily modified, such as proprietary or legacy systems. It supports business continuity by enabling rapid migration and deployment, making it suitable for large-scale enterprise migrations and hybrid cloud strategies.

**Important Considerations and Limitations:**  
While Managed Instance simplifies migration, IT professionals should assess compatibility with Azure App Service’s managed environment, including supported frameworks, dependencies, and integration points. It is essential to review application architecture to ensure seamless operation post-migration. Limitations may include restrictions on certain custom configurations or dependencies that are not supported within the managed instance model. Organizations should also consider network connectivity, security policies, and compliance requirements when planning migration.

**Integration with Related Azure Services:**  
Managed Instance on Azure App Service integrates with other Azure services such as Azure SQL Database, Azure Storage, and Azure Active Directory for authentication and data management. It supports monitoring and diagnostics through Azure Monitor and Application Insights, enabling comprehensive visibility into application performance and health. Integration with Azure DevOps facilitates CI/CD pipelines for ongoing application management and deployment.

**Summary Sentence:**  
Managed Instance on Azure App Service is now generally available, enabling organizations to migrate web applications from on-premises or virtual machines to Azure App Service with minimal configuration and no code changes, thereby streamlining cloud adoption and operational management.

---

### 3. Public Preview: Ipv6 support in Azure Firewall

**Published**: August 18, 2026 17:25:30 UTC
**Link**: [Public Preview: Ipv6 support in Azure Firewall](https://azure.microsoft.com/updates?id=569520)

**Update ID**: 569520
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure Firewall, Features

**Summary**:

- What was updated  
Azure Firewall now supports IPv6 in public preview, allowing dual-stack (IPv4 and IPv6) configurations.

- Key changes or new features  
  - Azure Firewall and Firewall Policy can be configured to handle both IPv4 and IPv6 traffic.  
  - Native IPv6 network rule filtering is enabled, allowing granular control over IPv6 traffic.  
  - DNS Proxy support for IPv6 is included, improving DNS resolution capabilities for dual-stack environments.

- Target audience affected  
  - Developers building applications or services that require IPv6 connectivity and security.  
  - IT professionals managing Azure network security, especially those planning or operating dual-stack (IPv4/IPv6) environments.

- Important notes  
  - This feature is currently in public preview, so it may not be suitable for production workloads.  
  - Customers can now start testing and validating IPv6 scenarios with Azure Firewall, preparing for broader IPv6 adoption.  
  - Review documentation for limitations or unsupported features during the preview phase.

Link: https://azure.microsoft.com/updates?id=569520

**Details**:

**Azure Update Report: Public Preview – IPv6 Support in Azure Firewall**

**Background and Purpose of the Update**  
This update introduces IPv6 support in Azure Firewall, now available in public preview. The primary purpose is to enable organizations to manage both IPv4 and IPv6 traffic through Azure Firewall, addressing the growing need for IPv6 adoption due to IPv4 address exhaustion and compliance requirements. By supporting dual-stack (IPv4 and IPv6) configurations, Azure Firewall enhances security and connectivity for modern cloud architectures.

**Specific Features and Detailed Changes**  
- **Dual-Stack Mode:** Azure Firewall and Firewall Policy can now be configured to process both IPv4 and IPv6 traffic simultaneously. This dual-stack capability allows seamless management of mixed-protocol environments.
- **Native IPv6 Network Rule Filtering:** Administrators can create and enforce network rules that specifically target IPv6 addresses, enabling granular control over IPv6 traffic flows.
- **DNS Proxy Support for IPv6:** Azure Firewall’s DNS Proxy feature now supports IPv6, allowing DNS queries and responses over IPv6 networks to be inspected and filtered according to policy.

**Technical Mechanisms and Implementation Methods**  
- **Firewall Configuration:** When deploying or updating an Azure Firewall instance, IT professionals can enable dual-stack mode, which provisions the firewall with both IPv4 and IPv6 front-end IP configurations.
- **Firewall Policy Integration:** Network rules within Azure Firewall Policy can specify IPv6 address prefixes, ranges, and protocols, leveraging the same rule constructs as for IPv4.
- **Traffic Inspection:** The firewall inspects, filters, and logs both IPv4 and IPv6 traffic according to the configured rules, ensuring consistent security posture across both protocols.
- **DNS Proxy Operation:** DNS queries over IPv6 are intercepted and processed by the DNS Proxy, which applies policy-based filtering and forwards queries as appropriate.

**Use Cases and Application Scenarios**  
- **Hybrid and Cloud-Native Applications:** Organizations transitioning to IPv6 or operating in hybrid environments can secure both IPv4 and IPv6 workloads using a unified firewall solution.
- **Regulatory Compliance:** Enterprises subject to mandates for IPv6 adoption can now enforce security policies for IPv6 traffic within Azure.
- **Global Services:** Applications serving regions or clients where IPv6 is prevalent can be protected without deploying separate security appliances.

**Important Considerations and Limitations**  
- **Public Preview Status:** As this feature is in public preview, it is not recommended for production workloads. Users should validate functionality and monitor for updates regarding general availability.
- **Feature Scope:** Only the features explicitly mentioned—dual-stack mode, network rule filtering, and DNS Proxy for IPv6—are supported in this preview. Other Azure Firewall features may not yet support IPv6.
- **Policy Configuration:** Careful configuration is required to ensure that both IPv4 and IPv6 rules do not conflict and that security coverage is comprehensive.

**Integration with Related Azure Services**  
- **Virtual Networks (VNets):** Azure Firewall with IPv6 support can be integrated into dual-stack VNets, allowing inspection of both address families.
- **Firewall Policy Management:** Policies can be centrally managed and applied to multiple firewalls, now including IPv6-specific rules.
- **DNS Services:** Integration with Azure DNS and custom DNS solutions is enhanced by IPv6 DNS Proxy support.

**Summary**  
Azure Firewall now supports IPv6 in public preview, enabling dual-stack configurations, native IPv6 rule filtering, and DNS Proxy for IPv6, thereby enhancing security for modern, mixed-protocol cloud environments.

---


*This report was automatically generated - 2026-08-19 03:02:37 UTC*