from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def books():
    # gets all books details
    if request.method == 'GET':
        df = pd.read_csv('books.csv')
    arr = []
    for i in range(0, 200):
        x = {
            "title": df["Title"][i],
            "authors": df["Authors"][i],
            "category": df["Category"][i],
            "description": df["Description"][i],
            "pages": df["Pages"][i],
        }

        #  y = json.dumps(x, ensure_ascii = False)
        arr.append(x)
    return {'books': arr}, 200


if __name__ == '__main__':
    app.run(debug=True)