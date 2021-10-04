from gpiozero import LED, Buzzer
from time import sleep


def beep_buzzer(time):
    int_time = int(time)
    myBuzzer = Buzzer(25)
    myBuzzer.on()
    sleep(int_time)
    myBuzzer.off()


def convert_binary(input_entry_f):
    int_entry = int(input_entry_f)
    string_binary = bin(int_entry)
    
    string_binary = string_binary[2:]
    
    while len(string_binary) != 8:
        string_binary = "0" + string_binary
    return string_binary


def show_binary(binary_f):
    
    led_array = []
    
    led_array.append(LED(4))
    led_array.append(LED(17))
    led_array.append(LED(27))
    led_array.append(LED(22))
    led_array.append(LED(5))
    led_array.append(LED(6))
    led_array.append(LED(13))
    led_array.append(LED(26))
    
    count = 0
    for char in binary_f:
        if char == "1":
            led_array[count].on()
        
        count += 1
    
    sleep(5)
    

def convert_tap_code(input_entry_f):
    global tap_code_dict

    input_capitalized = input_entry_f.upper()
    tap_code_f = ""

    count = 0
    for char in input_capitalized:
        if input_capitalized[count] == " ":
            tap_code_f = tap_code_f[:-1]
            tap_code_f += tap_code_dict.get(char)
        else:
            if char == "K":
                char = "C"
            tap_code_f += tap_code_dict.get(char) + " "

        count += 1

    return tap_code_f


def show_tap_code(tap_code_f):
    LED_code = LED(12)
    for char in tap_code_f:
        if char == ".":
            LED_code.on()
            sleep(0.25)
            LED_code.off()
            sleep(0.25)
            
        elif char == ",":
            LED_code.on()
            sleep(0.75)
            LED_code.off()
            sleep(0.25)
            
        elif char == "/":
            LED_code.on()
            sleep(2)
            LED_code.off()
            sleep(1.5)
            
        elif char == " ":
            LED_code.off()
            sleep(0.5)
        print(char, end = "")

tap_code_dict = {"A": ".,.", "B": ".,..", "C": ".,...", "D": ".,....", "E": ".,.....",
                 "F": "..,.", "G": "..,..", "H": "..,...", "I": "..,....", "J": "..,.....",
                 "L": "...,.", "M": "...,..", "N": "...,...", "O": "...,....", "P": "...,.....",
                 "Q": "....,.", "R": "....,..", "S": "....,...", "T": "....,....", "U": "....,.....",
                 "V": ".....,.", "W": ".....,..", "X": ".....,...", "Y": ".....,....", "Z": ".....,.....",
                 " ": "/"}

while True:
    input_entry = input("Entrez un message: ")

    if input_entry == "STOP":
        print("arret")
        break

    elif all(char.isalpha() or char.isspace() for char in input_entry):
        tap_code = convert_tap_code(input_entry)
        show_tap_code(tap_code)

    elif input_entry.isdecimal() and (255 >= int(input_entry) >= 0):
        binary = convert_binary(input_entry)
        print(binary)
        show_binary(binary)

    else:
        print("erreur")
        beep_buzzer(1)