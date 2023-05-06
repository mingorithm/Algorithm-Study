num=int(input())
for i in range(1,num+1): # 반복만큼 계산
    text=list(input())# 값넣음
    result=0
    for y in text:
        if y =="(":  
            result+=1
        elif y ==")":
            result-=1
        if result <0: # 애초에 -1 로 시작하면 결국엔 ) 2번째 케이스에서 이상해짐
            print("NO")
            break
    if result ==0:  # 0일경우 가로가 완성된 것 
        print("YES")
    elif result > 0: # 이거 안하면 걸림 ...
        print("NO")
        ################################
#초기
        num=int(input())
x=0
# while num>i:
for i in range(1,num+1): # 반복만큼 계산
    text=list(input())# 값넣음
    print(text)
    for y in text:
        if y =="(":
            result+=1
        if (text[0]=="(") and (text[-1]==")"):
            text.pop(0)
            text.pop(-1)
            x=x+1
            print(text)
            print(x)
        if len(text)==1:
            break
    if x==num:
        print("YES")
        print(x)
        print(text)
    else:
        print(x)
        print("No")
        print(text)
# print(x)
