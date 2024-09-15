import streamlit as st
import ast
import radon.metrics as metrics
from radon.complexity import cc_visit
from radon.raw import analyze
from radon.metrics import h_visit

def analyze_code(code):
    # 기존 분석
    tree = ast.parse(code)
    function_count = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))
    class_count = sum(isinstance(node, ast.ClassDef) for node in ast.walk(tree))
    
    # Raw metrics 분석
    raw_metrics = analyze(code)
    
    # MI (Maintainability Index) 계산
    mi = metrics.mi_visit(code, multi=True)
    
    # CC (Cyclomatic Complexity) 계산
    cc = cc_visit(code)
    avg_cc = sum(item.complexity for item in cc) / len(cc) if cc else 0
    
    # Halstead metrics 계산
    h_metrics = h_visit(code)
    
    return {
        "함수 수": function_count,
        "클래스 수": class_count,
        "LOC (Lines of Code)": raw_metrics.loc,
        "LLOC (Logical Lines of Code)": raw_metrics.lloc,
        "SLOC (Source Lines of Code)": raw_metrics.sloc,
        "주석 수": raw_metrics.comments,
        "다중 주석 수": raw_metrics.multi,
        "공백 라인 수": raw_metrics.blank,
        "MI (Maintainability Index)": mi,
        "평균 CC (Cyclomatic Complexity)": avg_cc,
        "Halstead Volume": h_metrics.total.volume,
        "Halstead Difficulty": h_metrics.total.difficulty,
        "Halstead Effort": h_metrics.total.effort
    }

st.title("파이썬 코드 정적 분석기")

code = st.text_area("분석할 파이썬 코드를 입력하세요:", height=300)

if st.button("분석"):
    if code:
        results = analyze_code(code)
        st.write("분석 결과:")
        
        # 복잡도 메트릭 (가장 먼저 표시)
        with st.expander("복잡도 메트릭", expanded=True):
            st.write("코드의 복잡도를 나타내는 지표입니다.")
            
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    label="MI (Maintainability Index)",
                    value=f"{results['MI (Maintainability Index)']:.2f}",
                    help="MI는 0-100 사이의 값으로, 높을수록 유지보수가 쉽습니다. 일반적으로 65 이상이 권장됩니다."
                )
            
            with col2:
                st.metric(
                    label="평균 CC (Cyclomatic Complexity)",
                    value=f"{results['평균 CC (Cyclomatic Complexity)']:.2f}",
                    help="CC는 코드의 복잡도를 나타내며, 일반적으로 10 이하가 권장됩니다."
                )
            
            st.write("MI가 높을수록, CC가 낮을수록 코드의 품질이 좋다고 볼 수 있습니다.")
            
            st.subheader("Halstead 메트릭")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(
                    label="Volume",
                    value=f"{results['Halstead Volume']:.2f}",
                    help="프로그램의 크기를 나타냅니다. 값이 클수록 프로그램이 더 크고 복잡합니다. 일반적으로 100-8000 사이의 값을 가지며, 8000 이상은 매우 큰 프로그램을 의미합니다."
                )
            with col2:
                st.metric(
                    label="Difficulty",
                    value=f"{results['Halstead Difficulty']:.2f}",
                    help="프로그램을 이해하고 수정하기 어려운 정도를 나타냅니다. 값이 높을수록 더 어렵습니다. 일반적으로 0-50 사이의 값을 가지며, 20 이상은 복잡한 프로그램을 의미합니다."
                )
            with col3:
                st.metric(
                    label="Effort",
                    value=f"{results['Halstead Effort']:.2f}",
                    help="프로그램을 구현하는 데 필요한 노력을 나타냅니다. 값이 높을수록 더 많은 노력이 필요합니다. 일반적으로 0-5000 사이의 값을 가지며, 1000 이상은 상당한 노력이 필요한 프로그램을 의미합니다."
                )
            st.write("Halstead 메트릭은 프로그램의 복잡도를 다양한 관점에서 측정합니다. 각 메트릭의 값이 낮을수록 일반적으로 더 좋은 코드 품질을 나타냅니다.")
        
        # 기본 정보
        with st.expander("기본 정보", expanded=True):
            st.write("코드의 기본적인 구조에 대한 정보입니다.")
            st.write(f"함수 수: {results['함수 수']}")
            st.write(f"클래스 수: {results['클래스 수']}")
        
        # 코드 크기 메트릭
        with st.expander("코드 크기 메트릭", expanded=True):
            st.write("코드의 크기를 나타내는 다양한 지표입니다.")
            st.write(f"LOC (Lines of Code): {results['LOC (Lines of Code)']}")
            st.write(f"LLOC (Logical Lines of Code): {results['LLOC (Logical Lines of Code)']}")
            st.write(f"SLOC (Source Lines of Code): {results['SLOC (Source Lines of Code)']}")
        
        # 주석 관련 메트릭
        with st.expander("주석 관련 메트릭", expanded=True):
            st.write("코드 내의 주석에 대한 정보입니다.")
            st.write(f"주석 수: {results['주석 수']}")
            st.write(f"다중 주석 수: {results['다중 주석 수']}")
            st.write(f"공백 라인 수: {results['공백 라인 수']}")
    else:
        st.warning("코드를 입력해주세요.")
