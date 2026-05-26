import streamlit as st #streamlit 라이브러리 임포트 
import numpy as np


#타이틀 텍스트 출력 
st.title('첫번째 웹 어플 만들기🐱')

"## 이건 부제목"

"""
# 비즈니스 모델 분석 

[네이버](https://www.naver.com)  
[홍익대학교](https://www.hongik.ac.kr)

이것이 일반 본문   **이것이 굵은 글씨**   *이것이 기울임 글씨* ~~이것이 취소선~~

:red[빨간색 글씨]

```python
import streamlit as st 

print("코드 블록")
```

"""

st.caption('캡션(작고 흐린 글씨로 표현됨):st.caption()')

with st.echo():
    #이 블록의 코드와 결과를 출력 
    name='Chunghun Ha'
    st.write("Hello, Streamlit", name)

st.latex('\int_a^b f(x)dx')
"$$\int_a^b f(x)dx$$"

'### :orange[이미지: st.image()]'
st.image("./data/고양이.jpg", caption="고양이", width=300)

'### :orange[동영상: st.video()]'
video_file = open("./data/산.mp4", "rb")

'### :orange[Pandas 데이터프레임]'
import pandas as pd
df = pd.DataFrame(
    {'id':[1,2,3],
     'name':['Alice','Bob','Charlie'],
     'age':[24,34,45]
     }
)

