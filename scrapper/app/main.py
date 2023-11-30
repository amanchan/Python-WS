from fastapi import FastAPI, Query
from typing import Annotated
from .scrapper import pages, feeds

app=FastAPI(title="Web Scraping using FastAPI",
            description="This app retrieves data from Reuters news website")


@app.get("/pages")
def home_pages(page: Annotated[str | None,
                            Query(title= "Show News Page Data for",
                                  description="business, markets, legal, technology etc")] = 'world'):
    data = pages(page)
    return data


@app.get("/news")
def home_news(page: str | None = 'world',
              category: Annotated[str | None, Query(
                  description="environment, energy etc in business page<br>africa, americas in world page"
              )] = 'africa'):
    data = feeds(page, category)
    return data
