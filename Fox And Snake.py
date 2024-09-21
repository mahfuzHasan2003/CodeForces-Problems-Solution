n, m = map(int, input().split())
dot_sign = "."
hash_sign = "#"
set_counter = 1
for i in range(n) :
    if i%2 == 0 :
        print(hash_sign * m)
    else :
        print((dot_sign*(m-1))+hash_sign if set_counter%2 != 0 else hash_sign+(dot_sign*(m-1)))
        set_counter += 1