import streamlit as st

# 'sac' 라이브러리를 추가해야 합니다.
import streamlit_antd_components as sac

st.set_page_config(layout='wide', page_title='streamlit-antd-components')

# 스타일 설정
st.markdown(f'''
    <style>
    .stApp .main .block-container{{
        padding:30px 50px
    }}
    .stApp [data-testid='stSidebar']>div:nth-child(1)>div:nth-child(2){{
        padding-top:50px
    }}
    iframe{{
        display:block;
    }}
    .stRadio div[role='radiogroup']>label{{
        margin-right:5px
    }}
    </style>
    ''', unsafe_allow_html=True)

# 사이드바 설정
with st.sidebar.container():
    new = sac.Tag('New', color='green', bordered=False)
    st.subheader(f'Streamlit-antd-components')
    menu = sac.menu(
        items=[
            sac.MenuItem('Happy Lab', tag=new),  # AI Lab을 Happy Lab으로 변경
            sac.MenuItem('Service Lab'),
            sac.MenuItem('플랫폼 관리', type='group', children=[sac.MenuItem('이용자 관리')]),
            sac.MenuItem('프롬프트 관리', type='group', children=[sac.MenuItem('프롬프트 템플릿')]),
            sac.MenuItem(label='통계 관리', type='group', children=[
                sac.MenuItem('사용 통계'),
                sac.MenuItem('성능 통계')
            ]),
            sac.MenuItem(label='데이터 분석', type='group', children=[
                sac.MenuItem('데이터 시각화'),
                sac.MenuItem('데이터 변환')
            ]),
            sac.MenuItem(label='사용자 활동', type='group', children=[
                sac.MenuItem('활동 로그'),
                sac.MenuItem('이벤트 관리')
            ]),
            sac.MenuItem(label='시스템 설정', type='group', children=[
                sac.MenuItem('사용자 권한'),
                sac.MenuItem('시스템 로그'),
                sac.MenuItem('환경 설정')
            ]),
            sac.MenuItem(label='알림 관리', type='group', children=[  # 새로운 메뉴 '알림 관리'
                sac.MenuItem('이메일 알림'),  # 새로운 메뉴 '이메일 알림'
                sac.MenuItem('SMS 알림')  # 새로운 메뉴 'SMS 알림'
            ]),
            sac.MenuItem(label='지원 센터', type='group', children=[  # 새로운 메뉴 '지원 센터'
                sac.MenuItem('FAQ'),  # 새로운 메뉴 'FAQ'
                sac.MenuItem('지원 티켓')  # 새로운 메뉴 '지원 티켓'
            ]),
            sac.MenuItem(label='문서 관리', type='group', children=[  # 새로운 메뉴 '문서 관리'
                sac.MenuItem('API 문서'),  # 새로운 메뉴 'API 문서'
                sac.MenuItem('사용 매뉴얼')  # 새로운 메뉴 '사용 매뉴얼'
            ]),
            sac.MenuItem(label='시스템 모니터링', type='group', children=[  # 새로운 메뉴 '시스템 모니터링'
                sac.MenuItem('서버 상태'),  # 새로운 메뉴 '서버 상태'
                sac.MenuItem('네트워크 상태')  # 새로운 메뉴 '네트워크 상태'
            ]),
            sac.MenuItem(label='프로젝트 관리', type='group', children=[  # 새로운 메뉴 '프로젝트 관리'
                sac.MenuItem('진행 상황'),  # 새로운 메뉴 '진행 상황'
                sac.MenuItem('업무 할당')  # 새로운 메뉴 '업무 할당'
            ]),
            sac.MenuItem(label='고급 사용법', type='group', children=[
                sac.MenuItem('세션 상태'),
                sac.MenuItem('콜백')
            ]),
        ],
        key='menu',
        open_all=True, indent=20,
        format_func='title',
    )

# 메인 컨테이너 설정
with st.container():
    if menu == 'Happy Lab':  
        # Happy Lab에 해당하는 함수 호출
        happy_lab()  
    elif menu == 'Service Lab':
        # Service Lab에 해당하는 함수 호출
        service_lab()
    elif menu == '세션 상태':
        session_usage()
    elif menu == '콜백':
        callback_usage()
    elif menu == '아이콘':
        icon()
    else:
        com_ = DEMO.get(menu)
        if com_:
            st.subheader(menu.title(), anchor=False)
            st.write(com_.get('doc'))
            tabs = sac.tabs([sac.TabsItem('시연', icon='easel'), sac.TabsItem('API', icon='cursor')], size='sm')
            if tabs == '시연':
                col = st.columns([2.2, 1])
                with col[-1].expander(f"{menu} 매개변수", True):
                    kw = com_.get('params')(key=menu)
                with col[0]:
                    com_.get('main')(kw)
            else:
                com_.get('api')()
        else:
            st.error('해당 페이지를 찾을 수 없습니다.')