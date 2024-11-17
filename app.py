from nicegui import ui
import yaml
import time
import pandas as pd
import os

if os.path.exists('data.csv'):
    data = pd.read_csv('data.csv')
else:
    data = pd.DataFrame(columns=['title', 'authors', 'journal', 
                                 'publication_date', 'abstract', 
                                 'rating', 'review', 'time_of_review'])
    data.to_csv('data.csv', index=False)
all_data = []

def save_review(components):
    title, authors, journal, date, abstract, rating, review = components
    # print(title.value)
    ui.notify('saved review!')
    data = dict()
    data['title'] = title.value
    data['authors'] = authors.value
    data['journal'] = journal.value
    data['publication_date'] = date.value
    data['abstract'] = abstract.value
    data['rating'] = rating.value
    data['review'] = review.value
    data['time_of_review']  = time.time()
    all_data.append(data)
    with open('data.yml', 'a') as outfile:
        yaml.dump(all_data, outfile)
    ui.navigate.to('/')

@ui.page('/')
def home():
    with open('data.yml', 'r') as file:
        data = yaml.safe_load(file)
    ui.label('saved reviews').style('font-size:200%')
    
    for review in data:
        with ui.card():
            ui.label(review['title']).style('font-size:120%')
            ui.label(review['authors']).style('font-size:120%')
            ui.label(review['journal']).style('font-size:120%')
            ui.label(review['publication_date']).style('font-size:120%')
            ui.label(review['abstract']).style('font-size:120%')
            ui.label(f'rating - {review["rating"]}').style('font-size:120%')
            ui.label(review['review']).style('font-size:120%')
            authors = review['authors']
            journal = review['journal']
            date = review['publication_date']
            abstract = review['abstract']
            rating = review['rating']
            review = review['review']

    ui.button('add review', on_click= lambda: ui.navigate.to('/add_review')).style('font-size:120%')

@ui.page('/add_review')
def add_review():
    ui.label('literature review').style('font-size:200%')
    title = ui.input(label='title').props('size=120')
    authors = ui.input(label='authors').props('size=120')
    journal = ui.input(label='journal').props('size=120')
    with ui.input('publication date') as date:
        with date.add_slot('append'):
            ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
        with ui.menu() as menu:
            ui.date().bind_value(date)
    abstract = ui.textarea(label='abstract').classes('w-full h-full large-textarea')

    ui.label('rating').style('font-size:120%')
    rating = ui.radio([1, 2, 3, 4, 5], value=1).props('inline')

    review = ui.textarea(label='review').classes('w-full h-full large-textarea')

    components = [title, authors, journal, date, abstract, rating, review]
    save = ui.button('save review', on_click= lambda: save_review(components))

    # define some custom CSS to make the textarea fill the height of the QInput component
    ui.add_head_html('<style>.large-textarea .q-field__control { height: 100%; } </style>')



ui.run()