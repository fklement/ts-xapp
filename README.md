# Traffic Steering (TS) xApp

The Traffic Steering (TS) xApp is a powerful tool tailored for the [OAIC O-RAN testbed](https://www.openaicellular.org/). It aims to manage and optimize traffic flow within cellular networks efficiently. By harnessing real-time metrics and adhering to dynamic policies, this xApp ensures optimal network performance through informed decisions about user equipment (UE) handovers between cells.

## 🌟 Key Features

- **Interface Integration**: Seamless integration with E2 and A1 interfaces for direct RAN communication and real-time metric acquisition.
- **Dynamic Policy Management**: Adapts traffic steering policies based on real-time A1 interface updates.
- **Load Balancing**: Detects overloaded cells and redistributes UEs for balanced load across cells.
- **UE Profiling**: Detailed profiling of each UE, including attributes like ID, cell, priority, type, origin, signal strength, and throughput.
- **InfluxDB Integration**: Logs metrics and policies in InfluxDB, facilitating historical data analysis and visualization with tools like Grafana.
- **Flask API Support**: Enables external xApps to dynamically push or modify policies, supporting ML/RL/DRL plugins.
- **Scalability**: Designed to handle an increasing number of UEs and cells without compromising efficiency.
- **Modular Design**: Future-proofed for easy integration of upcoming features.

## 🛠 Prerequisites

- Install [OAIC and SRSRAN](https://openaicellular.github.io/oaic/).
- Set up multiple UEs and initiate network traffic flow.

# 🚀 Getting Started

1. Execute the RIC installation script:
   ```bash
   ./Ricinstalation.sh

2. Run `srsran.sh`.

4. Clone the TS-xApp repository: https://github.com/natanzi/TS-xApp
5. Build the Docker image and submit it to the xApp registry:
   ```bash
   sudo docker build . -t xApp-registry.local:5008/TS-xApp:1.0.0
   
6. Get Local IP Address
   export HOST_IP=$(hostname -I | awk '{print $1}')

## 🤝 Contributing
Your contributions can enhance this xApp! Fork the repository and submit a pull request with your changes.
