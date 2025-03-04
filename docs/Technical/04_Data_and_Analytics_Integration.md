## Data and Analytics Integration

### Overview
AlumiCatalyst leverages a robust data integration pipeline to capture, process, and analyze real-time and batch data from production systems. This document outlines the end‑to‑end data flow, the transformation processes, and the integration with business intelligence tools to provide actionable insights.

### Data Sources
- **IoT Sensors:**  
  Real‑time data ingestion via Azure IoT Hub.
- **Legacy Systems:**  
  Batch imports from ERP, SCADA, and other existing databases.

### Data Pipeline Architecture(check the diagram below)
1. **Ingestion:**  
   - **Azure IoT Hub:** Captures real-time sensor data.
   - **Batch Imports:** Scheduled extraction from legacy systems using Azure Data Factory.
2. **Transformation:**  
   - **Azure Data Factory:** Processes raw data, cleanses it, and transforms it into structured formats.
   - **Data Preprocessing:** Applies cleaning rules, normalization, and aggregation (detailed in preprocessing modules).
3. **Storage:**  
   - **Azure Data Lake:** Central repository for raw and processed data.
   - **Azure SQL Database:** Stores structured data for immediate querying and reporting.
4. **Analytics:**  
   - **Azure Machine Learning:** Processes data to generate predictive insights and anomaly detection.
   - **Azure Synapse Analytics & Power BI:** Enable advanced reporting and visualization.

### Data Governance and Security
- **Data Dictionary & Schema:**  
  Maintain version-controlled definitions for all data elements.
- **Quality Assurance:**  
  ETL pipelines enforce schema consistency and perform data quality checks.
- **Access Control:**  
  Role-based access using Azure Active Directory.
- **Encryption:**  
  All data is encrypted in transit and at rest.

### Integration with BI Tools
- **Real-time Dashboards:**  
  Data is exposed to Power BI and custom dashboards for live monitoring.
- **APIs:**  
  RESTful endpoints provide data access for external systems and analytics.

### Best Practices
- Regular audits of ETL pipelines.
- Automated monitoring using Azure Monitor and Data Factory alerts.
- Periodic reviews of data governance policies.

```mermaid
flowchart TD
 subgraph subGraph0["Data Sources"]
        DS1["IoT Sensors"]
        DS2["Legacy ERP Data"]
  end
 subgraph subGraph1["Ingestion & Transformation"]
        A1["Azure IoT Hub"]
        A2["Azure Data Factory"]
  end
 subgraph Storage["Storage"]
        S1["Azure Data Lake"]
        S2["Azure SQL Database"]
  end
 subgraph Analytics["Analytics"]
        AN1["Azure Machine Learning"]
        AN2["Model Training & Prediction"]
        AN3["Anomaly Detection & Simulations"]
  end
 subgraph Visualization["Visualization"]
        V1["Power BI / Custom Dashboard"]
  end
    DS1 --> A1
    DS2 --> A2
    A1 --> A2
    A2 --> S1 & S2
    S1 --> AN1
    S2 --> AN1
    AN1 --> AN2 & AN3
    AN2 --> V1
    AN3 --> V1

     DS1:::MonetBlue
     DS2:::MonetBlue
     A1:::VanGoghYellow
     A1:::KlimtGold
     A2:::KlimtGold
     S1:::Rose
     S2:::Rose
     AN1:::DegasGreen
     AN2:::DegasGreen
     AN3:::DegasGreen
     V1:::DegasGreen
     V1:::Aqua
    classDef RenoirPink stroke-width:1px, stroke-dasharray:none, stroke:#E4A0A0, fill:#FBE5E5, color:#7D3E3E  
    classDef PicassoBlue stroke-width:1px, stroke-dasharray:none, stroke:#5A84A2, fill:#CDE0F2, color:#2D4661  
    classDef Ash stroke-width:1px, stroke-dasharray:none, stroke:#999999, fill:#EEEEEE, color:#000000
    classDef TurnerMist stroke-width:1px, stroke-dasharray:none, stroke:#B8C4D1, fill:#EAF2F8, color:#4A5B6F
    classDef MatisseLavender stroke-width:1px, stroke-dasharray:none, stroke:#B39DBC, fill:#ECE3F5, color:#4E3A5E
    classDef Pine stroke-width:1px, stroke-dasharray:none, stroke:#254336, fill:#27654A, color:#FFFFFF
    classDef HokusaiWave stroke-width:1px, stroke-dasharray:none, stroke:#6188A9, fill:#D4E8F2, color:#2A425D
    classDef Sky stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C
    classDef CezannePeach stroke-width:1px, stroke-dasharray:none, stroke:#E2A07D, fill:#FBE7DA, color:#6D4532
    classDef Peach stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D
    classDef MonetBlue stroke-width:1px, stroke-dasharray:none, stroke:#87AFC7, fill:#D4EAF7, color:#30577B
    classDef VanGoghYellow stroke-width:1px, stroke-dasharray:none, stroke:#E3B448, fill:#FDF6C9, color:#7D5A17
    classDef KlimtGold stroke-width:1px, stroke-dasharray:none, stroke:#D4A017, fill:#FBF2C1, color:#705A16
    classDef Rose stroke-width:1px, stroke-dasharray:none, stroke:#FF5978, fill:#FFDFE5, color:#8E2236
    classDef DegasGreen stroke-width:1px, stroke-dasharray:none, stroke:#A7C796, fill:#E6F4E2, color:#3E6A42
    classDef Aqua stroke-width:1px, stroke-dasharray:none, stroke:#46EDC8, fill:#DEFFF8, color:#378E7A
    style subGraph0 fill:transparent
    style subGraph1 fill:transparent
    style Storage fill:transparent
    style Analytics fill:transparent
    style Visualization fill:transparent

```
