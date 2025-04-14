import logging
from django.contrib.auth import get_user_model
from django.db import migrations

from dotenv import load_dotenv
import os

logger = logging.getLogger(__name__)

def generate_superuser(apps, schema_editor):
    
    load_dotenv()

    USERNAME = os.getenv("ADMIN_USERNAME")
    PASSWORD = os.getenv("ADMIN_PASSWORD")
    EMAIL = os.getenv("ADMIN_EMAIL")

    user = get_user_model()

    if not user.objects.filter(username=USERNAME, email=EMAIL).exists():
        logger.info("Creating new superuser")
        admin = user.objects.create_superuser(
           username=USERNAME, password=PASSWORD, email=EMAIL
        )
        admin.save()
    else:
        logger.info("Superuser already created!")


class Migration(migrations.Migration):

   dependencies = [('planet','0001_initial')]

   operations = [migrations.RunPython(generate_superuser)]