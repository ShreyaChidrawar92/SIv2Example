class ProjectNewFile:
    def __init__(self, **kwargs):
        self.RECORD_NUMBER = kwargs.get('RECORD_NUMBER')
        self.PF_NAME = kwargs.get('PF_NAME')
        self.PRJ_NAME = kwargs.get('PRJ_NAME')

Projectobject = ProjectNewFile(RECORD_NUMBER='112', PF_NAME='NaMe', PRJ_NAME='PrjName')
print Projectobject.PF_NAME
print Projectobject.RECORD_NUMBER
print Projectobject.PRJ_NAME
