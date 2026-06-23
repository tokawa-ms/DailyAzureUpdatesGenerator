# June 23, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 23, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Retirement: Azure VMware Solution AV36 Node Retirement now on September 30, 2027

**Published**: June 22, 2026 16:30:01 UTC
**Link**: [Retirement: Azure VMware Solution AV36 Node Retirement now on September 30, 2027](https://azure.microsoft.com/updates?id=503883)

**Update ID**: 503883
**Data source**: Azure Updates API

**Categories**: Compute, Azure VMware Solution, Retirements

**Summary**:

- What was updated  
The retirement date for the Azure VMware Solution (AVS) AV36 node type has been changed. The AV36 node will now be retired on September 30, 2027, instead of the previously announced June 30, 2028.

- Key changes or new features  
The end-of-support date for the AV36 node is now aligned with VMware’s roadmap and Broadcom’s support timeline for vSphere 8. After September 30, 2027, the AV36 SKU will not be compatible with supported VMware software versions.

- Target audience affected  
This update impacts IT professionals and cloud architects managing Azure VMware Solution environments, particularly those using or planning to use the AV36 node type. Developers who rely on AVS infrastructure for application hosting may also be affected.

- Important notes if any  
Customers using AV36 nodes must plan to migrate workloads to supported node types before September 30, 2027, to ensure continued support and compatibility. Early planning is recommended to avoid service disruptions. Review your AVS deployments and coordinate with Microsoft and VMware support teams as needed for migration guidance.

[More details](https://azure.microsoft.com/updates?id=503883)

**Details**:

**Azure Update Report: Retirement of Azure VMware Solution AV36 Node (Effective September 30, 2027)**

**Background and Purpose of the Update**  
Microsoft has announced a revised retirement date for the AV36 node type in Azure VMware Solution (AVS). Originally scheduled for June 30, 2028, the retirement date is now September 30, 2027. This change aligns with VMware’s roadmap, specifically Broadcom’s end-of-support for the AV36 version with vSphere 8. The update ensures that Azure VMware Solution remains compatible with supported VMware software versions and maintains alignment with upstream vendor support policies.

**Specific Features and Detailed Changes**  
- **AV36 Node Retirement:** The AV36 node SKU will no longer be available for deployment or support after September 30, 2027.
- **Compatibility:** The AV36 SKU is not compatible with future versions of vSphere beyond vSphere 8, as Broadcom will cease support for this hardware platform.
- **Transition Timeline:** Customers must plan migration or decommissioning of AV36 nodes before the retirement date to avoid unsupported configurations.

**Technical Mechanisms and Implementation Methods**  
- **Lifecycle Management:** Azure will enforce retirement by disabling provisioning of AV36 nodes post-September 30, 2027. Existing AV36 nodes will be subject to decommissioning, and customers will need to migrate workloads to supported node types.
- **VMware Version Alignment:** The retirement is triggered by Broadcom’s end-of-support for AV36 with vSphere 8, ensuring that Azure VMware Solution only offers hardware platforms compatible with supported VMware software.
- **Migration Path:** Customers are expected to utilize Azure VMware Solution migration tools and documentation to transition workloads to newer node types (e.g., AV36P, AV52, or other supported SKUs).

**Use Cases and Application Scenarios**  
- **Current AV36 Deployments:** Organizations running production workloads on AV36 nodes must plan for migration to supported node types before September 30, 2027.
- **VMware Upgrades:** Customers intending to upgrade to vSphere versions beyond 8 will need to ensure their node hardware is compatible, as AV36 will not be supported.
- **Capacity Planning:** IT teams should review their AVS cluster configurations and adjust their resource planning to accommodate the retirement and migration requirements.

**Important Considerations and Limitations**  
- **End-of-Support Risk:** Continuing to use AV36 nodes after the retirement date may expose organizations to unsupported configurations, security vulnerabilities, and compliance risks.
- **Migration Complexity:** Transitioning workloads may require downtime, reconfiguration, and validation to ensure compatibility with new node types.
- **SKU Availability:** Customers must verify the availability of alternative node SKUs in their Azure regions and confirm compatibility with their workload requirements.

**Integration with Related Azure Services**  
- **Azure VMware Solution:** The update directly impacts AVS, requiring integration with Azure migration tools and services for workload transition.
- **Azure Resource Manager:** Resource management and automation scripts must be updated to exclude AV36 node provisioning post-retirement.
- **Monitoring and Alerts:** IT teams should configure Azure Monitor and related alerting mechanisms to track AV36 usage and retirement timelines.

**Summary Sentence**  
Microsoft has revised the retirement date for Azure VMware Solution AV36 nodes to September 30, 2027, aligning with VMware’s roadmap and Broadcom’s end-of-support for vSphere 8, requiring customers to migrate workloads to supported node types before this deadline to maintain compatibility and support.

---


*This report was automatically generated - 2026-06-23 03:01:07 UTC*