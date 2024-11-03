import streamlit as st
from streamlit_disqus import st_disqus

def main():
    # 페이지 제목 설정
    st.title("Disqus 댓글 데모")
    
    # 페이지 내용 추가
    st.write("이 아래에 댓글이 표시됩니다.")
    
    # Disqus 댓글 섹션 추가
    # shortname은 Disqus에서 생성한 고유 식별자입니다
    st_disqus("streamlit-disqus-demo")

if __name__ == "__main__":
    main()
