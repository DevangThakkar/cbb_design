# generate a pseudorandom IGVesque read depth plot

from random import random

default_start = '<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!-- Generator: Adobe Illustrator 22.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->\n<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\"\n\tviewBox="0 0 1000 1000" style="enable-background:new 0 0 1000 1000;\" xml:space=\"preserve\">\n<g>'
default_end = '</g>\n</svg>'

y_base = 200
width = 5
height = 50.0
x = 100
n = 200
print(default_start)
for i in range(n):
	if (random() < 0.5 and height < 120) or height < 20:
		height = height + random()*5
	else:
		height = height - random()*5
	x = x + width
	print('<rect x=\"'+str(x)+'\" y=\"'+str(y_base-height)+'\" width=\"'+str(width)+'\" height=\"'+str(height)+'\"/>')
print(default_end)

# log output to an svg file