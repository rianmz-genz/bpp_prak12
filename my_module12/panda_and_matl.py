import matplotlib.pyplot as plt

def ringkasan_data(sales_data):
    summary_statistics = sales_data.describe()
    print("Ringkasan Statistik dari Data Penjualan:")
    print(summary_statistics)

def diagram_batang(sales_data):
    sales_data.plot(kind='bar', x='ProductName', y='UnitsSold', legend=False)
    plt.title('Jumlah Produk yang Terjual untuk Setiap Produk')
    plt.xlabel('Nama Produk')
    plt.ylabel('Jumlah Produk Terjual')
    plt.show()

def filter_produk(sales_data):
    product_c_data = sales_data[sales_data['ProductName'] == 'Product_C']
    print("\nData penjualan untuk 'Product_C':")
    print(product_c_data)

def total_pendapatan(sales_data):
    product_c_data = sales_data[sales_data['ProductName'] == 'Product_C']
    total_revenue_product_c = product_c_data['UnitsSold'] * product_c_data['UnitPrice']
    total_revenue_product_c = total_revenue_product_c.sum()
    print("\nTotal Pendapatan untuk 'Product_C': $", total_revenue_product_c)

def tambah_kolom_profit(sales_data):
    sales_data['Profit'] = sales_data['UnitsSold'] * (sales_data['UnitPrice'] - 500)

def diagram_lingkaran(sales_data):
    total_profit = sales_data['Profit'].sum()
    profit_contribution = sales_data.groupby('ProductName')['Profit'].sum() / total_profit * 100
    profit_contribution.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Kontribusi Profit Setiap Produk Terhadap Total Profit')
    plt.axis('equal')
    plt.show()
