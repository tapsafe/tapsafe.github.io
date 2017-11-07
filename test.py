#! venv/bin/python

import os
import subprocess
import threading
from contextlib import contextmanager
from http.server import HTTPServer, SimpleHTTPRequestHandler
from selenium import webdriver
from appium import webdriver as appdriver
from lektor.project import Project

@contextmanager
def ensure_source_connect():
    sc = None
    #Travis has already setup source connect.
    if "TRAVIS_JOB_NUMBER" not in os.environ:
        sc = subprocess.Popen(
            [
                'sc-4.4.9-linux/bin/sc',
                '-u',
                'tapsafe',
                '-i',
                'local'
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        while True:
            line = sc.stdout.readline().decode('utf-8').strip()
            print("SC:", line)
            if "you may start your tests." in line:
                break
        yield
        sc.terminate()
        sc.wait()
        print(sc.stdout.read().decode('utf-8'))
    else:
        yield

@contextmanager
def server():
    print("http.server: localhost:8000")
    os.chdir(Project.discover().get_output_path())
    SimpleHTTPRequestHandler.extensions_map.update(dict([(k, v + ';charset=UTF-8') for k, v in SimpleHTTPRequestHandler.extensions_map.items()]))
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server_thread = threading.Thread(target=lambda: httpd.serve_forever())
    server_thread.start()
    yield
    httpd.shutdown()
    server_thread.join()

@contextmanager
def get_driver(platform, browser, version, res, device="web"):
    print("Selenium:", platform, browser, version, res)
    if device == "web":
        driver = webdriver.Remote(
            desired_capabilities={
                "platform": platform,
                "browserName": browser,
                "version": version,
                "screenResolution": res,
                "tunnel-identifier": os.environ.get("TRAVIS_JOB_NUMBER", "local"),
                "build": os.environ.get("TRAVIS_BUILD_NUMBER", "local")
            },
            command_executor="http://%s:%s@localhost:4445/wd/hub" % (
                os.environ.get("SAUCE_USERNAME", "tapsafe"),
                os.environ["SAUCE_ACCESS_KEY"]
            )
        )
    else:
        driver = appdriver.Remote(
            desired_capabilities={
                "browserName": browser,
                "appiumVersion": "1.7.1",
                "deviceName": device,
                "deviceOrienation": res,
                "platformVersion": version,
                "platformName": platform,
                "tunnel-identifier": os.environ.get("TRAVIS_JOB_NUMBER", "local"),
                "build": os.environ.get("TRAVIS_BUILD_NUMBER", "local")
            },
            command_executor="http://%s:%s@localhost:4445/wd/hub" % (
                os.environ.get("SAUCE_USERNAME", "tapsafe"),
                os.environ["SAUCE_ACCESS_KEY"]
            )
        )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def tests(driver):
    print("Testing: http://localhost:8000")
    driver.get("http://localhost:8000")
    if not "Tapsafe" in driver.title:
        raise Exception("Unable to load page!")

def main():
    with ensure_source_connect():
        with server():
            with get_driver("Windows 10", "MicrosoftEdge", "14.14393", "1280x960") as driver:
                tests(driver)
            with get_driver("Windows 7", "internet explorer", "11.0", "1024x768") as driver:
                tests(driver)
            with get_driver("macOS 10.12", "chrome", "62.0", "2048x1536") as driver:
                tests(driver)
            with get_driver("macOS 10.12", "safari", "11.0", "2048x1536") as driver:
                tests(driver)
            with get_driver("Windows 10", "firefox", "52.0", "1600x1200") as driver:
               tests(driver)
            with get_driver("iOS", "Safari", "11.0", "portrait", "iPhone 8 Simulator") as driver:
                tests(driver)
            with get_driver("iOS", "Safari", "10.3", "portrait", "iPad Air 2 Simulator") as driver:
                tests(driver)
            with get_driver("Android", "Browser", "4.4", "portrait", "Samsung Galaxy S4 GoogleAPI Emulator") as driver:
                tests(driver)


if __name__ == "__main__":
    main()
