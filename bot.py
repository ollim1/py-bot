import os
import time
import multiprocessing as mp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


dirname = os.path.dirname(__file__)
driverfile = os.path.join(dirname, "ext/chromedriver")

def worker(instance):
    print("starting instance " + str(instance))
    executable_path = driverfile
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=driverfile)
    driver.get("https://www.amd.com/en/direct-buy/fi")

if __name__ == "__main__":
    instances = 4
    url = "http://www.amd.com/"
    p = mp.Pool(instances)
    p.map(worker, range(instances))
