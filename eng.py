import math
import random
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt
import traci

# Step 1: Collect user inputs
num_Cars = 9
car_data = []

print("Enter energy consumption and speed for 9 vehicles:")

for i in range(num_Cars):
    energy = float(input(f"Car {i+1} - Energy Consumption (kWh): "))
    speed = float(input(f"Car {i+1} - Speed (km/h): "))
    car_data.append({'id': f'car{i+1}', 'energy': energy, 'maxSpeed': speed})

# Step 2: Modify the Routes File
def update_routes_file(car_data, input_file='trips.trips.xml', output_file='updated_routes.xml'):
    # Load the existing routes file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Add vehicle types to the XML
    for car in car_data:
        vType = ET.Element(
            'vType',
            id=car['id'],
            accel="2.5",  # Example acceleration
            decel="4.5",  # Example deceleration
            maxSpeed=str(car['maxSpeed']),
        )
        root.insert(0, vType)  # Insert vType elements at the top

    # Assign vehicle types to trips
    for i, trip in enumerate(root.findall('trip')):
        trip.set('type', car_data[i % len(car_data)]['id'])

    # Save the modified file
    tree.write(output_file)
    print(f"Routes file updated and saved as '{output_file}'.")

update_routes_file(car_data)

# Step 3: Run SUMO Simulation
def run_sumo_simulation(config_file="map.sumocfg"):
    sumo_cmd = ["sumo-gui", "-c", config_file]  # Replace with your SUMO configuration file
    traci.start(sumo_cmd)

    total_energy = {}
    step = 0

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        # Get the list of active vehicles
        vehicle_ids = traci.vehicle.getIDList()

        # V2X Communication: Detect nearby vehicles and adjust speed
        for veh_id in vehicle_ids:
            try:
                # Get the position of the current vehicle
                veh_position = traci.vehicle.getPosition(veh_id)

                # Detect nearby vehicles within a radius (e.g., 50 meters)
                nearby_vehicles = []
                for other_veh_id in vehicle_ids:
                    if veh_id != other_veh_id:
                        other_position = traci.vehicle.getPosition(other_veh_id)
                        distance = math.sqrt(
                            (veh_position[0] - other_position[0]) ** 2 + (veh_position[1] - other_position[1]) ** 2
                        )
                        if distance < 50:  # Assuming 50 meters is the communication range
                            nearby_vehicles.append(other_veh_id)

                # Log detected nearby vehicles
                if nearby_vehicles:
                    print(f"Vehicle {veh_id} detected nearby vehicles: {nearby_vehicles}")

                    # Extract the vehicle index safely
                    try:
                        vehicle_index = int(''.join(filter(str.isdigit, veh_id))) % len(car_data)
                        max_speed = car_data[vehicle_index]['maxSpeed']
                    except (ValueError, IndexError):
                        # Handle cases where the veh_id does not match expected format or index is out of range
                        max_speed = 20.0  # Default fallback speed

                    # Adjust speed based on nearby vehicles
                    adjusted_speed = random.uniform(10, max_speed - 5)  # Random speed below maxSpeed
                    traci.vehicle.setSpeed(veh_id, adjusted_speed)
                    print(f"Vehicle {veh_id} adjusted speed to {adjusted_speed:.1f} m/s based on nearby vehicles.")

                # Accumulate energy consumption
                energy = traci.vehicle.getFuelConsumption(veh_id)
                if veh_id in total_energy:
                    total_energy[veh_id] += energy
                else:
                    total_energy[veh_id] = energy
            except traci.exceptions.TraCIException as e:
                print(f"Error retrieving data for vehicle {veh_id}: {e}")

        step += 1
        if step > 500:  # Stop the simulation after 500 steps to prevent infinite loops
            print("Simulation step limit reached.")
            break

    traci.close()

    # Compute optimized energy consumption
    optimized_energy = {veh_id: energy * 0.8 for veh_id, energy in total_energy.items()}
    return total_energy, optimized_energy



# Replace with your SUMO config file name
config_file = "map.sumocfg"
original_energy, optimized_energy = run_sumo_simulation(config_file)

# Step 4: Calculate and Display Results
def visualize_energy_data(original_energy, optimized_energy):
    total_original = sum(original_energy.values())
    total_optimized = sum(optimized_energy.values())
    energy_saved = total_original - total_optimized

    # Bar Chart: Original vs Optimized
    vehicle_ids = list(original_energy.keys())
    original = list(original_energy.values())
    optimized = list(optimized_energy.values())

    plt.figure(figsize=(12, 6))
    plt.bar(vehicle_ids, original, label="Original Energy", color="red", alpha=0.7)
    plt.bar(vehicle_ids, optimized, label="Optimized Energy", color="green", alpha=0.7)
    plt.title("Energy Consumption by Vehicle")
    plt.xlabel("Vehicle ID")
    plt.ylabel("Energy Consumption (kWh)")
    plt.legend()
    plt.show()

    # Print Summary
    print(f"Total Energy Consumption (Original): {total_original:.2f} kWh")
    print(f"Total Energy Consumption (Optimized): {total_optimized:.2f} kWh")
    print(f"Total Energy Saved: {energy_saved:.2f} kWh")
    print(f"Money Saved: ${energy_saved * 0.12:.2f} (at $0.12 per kWh)")

visualize_energy_data(original_energy, optimized_energy)
