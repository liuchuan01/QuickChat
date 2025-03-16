import streamlit as st
import completions

model_options = {
    "Anthropic": ["claude-3-5-sonnet-latest", "claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20241022",
                   "claude-3-5-haiku-20241022", "claude-3-7-sonnet-20250219-thinking", "claude-3-7-sonnet-thinking",
                   "claude-3-7-sonnet-20250219", "claude-3-7-sonnet-latest"
                   ],
    "OpenAI": ["chatgpt-4o-latest", "gpt-4o-mini", 'gpt-4.5-preview', "gpt-4.5-preview-2025-02-27",
               "o3-mini-all", "o1-mini-all", "o1-all", "o3-mini-high-all"
               ]

}

# Streamlit UI
st.set_page_config(layout="wide")

st.title("Quick Chat")
st.markdown("为了用Claude搭建的小工具～，支持**流式输出**")
st.markdown(
    "API用的 [这个](https://yunwu.ai/register?aff=ZDXj) 。claude-3-5-sonnet-20240620比较稳定，但BaseURL与APIKEY可自定义，理论上可用于任何兼容openAI库的模型")

# 输入区
st.session_state.base_url = st.sidebar.text_input("请输入你的API_BASE,默认：https://yunwu.ai/v1/chat/completions")
st.session_state.api_key = st.sidebar.text_input("输入你的API_KEY，确保和渠道一致")
st.session_state.model_factory = st.sidebar.selectbox("选择模型工厂(选择后筛选模型)", options=["Anthropic", "OpenAI"])

if st.session_state.model_factory is None or st.session_state.model_factory == "":
    st.session_state.model = st.sidebar.selectbox("选择模型", model_options["Anthropic"]+model_options["OpenAI"])
else:
    st.session_state.model = st.sidebar.selectbox("选择模型", model_options[st.session_state.model_factory])




if st.sidebar.checkbox("我要自行输入模型名称", value=False):
    st.session_state.model = st.sidebar.text_input("确保输入有效的模型名")

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
        st.session_state.api_key = 'sk-Q1DSG6RLztA4iWDOAF4XX1utdG8ElfzqnGZAmK9kmOOyoUVk'

    if not st.session_state.api_key:
        st.error("Please enter your API key.")
    elif not question:
        st.error("Please enter a question.")
    else:
        st.markdown("### Response:\n ----")
        response_area = st.empty()  # 保留动态更新的区域

        response_text = ""
        try:
            for chunk in completions.stream_response(question, st.session_state.api_key, st.session_state.model,
                                                     st.session_state.base_url):
                response_text += chunk
                response_area.write(response_text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
