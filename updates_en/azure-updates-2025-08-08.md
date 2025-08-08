# August 08, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 08, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Generally Available: Azure 128 & 192 vCPU sizes for the Esv6 and Edsv6 series VMs

**Published**: August 07, 2025 16:00:43 UTC
**Link**: [Generally Available: Azure 128 & 192 vCPU sizes for the Esv6 and Edsv6 series VMs](https://azure.microsoft.com/updates?id=499918)

**Update ID**: 499918
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines, Features

**Summary**:

- What was updated  
Azure has introduced generally available 128 and 192 vCPU VM sizes within the Esv6 and Edsv6 series.

- Key changes or new features  
These new VM sizes provide up to 192 vCPUs and 1832 GiB of RAM, designed to handle enterprise-scale workloads such as in-memory analytics, large relational databases, and in-memory caching. They include enhanced security features like Intel® Total Memory Encryption (Intel TME) to protect data in use.

- Target audience affected  
This update primarily benefits developers and IT professionals managing large-scale, compute-intensive applications requiring high memory and CPU capacity, including database administrators and analytics engineers.

- Important notes if any  
These VM sizes expand Azure’s capability to support demanding workloads with improved performance and security. Users should evaluate workload compatibility and cost implications when adopting these larger VM sizes. Availability may vary by region. For detailed specifications and pricing, refer to the official Azure documentation.

**Details**:

The recent general availability of Azure 128 and 192 vCPU VM sizes within the Esv6 and Edsv6 series significantly expands Azure’s capacity for high-performance, enterprise-grade workloads by offering virtual machines with up to 192 vCPUs and 1832 GiB of RAM. This update addresses the growing demand for large-scale compute resources optimized for memory-intensive and latency-sensitive applications such as in-memory analytics, large relational databases, and in-memory caching.

**Background and Purpose**  
As enterprises increasingly rely on data-intensive applications requiring substantial CPU and memory resources, Azure’s existing VM offerings needed to scale further to meet these demands. The Esv6 and Edsv6 series, based on the 3rd Generation Intel Xeon Scalable processors (Ice Lake), were previously available in smaller sizes. By introducing 128 and 192 vCPU sizes, Microsoft aims to provide customers with the ability to run large-scale, compute- and memory-heavy workloads more efficiently on a single VM, reducing the complexity and overhead of distributed architectures.

**Specific Features and Detailed Changes**  
- **VM Sizes**: The new sizes offer 128 and 192 virtual CPUs, paired with up to 1832 GiB of RAM, significantly increasing the compute and memory ceiling within the Esv6/Eds6v series.  
- **Processor Architecture**: These VMs leverage Intel’s Ice Lake processors, which provide improved performance per core, enhanced memory bandwidth, and advanced security features.  
- **Intel Total Memory Encryption (Intel TME)**: The Edsv6 series supports Intel TME, which encrypts the entire memory of the VM to protect data at rest in memory from physical attacks, enhancing security for sensitive workloads.  
- **Premium Storage Support**: These VMs support premium SSD storage, enabling high IOPS and low latency for demanding database and analytics workloads.  
- **Enhanced Networking**: They include accelerated networking capabilities, providing low latency and high throughput network performance essential for distributed and clustered applications.

**Technical Mechanisms and Implementation Methods**  
The VMs are implemented on Azure’s hyper-scale infrastructure, utilizing Intel’s Ice Lake CPUs with up to 3rd Gen Intel Xeon Scalable processors. The virtualization stack is optimized to support large NUMA nodes, ensuring efficient memory access and CPU scheduling across the high vCPU counts. Intel TME is integrated at the hardware level, transparently encrypting memory without impacting application performance. Azure’s platform ensures these VMs are deployed with optimized VM sizes, NUMA alignment, and storage/network configurations to maximize throughput and minimize latency.

**Use Cases and Application Scenarios**  
- **In-memory Analytics**: Large datasets can be processed in-memory with minimal latency, ideal for real-time analytics platforms such as SAP HANA or Apache Spark.  
- **Large Relational Databases**: Databases like SQL Server, Oracle, and PostgreSQL benefit from the high vCPU and memory capacity for OLTP and OLAP workloads, reducing the need for sharding or complex clustering.  
- **In-memory Cache**: Distributed caching solutions such as Redis or Memcached can leverage these VMs to provide large, fast caches supporting high throughput applications.  
- **Enterprise Applications**: ERP, CRM, and other enterprise-grade applications with heavy compute and memory demands can run efficiently on these VM sizes.

**Important Considerations and Limitations**  
- **Cost**: Larger VM sizes come with higher costs; careful workload sizing and cost management are essential.  
- **NUMA Awareness**: Applications should be NUMA-aware to fully leverage the multi-socket architecture and avoid performance degradation.  
- **Availability**: These VM sizes may have regional availability constraints; verify availability in your target Azure region.  
- **Licensing**: Some software licensing models may require adjustments when scaling to very large VM sizes.  
- **Startup Time**: Larger VMs may have longer provisioning and startup times due to resource allocation.

**Integration with

---


*This report was automatically generated - 2025-08-08 03:01:19 UTC*