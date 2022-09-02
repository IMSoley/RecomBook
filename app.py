import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request


# loading the model
popular_books = pickle.load(open('model/popular_books.pkl', 'rb'))
books = pickle.load(open('model/books.pkl', 'rb'))
p_table = pickle.load(open('model/p_table.pkl', 'rb'))
similarity_matrix = pickle.load(open('model/similarity_matrix.pkl', 'rb'))

books_dict = pickle.load(open('model/books_dict.pkl', 'rb'))
books_dict = pd.DataFrame(books_dict)


app = Flask(__name__)


@app.route('/recommend', methods=['POST', 'GET'])
def recommend_books():
    web_title = ["Popular 50 Books", "Recommended 10 Books", "Oops! No Books Found"]
    book_error = []
    if request.method == 'POST':
        user_input_book = request.form.get('user_input_book')
        # get index of the book
        try:
            book_index = np.where(p_table.index == user_input_book)[0][0]
        except:
            book_error = "Book not found"
            return render_template('index.html', book_error=book_error, web_title=web_title[2], books_dict=books_dict["Book-Title"].values, books_dict_len=len(books_dict["Book-Title"].values))
        # get similar books
        similar_books = sorted(enumerate(similarity_matrix[book_index]), key=lambda x: x[1], reverse=True)[1:11]
        # get recommended books
        data = []
        for i in similar_books:
            item = []
            temp_item = books[books["Book-Title"] == p_table.index[i[0]]].drop_duplicates("Book-Title")
            item.extend(list(temp_item["Book-Title"].values))
            item.extend(list(temp_item["Book-Author"].values))
            item.extend(list(temp_item["Image-URL-M"].values))
            data.append(item)
        return render_template('index.html', data=data, web_title=web_title[1], books_dict_len=len(books_dict["Book-Title"].values), user_input_book=user_input_book, books_dict=books_dict["Book-Title"].values)
    return render_template('index.html', 
        books_dict=books_dict["Book-Title"].values,
        books_dict_len=len(books_dict["Book-Title"].values),
        book_name=list(popular_books["Book-Title"].values),
        author=list(popular_books["Book-Author"].values),
        image=list(popular_books["Image-URL-M"].values),
        votes=list(popular_books["num_ratings"].values),
        rating=list(popular_books["avg_num_ratings"].values),
        web_title=web_title[0]
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
