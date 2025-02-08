from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import os

class FormFieldResponse(Model):
    class Meta:
        table_name = "form_field_responses"
        region = os.getenv('DYNAMODB_REGION', 'us-west-2')
        host = os.getenv('DYNAMODB_LOCAL_HOST', 'http://localhost:8000')

    # Composite key: form_response_id as partition key, form_field_id as range key
    form_response_id = UnicodeAttribute(hash_key=True)
    form_field_id = UnicodeAttribute(range_key=True)

    # Store the response value
    value = UnicodeAttribute()
