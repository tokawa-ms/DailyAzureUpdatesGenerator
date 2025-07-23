# July 23, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: July 23, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Public Preview: Web Application Firewall (WAF) running on Application Gateway for Containers

**Published**: July 22, 2025 16:00:45 UTC
**Link**: [Public Preview: Web Application Firewall (WAF) running on Application Gateway for Containers](https://azure.microsoft.com/updates?id=498272)

**Update ID**: 498272
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS), Web Application Firewall, Features, Services

**Summary**:

- What was updated  
Azure Application Gateway for Containers now supports Web Application Firewall (WAF) in public preview.

- Key changes or new features  
The integration of WAF enables enhanced layer 7 security for containerized workloads running in Kubernetes clusters. Developers and IT professionals can now apply WAF policies directly on Application Gateway for Containers to protect applications from common web vulnerabilities and attacks such as SQL injection and cross-site scripting. This update extends Azure’s dynamic traffic management and load balancing capabilities with built-in security enforcement at the application layer.

- Target audience affected  
Developers and IT professionals managing containerized applications on Azure Kubernetes Service (AKS) or other Kubernetes platforms who require advanced security controls integrated with application delivery and load balancing.

- Important notes if any  
This feature is currently in public preview, so it should be used with caution in production environments. Users should review WAF policy configurations and monitor performance impacts when enabling WAF on Application Gateway for Containers. Feedback during the preview phase is encouraged to improve the service.  

Reference: https://azure.microsoft.com/updates?id=498272

**Details**:

The recent public preview release of Web Application Firewall (WAF) support on Application Gateway for Containers marks a significant enhancement in Azure’s layer 7 load balancing and security capabilities tailored for Kubernetes workloads. Application Gateway for Containers is designed to provide dynamic traffic management and application delivery for containerized applications running within AKS or other Kubernetes clusters. By integrating WAF functionality directly into this container-native Application Gateway, Azure enables enterprises to enforce robust, centralized web security policies without sacrificing the scalability and agility of container orchestration.

**Background and Purpose:**  
Traditionally, Application Gateway has offered WAF capabilities to protect web applications from common threats such as SQL injection, cross-site scripting, and other OWASP Top 10 vulnerabilities. However, these capabilities were primarily available on the standard Application Gateway service, which is typically used for VM or App Service workloads. With the increasing adoption of Kubernetes and containerized microservices architectures, there was a need to extend these security features natively into Application Gateway for Containers, which is optimized for dynamic, ephemeral container environments. This update addresses that gap by enabling WAF on Application Gateway for Containers, allowing organizations to apply consistent security policies at the ingress layer of their containerized applications.

**Specific Features and Detailed Changes:**  
- **WAF Integration:** The preview introduces the ability to enable WAF policies on Application Gateway for Containers, leveraging the same core WAF engine used in the standard Application Gateway.  
- **OWASP Core Rule Sets:** Support for OWASP CRS 3.2 or later, providing protection against a broad spectrum of web vulnerabilities.  
- **Custom Rules:** Users can define custom WAF rules to tailor protection based on specific application requirements or threat models.  
- **Logging and Monitoring:** Integration with Azure Monitor and Log Analytics for detailed WAF logs, alerts, and diagnostics, enabling security teams to track and respond to threats effectively.  
- **Policy Management:** WAF policies can be managed declaratively via ARM templates, Azure CLI, or Kubernetes manifests, aligning with infrastructure-as-code and GitOps practices.  

**Technical Mechanisms and Implementation Methods:**  
Application Gateway for Containers operates as a Kubernetes ingress controller that dynamically configures the underlying Application Gateway to route traffic to containerized workloads. With WAF enabled, incoming HTTP/HTTPS requests are inspected at the Application Gateway layer before being forwarded to backend pods. The WAF engine performs deep packet inspection, pattern matching, and anomaly detection based on configured rules. The integration is implemented such that WAF policies are applied seamlessly without requiring changes to the container workloads themselves. Configuration is typically managed through Kubernetes ingress annotations or custom resource definitions (CRDs) that specify WAF policy attachments.

**Use Cases and Application Scenarios:**  
- **Secure Kubernetes Ingress:** Organizations running microservices on AKS can use Application Gateway for Containers with WAF to protect their APIs and web applications from common web attacks.  
- **Multi-tenant Environments:** Enterprises hosting multiple applications or tenants on a single AKS cluster can enforce distinct WAF policies per ingress, ensuring tailored security controls.  
- **DevSecOps Pipelines:** Integration with infrastructure-as-code enables automated deployment of WAF policies alongside application updates, embedding security into CI/CD workflows.  
- **Regulatory Compliance:** Helps meet compliance requirements (e.g., PCI DSS, HIPAA) by providing application-layer firewall protections and detailed logging.  

**Important Considerations and Limitations:**  
- **Preview Status:** As a public preview feature, WAF on Application Gateway for Containers may have limited SLA guarantees and could undergo changes before general availability. Production use should be carefully evaluated.  
- **Performance Impact:** Enabling WAF introduces additional processing overhead at the ingress layer, which may affect latency and throughput; performance testing is recommended.  
- **Rule Tuning:** Default OWASP rules may generate false positives; tuning custom rules and exclusions is often necessary to avoid blocking legitimate traffic.  
- **Feature Parity:** Some advanced WAF features available on the

---


*This report was automatically generated - 2025-07-23 03:01:12 UTC*