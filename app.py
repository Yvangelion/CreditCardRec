from flask import Flask, render_template, request
import json

from src.start import credit_app

app = Flask(__name__, template_folder="templates")

def process_expenses(expense_data):
    print("1 WE GOOD")
    print(expense_data)
    try:

        answer = credit_app(expense_data)
        print("WE GOOD")
        print(answer)
        
        return answer
    
    except ValueError:
        print("FAIL")
        return {"error": "Invalid input format"}

@app.route('/', methods=['GET', 'POST'])
def home():
    response = None

    if request.method == 'POST':
            user_input = request.form.to_dict()
            dict_ints = {key: int(value) for key, value in user_input.items()}
            response = process_expenses(dict_ints)


    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
