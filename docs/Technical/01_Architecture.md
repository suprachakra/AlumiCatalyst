## Architecture and Engineering Overview

AlumiCatalyst is a modular, microservices-based digital transformation platform for aluminum manufacturing built on Microsoft Azure. It is designed to capture real-time sensor data, perform advanced analytics, enforce blockchain-based traceability, and deliver a unified, customizable dashboard—all while ensuring high scalability, robust security, and continuous operational excellence.

This document outlines the complete architecture, technical stack, core modules, data flows, and security parameters. It also details how the system components interconnect and are orchestrated for enterprise-grade performance.

---

### 1. System Architecture Overview

#### Core Components & Modules

1. **IoT & Data Ingestion**
   - **Azure IoT Hub:**  
     - Captures real-time data from deployed IoT sensors on the production floor.
     - Ensures secure communication between sensors and cloud.
   - **Azure Data Factory:**  
     - Transforms and preprocesses raw sensor data.
     - Supports both real-time and batch processing from legacy systems.
   - **Azure Data Lake:**  
     - Central repository for storing raw and processed data.
     - Enables large-scale data storage and analytics.

2. **Analytics Engine**
   - **Azure Machine Learning:**  
     - Hosts predictive models for forecasting scrap loss and carbon emissions.
     - Supports continuous retraining and model refinement based on live data.
   - **Analytics Services:**  
     - Anomaly detection, “what‑if” simulation, and performance evaluation.
   - **Azure Synapse Analytics & Power BI:**  
     - Provide advanced data visualization and interactive reporting.

3. **Blockchain Traceability**
   - **Azure Confidential Ledger:**  
     - Implements an immutable ledger for recording production events.
     - Provides transparent and verifiable data for regulatory compliance and carbon credit reporting.
   - **Smart Contracts:**  
     - Execute predefined rules for event logging and automated reporting.

4. **Application Layer (Dashboard & UI)**
   - **Frontend (React):**  
     - Delivers a responsive, interactive, and customizable user interface.
     - Designed for real-time display of KPIs, alerts, and data visualizations.
   - **Backend (Node.js/Python):**  
     - Aggregates data from multiple modules.
     - Provides RESTful APIs for dashboard operations and user management.

5. **Integration & Messaging**
   - **Azure API Management:**  
     - Exposes secure, versioned APIs for integration with ERP and legacy systems.
   - **Azure Service Bus:**  
     - Facilitates asynchronous communication and message queuing between microservices.
   - **Data Connectors:**  
     - Enable seamless data synchronization with external systems.

6. **Deployment & DevOps**
   - **Azure Kubernetes Service (AKS):**  
     - Hosts containerized microservices for scalable and resilient deployment.
   - **Azure DevOps CI/CD:**  
     - Automates build, test, and deployment processes using pipelines and Helm charts.
   - **Monitoring & Logging:**  
     - Utilizes Azure Monitor and Application Insights for real-time performance tracking and alerting.

---

### 2. Technical Stack

| **Category**              | **Components**                                                                                          |
|---------------------------|---------------------------------------------------------------------------------------------------------|
| **Cloud Platform**        | Microsoft Azure                                                                                         |
| **Compute & Orchestration** | Azure Kubernetes Service (AKS)<br>Azure Functions for serverless processing                              |
| **Data Services**         | Azure IoT Hub<br>Azure Data Factory<br>Azure Data Lake<br>Azure SQL Database                              |
| **Analytics & AI**        | Azure Machine Learning<br>Azure Synapse Analytics<br>Power BI for visualization                         |
| **Blockchain**            | Azure Confidential Ledger                                                                               |
| **Security**              | Azure Active Directory (RBAC)<br>Azure Key Vault                                                        |
| **Integration**           | Azure API Management<br>Azure Service Bus                                                               |
| **DevOps**                | Azure DevOps CI/CD pipelines<br>Helm charts for deployment management                                   |

---

### 3. Data Flow & Security

### Data Flow Process
- **Primary Flow:**  
  1. **Sensors → Azure IoT Hub:** Real-time sensor data is captured.
  2. **IoT Hub → Azure Data Factory:** Data is preprocessed and transformed.
  3. **Data Factory → Azure Data Lake:** Data is stored for long-term analysis.
  4. **Data Lake → Azure Machine Learning:** Data is used to generate predictive insights.
  5. **Azure ML → Dashboard/API:** Predictions and analytics are served to the user interface.
- **Blockchain Integration:**  
  - In parallel, IoT Hub forwards production events to the Azure Confidential Ledger for immutable logging.

#### Security Measures
- **Encryption:** Data is encrypted in transit (TLS) and at rest.
- **Access Control:** Role-based access using Azure Active Directory.
- **Compliance:** Regular security audits and continuous compliance monitoring.
- **Logging & Monitoring:** Azure Monitor and Application Insights provide end-to-end logging and performance tracking.

---

### 4. Detailed Mermaid Diagram

Below is the detailed Mermaid diagram for the overall system architecture:

```mermaid
flowchart TD
 subgraph subGraph0["IoT & Data Ingestion"]
        B["Azure IoT Hub"]
        A["IoT Sensors"]
        C["Azure Data Factory"]
        D["Azure Data Lake"]
  end
 subgraph subGraph1["Analytics Engine"]
        E["Azure Machine Learning"]
        F["Predictive Models & Evaluations"]
        G["Anomaly Detection & Simulations"]
  end
 subgraph subGraph2["Blockchain Traceability"]
        H["Azure Confidential Ledger"]
        I["Smart Contract Execution"]
  end
 subgraph subGraph3["Application Layer"]
        J["Unified Dashboard Frontend"]
        K["Dashboard Backend APIs"]
        L["User Management"]
  end
 subgraph subGraph4["Integration & Messaging"]
        M["Azure API Management"]
        N["Azure Service Bus"]
        O["ERP / Legacy Systems"]
  end
 subgraph subGraph5["Deployment & DevOps"]
        P["Azure Kubernetes Service AKS"]
        Q["Azure DevOps CI/CD"]
  end
    A --> B
    B --> C & H
    C --> D
    D --> E
    E --> F & G
    H --> I
    F --> J
    J --> K & P
    K --> L & M
    M --> N & P
    N --> O
    Q --> P

     B:::pastel2
     B:::Peach
     A:::pastel1
     A:::pastel12
     A:::Peach
     C:::pastel3
     C:::Peach
     D:::pastel4
     D:::Peach
     E:::pastel5
     F:::pastel6
     F:::VanGoghYellow
     G:::pastel6
     G:::VanGoghYellow
     H:::pastel7
     H:::Aqua
     I:::pastel7
     I:::Aqua
     J:::pastel8
     J:::PicassoBlue
     J:::MonetBlue
     K:::pastel8
     K:::HokusaiWave
     L:::pastel8
     L:::MonetBlue
     M:::pastel9
     M:::Rose
     N:::pastel10
     N:::RenoirPink
     O:::pastel10
     O:::RenoirPink
     P:::pastel11
     Q:::pastel12
     Q:::DegasGreen
    classDef pastel1 fill:#fff5f5,stroke:#ffcccc,stroke-width:2px
    classDef pastel2 fill:#f5fff5,stroke:#ccffcc,stroke-width:2px
    classDef pastel3 fill:#fff5ff,stroke:#ffccff,stroke-width:2px
    classDef pastel4 fill:#f5f7ff,stroke:#cce0ff,stroke-width:2px
    classDef pastel5 fill:#fffaf0,stroke:#ffe5b4,stroke-width:2px
    classDef pastel6 fill:#e6ffed,stroke:#a5d4a5,stroke-width:2px
    classDef pastel7 fill:#fffbf0,stroke:#ffe5b4,stroke-width:2px
    classDef pastel8 fill:#f0faff,stroke:#a5d4d4,stroke-width:2px
    classDef pastel9 fill:#f7f0ff,stroke:#ffcccc,stroke-width:2px
    classDef pastel10 fill:#fff0f0,stroke:#ffcccc,stroke-width:2px
    classDef Ash stroke-width:1px, stroke-dasharray:none, stroke:#999999, fill:#EEEEEE, color:#000000
    classDef MatisseLavender stroke-width:1px, stroke-dasharray:none, stroke:#B39DBC, fill:#ECE3F5, color:#4E3A5E
    classDef Pine stroke-width:1px, stroke-dasharray:none, stroke:#254336, fill:#27654A, color:#FFFFFF
    classDef Sky stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C
    classDef CezannePeach stroke-width:1px, stroke-dasharray:none, stroke:#E2A07D, fill:#FBE7DA, color:#6D4532
    classDef KlimtGold stroke-width:1px, stroke-dasharray:none, stroke:#D4A017, fill:#FBF2C1, color:#705A16
    classDef VanGoghYellow stroke-width:1px, stroke-dasharray:none, stroke:#E3B448, fill:#FDF6C9, color:#7D5A17
    classDef PicassoBlue stroke-width:1px, stroke-dasharray:none, stroke:#5A84A2, fill:#CDE0F2, color:#2D4661
    classDef HokusaiWave stroke-width:1px, stroke-dasharray:none, stroke:#6188A9, fill:#D4E8F2, color:#2A425D
    classDef TurnerMist stroke-width:1px, stroke-dasharray:none, stroke:#B8C4D1, fill:#EAF2F8, color:#4A5B6F
    classDef MonetBlue stroke-width:1px, stroke-dasharray:none, stroke:#87AFC7, fill:#D4EAF7, color:#30577B
    classDef Rose stroke-width:1px, stroke-dasharray:none, stroke:#FF5978, fill:#FFDFE5, color:#8E2236
    classDef RenoirPink stroke-width:1px, stroke-dasharray:none, stroke:#E4A0A0, fill:#FBE5E5, color:#7D3E3E
    classDef DegasGreen stroke-width:1px, stroke-dasharray:none, stroke:#A7C796, fill:#E6F4E2, color:#3E6A42
    classDef pastel11 fill:#f0fff0, stroke:#a5d4a5, stroke-width:2px
    classDef Aqua stroke-width:1px, stroke-dasharray:none, stroke:#46EDC8, fill:#DEFFF8, color:#378E7A
    classDef pastel12 fill:#fff0fa, stroke:#ffccff, stroke-width:2px
    classDef Peach stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D
    style subGraph3 fill:transparent
    style subGraph5 fill:transparent
    style subGraph4 fill:transparent
    style subGraph1 fill:transparent
    style subGraph2 fill:transparent
    style subGraph0 fill:transparent
```
