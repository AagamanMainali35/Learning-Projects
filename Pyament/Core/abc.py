import hmac, hashlib, base64,uuid
SECRET_KEY = "8gBm/:&EnhH.1/q"
transaction_uuid=uuid.uuid4()
total_amount=1000
product_code='EPAYTEST'
signed_field_names = "total_amount,transaction_uuid,product_code"
data_to_sign = f"{total_amount},{transaction_uuid},{product_code}"
signature = base64.b64encode(hmac.new(SECRET_KEY.encode(), data_to_sign.encode(), hashlib.sha256).digest()).decode()
print(signature)
