menu = {
    '三明治' : 50,
    '咖啡' : 40,
    '沙拉' : 30
}

def order_meal():
    total = 0
    while order:= input('請點餐 : '):
        if order in menu:
            price = menu[order]
            total += price
            print(f'{order} {price} 元，總金額{total}')
        else:
            print(f'抱歉，我們沒有供應{order}')
    print(f'今天消費的金額為 : {total}')

order_meal()