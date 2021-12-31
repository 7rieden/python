#Chapter09
#파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드: w, 추가 모드: a, 
# 텍스트 모드 t, 바이너리 모드 b
# 상대 경로('../, ./')
# 절대 경로('C:\Django\example..')

# To read files
# example1

f = open('7rieden/python/python_lv1/resource/it_news.txt', 'r', encoding = 'UTF-8')

# 속성 확인
print(dir(f))

# 인코딩 확인
print(f.encoding)

# 파일 이름
print(f.name)

#모드 확인
print(f.mode)
cts = f.read()
print(cts)

#반드시 close
f.close

# Example2

with open('7rieden/python/python_lv1/resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# Example3
# read() : 전체 읽기, read(10) : 10Byte

with open('7rieden/python/python_lv1/resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20) # Cursor 존재
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)

print()


# Example4
# readline : 한 줄 씩 읽기

with open('7rieden/python/python_lv1/resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    line = f.readline()
    print(line)


# Example5
# readlines : 전체 읽고 라인 단위 리스트로 저장

with open('7rieden/python/python_lv1/resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()