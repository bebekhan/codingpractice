#practice with dictionaries

def dict_price_stock(prices, stock):
    """ 
    Given a dictionary of prices and stock per item,
    print in the following order per key with value from dictionaries.

    item
    price: 
    stock: 
    """
    prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

    stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

    for food in prices:
        print food
        print "price: %s" % prices[food]
        print "stock: %s" % stock[food]

return dict_price_stock(prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3},
 stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15} )

