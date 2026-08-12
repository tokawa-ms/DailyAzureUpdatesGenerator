# August 12, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 12, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Generally Available: 2.2X IDPS performance optimization in Azure Firewall

**Published**: August 11, 2026 17:26:51 UTC
**Link**: [Generally Available: 2.2X IDPS performance optimization in Azure Firewall](https://azure.microsoft.com/updates?id=569256)

**Update ID**: 569256
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure Firewall, Features

**Summary**:

- What was updated  
Azure Firewall Premium has received a significant performance optimization for its Intrusion Detection and Prevention System (IDPS).

- Key changes or new features  
The update increases maximum throughput with TLS inspection and IDPS in Deny mode to 22 Gbps, up from 10 Gbps—a 120% improvement. Additionally, per TCP connection throughput with IDPS enabled (in either Alert or Deny mode) has doubled to 600 Mbps from 300 Mbps. These enhancements apply to both TLS-inspected and non-TLS-inspected traffic.

- Target audience affected  
This update impacts IT professionals managing network security and developers deploying applications requiring high-throughput, secure connectivity in Azure environments. Organizations with demanding workloads or strict security requirements will benefit most.

- Important notes if any  
The improved performance allows for higher traffic volumes and more concurrent secure connections without compromising security. This is especially relevant for enterprises scaling their workloads or requiring robust protection against threats. No changes are needed to existing configurations to leverage these enhancements, but monitoring and capacity planning should be updated to reflect the new throughput limits.

For more details, visit the official Azure Update: https://azure.microsoft.com/updates?id=569256

**Details**:

**Azure Update Report: Generally Available – 2.2X IDPS Performance Optimization in Azure Firewall**

**Background and Purpose of the Update**  
Azure Firewall Premium is a managed, cloud-native network security service that provides advanced threat protection for Azure workloads. Intrusion Detection and Prevention System (IDPS) and TLS inspection are critical security features, but historically, enabling these features has introduced significant performance overhead. The purpose of this update is to substantially increase the throughput and per-connection performance of Azure Firewall Premium when IDPS and TLS inspection are enabled, addressing customer demand for higher performance in security-intensive environments.

**Specific Features and Detailed Changes**  
With this update, Azure Firewall Premium now supports up to 22 Gbps throughput with both TLS inspection and IDPS in Deny mode. This represents a 120% increase from the previous maximum of 10 Gbps. Additionally, the per TCP connection throughput with IDPS enabled (in either Alert or Deny mode) has doubled, rising from 300 Mbps to 600 Mbps. These enhancements are generally available and apply to all deployments of Azure Firewall Premium.

**Technical Mechanisms and Implementation Methods**  
The performance improvements are achieved through optimizations in the underlying processing architecture of Azure Firewall Premium. These likely include enhancements to packet processing pipelines, improved resource allocation, and more efficient handling of TLS inspection and IDPS operations. The update ensures that security features such as deep packet inspection and encrypted traffic analysis can operate at higher speeds without compromising detection accuracy or security posture. The IDPS operates in both Alert and Deny modes, allowing for flexible threat response, while TLS inspection decrypts and inspects traffic for threats.

**Use Cases and Application Scenarios**  
This update is particularly beneficial for organizations with high-bandwidth workloads requiring advanced security inspection. Typical scenarios include:
- Large-scale enterprise environments with significant east-west and north-south traffic.
- Workloads handling sensitive data that require TLS inspection and IDPS for regulatory compliance.
- Multi-tier applications where performance bottlenecks previously limited the use of deep security inspection.
- Scenarios where rapid threat response and high throughput are critical, such as financial services, healthcare, and e-commerce platforms.

**Important Considerations and Limitations**  
While the performance improvements are substantial, IT professionals should consider the following:
- The throughput figures (22 Gbps and 600 Mbps per TCP connection) are achieved with IDPS in Deny mode and with TLS inspection enabled; actual performance may vary based on traffic patterns and workloads.
- IDPS must be enabled in either Alert or Deny mode to benefit from the per-connection performance increase.
- Proper sizing and configuration of Azure Firewall Premium instances remain essential to achieve optimal performance.
- It is important to monitor and test the firewall in production environments to ensure that performance meets organizational requirements.

**Integration with Related Azure Services**  
Azure Firewall Premium integrates seamlessly with other Azure security and networking services, including Azure Virtual Networks, Azure Monitor, and Azure Security Center. The enhanced performance allows for more robust protection in complex architectures, supporting scenarios such as hub-and-spoke network topologies, hybrid connectivity, and integration with Azure Sentinel for advanced threat analytics. The update ensures that organizations can leverage advanced security features without sacrificing network throughput or scalability.

**Summary Sentence**  
Azure Firewall Premium now delivers up to 22 Gbps throughput with TLS inspection and IDPS in Deny mode, and up to 600 Mbps per TCP connection with IDPS enabled, providing a significant performance boost for security-intensive workloads.

---


*This report was automatically generated - 2026-08-12 03:01:19 UTC*