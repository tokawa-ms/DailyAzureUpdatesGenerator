# February 04, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: February 04, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Public Preview: X-Forwarded-For (XFF) grouping for rate limiting on Application Gateway WAF v2

**Published**: February 03, 2026 20:30:31 UTC
**Link**: [Public Preview: X-Forwarded-For (XFF) grouping for rate limiting on Application Gateway WAF v2](https://azure.microsoft.com/updates?id=555205)

**Update ID**: 555205
**Data source**: Azure Updates API

**Categories**: In development, Networking, Security, Web Application Firewall

**Summary**:

- What was updated  
Azure Application Gateway Web Application Firewall (WAF) v2 now supports public preview of rate-limiting grouping based on the X-Forwarded-For (XFF) HTTP header.

- Key changes or new features  
This update introduces new GroupBy options for rate limiting that leverage the XFF header, allowing more accurate client IP identification when Application Gateway is deployed behind proxies or Content Delivery Networks (CDNs). This enhancement enables more precise and effective rate limiting by grouping requests according to the originating client IP rather than the proxy IP.

- Target audience affected  
Developers and IT professionals managing Application Gateway WAF deployments, especially those operating behind proxies or CDNs, will benefit from improved rate-limiting controls. Security teams can better mitigate abuse and DDoS attacks by accurately tracking client request rates.

- Important notes if any  
This feature is currently in public preview, so it should be tested in non-production environments before widespread use. Proper configuration of the XFF header by upstream proxies or CDNs is required for accurate client IP extraction. Review Azure documentation for implementation guidance and limitations.

**Details**:

The recent public preview update for Azure Application Gateway Web Application Firewall (WAF) v2 introduces enhanced rate-limiting capabilities by supporting grouping based on the X-Forwarded-For (XFF) HTTP header, addressing a critical need for accurate client identification in complex network topologies.

**Background and Purpose**  
Application Gateway WAF v2 provides centralized protection for web applications against common threats and attacks, including rate limiting to mitigate denial-of-service (DoS) and brute-force attacks. Traditionally, rate limiting was applied based on the client IP address as seen by the Application Gateway. However, in modern architectures where Application Gateway is deployed behind proxies, load balancers, or Content Delivery Networks (CDNs), the client IP observed by the gateway is often the IP of the last proxy rather than the original client. This obscures true client identity, causing ineffective or overly broad rate limiting. The update enables rate limiting to be grouped by the original client IP extracted from the X-Forwarded-For HTTP header, improving accuracy and fairness in traffic control.

**Specific Features and Detailed Changes**  
- Introduction of new GroupBy options for rate limiting rules that use the X-Forwarded-For header value as the key for grouping requests.
- Support for parsing and extracting the client IP from the XFF header, which typically contains a comma-separated list of IPs representing the client and proxy chain.
- Ability to configure whether to use the first IP (original client) or last IP in the XFF header for grouping.
- Retains existing IP-based grouping for backward compatibility and flexibility.
- This feature is currently in public preview, allowing customers to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
When a request reaches Application Gateway WAF v2, the WAF inspects incoming HTTP headers. If rate limiting is enabled with XFF grouping, the WAF extracts the client IP from the configured position in the XFF header (commonly the first IP). This IP is then used as the grouping key for rate limiting counters instead of the source IP address of the TCP connection. The WAF maintains counters per client IP and enforces configured thresholds accordingly. This requires careful parsing of the XFF header, validation of IP formats, and handling of edge cases such as missing or malformed headers. Configuration is done via WAF custom rules where the GroupBy field now supports XFF-based options.

**Use Cases and Application Scenarios**  
- Deployments where Application Gateway is behind Azure Front Door, third-party CDNs, or reverse proxies that forward client IPs via XFF headers.
- Scenarios requiring granular rate limiting per original client IP to prevent a single client from overwhelming backend services despite proxy IP masking.
- Multi-tenant SaaS applications where fair usage policies depend on accurate client identification.
- Environments with complex network chains where relying on TCP source IP is insufficient or misleading.

**Important Considerations and Limitations**  
- The accuracy of rate limiting depends on the trustworthiness of the XFF header; if clients or intermediate proxies can spoof this header, rate limiting may be bypassed or misapplied.
- Customers should ensure that only trusted proxies add or modify the XFF header to prevent IP spoofing.
- The feature is in public preview; it may have limitations or require updates before general availability.
- Proper configuration is essential to select the correct IP position in the XFF header, as different proxies append IPs differently.
- Monitoring and logging should be enhanced to verify that grouping behaves as expected.

**Integration with Related Azure Services**  
- Azure Front Door and Azure CDN commonly insert or preserve XFF headers, making this feature highly relevant for solutions combining these services with Application Gateway.
- Azure Monitor and Azure Sentinel can be used to analyze WAF logs and metrics to observe the impact of XFF-based rate limiting.
- Integration with Azure Policy can help enforce configuration standards for WAF rules using XFF grouping.
- This update complements

---

### 2. Generally Available: Azure Container Storage v2.1.0 now with Elastic SAN integration and on demand installation

**Published**: February 03, 2026 20:30:31 UTC
**Link**: [Generally Available: Azure Container Storage v2.1.0 now with Elastic SAN integration and on demand installation](https://azure.microsoft.com/updates?id=553917)

**Update ID**: 553917
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Compute, Azure Container Storage, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Container Storage (ACS) version 2.1.0 has reached general availability.

- Key changes or new features  
This release introduces native integration with Azure Elastic SAN, enabling high-performance, scalable block storage for containerized workloads. Additionally, ACS v2.1.0 offers a lightweight, on-demand installation model that streamlines deployment and operational overhead for Kubernetes environments by allowing components to be installed as needed rather than upfront.

- Target audience affected  
Developers and IT professionals managing Kubernetes clusters on Azure who require scalable, performant persistent storage solutions will benefit. This update is particularly relevant for those leveraging containerized applications needing flexible storage provisioning and simplified storage management.

- Important notes if any  
The Elastic SAN integration enhances storage performance and scalability for stateful container workloads. The on-demand installation model reduces complexity and resource consumption during setup, improving agility in DevOps workflows. Users should review compatibility and upgrade paths to ensure smooth migration to this version.

For more details, visit: https://azure.microsoft.com/updates?id=553917

**Details**:

Azure Container Storage (ACS) v2.1.0 has reached general availability, introducing significant enhancements aimed at improving storage flexibility and deployment efficiency for Kubernetes workloads on Azure. This update primarily integrates native support for Azure Elastic SAN and implements an on-demand, lightweight installation model, streamlining the provisioning and management of persistent storage in containerized environments.

**Background and Purpose**  
Azure Container Storage is a cloud-native storage solution designed to provide persistent, scalable, and high-performance storage for Kubernetes clusters running on Azure. Prior versions required more involved installation processes and lacked native integration with Azure’s Elastic SAN, a high-throughput, low-latency block storage service optimized for enterprise workloads. The purpose of this update is twofold: to leverage Elastic SAN’s capabilities for container storage and to simplify ACS deployment, thereby enhancing operational agility and performance for stateful containerized applications.

**Specific Features and Detailed Changes**  
1. **Native Elastic SAN Support:** ACS v2.1.0 now directly integrates with Azure Elastic SAN, enabling Kubernetes workloads to consume Elastic SAN volumes as persistent storage. This integration allows containers to benefit from Elastic SAN’s high IOPS, low latency, and enterprise-grade durability, which is critical for databases, analytics, and other I/O intensive applications.

2. **On-Demand Installation Model:** The new installation approach is lightweight and modular, allowing ACS components to be deployed dynamically as needed rather than as a monolithic package. This reduces the initial setup complexity, accelerates deployment times, and minimizes resource consumption when ACS is idle or partially used.

**Technical Mechanisms and Implementation Methods**  
The Elastic SAN integration is implemented via the Container Storage Interface (CSI) driver that ACS provides, which has been updated to support Elastic SAN APIs for volume provisioning, attachment, and lifecycle management. The CSI driver communicates with the Azure Resource Manager (ARM) to orchestrate Elastic SAN volume creation and management seamlessly within Kubernetes.

The on-demand installation leverages Kubernetes Operators and Helm charts that enable dynamic component deployment. Instead of installing all ACS components upfront, the system installs core modules first and then pulls in additional features or drivers as workloads request them. This modular architecture improves maintainability and allows for easier upgrades or rollback.

**Use Cases and Application Scenarios**  
- **Stateful Applications:** Databases (SQL Server, PostgreSQL), messaging systems (Kafka), and analytics platforms running in Kubernetes can utilize Elastic SAN-backed persistent volumes to achieve high throughput and low latency.  
- **DevOps and CI/CD Pipelines:** The on-demand installation model supports rapid environment provisioning and teardown, ideal for ephemeral test clusters or development sandboxes.  
- **Hybrid and Multi-Cluster Deployments:** ACS with Elastic SAN can be used in multi-cluster Kubernetes setups requiring consistent, performant storage accessible across clusters or regions.

**Important Considerations and Limitations**  
- Elastic SAN availability is region-specific; ensure your Kubernetes cluster is deployed in a supported Azure region.  
- The on-demand installation model requires Kubernetes cluster versions compatible with the ACS operator and Helm chart versions; verify compatibility before upgrading.  
- While Elastic SAN offers high performance, cost implications should be evaluated based on workload IOPS and capacity requirements.  
- Backup and disaster recovery strategies should be revisited to incorporate Elastic SAN volumes, as snapshot and replication mechanisms may differ from previous ACS storage backends.

**Integration with Related Azure Services**  
- **Azure Kubernetes Service (AKS):** ACS v2.1.0 is optimized for AKS, enabling seamless persistent storage provisioning within managed Kubernetes clusters.  
- **Azure Monitor and Azure Policy:** Integration allows monitoring of storage performance and enforcing compliance policies on storage usage.  
- **Azure Resource Manager (ARM):** The CSI driver interacts with ARM APIs to provision and manage Elastic SAN resources dynamically.  
- **Azure Backup and Azure Site Recovery:** While not directly integrated, these services can be configured to protect Elastic SAN volumes used by ACS.

In summary, Azure Container Storage v2.1.0’s

---

### 3. Public Preview: Azure Kubernetes Fleet Manager namespace-scoped resource placement 

**Published**: February 03, 2026 20:30:31 UTC
**Link**: [Public Preview: Azure Kubernetes Fleet Manager namespace-scoped resource placement ](https://azure.microsoft.com/updates?id=548198)

**Update ID**: 548198
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Azure Kubernetes Fleet Manager

**Summary**:

- What was updated  
Azure Kubernetes Fleet Manager introduced namespace-scoped resource placement in public preview.

- Key changes or new features  
This feature enables fine-grained control over selecting and propagating individual namespace-scoped Kubernetes resources across multiple clusters within a fleet. Developers and IT professionals can now specify which namespaces and their resources are deployed to target clusters, improving resource management and consistency in multi-cluster environments.

- Target audience affected  
Kubernetes developers, cluster administrators, and IT professionals managing multi-cluster Kubernetes deployments using Azure Kubernetes Fleet Manager.

- Important notes if any  
This capability is currently in public preview, so users should evaluate it in non-production environments and provide feedback. It enhances multi-cluster resource governance but may have limitations typical of preview features. Refer to Azure documentation for detailed guidance on implementation and best practices.

**Details**:

The Azure Kubernetes Fleet Manager’s new public preview feature, namespace-scoped resource placement, enhances multi-cluster management by enabling precise control over the selection and propagation of individual namespace-scoped Kubernetes resources across multiple clusters within a fleet. This update addresses the complexity of managing namespace-specific configurations and workloads consistently at scale, improving operational efficiency and governance in hybrid and multi-cloud Kubernetes environments.

**Background and Purpose**  
Azure Kubernetes Fleet Manager is designed to simplify the management of multiple Kubernetes clusters by providing centralized control and policy enforcement. Previously, resource placement capabilities primarily focused on cluster-scoped resources, limiting granular control over namespace-scoped resources such as ConfigMaps, Secrets, and custom resources that are critical for application-specific configurations. The namespace-scoped resource placement feature was introduced to fill this gap, allowing IT professionals to selectively propagate resources at the namespace level, thereby aligning resource distribution with application boundaries and operational requirements.

**Specific Features and Detailed Changes**  
- **Fine-Grained Resource Selection:** Users can now specify individual namespace-scoped resources to be placed across clusters, rather than applying blanket policies at the cluster or fleet level.  
- **Selective Propagation:** This feature supports selective replication of resources such as Deployments, Services, ConfigMaps, Secrets, and other namespace-scoped Kubernetes objects, enabling tailored configurations per cluster or environment.  
- **Namespace-Level Targeting:** Placement policies can be scoped to specific namespaces, allowing different namespaces within the same cluster to receive different resource sets based on business or technical needs.  
- **Preview Status:** As a public preview, this feature is available for testing and feedback but may have evolving APIs and capabilities.

**Technical Mechanisms and Implementation Methods**  
Namespace-scoped resource placement leverages the Fleet Manager’s control plane to monitor and reconcile specified namespace-scoped resources across registered clusters. The mechanism involves:  
- Defining placement policies that declare which namespace-scoped resources should be propagated and to which clusters or namespaces.  
- The Fleet Manager’s controllers continuously watch for changes in the source namespace resources and synchronize them to target clusters, ensuring consistency.  
- Conflict resolution and versioning are managed to prevent drift and maintain resource integrity.  
- Integration with Kubernetes RBAC and Azure AD ensures secure access and authorization during propagation.

**Use Cases and Application Scenarios**  
- **Multi-Environment Configuration Management:** Propagate environment-specific ConfigMaps or Secrets to development, staging, and production clusters selectively.  
- **Application Lifecycle Management:** Deploy application manifests scoped to namespaces across multiple clusters for consistent application delivery.  
- **Compliance and Security:** Enforce security policies or network configurations at the namespace level across clusters to meet regulatory requirements.  
- **Hybrid and Multi-Cloud Deployments:** Manage namespace-scoped resources across on-premises and cloud clusters uniformly.

**Important Considerations and Limitations**  
- Being in public preview, users should expect potential changes and should not use this feature in production-critical environments without thorough testing.  
- Namespace-scoped resource placement currently supports a subset of Kubernetes resource types; users should verify compatibility with their resource manifests.  
- Propagation latency and conflict handling depend on the fleet size and network conditions.  
- Proper RBAC configurations are essential to avoid unauthorized resource propagation.  
- Monitoring and logging capabilities should be enabled to track placement operations and troubleshoot issues.

**Integration with Related Azure Services**  
- **Azure Arc-enabled Kubernetes:** Namespace-scoped resource placement extends Azure Arc’s multi-cluster management capabilities, enabling seamless governance of connected clusters.  
- **Azure Policy:** Can be used alongside to enforce compliance and guardrails on propagated resources.  
- **Azure Monitor:** Integration allows monitoring of resource placement operations and cluster health.  
- **Azure Active Directory:** Provides identity and access management for secure control plane operations.

In summary, the namespace-scoped resource placement feature in Azure Kubernetes Fleet Manager public preview offers IT professionals enhanced granularity and control in managing Kubernetes resources across multiple clusters, aligning resource distribution with organizational and application-specific requirements, and improving multi

---


*This report was automatically generated - 2026-02-04 03:02:13 UTC*