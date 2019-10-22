import unittest
from ExcelUtil import ExcelUtillpy
import ddt
from LogCommon import LogCommonpy
logger=LogCommonpy.mylog("CaseLog").getlog()
@ddt.ddt
class TestDome(unittest.TestCase):
    CaseData = ExcelUtillpy.ReadExcel(r"G:\API_project_test\ExcelFile\casedata.xlsx", "data")
    @ddt.data(*CaseData.getValue())
    def test_case(self,data):
        logger.info("执行员工工资计算用例")
        "员工工资计算用例"
        try:
            val1, val2, val3,sum= tuple(data)
            sum1=val1+val2+val3
            self.assertEqual(sum1,sum)
        except AssertionError as e:
            logger.error("测试结果错误"+str(e))
            raise AssertionError

if __name__=="__main__":
    unittest.main()

