from nicegui import ui

with ui.dialog() as add_review, ui.card():
    ui.button(icon='close', on_click=add_review.close).props('flat').classes('ml-auto')
    ui.input('Hello world!')

with ui.column().classes('mx-auto'):
    with ui.row().classes('w-full px-4'):
        ui.button('Add review', icon='add', on_click=add_review.open).props('flat').classes('ml-auto')

ui.run()