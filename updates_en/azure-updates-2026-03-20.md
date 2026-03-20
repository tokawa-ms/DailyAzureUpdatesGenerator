# March 20, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: March 20, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Public Preview: Azure Databricks OneLake Catalog Federation 

**Published**: March 19, 2026 17:00:53 UTC
**Link**: [Public Preview: Azure Databricks OneLake Catalog Federation ](https://azure.microsoft.com/updates?id=558927)

**Update ID**: 558927
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Analytics, Azure Databricks, Features

**Summary**:

- What was updated  
Azure Databricks now supports OneLake Catalog Federation in public preview, enabling direct integration with Microsoft Fabric OneLake data.

- Key changes or new features  
Developers and data engineers can connect Azure Databricks Unity Catalog to a OneLake catalog, allowing Databricks to automatically synchronize schemas and tables from Microsoft Fabric OneLake. This enables querying and analyzing OneLake data directly from Databricks without the need to copy or move data, streamlining data access and reducing data duplication.

- Target audience affected  
This update is relevant for data engineers, developers, and IT professionals working with Azure Databricks, Microsoft Fabric, and OneLake for analytics, data engineering, or data science workloads.

- Important notes if any  
The feature is currently in public preview and may not be suitable for production workloads. Users should review documentation for setup and limitations. This integration helps organizations simplify data governance and improve productivity by leveraging a unified data catalog across Azure Databricks and Microsoft Fabric OneLake.

For more details, see the [official update](https://azure.microsoft.com/updates?id=558927).

**Details**:

**Azure Update Report: Public Preview – Azure Databricks OneLake Catalog Federation**

**Background and Purpose of the Update:**  
This update introduces the public preview of OneLake catalog federation in Azure Databricks. The primary goal is to enable seamless data access between Azure Databricks and Microsoft Fabric OneLake, eliminating the need to copy or move data. This addresses common challenges in data integration, such as data duplication, synchronization overhead, and latency, by allowing direct querying of data stored in OneLake from within Databricks environments.

**Specific Features and Detailed Changes:**  
- **OneLake Catalog Federation:** Azure Databricks now supports connecting its Unity Catalog directly to a OneLake catalog.
- **Automatic Schema and Table Synchronization:** Once federation is enabled, Azure Databricks automatically synchronizes schemas and tables from the OneLake catalog. This ensures that Databricks users have up-to-date metadata and can discover new or updated tables in OneLake without manual intervention.
- **Direct Query Capability:** Users can query Microsoft Fabric OneLake data from Databricks without the need to copy or physically move datasets.

**Technical Mechanisms and Implementation Methods:**  
- **Catalog Connection:** The federation is established by connecting the Unity Catalog in Azure Databricks to a OneLake catalog. This connection enables Databricks to access OneLake metadata and data assets.
- **Metadata Synchronization:** Upon connection, Unity Catalog periodically syncs schema definitions and table metadata from OneLake, ensuring that Databricks reflects the current state of the OneLake catalog.
- **Federated Query Execution:** Queries executed in Databricks are able to reference tables in OneLake directly, leveraging the underlying data storage without data duplication.

**Use Cases and Application Scenarios:**  
- **Cross-Platform Analytics:** Data engineers and analysts can perform analytics on data residing in Microsoft Fabric OneLake from within Databricks notebooks or jobs, supporting scenarios such as unified reporting, ML model training, and data exploration.
- **Data Governance and Catalog Unification:** Organizations using both Azure Databricks and Microsoft Fabric can maintain a single source of truth for data definitions and governance policies by federating catalogs.
- **Operational Efficiency:** Eliminates the need for ETL pipelines to move data between OneLake and Databricks, reducing operational complexity and storage costs.

**Important Considerations and Limitations:**  
- **Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should be aware of potential changes or limitations in functionality and support.
- **Data Consistency and Security:** While schemas and tables are synchronized, users must ensure that appropriate access controls and data governance policies are enforced across both platforms.
- **Performance Considerations:** Query performance may depend on the underlying OneLake storage and network connectivity, as data is not cached or copied into Databricks.

**Integration with Related Azure Services:**  
- **Unity Catalog:** Serves as the integration point within Databricks, managing metadata and access control for federated data assets.
- **Microsoft Fabric OneLake:** Acts as the source data lake, providing storage and cataloging for datasets accessible by Databricks.
- **Azure Data Governance:** This federation supports unified data governance strategies, leveraging Azure’s security and compliance features across both Databricks and Fabric environments.

**Summary Sentence:**  
Azure Databricks now supports public preview of OneLake catalog federation, enabling direct querying of Microsoft Fabric OneLake data via Unity Catalog with automatic schema and table synchronization, streamlining cross-platform analytics and data governance without data movement.

---

### 2. Retirement: HC-series Azure Virtual Machines will be retired on May 31, 2027

**Published**: March 19, 2026 16:30:27 UTC
**Link**: [Retirement: HC-series Azure Virtual Machines will be retired on May 31, 2027](https://azure.microsoft.com/updates?id=548543)

**Update ID**: 548543
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machines, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of HC-series Azure Virtual Machines (VMs), specifically the Standard_HC44rs, Standard_HC44-16rs, and Standard_HC44-32rs sizes. These VM sizes will be retired on May 31, 2027.

- Key changes or new features  
After May 31, 2027, the specified HC-series VM sizes will no longer be available for deployment or support. Microsoft recommends migrating workloads to newer VM series for improved performance and ongoing support.

- Target audience affected  
This update affects developers, IT professionals, and organizations currently using HC-series VMs for high-performance computing (HPC) workloads, such as engineering simulations, computational fluid dynamics, and other compute-intensive applications.

- Important notes if any  
To avoid service disruption, users must plan and execute migration to supported VM sizes before the retirement date. Review current workloads and test compatibility with recommended replacement VM series. Early migration ensures continued support, access to new features, and better performance. For more details and migration guidance, refer to the official Azure update: https://azure.microsoft.com/updates?id=548543

**Details**:

**Azure Update Report: Retirement of HC-series Azure Virtual Machines (Effective May 31, 2027)**

**Background and Purpose of the Update**  
Microsoft Azure has announced the retirement of specific HC-series virtual machine (VM) sizes—namely, Standard_HC44rs, Standard_HC44-16rs, and Standard_HC44-32rs—effective May 31, 2027. The primary purpose of this update is to phase out these older VM sizes, encouraging customers to transition to newer, more performant, and supported VM offerings. This aligns with Azure’s ongoing lifecycle management strategy to deprecate legacy infrastructure and promote the adoption of advanced compute resources.

**Specific Features and Detailed Changes**  
The retirement specifically targets the following VM sizes:
- Standard_HC44rs
- Standard_HC44-16rs
- Standard_HC44-32rs

After May 31, 2027, these VM sizes will no longer be available for deployment or scaling. Existing instances must be migrated to supported VM series prior to the retirement date to avoid service disruption. No other HC-series sizes are mentioned in this update.

**Technical Mechanisms and Implementation Methods**  
The retirement will be enforced at the Azure platform level. This means:
- Creation of new VMs using the retired sizes will be blocked after the retirement date.
- Existing VMs of these sizes may be deallocated or deleted and cannot be re-provisioned.
- Customers are advised to plan and execute migration strategies to alternative VM sizes well before the cutoff date.

Migration typically involves:
- Assessing current workloads running on HC-series VMs.
- Identifying compatible VM sizes in the current Azure portfolio that meet or exceed existing performance requirements.
- Testing and validating application compatibility and performance on the new VM sizes.
- Updating deployment scripts, templates, and automation to reference the new VM sizes.

**Use Cases and Application Scenarios**  
The HC-series VMs are designed for high-performance computing (HPC) workloads, such as:
- Computational fluid dynamics (CFD)
- Finite element analysis
- Molecular modeling
- Other tightly-coupled parallel compute applications

Organizations leveraging these VM sizes for HPC workloads must review their compute requirements and transition to supported VM offerings that provide similar or improved performance characteristics.

**Important Considerations and Limitations**  
- All workloads running on Standard_HC44rs, Standard_HC44-16rs, and Standard_HC44-32rs must be migrated by May 31, 2027.
- Failure to migrate may result in service outages or loss of compute resources.
- Customers should validate that their chosen replacement VM sizes support required features such as InfiniBand networking, high memory bandwidth, and CPU core counts.
- Review Azure’s documentation and support channels for migration guidance and best practices.

**Integration with Related Azure Services**  
These VM sizes are commonly integrated with:
- Azure Batch for large-scale parallel job scheduling
- Azure CycleCloud for HPC cluster orchestration
- Azure Virtual Network for high-throughput, low-latency interconnects

When migrating, ensure that the new VM sizes are compatible with these services and that any required extensions or drivers are supported.

---

**Summary:**  
Microsoft Azure will retire the Standard_HC44rs, Standard_HC44-16rs, and Standard_HC44-32rs VM sizes on May 31, 2027; customers should plan to migrate affected workloads to supported VM offerings to ensure uninterrupted service and improved performance.

---

### 3. Retirement: HBv2-series Azure Virtual Machines will be retired on May 31, 2027

**Published**: March 19, 2026 16:30:27 UTC
**Link**: [Retirement: HBv2-series Azure Virtual Machines will be retired on May 31, 2027](https://azure.microsoft.com/updates?id=548525)

**Update ID**: 548525
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machines, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of HBv2-series Azure Virtual Machines (VMs), including the following sizes: Standard_HB120rs_v2, Standard_HB120-96rs_v2, Standard_HB120-64rs_v2, Standard_HB120-32rs_v2, and Standard_HB120-16rs_v2. The retirement date is set for May 31, 2027.

- Key changes or new features  
After May 31, 2027, the above HBv2-series VM sizes will no longer be available for deployment or scaling. Customers must transition their workloads to alternative VM series, such as the HBv3-series, which offer improved performance, scalability, and updated hardware features.

- Target audience affected  
This update impacts IT professionals, infrastructure administrators, and developers currently running workloads on HBv2-series VMs, especially those managing high-performance computing (HPC) environments.

- Important notes if any  
To avoid service disruption, plan and migrate workloads from HBv2-series VMs to supported alternatives before the retirement date. Review application compatibility and performance requirements when selecting replacement VM sizes. Microsoft recommends leveraging newer VM series for enhanced capabilities and ongoing support. For more details and migration guidance, refer to the official Azure update: https://azure.microsoft.com/updates?id=548525

**Details**:

**Azure Update Report: Retirement of HBv2-series Azure Virtual Machines on May 31, 2027**

**Background and Purpose of the Update**  
Microsoft Azure has announced the retirement of the HBv2-series virtual machine (VM) sizes, effective May 31, 2027. The retirement affects the following VM sizes: Standard_HB120rs_v2, Standard_HB120-96rs_v2, Standard_HB120-64rs_v2, Standard_HB120-32rs_v2, and Standard_HB120-16rs_v2. The primary purpose of this update is to phase out older HBv2-series hardware and encourage customers to transition to newer VM series that offer enhanced performance, improved scalability, and better support for modern workloads.

**Specific Features and Detailed Changes**  
The HBv2-series VMs are designed for high-performance computing (HPC) workloads, particularly those requiring significant CPU and memory resources. After May 31, 2027, these specific VM sizes will no longer be available for provisioning, and existing deployments will need to be migrated to supported VM series. This change impacts all regions and customers utilizing the listed HBv2 VM sizes.

**Technical Mechanisms and Implementation Methods**  
The retirement will be enforced at the platform level. After the retirement date, Azure Resource Manager (ARM) will prevent the creation of new instances of the retired VM sizes. Existing VMs of these sizes may be deallocated or deleted, depending on Microsoft’s retirement policy. Customers must plan and execute migration strategies to supported VM families before the cutoff date to avoid service disruption. Migration typically involves resizing VMs to a supported SKU, updating deployment templates, and validating workload compatibility.

**Use Cases and Application Scenarios**  
HBv2-series VMs are commonly used in technical computing scenarios such as computational fluid dynamics, finite element analysis, weather modeling, and other CPU-bound HPC applications. Organizations leveraging these VM sizes for research, engineering simulation, or large-scale parallel processing must identify alternative VM series that meet their performance and scalability requirements.

**Important Considerations and Limitations**  
- **Migration Planning:** Customers must assess their current workloads and plan for migration to newer VM series before May 31, 2027, to ensure business continuity.
- **Compatibility Testing:** It is essential to validate application performance and compatibility on the target VM series prior to migration.
- **Resource Availability:** Some features or hardware accelerations available in HBv2 may differ in newer VM series; review documentation for feature parity.
- **Automation and Templates:** Update ARM templates, scripts, and automation workflows to reference supported VM sizes.
- **Support:** After the retirement date, Microsoft support for HBv2-series VMs will be discontinued.

**Integration with Related Azure Services**  
HBv2-series VMs are often integrated with Azure Batch, Azure CycleCloud, Azure HPC Cache, and Azure Virtual Network for large-scale HPC workloads. Migration to newer VM series may require reconfiguration of these integrations to ensure optimal performance and compatibility. Customers should review dependencies and update service configurations as part of their migration plan.

**Summary**  
Microsoft Azure will retire HBv2-series VM sizes on May 31, 2027, requiring customers to migrate affected workloads to supported VM series to maintain service continuity and leverage improved platform capabilities.

---

### 4. Retirement: NP-series Azure Virtual Machines will be retired on May 31, 2027 

**Published**: March 19, 2026 16:30:27 UTC
**Link**: [Retirement: NP-series Azure Virtual Machines will be retired on May 31, 2027 ](https://azure.microsoft.com/updates?id=548497)

**Update ID**: 548497
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machines, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of NP-series Azure Virtual Machines (VMs)—specifically the Standard_NP10s, Standard_NP20s, and Standard_NP40s sizes—effective May 31, 2027.

- Key changes or new features  
These NP-series VM sizes will no longer be available after the retirement date. Customers using these VMs are advised to migrate their workloads to alternative Azure GPU VM offerings to maintain service continuity and performance. Microsoft recommends evaluating the latest GPU VM series for improved capabilities and support.

- Target audience affected  
This update impacts developers, IT professionals, and organizations currently running workloads on NP-series VMs, particularly those utilizing GPU acceleration for AI, machine learning, or graphics-intensive applications.

- Important notes if any  
Action is required before May 31, 2027, to avoid service disruptions. Begin planning and testing migration to supported GPU VM sizes as soon as possible. Review the Azure documentation for guidance on selecting replacement VM sizes and migration best practices. No automatic migration will occur; manual intervention is necessary. For more details, refer to the official Azure update: https://azure.microsoft.com/updates?id=548497

**Details**:

**Azure Update Report: Retirement of NP-series Azure Virtual Machines (May 31, 2027)**

**Background and Purpose of the Update:**  
Microsoft Azure has announced the retirement of the NP-series Virtual Machine (VM) sizes—specifically Standard_NP10s, Standard_NP20s, and Standard_NP40s—effective May 31, 2027. The NP-series VMs are GPU-enabled instances designed for workloads requiring parallel processing capabilities, such as deep learning, AI model training, and high-performance computing (HPC). The purpose of this update is to phase out these legacy VM sizes and encourage customers to migrate to newer Azure GPU VM offerings that provide enhanced performance, scalability, and support.

**Specific Features and Detailed Changes:**  
The retirement affects three VM sizes: Standard_NP10s, Standard_NP20s, and Standard_NP40s. After May 31, 2027, these VM sizes will no longer be available for deployment or scaling operations. Existing workloads running on these sizes must be transitioned to alternative GPU VM families before the retirement date to avoid service disruption. Microsoft recommends migrating to other Azure GPU VM families, which offer improved hardware specifications, updated drivers, and better integration with Azure’s evolving infrastructure.

**Technical Mechanisms and Implementation Methods:**  
The retirement process will be managed through Azure’s lifecycle management policies. After the retirement date, the NP-series VM sizes will be removed from the Azure portal, CLI, and ARM templates, preventing new deployments or scaling of existing resources. Customers should plan and execute migration strategies using Azure Migrate or custom scripts to move workloads to supported GPU VM families. This may involve updating VM images, reconfiguring networking, and validating application compatibility with the new VM hardware.

**Use Cases and Application Scenarios:**  
NP-series VMs are commonly used for GPU-intensive workloads, including machine learning training, inferencing, scientific simulations, and graphics rendering. Organizations leveraging these VMs for AI development, data analytics, or visualization tasks must identify suitable replacement VM sizes that meet their performance and compatibility requirements. Azure’s newer GPU VM families are designed to support these scenarios with improved compute power, memory, and GPU capabilities.

**Important Considerations and Limitations:**  
- **Migration Deadline:** All NP-series VM workloads must be migrated by May 31, 2027, to avoid service interruption.
- **Compatibility:** Applications may require validation and testing on the new GPU VM sizes to ensure compatibility and performance.
- **Resource Planning:** Customers should assess their current usage and plan for resource allocation, including updating automation scripts and infrastructure-as-code templates.
- **Cost Implications:** Pricing and billing may differ between NP-series and newer GPU VM families; review cost estimates before migration.

**Integration with Related Azure Services:**  
Migrating away from NP-series VMs may impact integration with Azure services such as Azure Machine Learning, Azure Batch, and Azure Kubernetes Service (AKS) if these workloads are GPU-dependent. Ensure that the new VM sizes are supported by these services and update configurations accordingly. Azure Migrate and Azure Advisor can assist with migration planning and optimization.

**Summary Sentence:**  
Microsoft Azure will retire the NP-series VM sizes (Standard_NP10s, Standard_NP20s, and Standard_NP40s) on May 31, 2027, and recommends transitioning workloads to newer Azure GPU VM families to maintain service continuity and performance.

---


*This report was automatically generated - 2026-03-20 03:03:12 UTC*