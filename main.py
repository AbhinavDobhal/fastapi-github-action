from fastapi import FastAPI

app = FastAPI()
app = FastAPI(title="EmembrApp1", description="EmembrApp for financial transaction", version="1.0.0",
              openapi_url="/api/openapi.json", docs_url="/api/docs/", redoc_url=None)


@app.get("/")
def main():
    return {'message': 'Demo for fastapi github action for heroku!'}
