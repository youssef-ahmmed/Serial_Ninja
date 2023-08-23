# Setting Dialog Combobox

BAUD_RATE = ['110', '300', '600', '1200', '2400', '4800', '9600', '14400',
             '19200', '38400', '57600', '115200', '128000', '256000']

COMMUNICATION_PROTOCOLS = ["Select Protocol", "UART", "SPI", "I2C", "CAN"]

FLOW_CONTROL = ["None", "Xon/Xoff", "RTS/CTS", "DSR/DTR"]


# Error Messages

PASSWORD_ERROR = "Password Not Valid"

SINGLETON_ERROR = "Controllers are singleton classes, please use the instance function"

TIMEOUT_ERROR = "Timeout in Sending Data"

CONFIGURATION_ERROR = "Device Can Not Be Found or Can Not Be Configured"

SETTING_ERROR = "No Setting Found"

SEND_SUCCESS = "Data Send Successfully"

PORT_NOT_OPEN_ERROR = "Port is not open"
