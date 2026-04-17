import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import structlog

log = structlog.get_logger()

_SMTP_HOST = "smtp.gmail.com"
_SMTP_PORT = 587


def send_digest_email(
    username: str,
    app_password: str,
    subject: str,
    html_body: str,
    to: str | None = None,
) -> bool:
    if not username or not app_password:
        log.warning("email_backup_skipped", reason="credentials not configured")
        return False

    recipient = to or username
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = username
    msg["To"] = recipient
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP(_SMTP_HOST, _SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(username, app_password)
            smtp.sendmail(username, [recipient], msg.as_string())
        log.info("email_sent", to=recipient, subject=subject)
        return True
    except Exception as exc:
        log.error("email_failed", error=str(exc))
        return False
