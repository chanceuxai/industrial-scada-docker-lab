# industrial-scada-docker-lab
Containerized Ignition SCADA and MS SQL time-series data pipeline simulating multi-node CIP routing

Project Overview: Industrial Automation Sandbox

Containerized infrastructure running dual Docker services: Ignition Gateway (SCADA) and Microsoft SQL Server.

Successfully established a live JDBC database connection between the Ignition Gateway and MS SQL for time-series logging.

Configured simulated Allen-Bradley PLC nodes (plc1 and plc2) to test and practice Common Industrial Protocol (CIP) multi-hop routing paths.

### Pipeline Verification & Data Flow

#### 1. Container Orchestration & Docker Setup
![Docker Container Stack Verification](assets/dockerIgnitionMSSQL.png)

#### 2.  Gateway Status & OPC UA Device Settings
![Ignition Gateway Device Overview](assets/GatewayIgnition-12e38be856c7.png)

#### 3. Database Connection Configuration
![Ignition Database Connection Setup](assets/databaseConnectionsForIgnition-12e38be856c7.png)

#### 4. Real-Time Perspective Power Chart
![Perspective Power Chart UI](<assets/SCADA-to-SQL Docker Sandbox Proof.png>)

#### 5. MS SQL Server Time-Series Storage (`sqlt_data_1`)
![MS SQL Server DBeaver Query](assets/mssql-tag-history-verification.png)

