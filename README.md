# RecomBook

A book recommender system using user-based Collaborative Filtering.

* Project website: <https://recom.soleyman.xyz>
* Dataset link: <https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset>

## How to run locally

* Clone the repository and `cd` into it.
* Create a virtual environment and activate it.
* Install the requirements using `pip install -r requirements.txt`.
* Run the app using `python app.py`.
* Open `localhost:5000` in your browser.

## Technology stack used

* [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.
* [Flask](https://flask.palletsprojects.com/): Web framework for Python.
* [Matplotlib](https://matplotlib.org/): For data visualization.
* [Jupyter Notebook](https://jupyter.org/): For data exploration and visualization.
* Numpy, JavaScript, HTML, CSS, Bootstrap, etc.

## Description

The dataset contains 278858 users, 1149780 ratings and 271360 books. It might take some time to load the search bar as it is using a large dataset _(it sits on my economic server)_. All the trained models are saved in the [`models`](model/) folder. The [`data`](data/) folder contains the dataset and the [`recommender.ipynb`](recommender.ipynb)  Jupyter notebooks used for data exploration and visualization.

* Content-based filtering is used to provide popular 50 books to users.
* The logic for user-based collaborative filtering is how many votes a user has given to a book. Books with more than 250 votes are considered for popularity.
* Number of votes and average rating of a book is shown in the popular books section.

![homepage](https://user-images.githubusercontent.com/13655344/188255792-d5391127-79ff-4aa8-b3b3-a5ce34f0e82a.PNG)

Then, user-based collaborative filtering is used to recommend books to users based on their ratings.

* Entering at least 3 characters in the search bar will show the top 5 books that match the search query.
* It searches within the entire exported model, not just the popular 50 books.

![book-suggestions](https://user-images.githubusercontent.com/13655344/188255911-dc23d919-39ad-4124-9565-965b0bfa918e.PNG)

* Once user enter a book name, and press the search button, the recommended 10 books will be shown.
* For example, if a user likes the book `1984`, the system will recommend 10 books that are similar to it.

![suggested_books](https://user-images.githubusercontent.com/13655344/188256267-2a97962a-4e8c-4c59-9078-b43e0ff08888.png)

## License

MIT License
