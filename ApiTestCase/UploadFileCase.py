import requests
from urllib3 import encode_multipart_formdata
import json
url="http://192.168.2.200:8083/appVouchers/importAppVouchers"
with open(r"G:\API_project_test\ExcelFile\ticket.xlsx","rb") as f:
    file = {"filename": ("ticket.xlsx",f.read()),"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"}
    encode_data=encode_multipart_formdata(file)
    file_data=encode_data[0]
    head = {"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7opNBKuO9kwLSOXJ",
            "Connection": "keep-alive",
            "Accept - Encoding": "gzip, deflate",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Cookie": "UM_distinctid=16df68e82bf5e0-056d0a6d7d3b92-386a410b-1fa400-16df68e82c03f3; __SDID=1dbd9faf09fbc2fe; Hm_lvt_93626e1499ca6f2f5a8e2cef3a87b746=1571799597,1572401571,1572853515; CNZZDATA1276157369=1676484865-1571799596-%7C1572937319; Hm_lpvt_93626e1499ca6f2f5a8e2cef3a87b746=1572937347; _welfareCompany=cXgCnqL1M+TMeRIcih3d7Ea9AYec776S2wRk5WV/7e86i+AiIcGSBLC9nk0UGi5Su0tcyoZoWi5Ii6FWX1wjYMOlu9A6kN3tlCavvItkIz/FK0yTVNY9NTfMst4l+nocAiMdygnMAE+t+uDr8HMSrtF5tH12Mg12TEEK0vnXClU=; _platform=c4edd85c3099109e1ec3ed9f31fa1e4e; _platformsdd=BT3d9hVMbvqhhH2+LewfuA7UpcfShHYVVG7NSCIyh3+V4PSM18415CD6r1UJ1qed9v3iu4RfpLNMWKsxcPP8xABQKQgcqL4+1RKu3Jvkm39DoPtIGxGB3+rkGFXoGcX3QARK+CAoS5WSDf3SZQlhtHTfZxu41XedbTefJZYqJTQ="}
    r=requests.post(url,headers=head,files=file)
print(r.json())