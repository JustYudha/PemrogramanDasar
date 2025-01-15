import RPi.GPIO as GPIO
import time

# Mengatur mode pin GPIO
GPIO.setmode(GPIO.BCM)

# Daftar pin LED yang akan digunakan
led_pins = [4, 6, 5, 17, 27, 22]

# Menyiapkan pin LED sebagai output
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        # Menyalakan LED dalam urutan normal tertentu
        normal_order = [led_pins[0], led_pins[3], led_pins[4], led_pins[5], led_pins[2], led_pins[1]]
        
        # Menyalakan LED satu per satu sesuai urutan
        for pin in normal_order:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.5)
        
        # Mematikan LED satu per satu sesuai urutan
        for pin in normal_order:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.5)
        
        # Menyalakan LED dalam pola zigzag (pertama LED pada posisi ganjil, kemudian posisi genap)
        for i in range(0, len(led_pins), 2):
            GPIO.output(led_pins[i], GPIO.HIGH)
            time.sleep(0.5)
        
        for i in range(1, len(led_pins), 2):
            GPIO.output(led_pins[i], GPIO.HIGH)
            time.sleep(0.5)

        # Mematikan LED dalam pola zigzag
        for i in range(0, len(led_pins), 2):
            GPIO.output(led_pins[i], GPIO.LOW)
            time.sleep(0.5)
        
        for i in range(1, len(led_pins), 2):
            GPIO.output(led_pins[i], GPIO.LOW)
            time.sleep(0.5)

except KeyboardInterrupt:
    print("Program Berhenti")

finally:
    GPIO.cleanup()
