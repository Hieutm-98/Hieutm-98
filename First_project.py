import streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Test ứng dụng chạy trên Streamlit với dữ liệu bất kỳ")
st.header("Phân Tích Dữ Liệu Bán Hàng")

@st.cache
def load_data():
    data = pd.read_csv("sales_data.csv")  # Thay đổi tên tệp CSV nếu cần
    return data

data = load_data()

st.subheader("Dữ Liệu Bán Hàng")
st.write(data)

st.subheader("Biểu Đồ Trực Quan")
chart_type = st.selectbox("Chọn loại biểu đồ:", ["Bar Chart", "Line Chart", "Scatter Plot"])

if chart_type == "Bar Chart":
    st.bar_chart(data)

elif chart_type == "Line Chart":
    st.line_chart(data)

else:
    st.scatter_chart(data)

st.subheader("Phân Tích Kỹ Thuật")

average_sales = data["Sales"].mean()
total_sales = data["Sales"].sum()

st.write(f"Trung bình doanh số bán hàng: ${average_sales:.2f}")
st.write(f"Tổng doanh số bán hàng: ${total_sales:.2f}")
