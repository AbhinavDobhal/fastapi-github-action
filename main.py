from fastapi import FastAPI

app = FastAPI()


@get.get('/')
async def root():
    return {'message': 'Demo for fastapi github action for heroku!'}
