def time(n):
    ans= f'{(2-len(str(int((n%3600)/60))))*'0'}{(int(n/60)%60)}:{(2-len(str(n%60)))*'0'}{n%60}'
    if n>3600:
        ans = f'{(2-len(str(int((n%43200)/3600))))*'0'}{int((n%43200)/3600)}:'+ans
    return ans

