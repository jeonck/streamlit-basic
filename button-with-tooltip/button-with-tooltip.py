import streamlit as st

# Example prompts
example_prompts = [
    "You gain life and enemy loses life",
    "Vampires cards with flying ability",
    "Blue and green colored sorcery cards",
    "White card with protection from black",
    "The famous 'Black Lotus' card",
    "Wizard card with Vigilance ability",
]

example_prompts_help = [
    "Look for a specific card effect",
    "Search for card type: 'Vampires', card color: 'black', and ability: 'flying'",
    "Color cards and card type",
    "Specific card effect to another mana color",
    "Search for card names",
    "Search for card types with specific abilities",
]

# 버튼을 두 개의 행으로 배치
button_cols = st.columns(3)  # 첫 번째 행에 세 개의 버튼
button_cols_2 = st.columns(3)  # 두 번째 행에 세 개의 버튼

# 선택된 버튼을 저장할 변수
button_pressed = ""

# 첫 번째 줄 버튼
if button_cols[0].button(example_prompts[0], help=example_prompts_help[0]):
    button_pressed = example_prompts[0]
elif button_cols[1].button(example_prompts[1], help=example_prompts_help[1]):
    button_pressed = example_prompts[1]
elif button_cols[2].button(example_prompts[2], help=example_prompts_help[2]):
    button_pressed = example_prompts[2]

# 두 번째 줄 버튼
elif button_cols_2[0].button(example_prompts[3], help=example_prompts_help[3]):
    button_pressed = example_prompts[3]
elif button_cols_2[1].button(example_prompts[4], help=example_prompts_help[4]):
    button_pressed = example_prompts[4]
elif button_cols_2[2].button(example_prompts[5], help=example_prompts_help[5]):
    button_pressed = example_prompts[5]

# 버튼이 눌렸을 때 처리
if button_pressed:
    st.write(f"You pressed: {button_pressed}")
