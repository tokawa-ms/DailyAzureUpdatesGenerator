# November 20, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 20, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Announcing: Multiparty private offers in Microsoft Marketplace expands to Malaysia and Saudi Arabia

**Published**: November 20, 2026 00:00:14 UTC
**Link**: [Announcing: Multiparty private offers in Microsoft Marketplace expands to Malaysia and Saudi Arabia](https://azure.microsoft.com/updates?id=580700)

**Update ID**: 580700
**Data source**: Azure Updates API

**Categories**: Microsoft Ignite, Announcement

**Summary**:

- What was updated  
Multiparty private offers in the Microsoft Marketplace are now available in Malaysia and Saudi Arabia.

- Key changes or new features  
This update allows Microsoft partners in Malaysia and Saudi Arabia to create and manage multiparty private offers for cloud and AI solutions. Multiparty private offers enable software vendors to collaborate with other partners, leveraging established customer relationships to expand into new markets. The feature streamlines procurement for customers, providing a secure and flexible way to purchase third-party solutions directly through the Marketplace.

- Target audience affected  
Microsoft partners, software vendors, developers, and IT professionals operating in or targeting Malaysia and Saudi Arabia. Organizations seeking to procure or sell cloud and AI solutions via the Microsoft Marketplace in these regions will benefit from this update.

- Important notes  
Multiparty private offers help partners accelerate sales cycles and reach new customers by combining their offerings and expertise. This expansion supports local compliance and procurement requirements, making it easier for customers in Malaysia and Saudi Arabia to access a broader range of solutions. Developers and IT professionals should consider leveraging this feature to enhance their go-to-market strategies and streamline solution procurement for their clients.

**Details**:

**Azure Update Report: Multiparty Private Offers in Microsoft Marketplace Expands to Malaysia and Saudi Arabia**

**Background and Purpose of the Update**  
Microsoft Marketplace’s multiparty private offers capability is designed to streamline procurement of third-party cloud and AI solutions. This update announces the expansion of multiparty private offers to Malaysia and Saudi Arabia, enabling Microsoft partners in these regions to leverage Marketplace for more flexible and collaborative procurement processes. The primary purpose is to facilitate software companies’ entry into new markets by allowing them to work with partners who have established customer relationships, thus accelerating solution adoption and deployment.

**Specific Features and Detailed Changes**  
Multiparty private offers allow multiple Microsoft partners to collaborate in creating tailored private offers for customers. With this update, partners and customers in Malaysia and Saudi Arabia can now access and utilize this feature. Key features include:
- Collaborative offer creation: Multiple partners (such as ISVs and resellers) can jointly structure private offers for specific customers.
- Expanded geographic availability: The feature is now accessible in Malaysia and Saudi Arabia, increasing the global reach.
- Procurement flexibility: Customers can procure third-party cloud and AI solutions through Marketplace, benefiting from customized pricing and terms negotiated by their trusted partners.

**Technical Mechanisms and Implementation Methods**  
Multiparty private offers are facilitated through Microsoft Marketplace’s backend integration. Partners initiate the offer creation process via the Marketplace portal, specifying participating parties, solution details, pricing, and terms. The technical workflow involves:
- Offer configuration: Partners define the solution, pricing, and participating entities.
- Secure negotiation: The Marketplace platform manages secure communication and negotiation between partners and customers.
- Transaction management: The platform handles purchase, billing, and fulfillment, ensuring compliance with regional regulations in Malaysia and Saudi Arabia.
- Integration with partner management tools: Offers are tracked and managed through Azure’s partner ecosystem, allowing for seamless coordination.

**Use Cases and Application Scenarios**  
Common scenarios include:
- ISVs collaborating with local resellers to deliver cloud and AI solutions to enterprise customers in Malaysia and Saudi Arabia.
- Partners leveraging established customer relationships to introduce new third-party solutions, accelerating digital transformation projects.
- Customers benefiting from customized offers that meet specific technical and business requirements, with local support and compliance.

**Important Considerations and Limitations**  
- Regional availability: Multiparty private offers are now available in Malaysia and Saudi Arabia; partners outside these regions must verify local support.
- Compliance: All transactions must adhere to local regulatory requirements, which may affect offer structure and fulfillment.
- Partner eligibility: Only Microsoft partners with Marketplace access and appropriate permissions can participate in multiparty private offers.
- Solution scope: The feature is focused on third-party cloud and AI solutions; applicability to other solution types should be verified.

**Integration with Related Azure Services**  
Multiparty private offers integrate seamlessly with Azure Marketplace, Azure billing and subscription management, and partner management tools. This ensures that offers are tracked, fulfilled, and supported within the broader Azure ecosystem, providing unified management and reporting capabilities for partners and customers.

**Summary Sentence**  
Multiparty private offers in Microsoft Marketplace are now available in Malaysia and Saudi Arabia, enabling partners to collaboratively procure third-party cloud and AI solutions for customers, expanding market reach and streamlining procurement through tailored, secure, and compliant transactions.

---

### 2. Generally Available: Soft delete in Azure Compute Gallery 

**Published**: November 19, 2026 23:47:55 UTC
**Link**: [Generally Available: Soft delete in Azure Compute Gallery ](https://azure.microsoft.com/updates?id=581907)

**Update ID**: 581907
**Data source**: Azure Updates API

**Categories**: Launched, Features, Microsoft Ignite

**Summary**:

- What was updated  
Soft delete functionality in Azure Compute Gallery is now generally available.

- Key changes or new features  
Soft delete allows recovery of accidentally deleted image versions in Azure Compute Gallery. You can configure a retention period between 7 and 365 days. During the retention period, soft-deleted images remain accessible for deployment (using supported API versions). This feature helps prevent data loss and enables easier image management.

- Target audience affected  
Developers and IT professionals managing VM images in Azure Compute Gallery, especially those responsible for image lifecycle, backup, and disaster recovery.

- Important notes  
Soft-deleted images can still be used for deployments during the retention period. After the retention period expires, images are permanently deleted and cannot be recovered. Ensure your API version supports this feature. Review and adjust retention policies as needed for compliance and operational requirements.

For more details, see the official Azure Update: [Soft delete in Azure Compute Gallery](https://azure.microsoft.com/updates?id=581907).

**Details**:

**Azure Update Report: Soft Delete in Azure Compute Gallery (Generally Available)**

**Background and Purpose of the Update**  
Azure Compute Gallery (formerly Shared Image Gallery) is a centralized repository for managing and sharing VM images across Azure environments. Accidental deletion of image versions can disrupt operations and complicate recovery. The introduction of soft delete addresses this risk by enabling recovery of deleted image versions, thereby enhancing operational resilience and data protection.

**Specific Features and Detailed Changes**  
The soft delete feature is now generally available in Azure Compute Gallery. When an image version is deleted, it is not permanently removed; instead, it enters a soft-deleted state. Administrators can configure a retention period ranging from 7 to 365 days, during which the deleted image version remains recoverable. Notably, even while in the soft-deleted state, image versions can still be used for deployment, ensuring continuity of service and minimizing downtime.

**Technical Mechanisms and Implementation Methods**  
Soft delete is implemented at the image version level within Azure Compute Gallery. Upon deletion, the image version is flagged as soft-deleted and retained in the gallery for the specified period. Recovery operations can be performed via supported API versions, allowing restoration of the image version to its original state. The retention period is configurable, providing flexibility to align with organizational policies and compliance requirements. During the retention window, the image version remains accessible for deployment operations, which is managed through the gallery’s API.

**Use Cases and Application Scenarios**  
- **Accidental Deletion Recovery:** Organizations can quickly restore image versions that were deleted unintentionally, reducing the risk of service disruption.
- **Operational Continuity:** Soft-deleted images can still be used for VM deployments, supporting ongoing operations while recovery decisions are made.
- **Change Management:** IT teams can implement safer image lifecycle management, knowing that deletions are reversible within the retention period.
- **Compliance and Audit:** The retention period can be set to meet regulatory requirements for data retention and recovery.

**Important Considerations and Limitations**  
- The retention period must be set between 7 and 365 days; image versions are permanently deleted after this period.
- Recovery and deployment from soft-deleted images require use of the appropriate API version (details available in Azure documentation).
- Soft delete applies only to image versions, not to other gallery resources.
- Administrators should ensure retention settings align with organizational backup and recovery policies.
- Permanent deletion is irreversible; after the retention window, recovery is not possible.

**Integration with Related Azure Services**  
Soft delete in Azure Compute Gallery integrates seamlessly with Azure VM provisioning workflows. It complements Azure’s broader data protection features, such as backup and recovery, by providing an additional layer of image version protection. The feature is accessible via Azure APIs, enabling automation and integration with CI/CD pipelines and image management tools.

**Summary Sentence**  
Soft delete in Azure Compute Gallery is now generally available, allowing IT professionals to recover accidentally deleted image versions within a configurable retention period of 7 to 365 days, and enabling deployment from soft-deleted images to ensure operational continuity.

---

### 3. Public Preview: PostgreSQL 19 on Azure Database for PostgreSQL  

**Published**: November 19, 2026 23:25:49 UTC
**Link**: [Public Preview: PostgreSQL 19 on Azure Database for PostgreSQL  ](https://azure.microsoft.com/updates?id=574587)

**Update ID**: 574587
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
PostgreSQL 19 is now available in public preview on Azure Database for PostgreSQL – Flexible Server, specifically in the East Asia region.

- Key changes or new features  
Developers and IT professionals can provision new PostgreSQL 19 servers using the Azure portal and Azure CLI. This release allows users to test and evaluate major version 19 features, including performance improvements, new SQL capabilities, and enhanced security options. The preview supports experimentation and validation of workloads before general availability.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals who use Azure Database for PostgreSQL – Flexible Server and are interested in adopting or testing the latest PostgreSQL features.

- Important notes if any  
The PostgreSQL 19 public preview is currently limited to the East Asia region. Workloads deployed during the preview may not be suitable for production use, as preview features may lack full support and stability. Users should monitor Azure documentation for updates on regional availability and general release status.

**Details**:

**Azure Update Technical Report: Public Preview of PostgreSQL 19 on Azure Database for PostgreSQL – Flexible Server (East Asia Region)**  
[Azure Update Link](https://azure.microsoft.com/updates?id=574587)

---

**Background and Purpose of the Update**  
Microsoft Azure has announced the public preview of PostgreSQL 19 on Azure Database for PostgreSQL – Flexible Server, specifically available in the East Asia region. The primary purpose of this update is to provide early access to the latest major version of PostgreSQL, allowing IT professionals and developers to evaluate, test, and prepare for adoption of new features and improvements before general availability. This aligns with Azure’s commitment to supporting the latest open-source database technologies and facilitating innovation in cloud-native application development.

**Specific Features and Detailed Changes**  
With this update, users can provision new PostgreSQL 19 servers directly through the Azure portal and Azure CLI. The preview enables testing of all major version 19 features as implemented by the PostgreSQL community. While the detailed feature set of PostgreSQL 19 is not enumerated in the update, the preview allows users to explore enhancements in performance, security, and SQL capabilities inherent to the new version. The Flexible Server deployment model offers granular control over server configuration, maintenance, and scaling options.

**Technical Mechanisms and Implementation Methods**  
Provisioning PostgreSQL 19 servers is facilitated via the Azure portal and Azure CLI, leveraging the Flexible Server deployment model. This model provides flexibility in server configuration, including compute, storage, and networking options. The implementation ensures that users can spin up isolated PostgreSQL 19 instances for development and testing purposes, with full access to the database engine’s new features. Azure’s infrastructure manages the underlying hardware, OS, and patching, allowing users to focus on database-specific tasks.

**Use Cases and Application Scenarios**  
- **Application Modernization:** Developers can test application compatibility with PostgreSQL 19, ensuring readiness for production migration once the version is generally available.
- **Feature Evaluation:** Database administrators and architects can evaluate new SQL features, performance improvements, and security enhancements introduced in PostgreSQL 19.
- **Dev/Test Environments:** Teams can set up isolated environments to validate new workloads and optimize schema designs for PostgreSQL 19.
- **Continuous Integration/Continuous Deployment (CI/CD):** Integration pipelines can be updated to include PostgreSQL 19 for automated testing of application changes.

**Important Considerations and Limitations**  
- **Regional Availability:** The public preview is currently limited to the East Asia region, restricting access for users in other geographies.
- **Preview Limitations:** As a public preview, PostgreSQL 19 may not be suitable for production workloads. Users should expect potential instability and limited support.
- **Upgrade Path:** There is no information provided regarding upgrade paths from earlier PostgreSQL versions to 19 within Flexible Server.
- **Feature Set:** Only the features available in the PostgreSQL 19 community release are accessible; Azure-specific enhancements may be limited during the preview phase.

**Integration with Related Azure Services**  
PostgreSQL 19 on Azure Database for PostgreSQL – Flexible Server integrates seamlessly with Azure’s ecosystem, including:
- **Azure Portal and Azure CLI:** For provisioning and management.
- **Azure Networking:** For configuring VNETs, private endpoints, and firewall rules.
- **Azure Monitoring:** For performance metrics and alerting.
- **Azure Backup and Restore:** For data protection and recovery.
- **Azure Security:** For role-based access control and compliance management.

---

**Summary Sentence:**  
Azure Database for PostgreSQL – Flexible Server now offers a public preview of PostgreSQL 19 in the East Asia region, enabling IT professionals to provision and test the latest major version through the Azure portal and CLI, with full access to new features and integration capabilities for development and evaluation purposes.

---

### 4. Public Preview: Zone resilience for Azure VMs

**Published**: November 19, 2026 20:34:19 UTC
**Link**: [Public Preview: Zone resilience for Azure VMs](https://azure.microsoft.com/updates?id=581254)

**Update ID**: 581254
**Data source**: Azure Updates API

**Categories**: In preview, Features, Microsoft Inspire

**Summary**:

- What was updated  
Zone resilience for Azure Virtual Machines (VMs) is now available in public preview.

- Key changes or new features  
This feature enables recovery of eligible zonal VMs in a different availability zone within the same region, while retaining the VM resource and its configuration. Zone-redundant storage (ZRS) managed disks replicate data synchronously across zones, ensuring data durability and minimizing downtime during zone failures. The recovery process leverages ZRS managed disks to restore VMs quickly and efficiently.

- Target audience affected  
Developers and IT professionals managing workloads on Azure VMs, especially those requiring high availability and disaster recovery within a region.

- Important notes if any  
Zone resilience is currently in public preview and only available for eligible zonal VMs using ZRS managed disks. Review the documentation to confirm VM and disk eligibility. This feature helps improve business continuity by reducing recovery time and maintaining VM configurations during zone outages.  
For more details, visit the [Azure Update page](https://azure.microsoft.com/updates?id=581254).

**Details**:

**Azure Update Report: Public Preview – Zone Resilience for Azure VMs**

**Background and Purpose of the Update**  
Zone resilience for Azure Virtual Machines (VMs) addresses the need for enhanced high availability and disaster recovery within Azure regions. Traditionally, zonal VMs are tied to a single availability zone, which exposes workloads to potential downtime if that zone experiences a failure. The purpose of this update is to allow eligible zonal VMs to be recovered in another availability zone within the same region, thereby improving business continuity and reducing the risk of service disruption.

**Specific Features and Detailed Changes**  
The update introduces the capability to recover an eligible zonal VM in a different availability zone while retaining the existing VM resource and configuration. This means that, in the event of a zone-level outage, the VM can be restored in another zone without the need to recreate the VM or manually reconfigure its settings. The feature leverages ZRS (Zone-Redundant Storage) managed disks, which replicate data synchronously across multiple zones within a region, ensuring that the VM’s disk data is always available for recovery.

**Technical Mechanisms and Implementation Methods**  
Zone resilience is achieved through the use of ZRS managed disks. ZRS disks provide synchronous replication of data across three availability zones within a region. When a zonal VM is configured with ZRS disks, its disk data is continuously replicated, enabling rapid recovery in another zone if the original zone fails. The recovery process retains the VM’s resource identity and configuration, simplifying operational management and minimizing downtime. The mechanism is integrated at the storage layer, ensuring that VM disks are always accessible from any zone in the region.

**Use Cases and Application Scenarios**  
Zone resilience is particularly valuable for mission-critical workloads that require high availability and minimal downtime, such as enterprise applications, databases, and web services. It is also beneficial for organizations with strict compliance or business continuity requirements, where the ability to recover VMs seamlessly across zones can meet regulatory standards and service level agreements (SLAs). Typical scenarios include multi-tier applications, financial services platforms, and healthcare systems that must remain operational during zone-level failures.

**Important Considerations and Limitations**  
- Only eligible zonal VMs can leverage zone resilience; eligibility depends on VM configuration and disk type.
- ZRS managed disks are required for synchronous replication across zones; VMs using other disk types (such as LRS or GRS) are not supported.
- The feature is currently in public preview, which may entail limitations in support, feature completeness, and production readiness.
- Recovery is limited to availability zones within the same region; cross-region recovery is not supported.
- IT professionals should review Azure documentation for supported VM sizes, disk types, and any preview-specific constraints.

**Integration with Related Azure Services**  
Zone resilience for Azure VMs integrates closely with Azure managed disks (specifically ZRS), Azure Availability Zones, and Azure VM resource management. It complements existing high availability solutions such as Azure Site Recovery and Azure Backup by providing intra-region, zone-level recovery capabilities. This integration allows for seamless management of VM resources and storage, enhancing overall resilience within the Azure ecosystem.

**Summary Sentence**  
Zone resilience for Azure VMs, now in public preview, enables eligible zonal VMs to be recovered in another availability zone within the same region while retaining their existing resource and configuration, using ZRS managed disks for synchronous data replication across zones.

---

### 5. Public Preview: Database Agent for Azure Database for PostgreSQL 

**Published**: November 19, 2026 17:25:28 UTC
**Link**: [Public Preview: Database Agent for Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=579579)

**Update ID**: 579579
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database Agent for Azure Database for PostgreSQL is now available in Public Preview.

- Key changes or new features  
The Database Agent introduces proactive monitoring for Azure Database for PostgreSQL. It automatically detects and surfaces database health and performance issues, consolidates metrics and configuration data, and provides actionable insights to help users understand and respond to problems faster. The agent streamlines troubleshooting by offering a unified view of database telemetry and health indicators.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals managing Azure Database for PostgreSQL instances. It is particularly useful for teams responsible for database performance, reliability, and incident response.

- Important notes if any  
The Database Agent is currently in Public Preview, so features and functionality may evolve based on user feedback. Early adopters should test the agent in non-production environments and review documentation for integration details. The agent aims to reduce manual monitoring overhead and improve response times to database issues. For more information and to get started, visit the official Azure Update page: https://azure.microsoft.com/updates?id=579579

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Database Agent for Azure Database for PostgreSQL  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579579)

---

**Background and Purpose of the Update**

The Database Agent for Azure Database for PostgreSQL has been introduced in public preview to address the need for enhanced monitoring, diagnostics, and response capabilities within managed PostgreSQL environments on Azure. The primary goal is to enable IT professionals and database administrators to proactively detect, understand, and respond to database health and performance issues, thereby improving operational efficiency and minimizing downtime.

---

**Specific Features and Detailed Changes**

- **Proactive Health Monitoring:** The Database Agent continuously monitors the health of PostgreSQL databases, enabling early detection of issues before they impact application performance or availability.
- **Centralized Metrics and Configuration:** The agent aggregates database metrics and configuration data, providing a unified view of the database’s operational state.
- **Issue Identification:** It identifies potential performance bottlenecks, configuration anomalies, and other health-related concerns, facilitating faster troubleshooting and remediation.
- **Enhanced Visibility:** By consolidating health and performance information, the agent offers improved visibility into database operations, supporting informed decision-making.

---

**Technical Mechanisms and Implementation Methods**

- **Agent-Based Architecture:** The Database Agent operates as a monitoring component within the Azure Database for PostgreSQL managed service. It collects telemetry data, including performance metrics and configuration details, directly from the database instance.
- **Data Aggregation:** Metrics and configuration information are brought together in a centralized manner, enabling correlation and analysis of database health indicators.
- **Automated Detection:** The agent leverages built-in logic to automatically detect issues, reducing the need for manual monitoring and intervention.
- **Integration with Azure Monitoring:** While the update does not specify integration details, the agent’s collected data is likely designed to complement existing Azure monitoring and diagnostic tools, such as Azure Monitor and Azure Advisor.

---

**Use Cases and Application Scenarios**

- **Production Workloads:** IT teams managing mission-critical PostgreSQL databases can use the Database Agent to ensure optimal performance and rapid response to issues.
- **Performance Troubleshooting:** The agent assists in identifying and resolving performance bottlenecks, configuration errors, and other operational challenges.
- **Compliance and Auditing:** Centralized metrics and configuration data can support compliance requirements and auditing processes by providing a clear record of database health and changes.
- **DevOps Automation:** The agent’s proactive monitoring capabilities can be integrated into DevOps workflows for automated alerting and remediation.

---

**Important Considerations and Limitations**

- **Preview Status:** The Database Agent is currently in public preview, which may imply limited feature set, incomplete documentation, or potential changes before general availability.
- **Scope of Monitoring:** The update does not specify the full range of metrics or configuration parameters monitored, nor does it detail integration with external alerting or automation systems.
- **Resource Overhead:** As with any monitoring agent, there may be additional resource consumption on the database instance, which should be evaluated during deployment.

---

**Integration with Related Azure Services**

- **Azure Database for PostgreSQL:** The agent is native to Azure’s managed PostgreSQL offering, ensuring seamless integration and compatibility.
- **Azure Monitoring Ecosystem:** Although not explicitly detailed, the agent’s metrics and health data are expected to align with Azure’s broader monitoring and diagnostic services, enhancing overall observability.

---

**Summary Sentence**

The Database Agent for Azure Database for PostgreSQL, now in public preview, provides proactive health and performance monitoring by aggregating metrics and configuration data, enabling IT professionals to detect and respond to database issues more efficiently within Azure’s managed PostgreSQL environment.

---


*This report was automatically generated - 2026-11-20 03:03:18 UTC*