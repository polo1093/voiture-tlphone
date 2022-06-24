def on_bluetooth_connected():
    global connected
    basic.show_icon(IconNames.HEART)
    connected = 1
    while connected == 1:
        rec_data = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        serial.write_string(rec_data)
        serial.write_line("")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SAD)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

connected = 0
connected2 = 0
serial.redirect_to_usb()
# boucle

def on_forever():
    led.toggle(0, dht11_dht22.read_data(dataType.TEMPERATURE))
basic.forever(on_forever)
