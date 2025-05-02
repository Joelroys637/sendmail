import streamlit as st
import smtplib

# Function to send email
def send_email(sender_email, sender_password, recipient_email, subject, message, limit):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        for _ in range(limit):
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, recipient_email, email_message)

        server.quit()
        return "Emails sent successfully!"
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Email Sender App")

sender_email = 'type mail id'  '''---->create a new mail id'''
sender_password ='xxxx xxxx xxxx xxxx' '''----> create app password  link:https://www.linkedin.com/posts/leo-joel-7384aa19b_python-one-line-code-to-send-the-email-activity-7275465639924809728-VXzr?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC7hkZwBxc55Kk87jOaFugFUoGDLFqkShzk'''
recipient_email = st.text_input("Recipient Email")
subject = st.text_input("Email Subject")
message = st.text_area("Email Message")
limit = st.number_input("Number of Emails to Send", min_value=1, value=1)

if st.button("Send Email"):
    response = send_email(sender_email, sender_password, recipient_email, subject, message, limit)
    st.success(response)
