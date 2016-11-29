from django.db import models
from django.conf import settings
import cx_Oracle


class SDM:
    title = models.CharField(max_length=100)
    CSDL_DB_settings = settings.STAGE_DB['SDM']
    host = CSDL_DB_settings['HOST']
    port = CSDL_DB_settings['PORT']
    SID = CSDL_DB_settings['SID']
    user = CSDL_DB_settings['USER']
    password = CSDL_DB_settings['PASSWORD']

    @classmethod
    def connect(self):
        dsn_tns = cx_Oracle.makedsn(self.host, self.port, self.SID)
        con = cx_Oracle.connect(self.user, self.password, dsn_tns)
        cur = con.cursor()
        return (con, cur)

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        # do something with the book
        return book

    @classmethod
    def getAllProjects(self):
        con, cur = SDM.connect()
        cur.execute(
            'SELECT RECORD_NUMBER, PLATFORM_NAME, VERSION, VERSION_TYPE '
            'FROM SDM_CSDL_PLATFORM_STATUS'
        )
        result = cur.fetchall()
        con.close()
        return result

    @classmethod
    def getProject(self, record_number):
        con, cur = SDM.connect()
        cur.execute(
            'SELECT RECORD_NUMBER FROM XMET_CSDL_PLATFORM_STATUS WHERE RECORD_NUMBER = ' + str(record_number)
        )
        try:
            result = cur.fetchall()[0]
        except IndexError:
            result = None
        con.close()
        return result

    @classmethod
    def getAwarenessRefreshCounts(self):
        con, cur = SDM.connect()
        cur.execute(
            'select SACNT,SOCNT,FUNDLWBCNT,ADVWBCNT,GBCNT,BLUEBELTCNT,BROWNBELTCNT,BLACKBELTCNT,COMPLETED#,V0,V2 '
            'from SDM_AWARENESS_V2_MV where userid=\'crobbins\''
        )
        try:
            result = cur.fetchall()[0]
        except IndexError:
            result = None
        con.close()
        return result

    @classmethod
    def fetch_projects_count(self):
        con, cur = SDM.connect()
        cur.execute("SELECT count(*) FROM SDM_METRICS_CURRENT_MV")
        try:
            result = cur.fetchall()
        except IndexError:
            result = None
        con.close()
        return result

    @classmethod
    def fetch_project(self):
        con, cur = SDM.connect()
        cur.execute("SELECT RECORD_NUMBER, PF_NAME, PRJ_NAME, SDM.VERSION, METRIC_ID, METRIC_PER_VALUE, \
                        METRIC_STATUS, LVL, TYPE, EC_TARGET_DATE, FCS_TARGET_DATE, MODIFIED_DATE, \
                        SDM.BE, SDM.TG, SDM.BU, CSDL.SEC_OWNERS \
                        FROM \
                        SDM_METRICS_CURRENT_MV SDM, \
                        SDM_CSDL_PLATFORM_STATUS CSDL \
                        WHERE \
                        record_number=355 AND \
                        LVL = 3 AND \
                        (TYPE='PRODUCT' OR TYPE='PROJECT') AND \
                        METRIC_ID IN  (10,20,270) AND \
                        ( PF_NAME = PLATFORM_NAME OR PRJ_NAME = PLATFORM_NAME ) AND \
                        NVL (SDM.VERSION, 'X') = NVL (CSDL.VERSION, 'X') \
                        ORDER BY PF_NAME ")
        try:
            result = cur.fetchall()
        except IndexError:
            result = None
        con.close()
        return result
