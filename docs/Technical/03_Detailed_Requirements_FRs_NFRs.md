# Detailed Requirements – Functional and Non‑Functional

## Functional Requirements (FRs)

| FR ID  | Requirement                                                      | Acceptance Criteria                                            | Risks & Fallbacks                                            | Cross-Dept Checks         | Priority |
|--------|------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------|---------------------------|----------|
| FR-001 | Ingest real‑time sensor data from production lines.             | Data latency < 5 seconds; 99% accuracy.                        | Revert to batch processing if real‑time ingestion fails.     | Operations, Engineering   | High     |
| FR-002 | Forecast scrap loss and carbon emissions using AI models.        | Predictive accuracy ≥85% over a 30‑day period.                 | Revert to rule‑based alerts if model performance degrades.    | Data, Engineering, QA     | High     |
| FR-003 | Record all production events on a blockchain ledger.             | 100% immutable audit traceability.                           | Activate conventional logging if blockchain connectivity fails.| Compliance, IT, Engineering | Medium   |
| FR-004 | Provide a role‑based, customizable dashboard for end‑users.       | Dashboard loads in <2 seconds; supports user customization.    | Default dashboard settings applied if customization fails.   | IT, Design, Operations    | High     |
| FR-005 | Generate automated alerts for anomalies and incidents.           | Alerts trigger within 30 seconds of detection.                | Manual monitoring activated if automated alerts fail.        | Operations, QA, IT        | Medium   |
| FR-006 | Seamlessly integrate with external ERP systems via secure APIs.   | API response <200 ms; 99% success rate in data synchronization. | Use fallback batch imports if API integration fails.         | IT, Engineering, Finance  | High     |

## Non‑Functional Requirements (NFRs)

| NFR ID | Requirement                                                     | Metric                                          | Risks & Fallbacks                                              | Dept Checks              | Priority |
|--------|-----------------------------------------------------------------|-------------------------------------------------|----------------------------------------------------------------|--------------------------|----------|
| NFR-001| System uptime must be maintained at 99.99%.                     | Monitored via Azure Monitor.                    | Deploy redundant clusters and failover mechanisms.             | IT, DevOps, Engineering  | High     |
| NFR-002| API response times must be under 200 ms for 95% of calls.       | Measured via load testing.                      | Optimize code and implement caching strategies if needed.      | Engineering, QA          | High     |
| NFR-003| Ensure all sensitive data is encrypted in transit and at rest.  | Verified via periodic security audits.          | Introduce additional encryption measures if vulnerabilities arise.| IT, Security, Compliance | High     |
| NFR-004| System scalability to support up to 500 sensors.                | Maintain latency <5 seconds under peak load.    | Implement horizontal scaling using Azure AKS and load balancers. | Engineering, DevOps      | High     |
| NFR-005| Maintain code maintainability with at least 90% test coverage.    | Automated test coverage reports.                | Increase automated tests and enforce rigorous code reviews.     | QA, Engineering          | Medium   |
