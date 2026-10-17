# October 17, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 17, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Public Preview: Azure Databricks Private network gateway

**Published**: October 16, 2026 16:59:02 UTC
**Link**: [Public Preview: Azure Databricks Private network gateway](https://azure.microsoft.com/updates?id=576556)

**Update ID**: 576556
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Analytics, Azure Databricks, Feature

**Summary**:

- What was updated  
Azure Databricks has introduced the Private Network Gateway feature in Public Preview.

- Key changes or new features  
The Private Network Gateway allows serverless compute resources in Azure Databricks to securely connect to your Azure Virtual Network (VNet) and any transitively connected networks via a single managed gateway. This enables direct access to private resources (such as databases, storage accounts, or APIs) within your VNet from Databricks serverless compute, without requiring complex network setups or manual configuration of network peering and firewall rules.

- Target audience affected  
This update is relevant for developers, data engineers, and IT professionals who use Azure Databricks and require secure, scalable connectivity between Databricks serverless compute and private resources in their Azure VNets.

- Important notes  
The feature is currently in Public Preview, so it may not be suitable for production workloads yet. Customers should review Azure Databricks documentation for configuration details and limitations. The gateway simplifies network management and enhances security for serverless workloads, but users should validate compatibility with their existing network architecture and compliance requirements.

**Details**:

**Azure Update Report: Public Preview – Azure Databricks Private Network Gateway**

**Background and Purpose of the Update**  
The introduction of the Private Network Gateway for Azure Databricks addresses the need for secure, scalable connectivity between Databricks serverless compute and customer-managed resources within their Azure Virtual Networks (VNets). Traditionally, serverless compute environments in Databricks operated in isolated networks, limiting direct access to resources such as databases, storage accounts, and other services within a customer’s VNet. This update aims to bridge that gap, providing a managed solution for secure network connectivity.

**Specific Features and Detailed Changes**  
The Private Network Gateway is now available in Public Preview. It enables Databricks serverless compute clusters to connect to resources within a customer’s VNet and any transitively connected networks, all via a single managed gateway. This feature simplifies network architecture by eliminating the need for multiple custom network configurations or manual gateway deployments. The gateway is managed by Azure, reducing operational overhead and ensuring consistent connectivity for serverless workloads.

**Technical Mechanisms and Implementation Methods**  
The gateway operates as a managed network endpoint that facilitates traffic between Databricks serverless compute and customer VNets. It leverages Azure’s networking infrastructure to securely route traffic, ensuring that data flows only through authorized paths. The gateway is provisioned and managed by Azure, requiring minimal configuration from the customer. Connectivity is established using Azure’s native networking capabilities, and the gateway supports transitively connected networks, meaning it can route traffic not only to the primary VNet but also to networks connected via peering or VPN.

**Use Cases and Application Scenarios**  
- **Secure Data Access:** Databricks serverless compute can securely access databases, storage accounts, and other resources within the customer’s VNet for data processing and analytics.
- **Simplified Network Management:** Organizations can centralize network connectivity through a single gateway, reducing complexity and improving maintainability.
- **Hybrid and Multi-Network Architectures:** The gateway supports transitively connected networks, making it suitable for environments with multiple VNets or hybrid cloud setups.
- **Compliance and Security:** By enabling direct connectivity to customer VNets, organizations can enforce network security policies and compliance requirements more effectively.

**Important Considerations and Limitations**  
- The feature is currently in Public Preview, which may imply limited support and potential changes before General Availability.
- Customers must ensure proper configuration of their VNets and transitively connected networks to allow traffic from the managed gateway.
- As a managed solution, certain customization options may be restricted compared to self-managed network gateways.
- Integration with existing network security groups (NSGs), firewalls, and routing policies should be carefully reviewed to avoid unintended access or connectivity issues.

**Integration with Related Azure Services**  
The Private Network Gateway integrates seamlessly with Azure Databricks and Azure networking services such as VNets, VNet peering, and VPN gateways. It enables Databricks serverless compute to interact with Azure resources like Azure SQL Database, Azure Storage, and other services hosted within the customer’s VNet. The managed nature of the gateway ensures compatibility with Azure’s security and monitoring tools, supporting centralized management and observability.

**Summary Sentence**  
Azure Databricks Private Network Gateway, now in Public Preview, provides a managed solution for secure, scalable connectivity between Databricks serverless compute and customer VNets, streamlining network architecture and enabling direct access to resources within transitively connected networks.

---

### 2. Generally Available: External key management for Azure Key Vault Managed HSM

**Published**: October 16, 2026 16:50:27 UTC
**Link**: [Generally Available: External key management for Azure Key Vault Managed HSM](https://azure.microsoft.com/updates?id=574296)

**Update ID**: 574296
**Data source**: Azure Updates API

**Categories**: Launched, Security, Key Vault, Feature

**Summary**:

- What was updated  
External key management for Azure Key Vault Managed HSM is now generally available in all Azure public regions.

- Key changes or new features  
Organizations can now use external key management to retain physical control of key-encryption keys (KEKs) for Azure Key Vault Managed HSM. This enables Azure services that support Managed HSM to use keys stored outside of Azure, meeting regulatory and data sovereignty requirements. The feature allows integration with external Hardware Security Modules (HSMs) or key management systems, providing enhanced flexibility and compliance.

- Target audience affected  
Developers and IT professionals responsible for cloud security, compliance, and key management, especially those in regulated industries or with strict sovereignty requirements.

- Important notes  
This update is significant for organizations needing to comply with regulations that require physical control over encryption keys. It enables secure integration between Azure and external key management solutions, reducing risk and improving compliance posture. Azure services using Managed HSM can now leverage externally managed keys without compromising security or operational efficiency.  
For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=574296

**Details**:

**Comprehensive Technical Explanation: Azure Update – External Key Management for Azure Key Vault Managed HSM (Generally Available)**

**Background and Purpose of the Update:**  
This update announces the general availability of external key management for Azure Key Vault Managed HSM across all Azure public regions. The primary purpose is to address the needs of organizations with regulatory or sovereignty requirements, specifically those who must retain physical control of key-encryption keys (KEKs). This capability enables compliance with strict data protection mandates, such as those found in financial, government, and healthcare sectors, by allowing customers to manage and store their KEKs outside of Azure infrastructure.

**Specific Features and Detailed Changes:**  
With this release, Azure Key Vault Managed HSM now supports the integration of external key management systems. Azure services that utilize Managed HSM can leverage externally managed KEKs, rather than relying solely on keys stored within Azure. This feature expands the flexibility of Managed HSM, allowing customers to use their own hardware security modules (HSMs) or key management appliances to generate, store, and control KEKs. The update provides a secure mechanism for Azure services to access and use these external keys for cryptographic operations, such as encryption and decryption, without compromising compliance requirements.

**Technical Mechanisms and Implementation Methods:**  
The technical implementation involves establishing a secure connection between Azure Key Vault Managed HSM and the external key management system. Typically, this is achieved using industry-standard protocols such as KMIP (Key Management Interoperability Protocol) or custom APIs, depending on the external system’s capabilities. When an Azure service requires access to a KEK, Managed HSM acts as a proxy, securely relaying cryptographic requests to the external key management system. The external system performs the cryptographic operation and returns the result, ensuring that the KEK never leaves the customer-controlled environment. This architecture maintains end-to-end security and auditability, while supporting Azure’s native integration with Managed HSM.

**Use Cases and Application Scenarios:**  
- **Regulatory Compliance:** Organizations subject to regulations such as GDPR, HIPAA, or financial sector requirements can maintain physical custody of their KEKs while using Azure services.
- **Data Sovereignty:** Enterprises operating in jurisdictions with strict data sovereignty laws can ensure that key material remains within their national borders or on-premises infrastructure.
- **Hybrid Cloud Security:** Customers with hybrid deployments can centralize key management in their own HSMs, while leveraging Azure for compute and storage workloads.
- **Multi-cloud Strategies:** Organizations using multiple cloud providers can unify key management across platforms, reducing operational complexity and risk.

**Important Considerations and Limitations:**  
- **Performance:** Cryptographic operations may incur additional latency, as requests traverse between Azure and external key management systems.
- **Availability:** The reliability of cryptographic operations depends on the availability and connectivity of the external key management system.
- **Supported Protocols:** Compatibility with external key management systems is determined by supported protocols and APIs; customers must ensure their systems are compatible.
- **Security:** Proper configuration and network security are essential to prevent unauthorized access to external KEKs.

**Integration with Related Azure Services:**  
External key management is fully integrated with Azure Key Vault Managed HSM, enabling seamless use by Azure services that support Managed HSM for cryptographic operations. This includes Azure Storage, Azure SQL Database, Azure Virtual Machines, and other services requiring encryption-at-rest. The update ensures that these services can leverage externally managed KEKs without modification to their existing workflows, supporting advanced security and compliance requirements.

**Summary Sentence:**  
External key management for Azure Key Vault Managed HSM is now generally available, enabling organizations to retain physical control of key-encryption keys for regulatory and sovereignty compliance while securely integrating with Azure services across all public regions.

---


*This report was automatically generated - 2026-10-17 03:01:44 UTC*