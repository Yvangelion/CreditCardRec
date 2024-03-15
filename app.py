from flask import Flask, render_template, request
import json

from src.start import credit_app

app = Flask(__name__, template_folder="templates")

def process_expenses(expense_data):
    try:

        sorted_merged_dict, dining_dict_sorted, travel_dict_sorted, other_dict_sorted = credit_app(expense_data)
        #answer = dining_dict_sorted
        return sorted_merged_dict, dining_dict_sorted, travel_dict_sorted, other_dict_sorted 
    
    except ValueError:
        return {"error": "Invalid input format"}

@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    sorted_merged_dict, dining_dict_sorted, travel_dict_sorted, other_dict_sorted  = None, None, None, None

    if request.method == 'POST':
        user_input = request.form.to_dict()
        dict_ints = {key: int(value) for key, value in user_input.items()}
        sorted_merged_dict, dining_dict_sorted, travel_dict_sorted, other_dict_sorted  = process_expenses(dict_ints)
        response = {}
        response['Best'] = sorted_merged_dict
        print( response['Best'])
        response['Dining'] = dining_dict_sorted
        response['Travel'] = travel_dict_sorted
        response['Other'] = other_dict_sorted

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
