def alternatingSums(a):
    out = [0, 0]
    count = 0
    for i in a:
        if count % 2 == 0:
            out[0] += i
        else:
            out[1] += i
        count+=1
    return out
