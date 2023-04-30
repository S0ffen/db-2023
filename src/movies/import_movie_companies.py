import asyncio
from asyncio import run, sleep

from db_class import DbService
from analysis_tools import *


async def main():
    db = DbService()
    await db.initialize()  # tu łączymy się z bazą danych

    companies = get_movie_companies('src/movies/data/tmdb_5000_movies.csv')
    tasks = []

    for i, company in enumerate(companies):
        tasks.append(asyncio.create_task(db.upsert_movie_company(company.company_id, company.movie_id)))
        if i % 100 == 0:
            print(f'import in {i / len(companies) * 100:.1f}% done')
            await asyncio.gather(*tasks)
            tasks = []

    await asyncio.gather(*tasks)
    await sleep(1)
    print('all done')


if __name__ == '__main__':
    run(main())
