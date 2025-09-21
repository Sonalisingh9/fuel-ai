from flask import Flask, render_template
import os

app = Flask(__name__)

# URLs of your deployed services
SERVICE_1_URL = "https://rag-agent-736626534462.us-central1.run.app/"
SERVICE_2_URL = "https://fuel-ai-736626534462.us-central1.run.app/"

@app.route("/")
def index():
    return render_template(
        "index.html",
        service1=SERVICE_1_URL,
        service2=SERVICE_2_URL,
        service1_desc="Holistic Decision Making: Cement plants are data-rich but insight-poor. Critical information is trapped in disconnected silos: sensor data, lab tests, ERP systems, and operator logbooks. When a problem occurs, engineers hunt for answers manually. This slow, inefficient process means critical operational questions take hours or days to answer, leading to extended downtime and lost revenue. ",
        service2_desc="Kiln Optimization (Alternate Fuel Mix and Clinkerization Process): Operating a cement kiln is a constant struggle between Cost, Compliance, and Quality. Today's control systems are reactive and weren't designed for the unpredictable alternative fuels used to cut costs. This leads to instability, emission breaches, and costly shutdowns. "
    )

@app.route("/ping")
def ping():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
