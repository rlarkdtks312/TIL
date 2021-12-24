# 딕셔너리는 어떻게 만들까?
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# key와 value의 쌍 여러 개가 {}로 둘러싸여 있다. 각각의 요소는 key : value 형태로 이루어져 있고 쉼표로 구분된다.

# 생성 예시들
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a = {1: 'hi'} # 정수 값을 키로 취할 수 있다.
a = { 'a': [1,2,3]}

# 딕셔너리 쌍 추가, 삭제하기
a = {1: 'a'}
a[2] = 'b' # 2를 키로하고 'b'로하여 추가한다.
a
a['name'] = 'pey' 
a
a[3] = [1,2,3]
a

# 딕셔너리 요소 삭제하기
del a[1] # key로 접근해서 삭제하기 {key:value} 쌍이 같이 삭제된다.
a

# 딕셔너리에서 key 사용해 value 얻기 / 인덱스를 이용하는게 아닌 키를 이용하는 것을 기억하자
grade = {'pey': 10, 'julliet': 99}
grade['pey']
grade['julliet']
a = {1:'a', 2:'b'}
a[1]
a[2]
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
dic['name']
dic['phone']
dic['birth']

# 딕셔너리 만들 떄 주의할 사항
a = {1:'a', 1:'b'} # 키값은 고유하기에 동일한 키가 존재하면 무시된다. 뒤에 추가한 key:value 쌍이 남는다.
a

a = {[1,2] : 'hi'} # key 값으론 list를 사용할 수 없다 하지만 tuple은 사용가능하고 이유는 불변한다는 점이다.

# 딕셔너리 관련 함수들
# key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys() # dict_keys(['name', 'phone', 'birth']) 반환되고 리스트를 사용하는 것과 유사하게 사용가능하지만 append, insert, pop, remove, sort 함수는 수행할 수 없다.

# dict_keys 객체를 리스트로 변환하기
list(a.keys())

# value 리스트 만들기(values)
a.values()

# dict_values 객체를 리스트로 변환하기
list(a.values())

# key, value 쌍 얻기(items)
a.items() # key : value 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.


# key: value 쌍 모두 지우기(clear)
a.clear()
a

# key로 value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a.get('name')
a.get('phone')
print(a.get('ulsan_kim')) # a[key]와 다른점은 None을 돌려준다는 차이가 있다.

a.get('foo', 'bar1234') # 딕셔너리 안에 찾는 key가 없는 경우에 미리 정해 둔 디폴트 값을 가져오게 할 수 있다.

# 해당 keys가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
'name' in a  # True
'email' in a # False