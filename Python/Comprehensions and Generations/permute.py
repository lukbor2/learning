#Check permute.txt for an explanation about how permute1 works.

def permute1(seq):
    if not seq:
        print('empty sequence')
        return [seq] #empty list
    else:
        res=[]
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:] # Delete current node
            for x in permute1(rest):   # Permute the others
                print('current seq: ', seq)
                res.append(seq[i:i+1] + x) # Add node at front
        return res

#same results using function generations
def permute2(seq):
    if not seq:
        yield [seq]
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x
        
s = [1,2,3]
r = permute1(s)
print('Result from permute1: ', r)

r= permute2(s)
print('Result from permute2: ', list(r))