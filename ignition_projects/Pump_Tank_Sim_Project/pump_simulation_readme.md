# Pump & Tank Process Simulator

An asynchronous Python OPC-UA server that models a closed-loop liquid tank system with automated control, manual overrides, and low-level safety interlocks.

## Overview

This script (`pump_tank_sim.py`) uses `asyncua` to run a local OPC-UA server, allowing Ignition SCADA (or other OPC-UA clients) to read and write live process tags.

### Operational Modes (`System_Mode`)

* **AUTO:** Automated differential control. The inlet valve opens below 50.0% level and closes above 70.0%. The pump turns on above 70.0% and turns off below 50.0%.
* **MANUAL:** Bypasses auto-logic and allows direct HMI toggling of valves and pumps.
* **STOP:** Freezes process physics and disables all actuator commands.
* **Low-Level Interlock:** If the tank level drops <= 5.0%, the system automatically forces a trip to STOP to prevent dry pump operation.

## OPC-UA Tags

* **Endpoint:** `opc.tcp://127.0.0.1:4840/freeopcua/server/`
* **Namespace:** `http://pumptank.simulation`

| Tag Name | Type | Access | Description |
| :--- | :--- | :--- | :--- |
| `Tank_Level_Percent` | Double | Read/Write | Current liquid level (0.0 - 100.0%) |
| `P101_Command` | Boolean | Read/Write | Pump running command |
| `Inlet_Valve_Command` | Boolean | Read/Write | Inlet valve command |
| `System_Mode` | String | Read/Write | Operational mode (`AUTO`, `MANUAL`, `STOP`) |

## Running Locally

### Step 1: Create a virtual environment and install dependencies

```
# 1. Create the virtual environment folder (usually named 'venv')
python -m venv venv

# 2. Activate it (tells your terminal to use this specific environment's Python/pip)
source venv/bin/activate       # On macOS / Linux
venv\Scripts\activate          # On Windows (Command Prompt / PowerShell)

# 3. Install the project dependencies locally into this folder
pip install -r requirements.txt

```

### Step 2: Run the simulation script

```
python pump_tank_sim.py
```