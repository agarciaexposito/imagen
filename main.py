def on_received_number(receivedNumber):
    imagen.show_image((receivedNumber+5)%10)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global offset
    offset += 1
    offset =offset % 10 
    radio.send_number(offset)
    imagen.show_image(offset)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global offset
    offset = offset - 1
    offset =offset % 10
    radio.send_number(offset)
    imagen.show_image(offset)
input.on_button_pressed(Button.B, on_button_pressed_b)

imagen: Image = None
offset = 0
offset = 0
imagen = images.create_big_image("""
    . . . # # . . . . .
        . . . . . # . . . .
        . . . . . # # . . .
        . # . # # # # # . #
        # # # # # # # # # #
""")