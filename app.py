import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from scipy.stats import pearsonr

st.set_page_config(page_title="Virtual Lab", layout="wide")

st.markdown(
    """
<style>
:root {
    --ink: #13253f;
    --ink-soft: #2f4565;
    --muted: #5e7291;
    --surface: rgba(255, 255, 255, 0.86);
    --surface-strong: #ffffff;
    --line: rgba(19, 37, 63, 0.12);
    --accent: #0f766e;
    --accent-2: #115e59;
    --highlight: #bfdbfe;
}

.stApp {
    background:
        radial-gradient(1200px 500px at 0% 0%, rgba(191, 219, 254, 0.55), transparent 65%),
        radial-gradient(900px 450px at 100% 0%, rgba(187, 247, 208, 0.35), transparent 70%),
        linear-gradient(180deg, #f8fafc 0%, #eef2ff 45%, #f8fafc 100%);
    color: var(--ink);
    font-family: "Trebuchet MS", "Segoe UI", sans-serif;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1f3a 0%, #163663 100%);
    border-right: 1px solid rgba(255, 255, 255, 0.15);
}

[data-testid="stSidebar"] [data-testid="stRadio"] > div {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

[data-testid="stSidebar"] [role="radiogroup"] label {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    margin-bottom: 0.35rem;
    padding: 0.35rem 0.5rem;
}

[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: rgba(255, 255, 255, 0.15);
}

.main .block-container {
    max-width: 1180px;
    padding-top: 1.4rem;
    padding-bottom: 1.8rem;
}

.hero {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.93), rgba(238, 242, 255, 0.95));
    border: 1px solid var(--line);
    border-radius: 18px;
    box-shadow: 0 14px 36px rgba(15, 23, 42, 0.08);
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
}

.hero-title {
    margin: 0;
    font-size: 2rem;
    color: var(--ink);
    letter-spacing: 0.2px;
}

.hero-subtitle {
    margin: 0.3rem 0 0;
    color: var(--muted);
    font-size: 1.02rem;
}

.panel {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    padding: 1.1rem 1.2rem;
    margin-bottom: 1rem;
    backdrop-filter: blur(6px);
}

.metric-strip {
    background: var(--surface-strong);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 0.65rem 0.8rem;
}

h1, h2, h3 {
    color: var(--ink);
}

p, li {
    color: var(--ink-soft);
    font-size: 1.08rem;
}

label, [data-testid="stMarkdownContainer"] p, .stCaption {
    font-size: 1.08rem !important;
}

[data-baseweb="select"] > div,
[data-testid="stFileUploader"] section,
[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    border: 1px solid var(--line) !important;
    background: var(--surface-strong) !important;
}

[data-testid="stRadio"] > div {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

[data-testid="stRadio"] label {
    background: transparent !important;
    border: none !important;
}

.stButton > button {
    background: linear-gradient(135deg, #16a34a, #15803d) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    padding: 0.52rem 1.2rem !important;
    box-shadow: 0 8px 16px rgba(21, 128, 61, 0.22);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #15803d, #166534) !important;
}

footer {
    visibility: hidden;
}

@media (max-width: 860px) {
    .hero-title {
        font-size: 1.5rem;
    }

    .hero-subtitle {
        font-size: 0.95rem;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
  <h1 class="hero-title">📊 Virtual Lab: Statistical Analysis</h1>
  <p class="hero-subtitle">Learn statistics through guided theory, live simulation, and smart quiz practice.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown("## 🧪 Virtual Lab")
st.sidebar.caption("Navigate through experiment sections")

menu = st.sidebar.radio(
    "Navigation",
    ["Aim", "Theory", "Procedure", "Simulation", "Observations", "Quiz", "References"],
)

if menu == "Aim":
    st.subheader("🎯 Aim")
    st.write("To explore descriptive and inferential statistics on datasets using real-world data.")
    st.markdown(
        """
This experiment helps you understand statistics in a practical, visual way:
- Descriptive statistics: mean, median, mode, variance, standard deviation, IQR.
- Data visualization: histogram, boxplot, scatter plot.
- Inferential insights: correlation and significance using p-values.

The workflow is designed to connect concepts with real data, making statistical thinking easier to apply in research, business analysis, and data science projects.
"""
    )

elif menu == "Theory":
    st.subheader("📚 Theory")
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### Descriptive Statistics")
        st.markdown("- Mean: average value")
        st.markdown("- Median: middle value")
        st.markdown("- Mode: most frequent value")
        st.markdown("- Standard Deviation: spread from mean")

    with c2:
        st.markdown("### Inferential Statistics")
        st.markdown("- Correlation: strength and direction of relation")
        st.markdown("- p-value: tests if relation is statistically significant")
        st.markdown("- If p-value < 0.05, relation is considered significant")

    st.markdown("### Visualization")
    v1, v2, v3 = st.columns(3)
    with v1:
        st.image(
            "https://th.bing.com/th/id/OIP.m620ll2UbKGEV-5kbX9MkAHaFj?w=225&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            caption="Histogram",
        )
    with v2:
        st.image(
            "https://th.bing.com/th/id/OIP.-XVVT92ks9VgZx5n94U5cwHaDd?w=339&h=163&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            caption="Boxplot",
        )
    with v3:
        st.image(
            "https://th.bing.com/th/id/OIP.sG6e2imMuM2lvqLJFO9JjQHaE8?w=276&h=184&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
            caption="Scatter Plot",
        )

elif menu == "Procedure":
    st.subheader("⚙️ Procedure")
    st.markdown(
        """
1. Upload a CSV dataset.
2. Preview the dataset table.
3. Select numeric columns for analysis.
4. Generate descriptive stats and plots.
5. Check correlation and p-value for selected features.
6. Review observations and complete quiz.
"""
    )

elif menu == "Simulation":
    st.subheader("🔬 Simulation")

    file = st.file_uploader("Upload CSV file", type=["csv"])

    if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df, use_container_width=True)

        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) > 0:
            col = st.selectbox("Select column for univariate analysis", numeric_cols)
            mean = df[col].mean()
            std = df[col].std()

            m1, m2 = st.columns(2)
            with m1:
                st.metric("Mean", f"{mean:.2f}")
            with m2:
                st.metric("Std Dev", f"{std:.2f}")

            c1, c2 = st.columns(2)
            with c1:
                fig, ax = plt.subplots(figsize=(6, 3.2))
                sns.histplot(df[col], kde=True, ax=ax, color="#0f766e")
                ax.set_title("Histogram")
                st.pyplot(fig, use_container_width=True)

            with c2:
                fig2, ax2 = plt.subplots(figsize=(6, 3.2))
                sns.boxplot(x=df[col], ax=ax2, color="#bfdbfe")
                ax2.set_title("Boxplot")
                st.pyplot(fig2, use_container_width=True)

            if len(numeric_cols) >= 2:
                x = st.selectbox("X-axis", numeric_cols)
                y = st.selectbox("Y-axis", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)

                fig3, ax3 = plt.subplots(figsize=(7, 3.6))
                sns.scatterplot(x=df[x], y=df[y], ax=ax3, color="#2563eb", alpha=0.85)
                ax3.set_title("Scatter Plot")
                st.pyplot(fig3, use_container_width=True)

                corr, p_value = pearsonr(df[x], df[y])
                s1, s2 = st.columns(2)
                with s1:
                    st.metric("Correlation", f"{corr:.2f}")
                with s2:
                    st.metric("p-value", f"{p_value:.4f}")

                st.session_state["mean"] = mean
                st.session_state["std"] = std
                st.session_state["corr"] = corr
                st.session_state["p_value"] = p_value
        else:
            st.warning("No numeric columns found in this CSV file.")

elif menu == "Observations":
    st.subheader("📌 Observations")

    if "mean" in st.session_state:
        o1, o2 = st.columns(2)
        with o1:
            st.metric("Mean", f"{st.session_state['mean']:.2f}")
        with o2:
            st.metric("Std Dev", f"{st.session_state['std']:.2f}")

        if st.session_state.get("p_value") is not None:
            if st.session_state["p_value"] < 0.05:
                st.success("Significant relationship detected (p < 0.05).")
            else:
                st.warning("No statistically significant relationship detected.")
    else:
        st.info("Run the Simulation tab first to generate observations.")

elif menu == "Quiz":
    st.subheader("🧠 Statistical Quiz")

    level = st.selectbox("Select Difficulty Level", ["Basic", "Moderate", "Advanced"])

    if level == "Basic":
        questions = [
            ("Mean represents?", ["Middle value", "Average", "Mode"], "Average"),
            ("Median is?", ["Average", "Middle value", "Highest"], "Middle value"),
            ("Mode is?", ["Frequent", "Average", "Middle"], "Frequent"),
            ("CSV file is?", ["Image", "Data file", "Audio"], "Data file"),
        ]
    elif level == "Moderate":
        questions = [
            ("Standard deviation measures?", ["Spread", "Center", "Count"], "Spread"),
            ("Histogram shows?", ["Relation", "Distribution", "Outliers"], "Distribution"),
            ("Boxplot detects?", ["Trend", "Outliers", "Mean"], "Outliers"),
            ("Scatter plot shows?", ["Relation", "Distribution", "Mean"], "Relation"),
            ("Variance represents?", ["Spread", "Center", "Count"], "Spread"),
        ]
    else:
        questions = [
            ("Correlation range?", ["0-1", "-1 to 1", "0-100"], "-1 to 1"),
            ("p-value < 0.05 means?", ["Significant", "Random", "None"], "Significant"),
            ("Null hypothesis means?", ["No relation", "Relation", "Random"], "No relation"),
            ("IQR stands for?", ["Inter Quartile Range", "Interval", "Internal"], "Inter Quartile Range"),
            ("Correlation measures?", ["Causation", "Relationship", "Distribution"], "Relationship"),
        ]

    score = 0
    answered_count = 0

    for i, (question, options, correct) in enumerate(questions):
        answer = st.radio(
            f"Q{i + 1}. {question}",
            options,
            index=None,
            key=f"{level}_{i}",
        )
        if answer is not None:
            answered_count += 1
            if answer == correct:
                score += 1

    if st.button("Submit Quiz"):
        if answered_count < len(questions):
            st.warning("Please answer all questions before submitting.")
        else:
            st.success(f"Score: {score}/{len(questions)}")
            if score == len(questions):
                st.success("Excellent performance.")
            elif score >= len(questions) // 2:
                st.info("Good effort. Keep practicing.")
            else:
                st.warning("Revise concepts and try again.")

elif menu == "References":
    st.subheader("📚 References")

    st.markdown(
        """
### Recent Research Papers
- https://arxiv.org/pdf/2108.02497.pdf
- https://arxiv.org/pdf/2002.07637.pdf
- https://arxiv.org/pdf/2203.15556.pdf
- https://www.mdpi.com/2227-7390/11/5/1234

### Core Learning
- https://www.statlearning.com/
- https://www.khanacademy.org/math/statistics-probability
- https://pandas.pydata.org/docs/
"""
    )

st.markdown(
    """
<hr>
<p style='text-align:center; font-size:14px; color:#64748b;'>
© Members: 1. Vedika Dhamale | 2. Shravani Bhosale | 3. Akash Jadhav
</p>
""",
    unsafe_allow_html=True,
)
