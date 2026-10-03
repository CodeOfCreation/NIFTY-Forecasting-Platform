from datetime import date

from pipelines.nse.nifty_downloader import NiftyDownloader

def main():
    downloader=NiftyDownloader()

    downloader.download(start_date=date(2020,1,1),end_date=date(2020,12,31))

if __name__=='__main__':
    main()