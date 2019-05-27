## input marks, output grade and percentage

m = float(input("How many marks did you obtain out of 75?\t"))

p = round(m*100/75, 2)

if p >= 90:
	g = "A+"
elif p >= 80:
	g = "A"
elif p >= 70:
	g = "B"
elif p >= 60:
	g = "C"
elif p >= 50:
	g = "D"
else:
	g = "Ungraded"

print ("Percentage = \t" + str(p))
print ("Grade = \t" + g)
