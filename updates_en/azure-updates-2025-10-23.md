# October 23, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 23, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Public Preview: VM vCore customization features disabling simultaneous multi-threading (SMT/HT) and constrained cores

**Published**: October 22, 2025 17:15:22 UTC
**Link**: [Public Preview: VM vCore customization features disabling simultaneous multi-threading (SMT/HT) and constrained cores](https://azure.microsoft.com/updates?id=516990)

**Update ID**: 516990
**Data source**: Azure Updates API

**Categories**: In preview, Features

**Summary**:

- What was updated  
Azure announced the public preview of new VM vCore customization features that allow customers to disable simultaneous multi-threading (SMT/Hyper-Threading) and constrain the number of active CPU cores on virtual machines.

- Key changes or new features  
1. **Disable SMT/HT:** Users can now disable simultaneous multi-threading on supported VM sizes, which can improve performance consistency and security by reducing shared resource contention.  
2. **Constrained cores:** Customers can limit the number of active vCPU cores below the VM’s maximum, enabling more granular control over CPU allocation to optimize licensing costs and workload requirements.

- Target audience affected  
Developers and IT professionals managing Azure VMs who need to optimize VM CPU configurations for performance tuning, licensing cost management, or specific workload demands.

- Important notes if any  
- This capability is in public preview and may have limitations or require specific VM series support.  
- Disabling SMT can impact performance characteristics; thorough testing is recommended before production use.  
- Constraining cores can help reduce software licensing costs tied to vCPU counts.  
- Users should review Azure documentation for supported VM sizes and configuration instructions.

**Details**:

Azure has announced the public preview of VM vCore customization features that enable customers to disable Simultaneous Multi-Threading (SMT/Hyper-Threading) and configure constrained cores on virtual machines, providing enhanced control over CPU configurations to optimize workload performance and licensing costs.

**Background and Purpose**  
Traditionally, Azure VMs allocate vCPUs based on physical cores with SMT enabled by default, meaning each physical core presents two logical processors. While SMT improves throughput for many workloads, certain applications—especially those sensitive to CPU contention or requiring strict licensing compliance—benefit from disabling SMT or restricting the number of active cores. Additionally, software licensing models often count logical processors, so controlling core allocation can reduce licensing expenses. This update addresses these needs by allowing granular customization of vCPU configurations.

**Specific Features and Detailed Changes**  
The update introduces two key capabilities:  
1. **Disable Simultaneous Multi-Threading (SMT/Hyper-Threading):** Customers can now opt to disable SMT on supported VM sizes, ensuring that only physical cores are utilized. This reduces resource contention and can improve performance consistency for workloads sensitive to SMT-induced variability.  
2. **Constrained Core Configuration:** Users can specify a subset of cores to be active on a VM, effectively limiting the number of vCPUs exposed to the guest OS. This allows for precise tuning of CPU resources and can help align VM configurations with software licensing requirements or workload demands.

These features are configurable via Azure Resource Manager (ARM) templates, Azure CLI, and PowerShell, enabling automation and integration into deployment pipelines.

**Technical Mechanisms and Implementation Methods**  
Under the hood, disabling SMT involves instructing the hypervisor to expose only physical cores to the VM, masking logical cores that SMT would otherwise present. Constrained cores are implemented by limiting the CPU scheduler’s visibility to a defined subset of cores, effectively pinning the VM’s vCPUs to specific physical cores. This is managed at the hypervisor level, ensuring isolation and consistent performance.

Configuration is done during VM creation or via update operations by setting new properties in the VM’s hardware profile, such as `disableSimultaneousMultiThreading` (boolean) and `coreCount` (integer). The VM size must support these features, and the Azure platform enforces constraints to prevent unsupported configurations.

**Use Cases and Application Scenarios**  
- **High-Performance Computing (HPC):** Workloads requiring predictable CPU performance and minimal thread contention can benefit from SMT disabling.  
- **Licensing Optimization:** Software licensed per core or per logical processor can leverage constrained cores to reduce licensing costs without overprovisioning VM resources.  
- **Latency-Sensitive Applications:** Real-time or low-latency applications can achieve more consistent CPU performance by disabling SMT.  
- **Testing and Development:** Developers can simulate specific CPU configurations to match on-premises environments or validate software behavior under constrained CPU scenarios.

**Important Considerations and Limitations**  
- Not all VM sizes support SMT disabling or core constraining; users must verify compatibility.  
- Disabling SMT may reduce total available logical processors, potentially impacting throughput for multi-threaded workloads.  
- Constraining cores reduces available CPU resources, which may affect performance if not carefully planned.  
- This feature is currently in public preview; production workloads should be tested thoroughly before adoption.  
- Some Azure services or features that depend on specific VM configurations may have compatibility considerations.

**Integration with Related Azure Services**  
These customization features integrate seamlessly with Azure VM Scale Sets, allowing for consistent CPU configurations across scale units. They also work with Azure Monitor and Azure Advisor, which can provide insights into CPU utilization and recommend optimal VM sizing. Additionally, integration with Azure Policy enables governance over VM CPU configurations to enforce organizational standards.

In summary, the public preview of VM vCore customization features in Azure empowers IT professionals with advanced CPU configuration controls—disabling SMT and constraining cores—enabling optimized workload performance

---

### 2. Generally Available: Azure SQL updates for mid-October 2025   

**Published**: October 22, 2025 16:30:07 UTC
**Link**: [Generally Available: Azure SQL updates for mid-October 2025   ](https://azure.microsoft.com/updates?id=513240)

**Update ID**: 513240
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance, Features

**Summary**:

- What was updated  
Azure SQL received key updates in mid-October 2025, focusing on connection improvements and database scalability enhancements.

- Key changes or new features  
1. The redirect connection type now requires only port 1433, simplifying firewall configurations and improving connectivity. This method is promoted to be the default connection type for Azure SQL Database.  
2. Azure SQL Database can now be converted to the Hyperscale tier while preserving existing geo-replication setups, enabling seamless scaling without disrupting geo-disaster recovery configurations.

- Target audience affected  
Developers and IT professionals managing Azure SQL databases, especially those concerned with network configuration, connectivity, and scaling strategies.

- Important notes if any  
The shift to redirect connection type using a single port (1433) reduces complexity in network security rules. The ability to convert to Hyperscale without losing geo-replication ensures high availability and disaster recovery continuity during scaling operations. Review your connection settings and geo-replication configurations to leverage these improvements effectively.

For more details, see: https://azure.microsoft.com/updates?id=513240

**Details**:

In mid-October 2025, Azure SQL introduced key enhancements aimed at simplifying connectivity and expanding scalability options, notably improving the redirect connection type to use only port 1433 by default and enabling conversion of Azure SQL Databases to Hyperscale tier while preserving existing geo-replication configurations.

**Background and Purpose:**  
Azure SQL continuously evolves to enhance performance, security, and manageability. Traditionally, redirect connection mode required multiple ports, complicating firewall configurations and network security. Simplifying this to a single port (1433) aligns with standard SQL Server connectivity, easing deployment and operational overhead. Additionally, the Hyperscale tier, designed for highly scalable workloads with rapid growth and large database sizes, lacked a straightforward migration path from existing databases with geo-replication. This update addresses that gap by allowing seamless conversion without disrupting geo-replication setups.

**Specific Features and Detailed Changes:**  
1. **Redirect Connection Type Defaulting to Port 1433:**  
   - The redirect connection type, which improves performance by directing client connections directly to the compute node, now requires only port 1433, the default SQL Server port.  
   - This change reduces the need to open multiple ports (previously 11000-11999 range), simplifying firewall rules and network security policies.  
   - The redirect mode is now promoted to the default connection type for Azure SQL Database, enhancing performance and reducing latency.

2. **Conversion to Hyperscale with Geo-Replication Preservation:**  
   - Customers can convert existing Azure SQL Databases to the Hyperscale tier without losing configured geo-replication relationships.  
   - This preserves disaster recovery and high availability setups during tier migration, minimizing downtime and operational complexity.  
   - The conversion process handles data movement and synchronization transparently.

**Technical Mechanisms and Implementation Methods:**  
- The redirect connection improvement leverages Azure SQL’s intelligent routing infrastructure, where the gateway forwards client requests directly to the compute node over port 1433. This eliminates the need for additional ports previously used for redirect traffic.  
- For Hyperscale conversion, Azure SQL orchestrates a backend data migration that transitions the database storage architecture to Hyperscale’s page server and log service model while maintaining geo-replication metadata and synchronization links. This involves snapshotting, data seeding, and phased cutover to ensure consistency.

**Use Cases and Application Scenarios:**  
- Enterprises with strict network security policies benefit from simplified firewall configurations by only needing to open port 1433. This is especially relevant for regulated industries or environments with stringent perimeter controls.  
- Organizations planning to scale their databases beyond the limits of standard tiers can migrate to Hyperscale without sacrificing existing geo-replication setups used for disaster recovery or read-scale scenarios.  
- Applications requiring low latency and high throughput gain from the redirect connection mode’s direct compute node access.

**Important Considerations and Limitations:**  
- While redirect mode on port 1433 is now default, legacy applications or network environments with custom port restrictions may require validation and testing before adopting this change.  
- The Hyperscale conversion process may incur transient performance impacts during migration; planning for maintenance windows is advisable.  
- Not all geo-replication configurations may be supported; users should consult Azure documentation for supported topologies and limitations.  
- Backup and restore strategies should be reviewed post-migration to align with Hyperscale’s architecture.

**Integration with Related Azure Services:**  
- This update complements Azure Virtual Network (VNet) service endpoints and Private Link configurations by simplifying network security management.  
- It integrates seamlessly with Azure Monitor and Azure SQL Analytics for performance monitoring under the new connection model.  
- Geo-replication preservation supports Azure’s global disaster recovery strategies and integrates with Azure Traffic Manager or Azure Front Door for multi-region failover and load balancing.

In summary, the mid-October 2025 Azure SQL update enhances connectivity by standardizing redirect connections on port 1433 and expands scalability

---

### 3. Generally Available: Near-zero downtime scaling for HA-enabled Azure Database for PostgreSQL servers 

**Published**: October 22, 2025 16:00:32 UTC
**Link**: [Generally Available: Near-zero downtime scaling for HA-enabled Azure Database for PostgreSQL servers ](https://azure.microsoft.com/updates?id=502004)

**Update ID**: 502004
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL servers with high availability (HA) now support near-zero downtime scaling.

- Key changes or new features  
Scaling operations on HA-enabled PostgreSQL servers are significantly accelerated, typically completing in under 30 seconds compared to the previous 2 to 10 minutes. This improvement minimizes user impact during scaling events, enhancing application availability and operational agility.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL instances with HA configurations who require seamless scaling to handle workload changes without disrupting service.

- Important notes if any  
This capability applies specifically to HA-enabled PostgreSQL servers in Azure. Users should verify their server configuration to leverage this feature. The update improves operational efficiency but does not change the underlying scaling limits or pricing. For detailed implementation guidance, refer to the official Azure documentation.

**Details**:

The recent general availability of near-zero downtime scaling for high availability (HA)-enabled Azure Database for PostgreSQL servers significantly enhances the operational agility and user experience by reducing scaling durations from several minutes to typically under 30 seconds. This update addresses the critical need for minimizing service disruption during resource scaling in production environments where HA configurations are employed.

**Background and Purpose**  
Azure Database for PostgreSQL is a managed database service that supports HA configurations to ensure business continuity and fault tolerance. Traditionally, scaling compute or storage resources on HA-enabled PostgreSQL servers involved failover and reconfiguration steps that could take between 2 to 10 minutes, causing noticeable downtime or degraded performance. This update aims to streamline the scaling process, enabling near-instantaneous resource adjustments while maintaining continuous availability, thus supporting dynamic workload demands and reducing operational risks.

**Specific Features and Detailed Changes**  
- **Near-zero downtime scaling:** The scaling operation now completes in less than 30 seconds on HA-enabled servers, a significant improvement over previous durations.  
- **Support for both compute and storage scaling:** Users can scale vCores and storage capacity with minimal impact.  
- **Seamless failover handling:** The update optimizes the failover mechanism during scaling to avoid prolonged connection drops.  
- **No manual intervention required:** The scaling process is fully managed by Azure, ensuring consistency and reliability.

**Technical Mechanisms and Implementation Methods**  
This enhancement leverages improvements in the underlying architecture of Azure Database for PostgreSQL HA clusters, including:  
- **Optimized replication synchronization:** The system ensures that replicas are fully synchronized before scaling operations, reducing the need for extended failover windows.  
- **Incremental resource allocation:** Instead of a full restart or failover, the platform applies resource changes incrementally and atomically to the primary and standby nodes.  
- **Connection draining and session preservation:** Active connections are gracefully managed during scaling to prevent abrupt termination.  
- **Enhanced orchestration logic:** Azure’s control plane coordinates scaling steps with precise timing to minimize service impact.

**Use Cases and Application Scenarios**  
- **Dynamic workload scaling:** Applications with variable workloads, such as e-commerce platforms or SaaS products, can scale resources rapidly in response to traffic spikes without downtime.  
- **DevOps and CI/CD pipelines:** Automated scaling during deployment or testing phases can be performed without affecting production availability.  
- **Cost optimization:** Organizations can downscale resources during off-peak hours with minimal disruption, optimizing costs while maintaining SLA commitments.  
- **Disaster recovery drills:** Near-zero downtime scaling facilitates realistic failover and scaling tests without impacting users.

**Important Considerations and Limitations**  
- The feature is applicable only to HA-enabled PostgreSQL servers; single-node configurations do not benefit from this update.  
- While scaling is near-instantaneous, very large scale operations or complex configurations might still experience slightly longer durations.  
- Applications should implement retry logic and connection resiliency to handle transient connection resets during scaling.  
- Monitoring and alerting should be configured to track scaling operations and performance metrics post-scaling.

**Integration with Related Azure Services**  
- **Azure Monitor:** Use to track scaling operations, performance metrics, and potential anomalies during scaling events.  
- **Azure Automation and Azure CLI:** Can be used to script and automate scaling operations leveraging the new near-zero downtime capability.  
- **Azure Private Link and Virtual Network:** Ensure secure connectivity remains uninterrupted during scaling in HA environments.  
- **Azure Backup and Azure Policy:** Maintain compliance and data protection standards during dynamic scaling activities.

In summary, the near-zero downtime scaling capability for HA-enabled Azure Database for PostgreSQL servers delivers a robust, efficient, and user-transparent scaling experience by optimizing failover orchestration, replication synchronization, and resource allocation processes, thereby enabling IT professionals to confidently manage dynamic workloads and maintain high availability with minimal operational impact.

---


*This report was automatically generated - 2025-10-23 03:02:45 UTC*