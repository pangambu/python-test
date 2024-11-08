def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
""" unpacking a list coins"""
print(total(*coins), "Knuts") 


coinz = {"galleons": 100, "sickles": 50, "knuts": 25}
"""unpacking a dictionary coinz"""
print(total(**coinz),"Knuts")
