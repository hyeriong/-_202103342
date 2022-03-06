Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>### Heading3 ###
##프로그래밍이란?
# programming : 프로그래밍 언어를 사용하여 프로그램을 개발하는 것
# program : 일련의 작업을 자동화하는 것
# python : 프로그래밍 언어 중 하나. 인간이 컴퓨터에게 작업을 명령하기 위해 사용하는 컴퓨터가 이해할 수 있는 언어

## Ch2. Data : Types, Values, Variables, and Names
a = 2
# a에 2를 대입했다.
a

a == 2
# a는 2와 같다. a는 2다.

#(markdown = m+)
# 변수 \variable(i,e,a): 측정 값을 저장하는 공간
# 값 \value : 2
# 자료형 \type: 2가 어떤 타입인가? 데이터의 형태(i.e., integer, int타입)
# 할당하다\ assign: 2를 a에 넣는 과정
# a가 2다. -> a==2(a는 2와 같다.)

##변수의 타입
# boolean\ 불리언 : True, False (bool)
# integer\ 정수 : 1,2,3,4,... (int)
# floating point number\ 부동 소수점 : 1.0,2.0,0.45,... (float)
# string\ 문자열 : 'apple',"apple" (str)

num = 4
print(num)
type(num)

type(a==2)

name = 'my name'
print(name)
type(name)

my_name  # 변수명으로 인식, 없는 변수 -> 에러

#single quote 안에 single quote를 문자로 인식하는 방법
#ex. 'I'm Sam.'
# 1. 슬래쉬 사용
print('I\'m Sam.')
# 2. 더블 quote로 바꾸기
print("I'm Sam.")

##변수명 정하기
# 소문자, 대문자, 숫자, 언더바(_)를 사용한다.
  # 예: name, my_name, NAME, Name, name3 (대문자는 특별한 용도가 있어 가능한 한 쓰지 않는 게 좋음.)
  # 불가능한 예: my-name, 3name
#변수명으로 사용할 수 없는 케이스
  # 1. 숫자로 시작할 수 없다.
  # 2. 예약어는 사용할 수 없다.

name = 'lee'
name

3name = 'kim'  # 숫자는 변수명 맨 앞에 올 수 없다.
def = 'Hwang'  # 예약어는 변수명으로 사용할 수 없다.

help("keywords")

# 주의할 점 (특별한 용도가 있어서 일반적으로 사용하지 않는 변수명 타입)
  # 1. 언더바로 시작하는 변수명 예: _name
  # 2. 언더바가 2개 있는 변수명 예: __name__
  # 3. 대문자로 시작하는 변수명 예: Car
  # 4. 전체가 대문자인 변수명 예: CAR

# 좋은 변수명 : 이름만으로도 용도를 확실히 알 수 있는 변수명

# number != Number
word1 = 'number'
word2 = 'Number'
word1 == word2  # 대소문자 구분한다.
word1 != word2

##할당하기
# 수학에서는 =가 양변이 같음을 의미하는데, 프로그램에서는 할당을 의미한다.
  # 예: name = 'lee' -> lee라는 값을 name에 넣는 것.
# 오른쪽에 있는 모든 것은 값을 가져야 한다. ("초기화")
# 변수 타입은 따로 지정하지 않는다.

car = 'hyundai'
kia = 'kia'
truck = kia  # 없는 값이기 때문에

x = 2
y = x + 10  # name 'x' is not defined
print(x,y)

type(car)  # str

#str car = 'kia'
car = 'kia'
car
