print('''
This program takes inputs of marks

\t of ALL your subjects
\t (Sindhi, Urdu, Eng, Math, Comp/Bio, Phy, Chem, P. St, Isl)

\t and outputs your whole marksheet.
''')

def g(percentage): 
    if float(percentage) >= 90: return "A+"
    elif float(percentage) >= 80: return "A"
    elif float(percentage) >= 70: return "B"
    elif float(percentage) >= 60: return "C"
    elif float(percentage) >= 50: return "D"
    else : return "Ungraded"
#
def p75(marks):
	return str(round(float(marks)*100/75, 2))
#

print('''
Enter your marks (out of 75) for the subjects below.
''')
snd = input("Sindhi:\t\t\t")

urd = input("Urdu:\t\t\t")

eng = input("English:\t\t")

mth = input("Maths:\t\t\t")

bio = input("Biology/Computer:\t")

phy = input("Physics:\t\t")

chm = input("Chemistry:\t\t")

pst = input("Pak Studies:\t\t")

isl = input("Islamiat:\t\t")

print('''
--------------------------------------------------------------------------------
----------------------------------MARK SHEET------------------------------------ 

Subjects				Marks	Percentage	Grade
--------				-----	----------	-----
Sindhi					'''+snd+'''	'''+p75(snd)+'''		'''+g(p75(snd))+'''
Urdu					'''+urd+'''	'''+p75(urd)+'''		'''+g(p75(urd))+'''
English					'''+eng+'''	'''+p75(eng)+'''		'''+g(p75(eng))+'''
Maths					'''+mth+'''	'''+p75(mth)+'''		'''+g(p75(mth))+'''
Biology/Computer			'''+bio+'''	'''+p75(bio)+'''		'''+g(p75(bio))+'''
Physics					'''+phy+'''	'''+p75(phy)+'''		'''+g(p75(phy))+'''
Chemistry				'''+chm+'''	'''+p75(chm)+'''		'''+g(p75(chm))+'''
Pak Studies				'''+pst+'''	'''+p75(pst)+'''		'''+g(p75(pst))+'''
Islamiat				'''+isl+'''	'''+p75(isl)+'''		'''+g(p75(isl))+'''
''')

