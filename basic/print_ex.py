'''
* 표준 출력 함수 print()
()안에 출력하고 싶은 변수, 리터럴 상수, 수식 등을 적으면
터미널에 텍스트를 출력합니다.
'''

# 출력할 데이터가 여러 개라면 괄호 안에 출력할 데이터들을
# 콤마로 나열해서 작성합니다.
# 여러 개의 값들을 공백과 함께 가로로 나란히 출력합니다.

dog = '멍멍이'
cat = '야옹이'
print(dog, cat, '좋아요~')

print('-----------------------------------------------')

'''
- print함수 내부에는 sep이라는 속성이 존재합니다.
- sep은 separator의 약자로 구분자 라고도 부릅니다.
- sep 속성은 기본값이 ' '(공백 문자열)로 지정되어 있으며
 만약 변경을 원한다면 sep 속성을 직접 작성하여 변경합니다.
'''
# print(dog, cat, '좋아요~', sep=' ') -> print 함수의 기본값
print(dog, cat, '좋아요~', sep='')

'''
- end 속성은 데이터 출력 이후 맨 끝에 포함할 문자를
지정하는 용도입니다.
- 기본값은 '\n'이 지정되어 있기 때문에
print 함수를 쓸 때마다 자동으로 줄 개행이 되는 것처럼 보이는 겁니다.
'''

# print(dog, cat, '좋아요', end='\n) -> 기본값
print(dog, cat, '좋아요', end='!!!')
print('이 문장은 줄 개행이 되어서 나올까?')


print(dog, cat, '좋아요',  end='', sep='->')
# print(end='', sep='->', dog, cat, '좋아요') (X) end and sep should be at the end of the print
print('야호~')


