def checkinventory2(prod):
    '''
    this function will accepts a product name and check if it's available in the inventory list
    if found, it will return the current quantity in inventory

    '''

    if prod in prodDict['beverages']:
        return bevInventDict[prod]
    if prod in prodDict['phoneAcces']:
        return pAccInventDict[prod]
    if prod in prodDict['toiletries']:
        return toiInventDict[prod]
    if prod in prodDict['pastry']:
        return pastInventDict[prod]
    if prod in prodDict['cosmetics']:
        return cosInventDict[prod]
    
prodCheck = input('enter product: ')

prodCount = checkinventory2(prodCheck)
print(prodCount)
#print(f'current inventory for {prodCheck} is {prodCount}')