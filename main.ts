radio.onReceivedNumber(function (receivedNumber) {
    imagen.showImage((receivedNumber + 5) % 10)
})
input.onButtonPressed(Button.A, function () {
    offset += 1
    offset = offset % 10
    radio.sendNumber(offset)
    imagen.showImage(offset)
})
input.onButtonPressed(Button.B, function () {
    offset = offset - 1
    offset = offset % 10
    radio.sendNumber(offset)
    imagen.showImage(offset)
})
let imagen: Image = null
let offset = 0
offset = 0
imagen = images.createBigImage(`
    . . . # # . . . . .
    . . . . . # . . . .
    . . . . . # # . . .
    . # . # # # # # . #
    # # # # # # # # # #
    `)
