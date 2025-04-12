import pytest
from unittest.mock import patch
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager

@pytest.mark.asyncio
@patch("app.utils.smtp_connection.smtplib.SMTP")
async def test_send_markdown_email(mock_smtp):
    email_service = EmailService(TemplateManager())
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }
    await email_service.send_user_email(user_data, 'email_verification')

    assert mock_smtp.called
    instance = mock_smtp.return_value.__enter__.return_value
    instance.sendmail.assert_called_once()

