import asyncio
from asyncua import Server, ua

async def main():
    # 1. Initialize OPC-UA Server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://127.0.0.1:4840/freeopcua/server/")
    server.set_server_name("Pump & Tank Process Simulator")

    # 2. Setup Namespace & Folder Structure
    uri = "http://pumptank.simulation"
    idx = await server.register_namespace(uri)
    
    objects = server.nodes.objects
    tank_folder = await objects.add_folder(idx, "PumpTank_System")

    # 3. Define Process Tags
    tank_level = await tank_folder.add_variable(idx, "Tank_Level_Percent", 40.0, ua.VariantType.Double)
    pump_cmd = await tank_folder.add_variable(idx, "P101_Command", False, ua.VariantType.Boolean)
    inlet_valve = await tank_folder.add_variable(idx, "Inlet_Valve_Command", False, ua.VariantType.Boolean)
    system_mode = await tank_folder.add_variable(idx, "System_Mode", "AUTO", ua.VariantType.String)
    
    # Make tags writable by Ignition
    await tank_level.set_writable()
    await pump_cmd.set_writable()
    await inlet_valve.set_writable()
    await system_mode.set_writable()

    print("OPC-UA Server Running at opc.tcp://127.0.0.1:4840")
    
    async with server:
        while True:
            # Read Current State from OPC Nodes
            level = await tank_level.get_value()
            pump = await pump_cmd.get_value()
            inlet = await inlet_valve.get_value()
            mode = await system_mode.get_value()

            fill_rate = 0.0
            drain_rate = 0.0

            if mode == "AUTO":
                # Interlock: Low Level Protection (Trips to STOP)
                if level <= 5.0:
                    print("CRITICAL ALARM: Low Level Interlock Tripped! Forcing System to STOP.")
                    await system_mode.set_value("STOP")
                    await pump_cmd.set_value(False)
                    await inlet_valve.set_value(False)
                    fill_rate = 0.0
                    drain_rate = 0.0
                else:
                    # Fill/Drain Control Logic
                    if level < 50.0 and not inlet:
                        await inlet_valve.set_value(True)
                        inlet = True
                    elif level > 70.0 and inlet:
                        await inlet_valve.set_value(False)
                        inlet = False

                    if level > 70.0 and not pump:
                        await pump_cmd.set_value(True)
                        pump = True
                    elif level < 50.0 and pump and level > 5.0:
                        await pump_cmd.set_value(False)
                        pump = False

                    if inlet: fill_rate = 2.0
                    if pump: drain_rate = 3.0

            elif mode == "STOP":
                # Force commands off and freeze level
                if pump:
                    await pump_cmd.set_value(False)
                    pump = False
                if inlet:
                    await inlet_valve.set_value(False)
                    inlet = False
                fill_rate = 0.0
                drain_rate = 0.0

            elif mode == "MANUAL":
                # Respect operator HMI toggle states directly
                if inlet: fill_rate = 2.0
                if pump: drain_rate = 3.0

            # Apply single unified physics step
            level += fill_rate - drain_rate
            level = max(0.0, min(100.0, level))
            await tank_level.set_value(round(level, 2))

            await asyncio.sleep(1.0)

if __name__ == "__main__":
    asyncio.run(main())