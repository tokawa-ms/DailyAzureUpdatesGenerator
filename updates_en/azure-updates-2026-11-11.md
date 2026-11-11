# November 11, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 11, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Public Preview: Distributed accelerator for cloud storage on AKS

**Published**: November 10, 2026 20:08:32 UTC
**Link**: [Public Preview: Distributed accelerator for cloud storage on AKS](https://azure.microsoft.com/updates?id=578454)

**Update ID**: 578454
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Azure Container Storage, Feature

**Summary**:

- What was updated  
Azure announced the public preview of Distributed Accelerator for Cloud Storage (DACS) for AI workloads on Azure Kubernetes Service (AKS).

- Key changes or new features  
DACS is a distributed read-through cache deployed within AKS clusters. It leverages local NVMe disks across cluster nodes to cache frequently accessed cloud storage data, significantly improving data access performance for AI and machine learning workloads. DACS is designed to reduce latency and increase throughput when reading large datasets from Azure Blob Storage or other cloud storage services.

- Target audience affected  
This update is relevant for developers and IT professionals running AI, machine learning, or data-intensive workloads on AKS. It is particularly beneficial for those who require high-performance access to cloud storage and are looking to optimize data pipelines and training jobs.

- Important notes if any  
DACS is currently in public preview, so it may not be suitable for production workloads yet. Users should evaluate performance and stability in their environments. Integration requires AKS clusters with NVMe-enabled nodes. Documentation and support are available through Azure for setup and configuration.  
For more details, visit the official Azure Update page: https://azure.microsoft.com/updates?id=578454

**Details**:

**Azure Update Report**

**Title:** Public Preview: Distributed accelerator for cloud storage on AKS  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=578454)

---

**Background and Purpose of the Update:**  
The Distributed Accelerator for Cloud Storage (DACS) is introduced in public preview to address performance bottlenecks for AI workloads running on Azure Kubernetes Service (AKS). AI and machine learning applications often require high-throughput, low-latency access to large datasets stored in cloud storage. Traditional access patterns can lead to latency and bandwidth constraints, especially when multiple nodes in a cluster concurrently access remote storage. DACS aims to optimize data access by leveraging local NVMe storage within AKS clusters, thereby accelerating read operations and improving overall workload efficiency.

---

**Specific Features and Detailed Changes:**  
- **Distributed Read-Through Cache:** DACS operates as a distributed caching layer within the AKS cluster, caching frequently accessed data from cloud storage onto local NVMe disks across cluster nodes.
- **Local NVMe Utilization:** The solution aggregates NVMe disks available on AKS nodes, enabling high-speed local storage for cached data.
- **Cluster-Wide Operation:** DACS is designed to run natively within AKS, ensuring that the cache is distributed and accessible across all participating nodes in the cluster.
- **Public Preview Availability:** The feature is currently in public preview, allowing users to evaluate its performance and integration within their AI workloads on AKS.

---

**Technical Mechanisms and Implementation Methods:**  
DACS is implemented as a distributed read-through cache, meaning that when a node requests data from cloud storage, DACS first checks the local NVMe cache. If the data is not present, it retrieves the data from cloud storage and stores it locally for subsequent access. The cache is distributed, so data cached on one node can be accessed by other nodes, optimizing resource utilization and reducing redundant data transfers. DACS leverages the high-speed NVMe disks attached to AKS nodes, providing low-latency access and high throughput for cached data.

---

**Use Cases and Application Scenarios:**  
- **AI and Machine Learning Workloads:** DACS is particularly beneficial for AI workloads that require repeated access to large datasets stored in Azure cloud storage, such as model training, inference, and data preprocessing.
- **High-Performance Computing (HPC):** Applications with intensive data access patterns can leverage DACS to minimize latency and maximize throughput.
- **Distributed Data Processing:** Scenarios where multiple AKS nodes concurrently access the same datasets can benefit from the distributed caching mechanism, reducing remote storage access and improving scalability.

---

**Important Considerations and Limitations:**  
- **Public Preview Status:** As DACS is in public preview, it may not be suitable for production workloads. Users should evaluate its stability and performance in test environments.
- **NVMe Disk Requirement:** The effectiveness of DACS depends on the availability of NVMe disks on AKS nodes. Clusters without NVMe storage will not benefit from the acceleration.
- **Cache Consistency and Management:** Users should consider cache consistency, eviction policies, and potential data staleness when using DACS, especially in scenarios with frequent data updates.

---

**Integration with Related Azure Services:**  
DACS is designed to integrate seamlessly with AKS, leveraging local NVMe disks provisioned within the cluster. It accelerates access to Azure cloud storage, such as Azure Blob Storage, by caching data locally. The solution complements AKS-native storage options and can be used in conjunction with other Azure services that require high-performance data access.

---

**Summary Sentence:**  
Distributed accelerator for cloud storage (DACS) is now available in public preview for AI workloads on AKS, offering a distributed read-through cache that utilizes local NVMe disks across cluster nodes to accelerate data access from cloud storage.

---

### 2. Generally Available: Azure Functions support for .NET 11

**Published**: November 10, 2026 20:07:45 UTC
**Link**: [Generally Available: Azure Functions support for .NET 11](https://azure.microsoft.com/updates?id=578773)

**Update ID**: 578773
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features, SDK and Tools, Feature

**Summary**:

- What was updated  
Azure Functions now supports .NET 11 in general availability.

- Key changes or new features  
Developers can build Azure Functions apps targeting .NET 11 using the isolated worker model. This enables use of the latest .NET features and improvements, while maintaining the Azure Functions programming model and host integration. The isolated worker model offers greater flexibility, improved dependency management, and enhanced compatibility with modern .NET libraries.

- Target audience affected  
Developers and IT professionals building serverless applications with Azure Functions, especially those looking to leverage .NET 11 features or migrate existing workloads to the latest .NET version.

- Important notes  
.NET 11 support is available only with the isolated worker model, not the in-process model. Existing Azure Functions apps using earlier .NET versions can be upgraded to .NET 11 for improved performance and security. Developers should review compatibility and migration guidance before updating. This update enables access to new .NET 11 language features, performance enhancements, and long-term support for production workloads.

For more details, visit: [Azure Update: Azure Functions support for .NET 11](https://azure.microsoft.com/updates?id=578773)

**Details**:

**Azure Update Report: Azure Functions support for .NET 11 (Generally Available)**  
[Source Link](https://azure.microsoft.com/updates?id=578773)

---

**Background and Purpose of the Update**  
Azure Functions is Microsoft’s serverless compute platform that enables developers to build event-driven applications. The release of .NET 11 support in Azure Functions addresses the need for modern runtime compatibility, allowing developers to leverage the latest .NET features and performance improvements within their serverless workloads. This update ensures that organizations can maintain up-to-date technology stacks and benefit from enhanced security, performance, and developer productivity.

**Specific Features and Detailed Changes**  
- **.NET 11 Support:** Azure Functions now allows developers to target .NET 11 for their function apps, providing access to new language features, APIs, and runtime enhancements introduced in .NET 11.
- **Isolated Worker Model:** The update supports the isolated worker model, which separates the function execution environment from the Azure Functions host process. This model offers greater flexibility in dependency management, improved isolation, and compatibility with the latest .NET runtime.
- **Continued Programming Model and Host Integration:** Developers can continue to use the familiar Azure Functions programming model, including triggers and bindings, and benefit from seamless integration with the Azure Functions host.

**Technical Mechanisms and Implementation Methods**  
- **Project Configuration:** Function apps targeting .NET 11 must be configured to use the isolated worker model. This involves setting the appropriate target framework in the project file (e.g., `<TargetFramework>net11.0</TargetFramework>`) and referencing the Azure Functions Worker SDK.
- **Deployment:** Function apps can be deployed to Azure using standard methods such as Azure CLI, Visual Studio, or GitHub Actions, ensuring compatibility with existing CI/CD pipelines.
- **Execution:** The isolated worker model runs the function logic in a separate process, communicating with the Azure Functions host via gRPC. This architecture allows developers to use any .NET 11 features and libraries without restrictions imposed by the host process.

**Use Cases and Application Scenarios**  
- **Modernization of Serverless Workloads:** Organizations can migrate legacy function apps to .NET 11, taking advantage of improved performance and security.
- **Event-Driven Microservices:** Developers can build scalable, event-driven microservices using the latest .NET features.
- **Integration with Azure Services:** Function apps can respond to events from Azure services such as Azure Event Grid, Azure Service Bus, and Azure Storage, leveraging .NET 11 capabilities.

**Important Considerations and Limitations**  
- **Isolated Worker Requirement:** .NET 11 is only supported in the isolated worker model; in-process execution is not available for this runtime.
- **Dependency Management:** Developers must ensure that all dependencies are compatible with .NET 11 and the isolated worker model.
- **Host Integration:** While host integration is maintained, certain advanced host features may require additional configuration or may not be available in the isolated model.

**Integration with Related Azure Services**  
- **Triggers and Bindings:** Azure Functions apps targeting .NET 11 can use standard triggers and bindings to integrate with Azure services (e.g., HTTP, Timer, Queue, Blob).
- **Monitoring and Diagnostics:** Integration with Azure Application Insights and Azure Monitor is available for tracking function execution and diagnosing issues.
- **CI/CD and DevOps:** Function apps can be integrated with Azure DevOps, GitHub Actions, and other deployment pipelines for automated builds and deployments.

---

**Summary Sentence:**  
Azure Functions support for .NET 11 is now generally available, enabling IT professionals to build and deploy serverless applications using the isolated worker model, while maintaining the Azure Functions programming model and host integration for modern, scalable, and secure workloads.

---

### 3. Public Preview: Azure Front Door adds native gRPC support 

**Published**: November 10, 2026 18:55:53 UTC
**Link**: [Public Preview: Azure Front Door adds native gRPC support ](https://azure.microsoft.com/updates?id=579383)

**Update ID**: 579383
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure Front Door, Features, Services

**Summary**:

**Azure Update Summary: Public Preview – Azure Front Door adds native gRPC support**

- **What was updated:**  
Azure Front Door now supports native gRPC protocol in public preview for both Standard and Premium tiers.

- **Key changes or new features:**  
  - Developers can build and deliver gRPC applications using Azure Front Door, enabling end-to-end gRPC communication.
  - Native gRPC support allows routing calls to specific services and methods, improving traffic distribution and service granularity.
  - Enhanced traffic management for gRPC workloads, including load balancing and failover.
  - Integration with Azure Front Door’s existing features like global routing, SSL termination, and Web Application Firewall (WAF).

- **Target audience affected:**  
  - Developers building microservices and modern cloud-native applications using gRPC.
  - IT professionals managing application delivery, network security, and traffic routing in Azure environments.

- **Important notes:**  
  - This feature is currently in public preview and may not be suitable for production workloads.
  - Users should review documentation for limitations and supported scenarios during preview.
  - Feedback is encouraged to help improve the feature before general availability.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=579383).

**Details**:

**Azure Update Report: Public Preview – Azure Front Door Adds Native gRPC Support**

**Background and Purpose of the Update:**  
Azure Front Door is a global, scalable, and secure entry point for web applications, providing features such as global load balancing, SSL offloading, and application acceleration. The introduction of native gRPC support in Azure Front Door addresses the growing demand for modern, high-performance communication protocols in distributed applications. gRPC is widely used for microservices and real-time client-server communication due to its efficiency and support for streaming. The purpose of this update is to enable IT professionals to build and deliver gRPC applications through Azure Front Door Standard and Premium, leveraging its global infrastructure and advanced routing capabilities.

**Specific Features and Detailed Changes:**  
With this update, Azure Front Door now supports routing gRPC calls natively. This means that users can configure Front Door to handle gRPC traffic, enabling direct routing to specific services and methods. The preview supports both Azure Front Door Standard and Premium SKUs, allowing organizations to utilize gRPC alongside existing HTTP/HTTPS workloads. Key features include:
- Native gRPC protocol support for end-to-end routing.
- Ability to distribute gRPC traffic across backend services.
- Support for routing calls to specific gRPC services and methods.
- Integration with Front Door’s traffic management and load balancing capabilities.

**Technical Mechanisms and Implementation Methods:**  
Azure Front Door implements gRPC support by recognizing and processing gRPC protocol traffic at the edge. This involves handling HTTP/2 requests, which gRPC relies on, and maintaining compatibility with gRPC’s binary serialization and streaming features. Users configure routing rules in Front Door to direct gRPC calls to appropriate backend pools, specifying service and method-level granularity. Traffic distribution is managed using Front Door’s existing load balancing algorithms, ensuring efficient and reliable delivery of gRPC requests to backend services.

**Use Cases and Application Scenarios:**  
- Microservices architectures: Organizations deploying microservices that communicate via gRPC can use Azure Front Door to manage ingress traffic, providing global reach and high availability.
- Real-time applications: Applications requiring low-latency, bidirectional streaming (such as chat, gaming, or IoT telemetry) benefit from Front Door’s gRPC support.
- Multi-region deployments: Enterprises can leverage Front Door’s global distribution to route gRPC traffic to the nearest backend, optimizing performance and resilience.
- API gateways: Azure Front Door can serve as a unified entry point for both REST and gRPC APIs, simplifying management and security.

**Important Considerations and Limitations:**  
- The gRPC support is currently in public preview, which may involve limitations in terms of stability, feature completeness, and support.
- Only Azure Front Door Standard and Premium SKUs are supported in this preview.
- Users should review documentation for any restrictions on protocol versions, streaming support, or integration with existing security policies.
- Preview features may not be suitable for production workloads until general availability.

**Integration with Related Azure Services:**  
Azure Front Door’s gRPC support can be integrated with backend services hosted on Azure Kubernetes Service (AKS), Azure App Service, or Azure Virtual Machines. It complements Azure’s ecosystem by providing a unified entry point for both gRPC and HTTP workloads, enabling seamless integration with Azure Monitor for traffic analytics, Azure Security Center for threat protection, and Azure Traffic Manager for advanced routing.

**Summary Sentence:**  
Azure Front Door now offers native gRPC support in public preview, enabling IT professionals to route and distribute gRPC traffic through its Standard and Premium SKUs, enhancing modern application architectures with efficient, protocol-aware ingress capabilities.

---

### 4. Generally Available: Azure Front Door edge actions 

**Published**: November 10, 2026 18:55:09 UTC
**Link**: [Generally Available: Azure Front Door edge actions ](https://azure.microsoft.com/updates?id=579310)

**Update ID**: 579310
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure Front Door, Features, Services

**Summary**:

- What was updated  
Azure Front Door edge actions are now generally available, enabling serverless compute at the edge for client request/response processing.

- Key changes or new features  
Edge actions allow customers to run lightweight JavaScript functions directly at Azure Front Door’s edge locations. This enables real-time modification of HTTP requests and responses, such as custom authentication, header manipulation, URL rewrites, and personalized content delivery. Functions are executed during the request/response lifecycle, improving performance and reducing latency by avoiding backend round trips.

- Target audience affected  
Developers and IT professionals managing web applications, APIs, and content delivery networks using Azure Front Door. Teams seeking to implement custom logic, security, or personalization at the edge without additional infrastructure will benefit.

- Important notes  
Edge actions are serverless and managed, requiring no additional compute resources. Functions are deployed and managed through Azure Front Door, with support for JavaScript. This feature enhances flexibility and control for application delivery and security scenarios. For implementation details and pricing, refer to the official documentation.

**Details**:

**Azure Update Report: Azure Front Door Edge Actions (General Availability)**

**Background and Purpose of the Update:**  
Azure Front Door is a global, scalable, and secure entry point for web applications, providing load balancing and content delivery. The general availability of Azure Front Door edge actions introduces serverless compute capabilities directly at the edge, enabling customers to execute lightweight JavaScript functions during the client request and response processing. The primary purpose of this update is to empower IT professionals to perform real-time decision-making and custom logic at the edge, enhancing performance, security, and flexibility without the need for backend modifications.

**Specific Features and Detailed Changes:**  
- **Edge Actions:** Customers can now deploy and run JavaScript functions at the Azure Front Door edge nodes. These functions are executed in response to HTTP requests and responses, allowing for dynamic processing and manipulation.
- **Serverless Compute:** The edge actions feature leverages a serverless model, eliminating the need for infrastructure management. Functions are executed on-demand, scaling automatically with traffic.
- **Real-Time Processing:** Functions can inspect, modify, or augment request and response data in real time, enabling scenarios such as custom authentication, header manipulation, URL rewrites, and more.

**Technical Mechanisms and Implementation Methods:**  
- **JavaScript Functions:** Edge actions are authored in JavaScript, providing a familiar and flexible programming environment for developers.
- **Execution at Edge Nodes:** Functions are deployed to Azure Front Door’s global edge network, ensuring low latency and high availability.
- **Integration with Request/Response Pipeline:** Edge actions are triggered during the processing of client requests and responses, allowing for intervention at critical points in the traffic flow.
- **Serverless Execution Model:** No explicit provisioning or scaling is required; Azure manages the execution environment and resources.

**Use Cases and Application Scenarios:**  
- **Custom Authentication and Authorization:** Implement logic to validate tokens or credentials at the edge before forwarding requests to backend services.
- **Header and Cookie Manipulation:** Add, remove, or modify HTTP headers and cookies for compliance, tracking, or personalization.
- **URL Rewriting and Redirects:** Dynamically rewrite URLs or issue redirects based on request parameters or business rules.
- **Security Enhancements:** Block or filter malicious requests, enforce additional security checks, or sanitize input data.
- **A/B Testing and Personalization:** Route traffic based on user attributes or experiment configurations for targeted experiences.

**Important Considerations and Limitations:**  
- **Function Complexity:** Edge actions are intended for lightweight processing; complex or resource-intensive operations may not be suitable.
- **Performance Impact:** While edge actions offer low latency, excessive or poorly optimized functions can impact request processing times.
- **Security:** Functions must be carefully authored to avoid introducing vulnerabilities or exposing sensitive data.
- **Resource Constraints:** There may be limits on execution time, memory, and other resources, as is typical with serverless edge computing.

**Integration with Related Azure Services:**  
- **Azure Front Door:** Edge actions are natively integrated, enhancing Front Door’s capabilities for traffic management, security, and customization.
- **Azure Functions and Logic Apps:** While edge actions provide serverless compute at the edge, more complex workflows can be offloaded to Azure Functions or Logic Apps for backend processing.
- **Azure Application Gateway and CDN:** Edge actions complement these services by providing additional programmability and real-time processing at the network edge.

**Summary Sentence:**  
Azure Front Door edge actions are now generally available, enabling IT professionals to execute lightweight JavaScript functions at the edge for real-time request and response processing, enhancing performance, security, and customization capabilities in a serverless manner.

---

### 5. Public Preview: Azure Route Server dual-stack IPv4/IPv6 support

**Published**: November 10, 2026 18:21:41 UTC
**Link**: [Public Preview: Azure Route Server dual-stack IPv4/IPv6 support](https://azure.microsoft.com/updates?id=579746)

**Update ID**: 579746
**Data source**: Azure Updates API

**Categories**: Networking, Azure Route Server, Features

**Summary**:

- What was updated  
Azure Route Server now supports dual-stack IPv4/IPv6 mode in public preview.

- Key changes or new features  
The update enables Azure Route Server to exchange routes for both IPv4 and IPv6 address families simultaneously across supported hybrid networking connections (such as ExpressRoute and VPN Gateway). Existing IPv4-only connections are unaffected, allowing organizations to adopt IPv6 routing without disrupting current IPv4 setups.

- Target audience affected  
This update is relevant for developers and IT professionals managing hybrid network architectures in Azure, especially those planning to implement or expand IPv6 connectivity alongside IPv4.

- Important notes  
- Dual-stack support is currently in public preview and may not be suitable for production workloads.  
- Organizations can transition to IPv6 routing incrementally, as IPv4 connections remain unchanged.  
- Supported hybrid connections include ExpressRoute and VPN Gateway.  
- Review Azure Route Server documentation for configuration details and limitations during the preview phase.

For more information, see the official Azure Update: [Azure Route Server dual-stack IPv4/IPv6 support](https://azure.microsoft.com/updates?id=579746).

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Route Server dual-stack IPv4/IPv6 support  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579746)

---

**Background and Purpose of the Update:**  
Azure Route Server is a managed service that simplifies dynamic routing between Azure virtual networks and on-premises networks using Border Gateway Protocol (BGP). Traditionally, Route Server has supported IPv4 routing. The increasing adoption of IPv6 due to address exhaustion and modern networking requirements has driven the need for dual-stack support. This update introduces IPv4/IPv6 dual-stack mode in public preview, allowing organizations to seamlessly exchange both IPv4 and IPv6 routes across hybrid networking connections.

**Specific Features and Detailed Changes:**  
- **Dual-stack Mode:** Azure Route Server now supports simultaneous route exchange for both IPv4 and IPv6 address families.
- **Hybrid Connectivity:** The dual-stack mode applies to supported hybrid networking connections, such as ExpressRoute and VPN Gateway, enabling organizations to extend their IPv6 routing capabilities alongside existing IPv4 connectivity.
- **Non-disruptive Adoption:** Existing IPv4 connections remain unchanged, ensuring backward compatibility and a smooth transition for organizations adopting IPv6 routing.

**Technical Mechanisms and Implementation Methods:**  
- **BGP Route Exchange:** Azure Route Server continues to use BGP for dynamic route exchange. In dual-stack mode, BGP sessions can be established for both IPv4 and IPv6, allowing the propagation of routes for each protocol.
- **Configuration:** Administrators can enable dual-stack mode on Route Server instances, configuring both IPv4 and IPv6 BGP peers as required. This enables the Route Server to handle route advertisements and learning for both address families.
- **Supported Connections:** The dual-stack capability is available across supported hybrid networking connections, ensuring interoperability with on-premises routers and gateways that are configured for dual-stack BGP.

**Use Cases and Application Scenarios:**  
- **Hybrid Cloud Deployments:** Enterprises with both IPv4 and IPv6 networks can leverage Azure Route Server to manage dynamic routing across their Azure and on-premises environments.
- **IPv6 Adoption:** Organizations transitioning to IPv6 can use dual-stack mode to gradually introduce IPv6 routing without disrupting existing IPv4 infrastructure.
- **Multi-cloud and Interconnectivity:** Scenarios requiring connectivity between Azure and other cloud providers or remote sites using both IPv4 and IPv6 can benefit from simplified route management.

**Important Considerations and Limitations:**  
- **Public Preview:** The dual-stack IPv4/IPv6 support is currently in public preview, which may include limitations in terms of support, features, and SLAs.
- **Compatibility:** Existing IPv4 connections are unaffected, but users must ensure their on-premises devices and Azure networking resources are properly configured for IPv6 routing and BGP dual-stack operation.
- **Supported Connections:** Dual-stack mode is available only across supported hybrid networking connections; unsupported scenarios may not benefit from this feature.

**Integration with Related Azure Services:**  
- **ExpressRoute and VPN Gateway:** Dual-stack mode enhances integration with ExpressRoute and VPN Gateway, allowing these services to propagate both IPv4 and IPv6 routes through Route Server.
- **Virtual Networks:** Azure Route Server continues to facilitate dynamic routing within Azure Virtual Networks, now with dual-stack capability.
- **Network Security and Monitoring:** Organizations should review their network security policies and monitoring tools to ensure compatibility with IPv6 traffic and route propagation.

**Summary Sentence:**  
Azure Route Server now offers public preview support for IPv4/IPv6 dual-stack mode, enabling seamless route exchange for both address families across supported hybrid networking connections, while maintaining compatibility with existing IPv4 setups.

---


*This report was automatically generated - 2026-11-11 03:03:14 UTC*