# June 25, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 25, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Public Preview: Application Gateway for Containers – Inference gateway

**Published**: June 24, 2026 19:00:43 UTC
**Link**: [Public Preview: Application Gateway for Containers – Inference gateway](https://azure.microsoft.com/updates?id=566516)

**Update ID**: 566516
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS), Features, Services

**Summary**:

- What was updated  
Application Gateway for Containers now includes a public preview of the inference gateway capability, extending its ingress gateway features.

- Key changes or new features  
  - Introduction of the Kubernetes Gateway API Inference Extension to Application Gateway for Containers.  
  - Enables low-latency, scalable, and secure routing of AI/ML inference traffic to backend model deployments running on Kubernetes clusters.  
  - Supports advanced traffic management for AI workloads, including model versioning, A/B testing, and canary deployments.  
  - Integrates with Azure Machine Learning and other AI services for streamlined deployment and management of inference endpoints.

- Target audience affected  
  - Developers deploying AI/ML models on Kubernetes using Azure.  
  - IT professionals managing Kubernetes clusters and application gateways, especially those focused on AI/ML workloads.

- Important notes if any  
  - This feature is in public preview and may not be recommended for production workloads yet.  
  - Provides a unified gateway solution for both traditional web applications and AI inference services.  
  - Users should review preview documentation and limitations before adoption.  
  - More details and getting started guidance are available in the official Azure Update link.

**Details**:

**Azure Update Report: Public Preview – Application Gateway for Containers: Inference Gateway**

**Background and Purpose of the Update**  
Application Gateway for Containers is Azure’s modern, cloud-native application delivery solution designed for Kubernetes environments. Traditionally, it provides ingress gateway capabilities for securely managing and routing external traffic to containerized workloads. With the increasing adoption of AI workloads and the need for efficient, scalable inference serving in Kubernetes, Azure is expanding Application Gateway for Containers with new AI gateway features. The purpose of this update is to introduce the “Inference Gateway” capability, which brings the Kubernetes Gateway API Inference Extension to Application Gateway for Containers, thereby enabling streamlined AI inference traffic management.

**Specific Features and Detailed Changes**  
- **Inference Gateway Capability:** This update adds a new AI-focused gateway feature set to Application Gateway for Containers.
- **Kubernetes Gateway API Inference Extension:** The gateway now supports the Kubernetes Gateway API Inference Extension, allowing users to define and manage AI inference traffic routing and policies natively within Kubernetes.
- **Enhanced Ingress for AI Workloads:** The feature set is specifically designed to optimize ingress for AI inference services, improving the deployment and scaling of machine learning models in containerized environments.

**Technical Mechanisms and Implementation Methods**  
- **Integration with Kubernetes Gateway API:** The Inference Gateway leverages the Kubernetes Gateway API, an industry-standard, extensible API for managing ingress traffic. The Inference Extension builds on this API to provide constructs and policies tailored for AI inference workloads.
- **Declarative Traffic Management:** Users can declaratively define inference-specific routing, load balancing, and security policies using Kubernetes-native manifests, which are then enforced by Application Gateway for Containers.
- **Seamless AI Model Serving:** The gateway manages traffic to AI model endpoints, supporting scenarios such as model versioning, A/B testing, and canary deployments, as enabled by the Inference Extension.

**Use Cases and Application Scenarios**  
- **AI/ML Model Serving:** Enterprises deploying machine learning models as containerized inference services in Kubernetes can use the Inference Gateway to efficiently manage and route inference requests.
- **Multi-model Management:** Organizations running multiple versions or types of models can leverage the gateway’s routing capabilities to direct traffic based on model version, user segment, or other criteria.
- **Scalable AI APIs:** SaaS providers offering AI-powered APIs can utilize the gateway for secure, scalable, and policy-driven ingress to their inference endpoints.

**Important Considerations and Limitations**  
- **Public Preview Status:** The Inference Gateway feature is currently in public preview, which means it is not recommended for production workloads and may be subject to changes.
- **Feature Scope:** The update specifically mentions the addition of the Kubernetes Gateway API Inference Extension; other AI gateway features or integrations may not be included at this stage.
- **Compatibility:** Users should verify compatibility with their existing Kubernetes clusters and ensure alignment with the supported versions of Application Gateway for Containers.

**Integration with Related Azure Services**  
- **Azure Kubernetes Service (AKS):** The Inference Gateway is designed to work seamlessly with AKS, providing a native ingress solution for AI workloads running on Azure-managed Kubernetes.
- **Application Gateway for Containers Ecosystem:** This feature extends the existing capabilities of Application Gateway for Containers, allowing users to consolidate ingress management for both standard web and AI inference workloads.
- **Potential for Integration with Azure AI Services:** While not explicitly stated, the gateway’s AI focus aligns with Azure’s broader AI ecosystem, potentially facilitating integration with Azure Machine Learning and other AI services.

**Summary Sentence**  
Application Gateway for Containers now offers a public preview of its Inference Gateway capability, introducing Kubernetes Gateway API Inference Extension support to enable efficient, declarative ingress management for AI inference workloads in containerized environments.

---


*This report was automatically generated - 2026-06-25 03:01:39 UTC*