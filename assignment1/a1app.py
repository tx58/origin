"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Tianli Xia
Date:   Sep 11th, 2018
"""

import introcs
import a1

currency_from=input("3-letter code for original currency:")
currency_to=input("3-letter code for the new currency:")
amount_from=input("Amount of the original currency:")
amount_to=a1.exchange(currency_from, currency_to, amount_from)
print("You can exchange " + str(amount_from)+ " "+ currency_from.upper() + " for "
+ str(amount_to) + " "+ currency_to.upper() + '.')
