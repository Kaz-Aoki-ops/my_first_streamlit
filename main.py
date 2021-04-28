import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
  '１列目':[1, 2, 3, 4],
  '２列目':[10, 20, 30, 40],
})

st.write(df)

st.dataframe(df, width=500, height=200) #dataframeメソッドはinteractiveかつwidthやheightを指定できる

st.dataframe(df.style.highlight_max(axis=0), width=300, height=100) #最大の値をhighlight表示する axis=0:列 axis=1:行

st.table(df) #staticな表を作りたい時はtableメソッドを使う

#magiccommand markdown記法
"""
# 章

## 節

### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

```

"""

#chart
# 20行3列のランダムな行列を生成
df = pd.DataFrame(
  np.random.rand(20, 3),
  columns=['a', 'b', 'c']
)
#グラフを表示
st.line_chart(df) #折れ線グラフ

st.area_chart(df) # エリアチャート

st.bar_chart(df) # 棒グラフ


#mapを表示する

df = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon'] #lat=緯度, lon=経度
)
# st.write(df)
st.map(df)

#画像を表示する
st.write('Display Image')

img = Image.open('sample.jpg')
st.image(img, caption='yui aragaki', use_column_width=True)

#チェックボックス チェックが入っているときに画像を表示する。
if st.checkbox('Show Image'):
  img = Image.open('sample.jpg')
  st.image(img, caption='yui aragaki', use_column_width=True)

#セレクトボックス
option = st.selectbox(
  'あなたが好きな数字を教えてください',
  list(range(1, 11))
)

'あなたの好きな数字は、' ,option, 'です'

#テキスト入力
st.write('Interactive Wigets')

text = st.text_input('あなたの趣味を教えてください')

'あなたの趣味は', text, 'です'

# #スライダー
# condition = st.slider('あなたの調子は？', 0, 100, 50)

# 'あなたのコンディション:', condition

#サイドバー .sidebarでサイドバーに表示できる
condition = st.sidebar.slider('あなたの調子は？', 0, 100, 50)

'あなたのコンディション:', condition

#２カラム
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右からむ')

#expander
expander = st.beta_expander('問いあわせ')
expander.write('問い合わせ内容を書く')

#プログレスバー
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i + 1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'Done!!'

