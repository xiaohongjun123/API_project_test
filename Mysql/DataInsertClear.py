import pymysql
from openpyxl import load_workbook

class DataInClrear(object):

    def GetData(self,excelname,sheetname):
        wb=load_workbook(excelname)
        sheet=wb.get_sheet_by_name(sheetname)
        listall=[]
        for row in sheet.rows:
            list=[]
            for cell in row:
                list.append(cell.value)
            listall.append(list)
        return listall

    def Insert(self):
        db=pymysql.connect('192.168.52.128','learn','Aa123456','learn')
        cursor=db.cursor()
        sql="insert into student VALUES ('111','李户籍','男','1978-09-01','95031')"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("unable connetc mysql")

if __name__=="__main__":
    print(DataInClrear().GetData(r"G:\API_New\API_project_test\Mysql\SqlData.xlsx","Sheet1"))



