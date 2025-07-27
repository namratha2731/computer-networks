
# Energy-Efficient Scheduling and Power Control in 5G V2X Networks

This repository provides a foundational simulation framework built around SUMO (Simulation of Urban MObility), designed to model and analyze traffic dynamics within urban environments. While primarily a mobility simulator, this project serves as a crucial underlying platform for investigating advanced topics such as Energy-Efficient Scheduling and Power Control in future 5G Vehicle-to-Everything (V2X) Networks. By accurately representing realistic vehicular movement and network topology, it creates a robust testbed for developing and evaluating communication and resource management strategies vital for next-generation intelligent transportation systems.

---

## ✨ Key Features & Components

- **Realistic Urban Mobility Modeling**  
  - **OpenStreetMap (OSM) Integration:** Uses `map.osm` to convert real-world road networks into SUMO-compatible format (`map.net.xml`), capturing detailed road infrastructure, intersections, and traffic regulations.
  - **Dynamic Traffic Generation:** Leverages `randomTrips.py` to generate diverse vehicle trips simulating varying densities and origins/destinations (`trips.trips.xml`, `map.rou.xml`).

- **Flexible Traffic Scenarios & Route Management**  
  - Supports primary (`map.rou.xml`) and alternative (`map.rou.alt.xml`) route definitions to simulate route choices and congestion effects.  
  - Enables use of refined or optimized routes (`updated_routes.xml`) for customized scenarios.

- **SUMO Simulation Environment Configuration**  
  - Centralized via `map.sumocfg`, linking network, routes, and simulation parameters (duration, step length, outputs) for reproducibility and flexibility.

- **Python Scripting for External Control & Analysis**  
  - Provides `eng.py` script to interact with SUMO simulations using TraCI or similar APIs for real-time control, data collection, and the injection of custom behaviors — essential for testing advanced scheduling and power control algorithms without modifying SUMO internals.

---

## 🛠️ Technologies Used

- **SUMO (Simulation of Urban MObility):** Core microscopic traffic and mobility simulation engine.  
- **Python 3.x:** For scripting and automation, including SUMO interaction.  
- **XML:** Standard format defining network, routes, and simulation configuration files.  
- **OpenStreetMap (OSM):** Source data for realistic geographical and road network information.

---

## 📁 Project Structure

```
computer-networks/
├── eng.py             # Python script for SUMO interaction (e.g., using TraCI)
├── map.net.xml        # Generated SUMO network from OSM data
├── map.osm            # Original OpenStreetMap data file
├── map.poly.xml       # SUMO polygon data (e.g., buildings, visual elements)
├── map.rou.alt.xml    # Alternative vehicle route definitions
├── map.rou.xml        # Primary vehicle route definitions
├── map.sumocfg        # Main SUMO configuration file for simulation orchestration
├── randomTrips.py     # Script to generate random vehicle trips in SUMO
├── trips.trips.xml    # Generated trips file referenced by routes
├── typemap.xml        # Vehicle and road property types definitions
└── updated_routes.xml # Refined or dynamically updated route definitions
```

---

## ⚙️ Setup and Installation

1. **Install SUMO**  
   Download and install from [https://sumo.dlr.de](https://sumo.dlr.de). Make sure `sumo` and `sumo-gui` executables are added to your system PATH to enable running the simulator and conversion tools.

2. **Install Python**  
   Ensure Python 3.x is installed on your system.

3. **Clone the Repository**  
   ```
   git clone 
   cd computer-networks
   ```

---

## ▶️ Getting Started

### 1. Generate SUMO Network  
If `map.net.xml` is missing or should be regenerated from OSM data:  
```
netconvert --osm-files map.osm -o map.net.xml --typemap typemap.xml --output.street-names true --geometry.remove --remove-edges.isolated --keep-edges.by-vclass passenger --keep-edges.by-id -v -x
```
*(Adjust netconvert options as needed for your network specifics.)*

### 2. Generate Traffic Trips  
Use `randomTrips.py` to simulate random trips and create route files:  
```
python randomTrips.py -n map.net.xml -r map.rou.xml -e  -p 
```
Replace `` and `` with your desired values.

### 3. Run the Simulation

- **With GUI (visualization):**  
  ```
  sumo-gui -c map.sumocfg
  ```

- **Without GUI (faster execution):**  
  ```
  sumo -c map.sumocfg
  ```

### 4. Interact via Python (using TraCI or similar)  
To use `eng.py` to control or analyze the simulation:  

- Start SUMO in client/server mode with a remote port:  
  ```
  sumo-gui -c map.sumocfg --remote-port 
  ```

- In another terminal, run the Python script:  
  ```
  python eng.py
  ```

---

## 💡 Conclusion

This project offers a robust and adaptable simulation environment for exploring complex challenges in urban mobility and vehicular communications. By enabling realistic traffic scenario generation and flexible network modeling, it lays a solid foundation for research into Energy-Efficient Scheduling and Power Control in 5G V2X Networks. Such a framework is integral to designing intelligent transportation systems that balance efficiency, reliability, and sustainability. Future extensions could integrate detailed 5G V2X communication models, sophisticated scheduling algorithms, and comprehensive energy consumption assessments to further optimize network performance for smart city applications.

