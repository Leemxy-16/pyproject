#sock_count = 1
#pairs = 0


def sockmerchant(ar):

    sock_count = {}
    pairs = 0
    for socks in ar:
        if socks in sock_count:
            sock_count[socks] += 1
    else :
        sock_count[socks] = 1
    for count in sock_count.values():
        pairs += count // 2
    return pairs
atry:


   arr  = input().split(",")
   print(sockmerchant(arr))
   #print(sockmerchant(arr))

except TypeError :
    print("i don't know what happened you have a trype error")
