from fastapi import FastAPI
from config.settings import settings

app= FastAPI(
    title='Nifty Forecasting Platform',
    description='This is a Nifty Forecasting Platform',
    version='0.1.0',
    author='Mahadev S'
)

@app.get('/')
def root():
    return {
        'message':f'{settings.app_name} is running',
        'version':settings.app_version,
        'enviroment':settings.enviroment
    }