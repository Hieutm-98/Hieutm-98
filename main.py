import streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Tỷ giá USD/VND tại Ngân hàng VCB giai đoạn 2014 - 2019")
st.header("Tỷ giá USD/VND là gì")
st.text("Tỷ giá USD/VND là tỷ giá hối đoái giữa đồng Đô la Mỹ (USD) và đồng Việt Nam Đồng \n(VND). Nó cho biết giá trị của một đơn vị tiền tệ USD so với tiền tệ VND. Tỷ giá\nnày thường được sử dụng để đo lường giá trị tiền tệ và tính toán giá trị giao dịch\nquốc tế.Tỷ giá USD/VND thường biến đổi hàng ngày dựa trên thị trường hối đoái quốc\ntế và có thể ảnh hưởng đến nhiều khía cạnh của nền kinh tế, bao gồm giá cả hàng hóa,\nlãi suất, và việc nhập khẩu và xuất khẩu của một quốc gia.")

duong_dan_excel = r'C:\Users\admin\Desktop\Tygia_USDVND.xlsx'

data = pd.read_excel(duong_dan_excel)
data.index = data.index + 1
data['Date'] = data['Date'].dt.date
st.header('Bảng tỷ giá USD/VND tại Ngân hàng VCB giai đoạn 2014 - 2019')

st.write(data)

st.header('Biểu đồ tỷ giá USD/VND tại Ngân hàng VCB giai đoạn 2014 - 2019')
fig, ax = plt.subplots()
ax.plot(data['Date'], data['Cash'], label='Tiền mặt')
ax.plot(data['Date'], data['Transfer'], label='Chuyển khoản')
ax.plot(data['Date'], data['Sell'], label='Bán ra')

plt.xlabel('Thời gian')
plt.ylabel('Giá trị')
plt.title('Biểu đồ tỷ giá USD/VND tại VCB')

plt.legend()

plt.xticks(rotation=45)

st.pyplot(fig)

ngay_bat_dau = st.date_input('Chọn ngày bắt đầu', min(data['Date']))
ngay_ket_thuc = st.date_input('Chọn ngày kết thúc', max(data['Date']))

chon_gia_tri = st.multiselect('Chọn giá trị', data.columns[1:])

data_filtered = data[(data['Date'] >= ngay_bat_dau) & (data['Date'] <= ngay_ket_thuc)]

if chon_gia_tri:
    data_filtered = data_filtered[['Date'] + chon_gia_tri]

col1, col2 = st.columns(2)

with col1:
    st.write(data_filtered)

with col2:
    if not data_filtered.empty:
            data_filtered.set_index('Date', inplace=True)
            st.line_chart(data_filtered)

    else:
        st.write('Không có dữ liệu để hiển thị.')


