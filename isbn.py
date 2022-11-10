def isbn10to13(isbn10: str):
    isbn10_list = [9, 7, 8] + [int(x) for x in list(isbn10[0:len(isbn10)-1])]   
    isbn10_list_prod = []
    for i, x in enumerate(isbn10_list):
        if (i % 2 == 0):
            isbn10_list_prod.append(x * 1)
        else:
            isbn10_list_prod.append(x * 3)

    total = sum(isbn10_list_prod)        
    total_mod = total % 10
    check_digit = 0 if total_mod == 0 else 10 - total_mod
    isbn10_list.append(check_digit)
    isbn10 = ''.join([str(x) for x in isbn10_list])
    return isbn10
