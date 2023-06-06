import requests as reqs
from bs4 import BeautifulSoup as BS
import shutil
import sys
import os

ROOT_URL = 'https://data.vision.ee.ethz.ch/cvl/DIV2K/'

def main(root_url, dw_addr):
    root_req = reqs.get(root_url)

    if root_req.status_code != 200:
        raise Exception(f"Server is down at {root_url}")

    soup = BS(root_req.content, 'lxml')
    a_s = soup.select('li > a')
    total_files = len([a for a in a_s if a['href'] is not None and 'DIV2K_train_HR.zip' in a['href']])
    downloaded_files = 0

    for a in a_s:
        url = a['href']
        if url is not None and 'DIV2K_train_HR.zip' in url:
            try:
                print(f"Downloading from {url}")
                fn = url.split('/')[-1]
                addr = f"{dw_addr}/{fn}"
                with reqs.get(url, stream=True) as r:
                    with open(addr, 'wb') as f:
                        shutil.copyfileobj(r.raw, f)

                downloaded_files += 1
                print(f"Downloaded {downloaded_files}/{total_files} files")
                
            except Exception as e:
                print(f"Couldn't download from {url}")
                print(e)

    print("Download completed!")


if __name__ == "__main__":
    download_dir = sys.argv[1]
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    main(ROOT_URL, download_dir)
