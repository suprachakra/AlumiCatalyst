
# API Documentation

## Overview
This document describes the RESTful API endpoints offered by AlumiCatalyst. All endpoints are secured using OAuth 2.0 and adhere to standardized JSON formats.

## Authentication
- **Endpoint:** `/auth/token`
- **Method:** POST
- **Description:** Accepts client credentials in JSON format and returns a JWT token.
- **Response:** JSON object with the access token and expiration details.

## Endpoints

### Sensor Data Ingestion
- **URL:** `/api/v1/iot/sensors`
- **Method:** POST
- **Request Body:**
```json
{
  "sensorId": "string",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
  "data": {
    "scrapWeight": number,
    "emissionLevel": number
  }
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Data ingested successfully"
}
```

### Predictive Analytics
- **URL:** `/api/v1/analytics/predict`
- **Method:** GET
- **Query Parameters:** `sensorId`, `startDate`, `endDate`
- **Response:**
```json
{
  "sensorId": "string",
  "prediction": {
    "scrapForecast": number,
    "emissionForecast": number
  }
}
```

### Blockchain Traceability
- **URL:** `/api/v1/blockchain/trace`
- **Method:** GET
- **Query Parameters:** `transactionId`
- **Response:**
```json
{
  "transactionId": "string",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",
  "details": "string"
}
```

### Dashboard Metrics
- **URL:** `/api/v1/dashboard/metrics`
- **Method:** GET
- **Response:**
```json
{
  "metrics": {
    "scrapLoss": number,
    "carbonEmission": number,
    "equipmentEfficiency": number
  }
}
```

## Error Handling
- **Standard Error Format:**
```json
{
  "errorCode": "string",
  "message": "string"
}
```

## Versioning and Rate Limiting
- APIs are versioned (e.g., `/api/v1/`).
- Rate limit: 1000 requests per minute per user.
```
