import requests
import os
import dotenv
from google import genai
from datetime import datetime
import json


now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

dotenv.load_dotenv()
client = genai.Client()

TOKEN = os.environ.get("SHEETY_API")

SHEET_ENDPOINT = "https://api.sheety.co/4447bc03f406d1edd84e7511274fa2d3/day38/sheet1"
HEADERS = {
    "Authorization": f'Basic {TOKEN}'
}
def get_sheet():
    response = requests.get(SHEET_ENDPOINT, headers=HEADERS)
    data = response.json().get("sheet1", [])
    return data

def add_data(date, time, exercise, duration, calories):
    body = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    response = requests.post(SHEET_ENDPOINT, json=body, headers=HEADERS)
    return response.json()

def catch_dupes():
    duplicate = True
    sheet_data = get_sheet()
    for item in sheet_data:
        if item.get("date") == inputs.get("date") and item.get("time") == inputs.get("time") and item.get("exercise") == inputs.get("exercise") and item.get("duration") == inputs.get("duration") and item.get("calories") == inputs.get("calories"):
            print("duplicate")
            duplicate = True
            return
        else:
            duplicate = False

    if not duplicate:        
        print("adding data")
        add_data(inputs.get("date"), inputs.get("time"), inputs.get("exercise"), inputs.get("duration"), inputs.get("calories"))
        return


inputs = {
    "date": "",
    "time": "",
    "exercise": "",
    "duration": "",
    "calories": ""
}

def ai_workflow(your_day):
    if len(your_day) < 1:
        return None
    prompt = """
    Here is what you are going to do:
    - You will receive information about somebodies day of exercise.
    - You will process that information into 5 categories. (date, time, exercise, duration, and calories)
    - You will then further process and format each of them according to this template:
        inputs = {
            "date": dd/mm/yyyy,
            "time": 24:00,
            "exercise": str.lower,
            "duration": 24:00,
            "calories": str.int
        }
    - Roughly estimate the calory count as per the exercise and duration.
    - Simplify the exercise. One or two words to describe the exercise.
    - You will lastly respond with only a 1 line formatted json as a string. Again, strictly format as a string.
    """ + f"""
    Here is the information to process:
    "{your_day}"
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return response.text

if __name__ == "__main__":
    prompt = input("Talk about your exercises today:\n> ")
    for _ in range(5):
        try:
            data = ai_workflow(prompt)
        except:
            print("A problem occurred, retrying..")
        else:
            json_string = str(data)
            input_dict = json.loads(json_string)
            input_dict["date"] = date
            print(input_dict)
            
            add_data(date=input_dict.get("date"), time=input_dict.get("time"), exercise=input_dict.get("exercise"), duration=input_dict.get("duration"), calories=input_dict.get("calories"))
            break

print("Sheets updated!")
