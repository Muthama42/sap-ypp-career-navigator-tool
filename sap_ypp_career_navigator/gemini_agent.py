import google.generativeai as genai

def get_gemini_recommendation(user_profile, extracted_keywords, certificates_df, api_key):
    """
    Calls Gemini with a prompt including the user profile, extracted keywords, and available certificates.
    Returns the AI-generated recommendation as a string.
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = f"""You are an SAP career advisor. Given this user profile: {user_profile}, extracted keywords: {extracted_keywords}, and these available SAP certificates: {certificates_df.head(10).to_string(index=False)}, recommend a personalized SAP career path and skill gap analysis. Be concise and actionable."""
    response = model.generate_content(prompt)
    return response.text 