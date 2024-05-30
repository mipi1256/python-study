
# 모듈 내에 존재하는 변수, 함수, 클래스 등을 직접 임포트 하는 방법

from math import factorial, gcd
import statistics as stats

print(factorial(3))
print(gcd(12, 18))

li = [34, 55, 12, 33, 55, 66, 99]
print(f'평균: {stats.mean(li)}')
print(f'분산: {stats.variance(li)}')
print(f'표준편차: {stats.stdev(li)}')

# 위에서 알려드린 두 가지 개념을 합쳐서도 사용이 가능합니다.
from math import factorial as fac
print(fac(8))


































