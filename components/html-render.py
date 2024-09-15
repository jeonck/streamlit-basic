import streamlit as st
import streamlit.components.v1 as stc

def main():
    st.set_page_config(layout="wide", page_title="Bootstrap HTML 렌더링 예제")

    st.title("Bootstrap HTML 렌더링 예제")
    st.markdown("<p>이것은 스트림릿 컴포넌트를 사용하여 Bootstrap HTML을 렌더링하는 예제입니다.</p>", unsafe_allow_html=True)

    # HTML_WRAPPER 수정
    HTML_WRAPPER = """
    <div style="width: 100%; overflow-x: auto; background-color: white;">
        {}
    </div>
    """

    stc.html(HTML_WRAPPER.format(
        """
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        
        <div class="container-fluid px-4">
            <div class="jumbotron bg-primary text-white text-center p-5 rounded my-4">
                <h1 class="display-4">안녕하세요!</h1>
                <p class="lead">스트림릿 컴포넌트를 사용하여 <strong>Bootstrap HTML</strong>을 렌더링합니다.</p>
            </div>
            
            <div class="row my-4">
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">카드 제목</h5>
                            <p class="card-text">이것은 카드 내용입니다. 여기에 다양한 정보를 넣을 수 있습니다.</p>
                            <a href="#" class="btn btn-primary">자세히 보기</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <h3>진행 상황</h3>
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: 70%;" aria-valuenow="70" aria-valuemin="0" aria-valuemax="100">70%</div>
                    </div>
                </div>
            </div>
            
            <div class="row my-4">
                <div class="col-md-6">
                    <h3>순서 있는 목록</h3>
                    <ol class="list-group list-group-numbered">
                        <li class="list-group-item">첫 번째 항목</li>
                        <li class="list-group-item">두 번째 항목</li>
                        <li class="list-group-item">세 번째 항목</li>
                    </ol>
                </div>
                <div class="col-md-6">
                    <h3>이미지</h3>
                    <img src="https://via.placeholder.com/300x200" alt="플레이스홀더 이미지" class="img-fluid rounded">
                </div>
            </div>
            
            <div class="my-4">
                <h3>표</h3>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>열 1</th>
                            <th>열 2</th>
                            <th>열 3</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>행 1, 열 1</td>
                            <td>행 1, 열 2</td>
                            <td>행 1, 열 3</td>
                        </tr>
                        <tr>
                            <td>행 2, 열 1</td>
                            <td>행 2, 열 2</td>
                            <td>행 2, 열 3</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="my-4">
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    모달 열기
                </button>

                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel">모달 제목</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                여기에 모달 내용을 넣습니다.
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                                <button type="button" class="btn btn-primary">저장</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    ), height=600, scrolling=True)

if __name__ == "__main__":
    main()