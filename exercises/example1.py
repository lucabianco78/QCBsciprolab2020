"""
This is the first example of Python script.
"""
a = 10 # variable a
b = 33 # variable b
c = a / b # variable c holds the ratio

# Let's print the result to screen.
print("a:", a, " b:", b, " a/b=", c)


from Bio.Seq import Seq

a = Seq("ATATATACG")

a.alphabet
a.sequence()


from Bio.Emboss.Applications import WaterCommandline
cline = WaterCommandline(gapopen=10, gapextend=0.5)
cline.asequence = "asis:ACCCGGGCGCGGT"
cline.bsequence = "asis:ACCCGAGCGCGGT"
cline.outfile = "temp_water.txt"
print(cline)
