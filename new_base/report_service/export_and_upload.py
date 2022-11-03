from new_base.report_service import *


class Report_exec(Report_service_interface):
    def report_export(self, excelConfigId, fileType, queryParam,fileFolderId):
        url = '%s/api/report/exportFile' % self.host
        data = {
            'excelConfigId': excelConfigId,
            'fileType': fileType,
            'exportType': 10100,
            'queryParam': queryParam,
            'fileFolderId': fileFolderId
        }
        result = self.post_request(url=url, json=data)
        return result


b = Report_exec()
token = b.login()
paramquery = {
    "token": 131441,
    "pageNo": "12324523443",
    "pageSize": 10,
    "currentPageNo": "1",
    "currentPageSize": "asdasd"
}
asss = open("cccc.xlsx",'wb')
bsss = b.report_export(excelConfigId="748038044344688640", fileType=1, queryParam=paramquery,fileFolderId="123214315413")
asss.write(bsss.content)
print(bsss.text)
