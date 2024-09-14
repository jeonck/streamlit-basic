import streamlit as st
import streamlit.components.v1 as stc

def main():
    st.set_page_config(layout="wide", page_title="부트스트랩을 적용한 st.html() 예제")

    st.title("부트스트랩을 적용한 st.html() 예제")
    st.markdown("<p>이것은 부트스트랩과 스트림릿 컴포넌트를 사용한 HTML 예제입니다.</p>", unsafe_allow_html=True)
    
    stc.html(
        """
        <!-- 부트스트랩 CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        
        <style>
        body, html {
            height: 100%;
            margin: 0;
            padding: 0;
        }
        .full-height {
            height: calc(100vh - 100px);
            display: flex;
            flex-direction: column;
        }
        .slide {
            display: none;
            flex-grow: 1;
            overflow-y: auto;
        }
        .slide-content {
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .slide-content h2 {
            margin-bottom: 20px;
        }
        .slide-content p {
            text-align: center;
            margin-bottom: 15px;
        }
        .slide-content ul {
            text-align: left;
        }
        </style>
        
        <div class="container-fluid full-height">
            <h1 class="text-center mb-4" style="color: tomato;">스트림릿과 부트스트랩 예제</h1>
            <div class="row h-100">
                <div class="col-12">
                    <div id="slide" class="slide p-4 bg-light border rounded">
                        <div class="slide-content"></div>
                    </div>
                    <div class="d-flex justify-content-center mt-3">
                        <button class="btn btn-primary me-2" onclick="prevSlide()">이전</button>
                        <button class="btn btn-primary" onclick="nextSlide()">다음</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- 부트스트랩 JS 및 Popper.js -->
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>

        <script>
        let currentSlide = 0;
        const slides = [
            `<h2>스트림릿 소개</h2>
            <p>스트림릿은 데이터 과학 및 머신러닝 애플리케이션을 위한 오픈소스 프레임워크입니다.</p>
            <ul>
                <li>파이썬으로 웹 앱 개발 가능</li>
                <li>데이터 시각화 도구 내장</li>
                <li>빠른 프로토타이핑에 적합</li>
            </ul>
            <p>자세한 내용은 <a href="https://streamlit.io" target="_blank">공식 웹사이트</a>를 참조하세요.</p>`,
            
            `<h2>부트스트랩 활용</h2>
            <p>부트스트랩은 반응형 웹 디자인을 위한 강력한 프론트엔드 프레임워크입니다.</p>
            <div class="alert alert-info" role="alert">
                이 슬라이드는 부트스트랩 컴포넌트를 사용하여 만들어졌습니다!
            </div>
            <button class="btn btn-success">부트스트랩 버튼</button>`,
            
            `<h2>스트림릿 + 부트스트랩</h2>
            <p>스트림릿과 부트스트랩을 함께 사용하면 강력한 데이터 애플리케이션을 만들 수 있습니다.</p>
            <div class="progress" style="height: 25px;">
                <div class="progress-bar bg-success" role="progressbar" style="width: 75%;" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">75%</div>
            </div>
            <p class="mt-3">위 프로그레스 바는 부트스트랩 컴포넌트의 예시입니다.</p>`
        ];
        
        function showSlide(n) {
            currentSlide = (n + slides.length) % slides.length;
            const slideElement = document.getElementById('slide');
            slideElement.style.display = 'block';
            slideElement.querySelector('.slide-content').innerHTML = slides[currentSlide];
        }
        
        function nextSlide() {
            showSlide(currentSlide + 1);
        }
        
        function prevSlide() {
            showSlide(currentSlide - 1);
        }

        showSlide(0);
        </script>
        """,
        height=600
    )

if __name__ == "__main__":
    main()