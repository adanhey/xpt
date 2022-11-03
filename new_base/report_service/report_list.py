from new_base.report_service import *


class Report_list(Report_service_interface):
    def report_list(self, templateFilter,page=1,pagesize=10,reportType=None,name=None):
        # url = '%s/api/report/reports' % self.host
        # data = {
        #     '$page':page,
        #     '$pageSize':pagesize,
        #     'templateFilter': templateFilter
        # }
        # result = self.get_request(url=url, param=data)
        # return result
        pass

b = Report_list()
print(b.report_list(0).text)
