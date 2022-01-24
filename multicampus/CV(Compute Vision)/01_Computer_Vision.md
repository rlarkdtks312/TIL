## 01. 2차원 신호의 디지털화 과정

*금오공과대학교 김성영교수님 자료를 참고했음을 밝힙니다.*



- 관련 용어 정리

  - Cartesian coordinate & Polar coordinate: 데카르트 좌표, 극 좌표

  - PPI : pixel per inch

  - DPI : dots per inch

  - uint8 : unsigned interger 2**8  = 256 (영상을 표현할 때 사용)

  - float32 : 영상을 연산할 때 사용 

    

- 영상 신호의 디지털화 과정
  - sampling(표본화)
    - 원래의 신호(아날로그)는 선형(linear)적인 신호이다. 
    - 하지만 우리가 저장을 할때는 무한대로 저장을 할 수 없기에 아주 짧은 시간으로 신호를 쪼개어 저장하고 이를 sampling이라고 한다.
    - sampling 주기가 짧아지면 신호의 퀄리티는 올라가고 용량은 늘어나는 등의 상충관계가 있다.
    - picture element, pixel, pel 화소: sampling  단위
  - quantizing(양자화)
    - pixel 하나에 대한 이야기, 상이 어떻게 맺힐 것인가 하는 이야기
    - 양자화라는 것은 무한대로 이루어진 셀 수 없는 아날로그 정보를 셀 수 있을 만큼의 간격으로 만들어서 유의미한 정보만을 사용하는 것이다. 이 말은 샘플링에도 유효할 것이다.
    - 양자화는 Level 단위로 나타내는데 Level이 높을 수록(더 세밀하게 잘라서 밝기값 혹은 컬러값을 표현할수록) 원래의 영상에 가깝게 이미지가 표현되는 것을 볼 수 있다.
  - coding(부호화)
    - jpg : lossg (손실 압축)
    - png : 무손실 압축



## 02. 디지털 영상의 구조 및 유형

- 학습목표 
  - 디지털 영상(bitmap)의 표현 방법을 설명할 수 있다. 
  - 디지털 영상(bitmap)의 유형(mode)을 구분하여 설명할 수 있다



- 디지털 영상의 표현 방법
  - 영상 좌표 (x, y)
  - 행렬 위치 (r, c)
  - 두 좌표계 표현방법이 서로 뒤집혀? 있기에 조심해야한다.
  - x, y: spatial coordinates
  - I: intensity (gray level) 흑백 표현
  - I<sub>r </sub>, I<sub>g</sub>,  I<sub>b </sub> 컬러도 표현
  - dithering: 제한된 색을 이용하여 음영이나 색을 나타내는 것이며, 여러 컬러의 색을 최대한 맞추는 과정 (ex 흰색 검은색만 사용하여 회색등을 나타내는 것)
  - Halftoning: **망점**(網點)은 점을 사용하여 크기나 간격에 따라 연속 색조의 상을 따라 만드는 복사(複寫) 기법이나 점으로, 그라디언트와 같은 효과를 낸다. 색을 표현할 때  여러 dot을 이용하여 표현하는 것
  - color image -> true color image : typically 24 bit / pixel 사실적인 컬러를 표현
  - color image -> indexed color image 8bit / pixel 데이터를 줄이기 위해서 사용
    - gif같은 것이다. 영상처리할때 gif같은 건 사용하지 않는게 좋다. 만화나 움짤 같은 재미요소를 위해 사용하는 데이터이다.







