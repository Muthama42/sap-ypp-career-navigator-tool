# SAP YPP Career Navigator Tool

Empower your SAP career journey with data-driven, AI-powered personalized recommendations.

---

## 🚀 What is this?

The SAP YPP Career Navigator Tool is a web app for SAP Young Professionals Program (YPP) graduates. It uses AI (Google Gemini) and real job market data to:
- Analyze your current SAP certificates, technical and non-technical skills, and interests
- Recommend the best next SAP certifications (max 4, based on your profile and market demand)
- Provide a personalized career path, skill gap analysis, and actionable next steps

---

## 🖥️ How to Use

1. **Go to the app:** [Streamlit Cloud Link](YOUR-STREAMLIT-URL-HERE)
2. **Fill in your profile:** Select your current SAP certs, skills, interests, and dream job.
3. **Get your dashboard:** See your personalized career roadmap, skill gap, and top certificate recommendations.

---

## 🛠️ Local Development

1. Clone the repo:
   ```sh
   git clone https://github.com/Muthama42/sap-ypp-career-navigator-tool.git
   cd sap-ypp-career-navigator-tool
   ```
2. Install requirements:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the app:
   ```sh
   streamlit run app.py
   ```

---

## 🌐 Deploy Your Own

- Fork this repo and deploy on [Streamlit Cloud](https://streamlit.io/cloud)
- Set your Gemini API key as a secret (`GEMINI_API_KEY`)
- Share your app link!

---

## 📁 Project Structure

```
app.py
requirements.txt
data/
  sap_certificates.csv
sap_ypp_career_navigator/
  __init__.py
  data_utils.py
  nlp.py
  recommender.py
  gemini_agent.py
```

---

## 🙏 Credits

- Built by Muthama42 and contributors
- Powered by Google Gemini and Streamlit 