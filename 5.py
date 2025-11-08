input = '''58:5,3,7,8,9,10,4,5,7,8,8'''
id,nums = input.split(':')
l,m,r = 'l','m','r'
fb = {}
for n in nums:
    placed = False
    for i in range(len(fb)):
        if not fb[i][l] and int(n) < int(fb[i][m]):
            fb[i][l] = n
            
        
    

