import streamlit as st
import datetime

st.title('📝 나의 To-Do 리스트')

# 세션 상태 초기화
if 'todos' not in st.session_state:
    st.session_state.todos = []

# 새 할 일 추가
new_todo = st.text_input("새로운 할 일을 입력하세요:")
if st.button("추가") and new_todo:
    st.session_state.todos.append({"task": new_todo, "done": False, "date": datetime.date.today()})
    st.success(f"'{new_todo}'가 추가되었습니다!")

# 할 일 목록 표시
if st.session_state.todos:
    st.write("---")
    st.subheader("할 일 목록")
    for idx, todo in enumerate(st.session_state.todos):
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            done = st.checkbox(todo["task"], todo["done"], key=f"todo_{idx}")
            if done != todo["done"]:
                st.session_state.todos[idx]["done"] = done
                if done:
                    st.success("잘 하셨어요! 할 일을 완료했습니다.")
                else:
                    st.info("할 일을 다시 열었습니다.")
        
        with col2:
            st.write(f"추가일: {todo['date']}")
        
        with col3:
            if st.button("삭제", key=f"del_{idx}"):
                del st.session_state.todos[idx]
                st.warning("할 일이 삭제되었습니다.")
                st.experimental_rerun()

    # 통계
    total = len(st.session_state.todos)
    completed = sum(1 for todo in st.session_state.todos if todo["done"])
    st.write("---")
    st.metric("전체 할 일", total)
    st.metric("완료한 일", completed)
    progress = completed / total if total > 0 else 0
    st.progress(progress)
    
    if progress == 1:
        st.balloons()
        st.success("축하합니다! 모든 할 일을 완료했습니다.")
    elif progress >= 0.7:
        st.info("거의 다 왔어요! 조금만 더 힘내세요.")
    elif progress >= 0.5:
        st.info("절반 이상 완료했습니다. 잘 하고 있어요!")
    elif progress > 0:
        st.info("천천히 꾸준히 해나가세요.")
    else:
        st.info("할 일을 하나씩 처리해 나가봐요.")

else:
    st.info("할 일을 추가해보세요!")

# 모든 할 일 삭제
if st.button("모든 할 일 삭제"):
    st.session_state.todos = []
    st.warning("모든 할 일이 삭제되었습니다.")
    st.experimental_rerun()
