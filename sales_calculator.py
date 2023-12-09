def salesCalc2(prod, qty):
    
    sp = ''
    tSales = ''
    if prod in prodDict['beverages']:
        sp = bevPriceDict[prod]
        #print('this is the selling price',sp)
        tSales = sp * qty
        #return tSales
   
    if prod in prodDict['phoneAcces']:
        sp = pAccDictt[prod]
        tSales = sp * qty
        #return tSales        
    if prod in prodDict['toiletries']:
        sp = toiPriceDict[prod]
        tSales = sp * qty
        #return tSales        
    if prod in prodDict['pastry']:
        sp = pastPriceDict[prod]
        tSales = sp * qty
        #return tSales        
    if prod in prodDict['cosmetics']:
        sp = cosPriceDict[prod]
        tSales = sp * qty
    return [sp, tSales]        

def salesFunc2():
    
    itemList = input('list all items bought seperated by comma: ')
    itemQty = input('list each item quantity bought seperated by comma: ')
    salesDict = dict()
    prods = itemList.split(',') 
    qtyList = itemQty.split(',')
    qtys = []
    for qty in qtyList:
        qtys.append(float(qty))
    print(prods)  
    print(qtys)
    for p  ,q in zip(prods,qtys ):
        print(p,q)
        pTSales = salesCalc2(p, q)
        print(pTSales)
        unitPrice = pTSales[0]
        totalSale = pTSales[1]
        salesDict[p]= [p, q, unitPrice, totalSale]
        #salesDict[p]= [q,  totalSale]
    return salesDict