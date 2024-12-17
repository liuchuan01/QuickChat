import streamlit as st
import completions

model_options = {
    "逆向（便宜）": ["claude-3-5-sonnet-latest", "claude-3-haiku-20240307", "claude-3-5-sonnet-20240620",
                   "claude-3-5-sonnet-20241022", "chatgpt-4o-latest", "gpt-4o-mini"],
    "管转": ["claude-3-5-sonnet-latest", "claude-3-5-haiku-20241022"],
    "直连（很贵）": ["claude-3-5-sonnet-latest", "claude-3-5-haiku-20241022", "claude-3-haiku-20240307"]
}

# Streamlit UI
st.set_page_config(layout="wide")

st.title("Quick Chat")
st.markdown("为了用Claude搭建的小工具～")
st.markdown(
    "API用的 [这个](https://yunwu.ai/register?aff=ZDXj) 。 支持**流式输出**，但有时候云雾那边会失效... 如果请求失败就换个模型再试试吧，claude-3-5-sonnet-20240620就是好用的")
st.markdown("实际上Key是**归属分组**的。所以你可以填写Key之后不选择分组**直接自定义模型**")

# 输入区
st.session_state.api_key = st.sidebar.text_input("输入你的API_KEY，确保和渠道一致")

channel = st.sidebar.radio("选择你的渠道", ["逆向（便宜）", "管转", "直连（很贵）"])

model = st.sidebar.selectbox("Select Model:", model_options[channel])

st.session_state.model = model

if st.sidebar.checkbox("我要自行输入模型名称", value=False):
    st.session_state.model = st.sidebar.text_input("确保输入有效、符合渠道的模型名")

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1, 1, 1, 1, 1, 1, 1, 1])
with col1:
    b1 = st.checkbox("1", value=False, label_visibility="hidden")
with col2:
    b2 = st.checkbox("2", value=False, label_visibility="hidden")
with col3:
    b3 = st.checkbox("3", value=False, label_visibility="hidden")
with col4:
    b4 = st.checkbox("4", value=False, label_visibility="hidden")
with col5:
    b5 = st.checkbox("5", value=False, label_visibility="hidden")
with col6:
    b6 = st.checkbox("6", value=False, label_visibility="hidden")
with col7:
    b7 = st.checkbox("7", value=False, label_visibility="hidden")
with col8:
    b8 = st.checkbox("8", value=False, label_visibility="hidden")

question = st.text_area("问题")

# 开始按钮
if st.button("Submit"):

    if b3 and not b2 and not b4 and not b1 and not st.session_state.api_key:
        if channel == "逆向（便宜）":
            # 你可以在这里偷偷写上你的KEY，自己用的时候偷个懒，通过勾选3号框不用每次填写，直连贵10倍所以不提供默认的了
            st.session_state.api_key = 'your-key'
        elif channel == "管转":
            st.session_state.api_key = 'your-key'

    if not st.session_state.api_key:
        st.error("Please enter your API key.")
    elif not question:
        st.error("Please enter a question.")
    else:
        st.markdown("### Response:\n ----")
        response_area = st.empty()  # 保留动态更新的区域

        response_text = ""
        for chunk in completions.stream_response(question, st.session_state.api_key, st.session_state.model):
            response_text += chunk
            response_area.write(response_text)
