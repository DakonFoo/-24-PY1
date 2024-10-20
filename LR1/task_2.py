disk_capacity = 1.44
pages = 100
lines = 50
chars = 25
bytes = 4

disk_capacity_bytes = disk_capacity * 1024 * 1024
book_size_bytes = pages * lines * chars * bytes
book_amm = disk_capacity_bytes // book_size_bytes

print(f"Количество книг, помещающихся на дискету: {int(book_amm)}")