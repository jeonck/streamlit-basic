import streamlit as st
import pandas as pd
import io

st.set_page_config(layout="wide")

st.title('CSV 파일 편집기')

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("데이터 편집기")
        st.write("편집이 필요한 셀을 더블클릭해서 데이터를 편집할 수 있습니다.")
        edited_df = st.data_editor(df)
    
    with col2:
        # "편집된 데이터" 텍스트와 다운로드 버튼을 나란히 배치
        subcol1, subcol2 = st.columns([3, 1])
        with subcol1:
            st.subheader("편집된 데이터")
            st.write("편집된 데이터를 다운로드할 수 있습니다.")
        with subcol2:
            # UTF-8 인코딩으로 CSV 생성 (BOM 포함)
            csv_buffer = io.StringIO()
            edited_df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
            csv_str = csv_buffer.getvalue()
            
            st.download_button(
                label="CSV 다운로드",
                data=csv_str,
                file_name="edited_file.csv",
                mime="text/csv",
            )
        
        # 데이터프레임 표시
        st.dataframe(edited_df)
