'''
taxesform.py
Author: ME, DIO!

Compute a persons income tax
1. SIGNIFICANT CONSTANTS
    tax rate
    stnd ded
    ded per dep
2. Inputs()
    gross inc
    # o dep
3. Com-pu-tations
    Taxable inc = GI - stnd ded - ded per dep
    inc tax = fixed percentage of the taxable inc
4. OUTPUTS
    inc tax
'''

TAX_RATE = 0.20
STND_DED = 10000.0
DEP_DED = 1000.0

grossInc = float(input("Enter your gross income, sir, maam, or nonbinary: "))
numDep = int(input("How many little buddies you got?: "))

taxableInc = grossInc - STND_DED - DEP_DED * numDep

incTax = taxableInc * TAX_RATE

print("The income tax is: " + str(incTax) + "$")