# Daniela Arrospide - Capstone Front End PY


#region IMPORTS
import streamlit as st
import pandas as pd
import re
import html

st.set_page_config(
    page_title="Compliance Gap Analyzer",
    layout="wide"
)
#endregion
#region BRAND HEADER

st.markdown("""
<style>
.dashboard-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #1f2937;
    margin-bottom: 0.2rem;
}

.dashboard-subtitle {
    font-size: 1rem;
    color: #6b7280;
    margin-bottom: 1.5rem;
}

.metric-card {
    border-radius: 16px;
    padding: 1.2rem 1rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(0, 0, 0, 0.06);
    min-height: 145px;
    margin-bottom: 0.5rem;
}

.metric-label {
    font-size: 0.95rem;
    font-weight: 600;
    color: #374151;
    margin-bottom: 0.45rem;
}

.metric-value {
    font-size: 2.3rem;
    font-weight: 700;
    line-height: 1.1;
    color: #111827;
    margin-bottom: 0.35rem;
}

.metric-note {
    font-size: 0.85rem;
    color: #4b5563;
}

.overall-card {
    background: linear-gradient(135deg, #dbeafe, #eff6ff);
}

.passed-card {
    background: linear-gradient(135deg, #dcfce7, #f0fdf4);
}

.failed-card {
    background: linear-gradient(135deg, #fee2e2, #fff1f2);
}

.review-card {
    background: linear-gradient(135deg, #fef3c7, #fffbeb);
}

.stApp {
    background: linear-gradient(180deg, #eaf1ff 0%, #f8fafc 45%, #ffffff 100%);
}

div[data-testid="stExpander"] {
    border-radius: 18px;
    border: 1px solid rgba(148, 163, 184, 0.35);
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.07);
    background: linear-gradient(135deg, #ffffff, #f8fafc);
    margin-bottom: 1rem;
    overflow: hidden;
}

div[data-testid="stExpander"] summary {
    font-size: 1.05rem;
    font-weight: 700;
    padding: 0.85rem 1rem;
    background: linear-gradient(135deg, #f8fafc, #eef2ff);
    border-radius: 18px;
}

div[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
}

hr {
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
    border-color: rgba(148, 163, 184, 0.25);
}

.priority-card {
    border-radius: 18px;
    padding: 1rem 1rem 1.15rem 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.07);
    border: 1px solid rgba(148, 163, 184, 0.20);
    min-height: 260px;
}

.priority-fail-card {
    background: linear-gradient(135deg, #fff7f7, #fff1f2);
    border-left: 6px solid #fca5a5;
}

.priority-review-card {
    background: linear-gradient(135deg, #fffcf2, #fffbeb);
    border-left: 6px solid #fde68a;
}

.priority-badge {
    display: inline-block;
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 700;
    margin-bottom: 0.8rem;
}

.badge-fail {
    background: #fee2e2;
    color: #991b1b;
}

.badge-review {
    background: #fef3c7;
    color: #92400e;
}

.priority-category {
    font-size: 0.9rem;
    font-weight: 700;
    color: #475569;
    margin-bottom: 0.35rem;
}

.priority-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #111827;
    line-height: 1.4;
    margin-bottom: 0.8rem;
}

.priority-section-label {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #64748b;
    margin-top: 0.7rem;
    margin-bottom: 0.25rem;
}

.priority-text {
    font-size: 0.92rem;
    color: #334155;
    line-height: 1.5;
}
            
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 18px;
    background: linear-gradient(135deg, #ffffff, #f8fafc);
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
}

#snapshot css addition
            
html, body, [class*="css"] {
    font-family: "Inter", "Segoe UI", Arial, sans-serif;
}

.snapshot-card,
.priority-card,
.metric-card,
.dashboard-title,
.dashboard-subtitle {
    font-family: "Inter", "Segoe UI", Arial, sans-serif;
}

.snapshot-card {
    border-radius: 0;
    padding: 0.65rem 0.85rem 0.75rem 0.85rem;
    margin-bottom: 0;
    border-bottom: 1.5px solid rgba(148, 163, 184, 0.28);
    display: flex;
    align-items: flex-start;
    gap: 0.7rem;
    max-width: 100%;
}

.snapshot-pass {
    background: #f8fffa;
    border-left: 4px solid #86efac;
}

.snapshot-fail {
    background: #fff8f8;
    border-left: 4px solid #fca5a5;
}

.snapshot-review {
    background: #fffdf5;
    border-left: 4px solid #fde68a;

}

.snapshot-icon {
    font-size: 1rem;
    line-height: 1.3;
    min-width: 1.25rem;
    margin-top: 0.05rem;
}

.snapshot-content {
    flex: 1;
}

.snapshot-status {
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #121314;
    margin-bottom: 0.18rem;
}

.snapshot-control {
    font-size: 0.9rem;
    font-weight: 500;
    color: #111827;
    line-height: 1.35;
}

</style>
""", unsafe_allow_html=True)

brand_banner = (
    '<div style="'
    'display:flex;'
    'align-items:center;'
    'justify-content:space-between;'
    'padding:1rem 1.2rem;'
    'margin-bottom:1.2rem;'
    'border-radius:18px;'
    'background:linear-gradient(135deg, #0f172a, #1e3a8a);'
    'color:white;'
    'box-shadow:0 6px 18px rgba(15, 23, 42, 0.18);'
    '">'
        '<div style="display:flex; align-items:center; gap:0.9rem;">'
            '<div style="'
            'width:42px;'
            'height:42px;'
            'border-radius:14px;'
            'background:rgba(255,255,255,0.16);'
            'display:flex;'
            'align-items:center;'
            'justify-content:center;'
            'font-size:1.4rem;'
            '">◆</div>'
            '<div>'
                '<div style="font-size:1.25rem; font-weight:800; letter-spacing:0.02em;">'
                'Capstone Enterprises'
                '</div>'
                '<div style="font-size:0.85rem; opacity:0.86;">'
                'Internal Compliance Analytics Portal'
                '</div>'
            '</div>'
        '</div>'
        '<div style="'
        'padding:0.35rem 0.75rem;'
        'border-radius:999px;'
        'background:rgba(255,255,255,0.14);'
        'font-size:0.78rem;'
        'font-weight:700;'
        'letter-spacing:0.04em;'
        'text-transform:uppercase;'
        '">'
        'Synthetic Data Demo'
        '</div>'
    '</div>'
)

st.markdown(brand_banner, unsafe_allow_html=True)

st.markdown(
    '<div class="dashboard-title">Compliance Gap Analyzer Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">Upload a control library and evidence dataset to identify compliance gaps, review-needed controls, and priority action areas.</div>',
    unsafe_allow_html=True
)

#endregion
#region TEXT CLEANING & PREPROCESSING
## Prepare text for analysis and convert control requirements
## into structured keyword lists

# Cleans raw text so it can be analyzed consistently
def clean_text(text):
    text = str(text).lower().strip()
    text = text.replace("’", "'").replace("", "'")
    text = re.sub(r"[^a-z0-9\s']", "", text)
    text = text.replace("'", "")
    text = re.sub(r"\s+", " ", text)
    return text

# Splits keyword strings from control library into usable lists
def split_keywords(keyword_string):
    return [k.strip().lower() for k in str(keyword_string).split(",") if k.strip()]

#endregion

#region CORE ANALYZER ENGINE

## Function to evaluate one evidence against one control
## and determine PASS / FAIL / NEEDS REVIEW

def analyze_evidence_against_control(evidence_text, control_row):

    # Step 1: Clean the input text
    text = clean_text(evidence_text)

    # Step 2: Extract keyword groups from control
    required_keywords = split_keywords(control_row["Required_Keywords"])
    optional_keywords = split_keywords(control_row["Optional_Keywords"])
    failure_keywords = split_keywords(control_row["Failure_Indicators"])

    # Step 3: Match keywords in evidence
    required_matches = [kw for kw in required_keywords if kw in text]
    optional_matches = [kw for kw in optional_keywords if kw in text]
    failure_matches = [kw for kw in failure_keywords if kw in text]

    global_review_indicators = [
        "not consistent",
        "not as formal",
        "not formal",
        "cannot say",
        "not documented",
        "not reviewed",
        "not enforced",
        "not always",
        "not sure",
        "cannot confirm",
        "not completely sure",
        "inconsistent",
        "informal",
        "unclear",
        "no clear proof",
        "do not have clear evidence",
        "don't have clear evidence"
    ]
    global_review_matches = [
        phrase for phrase in global_review_indicators
        if phrase in text
    ]

    # Step 4: Detect negation (e.g., "don't", "not", "without")
    negation_words = {"no", "not", "dont", "doesnt", "never", "without"}
    words = text.split()

    negation_flag = False
    for i, word in enumerate(words):
        if word in negation_words:
            window = words[i:i+4]
            window_text = " ".join(window)
            if any(kw in window_text for kw in required_keywords + optional_keywords):
                negation_flag = True
                break

    # Step 5: Calculate weighted score
    score = (len(required_matches) * 2) + (len(optional_matches) * 1) - (len(failure_matches) * 3)

    # Step 6: Apply classification rules
    if len(failure_matches) > 0:
        status = "FAIL"
    elif negation_flag:
        status = "FAIL"
    elif len(global_review_matches) > 0:
        status = "UNKNOWN"
    elif len(required_matches) > 0 and score >= 2:
        status = "PASS"
    else:
        status = "UNKNOWN"

    # Step 7: Return structured result
    return {
        "Required_Matches": required_matches,
        "Optional_Matches": optional_matches,
        "Failure_Matches": failure_matches,
        "Global_Review_Matches": global_review_matches,
        "Negation_Flag": negation_flag,
        "Score": score,
        "Predicted_Status": status
    }

#endregion

#region FILE UPLOAD & DATA LOADING
control_file = st.file_uploader("Upload Control Library CSV", type=["csv"])
evidence_file = st.file_uploader("Upload Evidence Dataset CSV", type=["csv"])

if control_file is not None and evidence_file is not None:
#endregion

#region DATA CLEANING & PREPARATION
    controls = pd.read_csv(control_file, encoding="latin-1")
    evidence = pd.read_csv(evidence_file, encoding="latin-1")

    controls.columns = (
        controls.columns
        .str.replace("\ufeff", "", regex=False)
        .str.replace("ï»¿", "", regex=False)
        .str.strip()
        .str.replace(" ", "_")
)

    evidence.columns = (
        evidence.columns
        .str.replace("\ufeff", "", regex=False)
        .str.replace("ï»¿", "", regex=False)
        .str.strip()
        .str.replace(" ", "_")
)

    evidence["Evidence_Text"] = evidence["Evidence_Text"].astype(str).str.strip()
    evidence = evidence[evidence["Evidence_Text"] != ""]
    evidence = evidence[evidence["Evidence_Text"].str.lower() != "nan"]
    evidence = evidence.reset_index(drop=True)
#endregion

#region OUTPUT - Files Uploaded - Ready
st.success("Files uploaded successfully. Ready to analyze.")
#endregion

#region RUN ANALYSIS

if st.button("Analyze Compliance"):

    # Normalize Control IDs to match between files
    controls["Control_ID"] = controls["Control_ID"].astype(str).str.strip()
    evidence["Control_ID"] = evidence["Control_ID"].astype(str).str.strip()

    if not controls["Control_ID"].astype(str).str.startswith("C").all():
        controls["Control_ID"] = "C" + controls["Control_ID"].astype(str)

    # Run analyzer
    results = []

    for _, ev in evidence.iterrows():
        matching_control = controls[controls["Control_ID"] == ev["Control_ID"]]

        if matching_control.empty:
            st.warning(f"No matching control found for {ev.get('Evidence_ID', 'Unknown')} / {ev['Control_ID']}")
            continue

        ctrl = matching_control.iloc[0]
        result = analyze_evidence_against_control(ev["Evidence_Text"], ctrl)

        results.append({
            "Evidence_ID": ev.get("Evidence_ID", ""),
            "Control_ID": ev["Control_ID"],
            "Control_Type": ctrl.get("Control_Type", ""),
            "Severity": ctrl.get("Severity", 1),
            "Domain_Group": ctrl.get("Domain_Group", ""),
            "Control_Question": ev.get("Control_Question", ""),
            "Control_Description": ctrl["Control_Description"],
            "Evidence_Text": ev["Evidence_Text"],
            "Expected_Status": ev.get("Expected_Status", ""),
            "Score": result["Score"],
            "Predicted_Status": result["Predicted_Status"],
            "Required_Matches": ", ".join(result["Required_Matches"]),
            "Optional_Matches": ", ".join(result["Optional_Matches"]),
            "Failure_Matches": ", ".join(result["Failure_Matches"]),
            "Negation_Flag": result["Negation_Flag"]
        })

    # Build results DataFrame
    results_df = pd.DataFrame(results)

    # Select best result per control
    best_results = results_df.sort_values(
        by=["Evidence_ID", "Score"],
        ascending=[True, False]
    ).drop_duplicates(subset=["Evidence_ID"]).copy()

    # Standardize status labels
    best_results["Predicted_Status"] = best_results["Predicted_Status"].astype(str).str.strip().str.upper()
    best_results["Compliance_Result"] = best_results["Predicted_Status"].replace({
        "PASS": "Passed",
        "FAIL": "Failed",
        "UNKNOWN": "Needs Review"
    })

    # Calculate metrics
    total = len(best_results)
    pass_count = (best_results["Predicted_Status"] == "PASS").sum()
    fail_count = (best_results["Predicted_Status"] == "FAIL").sum()
    unknown_count = (best_results["Predicted_Status"] == "UNKNOWN").sum()

    compliance_pct = round((pass_count / total) * 100, 1) if total > 0 else 0

    # Only calculate model accuracy when Expected_Status contains real labels
    has_expected_status = (
        "Expected_Status" in best_results.columns
        and best_results["Expected_Status"]
        .astype(str)
        .str.strip()
        .str.upper()
        .isin(["PASS", "FAIL", "UNKNOWN"])
        .any()
    )

    if has_expected_status:
        best_results["Expected_Status"] = best_results["Expected_Status"].astype(str).str.strip().str.upper()
        accuracy = round((best_results["Expected_Status"] == best_results["Predicted_Status"]).mean() * 100, 1)
    else:
        accuracy = None

    # -------------------------
    #EXECUTIVE SUMMARY
    # -------------------------


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card overall-card">
            <div class="metric-label">Overall Compliance</div>
            <div class="metric-value">{compliance_pct}%</div>
            <div class="metric-note">{total} total controls analyzed</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card passed-card">
            <div class="metric-label">Passed</div>
            <div class="metric-value">{pass_count}</div>
            <div class="metric-note">Controls meeting requirements</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card failed-card">
            <div class="metric-label">Failed</div>
            <div class="metric-value">{fail_count}</div>
            <div class="metric-note">Controls requiring immediate attention</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card review-card">
            <div class="metric-label">Needs Review</div>
            <div class="metric-value">{unknown_count}</div>
            <div class="metric-note">Controls needing clearer evidence</div>
        </div>
        """, unsafe_allow_html=True)


    # -------------------------
    # COMPLIANCE RISK TREE MAP
    # -------------------------

    import plotly.graph_objects as go

    st.write("")
    st.divider()
    st.subheader("Compliance Risk Map")
    st.write(
        "This TreeMap visualization groups controls by category. Each block is sized by severity and colored by analyzer result. Hover over each block to view control details."
    )

    risk_map_df = best_results.copy()

    # Make sure Severity is usable for sizing the treemap
    if "Severity" not in risk_map_df.columns:
        risk_map_df["Severity"] = 1

    risk_map_df["Severity"] = pd.to_numeric(
        risk_map_df["Severity"],
        errors="coerce"
    ).fillna(1)

    # Softer, dashboard-friendly colors
    status_colors = {
        "Passed": "#dcfce7",
        "Needs Review": "#fef3c7",
        "Failed": "#fee2e2"
    }

    parent_color = "#a5c1e98e"
    category_color = "#7481AE"

    labels = ["Compliance Risk Treemap"]
    ids = ["root"]
    parents = [""]
    values = [risk_map_df["Severity"].sum()]
    colors = [parent_color]
    customdata = [["", "", "", ""]]
    hovertext = ["Compliance Risk Treemap"]

    # Add category parent boxes
    category_summary = (
        risk_map_df
        .groupby("Control_Type", as_index=False)["Severity"]
        .sum()
        .sort_values("Severity", ascending=False)
    )

    for _, category_row in category_summary.iterrows():
        category = category_row["Control_Type"]
        category_id = f"category_{category}"

        labels.append(category)
        ids.append(category_id)
        parents.append("root")
        values.append(category_row["Severity"])
        colors.append(category_color)
        customdata.append([category, "Category", category_row["Severity"], ""])
        hovertext.append(
            f"<b>{category}</b><br>"
            f"Total Severity Weight: {category_row['Severity']}"
        )


    # Add individual control boxes
    for _, row in risk_map_df.iterrows():
        control_id = str(row["Control_ID"])
        category = str(row["Control_Type"])
        result = str(row["Compliance_Result"])
        severity = row["Severity"]
        description = str(row["Control_Description"])

        labels.append(f"{control_id}<br>{result}")
        ids.append(f"control_{control_id}")
        parents.append(f"category_{category}")
        values.append(severity)
        colors.append(status_colors.get(result, "#e5e7eb"))
        customdata.append([category, result, severity, description])
        hovertext.append(
            f"<b>{control_id}</b><br>"
            f"<b>Control:</b> {html.escape(description)}<br>"
            f"<b>Category:</b> {html.escape(category)}<br>"
            f"<b>Result:</b> {html.escape(result)}<br>"
            f"<b>Severity:</b> {severity}"
        )

    fig = go.Figure(go.Treemap(
        labels=labels,
        ids=ids,
        parents=parents,
        values=values,
        branchvalues="total",
        hovertext=hovertext,
        marker=dict(
            colors=colors,
            line=dict(width=3, color="#ffffff")
        ),
        textfont=dict(
            size=20,
            family="Inter, Segoe UI, Arial, sans-serif",
            color="#1f2937"
        ),
        textposition="middle center",
        hovertemplate="%{hovertext}<extra></extra>",
        tiling=dict(
            pad=5
        )
    ))

    fig.update_layout(
        height=540,
        margin=dict(t=12, l=12, r=12, b=12),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Arial",
            size=15,
            color="#334155"
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=13,
            font_family="Arial",
            font_color="#1f2937",
            bordercolor="#cbd5e1"
        )
    )

    with st.container(border=True):
        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # -------------------------
    # BUSINESS INTERPRETATION
    # -------------------------

    st.write("")

    if fail_count > 0:
        business_finding_title = "Top Business Finding: Immediate attention required"
        business_finding_text = (
            f"The analyzer found {fail_count} failed control(s). "
            "These areas should be reviewed first because the submitted evidence may indicate a compliance gap."
        )
        finding_style = "failed-card"

    elif unknown_count > 0:
        business_finding_title = "Top Business Finding: Evidence needs clarification"
        business_finding_text = (
            f"The analyzer found {unknown_count} control(s) that need review. "
            "This means the company may not have enough clear evidence yet to confirm full compliance."
        )
        finding_style = "review-card"

    else:
        business_finding_title = "Top Business Finding: Strong compliance coverage"
        business_finding_text = (
            "All submitted controls passed the analyzer check. "
            "No immediate compliance gaps were identified in this evidence set."
        )
        finding_style = "passed-card"

    st.markdown(f"""
    <div class="metric-card {finding_style}" style="min-height: 115px;">
        <div class="metric-label">{business_finding_title}</div>
        <div class="metric-note" style="font-size: 1rem; line-height: 1.6;">
            {business_finding_text}
        </div>
    </div>
    """, unsafe_allow_html=True)
    

    # Create clean user-facing results table
    display_results = best_results[[
        "Control_ID",
        "Control_Type",
        "Control_Description",
        "Compliance_Result",
        "Evidence_Text"
    ]].rename(columns={
        "Control_ID": "Control ID",
        "Control_Type": "Control Category",
        "Control_Description": "Control Requirement",
        "Compliance_Result": "Compliance Result",
        "Evidence_Text": "Submitted Evidence"
    })

    # Areas needing attention
    needs_work = display_results[
        display_results["Compliance Result"].isin(["Failed", "Needs Review"])
    ]



    # -------------------------
    # PRIORITY ACTION PLAN
    # -------------------------

    st.write("")
    st.write("")
    st.divider()
    st.subheader("Priority Action Plan")
    st.write(
        "This section translates the analyzer results into business actions so the company can "
        "focus on the controls that need attention first."
    )
    # -------------------------
    # 10-CONTROL REVIEW SNAPSHOT
    # -------------------------


    with st.container(border=True):
        st.markdown("#### ITCG Score Snapshot")
        st.write(
            "This snapshot shows the result of each control in the review library at a glance."
        )

        snapshot_results = display_results.copy()

        status_sort = {
            "Failed": 1,
            "Needs Review": 2,
            "Passed": 3
        }

        snapshot_results["Sort_Order"] = snapshot_results["Compliance Result"].map(status_sort)
        snapshot_results = snapshot_results.sort_values(
            ["Sort_Order", "Control Category", "Control Requirement"]
        ).reset_index(drop=True)

    

        for i, row in snapshot_results.iterrows():
            result = str(row["Compliance Result"])
            control_text = html.escape(str(row["Control Requirement"]))

            if result == "Passed":
                card_class = "snapshot-card snapshot-pass"
                status_text = "✅Passed"
                status_icon = ""
            elif result == "Failed":
                card_class = "snapshot-card snapshot-fail"
                status_text = "❌Failed"
                status_icon = ""
            else:
                card_class = "snapshot-card snapshot-review"
                status_text = "❔Needs Review"
                status_icon = ""

            snapshot_html = (
                f'<div class="{card_class}">'
                f'<div class="snapshot-icon">{status_icon}</div>'
                f'<div class="snapshot-content">'
                f'<div class="snapshot-status">{status_text}</div>'
                f'<div class="snapshot-control">{control_text}</div>'
                f'</div>'
                f'</div>'
            )

            st.markdown(snapshot_html, unsafe_allow_html=True)

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    st.write("")

    failed_items = display_results[display_results["Compliance Result"] == "Failed"]
    review_items = display_results[display_results["Compliance Result"] == "Needs Review"]

    action_col1, action_col2, action_col3 = st.columns(3)

    with action_col1:
        st.markdown(f"""
        <div class="metric-card failed-card">
            <div class="metric-label">Immediate Action</div>
            <div class="metric-value">{len(failed_items)}</div>
            <div class="metric-note">Failed controls requiring correction or escalation</div>
        </div>
        """, unsafe_allow_html=True)

    with action_col2:
        st.markdown(f"""
        <div class="metric-card review-card">
            <div class="metric-label">Evidence Review</div>
            <div class="metric-value">{len(review_items)}</div>
            <div class="metric-note">Controls needing clearer documentation</div>
        </div>
        """, unsafe_allow_html=True)

    with action_col3:
        if needs_work.empty:
            top_focus_area = "None"
            top_focus_count = 0
            top_focus_note = "No follow-up areas found"
        else:
            top_focus_area = needs_work["Control Category"].value_counts().idxmax()
            top_focus_count = needs_work["Control Category"].value_counts().max()
            top_focus_note = "Category with the most follow-up items"

        st.markdown(f"""
        <div class="metric-card overall-card">
            <div class="metric-label">Top Focus Area</div>
            <div class="metric-value" style="font-size: 1.6rem;">{top_focus_area}</div>
            <div class="metric-note">{top_focus_count} item(s) • {top_focus_note}</div>
        </div>
        """, unsafe_allow_html=True)

    if needs_work.empty:
        st.success("No priority action items were found. All submitted controls passed the analyzer check.")
    else:
        st.markdown("#### Priority Controls")
        st.write(
            "These are the specific controls the company should focus on next based on failed "
            "or review-needed results."
        )

        priority_cards = needs_work.copy()

        priority_cards["Sort_Order"] = priority_cards["Compliance Result"].map({
            "Failed": 1,
            "Needs Review": 2
        })

        priority_cards["Recommended Action"] = priority_cards["Compliance Result"].map({
            "Failed": "Correct the control gap or escalate for immediate remediation.",
            "Needs Review": "Gather clearer evidence or supporting documentation before confirming compliance."
        })

        priority_cards = priority_cards.sort_values(
            ["Sort_Order", "Control Category"]
        ).reset_index(drop=True)

        card_col1, card_col2 = st.columns(2)

        for i, row in priority_cards.iterrows():
            if row["Compliance Result"] == "Failed":
                card_class = "priority-card priority-fail-card"
                badge_class = "priority-badge badge-fail"
                badge_text = "Immediate Action"
            else:
                card_class = "priority-card priority-review-card"
                badge_class = "priority-badge badge-review"
                badge_text = "Needs Review"

            target_col = card_col1 if i % 2 == 0 else card_col2

            category = html.escape(str(row["Control Category"]))
            requirement = html.escape(str(row["Control Requirement"]))
            evidence_text = html.escape(str(row["Submitted Evidence"]))
            recommended_action = html.escape(str(row["Recommended Action"]))

            card_html = (
                f'<div class="{card_class}">'
                f'<div class="{badge_class}">{badge_text}</div>'
                f'<div class="priority-category">{category}</div>'
                f'<div class="priority-title">{requirement}</div>'
                f'<div class="priority-section-label">Submitted Evidence</div>'
                f'<div class="priority-text">{evidence_text}</div>'
                f'<div class="priority-section-label">Recommended Action</div>'
                f'<div class="priority-text">{recommended_action}</div>'
                f'</div>'
            )

            with target_col:
                st.markdown(card_html, unsafe_allow_html=True)    
    
    # -------------------------
    # COMPANY FOCUS AREAS
    # -------------------------

    st.write("")
    st.divider()
    st.subheader("Company Focus Areas")
    st.write(
        "This section groups results by control category so the company can quickly see "
        "which areas need attention and what evidence caused the finding."
    )

    # Add recommended action guidance for each result
    best_results["Recommended_Action"] = best_results["Compliance_Result"].replace({
        "Passed": "No immediate action needed.",
        "Failed": "Review this control immediately. Evidence may be missing, conflicting, or non-compliant.",
        "Needs Review": "Request clearer evidence or additional documentation before marking this control as compliant."
    })

    # Build a summary by Control Type
    focus_summary = (
        best_results
        .groupby("Control_Type")
        .agg(
            Total_Controls=("Control_ID", "count"),
            Passed=("Compliance_Result", lambda x: (x == "Passed").sum()),
            Failed=("Compliance_Result", lambda x: (x == "Failed").sum()),
            Needs_Review=("Compliance_Result", lambda x: (x == "Needs Review").sum())
        )
        .reset_index()
    )

    # Determine focus status for each control type
    def get_focus_status(row):
        if row["Failed"] > 0:
            return "Immediate Focus"
        elif row["Needs_Review"] > 0:
            return "Needs Review"
        else:
            return "Healthy"

    focus_summary["Focus_Status"] = focus_summary.apply(get_focus_status, axis=1)

    status_order = {
        "Immediate Focus": 1,
        "Needs Review": 2,
        "Healthy": 3
    }

    focus_summary["Sort_Order"] = focus_summary["Focus_Status"].map(status_order)
    focus_summary = focus_summary.sort_values(["Sort_Order", "Control_Type"])

    for _, area in focus_summary.iterrows():
        control_type = area["Control_Type"]
        focus_status = area["Focus_Status"]

        if focus_status == "Immediate Focus":
            icon = "🔴"
            message = "This area has failed controls and should be reviewed first."
        elif focus_status == "Needs Review":
            icon = "🟡"
            message = "This area has evidence that needs clarification before it can be considered compliant."
        else:
            icon = "🟢"
            message = "This area appears healthy based on the submitted evidence."

        expander_title = f"{icon} {control_type} — {focus_status}"

        with st.expander(expander_title, expanded=(focus_status != "Healthy")):
            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Controls Reviewed", int(area["Total_Controls"]))
            c2.metric("Passed", int(area["Passed"]))
            c3.metric("Failed", int(area["Failed"]))
            c4.metric("Needs Review", int(area["Needs_Review"]))

            st.write(f"**Recommended Focus:** {message}")

            area_details = best_results[
                best_results["Control_Type"] == control_type
            ][[
                "Control_ID",
                "Control_Description",
                "Compliance_Result",
                "Evidence_Text",
                "Recommended_Action"
            ]].rename(columns={
                "Control_ID": "Control ID",
                "Control_Description": "Control Requirement",
                "Compliance_Result": "Result",
                "Evidence_Text": "Submitted Evidence",
                "Recommended_Action": "Recommended Action"
            })

            st.dataframe(area_details, use_container_width=True)


    # Keep model accuracy available, but not prominent
    if accuracy is not None:
        with st.expander("Technical Evaluation / Model Diagnostics"):
            st.metric("Model Accuracy", f"{accuracy}%")
    if fail_count > 0:
        st.error("Some controls failed and require immediate attention.")
    elif unknown_count > 0:
        st.warning("Some controls need additional review or clarification.")
    




    # -------------------------
    # DETAILED FINDINGS
    # -------------------------

    st.write("")
    st.write("")
    st.divider()

    with st.expander("Full Results Table", expanded=False):
        st.write(
            "This table provides the complete analyzer output for all submitted controls. "
            "It is included as the full audit trail behind the dashboard summary."
        )

        st.dataframe(display_results, use_container_width=True, hide_index=True)

    # Technical details for professor/demo only
    with st.expander("Technical Details"):
        technical_results = best_results[[
            "Control_ID",
            "Score",
            "Required_Matches",
            "Optional_Matches",
            "Failure_Matches",
            "Negation_Flag"
        ]].rename(columns={
            "Control_ID": "Control ID",
            "Required_Matches": "Detected Control Signals",
            "Optional_Matches": "Supporting Signals",
            "Failure_Matches": "Gap Indicators",
            "Negation_Flag": "Negation Detected"
        })

        st.dataframe(technical_results, use_container_width=True)

    # Download
    csv = best_results.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Results CSV",
        data=csv,
        file_name="final_results.csv",
        mime="text/csv"
    )

#endregion

#region NOTES
#python -m streamlit run app.py
#cd "Desktop\GRAD 26\CAPSTONE\CAPSTONE_FRONTEND"
#pip install matplotlib
#endregion
