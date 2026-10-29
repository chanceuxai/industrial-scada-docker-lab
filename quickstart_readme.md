# Industrial SCADA Docker Lab

A containerized sandbox environment running Ignition SCADA, MS SQL Server, and local process simulators via Docker Compose.

---

## Architecture & Services

This repository uses a single `docker-compose.yaml` file to orchestrate two core containers on an isolated internal network:
1. **Ignition Gateway (`ignition`):** Handles the SCADA HMI, tag provider, and project logic, exposed locally on port `8088`.
2. **MS SQL Server (`mssql`):** Acts as the time-series historian and relational database backend, exposed locally on port `1433`.

---

## Prerequisites
* [Docker Desktop](https://www.docker.com/) installed and running.

---

## Quickstart

### Step 1: Clone the repository and set up environment variables
```bash
git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>
cp .env.example .env
```

### Step 2: Launch the container stack
Run the following command in the root directory where your docker-compose.yaml lives:
```bash
docker compose up -d
```
Docker will automatically read the compose file, pull the container images, create the internal bridge network, and start both the MS SQL Server and Ignition Gateway in the background.

### Step 3: Access Services
Use these addresses for each service.
* **Ignition Gateway UI:** `http://localhost:8088`
* **MS SQL Server:** `localhost:1433`

### Step 4: Stop the stack
When you are done working and want to shut down the containers cleanly, run:
```bash
docker compose down
```
(Note: Your data and database volumes will remain safely preserved locally).