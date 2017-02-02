"""Method Exercise
Tax in US based on states:

Create a method, which takes the state and gross income as the arguments
and returns the net income after deducting tax based on the state.

Assume Federal tax is 10%
Assume State tax on your wish.
"""

def taxCalc(grossInc, state):
    """
    Calculate the net income after federal and state tax
    :param grossInc: Gross income
    :param state: State name
    :return: Net income
    """

    # Calculate net income after federal tax
    netInc = grossInc - (grossInc * 10 / 100)

    # Calculate net income after state tax
    stateTaxMatrix = {'CA': 10, 'AZ': 8.5, 'FL': 7.3, 'NV': 6.75}
    if state in stateTaxMatrix:
        netInc = netInc - (netInc * stateTaxMatrix[state]/100)

    return netInc

print("---", "Calculates federal and state tax", "-"*10)
myGrossInc = 98450
st = 'NV'

print("My gross income is:", str(myGrossInc))
print("My state is:", str(st))
print("My net income is:", taxCalc(myGrossInc, st))
