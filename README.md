#Energy-Efficient Scheduling and Power Control in 5G V2X Networks

This repository provides tools and resources for simulating and analyzing urban traffic networks using SUMO (Simulation of Urban MObility). You'll find everything needed to set up a realistic traffic environment, generate vehicle routes, and run and analyze simulations in various traffic scenarios.

## ✨ Features

- **Custom Network Creation:** Build realistic road networks from OpenStreetMap (OSM) data (`map.osm`).
- **Traffic Route Generation:** Create random or scenario-based vehicle trips and routes, supporting diverse traffic patterns (`randomTrips.py`, `map.rou.xml`, `map.rou.alt.xml`, `trips.trips.xml`).
- **SUMO Simulation Configuration:** Tweak and run simulations via SUMO configuration files (`map.sumocfg`).
- **Python Scripting:** Includes helper Python scripts (`eng.py`) for interacting with SUMO (e.g., automation, analysis, or generating simulation inputs).

## 🛠️ Technologies Used

- **SUMO:** Main tool for microscopic traffic simulation.
- **Python 3.x:** Scripting and automation.
- **XML:** Format for SUMO’s network, route, and configuration files.
- **OpenStreetMap (OSM):** Source for map data.

## 📁 Project Structure

```
computer-networks/
├── eng.py             # Python script for SUMO interaction and analysis
├── map.net.xml        # SUMO network, generated from OSM data
├── map.osm            # Raw OpenStreetMap file
├── map.poly.xml       # Polygon data (e.g., buildings, areas)
├── map.rou.alt.xml    # Alternative route definitions
├── map.rou.xml        # Main vehicle route definitions
├── map.sumocfg        # SUMO simulation configuration
├── randomTrips.py     # Script for generating random vehicle trips
├── trips.trips.xml    # Generated trip data
├── typemap.xml        # Type definitions for network elements
└── updated_routes.xml # Updated/refined routes
```

## ⚙️ Setup and Installation

1. **Install SUMO**  
   Follow the official [SUMO documentation](https://sumo.dlr.de/docs/Installing.html) to install SUMO on your operating system. Add both `sumo-gui` and `sumo` to your system `PATH`.

2. **Install Python**  
   Ensure you have Python 3.x installed.

3. **Clone the Repository**
   ```
   git clone 
   cd computer-networks
   ```

## ▶️ Usage

**Step 1: Generate Network and Routes (if needed)**

- **Build SUMO Network from OSM:**
  ```
  netconvert --osm-files map.osm -o map.net.xml
  ```

- **Generate Random Vehicle Trips:**
  ```
  python randomTrips.py -n map.net.xml -r map.rou.xml -e  -p 
  ```
  Replace `` and `` with desired simulation settings (e.g., duration, trip frequency).

**Step 2: Run the Simulation**

- **With GUI:**
  ```
  sumo-gui -c map.sumocfg
  ```
- **Command-line Only:**
  ```
  sumo -c map.sumocfg
  ```

**Step 3: Analyze or Extend the Simulation**

- **Run Python Analysis/Interaction Scripts:**
  ```
  python eng.py
  ```
  Ensure SUMO is running in client/server mode if your scripts require direct interaction.

---

*For further information and custom scenario creation, refer to SUMO's documentation and the comments within each script. Replace `` above with your own repo link.*
```
