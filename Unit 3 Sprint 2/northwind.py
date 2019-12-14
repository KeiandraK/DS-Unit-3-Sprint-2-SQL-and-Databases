import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# THe 10 most exspensive items
def most_exp_item():
    q1 = ''' SELECT ProductName, UnitPrice, SupplierID
    FROM Product 
    ORDER BY UnitPrice DESC 
    LIMIT 10'''
    curs.execute(q1)
    return curs.fetchall()

most_exp_item()

# Average of the hiring age
def avg_age():
    q2 = '''
    SELECT AVG
    (HireDate - BIrthDate)
    FROM Employee
    '''
    curs.execute(q2)
    return curs.fetchall()

avg_age()

# Add supp names to the top 10
def sup_names():
    q3 = """SELECT
    Product.ProductName AS "ProductName",
    Product.UnitPrice AS Price,
    SUpplier.CompanyName AS "SupplierName"
    FROM Product, Supplier
    WHERE Product.SUpplierId = Supplier.ID
    ORDER BY UnitPrice DESC
    LIMIT 10
    """
    curs.execute(q3)
    return curs.fetchall()

sup_names()

#Finding the largest category
def largest_category():
    q4 = """
    SELECT CategoryName
    FROM Category
    WHERE Id = (
    SELECT Product.CategoryId
    FROM Product
    GROUP BY Product.CategoryId
    ORDER BY COUNT(Product.ProductName)DESC
    LIMIT 1)
    """
    curs.execute(q4)
    return curs.fetchall()

largest_category()

