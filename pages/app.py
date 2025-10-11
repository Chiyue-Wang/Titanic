# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置 Seaborn 风格
sns.set_style("whitegrid")

# 设置页面标题
st.title("Titanic App by Chiyue Wang")

# 读取数据
df = pd.read_csv("train (1).csv")   # 请确保文件名和路径一致
st.write("### Titanic Dataset Preview")
st.dataframe(df)

# 创建三个并排的箱线图 (15x5)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 不同舱位的票价分布
classes = [1, 2, 3]

for i, pclass in enumerate(classes):
    sns.boxplot(
        x=df[df["Pclass"] == pclass]["Fare"],
        ax=axes[i],
        color="skyblue"
    )
    axes[i].set_title(f"Pclass {pclass}")
    axes[i].set_xlabel("Fare")
    axes[i].set_ylabel("")

# 显示图表
st.pyplot(fig)
