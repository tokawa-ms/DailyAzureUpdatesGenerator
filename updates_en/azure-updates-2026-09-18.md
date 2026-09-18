# September 18, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 18, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Public Preview: Azure Payments HSM v2

**Published**: September 17, 2026 18:36:44 UTC
**Link**: [Public Preview: Azure Payments HSM v2](https://azure.microsoft.com/updates?id=570509)

**Update ID**: 570509
**Data source**: Azure Updates API

**Categories**: In preview, Features, Security, Services

**Summary**:

- What was updated  
Azure Payments HSM v2 has been released in Public Preview.

- Key changes or new features  
Azure Payments HSM v2 provides a highly available, single-tenant Hardware Security Module (HSM) service specifically designed for payment processing workloads. Key features include support for payment transaction processing, credential issuance, PIN processing, cryptographic key management, and authentication data protection. Customers have exclusive administrative control over their dedicated HSM instance, ensuring isolation and compliance with industry standards.

- Target audience affected  
This update is relevant for developers and IT professionals working in the financial services sector, payment processors, and organizations that require secure, compliant, and dedicated HSM infrastructure for handling sensitive payment data and cryptographic operations.

- Important notes if any  
Azure Payments HSM v2 is currently in Public Preview and is intended for scenarios requiring high security and compliance, such as PCI DSS. Customers are responsible for managing and configuring their HSM instances. Integration with Azure services and APIs enables automation and scalability for payment and cryptographic workflows. Early adopters should review preview limitations and plan for potential changes before general availability.

Data source: [Azure Updates](https://azure.microsoft.com/updates?id=570509)

**Details**:

**Azure Update Report: Public Preview – Azure Payments HSM v2**

**Background and Purpose of the Update**  
Azure Payments HSM v2 enters public preview as a dedicated, highly available, single-tenant Hardware Security Module (HSM) service specifically designed for the payments industry. The purpose of this update is to provide organizations with a secure and compliant environment for critical payment processing operations, including credential issuance, PIN processing, key management, and authentication data protection. By offering exclusive administrative control and tenant isolation, Azure addresses the stringent security and regulatory requirements of financial services and payment processing entities.

**Specific Features and Detailed Changes**  
Azure Payments HSM v2 introduces several key features:
- **Single-Tenant Architecture:** Each customer receives an isolated HSM instance, ensuring exclusive administrative access and eliminating multi-tenancy risks.
- **High Availability:** The service is architected for high uptime, supporting business continuity for mission-critical payment operations.
- **Comprehensive Payment Operations Support:** The HSM supports a broad range of payment-related cryptographic operations, including secure credential issuance, PIN processing, and key lifecycle management.
- **Authentication Data Protection:** Sensitive authentication data is protected using industry-standard cryptographic mechanisms.

**Technical Mechanisms and Implementation Methods**  
Azure Payments HSM v2 is implemented as a fully managed, single-tenant service. Customers are provisioned with a dedicated HSM instance, physically and logically isolated from other tenants. Administrative control is retained exclusively by the customer, enabling them to manage cryptographic keys, configure security policies, and control access. The service is designed for high availability, utilizing Azure’s resilient infrastructure to minimize downtime and ensure operational continuity for payment workloads.

**Use Cases and Application Scenarios**  
- **Payment Transaction Processing:** Securely process payment transactions requiring PIN translation, encryption, and validation.
- **Credential Issuance:** Issue and manage payment credentials (e.g., EMV cards, mobile payment tokens) in a compliant environment.
- **Key Management:** Generate, store, and rotate cryptographic keys used in payment ecosystems, ensuring compliance with industry standards.
- **Authentication Data Protection:** Protect sensitive authentication data, such as PINs and cryptograms, during transmission and storage.

**Important Considerations and Limitations**  
- **Single-Tenant Model:** While providing enhanced security, the single-tenant model may have implications for resource allocation and cost compared to multi-tenant HSM services.
- **Administrative Responsibility:** Customers are solely responsible for the administration and management of their HSM instance, including key management and access controls.
- **Public Preview Status:** As the service is in public preview, it may not yet be suitable for production workloads requiring full SLA guarantees or regulatory certifications.

**Integration with Related Azure Services**  
Azure Payments HSM v2 can be integrated with other Azure services to build end-to-end payment solutions. For example, it can work alongside Azure Key Vault for broader key management scenarios, or be used in conjunction with Azure Virtual Network for secure connectivity. The service’s isolation and administrative control make it suitable for integration into regulated payment processing architectures.

**Summary**  
Azure Payments HSM v2 (Public Preview) offers a highly available, single-tenant HSM service for secure payment processing, credential issuance, PIN processing, key management, and authentication data protection, with exclusive administrative control and tenant isolation for compliance-focused organizations.

---

### 2. Generally Available: High-scale mesh in Azure Virtual Network Manager

**Published**: September 17, 2026 17:40:33 UTC
**Link**: [Generally Available: High-scale mesh in Azure Virtual Network Manager](https://azure.microsoft.com/updates?id=571572)

**Update ID**: 571572
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Azure Virtual Network Manager, Features, Management, Services

**Summary**:

- What was updated  
High-scale mesh connectivity in Azure Virtual Network Manager (AVNM) is now generally available.

- Key changes or new features  
Customers can now connect up to 3,000 virtual networks within a single mesh connectivity configuration by default, using the connected group feature in AVNM. This significantly increases the scale for managing large, complex network topologies. Additionally, higher-scale IP connectivity options are available for customers with advanced requirements.

- Target audience affected  
This update is relevant for network architects, IT professionals, and developers managing large-scale Azure environments, especially those responsible for networking, security, and connectivity across multiple virtual networks.

- Important notes if any  
The high-scale mesh feature is available only in supported Azure regions. Customers should verify regional availability before planning deployments. This enhancement streamlines network management and connectivity for large organizations, reducing operational complexity and improving scalability. For advanced scenarios requiring more than 3,000 virtual networks, contact Microsoft for higher scale options.

Data source: [Azure Updates API](https://azure.microsoft.com/updates?id=571572)

**Details**:

**Azure Update: Generally Available – High-scale mesh in Azure Virtual Network Manager**

**Background and Purpose of the Update:**  
Azure Virtual Network Manager (AVNM) is a centralized management service for configuring and managing connectivity and security across virtual networks (VNets) in Azure. Traditionally, establishing mesh connectivity at scale between VNets required significant manual configuration and was limited in scalability. This update addresses the need for larger, more scalable, and centrally managed mesh network topologies, enabling enterprises to simplify network management and support larger cloud environments.

**Specific Features and Detailed Changes:**  
With this update, the high-scale mesh capability using the "connected group" feature in AVNM is now generally available. Key changes include:
- **Increased Scale:** Customers can now connect up to 3,000 VNets within a single mesh connectivity configuration by default. This is a significant increase over previous limits, supporting larger enterprise environments and complex network topologies.
- **Higher Scale IP Connectivity:** The update also enables higher scale IP connectivity, though specific details are not provided in the announcement.

**Technical Mechanisms and Implementation Methods:**  
- **Connected Group in AVNM:** The "connected group" is a logical grouping of VNets managed within AVNM. By defining a mesh connectivity configuration for a connected group, AVNM automatically establishes full mesh peering between all VNets in the group.
- **Centralized Policy Application:** Network connectivity is managed centrally, reducing the need for manual VNet peering configuration and ensuring consistent connectivity policies across large environments.
- **Automation and Orchestration:** AVNM handles the orchestration of VNet peerings and routing configurations required for mesh connectivity, abstracting complexity from network administrators.

**Use Cases and Application Scenarios:**  
- **Large Enterprise Environments:** Organizations with hundreds or thousands of VNets (e.g., multi-department, multi-region deployments) can now efficiently manage full mesh connectivity.
- **Regulatory and Security Compliance:** Centralized management helps enforce consistent connectivity and security policies across all VNets.
- **Dynamic and Scalable Applications:** Scenarios requiring rapid scaling or dynamic addition/removal of VNets benefit from simplified connectivity management.

**Important Considerations and Limitations:**  
- **Regional Availability:** High-scale mesh is available only in supported Azure regions. Customers should verify regional support before planning deployments.
- **Default Limits:** The default maximum is 3,000 VNets per mesh configuration. For requirements exceeding this, customers may need to request increased limits or consult Azure support.
- **IP Connectivity Scale:** While higher scale IP connectivity is enabled, specific throughput or performance characteristics are not detailed in this update.

**Integration with Related Azure Services:**  
- **Seamless Integration with AVNM:** High-scale mesh is fully integrated into Azure Virtual Network Manager, leveraging its centralized policy and connectivity management capabilities.
- **Compatibility with Azure Networking Services:** Mesh-connected VNets can interoperate with other Azure networking services (e.g., Azure Firewall, VPN Gateway, ExpressRoute) as per standard AVNM configurations.

**Summary:**  
High-scale mesh connectivity in Azure Virtual Network Manager is now generally available, allowing customers to connect up to 3,000 VNets in a single mesh configuration by default, thereby simplifying large-scale network management and enabling higher scale IP connectivity in supported regions.

---


*This report was automatically generated - 2026-09-18 03:02:07 UTC*