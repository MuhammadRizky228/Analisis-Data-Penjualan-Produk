import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data_penjualan = {
    'Tanggal': [datetime(2023, 6, 1), datetime(2023, 6, 2), datetime(2023, 6, 3), datetime(2023, 6, 4)],
    'Produk': ['Produk_A', 'Produk_B', 'Produk_C', 'Produk_D'],
    'Jumlah': [10, 20, 30, 40],
    'Harga': [10000, 20000, 30000, 40000]
}

data_pelanggan = {
    'Pelanggan_ID': [1, 2, 3, 4],
    'Nama': ['John Doe', 'Jane Doe', 'Alice', 'Bob'],
    'Email': ['john@example.com', 'jane@example.com', 'alice@example.com', 'bob@example.com'],
    'Telepon': ['08123456789', '08198765432', '08123455678', '08198765321']
}

data_transaksi = {
    'Transaksi_ID': [101, 102, 103, 104],
    'Pelanggan_ID': [1, 2, 3, 4],
    'Produk': ['Produk_A', 'Produk_B', 'Produk_C', 'Produk_D'],
    'Tanggal': [datetime(2023, 6, 1), datetime(2023, 6, 2), datetime(2023, 6, 3), datetime(2023, 6, 4)]
}

# Create DataFrames
tabel_penjualan = pd.DataFrame(data_penjualan)
tabel_pelanggan = pd.DataFrame(data_pelanggan)
tabel_transaksi = pd.DataFrame(data_transaksi)

# Histogram: Distribusi jumlah produk terjual
plt.figure(figsize=(8, 6))
sns.histplot(tabel_penjualan['Jumlah'], bins=5, kde=True)
plt.title('Distribusi Jumlah Produk Terjual')
plt.xlabel('Jumlah')
plt.ylabel('Frekuensi')
plt.show()

# Bar Chart: Pendapatan per produk
tabel_penjualan['Pendapatan'] = tabel_penjualan['Jumlah'] * tabel_penjualan['Harga']
plt.figure(figsize=(8, 6))
sns.barplot(x='Produk', y='Pendapatan', data=tabel_penjualan)
plt.title('Pendapatan per Produk')
plt.xlabel('Produk')
plt.ylabel('Pendapatan')
plt.show()

# Pie Chart: Proporsi pendapatan dari masing-masing produk
plt.figure(figsize=(8, 6))
plt.pie(tabel_penjualan['Pendapatan'], labels=tabel_penjualan['Produk'], autopct='%1.1f%%', startangle=140)
plt.title('Proporsi Pendapatan dari Masing-masing Produk')
plt.show()

# Scattergraph: Hubungan antara jumlah dan harga produk
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Jumlah', y='Harga', data=tabel_penjualan, hue='Produk', s=100)
plt.title('Hubungan antara Jumlah dan Harga Produk')
plt.xlabel('Jumlah')
plt.ylabel('Harga')
plt.legend(title='Produk')
plt.show()