# September 15, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 15, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Announcing: New Windows App client-side endpoints for Azure Virtual Desktop

**Published**: September 14, 2026 18:24:04 UTC
**Link**: [Announcing: New Windows App client-side endpoints for Azure Virtual Desktop](https://azure.microsoft.com/updates?id=571360)

**Update ID**: 571360
**Data source**: Azure Updates API

**Categories**: Compute, Virtual desktop infrastructure, Azure Virtual Desktop, Announcement

**Summary**:

- What was updated  
Azure Virtual Desktop will introduce three new wildcard FQDNs for Windows App client-side service traffic starting in early October 2026.

- Key changes or new features  
Windows App clients connecting to Azure Virtual Desktop will require access to three new wildcard FQDNs. These FQDNs are already part of the cloud-side connectivity requirements but will now be necessary for client-side traffic as well. This change is intended to support improved service connectivity and reliability.

- Target audience affected  
Developers and IT professionals managing Azure Virtual Desktop environments, especially those responsible for configuring network security, firewalls, and connectivity for Windows App clients.

- Important notes  
IT administrators must update their network configurations and firewall rules to allow outbound traffic to these new wildcard FQDNs for Windows App clients by October 2026. Failure to do so may result in connectivity issues for Azure Virtual Desktop users. Review and update your allowlists to ensure uninterrupted service.  
For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=571360

**Details**:

**Azure Update Report: New Windows App Client-Side Endpoints for Azure Virtual Desktop**

**Background and Purpose of the Update**  
Starting in early October 2026, Microsoft will introduce three new wildcard fully qualified domain names (FQDNs) for client-side service traffic in the Windows App for Azure Virtual Desktop (AVD). This update is designed to enhance the connectivity and operational efficiency of the Windows App when accessing AVD resources. The new FQDNs are already part of the cloud-side connectivity requirements, ensuring alignment between client and cloud communication endpoints.

**Specific Features and Detailed Changes**  
The update specifically adds three new wildcard FQDNs to the list of domains used by the Windows App for client-side service traffic. These FQDNs will be utilized by Windows App clients when connecting to Azure Virtual Desktop environments. The change does not affect existing cloud-side connectivity requirements, as these domains are already included, but it does require IT professionals to ensure that client-side network configurations permit traffic to these new domains.

**Technical Mechanisms and Implementation Methods**  
From a technical perspective, the Windows App communicates with Azure Virtual Desktop services over the internet using specific FQDNs. With this update, the Windows App will initiate client-side traffic to three new wildcard FQDNs. Wildcard FQDNs allow for flexible subdomain routing, which can facilitate load balancing, regional failover, and service expansion without requiring frequent updates to network allowlists. IT administrators must update their firewall and proxy configurations to allow outbound traffic to these new FQDNs, ensuring uninterrupted connectivity for end users.

**Use Cases and Application Scenarios**  
This update is relevant for organizations deploying Azure Virtual Desktop and using the Windows App as their client interface. Typical scenarios include remote workforces accessing virtual desktops, application streaming, and secure access to corporate resources via AVD. Ensuring proper client-side connectivity to these new FQDNs is essential for seamless user experience, especially in environments with strict network controls or custom security policies.

**Important Considerations and Limitations**  
IT professionals should note that the new FQDNs are already included in cloud-side requirements, but client-side network configurations may need to be updated. Failure to allow traffic to these domains could result in connectivity issues or degraded performance for Windows App users. It is critical to review and update firewall rules, proxy settings, and any network security appliances to accommodate these new endpoints. Additionally, organizations should monitor for any changes in traffic patterns and validate that all endpoints are reachable from client devices.

**Integration with Related Azure Services**  
The Windows App is a primary client for Azure Virtual Desktop, and its connectivity is tightly integrated with AVD infrastructure. The update ensures that client-side traffic is routed efficiently to Azure resources, leveraging Azure’s global network and security features. This change aligns with Azure’s broader connectivity and endpoint management strategies, supporting secure and scalable access to virtualized desktops and applications.

**Summary Sentence**  
Beginning in early October 2026, Windows App will utilize three new wildcard FQDNs for client-side service traffic to Azure Virtual Desktop, requiring IT professionals to update network configurations to ensure seamless connectivity and alignment with existing cloud-side requirements.

---

### 2. Public Preview: HTTP/3 over QUIC support in Azure Application Gateway

**Published**: September 14, 2026 17:55:00 UTC
**Link**: [Public Preview: HTTP/3 over QUIC support in Azure Application Gateway](https://azure.microsoft.com/updates?id=571123)

**Update ID**: 571123
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Features

**Summary**:

- What was updated  
Azure Application Gateway now supports HTTP/3 over QUIC in public preview.

- Key changes or new features  
HTTP/3 is the latest HTTP protocol, leveraging QUIC (Quick UDP Internet Connections) to enhance web application performance. This update enables faster connection setup, reduced latency, and improved resiliency for applications and APIs served via Azure Application Gateway. Developers and IT professionals can now configure Application Gateway to accept HTTP/3 traffic, allowing clients to benefit from these improvements without changes to backend services.

- Target audience affected  
Developers and IT professionals managing web applications, APIs, or services behind Azure Application Gateway, especially those seeking improved performance and reliability for modern client devices and browsers.

- Important notes  
HTTP/3 support is currently in public preview and may not be suitable for production workloads yet. Existing Application Gateway configurations and backend services do not require changes to leverage HTTP/3, as it is handled at the gateway layer. Ensure client devices and browsers support HTTP/3 to fully benefit from this feature. Monitor Azure documentation for updates on general availability and best practices.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: HTTP/3 over QUIC support in Azure Application Gateway  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=571123)

---

**Background and Purpose of the Update**  
Azure Application Gateway now offers public preview support for HTTP/3 over QUIC. HTTP/3 represents the latest evolution of the HTTP protocol, designed to address performance and reliability challenges inherent in previous versions. By leveraging QUIC—a transport protocol built atop UDP—HTTP/3 aims to improve connection setup times, reduce latency, and enhance resiliency for modern web applications and APIs. This update aligns with Azure’s commitment to providing cutting-edge networking capabilities for cloud-hosted applications.

**Specific Features and Detailed Changes**  
The primary feature introduced is the ability for Azure Application Gateway to accept and process HTTP/3 traffic using the QUIC protocol. This enhancement allows clients to establish connections using HTTP/3, which is particularly beneficial for applications requiring low latency and robust connectivity. The update does not alter existing HTTP/1.1 or HTTP/2 support; instead, it adds HTTP/3 as an additional protocol option for frontend communication.

**Technical Mechanisms and Implementation Methods**  
HTTP/3 operates over QUIC, a protocol that uses UDP rather than TCP. QUIC enables faster connection establishment through zero round-trip time (0-RTT) handshakes and improved multiplexing, reducing the impact of packet loss and head-of-line blocking. Azure Application Gateway’s implementation allows clients to negotiate HTTP/3 during the TLS handshake, seamlessly transitioning from older HTTP versions if supported. The gateway manages QUIC sessions and ensures secure, reliable delivery of web traffic to backend pools, which continue to operate using HTTP/1.1 or HTTP/2.

**Use Cases and Application Scenarios**  
- **Modern Web Applications:** Applications with high user concurrency and performance requirements benefit from reduced latency and faster connection setup.
- **APIs:** APIs serving mobile or geographically distributed clients can leverage HTTP/3’s improved resiliency and performance.
- **Real-Time Services:** Services such as gaming, streaming, or collaborative platforms gain from QUIC’s efficient packet handling and rapid reconnection capabilities.
- **Mobile and IoT:** Devices with unreliable or variable network conditions can maintain better connectivity and user experience.

**Important Considerations and Limitations**  
- **Preview Status:** The feature is currently in public preview, which means it may not be suitable for production workloads and is subject to change.
- **Protocol Support:** Backend pools on Application Gateway continue to use HTTP/1.1 or HTTP/2; HTTP/3 is only supported for frontend client connections.
- **Compatibility:** Clients must support HTTP/3 and QUIC to benefit from this feature. Older clients will default to HTTP/1.1 or HTTP/2.
- **UDP Requirements:** QUIC uses UDP, so network environments must allow UDP traffic on the relevant ports.
- **Monitoring and Diagnostics:** Existing monitoring tools may need updates to fully support HTTP/3 traffic analysis.

**Integration with Related Azure Services**  
Azure Application Gateway remains compatible with other Azure networking and security services, such as Azure Web Application Firewall (WAF), Azure Front Door, and Azure Traffic Manager. HTTP/3 support enhances Application Gateway’s ability to serve as a robust entry point for web applications, complementing these services by providing improved performance and reliability for frontend connections.

---

**Summary Sentence:**  
Azure Application Gateway now supports HTTP/3 over QUIC in public preview, enabling faster, more resilient client connections for modern web applications and APIs while maintaining compatibility with existing backend protocols and Azure networking services.

---


*This report was automatically generated - 2026-09-15 03:01:49 UTC*