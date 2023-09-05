def my_roman_numerals_converter(param_1):
    value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman = ""
    i = 0
    while param_1>0:
        div = param_1//value[i]
        param_1 = param_1%value[i]
        while div:
            roman = roman+symbol[i]
            div = div-1
        i=i+1
    return roman

    # if param_1 > 3000:
    #     print ("Enter number less than 3000")
    #     return