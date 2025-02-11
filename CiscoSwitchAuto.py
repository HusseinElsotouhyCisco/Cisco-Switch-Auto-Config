import csv
from netmiko import ConnectHandler

# Open and read the CSV file
with open('devices.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in CSV file
    for row in csv_reader:
        # Extract device details from each row
        ip = row['ip']
        username = row['username']
        password = row['password']
        secret = row['secret']
        config_file = row['config_file']
        

        # Establish a connection to the device
        device = ConnectHandler(
            ip=ip,
            device_type='cisco_nxos', #device type can be different depending on device vendor and model
            username=username,
            password=password,
            secret=secret
        )
        

        # Enter enable mode
        device.enable()

        # Send configuration commands from the specified file
        output = device.send_config_from_file(config_file=config_file)
        
        print(f"\nConfiguration output for {ip}:\n{output}")
        
        #use this to save every device output in separate text files
        #file = open(ip +'_output.txt','w')
        #file.write(output)

        save = device.save_config()
        print(save)
        

        # Disconnect from the device
        device.disconnect()
