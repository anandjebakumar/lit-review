#!/usr/bin/env python3
from typing import List

import models
from tortoise import Tortoise

from nicegui import app, ui


async def init_db() -> None:
    await Tortoise.init(db_url='sqlite://db.sqlite3', modules={'models': ['models']})
    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()

app.on_startup(init_db)
app.on_shutdown(close_db)


@ui.refreshable
async def list_of_papers() -> None:
    async def delete(paper: models.Paper) -> None:
        await paper.delete()
        list_of_papers.refresh()

    papers: List[models.Paper] = await models.Paper.all()
    for paper in reversed(papers):
        with ui.card():
            with ui.row().classes('items-center'):
                ui.label(paper.title)
                ui.label(paper.authors)
                ui.button(icon='edit', on_click=lambda p=paper: delete(p)).props('flat')
                ui.button(icon='delete', on_click=lambda p=paper: delete(p)).props('flat')

@ui.page('/')
async def index():
    async def create() -> None:
        await models.Paper.create(title=title.value, authors=authors.value)
        title.value = ''
        authors.value = None
        list_of_papers.refresh()

    with ui.column().classes('mx-auto'):
        with ui.row().classes('w-full items-center px-4'):
            title = ui.input(label='Title')
            authors = ui.input(label='Author')
            ui.button(on_click=create, icon='add').props('flat').classes('ml-auto')
        await list_of_papers()

ui.run()