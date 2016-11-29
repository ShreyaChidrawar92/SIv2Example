from django.test import TestCase
from v2example.models import SDM

class TestCSDL(TestCase):
    _Project_id = 2532


    def test_projects_Exists(self):

        projectCount = SDM.fetch_projects_count()
        #self.assertGreaterEqual(projectCount,1,'Projects does not exist')
        print 'projectCount are ', projectCount

    #def check_csdl_scores(self):

    def test_Process_product_score(self):

        csdlProcessScore = 100
        csdlComplianceScore = 80
        for rec in SDM.fetch_project():
            RECORD_NUMBER, PF_NAME, PRJ_NAME, VERSION, METRIC_ID, METRIC_PER_VALUE, METRIC_STATUS, LVL, TYPE, EC_TARGET_DATE, FCS_TARGET_DATE, MODIFIED_DATE, BE, TG, BU, SEC_OWNERS = rec
            #print 'Record', METRIC_ID
            if METRIC_ID == '10':
                self.assertGreaterEqual(csdlProcessScore, METRIC_PER_VALUE, msg='Process score has been dropped')

            if METRIC_ID == '20':
                self.assertGreaterEqual(csdlComplianceScore, METRIC_PER_VALUE, msg='Compliance score has been dropped')


    def test_to_getProject(self):

        csdl_proj = SDM.getProject(self.CSDL_Project_id)
        #print 'csdl_projs is ', csdl_proj
        rec_no, = csdl_proj
        print 'record Number',rec_no
        self.assertTrue(csdl_proj)
        self.assertEqual(rec_no, self.CSDL_Project_id)






