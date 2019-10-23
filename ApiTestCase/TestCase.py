import unittest
from ExcelUtil import ExcelUtillpy
import ddt
from LogCommon import LogCommonpy
import requests
import json

logger=LogCommonpy.mylog("CaseLog").getlog()
@ddt.ddt
class TestDome(unittest.TestCase):

    def setUp(self):
        self.head={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Cookie": "_platform=721596290b3b28373708375aa9c93353; _platformsdd=fVZHa3uGXJ7ags78DYwxL3jhYelauRY+xgjzcbSM4/mkRkrEL5DbK1mL3zi36ZEhuT"
            "ftu1J5ud9BxeJlFZKRGIwhgWYJ7N7lJvvLgOGF58m3gR8lpYGlxBpxLMx0Jz2+6yFOllKUQ+eznHtaQX9EYNstL+IIXpY8oGA/aqanaSU="}

    CaseData = ExcelUtillpy.ReadExcel(r"G:\API_project_test\ExcelFile\casedata.xlsx", "API_Add_Org_Data")
    @ddt.data(*CaseData.getValue())
    def test_case(self,data):
        api_url,org_name,porgld,phone,address,expect_result=tuple(data)
        logger.info("新增组织接口测试")
        "新增组织接口测试"
        url = api_url
        payload = {"orgName": org_name, "pOrgld": porgld, "phone": phone, "address": address}
        r = requests.post(url, data=payload, headers=self.head)
        self.assertEqual(r.json()["msg"],expect_result)



if __name__=="__main__":
    unittest.main()

