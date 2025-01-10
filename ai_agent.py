from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import requests
import os
from typing import Optional
import warnings
import json
try:
    from langflow.load import upload_file
except ImportError:
    warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")
    upload_file = None

load_dotenv()


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "98135cfd-4c2f-43d4-b484-e5d1c0b99fd3"
APPLICATION_TOKEN_1 = os.getenv("LANGFLOW_TOKEN")

def dict_to_string(obj, level=0):
    strings = []
    indent = "  " * level  # Indentation for nested levels
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                nested_string = dict_to_string(value, level + 1)
                strings.append(f"{indent}{key}: {nested_string}")
            else:
                strings.append(f"{indent}{key}: {value}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            nested_string = dict_to_string(item, level + 1)
            strings.append(f"{indent}Item {idx + 1}: {nested_string}")
    else:
        strings.append(f"{indent}{obj}")

    return ", ".join(strings)

def get_macros(goals,profile):
    TWEAKS = {
        "TextInput-bugYf": {
            "input_value": ", ".join(goals)
        },
        "TextInput-Kn6PM": {
            "input_value": dict_to_string(profile)
        }
    }
    return run_flow_1("", tweaks=TWEAKS, application_token=APPLICATION_TOKEN_1)

def run_flow_1(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
 
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/macros"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return json.loads(response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"])

# res = get_macros("gender:Female, weight:52kgs, height: 153cm, age:23","muscle gain")
# print(res)

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "98135cfd-4c2f-43d4-b484-e5d1c0b99fd3"
APPLICATION_TOKEN_2 = os.getenv("LANGFLOW_TOKEN_2")

def askai(question, profile):
    TWEAKS = {
        "TextInput-Y2q7Z": {
            "input_value": question
        },
        "TextInput-5FSqa": {
            "input_value": dict_to_string(profile)
        }
    }
    return run_flow_2("",tweaks=TWEAKS, application_token=APPLICATION_TOKEN_2)

# def parse_response(response_json):
#     """Parse the API response dynamically."""
#     try:
#         # Check if outputs exist
#         outputs = response_json.get("outputs", [])
#         if not outputs:
#             return "Error: No outputs in response."

#         # Extract first output
#         first_output = outputs[0].get("outputs", [])
#         if first_output:
#             # Try to retrieve text response
#             text_data = first_output[0].get("results", {}).get("text", {}).get("data", {}).get("text", None)
#             if text_data:
#                 return text_data

#         # Return fallback message if text data isn't found
#         return "Error: No valid text response in outputs."
#     except (KeyError, IndexError) as e:
#         print(f"Error parsing response: {e}")
#         return "Error: Unable to parse API response."


def run_flow_2(message: str,
  
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
  
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/ask-ai"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    # # Debug: Print raw response
    # print("Raw API Response:", response.text)

    # try:
    #     response_json = response.json()
    #     print("Parsed API Response:", response_json)
    #     return parse_response(response_json)  # Use the parser
    # except ValueError as e:
    #     print("Error parsing JSON:", e)
    #     return "Error: Unable to parse response"
 
    return response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]

    

advice = askai("give me a good chest workout", "gender:Female, weight:52kgs, height: 153cm, age:23")
print(advice)