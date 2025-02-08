from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import uuid
import os

class UserModel(Model):
    """
    DynamoDB Model for User
    """
    class Meta:
        table_name = 'users'
        region = os.getenv('DYNAMODB_REGION', 'us-west-2')  # Fetch region from settings or environment variable
        host = os.getenv('DYNAMODB_LOCAL_HOST', 'http://localhost:8000')  # For local DynamoDB, update as needed

    # Primary key
    id = UnicodeAttribute(hash_key=True, default=lambda: str(uuid.uuid4()))
    
    # Email with uniqueness constraint handled by application logic
    email = UnicodeAttribute()
