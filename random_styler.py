# generate matrix rain using ACGT
# font family required: OverpassMono-Bold
# 	download - https://www.fontsquirrel.com/fonts/overpass-mono
# 	google fonts - https://fonts.google.com/specimen/Overpass+Mono

from random import random, randint

default_start = '<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!-- Generator: Adobe Illustrator 22.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->\n<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\"\n\t viewBox=\"0 0 1000 1000\" style=\"enable-background:new 0 0 1000 1000;\" xml:space=\"preserve\">\n<style type=\"text/css\">\n\t.st0{font-family:\'OverpassMono-Bold\';}\n\t.st1{font-size:27.053px;}\n\t.st2{letter-spacing:1;}'
default_end = '</g>\n</svg>'
print(default_start)

colors = ['#003B00', '#008F11', '#00FF41']
opacities = [0.05 * i for i in range(3, 15)]
# get color schemes
nstyles = 40
for i in range(nstyles):
	print('\t.st'+str(i+3)+'{opacity:'+str(opacities[randint(0, len(opacities)-1)])+';fill:'+colors[randint(0, len(colors)-1)]+';}')
print('</style>')

gc = 0.69
nchars = 2000
nrows = 20
line_length = 45
width = 17.639
count = 0

alphabets = []
for i in range(nchars):
	if random() < gc:
		if random() < 0.5:
			alphabets.append('C')
		else:
			alphabets.append('G')
	else:
		if random() > 0.5:
			alphabets.append('A')
		else:
			alphabets.append('T')

print('<g>')
for i in range(nrows):
	for j in range(line_length):
		print('\t<text transform=\"matrix(1 0 0 1 '+str(20+width*j)+' '+str(70+25*i)+')\" class=\"st'+str(randint(3, nstyles+2))+' st1 st2 st0\">', end='')
		print(alphabets[count], end='')
		print('</text>')
		count += 1
print(default_end)

# log output to an svg file