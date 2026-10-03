from pathlib import Path
from datetime import date
import requests

NSE_URL='https://www.nseindia.com/reports-indices-historical-index-data'

class NiftyDownloader:
    def __init__(self,output_dir:str= "data/raw/nse/nifty"):
        self.output_dir=Path(output_dir)
        self.output_dir.mkdir(parents=True,exist_ok=True)

    def download(self,start_date:date,end_date:date):
        headers={
            'User-Agent':("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/140.0.0.0 Safari/537.36")
                ,'Accept':"text/csv,application/csv,*/*",
                "Referer": "https://www.nseindia.com/"

        }
        session=requests.session()
        session.headers.update(headers)

        response=session.get("https://www.nseindia.com/",timeout=30,)
        response.raise_for_status()

        raise NotImplementedError("NSE historical CSV endpoint needs to be wired here.")

