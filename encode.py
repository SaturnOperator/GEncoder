import re

# Conversion constants
POINT2IN = 1/72
POINT2MM = POINT2IN*25.4

# Regex
dimensionPattern = r'^%%HiResBoundingBox: (?:[0-9.]*\s?){4}$'
curvePattern = r'^\s%.*?/DeviceRGB'
cordPattern = r'(?:[0-9\.]+\s?){2}'

fileName = 'test.eps'

with open(fileName, 'rU') as file:
	data = file.read()
	file.close()

curves = re.findall(curvePattern, data, flags=re.M|re.S)
