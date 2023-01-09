from flask import Flask,jsonify, request
app = Flask(__name__)

books_db= [
    {
      'name': 'secret',
      'price':250
    },
    {
       'name': 'Deep work',
       'price' :347
    }
]
   
@app.route('/books')
def get_all_books():
    return jsonify({'books':books_db})


@app.route('/book/<string:name>') 
def get_book(name):
    for book in books_db:
        if book['name']==name:
            return jsonify(book)
        

    return jsonify({'message':'book not found'})

@app.route('/book',methods=['POST'])
def create_book():
     body_data = request.get_json() 
     print(body_data,"............")
     name=body_data["name"]
     price=body_data["price"]
     print("name..........",name)
     print("price.....",price)
     books_db.append(body_data)
     return jsonify({"message":"book has been created"})


@app.route('/')
def home():
    return "hey"
app.run(port=8000)