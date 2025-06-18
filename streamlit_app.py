
import streamlit as st
import random
import time
import base64

# ページ設定
st.set_page_config(page_title="まむこから取り戻せ", layout="centered")
st.title("まむこから取り戻せ ")

# 音声ファイルの埋め込み
def load_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        return f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """

# セッション変数の初期化
if "score" not in st.session_state:
    st.session_state.score = 0
if "ojisan_x" not in st.session_state:
    st.session_state.ojisan_x = random.randint(50, 350)
if "ojisan_y" not in st.session_state:
    st.session_state.ojisan_y = random.randint(100, 300)

# スコア表示
st.markdown(f"### 💰 現在の回収額：{st.session_state.score} 円")

# 顔画像の表示位置（CSSで動かす）
st.markdown(
    f"""
    <style>
    .ojisan-button {{
        position: absolute;
        top: {st.session_state.ojisan_y}px;
        left: {st.session_state.ojisan_x}px;
        z-index: 10;
    }}
    </style>
    <div class="ojisan-button">
        <form action="" method="post">
            <button name="tap" style="background: none; border: none;">
                <img src="https://github.com/tama-one/recover-the-missing-money/blob/main/ojisan_game_assets/ojisan.png?raw=true" width="100">
            </button>
        </form>
    </div>
    """,
    unsafe_allow_html=True
)

# クリック検知
if st.button("👈 まむこをしばく！"):
    st.session_state.score += 500
    st.session_state.ojisan_x = random.randint(50, 350)
    st.session_state.ojisan_y = random.randint(100, 300)
    st.markdown(load_audio("ojisan_game_assets/charin.mp3"), unsafe_allow_html=True)

# クリア判定
if st.session_state.score >= 5000:
    st.success("🎉 クリア！まむこから5,000円を回収した！")
    st.markdown(load_audio("ojisan_game_assets/fanfare.mp3"), unsafe_allow_html=True)
    st.balloons()

    # ▶️ もう一度プレイボタン
    if st.button("🔁 もう一度まむこをしばく！"):
        st.session_state.score = 0
        st.session_state.ojisan_x = random.randint(50, 350)
        st.session_state.ojisan_y = random.randint(100, 300)
        st.rerun()
    st.stop()


st.markdown("---")
