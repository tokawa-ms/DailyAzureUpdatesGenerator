# December 10, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: December 10, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Generally Available: FIPS compliant mode for Application Gateway V2 SKUs 

**Published**: December 09, 2025 13:15:11 UTC
**Link**: [Generally Available: FIPS compliant mode for Application Gateway V2 SKUs ](https://azure.microsoft.com/updates?id=536712)

**Update ID**: 536712
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway

**Summary**:

- What was updated  
Azure Application Gateway V2 SKUs now support a FIPS 140-2 compliant mode.

- Key changes or new features  
The update enables Application Gateway V2 to operate in a FIPS 140-2 validated cryptographic mode, meeting US government standards for cryptographic modules. This ensures that all cryptographic operations within the gateway adhere to strict security requirements, enhancing compliance and security posture for regulated environments.

- Target audience affected  
Developers and IT professionals managing secure Azure network infrastructure, especially those in government, defense, finance, or other regulated industries requiring FIPS compliance.

- Important notes if any  
Enabling FIPS mode may impact performance due to the use of FIPS-validated cryptographic modules. Users should validate compatibility with their applications and workloads before enabling this mode. This feature is generally available and can be configured on existing Application Gateway V2 deployments.

**Details**:

The recent Azure update announces the general availability of FIPS 140-2 compliant mode for Application Gateway V2 SKUs, enhancing cryptographic security to meet stringent US government standards. FIPS 140-2 is a federal standard that specifies security requirements for cryptographic modules used within IT products, ensuring data protection and compliance in regulated environments. By enabling FIPS mode, Azure Application Gateway V2 now supports cryptographic operations validated against these standards, making it suitable for workloads requiring high-assurance security.

**Background and Purpose:**  
This update addresses the need for organizations, especially those in government, defense, finance, and healthcare sectors, to comply with federal security mandates. Application Gateway is a Layer 7 load balancer and web application firewall (WAF) service that manages inbound web traffic. Prior to this update, customers requiring FIPS 140-2 compliance had to implement additional controls or use other services. The introduction of FIPS mode directly within Application Gateway V2 simplifies compliance and reduces operational overhead.

**Specific Features and Changes:**  
- Introduction of a FIPS-compliant cryptographic module within the Application Gateway V2 SKU.  
- Support for TLS cipher suites and cryptographic algorithms validated under FIPS 140-2.  
- Ability to enable FIPS mode via configuration settings during gateway creation or update.  
- Ensures that all cryptographic operations, including SSL/TLS termination and backend communication, adhere to FIPS requirements.

**Technical Mechanisms and Implementation:**  
The FIPS mode leverages cryptographic libraries that have been validated against FIPS 140-2 standards. When enabled, the Application Gateway enforces the use of FIPS-approved algorithms such as AES for encryption, SHA-2 for hashing, and RSA or ECDSA for key exchange and digital signatures. TLS protocols and cipher suites are restricted to those compliant with FIPS, disabling weaker or non-validated algorithms. Configuration is typically done through Azure CLI, PowerShell, or ARM templates by setting the `enableFips` flag to true on the Application Gateway resource. Internally, the gateway’s SSL termination process uses FIPS-certified cryptographic modules, ensuring end-to-end compliance.

**Use Cases and Application Scenarios:**  
- Government agencies deploying web applications that must comply with federal security regulations.  
- Financial institutions requiring cryptographic validation for customer-facing portals.  
- Healthcare providers ensuring HIPAA compliance with FIPS-validated encryption.  
- Enterprises operating in regulated industries that mandate FIPS 140-2 compliance for all cryptographic operations.  
- Organizations leveraging Azure Security and Compliance frameworks to meet audit requirements.

**Important Considerations and Limitations:**  
- Enabling FIPS mode may restrict the set of supported TLS cipher suites, potentially impacting compatibility with some legacy clients or devices.  
- Performance overhead could be slightly higher due to the use of FIPS-validated cryptographic modules, although this is generally minimal.  
- FIPS mode is currently available only on Application Gateway V2 SKUs; V1 SKUs do not support this feature.  
- Customers should validate their application and client compatibility with the restricted cipher suites before enabling FIPS mode in production.  
- This mode does not automatically ensure full compliance with all regulatory requirements; it addresses cryptographic module validation only.

**Integration with Related Azure Services:**  
- Azure Key Vault can be used in conjunction with Application Gateway to securely manage SSL/TLS certificates, which when combined with FIPS mode, ensures end-to-end cryptographic compliance.  
- Azure Security Center and Azure Policy can monitor and enforce the use of FIPS mode across Application Gateway instances for governance.  
- Application Gateway’s integration with Azure Firewall and Azure Front Door can complement security posture by providing layered protection with FIPS-validated cryptography.  
- Azure Monitor and Azure Log Analytics can track and audit Application Gateway operations under FIPS mode for compliance reporting.

In summary, the general availability of FIPS 140-2 compliant mode for Azure Application Gateway V2

---


*This report was automatically generated - 2025-12-10 03:01:18 UTC*