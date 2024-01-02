import numpy as np
from my_module12 import nump as n
from my_module12 import panda_and_matl as p
import pandas as pd
# Assume you have the sales data defined here
sales_data = np.array([
    [101, 'Product_A', 150, 1200],
    [102, 'Product_B', 200, 1800],
    [103, 'Product_A', 180, 1500],
    [104, 'Product_C', 120, 1000],
    [105, 'Product_B', 250, 2000]
])

n.tampil_data(sales_data)
n.jumlah_sold(sales_data)
n.hitung_pendapatan(sales_data)
n.tampil_pilih_a(sales_data)
n.rata_rata(sales_data)

# Assume you have the sales data defined here
sales_data1 = pd.DataFrame({
    'ProductID': [101, 102, 103, 104, 105],
    'ProductName': ['Product_A', 'Product_B', 'Product_A', 'Product_C', 'Product_B'],
    'UnitsSold': [150, 200, 180, 120, 250],
    'UnitPrice': [1200, 1800, 1500, 1000, 2000]
})
p.ringkasan_data(sales_data1)
p.diagram_batang(sales_data1)
p.filter_produk(sales_data1)
p.total_pendapatan(sales_data1)
p.tambah_kolom_profit(sales_data1)
p.diagram_lingkaran(sales_data1)
