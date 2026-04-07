import requests
import hmac
import hashlib
import base64
import json
from datetime import datetime, timezone

# Configuration
url = "http://127.0.0.1:8000/webhook"
secret = "super_secret_key_12345"

# Payload
payload = {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "occurredOn": datetime.now(timezone.utc).isoformat(),
    "data": {
        "payment": "ANI426541743",
        "reference": "123e4567-e89b-12d3-a456-426614174001",
        "status": "GUARANTEED"
    }
}
raw_body = json.dumps(payload).encode('utf-8')

# Calculate Signature
hmac_obj = hmac.new(secret.encode(), raw_body, hashlib.sha256)
signature = base64.b64encode(hmac_obj.digest()).decode()

# Send Request
headers = {
    "Content-Type": "application/json",
    "Message-Signature": signature
}

response = requests.post(url, data=raw_body, headers=headers)

print(f"Status Code: {response.status_code}") # Should be 204