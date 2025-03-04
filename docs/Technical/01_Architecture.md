## Architecture

### Overview
AlumiCatalyst is built on a modular, microservices-based architecture leveraging Azure’s robust cloud services. This design enables real-time data ingestion, advanced analytics, blockchain traceability, and a unified dashboard, all while ensuring scalability, resilience, and high performance.

### Key Components
- **IoT & Data Ingestion:**  
  - **Azure IoT Hub:** Captures real-time sensor data from the production environment.
  - **Azure Data Factory:** Preprocesses and transforms raw sensor data.
  - **Azure Data Lake:** Stores both raw and processed data for long-term analytics.

- **Analytics Engine:**  
  - **Azure Machine Learning:** Hosts predictive models to forecast scrap loss and carbon emissions.
  - **Evaluation & Monitoring:** Provides real-time anomaly detection and “what-if” simulation capabilities.

- **Blockchain Traceability:**  
  - **Azure Confidential Ledger:** Implements an immutable ledger for production event logging, ensuring regulatory compliance and transparent carbon credit verification.

- **Application Layer (Dashboard):**  
  - **Frontend (React):** Offers an intuitive, customizable user interface.
  - **Backend (Node.js/Python):** Aggregates data and exposes RESTful APIs for dashboard functionalities.
  
- **Integration & Messaging:**  
  - **Azure API Management:** Facilitates secure API exposure and integration with ERP and legacy systems.
  - **Azure Service Bus:** Supports asynchronous messaging between microservices.

- **Deployment & Orchestration:**  
  - **Azure Kubernetes Service (AKS):** Hosts containerized microservices to ensure scalability.
  - **Azure DevOps:** Provides CI/CD pipelines for continuous integration, testing, and deployment.

### Data Flow & Security
- **Data Flow:**  
  - **Flow:** Sensors → IoT Hub → Data Factory → Data Lake → Machine Learning → Dashboard/API  
  - **Blockchain Integration:** IoT Hub also forwards event data to the Confidential Ledger for secure traceability.
  
- **Security Measures:**  
  - **Encryption:** All data is encrypted both in transit and at rest.
  - **Access Control:** Role-based access is enforced via Azure Active Directory.
  - **Compliance:** Regular security audits and compliance checks are performed.

### Diagram
Refer below to the architecture diagram for a visual representation.
```mermaid
---
config:
  theme: default
  themeVariables:
    primaryColor: '#f9f9f9'
    primaryTextColor: '#333333'
    primaryBorderColor: '#d4a5a5'
    secondaryColor: '#f0fff0'
    secondaryTextColor: '#333333'
    secondaryBorderColor: '#a5d4a5'
    tertiaryColor: '#fef0ff'
    tertiaryTextColor: '#333333'
    tertiaryBorderColor: '#d4a5d4'
  layout: fixed
---
flowchart TD
 subgraph subGraph0["**IoT Layer**"]
        B["Azure IoT Hub"]
        A["IoT Sensors"]
  end
 subgraph subGraph1["**Data Processing**"]
        C["Azure Data Factory"]
        D["Azure Data Lake"]
  end
 subgraph Analytics["**Analytics**"]
        E["Azure Machine Learning"]
        F["Real-time Predictions"]
        G["Azure Confidential Ledger"]
  end
 subgraph Application["**Application**"]
        H["Unified Dashboard"]
        I["Azure API Management"]
  end
 subgraph Integration["**Integration**"]
        J["Azure Service Bus"]
        K["ERP / Legacy Systems"]
  end
 subgraph Deployment["**Deployment**"]
        L["Azure Kubernetes Service AKS"]
        M["Azure DevOps CI/CD"]
  end
    A --> B
    B --> C & G
    C --> D
    D --> E
    E --> F
    F --> H
    H --> I & L
    I --> J & L
    J --> K
    M --> L
     B:::pastel2
     B:::KlimtGold
     A:::pastel1
     A:::KlimtGold
     C:::pastel3
     C:::RenoirPink
     C:::Rose
     D:::pastel4
     D:::Rose
     E:::pastel5
     E:::MonetBlue
     F:::pastel6
     F:::MonetBlue
     G:::pastel7
     G:::MonetBlue
     H:::pastel8
     H:::MatisseLavender
     H:::Peach
     I:::pastel9
     I:::Peach
     J:::pastel10
     J:::Aqua
     K:::pastel11
     K:::Aqua
     L:::pastel12
     L:::DegasGreen
     M:::pastel13
     M:::DegasGreen
    classDef VanGoghYellow stroke-width:1px, stroke-dasharray:none, stroke:#E3B448, fill:#FDF6C9, color:#7D5A17 
    classDef PicassoBlue stroke-width:1px, stroke-dasharray:none, stroke:#5A84A2, fill:#CDE0F2, color:#2D4661  
    classDef Ash stroke-width:1px, stroke-dasharray:none, stroke:#999999, fill:#EEEEEE, color:#000000
    classDef TurnerMist stroke-width:1px, stroke-dasharray:none, stroke:#B8C4D1, fill:#EAF2F8, color:#4A5B6F
    classDef Pine stroke-width:1px, stroke-dasharray:none, stroke:#254336, fill:#27654A, color:#FFFFFF
    classDef HokusaiWave stroke-width:1px, stroke-dasharray:none, stroke:#6188A9, fill:#D4E8F2, color:#2A425D
    classDef Sky stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C
    classDef CezannePeach stroke-width:1px, stroke-dasharray:none, stroke:#E2A07D, fill:#FBE7DA, color:#6D4532
    classDef KlimtGold stroke-width:1px, stroke-dasharray:none, stroke:#D4A017, fill:#FBF2C1, color:#705A16
    classDef MonetBlue stroke-width:1px, stroke-dasharray:none, stroke:#87AFC7, fill:#D4EAF7, color:#30577B
    classDef RenoirPink stroke-width:1px, stroke-dasharray:none, stroke:#E4A0A0, fill:#FBE5E5, color:#7D3E3E
    classDef Rose stroke-width:1px, stroke-dasharray:none, stroke:#FF5978, fill:#FFDFE5, color:#8E2236
    classDef DegasGreen stroke-width:1px, stroke-dasharray:none, stroke:#A7C796, fill:#E6F4E2, color:#3E6A42
    classDef MatisseLavender stroke-width:1px, stroke-dasharray:none, stroke:#B39DBC, fill:#ECE3F5, color:#4E3A5E
    classDef Peach stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D
    classDef Aqua stroke-width:1px, stroke-dasharray:none, stroke:#46EDC8, fill:#DEFFF8, color:#378E7A
    style subGraph0 fill:transparent
    style subGraph1 fill:transparent
    style Analytics fill:transparent
    style Application fill:transparent
    style Deployment fill:transparent
    style Integration fill:transparent
```
