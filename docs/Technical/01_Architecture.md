# Architecture

## Overview
AlumiCatalyst is built on a modular, microservices-based architecture leveraging Azure’s robust cloud services. This design enables real-time data ingestion, advanced analytics, blockchain traceability, and a unified dashboard, all while ensuring scalability, resilience, and high performance.

## Key Components
- **IoT Data Acquisition:**  
  - Utilizes Azure IoT Hub to capture real-time sensor data.
  - Preprocessing is handled by Azure Data Factory.
  - Raw and processed data are stored in Azure Data Lake.

- **Analytics Engine:**  
  - Implements Azure Machine Learning for predictive analytics.
  - Provides real-time insights, anomaly detection, and “what‑if” simulation capabilities.

- **Blockchain Module:**  
  - Uses Azure Confidential Ledger to create an immutable log of production events.
  - Supports secure traceability and regulatory reporting for carbon credits.

- **Dashboard and UI:**  
  - Frontend built with React and deployed on Azure App Service.
  - Backend services (Node.js/Python) aggregate data and expose RESTful APIs.

- **Integration Layer:**  
  - Managed via Azure API Management for secure communication with ERP and legacy systems.
  - Employs Azure Service Bus for asynchronous messaging between services.

- **Deployment and Orchestration:**  
  - Containerized microservices orchestrated using Azure Kubernetes Service (AKS).
  - CI/CD pipelines are implemented using Azure DevOps.

## Data Flow & Security
- **Data Flow:**  
  - Sensor → IoT Hub → Data Factory → Data Lake → Machine Learning → Dashboard/API
- **Security Measures:**  
  - Data is encrypted in transit and at rest.
  - Role-based access control is enforced via Azure Active Directory.
  - Regular security audits and compliance checks are conducted.

## Diagram
Refer below to the supplementary architecture diagram for a visual representation.
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
     A:::pastel1
     C:::pastel3
     D:::pastel4
     E:::pastel5
     F:::pastel6
     G:::pastel7
     H:::pastel8
     I:::pastel9
     J:::pastel10
     K:::pastel11
     L:::pastel12
     M:::pastel13
    classDef pastel1 fill:#ffefef,stroke:#d4a5a5,stroke-width:2px
    classDef pastel2 fill:#f0fff0,stroke:#a5d4a5,stroke-width:2px
    classDef pastel3 fill:#fef0ff,stroke:#d4a5d4,stroke-width:2px
    classDef pastel4 fill:#f0f7ff,stroke:#a5b8d4,stroke-width:2px
    classDef pastel5 fill:#fffaf0,stroke:#d4cfa5,stroke-width:2px
    classDef pastel6 fill:#f7fff0,stroke:#a5d4a5,stroke-width:2px
    classDef pastel7 fill:#fffbf0,stroke:#d4cfa5,stroke-width:2px
    classDef pastel8 fill:#f0faff,stroke:#a5d4d4,stroke-width:2px
    classDef pastel9 fill:#f7f0ff,stroke:#d4a5d4,stroke-width:2px
    classDef pastel10 fill:#fff0f0,stroke:#d4a5a5,stroke-width:2px
    classDef pastel11 fill:#f0fff7,stroke:#a5d4a5,stroke-width:2px
    classDef pastel12 fill:#f0fff0,stroke:#a5d4a5,stroke-width:2px
    classDef pastel13 fill:#fff0fa,stroke:#d4a5d4,stroke-width:2px
    style subGraph0 fill:transparent
    style subGraph1 fill:transparent
    style Analytics fill:transparent
    style Application fill:transparent
    style Deployment fill:transparent
    style Integration fill:transparent
```
