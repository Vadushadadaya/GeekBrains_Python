def num_translate(a):
    d = {'zero':'ноль', 'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}
    if a[0].isupper():
        print(d.get(a.lower()).capitalize())
    else:
        print(d.get(a))
num_translate(input())