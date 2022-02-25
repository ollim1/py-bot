import os
import time
import sys
import argparse
import multiprocessing as mp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

dirname = os.path.dirname(__file__)
driverfile = os.path.join(dirname, "ext/chromedriver")

def worker(opts):
    print("starting instance " + str(opts["instance"]))
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("force-device-scale-factor=" + opts["scale"])
    driver = webdriver.Chrome(options=options, service=Service(driverfile))
    driver.get(opts["url"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Open url in n windows")
    parser.add_argument("-l")
    parser.add_argument("-n")
    parser.add_argument("-s")
    instances = 4
    args = parser.parse_args()

    if args.l is None:
        print("no location specified")
        sys.exit()
    else:
        url = args.l
    if args.n is None:
        instances = 4
    else:
        instances = int(args.n)
    if args.s is None:
        scale = "1"
    else:
        scale = args.s

    t = []
    for i in range(instances):
        t.append({
            "url": url,
            "instance": i,
            "scale": scale
            })

    p = mp.Pool()
    p.map(worker, t)
    p.close()
    p.join()
