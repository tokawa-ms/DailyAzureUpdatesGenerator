# July 30, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: July 30, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Customer-controlled maintenance

**Published**: July 29, 2025 17:00:48 UTC
**Link**: [Generally Available: Customer-controlled maintenance](https://azure.microsoft.com/updates?id=499396)

**Update ID**: 499396
**Data source**: Azure Updates API

**Categories**: Launched, Hybrid + multicloud, Networking, Security, Azure ExpressRoute, Virtual WAN, VPN Gateway, Features, Management, Services

**Summary**:

- What was updated  
Azure Virtual WAN Service’s Point-to-Site VPN Gateway now supports customer-controlled maintenance windows.

- Key changes or new features  
Customers can configure and schedule maintenance windows for their Point-to-Site VPN Gateways within Virtual WAN. This allows them to control when gateway maintenance occurs, minimizing unexpected downtime and aligning maintenance with their operational schedules. The P2S VPN in Virtual WAN has reached general availability, making this feature broadly accessible.

- Target audience affected  
Developers and IT professionals managing Azure Virtual WAN environments, especially those using Point-to-Site VPN Gateways, benefit from improved maintenance control and scheduling flexibility.

- Important notes if any  
Configurable maintenance windows help reduce service disruption by allowing planned maintenance during low-impact periods. This feature enhances operational reliability and customer control over gateway availability. Users should review their maintenance schedules to optimize uptime and avoid conflicts with critical workloads.

For more details, visit: https://azure.microsoft.com/updates?id=499396

**Details**:

The recent Azure update announces the general availability of customer-controlled maintenance windows for Point-to-Site (P2S) VPN Gateways within the Azure Virtual WAN service, enabling customers to schedule and manage gateway maintenance proactively.

**Background and Purpose**  
Azure Virtual WAN provides a unified networking service to connect branches, remote users, and on-premises sites to Azure resources. The Point-to-Site VPN Gateway in Virtual WAN allows individual clients to securely connect to Azure via VPN. Previously, maintenance activities on these gateways were managed solely by Azure, often causing unplanned or inconvenient downtime. The update addresses the need for greater customer control over maintenance timing to minimize disruption and align maintenance with organizational windows.

**Specific Features and Detailed Changes**  
- Introduction of configurable maintenance windows specifically for P2S VPN Gateways in Virtual WAN.  
- Customers can now define preferred time slots during which Azure can perform necessary gateway maintenance tasks such as patching, updates, or infrastructure improvements.  
- Maintenance outside the configured window is avoided unless critical, thus reducing unexpected service interruptions.  
- This feature is available now in general availability (GA), indicating full production readiness and SLA-backed support.

**Technical Mechanisms and Implementation Methods**  
- Maintenance windows are configured via Azure Portal, Azure CLI, or ARM templates, allowing integration into existing infrastructure-as-code workflows.  
- The configuration specifies start time, duration, and recurrence parameters for maintenance windows.  
- Azure’s backend scheduling system respects these windows when orchestrating gateway maintenance, deferring non-critical updates to the defined periods.  
- If urgent security patches or critical fixes are required, Azure retains the ability to override windows but will notify customers accordingly.  
- The feature leverages Virtual WAN’s centralized management plane, ensuring consistent application across all P2S VPN Gateways under a Virtual WAN hub.

**Use Cases and Application Scenarios**  
- Enterprises with strict uptime requirements can schedule maintenance during off-peak hours to avoid impacting remote workers’ connectivity.  
- Organizations in regulated industries can align maintenance with compliance windows or change management policies.  
- Managed service providers can coordinate maintenance across multiple customers’ Virtual WAN environments to optimize operational efficiency.  
- Development and test environments can be scheduled for maintenance during low-usage periods to minimize disruption.

**Important Considerations and Limitations**  
- Maintenance windows apply only to P2S VPN Gateways within Virtual WAN and do not currently extend to Site-to-Site VPN Gateways or other gateway types.  
- Customers must actively configure maintenance windows; absence of configuration defaults to Azure-managed scheduling.  
- Critical updates may still occur outside the configured window to ensure security and stability, so some downtime risk remains.  
- Time zone considerations are important when defining windows, especially for globally distributed teams.  
- Monitoring and alerting should be configured to track maintenance events and gateway health proactively.

**Integration with Related Azure Services**  
- This update complements Azure Virtual WAN’s broader networking capabilities, including branch connectivity, ExpressRoute integration, and firewall policies.  
- Maintenance window configurations can be integrated into Azure Policy to enforce organizational standards.  
- Azure Monitor and Azure Network Watcher can be used to track VPN gateway performance and maintenance events, enabling operational insights.  
- Integration with Azure Automation or Logic Apps can facilitate notifications or automated workflows triggered by maintenance events.

In summary, the general availability of customer-controlled maintenance windows for P2S VPN Gateways in Azure Virtual WAN empowers IT professionals to align gateway maintenance with organizational needs, reducing unplanned downtime and enhancing operational control while maintaining Azure’s security and reliability standards.

---

### 2. Retirement: Azure Front Door (classic) and Azure CDN from Microsoft Classic SKU ending CNAME based domain validation and new domain/profile creations by August 15, 2025

**Published**: July 29, 2025 14:30:43 UTC
**Link**: [Retirement: Azure Front Door (classic) and Azure CDN from Microsoft Classic SKU ending CNAME based domain validation and new domain/profile creations by August 15, 2025](https://azure.microsoft.com/updates?id=498522)

**Update ID**: 498522
**Data source**: Azure Updates API

**Categories**: Networking, Security, Media, Web, Azure Front Door, Content Delivery Network, Features, Retirements, Services

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure Front Door (classic) and Azure CDN from Microsoft Classic SKUs regarding domain onboarding and profile creation processes, effective August 15, 2025. Additionally, DigiCert is discontinuing support for CNAME-based Domain Control Validation (DCV).

- Key changes or new features  
After August 15, 2025, no new custom domains or profiles can be created on Azure Front Door (classic) and Azure CDN Classic SKUs. Existing domains and profiles will continue to function but cannot be expanded or newly validated using CNAME-based DCV, as DigiCert will no longer support this validation method.

- Target audience affected  
Developers and IT professionals managing Azure Front Door (classic) and Azure CDN Classic SKU deployments, especially those who onboard new custom domains or create new profiles. Teams relying on CNAME-based DCV for domain validation must plan for alternative validation methods or migration.

- Important notes if any  
Customers should consider migrating to the latest Azure Front Door Standard/Premium SKUs or Azure CDN from Verizon/Akamai SKUs, which support updated domain validation methods and new profile creation. Planning migration ahead of the August 2025 deadline is critical to avoid service disruption or onboarding limitations. Review DigiCert’s updated DCV requirements and Azure’s newer offerings to ensure compliance and continuity.

**Details**:

The announced retirement of Azure Front Door (classic) and Azure CDN from Microsoft Classic SKUs’ support for new domain onboarding and profile creation by August 15, 2025, along with the deprecation of DigiCert’s CNAME-based Domain Control Validation (DCV), reflects a strategic shift to enhance security, streamline domain validation processes, and encourage migration to newer SKUs with improved capabilities.

**Background and Purpose of the Update**  
Azure Front Door (classic) and the Microsoft Classic SKU for Azure CDN have been foundational services for global web application acceleration and secure content delivery. However, these classic SKUs rely on legacy domain validation methods, notably CNAME-based DCV, which DigiCert is deprecating due to security and operational concerns. This update aims to phase out older domain onboarding workflows that depend on CNAME-based validation, encouraging customers to adopt newer Azure Front Door Standard/Premium SKUs and Azure CDN Standard/Premium SKUs, which support more secure and flexible domain validation methods such as HTTP-based or DNS TXT record validation.

**Specific Features and Detailed Changes**  
- **End of New Domain Onboarding and Profile Creation:** After August 15, 2025, customers will no longer be able to create new custom domain profiles or onboard new domains on Azure Front Door (classic) or Azure CDN Microsoft Classic SKUs. Existing domains and profiles will continue to function, but no new additions will be permitted.  
- **CNAME-based DCV Deprecation:** DigiCert, the certificate authority used for SSL/TLS certificates in these services, is discontinuing support for CNAME-based DCV, a method where domain ownership is validated by creating a specific CNAME DNS record. This method is being replaced by more secure and reliable validation techniques.  
- **Migration Encouraged:** Customers are advised to migrate to the newer SKUs that support modern domain validation mechanisms and provide enhanced features such as better performance, security, and integration capabilities.

**Technical Mechanisms and Implementation Methods**  
CNAME-based DCV involves proving domain ownership by adding a DNS CNAME record pointing to a DigiCert-controlled domain. This method is being deprecated because it can be less secure and more prone to misconfiguration or hijacking. Newer validation methods include:  
- **HTTP-based Validation:** A specific file or token is hosted on the domain’s web server, which DigiCert verifies via HTTP requests.  
- **DNS TXT Record Validation:** A TXT record containing a validation token is added to the domain’s DNS zone, which DigiCert queries to confirm ownership.  
Azure Front Door Standard/Premium and Azure CDN Standard/Premium SKUs support these methods, enabling more secure and flexible domain validation workflows.

**Use Cases and Application Scenarios**  
- Organizations using Azure Front Door (classic) or Azure CDN Classic SKU to accelerate and secure web applications with custom domains will need to plan for migration if they intend to add new domains or profiles post-August 2025.  
- Enterprises requiring compliance with stricter security standards will benefit from the enhanced validation methods available in newer SKUs.  
- Customers leveraging automated domain onboarding and SSL certificate issuance workflows must update their processes to align with the new validation methods.

**Important Considerations and Limitations**  
- Existing domains and profiles on the classic SKUs will continue to operate but cannot be expanded with new domains or profiles after the cutoff date.  
- Migration to newer SKUs may require configuration changes, including updating DNS records and revalidating domains using supported methods.  
- Customers should audit their current domain validation setups to identify dependencies on CNAME-based DCV and plan accordingly.  
- There may be cost implications associated with migrating to newer SKUs, which typically offer enhanced features but at different pricing tiers.

**Integration with Related Azure Services**  
- Azure Front Door Standard/Premium and Azure CDN Standard/Premium SKUs integrate seamlessly with Azure DNS, enabling streamlined DNS TXT record validation.  
- Azure Key Vault and Azure App Service can be

---


*This report was automatically generated - 2025-07-30 03:01:35 UTC*