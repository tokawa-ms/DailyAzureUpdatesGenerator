# October 10, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 10, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Generally Available: Custom port support for Azure Database for MySQL – Flexible Server 

**Published**: October 09, 2025 17:30:09 UTC
**Link**: [Generally Available: Custom port support for Azure Database for MySQL – Flexible Server ](https://azure.microsoft.com/updates?id=503627)

**Update ID**: 503627
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure Database for MySQL, Features

**Summary**:

- What was updated  
Azure Database for MySQL – Flexible Server now supports configuring custom ports during server creation.

- Key changes or new features  
Users can specify a custom port number in the range 25001–26000 for both public and private access-enabled Flexible Servers. This flexibility allows better integration with existing applications that require non-default ports and helps align with organizational security policies. Previously, the service used the default MySQL port (3306) only.

- Target audience affected  
Developers and IT professionals managing Azure Database for MySQL Flexible Servers who need custom network configurations or enhanced security compliance.

- Important notes if any  
The custom port must be set at server creation and cannot be changed afterward. Ensure firewall and network security groups are updated accordingly to allow traffic on the chosen port. This feature improves security posture by enabling non-standard port usage, reducing exposure to common port scans.  

For more details, visit: https://azure.microsoft.com/updates?id=503627

**Details**:

The recent Azure update announces the general availability of custom port support for Azure Database for MySQL – Flexible Server, allowing users to specify a custom port number within the range 25001 to 26000 during server creation for both public and private access-enabled deployments. This enhancement addresses the need for greater flexibility in network configuration and security alignment, facilitating smoother integration with existing applications and organizational security policies.

**Background and Purpose:**  
By default, Azure Database for MySQL – Flexible Server uses the standard MySQL port 3306 for client-server communication. While this default port is widely recognized and supported, some enterprise environments impose strict network security controls that require the use of non-standard ports to reduce exposure to automated attacks or to comply with internal network segmentation policies. Prior to this update, users could not customize the port at server creation, limiting their ability to align the database service with their security postures or application requirements. This update enables customers to specify a custom port within a defined range, enhancing security and compatibility.

**Specific Features and Detailed Changes:**  
- **Custom Port Range:** Users can now select any port between 25001 and 26000 during the creation of a Flexible Server instance.  
- **Applicable to Both Access Types:** This feature applies to servers configured for public access as well as those restricted to private network access, ensuring consistent flexibility regardless of deployment model.  
- **Default Behavior:** If no custom port is specified, the server continues to use the default MySQL port 3306, maintaining backward compatibility.  
- **Configuration at Creation:** The port must be specified at server creation time; changing the port post-deployment is not supported, ensuring stability and predictable network behavior.

**Technical Mechanisms and Implementation Methods:**  
When a Flexible Server instance is provisioned with a custom port, Azure configures the underlying network security groups (NSGs) and firewall rules to allow inbound traffic on the specified port. The MySQL server process is configured to listen on the selected port, and connection strings must be updated accordingly by clients. For private access servers, the custom port is opened within the virtual network, while for public access servers, the port is exposed through the public IP with appropriate firewall rules. Azure’s management plane enforces these configurations automatically during provisioning, minimizing manual network configuration.

**Use Cases and Application Scenarios:**  
- **Security Compliance:** Organizations with strict network security policies can avoid using the default port 3306, which is commonly targeted by automated scans and attacks.  
- **Application Compatibility:** Legacy or third-party applications that require or expect a non-standard port can now connect without complex network workarounds.  
- **Network Segmentation:** Enterprises implementing micro-segmentation or port-based access controls can better integrate Flexible Server instances into their security zones.  
- **Multi-Database Environments:** Running multiple MySQL instances on the same network segment without port conflicts is simplified by assigning distinct custom ports.

**Important Considerations and Limitations:**  
- The custom port must be within the specified range (25001–26000); ports outside this range are not supported.  
- Port configuration is immutable post-deployment; changing the port requires creating a new server instance.  
- Client applications and connection strings must be updated to specify the custom port explicitly.  
- Network security rules and firewall configurations external to Azure (e.g., on-premises firewalls or VPNs) must be updated to allow traffic on the chosen port.  
- Some managed services or tools that assume the default MySQL port may require configuration changes to support custom ports.

**Integration with Related Azure Services:**  
- **Azure Virtual Network (VNet):** Custom port support integrates seamlessly with VNet service endpoints and private access configurations, enabling secure, private connectivity on the specified port.  
- **Azure Firewall and NSGs:** These network security components automatically accommodate the custom port during server provisioning, but administrators must verify that any additional custom rules align with the chosen port.  
- **

---

### 2. Generally Available: Azure Firewall updates - Customer provided public IP address support in secured hubs

**Published**: October 09, 2025 17:00:43 UTC
**Link**: [Generally Available: Azure Firewall updates - Customer provided public IP address support in secured hubs](https://azure.microsoft.com/updates?id=512875)

**Update ID**: 512875
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure Firewall, Azure Firewall Manager, Features

**Summary**:

- What was updated  
Azure Firewall in Virtual WAN secured hubs now supports customer-provided public IP addresses.

- Key changes or new features  
Organizations can bring and assign their own public IP addresses to Azure Firewall instances deployed within secured Virtual WAN hubs. This enhances IP address management flexibility, allowing better alignment with existing network architectures and compliance requirements.

- Target audience affected  
Developers and IT professionals managing Azure Firewall deployments in Virtual WAN environments, especially those requiring control over public IP address allocation for security, compliance, or operational reasons.

- Important notes if any  
This feature is generally available, meaning it is fully supported for production workloads. Customers should ensure their provided public IP addresses meet Azure Firewall requirements and coordinate IP address management to avoid conflicts. This update improves integration capabilities for secured hub architectures in Virtual WAN deployments.  

Reference: https://azure.microsoft.com/updates?id=512875

**Details**:

The recent Azure Firewall update introduces general availability support for customer-provided public IP addresses in secured Virtual WAN hubs, enhancing IP address management flexibility and control for organizations deploying Azure Firewall within Azure Virtual WAN environments.

**Background and Purpose of the Update**  
Azure Firewall is a cloud-native, stateful firewall service that provides network and application-level protection for Azure Virtual Networks. Azure Virtual WAN simplifies large-scale branch connectivity and security by providing a unified hub-and-spoke architecture. Secured hubs in Virtual WAN incorporate Azure Firewall to enforce centralized security policies. Previously, Azure Firewall in secured hubs required Microsoft-assigned public IP addresses, limiting organizations’ ability to use their own IP address ranges. This update addresses that limitation by enabling Bring Your Own IP (BYOIP) capabilities for public IPs, allowing organizations to maintain consistent IP address branding, comply with regulatory requirements, or manage IP reputation more effectively.

**Specific Features and Detailed Changes**  
- Support for customer-provided public IP addresses in Azure Firewall deployed within secured Virtual WAN hubs.  
- The ability to associate pre-owned public IP addresses with Azure Firewall instances in secured hubs, replacing the default Microsoft-assigned IPs.  
- This feature is generally available (GA), indicating full production readiness and Microsoft support.  
- The update supports both IPv4 and IPv6 public IP addresses that customers bring into their Azure environment and register for use.  

**Technical Mechanisms and Implementation Methods**  
- Customers must first bring their public IP addresses into Azure using the Azure BYOIP process, which involves IP prefix registration, validation, and ownership proof via Azure Portal or CLI.  
- Once the IP prefixes are registered and announced via Azure’s network infrastructure, these IP addresses become available for assignment.  
- During Azure Firewall deployment or configuration within a secured Virtual WAN hub, administrators can specify these customer-owned public IP addresses instead of relying on Microsoft-assigned IPs.  
- The Azure Firewall instance then uses these IPs for inbound and outbound traffic, maintaining consistent public IP presence.  
- The secured Virtual WAN hub architecture ensures that the firewall is integrated with the global transit network, and the BYOIP IPs are advertised appropriately for routing.  

**Use Cases and Application Scenarios**  
- Enterprises with strict compliance or regulatory requirements that mandate use of owned IP address ranges for outbound traffic.  
- Organizations aiming to maintain consistent public IP addresses for reputation management, such as avoiding IP-based blocking or blacklisting.  
- Scenarios requiring IP address continuity during migration from on-premises firewalls or other cloud providers to Azure Firewall in Virtual WAN secured hubs.  
- Multi-region deployments where centralized IP address management is critical for governance and auditing.  

**Important Considerations and Limitations**  
- Customer-provided IP addresses must be registered and validated through Azure’s BYOIP process before use. This process can take several days depending on verification steps.  
- Only public IP prefixes that are owned and verifiably controlled by the customer can be used; Microsoft does not support IP spoofing or unverified IPs.  
- The feature applies specifically to Azure Firewall instances deployed in secured Virtual WAN hubs and may not be applicable to standalone Azure Firewall deployments outside Virtual WAN.  
- Proper routing and network configuration are required to ensure that the BYOIP addresses are correctly advertised and reachable.  
- Customers should monitor IP address usage and ensure compliance with Azure Firewall and Virtual WAN service limits.  

**Integration with Related Azure Services**  
- Azure Virtual WAN: The update enhances Azure Firewall integration within Virtual WAN secured hubs by allowing BYOIP, improving network architecture flexibility.  
- Azure BYOIP: This feature relies on the Azure Bring Your Own IP service for IP prefix registration and management.  
- Azure Monitor and Azure Security Center can be used to monitor firewall traffic and security posture when using customer-provided IPs.  
- Azure Route Server and ExpressRoute or VPN gateways in Virtual WAN can complement the routing and connectivity aspects of the secured hub deployment.

---

### 3. Generally Available: Firmware analysis enabled by Azure Arc 

**Published**: October 09, 2025 14:15:20 UTC
**Link**: [Generally Available: Firmware analysis enabled by Azure Arc ](https://azure.microsoft.com/updates?id=512201)

**Update ID**: 512201
**Data source**: Azure Updates API

**Categories**: Launched, Hybrid + multicloud, Azure Arc, Features

**Summary**:

- What was updated  
Firmware analysis capabilities enabled by Azure Arc have reached general availability.

- Key changes or new features  
This update introduces deep visibility into the firmware running on IoT, OT, and network devices managed via Azure Arc. It enables security teams and developers to analyze firmware components, detect vulnerabilities, and gain insights into devices that traditionally operate as “black boxes.” This enhances security posture by providing firmware-level threat detection and compliance monitoring across hybrid and multi-cloud environments.

- Target audience affected  
Developers, IT professionals, security engineers, and operations teams managing IoT, OT, and network devices in hybrid infrastructures using Azure Arc will benefit from this update.

- Important notes if any  
Firmware analysis requires Azure Arc-enabled devices and proper onboarding to the service. Organizations should ensure devices are connected and compliant with Azure Arc prerequisites to leverage these capabilities. This feature extends Azure Security Center’s protection scope to firmware, helping reduce risks from firmware-level attacks in complex environments.

For more details, visit: https://azure.microsoft.com/updates?id=512201

**Details**:

The recent general availability of firmware analysis enabled by Azure Arc introduces a powerful capability for IT professionals to gain deep visibility and enhanced security insights into the firmware layer of IoT, OT, and network devices, which traditionally operate as opaque “black boxes” with limited monitoring options. This update addresses a critical security gap by extending Azure Arc’s management and security capabilities to the firmware level, enabling organizations to detect vulnerabilities, unauthorized changes, and potential threats within device firmware across hybrid and multi-cloud environments.

**Background and Purpose:**  
Firmware, the low-level software embedded in hardware devices, is foundational to device operation but often lacks comprehensive security visibility and management. Many IoT and OT devices run legacy or proprietary firmware that is difficult to monitor, making them prime targets for cyberattacks that can compromise critical infrastructure or network integrity. The purpose of this update is to provide enterprises with a scalable, centralized solution to analyze firmware integrity and security posture by leveraging Azure Arc’s hybrid management framework, thereby reducing risks associated with firmware vulnerabilities and unauthorized modifications.

**Specific Features and Detailed Changes:**  
- **Firmware Inventory and Analysis:** Azure Arc now supports automated discovery and inventory of firmware versions across connected devices, providing detailed metadata and version tracking.  
- **Security Posture Assessment:** The service performs deep analysis to identify known vulnerabilities, configuration anomalies, and unauthorized firmware changes using threat intelligence and firmware baselines.  
- **Continuous Monitoring:** Firmware states are continuously monitored and compared against trusted baselines to detect deviations or potential compromises in near real-time.  
- **Integration with Azure Security Center:** Firmware analysis findings feed directly into Azure Security Center (now Microsoft Defender for Cloud), enabling unified security alerts, recommendations, and compliance reporting.  
- **Cross-Platform Support:** Supports a wide range of IoT/OT devices and network hardware through Azure Arc’s extensible agent model, enabling firmware analysis across heterogeneous environments.

**Technical Mechanisms and Implementation Methods:**  
Firmware analysis leverages Azure Arc’s connected machine agents deployed on edge devices or gateways that interface with the target hardware. These agents extract firmware data using vendor-specific APIs, standard protocols (e.g., Redfish for servers, SNMP for network devices), or custom connectors. Extracted firmware images and metadata are securely transmitted to Azure for analysis using cloud-based threat intelligence, machine learning models, and signature databases to detect anomalies and vulnerabilities. The system maintains a firmware baseline repository per device type, enabling integrity checks and continuous compliance validation. Integration with Azure Policy allows automated remediation workflows based on firmware analysis outcomes.

**Use Cases and Application Scenarios:**  
- **Critical Infrastructure Protection:** Utilities and manufacturing firms can monitor firmware integrity of OT devices to prevent sabotage or ransomware attacks targeting industrial control systems.  
- **Network Security:** Enterprises can detect unauthorized firmware modifications in routers, switches, and firewalls that might indicate compromise or insider threats.  
- **IoT Device Management:** Organizations managing large IoT fleets can ensure devices run approved firmware versions, reducing attack surfaces and compliance risks.  
- **Hybrid Cloud Environments:** Firms operating workloads across on-premises, edge, and cloud can maintain consistent firmware security posture visibility through Azure Arc’s unified management plane.

**Important Considerations and Limitations:**  
- **Device Compatibility:** Firmware analysis depends on device support for firmware extraction APIs or protocols; legacy or proprietary devices without such interfaces may have limited visibility.  
- **Agent Deployment:** Requires deployment of Azure Arc agents or compatible connectors on devices or gateways, which may be constrained by device resource limitations or network policies.  
- **Data Privacy and Security:** Firmware data transmitted to Azure must be handled according to organizational compliance and privacy policies, especially in regulated industries.  
- **Update Frequency:** Continuous monitoring intervals and analysis frequency should be tuned to balance security needs and network/resource overhead.

**Integration with Related Azure Services:**  
- **Microsoft Defender for Cloud:** Firmware analysis alerts and recommendations integrate into the broader security posture management dashboard.  
- **Azure Policy:** Enables governance by enforcing firmware compliance policies and triggering

---

### 4. Retirement: Azure AI Health Insights and related models

**Published**: October 09, 2025 12:45:35 UTC
**Link**: [Retirement: Azure AI Health Insights and related models](https://azure.microsoft.com/updates?id=502049)

**Update ID**: 502049
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of the Azure AI Health Insights service along with the Clinical Trials Matcher and Radiology Insights AI models.

- Key changes or new features  
These services and models will be fully retired and unavailable for use or integration starting December 31, 2025. No new features or updates will be provided beyond this date.

- Target audience affected  
Developers and IT professionals who currently use or integrate Azure AI Health Insights and the related Clinical Trials Matcher and Radiology Insights models in healthcare or clinical applications.

- Important notes if any  
Users should plan to migrate workloads and integrations relying on these services before the retirement date. Microsoft recommends evaluating alternative AI services or custom solutions to replace the retiring models. This retirement is part of a broader strategic review of Microsoft’s AI portfolio, reflecting a shift in focus and resource allocation. Early planning is advised to avoid disruption in healthcare AI workflows dependent on these models.

**Details**:

The Azure update announces the planned retirement of the Azure AI Health Insights service along with its associated Clinical Trials Matcher and Radiology Insights models, effective December 31, 2025. This decision follows a strategic review of Microsoft’s AI portfolio aimed at streamlining offerings and focusing on core capabilities.

**Background and Purpose:**  
Azure AI Health Insights was designed to provide healthcare organizations with AI-powered tools to extract actionable insights from clinical data, facilitating improved patient care and research. The Clinical Trials Matcher model helped match patients to relevant clinical trials by analyzing medical records, while the Radiology Insights model supported automated interpretation of radiology images. The retirement reflects Microsoft’s intent to consolidate AI services, possibly to enhance innovation in other areas or integrate health AI capabilities into broader platforms.

**Specific Features and Changes:**  
Post-retirement, these services and models will no longer be accessible for new or existing deployments. This means that any applications or workflows relying on Azure AI Health Insights or its related models must be transitioned away before the cutoff date. No further updates, support, or integrations will be provided after December 31, 2025. The deprecation affects APIs, SDKs, and any embedded AI functionalities tied to these services.

**Technical Mechanisms and Implementation:**  
From a technical standpoint, Azure will disable the backend endpoints servicing the Health Insights APIs and models. Clients invoking these endpoints will receive errors once the service is fully retired. Organizations currently using these services should plan to export their data and migrate workloads to alternative solutions well in advance. Microsoft typically provides migration guidance and tools for such transitions, although specific replacement services for these models have not been explicitly stated in the update.

**Use Cases and Application Scenarios:**  
Azure AI Health Insights was primarily used in clinical environments to enhance decision-making by extracting insights from unstructured clinical notes, matching patients to clinical trials, and assisting radiologists with image interpretation. Hospitals, research institutions, and healthcare software vendors integrated these AI models to improve patient outcomes, accelerate research, and optimize clinical workflows. With the retirement, these use cases will require alternative AI solutions or custom implementations.

**Important Considerations and Limitations:**  
IT professionals must carefully inventory all dependencies on the retiring services, including direct API calls, embedded SDKs, and downstream integrations. Data privacy and compliance considerations are paramount when migrating sensitive health data. Additionally, the retirement timeline provides a multi-year window, but early planning is critical to avoid service disruption. There may be limitations in finding one-to-one replacement services within Azure, necessitating evaluation of third-party or custom AI models.

**Integration with Related Azure Services:**  
While Azure AI Health Insights and its models are retiring, Microsoft continues to invest in broader Azure AI and healthcare-focused services such as Azure Health Bot, Azure API for FHIR, and Azure Machine Learning. Organizations are encouraged to explore these platforms for building custom AI solutions or leveraging other healthcare data interoperability tools. Integration with Azure Data Factory, Azure Synapse Analytics, and Power BI can facilitate advanced analytics and reporting workflows as part of a re-architecture strategy.

In summary, the retirement of Azure AI Health Insights and its Clinical Trials Matcher and Radiology Insights models by the end of 2025 requires healthcare IT teams to proactively plan migration strategies, identify alternative AI capabilities, and ensure continuity of clinical AI applications within the evolving Azure ecosystem.

---


*This report was automatically generated - 2025-10-10 03:02:33 UTC*