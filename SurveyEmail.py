import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace these values with your Adobe Experience Platform credentials
CLIENT_ID = '138d949ca44442ff8a9184998a199ab5'
CLIENT_SECRET = 'p8e-TLip9cTnSnO61ufwi2ZHFLPh8rtPufGu'
AEP_DATASET_URL = 'https://dcs.adobedc.net/collection/e5ff437dbb274fa9b4e293297f82d04432cd80e793e37831b6e7fdac73d1804f?syncValidation=false'

# Replace with your sandbox name and authorization token
SANDBOX_NAME = 'capstone-sandbox-9'
AUTH_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3MDgxNjUzMjcwODNfMDFlY2NhODgtZTkzZS00NTJlLWI1MDMtMDZmOGExZDM5ZWEzX3V3MiIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiJleGNfYXBwIiwidXNlcl9pZCI6IjZGOUQyOTgxNjQxN0UzQTYwQTQ5NUZFMUBjNzllN2Q3NDYyYWIyNjc0NDk1YzQyLmUiLCJzdGF0ZSI6IntcInNlc3Npb25cIjpcImh0dHBzOi8vaW1zLW5hMS5hZG9iZWxvZ2luLmNvbS9pbXMvc2Vzc2lvbi92MS9ORE0xWmpoak1tSXROakE0TVMwMFlUSTJMV0U0TW1RdE9UZ3hOMlUzWlRnNVpEVTVMUzFEUTBKR05UZEZRalUwT0RsR1FUVXhNRUUwUXprNFFUVkFZV1J2WW1VdVkyOXRcIn0iLCJhcyI6Imltcy1uYTEiLCJhYV9pZCI6IkNDQkY1N0VCNTQ4OUZBNTEwQTRDOThBNUBhZG9iZS5jb20iLCJjdHAiOjAsImZnIjoiWUdUWTU1SVlYUFA3TUhXS0hPUVYyWEFBVkU9PT09PT0iLCJzaWQiOiIxNzA4MTY0MjgzMjAzXzhjY2QzMWM3LTk5MjItNGFlMy04NTJhLWRlNDNhOTliYjU0MV91dzIiLCJtb2kiOiI2Njg5N2E1NSIsInBiYSI6Ik1lZFNlY05vRVYsTG93U2VjIiwiZXhwaXJlc19pbiI6Ijg2NDAwMDAwIiwiY3JlYXRlZF9hdCI6IjE3MDgxNjUzMjcwODMiLCJzY29wZSI6ImFiLm1hbmFnZSxhY2NvdW50X2NsdXN0ZXIucmVhZCxhZGRpdGlvbmFsX2luZm8sYWRkaXRpb25hbF9pbmZvLmpvYl9mdW5jdGlvbixhZGRpdGlvbmFsX2luZm8ucHJvamVjdGVkUHJvZHVjdENvbnRleHQsYWRkaXRpb25hbF9pbmZvLnJvbGVzLEFkb2JlSUQsYWRvYmVpby5hcHByZWdpc3RyeS5yZWFkLGFkb2JlaW9fYXBpLGF1ZGllbmNlbWFuYWdlcl9hcGksY3JlYXRpdmVfY2xvdWQsbXBzLG9wZW5pZCxvcmcucmVhZCxwcHMucmVhZCxyZWFkX29yZ2FuaXphdGlvbnMscmVhZF9wYyxyZWFkX3BjLmFjcCxyZWFkX3BjLmRtYV90YXJ0YW4sc2Vzc2lvbiJ9.iDkNK1pElL_0E6NE-zLmbKtvl6hEJX7eAVazQSwIH-xlqzs2cRiQOQ95rRTqYXSfV7vMVHLJcaZ4hi5Fyv99b6w8yrD-8HnAqRinukQmE5qBjyl1zeFrYT3M-WTlvTy8WwCVGTzyZADsaZeyNJ-F6Cyn1-QiOnF7y02ZnF86lSJYpcp31uE6F9J-_hSjYpyHB0DLvUUFyYYsLYoF-MbvMwZ6ttCe3F6uzcB1b9wd7TTujF9-oVxGBWjo-iw5cjfU8dgKPVDUpyGquAsnhAOca43r1TTLRH5VPfU9UdyzD-Ewr7Mi07rIQzDupAyXarzsBcNkQ6ED6z-mn_K3UFRAcQ'

def send_to_aep(data):
    headers = {
        'Content-Type': 'application/json',
        'sandbox-name': SANDBOX_NAME,
        'Authorization': AUTH_TOKEN
    }
    response = requests.post(AEP_DATASET_URL, json=data, headers=headers)
    return response.json()

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    # Extract feedback data from the form submission
    product = request.form.get('product')
    print (product)
    feedback_comment = request.form.get('feedbackComment')
    print(feedback_comment)
    # Construct the payload for AEP
    data = {
        "header": {
            "schemaRef": {
                "id": "https://ns.adobe.com/acssandboxgdcthree/schemas/1c742ed47da1b4016524f82cc910affc7072b5e543be8b8b",
                "contentType": "application/vnd.adobe.xed-full+json;version=1.0"
            },
            "imsOrgId": "C73F174362AB26490A495EC6@AdobeOrg",
            "datasetId": "65d088435626af2c69c53ece",
            "source": {
                "name": "Streaming dataflow - 02/17/2024, 3:54 PM"
            }
        },
        "body": {
            "xdmMeta": {
                "schemaRef": {
                    "id": "https://ns.adobe.com/acssandboxgdcthree/schemas/1c742ed47da1b4016524f82cc910affc7072b5e543be8b8b",
                    "contentType": "application/vnd.adobe.xed-full+json;version=1.0"
                }
            },
            "xdmEntity": {
                "_acssandboxgdcthree": {
                    "Question1": product,
                    "Question2": product,
                    "Question3": product,
                    "Question4": product,
                    "Question5": feedback_comment
                    # Add more questions as needed
                },
                "_id": "https://www.coke2home.com/"
            }
        }
    }
    
    # Send data to AEP
    response = send_to_aep(data)
    print(data)
    # Handle the response from AEP as needed
    print(response)
    return jsonify({'status': 'success', 'message': 'Feedback sent to AEP'})

if __name__ == '__main__':
    # Run the Flask app
    app.run()
