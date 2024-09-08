import streamlit as st
import pandas as pd
import numpy as np

# CSV 파일 업로드 기능
uploaded_file = st.sidebar.file_uploader("Upload project CSV", type=["csv"])

# 기본 프로젝트 데이터 설정
if uploaded_file is not None:
    # 업로드된 CSV 파일을 pandas DataFrame으로 읽어들임
    st.session_state.projects = pd.read_csv(uploaded_file)
else:
    # 업로드된 파일이 없으면 기본 데이터 사용
    project_data = pd.DataFrame({
        "Project ID": [1001, 1002, 1003, 1004],
        "Project Name": ["Website Redesign", "Mobile App Development", "Data Migration", "SEO Optimization"],
        "Status": ["In Progress", "Pending", "Completed", "In Progress"],
        "Priority": ["Medium", "Low", "High", "Medium"],
        "Completion %": [50, 0, 100, 40],
        "Due Date": ["2024-09-30", "2024-10-15", "2024-08-31", "2024-09-20"]
    })

    if "projects" not in st.session_state:
        st.session_state.projects = project_data

# 프로젝트 데이터 편집기
st.write("Editable Project List:")
edited_projects = st.data_editor(
    st.session_state.projects,
    num_rows="dynamic"  # 행 동적 추가 가능
)

# 우선순위 자동 설정 기준
st.sidebar.header("Set Priority Automatically")
completion_threshold = st.sidebar.slider("Completion Threshold for High Priority", 0, 100, 80)
due_date_range = st.sidebar.number_input("Days Until Due Date for High Priority", min_value=1, value=7)

# 우선순위 자동 설정 함수
def apply_auto_priority(projects_df):
    condition = (projects_df["Completion %"] < completion_threshold) & \
                (pd.to_datetime(projects_df["Due Date"]) - pd.Timestamp.now()).dt.days <= due_date_range
    projects_df.loc[condition, "Priority"] = "High"
    return projects_df

# 우선순위 자동 설정 버튼
if st.sidebar.button("Apply Auto Priority"):
    st.session_state.projects = apply_auto_priority(st.session_state.projects)
    st.success("Priority has been updated based on the rules.")
    st.rerun()

# 필터링 기능
st.sidebar.write("Filter Projects by Status")
filter_status = st.sidebar.selectbox("Select Status", ["All", "In Progress", "Pending", "Completed"])

if filter_status != "All":
    filtered_projects = st.session_state.projects[st.session_state.projects["Status"] == filter_status]
    st.write(f"Projects with status '{filter_status}':")
    st.write(filtered_projects)
else:
    st.write("All Projects:")
    st.write(st.session_state.projects)

# CSV 다운로드 기능
csv = st.session_state.projects.to_csv(index=False)
st.download_button(
    label="Download Project Data as CSV",
    data=csv,
    file_name="projects.csv",
    mime="text/csv"
)

# 프로젝트 추가 기능
st.sidebar.header("Add New Project")
new_project_id = st.sidebar.number_input("Project ID", min_value=1000, step=1)
new_project_name = st.sidebar.text_input("Project Name")
new_status = st.sidebar.selectbox("Status", ["In Progress", "Pending", "Completed"])
new_priority = st.sidebar.selectbox("Priority", ["Low", "Medium", "High"])
new_completion = st.sidebar.slider("Completion %", 0, 100, step=5)
new_due_date = st.sidebar.date_input("Due Date")

if st.sidebar.button("Add Project"):
    new_project = pd.DataFrame({
        "Project ID": [new_project_id],
        "Project Name": [new_project_name],
        "Status": [new_status],
        "Priority": [new_priority],
        "Completion %": [new_completion],
        "Due Date": [new_due_date]
    })
    
    st.session_state.projects = pd.concat([st.session_state.projects, new_project], ignore_index=True)
    st.rerun()  # 새 프로젝트 추가 후 자동 갱신
