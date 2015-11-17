def intersect(*args):
    res=[]
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break #This is a for...else construct.
            #The else is executed after the for, but only if the for terminates normally (not by a break).
        else:
            res.append(x)
    return res

s1="SPAM"
s2="SCAM"
s3="SLAM"

print(intersect(s1,s2))
print(intersect([1,2,3], (1,4)))