import random
import hashlib
def keygen():
    s = random.randint(2**165, (2**166)-1)
    k = input("type a pwd: ")
    k = "asd"
    k = int(hashlib.sha1(k.encode("utf-8")).hexdigest(),16)
    p = int(s/k)
    so = open("key.sec", "w" , encoding="utf-8")
    so.write(str(s))
    so.close()
    po = open("key.pwd", "w" , encoding="utf-8")
    po.write(str(k))
    po.close()
    ko = open("key.pub", "w" , encoding="utf-8")
    ko.write(str(p))
    ko.close()
    print("ok")
keygen()
