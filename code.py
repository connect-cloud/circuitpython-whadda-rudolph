import board
import time
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy

pixel_pin = board.D2
num_pixels = 24
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False, pixel_order='RGB')


pixels.brightness = 0.2

led_rowmap = [
    [18,19,20],
    [15,16,17],
    [12,13,14],
    [23],
    [21,22],
    [4,5,6,7],
    [1,3,8,10],
    [0,2,9,11]
    ]
left_ear = [0,1,2,3,4,5]
right_ear = [6,7,8,9,10,11]
nose = 23
left_eye = 21
right_eye = 22
belly_rowmap = [
    [18,19,20],
    [15,16,17],
    [12,13,14]
    ]
ear_rowmap = [
    [4,5,6,7],
    [1,3,8,10],
    [0,2,9,11]
    ]


def fade_color_list(start_color = (0,0,0), end_color = (255,255,255), steps = 100):
    start_color = fancy.CRGB(start_color[0], start_color[1], start_color[2])
    end_color = fancy.CRGB(end_color[0], end_color[1], end_color[2])
    temp_colorlist = [fancy.mix(start_color, end_color, i / (steps - 1)) for i in range(steps)]
    colorlist = []
    for color in temp_colorlist:
        colorlist.append(color.pack())
    colorlist = colorlist + colorlist[::-1] + colorlist # Add a fadeout
    return colorlist


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def row_rainbow(wait, rowmap):
    for j in range(255):
        for row_idx, row in enumerate(rowmap):
            color_index = (row_idx * 256 // num_pixels) + j
            for led in row:
                pixels[led] = wheel(color_index & 255)
            pixels.show()
            time.sleep(wait)

def row_solid(color, rowmap):
    for row in rowmap:
        for led in row:
            pixels[led] = color

def ear_fade(wait, color):
    colorlist = fade_color_list(start_color = (0,0,0), end_color = color, steps = 100)
    for color in colorlist:
        for led in left_ear:
            pixels[led] = color
        pixels.show()
        time.sleep(wait)
    for color in colorlist:
        for led in right_ear:
            pixels[led] = color
        pixels.show()
        time.sleep(wait)


while True:
    pixels[nose] = (255,0,0)
    pixels[left_eye] = (150,150,150)
    pixels[right_eye] = (150,150,150)
    pixels.show()
    ear_fade(0.01, (200,200,0))
    row_rainbow(0.01, ear_rowmap)
    row_solid((200,200,0),ear_rowmap)
    row_rainbow(0.01, belly_rowmap)
    time.sleep(1)
