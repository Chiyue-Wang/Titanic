import streamlit as st
import joblib
import numpy as np

# 加载模型
@st.cache_resource
def load_model():
    return joblib.load("titanic_model.pkl")

model = load_model()

st.title("Titanic Survival Prediction")

st.subheader("Please enter the passenger information for survival probability prediction:")

# 输入控件
pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100, value=24)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0)

# 输入编码
sex_encoded = 1 if sex == "male" else 0
X = np.array([[pclass, sex_encoded, age, fare]])

if st.button("Forecast survival probability"):
    prob = model.predict_proba(X)[0][1]  # [0][1] 表示生存的概率

    st.success(f"Forecast survival probability is：{prob*100:.2f}%")
