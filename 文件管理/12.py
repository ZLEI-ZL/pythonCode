with open('123.txt', 'a+') as fo:
    try:
        fo.seek(0,0)
        js = fo.read()

        print(js)

        if js == '':
            print('456')
        else:
            print('123')
    finally:
        fo.close()