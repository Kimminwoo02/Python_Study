

s = ['hello']; del s[0]
print(s)

s1= 0
s2 = 0
s3 = 0
s4= 20
s5 =0
sum =0
s1 = s1+10;
for v in range(1,6,2):
        s2 =s2 +v;
        s3=s2+s4;
sum = sum+s1+s2+s3+s4;
print("sum:"+str(sum));


s=[10,20,30,40,50,60,70,80,90,100]
r=s[-9:len(s)-1:]
print(r)
a= tuple(range(-10,10,3))
print(a)

a = [[0 for s in range(3)] for v in range(3)]
print(a)

s1= 0

s2 = 0
s3 = 0
s4= 20
s5 =0
sum =0
s1 = s1+10;
v= 1
while v <10:
    s2 = s2+v;
    s3 = s2+s4;
    v = v+2;
sum = sum+s1+s2+s3+s4;
print("sum:"+str(sum));


s=[10,20,30,40,50,60,70,80,90,100]
a=s[len(s)-6]
print(a)