# November 26, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 26, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Public Preview: ECMP Nexthop 

**Published**: November 25, 2026 23:14:20 UTC
**Link**: [Public Preview: ECMP Nexthop ](https://azure.microsoft.com/updates?id=582326)

**Update ID**: 582326
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Virtual Network, Management, Services, Feature

**Summary**:

- What was updated  
Azure Virtual Network now supports Equal-Cost Multi-Path (ECMP) routing in public preview.

- Key changes or new features  
ECMP routing allows customers to distribute network traffic across multiple network appliances using a single user-defined route (UDR). Users can configure 2 to 16 next-hop IP addresses for a UDR, enabling automatic load balancing and improved network resiliency. This feature helps optimize traffic flows and supports scaling out network virtual appliances (NVAs) without complex routing configurations.

- Target audience affected  
This update is relevant for developers and IT professionals managing Azure Virtual Networks, especially those deploying NVAs for scenarios such as firewalls, load balancers, or custom routing solutions.

- Important notes if any  
ECMP routing is currently available in public preview and may not be suitable for production workloads. Customers should test thoroughly before deploying in critical environments. The feature is designed to simplify network architecture and improve performance for multi-appliance scenarios. For more details and limitations, refer to the official Azure documentation.

**Details**:

**Azure Update: Public Preview – ECMP Nexthop for Azure Virtual Network**

**Background and Purpose of the Update**  
The introduction of Equal-Cost Multi-Path (ECMP) routing for Azure Virtual Network addresses the need for improved network traffic distribution and high availability within cloud environments. Traditionally, user-defined routes (UDRs) in Azure Virtual Networks allowed only a single next hop, which could lead to bottlenecks and single points of failure when routing traffic through network virtual appliances (NVAs) or firewalls. This update aims to enhance scalability, redundancy, and performance by enabling traffic distribution across multiple next hops.

**Specific Features and Detailed Changes**  
With this public preview, customers can now configure a single UDR with 2 to 16 next-hop IP addresses. This allows Azure to automatically distribute outbound traffic destined for a particular prefix evenly across the specified next hops. The primary feature is the ability to define multiple next-hop addresses in a single route, which previously was not supported. This update is particularly beneficial for scenarios requiring load balancing and high availability at the routing level.

**Technical Mechanisms and Implementation Methods**  
ECMP routing works by leveraging the Azure Virtual Network routing engine to perform hash-based traffic distribution. When a packet matches a UDR with multiple next hops, Azure computes a hash based on packet attributes (such as source/destination IP and port) and selects one of the configured next hops for forwarding. This ensures that flows are consistently routed through the same next hop, preserving session affinity. The configuration is managed through the Azure Portal, CLI, or ARM templates by specifying multiple next-hop IPs in the UDR definition.

**Use Cases and Application Scenarios**  
- **High Availability NVAs:** Distribute traffic across multiple instances of NVAs (e.g., firewalls, load balancers) for redundancy and failover.
- **Scalable Security Appliances:** Scale out security appliances by routing traffic across several appliances without the need for an external load balancer.
- **Hybrid Connectivity:** Enhance resilience for on-premises connectivity by distributing traffic across multiple VPN gateways or ExpressRoute circuits.
- **Service Chaining:** Implement advanced service chaining scenarios where traffic must traverse multiple appliances for inspection or processing.

**Important Considerations and Limitations**  
- The feature is currently in public preview and may not be suitable for production workloads.
- Customers can configure between 2 and 16 next-hop IP addresses per UDR.
- All next hops must be reachable and functional; failed next hops may result in dropped traffic until manual intervention or reconfiguration.
- ECMP does not provide health monitoring of next hops—external monitoring and failover mechanisms are recommended.
- Integration with network security groups (NSGs), route tables, and other Azure networking constructs remains unchanged.

**Integration with Related Azure Services**  
ECMP Nexthop integrates seamlessly with Azure Virtual Network routing and user-defined routes. It complements existing features such as NVAs, Azure Firewall, and custom routing scenarios. Customers can use ECMP in conjunction with Azure’s network monitoring tools to observe traffic distribution and performance. The feature also enhances integration with hybrid connectivity solutions (VPN Gateway, ExpressRoute) by providing more resilient routing options.

**Summary**  
The public preview of ECMP Nexthop for Azure Virtual Network enables customers to distribute traffic across multiple network appliances using a single user-defined route, enhancing scalability, redundancy, and performance for critical network workloads.

---

### 2. Retirement: Support for Java 8, 11 and 17 in Azure Functions ends on September 1, 2027

**Published**: November 25, 2026 21:53:30 UTC
**Link**: [Retirement: Support for Java 8, 11 and 17 in Azure Functions ends on September 1, 2027](https://azure.microsoft.com/updates?id=568586)

**Update ID**: 568586
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Internet of Things, Azure Functions, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of support for Java 8, 11, and 17 in Azure Functions, effective September 1, 2027.

- Key changes or new features  
After this date, Azure Functions will no longer provide security updates or customer support for applications using Java 8, 11, or 17. Existing apps will continue to run, but will not receive maintenance or security patches for these Java versions.

- Target audience affected  
This update impacts developers and IT professionals who deploy or manage Azure Functions applications using Java 8, 11, or 17.

- Important notes if any  
To maintain security and support, users should plan to migrate their Azure Functions apps to newer, supported Java versions before September 1, 2027. Continuing to use unsupported Java versions may expose applications to security risks and lack of technical assistance. Review your current deployments and update your migration plans accordingly.

For more details, visit: https://azure.microsoft.com/updates?id=568586

**Details**:

**Azure Update Report: Retirement of Java 8, 11, and 17 Support in Azure Functions (Effective September 1, 2027)**

**Background and Purpose of the Update:**  
Microsoft Azure is announcing the retirement of support for Java 8, 11, and 17 within Azure Functions, effective September 1, 2027. This update is part of Azure’s lifecycle management strategy to ensure that supported runtime environments remain secure, performant, and aligned with industry standards. The retirement aims to encourage customers to transition to newer Java versions, which typically offer enhanced security, performance improvements, and long-term support.

**Specific Features and Detailed Changes:**  
After September 1, 2027, Azure Functions will no longer provide security updates or customer service for applications running on Java 8, 11, or 17. While existing apps will continue to operate, they will not receive any further patches or technical support. This change affects all Azure Functions hosting environments that utilize these Java runtime versions. The update does not impact the execution of current workloads but removes official support and maintenance.

**Technical Mechanisms and Implementation Methods:**  
Azure Functions currently allows users to select Java runtime versions (8, 11, 17) as part of their function app configuration. The retirement will be implemented by ceasing the release of security updates and technical support for these versions. Azure will likely update its documentation and portal interfaces to reflect the unsupported status post-retirement. Customers will need to manually upgrade their function apps to newer, supported Java versions to maintain access to security patches and support. The mechanism does not forcibly stop workloads but shifts responsibility for maintenance and risk management to the customer.

**Use Cases and Application Scenarios:**  
This update primarily impacts organizations running serverless workloads, event-driven architectures, or microservices on Azure Functions with Java 8, 11, or 17. Common scenarios include backend processing, API endpoints, and integration tasks. Teams relying on these Java versions for compatibility or legacy reasons must plan migration strategies to newer Java versions before the retirement date to ensure continued security and support.

**Important Considerations and Limitations:**  
- **Security Risk:** Post-retirement, applications running on Java 8, 11, or 17 will not receive security updates, increasing vulnerability exposure.
- **Support Limitation:** Microsoft will not provide customer service for issues related to these Java versions in Azure Functions.
- **Operational Continuity:** Apps will continue to run, but without maintenance, which may lead to compliance and operational risks.
- **Migration Requirement:** Customers must proactively upgrade to newer Java versions to retain support and security benefits.

**Integration with Related Azure Services:**  
Azure Functions is often integrated with other Azure services such as Azure Logic Apps, Azure Event Grid, and Azure Storage. The retirement of Java 8, 11, and 17 support may affect interoperability and integration scenarios if dependent services require updated Java runtimes. Customers should review their end-to-end architectures and ensure all components are compatible with newer Java versions to avoid disruption.

**Summary Sentence:**  
Support for Java 8, 11, and 17 in Azure Functions will end on September 1, 2027; while apps will continue to run, security updates and customer service will no longer be provided, requiring customers to upgrade to newer Java versions to maintain support and security.

---


*This report was automatically generated - 2026-11-26 03:02:03 UTC*