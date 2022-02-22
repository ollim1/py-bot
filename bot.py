import os
import time
import sys
import argparse
import multiprocessing as mp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

dirname = os.path.dirname(__file__)
driverfile = os.path.join(dirname, "ext/chromedriver")

def worker(tup):
    print("starting instance " + str(tup[1]))
    executable_path = driverfile
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=driverfile)
    driver.get(tup[0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Open url in n windows")
    parser.add_argument("-l")
    parser.add_argument("-n")
    instances = 4
    args = parser.parse_args()

    if args.l is None:
        printf("no location specified")
        sys.exit()
    else:
        url = args.l
    if args.n is None:
        instances = 4
    else:
        instances = int(args.n)

    t = []
    for i in range(instances):
        t.append((url, i))
    p = mp.Pool()
    p.map(worker, t)
    p.close()
    p.join()
