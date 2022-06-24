bluetooth.onBluetoothConnected(function () {
    let rec_data: string;
basic.showIcon(IconNames.Heart)
    connected = 1
    while (connected == 1) {
        rec_data = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Hash))
        serial.writeString(rec_data)
        serial.writeLine("")
    }
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.Sad)
})
let connected = 0
let connected2 = 0
serial.redirectToUSB()
// boucle
basic.forever(function () {
	
})
