import streamlit as st
import completions

# Streamlit UI
st.set_page_config(layout="wide")

st.title("Quick Chat")
st.markdown("为了用Claude搭建的小工具～  APIKEY用的[这个](https://yunwu.ai/register?aff=ZDXj) 其实有流式输出但好像云雾那边流式也是一起返回的...")

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    b1 = st.checkbox("1", value=False, label_visibility="hidden")
with col2:
    b2 = st.checkbox("2", value=False, label_visibility="hidden")
with col3:
    b3 = st.checkbox("3", value=False, label_visibility="hidden")
with col4:
    b4 = st.checkbox("4", value=False, label_visibility="hidden")

# 输入区
api_key = st.text_input("输入你的API_KEY，确保和渠道一致")

col1, col2 = st.columns([1, 1])
with col1:
    channel = st.radio("选择你的渠道", ["逆向（便宜）", "管转", "直连（很贵）"])

with col2:
    model_options = {
        "逆向（便宜）": ["claude-3-5-sonnet-latest", "claude-3-haiku-20240307", "chatgpt-4o-latest", "gpt-4o-mini"],
        "管转": ["claude-3-5-sonnet-latest", "claude-3-5-haiku-20241022"],
        "直连（很贵）": ["claude-3-5-sonnet-latest", "claude-3-5-haiku-20241022", "claude-3-haiku-20240307"]
    }
    model = st.selectbox("Select Model:", model_options[channel])

question = st.text_area("问题")

# 开始按钮
if st.button("Submit"):

    if b3 and not b2 and not b4 and not b1 and not api_key:
        if channel == "逆向（便宜）":
            api_key = '你可以在这里偷偷写上你的KEY，自己用的时候偷个懒，通过勾选3号框不用每次填写'
        elif channel == "管转":
            api_key = '你可以在这里偷偷写上你的KEY，自己用的时候偷个懒，通过勾选3号框不用每次填写'

    if not api_key:
        st.error("Please enter your API key.")
    elif not question:
        st.error("Please enter a question.")
    else:
        st.markdown("### Response:")
        response_area = st.empty()  # 保留动态更新的区域

        response_text = ""
        for chunk in completions.stream_response(question, api_key, model):
            response_text += chunk
            response_area.markdown(response_text)
