import streamlit as st


# 코드 보기 

def show_code():
    st.divider()
    st.markdown("### 코드가 궁금하시면 아래를 참고하세요. &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    st.title("모듈별 Code Block")
    with open('./asset/codeblock-module.txt', 'r') as file:
        code = file.read()  # Read the entire content of the file
        st.code(code, language='python')

    
# 섹션 
def section():
    st.title("섹션별 구분 표시")
    # 섹션 1
    st.header('첫 번째 섹션')

    # 섹션 1의 그리드 레이아웃을 만듭니다.
    # st.columns 함수를 사용하여 여러 열을 만들 수 있습니다.
    # 이 예제에서는 2개의 열을 만듭니다.
    col1, col2 = st.columns(2)

    # 첫 번째 열에 텍스트 추가
    with col1:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg', caption='이미지 캡션 - 열 2', use_column_width=True)

    # 두 번째 열에 이미지 추가
    with col2:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg', caption='이미지 캡션 - 열 2', use_column_width=True)

    # 섹션 2
    st.header('두 번째 섹션')

    # 섹션 2의 그리드 레이아웃을 만듭니다.
    # 이번에는 3개의 열을 만듭니다.
    col3, col4, col5 = st.columns(3)

    # 열에 각각 내용 추가
    with col3:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg', caption='이미지 캡션 - 열 2', use_column_width=True)

    with col4:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg', caption='이미지 캡션 - 열 2', use_column_width=True)

    with col5:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg', caption='이미지 캡션 - 열 2', use_column_width=True)

    ## 섹션 end  =====================================================================================================================
    show_code()
    return '' 

def codeblock():
    st.title("코드 블록")
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')
    
    show_code()
    return '' 
    

# 멀티 셀렉트 
def multiselect(): 
    st.title("멀티 셀렉트")
    hobby = ['운동', '영화감상', '음악듣기', '산책하기', '먹기']
    st.multiselect('당신의 취미를 선택하세요. 복수 선택 가능', hobby)
    
    language = ['음악 감상', '영화 감상', '독서', '요리', '운동']
    st.radio('당신의 취미를 선택하세요.', language)
    
    h2 = ['음악 감상', '영화 감상', '독서', '요리', '운동']
    st.checkbox('당신의 취미를 선택하세요.', h2)


    
    st.divider()
    st.markdown("코드가 궁금하시면 아래를 참고하세요. &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    code = '''
        st.title("멀티 셀렉트")
        language = ['운동', '영화감상', '음악듣기', '산책하기', '먹기']
        st.multiselect('당신의 취미를 선택하세요. 복수 선택 가능', language)
    '''
    st.code(code, language='python')
    
    show_code()
    
    return '' 

# 숫자 입력 : 정수, 실수    
def numbers():
    st.title("숫자 입력")
    st.number_input('정수 입력', 1, 100)
    st.number_input('실수 입력', 1.0, 100.0)
    
    st.divider()
    st.markdown("코드가 궁금하시면 아래의 코드를 참고하세요. &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    code = '''
        st.title("숫자 입력")
        st.number_input('정수 입력', 1, 100)
        st.number_input('실수 입력', 1.0, 100.0)
    '''
    st.code(code, language='python')
    show_code()
    return '' 

# 익스팬더 
def expander():
    st.title('데이터프레임 보기')
    data=[1,2,3,4]
    with st.expander('데이터프레임 보기') :
        st.dataframe(data)
    
    st.divider()
    st.markdown("코드가 궁금하시면 아래를 참고하세요. &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    code = '''
        data=[1,2,3,4]
        with st.expander('데이터프레임 보기') :
            st.dataframe(data)
    '''
    st.code(code, language='python')
    show_code()   
    return '' 

# 그림과 텍스트 
def picandtext():
    st.title("그림과 텍스트 출력 예제")
    st.image("sample.jpeg", caption="이미지 캡션")
    st.write("이미지와 함께 텍스트를 출력합니다.")
    
    st.divider()
    st.markdown("코드가 궁금하시면 아래를 참고하세요. &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    code = '''
        st.title("그림과 텍스트 출력 예제")
        st.image("sample.jpeg", caption="이미지 캡션")
        st.write("이미지와 함께 텍스트를 출력합니다.")
    '''
    st.code(code, language='python')
    show_code()
    return '' 

def pagemove():
    st.title("페이지 간 이동 예제")
    if st.button("다음 페이지로 이동"):
        st.write("다음 페이지로 이동합니다.")
        
    show_code()
    return '' 

def textinput():
    st.title("텍스트 입력 검색 예제")
    search_query = st.text_input("검색어를 입력하세요")
    if st.button("검색"):
        st.write(f"검색어: {search_query}")
    
    show_code()
    return '' 

def dataframe():
    import pandas as pd
    st.title("데이터 프레임 시각화 예제")
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    st.table(data)
    
    show_code()
    return '' 

def graphtable():
    import matplotlib.pyplot as plt
    import pandas as pd
    st.title("그래프와 표 조합 예제")
    data = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]})
    st.line_chart(data)
    st.table(data)
    
    show_code()
    return '' 

def markdowntext():
    st.title("마크다운 텍스트 예제")
    st.markdown("이 텍스트는 *마크다운* 형식으로 작성됩니다.")
    
    show_code()
    return '' 

def slider():
    st.title("슬라이더 예제")
    value = st.slider("값을 조절하세요", 0, 100, 50)
    st.write(f"선택한 값: {value}")
    
    show_code()

def buttonclick():
    st.title("버튼 클릭으로 텍스트 변경 예제")
    text = st.text("기본 텍스트")
    if st.button("클릭"):
        text.text("버튼이 클릭되었습니다!")
        
    show_code()
    return '' 

def simplegraph():
    import matplotlib.pyplot as plt
    import numpy as np
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("간단한 그래프 예제")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    st.pyplot()
    
    show_code()
    return '' 

def table():
    import pandas as pd
    st.title("데이터 테이블 예제")
    data = pd.DataFrame({'이름': ['Alice', 'Bob', 'Charlie'], '나이': [25, 30, 35]})
    st.dataframe(data)
    
    show_code()
    return '' 

def image():
    from PIL import Image
    st.title("이미지 표시 예제")
    image = Image.open("./asset/sample.jpeg")
    st.image(image, caption='이미지 캡션', use_column_width=True)
    
    show_code()
    return '' 

def radiobutton():
    st.title("라디오 버튼 예제")
    color = st.radio("좋아하는 색상을 선택하세요", ["빨강", "노랑", "파랑"])
    st.write(f"선택한 색상: {color}")
    
    show_code()
    return '' 

def datepick():
    import datetime
    st.title("날짜 선택 예제")
    date = st.date_input("날짜를 선택하세요", datetime.date(2023, 11, 11))
    st.write(f"선택한 날짜: {date}")
    
    show_code()
    return '' 

def fileupload():
    st.title("파일 업로드 예제")
    uploaded_file = st.file_uploader("파일을 업로드하세요", type=["jpg", "png", "pdf"])
    if uploaded_file:
        st.write(f"업로드한 파일 이름: {uploaded_file.name}")
        
    show_code()   
    return '' 

def addlink():
    st.title("링크 추가")
    st.write("이프랜드스튜디오:", "[공식 홈페이지](https://studio.ifland.io/)")
    st.write("Streamlit:", "[Streamlit 공식 홈페이지](https://streamlit.io/)")
    
    show_code()
    return '' 

# 데이터 테이블 표시
def datatable():
    st.title("데이터 테이블")
    data = [1,2,3,4]
    st.dataframe(data)
    
    show_code()
    return '' 

# 라인 차트 그리기
def chart():
    data = {'데이터1': [1, 2, 3, 4, 5],
            '데이터2': [10, 20, 30, 40, 50]}
    st.title("데이터1의 라인 차트")
    st.line_chart(data['데이터1'])
    # 바 차트 그리기
    st.title("데이터2의 바 차트")
    st.bar_chart(data['데이터2'])
    
    show_code()
    return ''

# 마크다운 추가
def markdown():
    st.markdown('''
    ## 사용 방법
    1. 텍스트 입력란에 분류하고자 하는 텍스트를 입력합니다.
    2. '카테고리 분류' 버튼을 클릭합니다.
    3. 분류 결과가 화면에 출력됩니다.
    ''')
    
    show_code()
    return '' 

# 진행 상태 표시 
def progress():
    import time
    st.title("진행 상태 표시 예제")
    progress_bar = st.progress(0)
    for i in range(101):
        time.sleep(0.05)
        progress_bar.progress(i)
    
    show_code()
    return '' 


# Define a dictionary to map menu names to functions
menu_options = {
    "섹션": (section, "섹션"),
    "다중 선택": (multiselect, "다중 선택"),
    "숫자 입력": (numbers, "숫자 입력"),
    "확장기": (expander, "확장기"),
    "그림과 텍스트": (picandtext, "그림과 텍스트"),
    "페이지 이동": (pagemove, "페이지 이동"),
    "텍스트 입력": (textinput, "텍스트 입력"),
    "dataframe": (dataframe, "데이터 프레임"),
    "그래프와 표": (graphtable, "그래프와 표"),
    "이미지": (image, "이미지"),
    "라디오 버튼": (radiobutton, "라디오 버튼"),
    "날짜 선택": (datepick, "날짜 선택"),
    "파일 업로드": (fileupload, "파일 업로드"),
    "링크 추가": (addlink, "링크 추가"),
    "데이터 테이블": (datatable, "데이터 테이블"),
    "chart": (chart, "차트"),
    "Markdown": (markdown, "마크다운"),
    "진행 상황 표시기": (progress, "진행 상황 표시기"),
    "코드 블록": (codeblock, "코드 블록")
}


### General Part Select Box #########################################################################
# Get the selected option from the user
selected_option = st.sidebar.selectbox("기능을 구현할 메뉴를 선택하세요.", list(menu_options.keys()))

# Retrieve the corresponding function and Korean name from the dictionary
selected_function, menu_name = menu_options[selected_option]

# Display the selected menu and execute the corresponding function
# st.write(f"선택한 메뉴: {menu_name}")
st.write(selected_function())
