def exsort(li):
    result = sorted(li, key=lambda x: x.split('.')[-1])
    print(result)             
exsort(['a.txt','aslam.mkv'])
