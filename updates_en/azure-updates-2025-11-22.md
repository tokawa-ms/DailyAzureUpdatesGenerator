# November 22, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 22, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Custom handler support in Azure Functions Flex consumption 

**Published**: November 21, 2025 19:15:38 UTC
**Link**: [Generally Available: Custom handler support in Azure Functions Flex consumption ](https://azure.microsoft.com/updates?id=512413)

**Update ID**: 512413
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features

**Summary**:

- What was updated  
Azure Functions Flex Consumption plan now generally supports custom handlers.

- Key changes or new features  
Custom handlers enable developers to run Functions written in any language that supports HTTP primitives by implementing lightweight web servers. This expands language flexibility beyond the built-in runtime languages. The Functions host communicates with these custom handlers via HTTP, allowing seamless event processing. This feature is now fully available in the Flex Consumption hosting model, which provides dynamic scaling and cost efficiency.

- Target audience affected  
Developers seeking to build Azure Functions in languages not natively supported by Azure Functions runtime, and IT professionals managing serverless workloads requiring flexible language support and scalable consumption plans.

- Important notes if any  
Custom handlers must implement HTTP endpoints to interact with the Functions host. This update enhances the flexibility of serverless architectures on Azure by allowing more diverse language ecosystems in a cost-effective, scalable environment. Developers should ensure their custom handlers handle HTTP communication correctly to integrate smoothly with the Functions runtime.

**Details**:

The recent Azure update announces the general availability of custom handler support in Azure Functions Flex Consumption plan, enabling developers to implement serverless functions using any programming language that can handle HTTP requests. This enhancement expands the flexibility and language support of Azure Functions beyond the built-in runtime languages by allowing lightweight web servers, known as custom handlers, to receive and process events from the Functions host.

**Background and Purpose:**  
Azure Functions traditionally supports several languages such as C#, JavaScript, Python, and PowerShell through its built-in runtime. However, this limits developers who want to use other languages or frameworks that are not natively supported. Custom handlers were introduced to address this gap by allowing developers to write functions in any language or runtime that can expose an HTTP endpoint. Previously, custom handler support was available only in the Consumption and Premium plans but was limited or in preview for the Flex Consumption plan. The Flex Consumption plan offers enhanced scaling and resource isolation compared to the standard Consumption plan, making it suitable for more demanding or enterprise-grade workloads. This update brings custom handler support to Flex Consumption in GA, broadening the scenarios where developers can leverage flexible language choices with the benefits of the Flex Consumption hosting model.

**Specific Features and Detailed Changes:**  
- Full general availability of custom handler support in the Azure Functions Flex Consumption plan.  
- Enables deployment of custom handlers as lightweight HTTP servers that communicate with the Functions host via HTTP protocol.  
- Supports any language or framework capable of HTTP communication, including but not limited to Rust, Go, C++, or custom frameworks.  
- Maintains the event-driven programming model of Azure Functions while decoupling the runtime from language constraints.  
- Provides seamless integration with Azure Functions triggers and bindings, enabling event sources like HTTP requests, timers, queues, and more to invoke custom handlers.  
- Supports scaling and lifecycle management consistent with Flex Consumption plan capabilities.

**Technical Mechanisms and Implementation Methods:**  
Custom handlers operate by running a lightweight web server that listens on a specified port and communicates with the Azure Functions host via HTTP. The Functions host acts as a proxy, forwarding incoming events to the custom handler endpoint and receiving responses to return to the caller or trigger subsequent bindings. Developers define a `host.json` configuration file specifying the custom handler’s executable path and port, along with function metadata in `function.json` files. The custom handler must implement the HTTP protocol contract expected by the Functions host, including handling function invocation requests and returning appropriate HTTP responses. Deployment involves packaging the custom handler executable alongside function metadata and deploying to the Flex Consumption environment, which manages scaling based on event load.

**Use Cases and Application Scenarios:**  
- Implementing serverless functions in languages not natively supported by Azure Functions, such as Rust, Go, or C++.  
- Migrating existing HTTP-based microservices or lightweight APIs into a serverless architecture without rewriting code in supported languages.  
- Building high-performance or specialized compute functions that benefit from custom runtimes or frameworks.  
- Integrating legacy systems or proprietary protocols by wrapping them in HTTP-based custom handlers.  
- Leveraging Flex Consumption’s enhanced scaling and isolation for production workloads requiring custom language support.

**Important Considerations and Limitations:**  
- Custom handlers must adhere strictly to the HTTP protocol contract defined by Azure Functions to ensure proper invocation and response handling.  
- Debugging and monitoring may require additional setup compared to built-in runtimes, as telemetry and logs from the custom handler process need to be integrated with Azure Monitor or Application Insights.  
- Cold start times may vary depending on the custom handler’s startup time and resource requirements.  
- Some advanced Azure Functions features or bindings may have limited or no support depending on the custom handler implementation.  
- Security considerations include ensuring the custom handler properly validates and sanitizes incoming requests and handles authentication if required.

**Integration with Related Azure Services:**  
- Custom handlers in Flex Consumption seamlessly integrate with Azure Event Grid, Azure Storage Queues, Service Bus, and other trigger sources supported by

---

### 2. Retirement: Migrate to dedicated VM for your compute clusters

**Published**: November 21, 2025 18:45:18 UTC
**Link**: [Retirement: Migrate to dedicated VM for your compute clusters](https://azure.microsoft.com/updates?id=501658)

**Update ID**: 501658
**Data source**: Azure Updates API

**Categories**: AI + machine learning, Internet of Things, Azure Machine Learning, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of Low-Priority VMs for compute clusters, with end of life on September 30, 2025. Support within Azure Machine Learning will continue until March 31, 2026.

- Key changes or new features  
Users must migrate their compute clusters from Low-Priority VMs to dedicated VMs to avoid automatic scale-downs and ensure stable cluster performance. Dedicated VMs provide guaranteed capacity and reliability compared to Low-Priority VMs, which are subject to eviction.

- Target audience affected  
Developers and IT professionals managing Azure Machine Learning compute clusters that currently utilize Low-Priority VMs.

- Important notes if any  
Migration should be planned ahead of the September 2025 deadline to prevent disruptions. Although support continues until March 2026, running clusters on Low-Priority VMs post-retirement may lead to unexpected scaling behavior. Transitioning to dedicated VMs ensures consistent compute availability and better workload stability.  
For detailed migration guidance, refer to the official Azure update link.

**Details**:

The Azure update titled "Retirement: Migrate to dedicated VM for your compute clusters" announces the end-of-life (EOL) for Low-Priority Virtual Machines (VMs) on September 30, 2025, with continued support on Azure Machine Learning until March 31, 2026. This update advises users to migrate their compute clusters to dedicated VMs to avoid automatic scale-down and ensure uninterrupted operation.

**Background and Purpose of the Update**  
Low-Priority VMs have been a cost-effective option for running batch and non-critical workloads by utilizing surplus capacity at discounted rates. However, due to evolving infrastructure strategies and the need for more reliable and predictable compute resources, Microsoft is retiring Low-Priority VMs. The update’s purpose is to guide users toward dedicated VM instances, which provide guaranteed availability and stability for compute clusters, especially in Azure Machine Learning environments.

**Specific Features and Detailed Changes**  
- **End of Life Date:** Low-Priority VMs will no longer be available after September 30, 2025.  
- **Support Extension:** Azure Machine Learning will continue to support existing Low-Priority VM clusters until March 31, 2026, allowing a transition period.  
- **Migration Recommendation:** Users are encouraged to migrate their compute clusters to dedicated VMs to prevent automatic scale-down events that occur when Low-Priority VMs are preempted or reclaimed.  
- **Impact on Auto-scaling:** Dedicated VMs provide stable capacity, eliminating the unpredictability of Low-Priority VM preemption, thus improving cluster reliability and performance.

**Technical Mechanisms and Implementation Methods**  
- **Migration Process:** Users should identify compute clusters currently using Low-Priority VMs and reconfigure these clusters to use dedicated VM SKUs. This typically involves updating the cluster configuration in Azure Machine Learning or other compute management tools to specify dedicated VM types.  
- **Cluster Configuration:** In Azure Machine Learning, this can be done by modifying the compute target’s VM priority setting from ‘low-priority’ to ‘dedicated’.  
- **Scaling Behavior:** Dedicated VMs maintain consistent availability, so auto-scaling policies can be optimized without accounting for preemption risks.  
- **Resource Allocation:** Dedicated VMs guarantee resource allocation, which improves job scheduling and reduces failures caused by VM eviction.

**Use Cases and Application Scenarios**  
- **Machine Learning Training:** Workloads requiring consistent compute power, such as large-scale model training and hyperparameter tuning, benefit from dedicated VMs to avoid interruptions.  
- **Batch Processing:** Jobs that cannot tolerate preemption or require guaranteed runtime should migrate to dedicated VMs.  
- **Production Workloads:** Any production-grade AI or data processing pipelines that demand high availability and reliability should transition away from Low-Priority VMs.  
- **Development and Testing:** While Low-Priority VMs were suitable for cost-sensitive dev/test environments, dedicated VMs now offer a more stable alternative.

**Important Considerations and Limitations**  
- **Cost Implications:** Dedicated VMs are generally more expensive than Low-Priority VMs due to guaranteed availability; budget adjustments may be necessary.  
- **Preemption Risk:** Low-Priority VMs are subject to eviction when Azure requires capacity; migrating eliminates this risk but at a higher cost.  
- **Migration Timeline:** Users should plan migration well before the September 2025 deadline to avoid service disruption.  
- **Compatibility:** Ensure that all cluster configurations and dependent services support dedicated VM SKUs.  
- **Scaling Policies:** Review and adjust auto-scaling rules to leverage the stability of dedicated VMs.

**Integration with Related Azure Services**  
- **Azure Machine Learning:** The primary service affected, where compute clusters must be reconfigured to use dedicated VMs for training and inference workloads.  
- **Azure Batch:** Users employing Low-Priority VMs for batch jobs should consider dedicated VM pools or alternative cost-saving mechanisms such as spot VMs with eviction policies.

---


*This report was automatically generated - 2025-11-22 03:01:49 UTC*