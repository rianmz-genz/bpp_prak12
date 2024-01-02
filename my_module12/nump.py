import numpy as np

def tampil_data(sales_data):
    print("Data Penjualan:")
    print(sales_data)

def jumlah_sold(sales_data):
    total_products_sold = len(np.unique(sales_data[:, 1]))
    print("\nJumlah produk yang terjual:", total_products_sold)

def hitung_pendapatan(sales_data):
    total_revenue = np.sum(sales_data[:, 2].astype(int) * sales_data[:, 3].astype(int))
    print("Pendapatan total dari semua produk: $", total_revenue)

def tampil_pilih_a(sales_data):
    product_a_data = sales_data[sales_data[:, 1] == 'Product_A']
    print("\nData penjualan untuk 'Product_A':")
    print(product_a_data)

def rata_rata(sales_data):
    unique_products = np.unique(sales_data[:, 1])
    average_price_per_unit = []

    for product in unique_products:
        product_data = sales_data[sales_data[:, 1] == product]
        total_units_sold = np.sum(product_data[:, 2].astype(int))
        total_revenue_product = np.sum(product_data[:, 2].astype(int) * product_data[:, 3].astype(int))
        average_price = total_revenue_product / total_units_sold
        average_price_per_unit.append((product, average_price))

    print("\nRata-rata harga per unit untuk setiap produk:")
    for product, average_price in average_price_per_unit:
        print(f"{product}: ${average_price:.2f}")
