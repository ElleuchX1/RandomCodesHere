def parenth(Start,End,numb,a=[]):
    if End == numb:
        return ''.join(a)
        
    else:
        
        if Start<numb:
            a.append('(')
            parenth(Start+1,End,numb,a)
            a.pop()
        if Start>End:
            a.append(')')
            parenth(Start,End+1,numb,a)
            a.pop()
