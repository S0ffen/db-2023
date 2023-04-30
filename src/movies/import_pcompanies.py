import asyncio
from asyncio import run, sleep, create_task

from db_class import DbService
from analysis_tools import *


async def main():
    db = DbService()
    await db.initialize()  # tu łączymy się z bazą danych

    p_comanies = get_pcompanies()
    print(len(p_comanies))
    tasks = []

    for i, company in enumerate(p_comanies):
        tasks.append(create_task(db.upsert_company(company)))
        if i % 100 == 0:
            print(f'import in {i / len(p_comanies) * 100:.1f}% done')
            await asyncio.gather(*tasks)
            tasks = []

    await asyncio.gather(*tasks)
    await sleep(1)


if __name__ == '__main__':
    run(main())
