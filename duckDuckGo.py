import requests
import pytest

url_ddg = "https://api.duckduckgo.com"
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Van Buren", "Harrison", "Tyler", "Polk", "Taylor",
              "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland",
              "Taft", "McKinley", "Roosevelt", "Wilson", "Harding", "Coolidge", "Hoover", "Truman",
              "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"]
def test_ddg0():
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json&pretty=1")
    rsp_data = resp.json()

    assert "Presidents" in rsp_data["Heading"]
    print(rsp_data)

test_ddg0()
