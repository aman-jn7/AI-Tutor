import yagmail
import os
import markdown2
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_study_plan_email(to_email: str, topic: str, study_plan: str):
    try:
        # If study_plan is an AIMessage object, extract its content
        if hasattr(study_plan, 'content'):
            study_plan = study_plan.content

        # Convert Markdown to HTML
        html_study_plan = markdown2.markdown(study_plan)

        yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)

        subject = f"Your Study Plan for: {topic} - Tailored to Your Learning Journey"

        content = f"""
        <html>
        <body>
        <p>Hello 👋,</p>

        <p>We are excited to present your personalized study plan for <strong>{topic}</strong>:</p>

        {html_study_plan}

        <p>Happy learning! 🚀<br>
        Best of Luck with your studies! 📚 ✨<br>
        — AI Tutor Team</p>
        </body>
        </html>
        """

        yag.send(to=to_email, subject=subject, contents=content)
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False