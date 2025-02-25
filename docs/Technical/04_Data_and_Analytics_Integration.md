# Data and Analytics Integration

## Data Sources
- **IoT Sensors:**  
  - Real-time sensor data is ingested via Azure IoT Hub.
- **Legacy Systems:**  
  - Batch imports from ERP and other existing systems.

## Data Pipeline Architecture
- **Ingestion:**  
  - Azure IoT Hub collects sensor data and transmits it to Azure Data Lake.
- **Transformation:**  
  - Azure Data Factory processes raw data into structured formats.
- **Analytics:**  
  - Azure Machine Learning analyzes data to produce predictive insights.
- **Storage:**  
  - Processed data is stored in both Azure Data Lake and Azure SQL Database.

## Data Models and Governance
- A version-controlled data dictionary is maintained.
- ETL pipelines enforce schema consistency and data quality.
- Role-based access controls and encryption are applied across all data stores.

## Integration with BI Tools
- Azure Synapse Analytics and Power BI deliver real-time dashboards.
- RESTful APIs expose data for consumption by external analytics tools.
