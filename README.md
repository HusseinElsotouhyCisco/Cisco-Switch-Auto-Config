# Cisco Switch Configuration Automation

This repository contains a Python script to automate the configuration of Cisco switches and routers using the **Netmiko** library. It is designed for data center environments and has been tested on **EVE labs** and onsite.

## Prerequisites

Before using this script, ensure you have the following:

- **Python 3.8+** installed on your machine.
- Install the **Netmiko** library:
  ```bash
  pip install netmiko

Setup Instructions
------------------

### 1\. Check Your Network Settings

*   Open Command Prompt on your Windows machine and run:

 ```bash
  ipconfig
```

*   Find the **"Ethernet adapter VMware Network Adapter"** and note its IPv4 subnet --For EVE Lab Testing--

*   Find the Ethernet adapter connected to network, make sure it is in the same subnet as vlan assigned to switchport port --For data center/enterprise use--
    

### 2\. Configure Your Router Interface

*   Assign an IP address to the router interface connected to the **management cloud** within the same subnet as the **Ethernet adapter VMware Network Adapter**, with the same subnet mask. --For EVE Lab Testing--
    

### 3\. Apply Router Configuration --For EVE Lab/data center/enterprise use Testing--

*   Access the router console and enter the following commands:
```bash
conf t
!
hostname <your-choice-of-hostname>
ip route 0.0.0.0 0.0.0.0 Ethernet0/0
username <your-choice-of-username> password <your-choice-of-password>
line vty 0 4
  login local
  transport input telnet ssh
ip domain-name lab.local
crypto key generate rsa mod 2048
ip ssh version 2
enable password <your-choice-of-enable-password>
end
copy run start
```
*   Verify that you can **SSH** into the router. -- Router/Switch must be reachable through SSH --
    

Files in This Repository
------------------------

*   **config.txt** – Contains the configuration commands to be applied to multiple routers/switches.
    
*   **CiscoSwitchAuto.py** – The main Python script that connects to routers and switches using Netmiko and applies configurations from config.txt.
    

Installation
------------

### 1\. Clone this repository:
```bash
  clone https://github.com/yourusername/cisco-switch-config.git
```    
### 2\. Change into the project directory:
```bash
  cd cisco-switch-config
```  
### 3\. Edit `config.txt` to include the desired configuration for your devices.
    

Running the Script
------------------

To execute the script, use the following command:
```bash
python CiscoSwitchAuto.py
````

### Example Usage

1.  **Automate Configuration**: The script connects to all routers/switches listed in `devices.csv` and automatically applies the configuration.
    
2.  **Modify Configuration**: You can edit `config.txt` to add new devices or update configurations.
    

More Information
----------------

For more details on **Netmiko**, visit the [Netmiko Documentation](https://pypi.org/project/netmiko/).

Developed by [Hussein Elsotouhy](https://eg.linkedin.com/in/hussein-elsotouhy-03137519b).

Special thanks to [Nour Nada](http://www.linkedin.com/in/nour-mamdouh-nada-920a65191) for support.
