v="aeiouAEIOU"
s="ave"
print("Input  string : ",s) 
for i in v:
    if(i in s):
        s=s.replace(i,"")
print(s)
