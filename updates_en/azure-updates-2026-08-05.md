# August 05, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 05, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Retirement: Nested confidential (cc_v5) VMs will be retired on September 1, 2026

**Published**: August 05, 2026 00:22:49 UTC
**Link**: [Retirement: Nested confidential (cc_v5) VMs will be retired on September 1, 2026](https://azure.microsoft.com/updates?id=568661)

**Update ID**: 568661
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machines, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of the cc_v5 confidential VM series, specifically the DCas_c VM sizes, effective September 1, 2026.

- Key changes or new features  
The cc_v5 confidential VMs will no longer be available for use or purchase after the retirement date. Any affected VMs not resized or migrated before September 1, 2026, will be deallocated automatically.

- Target audience affected  
Developers and IT professionals using Azure confidential computing workloads with cc_v5 (DCas_c) VM sizes are directly impacted. This includes those running nested confidential workloads or relying on these VM types for enhanced security and privacy.

- Important notes if any  
To avoid service disruption, users must resize or migrate their workloads to supported VM sizes before the retirement date. Microsoft recommends reviewing current deployments and planning for migration to alternative confidential VM series. Failure to act will result in automatic deallocation of affected VMs. For more information and migration guidance, refer to the official Azure update link: https://azure.microsoft.com/updates?id=568661

**Details**:

**Azure Update Technical Report**

**Title:** Retirement: Nested confidential (cc_v5) VMs will be retired on September 1, 2026  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=568661)

---

**Background and Purpose of the Update**  
Microsoft Azure is announcing the retirement of the cc_v5 confidential VM series, specifically the DCas_c sizes, effective September 1, 2026. The purpose of this update is to inform customers and IT professionals that these VM types will no longer be available for use or purchase after the specified date. This retirement is part of Azure’s ongoing lifecycle management and modernization of its confidential computing offerings.

**Specific Features and Detailed Changes**  
The cc_v5 confidential VM series, which supports nested confidential computing capabilities, will be deprecated. The impacted VM sizes are DCas_c. After September 1, 2026, these VM sizes will be deallocated if not resized to a supported VM type. No new deployments or purchases of cc_v5 VMs will be possible post-retirement. Existing VMs must be migrated or resized before the deadline to avoid service disruption.

**Technical Mechanisms and Implementation Methods**  
Azure will enforce the retirement by deallocating any cc_v5 confidential VMs (DCas_c sizes) that remain active after the retirement date. Deallocation means that the VM will be stopped and resources released, resulting in loss of compute availability for affected workloads. Migration or resizing can be performed using Azure portal, CLI, or PowerShell tools to transition workloads to supported VM series. Azure’s VM lifecycle management and resource orchestration will ensure that retired VM types are systematically removed from the platform.

**Use Cases and Application Scenarios**  
The cc_v5 confidential VM series has been used for workloads requiring enhanced security through confidential computing, such as protecting sensitive data in use, secure multi-party computation, and regulated industry workloads (e.g., finance, healthcare). Nested confidential VMs are particularly relevant for scenarios where additional isolation is needed within a VM, such as running secure containers or trusted execution environments.

**Important Considerations and Limitations**  
- Any cc_v5 confidential VM (DCas_c sizes) not resized or migrated before September 1, 2026 will be deallocated, leading to potential service interruption.
- Customers must plan migration strategies well ahead of the retirement date to ensure business continuity.
- No new cc_v5 confidential VMs can be deployed or purchased after the retirement date.
- It is critical to review current workloads and dependencies on these VM sizes and identify suitable alternatives within Azure’s confidential computing portfolio.

**Integration with Related Azure Services**  
The retirement affects integration with Azure services that leverage confidential computing, such as Azure Key Vault, Azure Confidential Ledger, and confidential containers. Workloads using cc_v5 VMs should be evaluated for compatibility with other Azure confidential VM series or related services. Migration may involve updating deployment templates, security policies, and integration points with Azure management and monitoring tools.

---

**Summary Sentence:**  
On September 1, 2026, Azure will retire the cc_v5 confidential VM series (DCas_c sizes), requiring customers to migrate or resize affected VMs before this date to avoid deallocation and service disruption.

---

### 2. Public Preview: Perimeter link feature in network security perimeter 

**Published**: August 04, 2026 18:30:09 UTC
**Link**: [Public Preview: Perimeter link feature in network security perimeter ](https://azure.microsoft.com/updates?id=568837)

**Update ID**: 568837
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Azure Private Link, Security, Feature

**Summary**:

**What was updated:**  
Azure has introduced the Perimeter Link feature in Network Security Perimeter, now available in Public Preview.

**Key changes or new features:**  
- Perimeter Link enables secure, cross-perimeter connectivity between trusted resources located in different network security perimeters.
- Communication is facilitated using Managed Identity (MSI), eliminating the need for additional credentials or manual configuration.
- This feature supports scenarios where resources must interact across perimeters while maintaining strict security boundaries.

**Target audience affected:**  
- Developers building applications that require secure interactions between resources in separate network security perimeters.
- IT professionals managing Azure network security, especially those responsible for configuring and maintaining perimeter-based isolation and connectivity.

**Important notes:**  
- The feature is currently in Public Preview, so it may not be suitable for production workloads yet.
- Perimeter Link simplifies secure resource communication, reducing operational overhead and potential security risks associated with manual credential management.
- Review documentation and preview limitations before implementation to ensure compatibility with existing network security architectures.

[More details](https://azure.microsoft.com/updates?id=568837)

**Details**:

**Azure Update Report: Public Preview – Perimeter Link Feature in Network Security Perimeter**

**Background and Purpose of the Update**  
The perimeter link feature is introduced as part of Azure’s network security perimeter capabilities to address the need for secure, scalable, and manageable communication between trusted resources located in separate network security perimeters. Traditionally, establishing connectivity across different perimeters required complex configurations, such as explicit network peering or manual credential management, which could increase operational overhead and potential security risks. The perimeter link aims to streamline cross-perimeter connectivity by leveraging Azure’s Managed Identity (MSI) for authentication and authorization, thereby enhancing security and simplifying resource access management.

**Specific Features and Detailed Changes**  
- **Cross-Perimeter Connectivity:** The perimeter link enables resources in two distinct network security perimeters to communicate securely without the need for additional network peering or manual credential exchanges.
- **Managed Identity Integration:** Communication between resources is authenticated using Azure Managed Identity, eliminating the need for explicit secrets or credentials.
- **Simplified Configuration:** The feature reduces the complexity of configuring secure connectivity by automating identity-based access, allowing IT professionals to focus on resource management rather than network security configuration.

**Technical Mechanisms and Implementation Methods**  
- **Managed Identity (MSI):** Azure resources are assigned managed identities, which are used to authenticate and authorize communications across perimeters. This ensures that only trusted resources can interact, and credentials are managed by Azure, reducing the risk of exposure.
- **Network Security Perimeter Enforcement:** The perimeter link operates within the boundaries defined by Azure’s network security perimeter policies, ensuring that all communications adhere to organizational security requirements.
- **No Additional Network Peering Required:** Unlike traditional methods, the perimeter link does not require setting up explicit network peering or VPN connections between perimeters, thus minimizing network configuration and maintenance.

**Use Cases and Application Scenarios**  
- **Multi-Environment Resource Access:** Organizations with resources distributed across multiple network security perimeters (such as production and development environments) can enable secure, controlled communication between these environments for tasks like data synchronization or shared service access.
- **Regulatory Compliance:** Enterprises needing to enforce strict perimeter isolation for compliance can still facilitate necessary cross-perimeter operations without compromising security or increasing administrative burden.
- **Microservices Architectures:** Applications composed of microservices deployed in different perimeters can securely interact using managed identities, supporting scalable and modular architectures.

**Important Considerations and Limitations**  
- **Public Preview Status:** The perimeter link feature is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes or limitations.
- **Managed Identity Dependency:** Only resources that support Azure Managed Identity can utilize this feature for cross-perimeter connectivity.
- **Scope of Connectivity:** The feature is designed for trusted resources; untrusted or external resources cannot leverage perimeter link for communication.

**Integration with Related Azure Services**  
- **Azure Active Directory:** Managed Identity is backed by Azure AD, ensuring robust identity management and integration with existing organizational policies.
- **Network Security Perimeter Controls:** The perimeter link works in conjunction with Azure’s perimeter controls, allowing seamless enforcement of security policies.
- **Resource Management Tools:** Azure Resource Manager and related tools can be used to configure and monitor perimeter link connections, supporting automation and governance.

**Summary Sentence:**  
The perimeter link feature in Azure network security perimeter, now in public preview, enables secure, identity-based cross-perimeter connectivity for trusted resources using Managed Identity, simplifying configuration and enhancing security without requiring additional network peering.

---

### 3. Public Preview: Azure Private Link support over IPv6 

**Published**: August 04, 2026 18:29:36 UTC
**Link**: [Public Preview: Azure Private Link support over IPv6 ](https://azure.microsoft.com/updates?id=568842)

**Update ID**: 568842
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Azure Private Link, Features

**Summary**:

- What was updated  
Azure Private Link now supports IPv6 connectivity in public preview.

- Key changes or new features  
Azure Private Link allows private access to Azure PaaS services (e.g., Azure Storage, Azure SQL Database) using IPv6-based connections. Developers and IT professionals can now create IPv6 private endpoints within Azure virtual networks, enabling secure, private access from IPv6-enabled clients. This enhancement supports dual-stack (IPv4/IPv6) scenarios, improving flexibility for organizations migrating to IPv6 or operating in IPv6-only environments.

- Target audience affected  
This update impacts developers, network architects, and IT professionals managing Azure resources, especially those planning or implementing IPv6 adoption, requiring secure access to Azure PaaS services, or operating in environments with IPv6-only clients.

- Important notes if any  
The feature is currently in public preview and may not be suitable for production workloads. Ensure your Azure virtual network and clients are configured for IPv6. Review documentation for supported regions and limitations. This update helps organizations meet compliance and future-proof their cloud infrastructure as IPv6 adoption increases.

For more details, visit: https://azure.microsoft.com/updates?id=568842

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Azure Private Link support over IPv6  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=568842)

---

### Background and Purpose of the Update

This update introduces Azure Private Link support over IPv6, now in public preview. The primary purpose is to enable private access to Azure PaaS services—such as Azure Storage and Azure SQL Database—using IPv6-based connectivity. This enhancement addresses the growing need for IPv6 adoption due to IPv4 address exhaustion and compliance requirements, and enables organizations to modernize their network architectures with end-to-end IPv6 support.

---

### Specific Features and Detailed Changes

- **IPv6 Private Endpoints:** Azure customers can now create private endpoints using IPv6 addresses within their Azure virtual networks (VNets).
- **PaaS Service Access:** These IPv6 private endpoints allow secure, private connectivity to supported Azure PaaS services (e.g., Azure Storage, Azure SQL Database) over IPv6.
- **Client Connectivity:** IPv6 clients within an Azure VNet can directly access PaaS resources via these IPv6 private endpoints, ensuring traffic remains on the Microsoft backbone and is not exposed to the public internet.

---

### Technical Mechanisms and Implementation Methods

- **Private Endpoint Creation:** When configuring a private endpoint, users can now specify IPv6 as the IP family. The endpoint is assigned an IPv6 address from the VNet’s IPv6 address space.
- **Network Traffic Flow:** Traffic from IPv6 clients in the VNet is routed privately to the Azure PaaS service through the IPv6 private endpoint, leveraging Azure’s software-defined networking (SDN) capabilities.
- **DNS Integration:** DNS records are updated to resolve the PaaS resource’s private link FQDN to the IPv6 address of the private endpoint, ensuring seamless name resolution for IPv6 clients.

---

### Use Cases and Application Scenarios

- **IPv6-Only or Dual-Stack Environments:** Organizations operating IPv6-only or dual-stack (IPv4/IPv6) networks can now extend private connectivity to Azure PaaS services without relying on IPv4.
- **Compliance and Future-Proofing:** Enterprises with regulatory or policy requirements for IPv6 adoption can leverage this feature to maintain compliance and prepare for future networking needs.
- **Secure Data Access:** Applications and workloads that require secure, private access to Azure Storage or Azure SQL Database can now do so over IPv6, reducing exposure to public networks.

---

### Important Considerations and Limitations

- **Public Preview:** This feature is in public preview and may not be suitable for production workloads. Customers should evaluate and test thoroughly before broad deployment.
- **Service Support:** Only specific Azure PaaS services (currently Azure Storage and Azure SQL Database) are supported for IPv6 private endpoints in this preview.
- **VNet Requirements:** The Azure VNet must be configured with an IPv6 address space to utilize IPv6 private endpoints.
- **Client Compatibility:** Only IPv6-capable clients within the VNet can leverage these endpoints; IPv4-only clients must continue using IPv4 private endpoints.

---

### Integration with Related Azure Services

- **Azure Virtual Network:** IPv6 private endpoints are provisioned within Azure VNets, leveraging their IPv6 address space.
- **Azure DNS:** Integration ensures private DNS zones can resolve PaaS resource names to the correct IPv6 private endpoint addresses.
- **Network Security:** Standard Azure networking controls (e.g., Network Security Groups, User-Defined Routes) can be applied to IPv6 traffic to and from private endpoints.

---

**Summary:**  
Azure Private Link now supports IPv6 private endpoints in public preview, enabling secure, private access to Azure PaaS services like Storage and SQL Database from IPv6 clients within an Azure virtual network.

---

### 4. Public Preview: Azure DNS enables DNS-based load balancing through Traffic Manager integration

**Published**: August 04, 2026 17:04:55 UTC
**Link**: [Public Preview: Azure DNS enables DNS-based load balancing through Traffic Manager integration](https://azure.microsoft.com/updates?id=565214)

**Update ID**: 565214
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Management and governance, Azure DNS, Traffic Manager, Services, Feature

**Summary**:

**What was updated:**  
Azure DNS now supports direct integration with Azure Traffic Manager for DNS-based load balancing, available in Public Preview.

**Key changes or new features:**  
- You can now associate Azure DNS record sets directly with Traffic Manager profiles.  
- This eliminates the need to create a CNAME record pointing to the trafficmanager.net domain.  
- DNS-based traffic routing is simplified, enabling more efficient and native load balancing.

**Target audience affected:**  
- Developers managing application traffic routing and DNS configurations.  
- IT professionals responsible for DNS management and high availability solutions in Azure.

**Important notes:**  
- This integration streamlines DNS-based load balancing, reducing configuration complexity and improving performance.  
- The feature is currently in Public Preview; production use should be evaluated accordingly.  
- Existing solutions using CNAME records can consider migrating to this new approach for improved manageability.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=565214).

**Details**:

**Azure Update Technical Explanation**

**Title:** Public Preview: Azure DNS enables DNS-based load balancing through Traffic Manager integration

---

**Background and Purpose of the Update**

Previously, integrating Azure DNS with Azure Traffic Manager for DNS-based load balancing required customers to create a CNAME record in their Azure DNS zone, which pointed to the Traffic Manager profile’s FQDN (ending with *.trafficmanager.net*). This approach introduced dependencies on CNAME records, which can complicate DNS configurations—especially when using apex (root) domains, where CNAME records are not permitted. The purpose of this update is to streamline DNS-based traffic routing by enabling direct association between Azure DNS record sets and Traffic Manager profiles, eliminating the need for intermediate CNAME records.

---

**Specific Features and Detailed Changes**

- **Direct Association:** Customers can now associate an Azure DNS record set directly with a Traffic Manager profile. This removes the requirement to create a CNAME record that points to the Traffic Manager’s FQDN.
- **Simplified Configuration:** DNS-based load balancing can now be configured natively within Azure DNS, reducing configuration steps and potential points of failure.
- **Public Preview Availability:** This feature is currently in public preview, allowing customers to evaluate and provide feedback before general availability.

---

**Technical Mechanisms and Implementation Methods**

- **DNS Record Set Integration:** Instead of configuring a CNAME record, users can directly bind an Azure DNS record set (such as an A or AAAA record) to a Traffic Manager profile. This integration is managed within the Azure DNS and Traffic Manager resource configurations.
- **Traffic Routing:** When a DNS query is made for the associated domain, Azure DNS interacts with Traffic Manager to determine the optimal endpoint based on the configured routing method (e.g., performance, priority, weighted, or geographic).
- **No CNAME Dependency:** The DNS response can now directly reflect the Traffic Manager’s routing decision without requiring DNS clients to resolve an additional CNAME layer.

---

**Use Cases and Application Scenarios**

- **Root Domain Load Balancing:** Organizations can implement DNS-based load balancing for apex domains (e.g., example.com) without violating DNS standards that prohibit CNAME records at the zone apex.
- **Simplified Multi-Region Deployments:** Enterprises with applications deployed across multiple Azure regions can use this integration to distribute traffic efficiently and with reduced DNS complexity.
- **Zero-Downtime Migrations:** During infrastructure migrations, DNS-based routing can be managed more seamlessly, minimizing configuration errors and propagation delays.

---

**Important Considerations and Limitations**

- **Public Preview:** As this feature is in public preview, it may not be suitable for production workloads requiring strict SLAs. Customers should evaluate and test thoroughly before broad deployment.
- **Feature Scope:** The update specifically removes the need for CNAME records for Traffic Manager integration; other advanced DNS or Traffic Manager features are unchanged.
- **Compatibility:** Existing configurations using CNAME records will continue to function, but customers may need to update their DNS record sets to leverage direct association.

---

**Integration with Related Azure Services**

- **Azure DNS:** The integration is native to Azure DNS, allowing for direct management within the Azure portal, CLI, or ARM templates.
- **Azure Traffic Manager:** All Traffic Manager routing methods (performance, priority, weighted, geographic) are supported through this integration.
- **Other Azure Networking Services:** This update complements Azure Front Door and Application Gateway by providing a more streamlined DNS-based traffic management option.

---

**Summary Sentence**

Azure DNS now enables direct integration with Azure Traffic Manager for DNS-based load balancing, allowing customers to associate DNS record sets with Traffic Manager profiles without requiring CNAME records, thereby simplifying DNS configurations and supporting apex domain scenarios.

---

### 5. Generally Available: Azure Virtual Network routing appliance

**Published**: August 04, 2026 17:03:38 UTC
**Link**: [Generally Available: Azure Virtual Network routing appliance](https://azure.microsoft.com/updates?id=568605)

**Update ID**: 568605
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Virtual Network, Management, Services, Feature

**Summary**:

- What was updated  
Azure Virtual Network routing appliance is now generally available.

- Key changes or new features  
This new appliance enables private connectivity across Azure virtual networks using specialized hardware. It offers significantly lower latency, higher throughput, and improved performance compared to traditional routing via virtual machines. The appliance supports scalable, high-speed routing and is designed for enterprise workloads requiring robust network performance.

- Target audience affected  
Developers and IT professionals managing Azure networking, especially those responsible for designing, deploying, or maintaining large-scale, high-performance network architectures in Azure.

- Important notes  
The routing appliance is ideal for scenarios where network performance and reliability are critical, such as multi-tier applications, hybrid cloud deployments, and environments with intensive east-west traffic. It simplifies network architecture by reducing reliance on VM-based routers, lowering operational overhead and costs. Integration with Azure Virtual Network and compatibility with existing network security and monitoring tools is supported. For deployment guidance and pricing, refer to Azure documentation.

Link: https://azure.microsoft.com/updates?id=568605

**Details**:

**Azure Update Technical Report: Generally Available – Azure Virtual Network Routing Appliance**

**Background and Purpose of the Update:**  
The Azure Virtual Network routing appliance is now generally available, marking a significant enhancement in Azure’s networking capabilities. This update addresses the need for improved private connectivity across virtual networks (VNets) within Azure, focusing on delivering superior network performance compared to traditional routing solutions based on virtual machines (VMs).

**Specific Features and Detailed Changes:**  
- **Private Connectivity:** The routing appliance enables private connectivity between VNets, facilitating secure and isolated network communication within Azure environments.
- **Specialized Hardware:** Unlike VM-based routing solutions, this appliance leverages dedicated hardware, resulting in lower latency, higher throughput, and overall better network performance.
- **General Availability:** The service has moved from preview or limited release to full general availability, indicating production readiness and broader support.

**Technical Mechanisms and Implementation Methods:**  
- **Hardware-Based Routing:** The appliance is implemented using specialized hardware rather than general-purpose VMs. This approach reduces the overhead associated with software-based routing and eliminates the performance bottlenecks typical of VM-based network virtual appliances.
- **Integration with Azure Virtual Network:** The routing appliance is deployed within Azure Virtual Networks, acting as a dedicated network function for routing traffic between VNets.
- **Performance Optimization:** By utilizing hardware acceleration, the appliance achieves lower packet forwarding latency and higher data throughput, which is critical for latency-sensitive and high-bandwidth applications.

**Use Cases and Application Scenarios:**  
- **Enterprise Network Segmentation:** Organizations can use the routing appliance to securely connect multiple VNets, supporting scenarios such as hub-and-spoke architectures or multi-tier application deployments.
- **High-Performance Workloads:** Applications requiring low-latency and high-throughput inter-VNet communication, such as real-time analytics, distributed databases, or high-frequency trading platforms, benefit from the appliance’s enhanced performance.
- **Hybrid Networking:** The appliance can be used to facilitate complex routing scenarios in hybrid cloud environments, ensuring efficient and secure connectivity between on-premises networks and Azure VNets.

**Important Considerations and Limitations:**  
- **Specialized Hardware Dependency:** As the appliance relies on dedicated hardware, deployment options and regional availability may be subject to Azure’s hardware provisioning.
- **Cost Implications:** While not specified in the update, hardware-based appliances typically have different pricing models compared to VM-based solutions, which should be evaluated during planning.
- **Compatibility:** The routing appliance is designed for private VNet connectivity; integration with public endpoints or internet-bound traffic is not detailed in the update.

**Integration with Related Azure Services:**  
- **Azure Virtual Network:** The appliance is natively integrated with Azure VNets, serving as a core component in network topology design.
- **Network Security:** While not explicitly mentioned, the appliance can be combined with Azure Network Security Groups (NSGs) and Azure Firewall for comprehensive security management.
- **Azure Monitoring:** Integration with Azure Monitor and Network Watcher is implied for operational visibility, though specific monitoring features are not detailed in the update.

**Summary:**  
The general availability of the Azure Virtual Network routing appliance introduces a high-performance, hardware-based solution for private VNet connectivity, offering lower latency and higher throughput than VM-based routing. This update enables IT professionals to design more efficient, secure, and scalable network architectures within Azure, particularly for scenarios demanding robust inter-VNet communication.

---


*This report was automatically generated - 2026-08-05 03:04:11 UTC*