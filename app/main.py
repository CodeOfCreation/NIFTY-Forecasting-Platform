from fastapi import FastAPI

app= FastAPI(
    title='Nifty Forecasting Platform',
    description='This is a Nifty Forecasting Platform',
    version='0.1.0',
    author='Mahadev S'
)

@app.get('/')
def root():
    return {'message':'Welcome to Nifty Forecasting Platform'}