from netmiko import ConnectHandler

cisco_sw = {
    'device_type': 'cisco_ios',
    'host': input("please write the ip or the name of the switch : "),
    """                                                                                               
    in the user name and password you will need change and add you're admin permission.               
    """                                                                                               
    'username': '**********',
    'password': '**********',
}

net_connect = ConnectHandler(**cisco_sw)

output = net_connect.send_command("show interfaces status")
print(output)
