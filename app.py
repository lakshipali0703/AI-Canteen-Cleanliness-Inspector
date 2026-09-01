
import streamlit as st
import pandas as pd
import subprocess
import json
import re
import os
from datetime import datetime


st.set_page_config(
    page_title="AI Canteen Cleanliness Inspector",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.main-title {
    font-size: 40px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.main-subtitle {
    text-align: center;
    font-size: 17px;
    margin-bottom: 30px;
    opacity: 0.75;
}

[data-testid="stForm"] {
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,0.35);
    background-color: rgba(255,255,255,0.04);
}

[data-testid="stMetric"] {
    border: 1px solid rgba(128,128,128,0.35);
    border-radius: 12px;
    padding: 15px;
}

.stButton > button,
.stFormSubmitButton > button {
    border-radius: 8px;
    font-weight: 600;
    min-height: 45px;
}

[data-testid="stSidebar"] {
    border-right: 1px solid rgba(128,128,128,0.25);
}

</style>
""", unsafe_allow_html=True)


CANTEEN_FILE = "Canteen_DB.xlsx"
COMPLAINT_FILE = "Complaints_DB.xlsx"


def load_canteens():

    if os.path.exists(CANTEEN_FILE):

        df = pd.read_excel(CANTEEN_FILE)

        required_columns = [
            "Canteen No.",
            "Canteen Name"
        ]

        for col in required_columns:
            if col not in df.columns:
                df[col] = ""

        return df[required_columns]

    return pd.DataFrame({
        "Canteen No.": ["C01"],
        "Canteen Name": ["Central Canteen"]
    })


def load_complaints():

    columns = [
        "Complaint ID",
        "Canteen No.",
        "Canteen Name",
        "Table No.",
        "Issue",
        "Description",
        "Severity",
        "Priority",
        "Status",
        "Staff",
        "Reported Time"
    ]

    if os.path.exists(COMPLAINT_FILE):

        df = pd.read_excel(COMPLAINT_FILE)

        for col in columns:

            if col not in df.columns:
                df[col] = ""

        return df[columns]

    return pd.DataFrame(columns=columns)


canteen_db = load_canteens()
complaints_db = load_complaints()


issue_categories = [
    "Dirty Table",
    "Spilled Food",
    "Leftover Plates",
    "Dirty Floor",
    "Bad Odour",
    "Pest",
    "Overflowing Trash",
    "Dirty Chairs",
    "Unclean Utensils",
    "Water Spill",
    "Food Waste",
    "Dirty Wash Area",
    "Blocked Bin Area",
    "Unclean Serving Area",
    "Other"
]


def analyze_complaint(issue, description):

    prompt = f"""
You are an AI cleanliness complaint analysis system
for a university canteen.

Analyze the following complaint.

Issue: {issue}

Description: {description}

Return ONLY a JSON object with exactly these fields:

{{
    "issue_category": "...",
    "severity": "...",
    "priority": "...",
    "recommended_action": "...",
    "reason": "..."
}}

Allowed Severity:
Low, Medium, High, Critical

Allowed Priority:
Routine, High, Immediate

Do not use markdown.
Do not use code fences.
Do not add explanations outside the JSON.
"""

    try:

        result = subprocess.run(
            ["ollama", "run", "gemma3:4b", prompt],
            capture_output=True,
            text=True,
            timeout=120
        )

        raw_response = result.stdout.strip()

        raw_response = re.sub(
            r"```json|```",
            "",
            raw_response,
            flags=re.IGNORECASE
        ).strip()

        match = re.search(
            r"\{.*\}",
            raw_response,
            re.DOTALL
        )

        if match:

            data = json.loads(match.group(0))

            severity = data.get(
                "severity",
                "Medium"
            )

            priority = data.get(
                "priority",
                "High"
            )

            if severity not in [
                "Low",
                "Medium",
                "High",
                "Critical"
            ]:
                severity = "Medium"

            if priority not in [
                "Routine",
                "High",
                "Immediate"
            ]:
                priority = "High"

            return {
                "issue_category": data.get(
                    "issue_category",
                    issue
                ),
                "severity": severity,
                "priority": priority,
                "recommended_action": data.get(
                    "recommended_action",
                    "Inspect and clean the affected area"
                ),
                "reason": data.get(
                    "reason",
                    "The reported cleanliness issue requires attention."
                )
            }

    except Exception:
        pass

    return {
        "issue_category": issue,
        "severity": "Medium",
        "priority": "High",
        "recommended_action": "Inspect and clean the affected area",
        "reason": "The reported cleanliness issue requires attention."
    }


st.markdown(
    '<div class="main-title">'
    '🧹 AI Canteen Cleanliness Inspector'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Smart complaint reporting and AI-powered hygiene monitoring system'
    '</div>',
    unsafe_allow_html=True
)


st.sidebar.title("🧹 Canteen Inspector")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "👨‍🎓 Student Complaint",
        "👨‍💼 Management Dashboard"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "AI-powered cleanliness monitoring system"
)


if page == "👨‍🎓 Student Complaint":

    st.subheader("📝 Report a Cleanliness Issue")

    st.write(
        "Help us maintain a clean and hygienic canteen "
        "by reporting any cleanliness issue you observe."
    )

    st.markdown("### Complaint Details")

    with st.form("complaint_form"):

        canteen_options = [
            f"{row['Canteen No.']} - {row['Canteen Name']}"
            for _, row in canteen_db.iterrows()
        ]

        if len(canteen_options) == 0:

            canteen_options = [
                "C01 - Central Canteen"
            ]

        col1, col2 = st.columns(2)

        with col1:

            canteen = st.selectbox(
                "🏫 Canteen",
                canteen_options
            )

        with col2:

            table_number = st.number_input(
                "🪑 Table Number",
                min_value=1,
                step=1
            )

        issue = st.selectbox(
            "🧹 Type of Issue",
            issue_categories
        )

        description = st.text_area(
            "📋 Describe the Problem",
            placeholder=(
                "Example: There is spilled food on the "
                "floor near the table."
            ),
            height=130
        )

        st.markdown("")

        submitted = st.form_submit_button(
            "🚨 Submit Complaint",
            use_container_width=True
        )


    if submitted:

        if not description.strip():

            st.error(
                "⚠️ Please describe the cleanliness issue "
                "before submitting."
            )

        else:

            if len(complaints_db) == 0:

                complaint_number = 1

            else:

                existing_ids = (
                    complaints_db["Complaint ID"]
                    .astype(str)
                    .str.extract(r"(\d+)")
                    .dropna()
                )

                if len(existing_ids) > 0:

                    complaint_number = (
                        existing_ids[0]
                        .astype(int)
                        .max()
                        + 1
                    )

                else:

                    complaint_number = 1


            complaint_id = f"C{complaint_number:03d}"


            canteen_no, canteen_name = canteen.split(
                " - ",
                1
            )


            with st.spinner(
                "🤖 AI is analysing your complaint..."
            ):

                ai_result = analyze_complaint(
                    issue,
                    description
                )


            new_complaint = {

                "Complaint ID": complaint_id,

                "Canteen No.": canteen_no,

                "Canteen Name": canteen_name,

                "Table No.": table_number,

                "Issue": issue,

                "Description": description,

                "Severity": ai_result["severity"],

                "Priority": ai_result["priority"],

                "Status": "Reported",

                "Staff": "Not Assigned",

                "Reported Time":
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
            }


            complaints_db = pd.concat(
                [
                    complaints_db,
                    pd.DataFrame([new_complaint])
                ],
                ignore_index=True
            )


            complaints_db.to_excel(
                COMPLAINT_FILE,
                index=False
            )


            st.success(
                f"✅ Complaint {complaint_id} "
                f"submitted successfully!"
            )


            st.markdown("### 🤖 AI Analysis")


            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "⚠️ Severity",
                    ai_result["severity"]
                )

            with col2:

                st.metric(
                    "🚨 Priority",
                    ai_result["priority"]
                )


            st.write(
                "**Issue Category:**",
                ai_result["issue_category"]
            )

            st.write(
                "**Recommended Action:**",
                ai_result["recommended_action"]
            )

            st.write(
                "**Reason:**",
                ai_result["reason"]
            )

            st.info(
                f"📌 Complaint ID: **{complaint_id}**  |  "
                f"Status: **Reported**"
            )


else:

    st.subheader("👨‍💼 Management Dashboard")

    st.write(
        "Monitor cleanliness complaints, risks and complaint trends."
    )


    if complaints_db.empty:

        st.info(
            "📊 No complaints have been submitted yet. "
            "Dashboard statistics will appear automatically "
            "after complaints are reported."
        )

    else:

        complaints_db["Reported Time"] = pd.to_datetime(
            complaints_db["Reported Time"],
            errors="coerce"
        )


        total = len(complaints_db)


        high_critical = complaints_db[
            complaints_db["Severity"].isin(
                ["High", "Critical"]
            )
        ].shape[0]


        immediate = complaints_db[
            complaints_db["Priority"] == "Immediate"
        ].shape[0]


        reported = complaints_db[
            complaints_db["Status"] == "Reported"
        ].shape[0]


        resolved = complaints_db[
            complaints_db["Status"]
            .astype(str)
            .str.lower()
            .isin(
                ["resolved", "closed"]
            )
        ].shape[0]


        col1, col2, col3, col4, col5 = st.columns(5)


        col1.metric(
            "Total",
            total
        )

        col2.metric(
            "High/Critical",
            high_critical
        )

        col3.metric(
            "Immediate",
            immediate
        )

        col4.metric(
            "Reported",
            reported
        )

        col5.metric(
            "Resolved",
            resolved
        )


        st.divider()


        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "🏫 Complaints by Canteen"
            )

            st.bar_chart(
                complaints_db[
                    "Canteen Name"
                ].value_counts()
            )


        with col2:

            st.subheader(
                "🧹 Complaints by Issue"
            )

            st.bar_chart(
                complaints_db[
                    "Issue"
                ].value_counts()
            )


        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "⚠️ Severity Distribution"
            )

            st.bar_chart(
                complaints_db[
                    "Severity"
                ].value_counts()
            )


        with col2:

            st.subheader(
                "🚨 Priority Distribution"
            )

            st.bar_chart(
                complaints_db[
                    "Priority"
                ].value_counts()
            )


        st.subheader(
            "📋 Complaint Records"
        )


        display_columns = [
            "Complaint ID",
            "Canteen Name",
            "Table No.",
            "Issue",
            "Severity",
            "Priority",
            "Status",
            "Staff",
            "Reported Time"
        ]


        st.dataframe(
            complaints_db[
                display_columns
            ],
            use_container_width=True,
            hide_index=True
        )
