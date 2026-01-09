import requests
import random
parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean",
}
API_ENDPOINT = "https://opentdb.com/api.php"
questions = []

def retrieve_question_data():
    response = requests.get(API_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    questions = [{"question": item["question"], "correct_answer": item["correct_answer"]} for item in data["results"]]
    
    return questions

question_data = retrieve_question_data()