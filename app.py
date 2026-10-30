from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os

app = Flask(__name__)

# Synthetic demo data only; not collected from real people.
DATA = [
    {"group":"General population","age_band":"18–29","wellbeing_score":68,"stress_level":3.1,"sleep_hours":7.1,"social_support":7.2,"physical_activity_days":3.4},
    {"group":"General population","age_band":"30–44","wellbeing_score":65,"stress_level":3.4,"sleep_hours":7.0,"social_support":7.0,"physical_activity_days":3.2},
    {"group":"General population","age_band":"45–59","wellbeing_score":63,"stress_level":3.2,"sleep_hours":7.2,"social_support":6.8,"physical_activity_days":2.9},
    {"group":"General population","age_band":"60+","wellbeing_score":66,"stress_level":2.8,"sleep_hours":7.4,"social_support":7.1,"physical_activity_days":2.7},
    {"group":"Physical challenges","age_band":"18–29","wellbeing_score":58,"stress_level":3.8,"sleep_hours":6.8,"social_support":6.6,"physical_activity_days":2.4},
    {"group":"Physical challenges","age_band":"30–44","wellbeing_score":55,"stress_level":4.1,"sleep_hours":6.7,"social_support":6.3,"physical_activity_days":2.2},
    {"group":"Physical challenges","age_band":"45–59","wellbeing_score":54,"stress_level":3.9,"sleep_hours":6.9,"social_support":6.2,"physical_activity_days":2.0},
    {"group":"Physical challenges","age_band":"60+","wellbeing_score":57,"stress_level":3.5,"sleep_hours":7.0,"social_support":6.5,"physical_activity_days":1.8},
]
df = pd.DataFrame(DATA)

METRICS = {
    "wellbeing_score": ("Wellbeing score (illustrative 0–100 scale)", "Higher is better"),
    "stress_level": ("Self-reported stress (illustrative 1–5 scale)", "Higher is more stress"),
    "sleep_hours": ("Average sleep (illustrative hours/night)", "Hours per night"),
    "social_support": ("Perceived social support (illustrative 1–10 scale)", "Higher is more support"),
    "physical_activity_days": ("Physical activity (illustrative days/week)", "Days per week"),
}

@app.route("/")
def index():
    metric = request.args.get("metric", "wellbeing_score")
    if metric not in METRICS:
        metric = "wellbeing_score"
    title, subtitle = METRICS[metric]
    summary = df.groupby("group")[metric].mean().round(1).to_dict()
    gap = round(summary.get("General population", 0) - summary.get("Physical challenges", 0), 1)
    fig = px.bar(df, x="age_band", y=metric, color="group", barmode="group",
                 title=title, labels={"age_band":"Age band","group":"Comparison group",metric:title},
                 color_discrete_sequence=["#2563eb", "#14b8a6"])
    fig.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=60, b=20), legend_title_text="")
    chart = pio.to_html(fig, full_html=False, include_plotlyjs="cdn", config={"displayModeBar": False, "responsive": True})
    return render_template("index.html", chart=chart, metric=metric, metrics=METRICS,
                           summary=summary, gap=gap, title=title, subtitle=subtitle)

@app.route("/data")
def download_data():
    return df.to_csv(index=False), 200, {
        "Content-Type": "text/csv; charset=utf-8",
        "Content-Disposition": "attachment; filename=illustrative_mental_health_data.csv"
    }

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
