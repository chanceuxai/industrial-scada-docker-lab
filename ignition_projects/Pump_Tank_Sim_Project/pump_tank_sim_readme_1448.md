# Pump & Tank Process Simulator

An asynchronous Python OPC-UA server that models a closed-loop liquid tank system with automated control, manual overrides, and low-level safety interlocks.

## Overview

This script (`pump_tank_sim.py`) uses `asyncua` to run a local OPC-UA server, allowing Ignition SCADA (or other OPC-UA clients) to read and write live process tags.

### Operational Modes (`System_Mode`)

* **AUTO:** Automated differential control. The inlet valve opens below 50.0% level and closes above 70.0%. The pump turns on above 70.0% and turns off below 50.0%.
* **MANUAL:** Bypasses auto-logic and allows direct HMI toggling of valves and pumps.
* **STOP:** Freezes process physics and disables all actuator commands. If the system is stopped while the level is between 50.0% and 70.0%, it will not automatically resume and requires a manual start.
* **Low-Level Interlock:** If the tank level drops <= 5.0%, the system automatically forces a trip to STOP to prevent dry pump operation.
* **High-Level Alarm:** If the tank level reaches 100.0%, the tank display turns red to visually indicate an overflow condition.

---

## Ignition Setup & Restoration

You can restore the project into your running Ignition Gateway using either the full gateway backup or the project zip file:

### Option A: Using the Gateway Backup (`.gwbk`)
1. Open your Ignition Gateway UI at 'http://localhost:8088'.
2. Navigate to **Config** > **System** > **Backup/Restore**.
3. Select **Restore** and upload the Gateway backup file 'pump-tank-sim-backup.gwbk'.

### Option B: Using the Project Zip File
1. Open your Ignition Gateway UI at 'http://localhost:8088'.
2. Navigate to your **Config** > **Projects** section.
3. Click **Import Project** and upload your exported project zip file.

---

## OPC-UA Tags

* **Endpoint:** 'opc.tcp://127.0.0.1:4840/freeopcua/server/'
* **Namespace:** 'http://pumptank.simulation'

| Tag Name | Type | Access | Description |
| :--- | :--- | :--- | :--- |
| `Tank_Level_Percent` | Double | Read/Write | Current liquid level (0.0 - 100.0%) |
| `P101_Command` | Boolean | Read/Write | Pump running command |
| `Inlet_Valve_Command` | Boolean | Read/Write | Inlet valve command |
| `System_Mode` | String | Read/Write | Operational mode (`AUTO`, `MANUAL`, `STOP`) |

---

## Running the Simulation Locally

### Step 1: Create a virtual environment and install dependencies

```bash
# Create the virtual environment
python -m venv venv

# Activate it
source venv/bin/activate       # On macOS / Linux
venv\Scripts\activate          # On Windows

# Install dependencies
pip install -r requirements.txt
```

###Step 2: Run the simulation script
```bash
python pump_tank_sim.py
```