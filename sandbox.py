from nicegui import ui

with ui.header():
    ui.label('Literature Review')

ui.label('Reviewd papers')

for i in range(10):
    with ui.link(target=f'/paper{i}').style('text-decoration: none').classes('w-full'):
        with ui.card().classes('w-full'):
            ui.label(f'Paper {i}').style('font-size:120%')
        
ui.left_drawer()
ui.right_drawer()

# with ui.footer():
#     ui.label('FOOTER')

ui.run()