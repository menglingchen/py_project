import streamlit as st
import pandas as pd
import seaborn as sns
from bokeh.plotting import figure, show
import numpy as np
import datetime


st.markdown('### 三次方计算器 :sunglasses:')
x = st.slider('输入一个数字')
st.write(x, '的三次方为：', x**3)
st.markdown('> Streamlit挺好''')


"""Use checkboxes to show/hide data"""
if st.checkbox('显示dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


# """Use a selectbox for options"""
# option = st.selectbox(
#     'Which number do you like best?',
#      df['机构'])

# 'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


# tf = pd.DataFrame(
# np.random.randn(10, 5),
# columns=('col %d' % i for i in range(5)))
# # st.dataframe(tf.style.highlight_max(axis=0))
# # st.table(tf)

# st.line_chart(tf)


"""Bokeh"""
import streamlit as st
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)

import streamlit as st
import plotly.figure_factory as ff
import numpy as np
# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
# Group data together


hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']


# Create distplot with custom bin_size
fig = ff.create_distplot(
hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=True)


d = st.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)
    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)
    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe.head(10))

