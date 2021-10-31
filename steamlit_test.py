import streamlit as st
import pandas as pd
import time
import numpy as np

st.title('部署成功了！')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.button("Re-run")