import streamlit as st

# Mode descriptions: mode -> [Description, Example usage, Max cards]
mode_descriptions = {
    "BM25": ["BM25 검색 모드는 전통적인 역문서 빈도를 기반으로 합니다.", "Example usage: BM25 Search", 10],
    "Vector": ["벡터 검색 모드는 임베딩 기반으로 문서 간의 유사성을 계산합니다.", "Example usage: Vector Search", 15],
    "Hybrid": ["하이브리드 검색 모드는 BM25와 벡터 검색을 결합한 방식입니다.", "Example usage: Hybrid Search", 20],
    "Generative": ["생성 검색 모드는 질의에 대한 텍스트 생성 및 검색을 지원합니다.", "Example usage: Generative Search", 5]
}

# Custom CSS to override default styles except for background color
st.markdown(
    """
    <style>
    .stSidebar .stAlert {
        border-radius: 10px !important;       /* Rounded corners */
        padding: 10px !important;            /* Padding inside */
        border: none !important;             /* Remove borders */
        box-shadow: none !important;         /* Remove shadow */
        color: black !important;             /* Ensure text is black */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# User Configuration Sidebar
with st.sidebar:
    mode = st.radio(
        "Search Mode", options=["BM25", "Vector", "Hybrid", "Generative"], index=3
    )
    limit = st.slider(
        label="Number of cards",
        min_value=1,
        max_value=mode_descriptions[mode][2],
        value=6,
    )
    st.info(mode_descriptions[mode][0])

st.divider()

# Display the user's selected options
st.write(f"**Selected Search Mode:** {mode}")
st.write(f"**Number of Cards to Display:** {limit}")

# Show the search example based on the mode
st.write(f"### Example usage for {mode}:")
st.write(mode_descriptions[mode][1])

st.divider()

# Display some placeholder cards (for demonstration purposes)
st.write("### Search Results:")
for i in range(limit):
    st.write(f"#### Card {i + 1}")
    st.write(f"Content for {mode} search result {i + 1}")
    st.write("---")
