# 파일 생성 반복 코드
prefix = "BA2"
n = 8
ASCII_big = [chr(i) for i in range(65, 65+n)]
for j in range(n):
    filename = prefix + ASCII_big[j] + ".py"
    with open(filename,"w") as f:
        f.write("")
