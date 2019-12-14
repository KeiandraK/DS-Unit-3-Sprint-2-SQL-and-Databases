{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = sqlite3.connect('northwind_small (2).sqlite3')\n",
    "curs = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "# THe 10 most exspensive items\n",
    "def most_exp_item():\n",
    "    q1 = ''' SELECT ProductName, UnitPrice, SupplierID\n",
    "    FROM Product \n",
    "    ORDER BY UnitPrice DESC \n",
    "    LIMIT 10'''\n",
    "    curs.execute(q1)\n",
    "    return curs.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Côte de Blaye', 263.5, 18),\n",
       " ('Thüringer Rostbratwurst', 123.79, 12),\n",
       " ('Mishi Kobe Niku', 97, 4),\n",
       " (\"Sir Rodney's Marmalade\", 81, 8),\n",
       " ('Carnarvon Tigers', 62.5, 7),\n",
       " ('Raclette Courdavault', 55, 28),\n",
       " ('Manjimup Dried Apples', 53, 24),\n",
       " ('Tarte au sucre', 49.3, 29),\n",
       " ('Ipoh Coffee', 46, 20),\n",
       " ('Rössle Sauerkraut', 45.6, 12)]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "most_exp_item()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Average of the hiring age\n",
    "def avg_age():\n",
    "    q2 = '''\n",
    "    SELECT AVG\n",
    "    (HireDate - BIrthDate)\n",
    "    FROM Employee\n",
    "    '''\n",
    "    curs.execute(q2)\n",
    "    return curs.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(37.22222222222222,)]"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg_age()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add supp names to the top 10\n",
    "def sup_names():\n",
    "    q3 = \"\"\"SELECT\n",
    "    Product.ProductName AS \"ProductName\",\n",
    "    Product.UnitPrice AS Price,\n",
    "    SUpplier.CompanyName AS \"SupplierName\"\n",
    "    FROM Product, Supplier\n",
    "    WHERE Product.SUpplierId = Supplier.ID\n",
    "    ORDER BY UnitPrice DESC\n",
    "    LIMIT 10\n",
    "    \"\"\"\n",
    "    curs.execute(q3)\n",
    "    return curs.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),\n",
       " ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),\n",
       " ('Mishi Kobe Niku', 97, 'Tokyo Traders'),\n",
       " (\"Sir Rodney's Marmalade\", 81, 'Specialty Biscuits, Ltd.'),\n",
       " ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),\n",
       " ('Raclette Courdavault', 55, 'Gai pâturage'),\n",
       " ('Manjimup Dried Apples', 53, \"G'day, Mate\"),\n",
       " ('Tarte au sucre', 49.3, \"Forêts d'érables\"),\n",
       " ('Ipoh Coffee', 46, 'Leka Trading'),\n",
       " ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sup_names()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Finding the largest category\n",
    "def largest_category():\n",
    "    q4 = \"\"\"\n",
    "    SELECT CategoryName\n",
    "    FROM Category\n",
    "    WHERE Id = (\n",
    "    SELECT Product.CategoryId\n",
    "    FROM Product\n",
    "    GROUP BY Product.CategoryId\n",
    "    ORDER BY COUNT(Product.ProductName)DESC\n",
    "    LIMIT 1)\n",
    "    \"\"\"\n",
    "    curs.execute(q4)\n",
    "    return curs.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Confections',)]"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "largest_category()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
