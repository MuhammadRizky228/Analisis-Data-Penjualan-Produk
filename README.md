# Analisis-Data-Penjualan-Produk
Muhammad Rizky_12030122140228
Berikut adalah interpretasi dari data yang telah dianalisis dan divisualisasikan:

### Tabel Penjualan
**Kolom:**
- `Tanggal`: Tanggal penjualan produk.
- `Produk`: Nama produk yang dijual.
- `Jumlah`: Jumlah produk yang terjual.
- `Harga`: Harga per unit produk.

**Tabel Penjualan:**
| Tanggal     | Produk   | Jumlah | Harga  |
|-------------|----------|--------|--------|
| 2023-06-01  | Produk_A | 10     | 10000  |
| 2023-06-02  | Produk_B | 20     | 20000  |
| 2023-06-03  | Produk_C | 30     | 30000  |
| 2023-06-04  | Produk_D | 40     | 40000  |

### Tabel Pelanggan
**Kolom:**
- `Pelanggan_ID`: ID unik pelanggan.
- `Nama`: Nama pelanggan.
- `Email`: Alamat email pelanggan.
- `Telepon`: Nomor telepon pelanggan.

**Tabel Pelanggan:**
| Pelanggan_ID | Nama      | Email             | Telepon      |
|--------------|-----------|-------------------|--------------|
| 1            | John Doe  | john@example.com  | 08123456789  |
| 2            | Jane Doe  | jane@example.com  | 08198765432  |
| 3            | Alice     | alice@example.com | 08123455678  |
| 4            | Bob       | bob@example.com   | 08198765321  |

### Tabel Transaksi
**Kolom:**
- `Transaksi_ID`: ID unik transaksi.
- `Pelanggan_ID`: ID pelanggan yang melakukan transaksi.
- `Produk`: Nama produk yang dibeli.
- `Tanggal`: Tanggal transaksi.

**Tabel Transaksi:**
| Transaksi_ID | Pelanggan_ID | Produk   | Tanggal    |
|--------------|--------------|----------|------------|
| 101          | 1            | Produk_A | 2023-06-01 |
| 102          | 2            | Produk_B | 2023-06-02 |
| 103          | 3            | Produk_C | 2023-06-03 |
| 104          | 4            | Produk_D | 2023-06-04 |

### Interpretasi Visualisasi

1. **Histogram: Distribusi Jumlah Produk Terjual**

    Histogram menunjukkan distribusi jumlah produk yang terjual. Distribusi ini penting untuk memahami variasi penjualan harian.

    ![Distribusi Jumlah Produk Terjual](attachment:histogram.png)

    - Sebagian besar penjualan berada di kisaran 10 hingga 40 unit per hari.
    - Puncak distribusi menunjukkan jumlah penjualan terbanyak ada pada nilai tertentu, menunjukkan produk-produk dengan penjualan yang sangat baik.

2. **Bar Chart: Pendapatan per Produk**

    Bar chart ini menunjukkan pendapatan dari masing-masing produk. 

    ![Pendapatan per Produk](attachment:bar_chart.png)

    - Produk D memberikan pendapatan tertinggi sebesar Rp1,600,000.
    - Produk C memberikan pendapatan sebesar Rp900,000.
    - Produk B memberikan pendapatan sebesar Rp400,000.
    - Produk A memberikan pendapatan sebesar Rp100,000.
    
    Pendapatan setiap produk meningkat seiring dengan harga dan jumlah yang terjual.

3. **Pie Chart: Proporsi Pendapatan dari Masing-masing Produk**

    Pie chart ini menunjukkan proporsi pendapatan dari masing-masing produk.

    ![Proporsi Pendapatan](attachment:pie_chart.png)

    - Produk D menyumbang bagian terbesar dari total pendapatan.
    - Produk A menyumbang bagian terkecil dari total pendapatan.
    - Proporsi ini memberikan gambaran visual tentang kontribusi masing-masing produk terhadap total pendapatan.

4. **Scattergraph: Hubungan antara Jumlah dan Harga Produk**

    Scattergraph ini menunjukkan hubungan antara jumlah produk yang terjual dan harga per unit.

    ![Hubungan antara Jumlah dan Harga Produk](attachment:scattergraph.png)

    - Terdapat korelasi positif antara jumlah produk yang terjual dan harga per unit.
    - Produk dengan harga lebih tinggi cenderung memiliki jumlah penjualan lebih tinggi, meskipun ini mungkin bervariasi tergantung pada faktor-faktor lain seperti permintaan pasar dan strategi pemasaran.

![Figure_1](https://github.com/MuhammadRizky228/Analisis-Data-Penjualan-Produk/assets/167239200/5afe4570-d301-483e-a34a-33f027847392)


### Kesimpulan
1. **Pendapatan Total**: Total pendapatan dari penjualan produk adalah Rp3,000,000.
2. **Pelanggan Aktif**: Semua pelanggan dalam dataset melakukan transaksi setidaknya sekali, dengan total pelanggan unik sebanyak 4 orang.
3. **Produk Terpopuler**: Produk D adalah yang paling populer berdasarkan jumlah penjualan dan pendapatan.
4. **Tanggal Penjualan Tertinggi**: Penjualan tertinggi terjadi pada tanggal 2023-06-04, dimana Produk D terjual sebanyak 40 unit.

Dengan analisis ini, dapat disimpulkan bahwa strategi penjualan yang fokus pada produk dengan permintaan tinggi dan harga lebih tinggi dapat memberikan pendapatan yang lebih besar. Juga, memonitor tren penjualan harian dan pola pembelian pelanggan dapat membantu dalam perencanaan inventaris dan strategi pemasaran.
