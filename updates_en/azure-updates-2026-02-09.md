# February 09, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: February 09, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Public Preview: Application Gateway for Containers - AKS managed add-on 

**Published**: February 09, 2026 19:45:45 UTC
**Link**: [Public Preview: Application Gateway for Containers - AKS managed add-on ](https://azure.microsoft.com/updates?id=555603)

**Update ID**: 555603
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Features

**Summary**:

- What was updated  
Public preview release of an Azure Kubernetes Service (AKS) managed add-on for Application Gateway for Containers and its Application Load Balancer (ALB) Controller.

- Key changes or new features  
  - The new AKS managed add-on streamlines the deployment and lifecycle management of Application Gateway for Containers and its ALB Controller within AKS clusters.  
  - Developers and IT admins can now enable Application Gateway for Containers directly from the AKS add-on interface, reducing manual setup and configuration.  
  - The add-on provides integrated management, automatic updates, and simplified scaling for containerized application ingress.

- Target audience affected  
  - AKS cluster administrators  
  - DevOps engineers managing containerized workloads  
  - Developers deploying applications on AKS that require advanced ingress, traffic management, or layer 7 load balancing

- Important notes if any  
  - This feature is currently in public preview and not recommended for production workloads.  
  - The managed add-on reduces operational overhead and ensures best practices for deploying Application Gateway for Containers.  
  - For more details and enrollment instructions, refer to the [Azure Update announcement](https://azure.microsoft.com/updates?id=555603).

**Details**:

**Azure Update Report: Public Preview – Application Gateway for Containers as an AKS Managed Add-on**

**Background and Purpose of the Update**  
Azure Kubernetes Service (AKS) is widely used for orchestrating containerized workloads, and secure, scalable ingress is a critical requirement for production deployments. Traditionally, deploying Application Gateway for Containers (AGIC) and its Application Load Balancer (ALB) Controller required manual installation, configuration, and lifecycle management, introducing operational overhead and potential for misconfiguration. The introduction of an AKS managed add-on for Application Gateway for Containers aims to streamline this process, enabling IT teams to deploy and manage ingress at scale with reduced complexity and improved integration.

**Specific Features and Detailed Changes**  
- **Managed Add-on Experience:** The Application Gateway for Containers and its ALB Controller can now be enabled directly as a managed add-on from the AKS cluster configuration, either via the Azure Portal, CLI, or ARM/Bicep templates.
- **Simplified Lifecycle Management:** Azure handles installation, upgrades, and patching of the add-on, ensuring alignment with AKS cluster lifecycle and reducing maintenance burden.
- **Integrated Monitoring and Diagnostics:** The add-on integrates with Azure Monitor, providing out-of-the-box metrics and logs for troubleshooting and performance analysis.
- **Declarative Ingress Management:** Supports Kubernetes-native ingress resources, allowing developers to define routing rules and TLS termination using standard manifests.
- **Security and Compliance:** The managed add-on benefits from Azure’s security controls, including managed identities and network isolation.

**Technical Mechanisms and Implementation Methods**  
- **Controller Deployment:** When the add-on is enabled, Azure provisions the Application Gateway for Containers and deploys the ALB Controller as a managed component within the AKS cluster.
- **Resource Management:** The add-on manages the lifecycle of Application Gateway resources, synchronizing with Kubernetes ingress resources and ensuring state consistency.
- **Networking:** The solution supports integration with AKS-managed virtual networks, enabling secure, private connectivity between the cluster and the Application Gateway.
- **Automation:** Updates and patches to the controller are handled by Azure, minimizing manual intervention and ensuring compatibility with AKS upgrades.

**Use Cases and Application Scenarios**  
- **Production-Grade Ingress:** Enterprises running multi-tenant or microservices-based applications on AKS can leverage the managed add-on for robust, scalable ingress.
- **Zero-Trust Networking:** Organizations requiring strict network boundaries can use private Application Gateway deployments with AKS.
- **DevOps Automation:** Teams can automate ingress provisioning as part of their CI/CD pipelines using the managed add-on and Kubernetes manifests.

**Important Considerations and Limitations**  
- **Public Preview:** The add-on is currently in public preview; it is not recommended for mission-critical production workloads until GA.
- **Feature Parity:** Some advanced features of Application Gateway for Containers may not be available in the managed add-on during preview.
- **Regional Availability:** The preview may be limited to specific Azure regions.
- **Cost Implications:** While the add-on simplifies management, standard Application Gateway and AKS resource charges apply.

**Integration with Related Azure Services**  
- **Azure Monitor:** Native integration for logging and metrics.
- **Azure Policy:** Supports governance and compliance via policy enforcement.
- **Azure Active Directory (AAD):** Managed identities can be used for secure resource access.
- **Azure DevOps/GitHub Actions:** Enables automated deployment and configuration as part of CI/CD workflows.

**Summary:**  
The public preview of the AKS managed add-on for Application Gateway for Containers provides a streamlined, integrated solution for deploying and managing ingress controllers in AKS, reducing operational overhead and improving security and compliance for containerized workloads.

---


*This report was automatically generated - 2026-02-15 16:58:23 UTC*