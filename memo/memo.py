# つたえること
# 文字列の掛け算
x = "x"*3
print(x)

# 演算子
sum = 1+1
sub = 5-2
mul = 2*3
div = 10/2
div2 = 10/3

# 文字列の合成(format文)
print(f'{sum}, {sub}, {mul}, {div}, {div2}')

# for文を実際に使ってみよう
a = []
i=0
for i in range(0,10,2):
    a.append(i)
    print(a)

# 比較演算子 and if-else文を使おう
i=3
if(i==3):
    print(f'3です')
elif(i < 3):
    print('f{i}は3より小さい')
elif(i > 3):
    print(f'{i}は3より大きい')
elif(i >= 8):
    print(f'{i}は8以上です')

b = []
for i in range(1,11):
    b.append(i)
    
    if(i < 3):
        print(f'{i}は3より小さいです')
    elif(i==3):
        print(f'3です')
    elif(i >= 8):
        print(f'{i}は8以上です')
    elif(i > 3):
        print(f'{i}は3より大きいです')

# 論理演算子を使ってみよう
print(True and True)
print(True and False)
print(True and False)
print(True or False)
print(False or True)
print(not (True))

# for 文からbreak文で脱出しようね
i=0
while(1):
    if(i == 8):
        break
    i+=1
    print(i)

# アルゴリズムって大事だよね~~雰囲気つかむだけ~~
a = "hoge"
b = "huga"
print(f'aは{a}です。bは{b}です')
work = a
a = b
b= work
print(f'aは{a}です。bは{b}です')

# -->ひとまずmemo2をとばしてmemo3へ



