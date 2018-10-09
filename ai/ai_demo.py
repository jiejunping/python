def wordcount(data):
    re = {}
    for i in data:
        re[i] = re.get(i,0)+1
    return re


if __name__ == "__main__":
    data = ["ab","cd","ab","d","d"]
    dic = wordcount(data);
    print("the result is %s" %(dic))