from rest_framework_api_key.models import APIKey
api_key, key = APIKey.objects.create_key(name="test")
print(f"::set-output name=api_key::{key}")