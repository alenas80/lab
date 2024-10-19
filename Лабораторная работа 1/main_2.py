# TODO Найдите количество книг, которое можно разместить на дискете
col_page = 100
col_string = 50
col_symbols = 25
volume_symbol = 4
volume_disk = 1.44

book = col_page * col_string * col_symbols * volume_symbol / (1024 * 1024)
col_book = volume_disk // book

print("Количество книг, помещающихся на дискету:", int(col_book))
