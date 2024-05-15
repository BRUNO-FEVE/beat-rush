from picozero import Speaker, LED
from picozero import Button
from time import sleep

speaker = Speaker(15)
button_1 = Button(18)
button_2 = Button(21)
button_3 = Button(16)
button_4 = Button(17)
button_5 = Button(17)
button_6 = Button(17)
button_7 = Button(17)

led_1 = LED(19)
led_2 = LED(20)
led_3 = LED(13)
led_4 = LED(12)
led_5 = LED(13)
led_6 = LED(12)
led_7 = LED(12)

BEAT = 0.3  

##liten_mus = [ ['d5', BEAT / 2], ['d#5', BEAT / 2], ['f5', BEAT], ['d6', BEAT], ['a#5', BEAT], ['d5', BEAT],
##              ['f5', BEAT], ['d#5', BEAT], ['d#5', BEAT], ['c5', BEAT / 2],['d5', BEAT / 2], ['d#5', BEAT],
##              ['c6', BEAT], ['a5', BEAT], ['d5', BEAT], ['g5', BEAT], ['f5', BEAT], ['f5', BEAT], ['d5', BEAT / 2],
##              ['d#5', BEAT / 2], ['f5', BEAT], ['g5', BEAT], ['a5', BEAT], ['a#5', BEAT], ['a5', BEAT], ['g5', BEAT],
##              ['g5', BEAT], ['', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT / 2], ['d6', BEAT / 2], ['c6', BEAT / 2],
##              ['a#5', BEAT / 2], ['a5', BEAT / 2], ['g5', BEAT / 2], ['a5', BEAT / 2], ['a#5', BEAT / 2], ['c6', BEAT],
##              ['f5', BEAT], ['f5', BEAT], ['f5', BEAT / 2], ['d#5', BEAT / 2], ['d5', BEAT], ['f5', BEAT], ['d6', BEAT],
##              ['d6', BEAT / 2], ['c6', BEAT / 2], ['b5', BEAT], ['g5', BEAT], ['g5', BEAT], ['c6', BEAT / 2],
##              ['a#5', BEAT / 2], ['a5', BEAT], ['f5', BEAT], ['d6', BEAT], ['a5', BEAT], ['a#5', BEAT * 1.5] ]


liten_mus = [['c4', BEAT], ['d4', BEAT], ['c4', BEAT], ['c4', BEAT],
             ['c4', BEAT], ['d4', BEAT], ['c4', BEAT], ['c4', BEAT],
             ['c4', BEAT], ['d4', BEAT], ['c4', BEAT], ['c4', BEAT],
             ['c4', BEAT], ['d4', BEAT], ['c4', BEAT], ['c4', BEAT]]

def c4():
    led_1.on()
    button_C4_pressed = False
    
    while not button_C4_pressed:  
        if button_1.is_pressed:
            led_1.off()
            button_C4_pressed = True
    
    return button_C4_pressed

def d4():
    led_2.on()
    button_D4_pressed = False
    
    while not button_D4_pressed:  
        if button_2.is_pressed:
            led_2.off()
            button_D4_pressed = True
    
    return button_D4_pressed

def e4():
    led_3.on()
    button_E4_pressed = False
    
    while not button_E4_pressed:  
        if button_3.is_pressed:
            led_3.off()
            button_E4_pressed = True
    
    return button_E4_pressed

def f4():
    led_4.on()
    button_F4_pressed = False
    
    while not button_F4_pressed:  
        if button_4.is_pressed:
            led_4.off()
            button_F4_pressed = True
    
    return button_F4_pressed

def g4():
    led_5.on()
    button_G4_pressed = False
    
    while not button_G4_pressed:  
        if button_5.is_pressed:
            led_5.off()
            button_G4_pressed = True
    
    return button_G4_pressed

def a4():
    led_6.on()
    button_A4_pressed = False
    
    while not button_A4_pressed:  
        if button_6.is_pressed:
            led_6.off()
            button_A4_pressed = True
    
    return button_A4_pressed

def b4():
    led_7.on()
    button_B4_pressed = False
    
    while not button_B4_pressed:  
        if button_7.is_pressed:
            led_7.off()
            button_B4_pressed = True
    
    return button_B4_pressed

def default_case():
    print("Invalid case")

def switch(note):
    switcher = {
        'c4': c4,
        'd4': d4,
        'e4': e4,
        'f4': f4,
        'g4': g4,
        'a4': a4,
        'b4': b4
        }
    
    case = switcher.get(note, default_case)
    return case()

def play():
    noteNumber = 0
    while noteNumber < len(liten_mus):
        
        is_pressed = switch(liten_mus[noteNumber][0])
        if is_pressed:
            speaker.play(liten_mus[noteNumber][0], liten_mus[noteNumber][1])
            sleep(0.1)
            noteNumber += 1
    print('Fim da Musica!!')


def c_note():
    speaker.play('c4',0.3)
def d_note():
    speaker.play('d4',0.3)
def e_note():
    speaker.play('e4',0.3)
def f_note():
    speaker.play('f4',0.3)
def play_liten_mus():
    speaker.play(liten_mus)
def note_1():
    led_1.off()
    
play()
button_1.when_pressed = c_note
button_2.when_pressed = d_note
#button_3.when_pressed = e_note
#button_4.when_pressed = f_note

