import logging
import smtplib

from celery import shared_task
from django.core.mail import send_mail

from config import settings

logger = logging.getLogger(__name__)


@shared_task
def send_registration_mail(email):
    """Функция для приветсвенного письма при регистрации"""

    try:
        send_mail(
            subject='Добро пожаловать в библиотеку',
            message='Регистрация в библиотеку прошла успешно',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )

        logger.info(f'Mail sent to {email}')
    except smtplib.SMTPException as e:
        # Обработка исключения SMTPError
        logger.error(f'Failed to send email: {str(e)}')
