import re

# ca?e
# caae, cabe, cace, cade, ...

p = re.compile("ca.e")  
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ se($) : 문자열의 끝 > case, base (o) | face (x)

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열 반환
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않았습니다.")


"""
m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m) # care
"""

"""
m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인 
print_match(m) # care
"""

"""
lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst) # ['care', 'cafe']
"""



# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ se($) : 문자열의 끝 > case, base (o) | face (x)