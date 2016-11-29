from django.test import TestCase
from v2example.models import SDM


class TestAwareness(TestCase):
    SAcountOnUI = 491
    SOcountOnUI = 150
    fundlwtbeltCountOnUI = 12851
    advwtbeltOnUI = 23689
    gbCountOnUI = 5025
    blueBeltOnUI = 434
    brownBeltOnUI = 166
    blackBeltOnUI = 93
    opensourcecompletedOnUI = 15754
    v0OnUI = 12752
    v1OnUI = 3725
    SAcount, SOcount, fundlwtbeltCount, advwtbelt, gbCount, blueBelt, brownBelt, blackBelt, opensourceCompleted, v0, v1 = SDM.getAwarenessRefreshCounts()


    def test_to_check_SA_counts(self):
        self.assertGreaterEqual(self.SAcountOnUI, self.SAcount ,msg='Security Advocate count is less then expected')

    def test_to_check_SO_counts(self):
        self.assertGreaterEqual(self.SOcountOnUI, self.SOcount, msg='Security Officer count is less then expected')
        print 'SOcountOnUI',self.SOcountOnUI
        print 'SOcount', self.SOcount

    def test_to_check_fundlwtbelt_counts(self):
        self.assertGreaterEqual(self.fundlwtbeltCountOnUI, self.fundlwtbeltCount,msg='Fundamental Whitebelt count is less then expected')

    def test_to_check_advwtbelt_counts(self):
        self.assertGreaterEqual(self.advwtbeltOnUI, self.advwtbelt, msg='Advanced Whitebelt count is less then expected')

    def test_to_check_gbbelt_counts(self):
        self.assertGreaterEqual(self.gbCountOnUI, self.gbCount, msg='Green Belt count is less then expected')

    def test_to_check_bluebelt_counts(self):
        self.assertGreaterEqual(self.blueBeltOnUI, self.blueBelt, msg='Blue Belt count is less then expected')

    def test_to_check_brownbelt_counts(self):
        self.assertGreaterEqual(self.brownBeltOnUI,self.brownBelt, msg='Brown Belt count is less then expected')

    def test_to_check_blackbelt_counts(self):
        self.assertGreaterEqual(self.blackBeltOnUI, self.blackBelt, msg='Black Belt count is less then expected')

    def test_to_check_opensource_completed(self):
        self.assertGreaterEqual(self.opensourcecompletedOnUI, self.opensourceCompleted,msg='Open source count is less then expected')

    def test_to_check_v0_count(self):
        self.assertGreaterEqual(self.v0OnUI, self.v0, msg='v0 count is less then expected')

    def test_to_check_v1_counts(self):
        self.assertGreaterEqual(self.v1OnUI, self.v1, msg='v1 count is less then expected')

        '''
        self.assertGreaterEqual(SOcountOnUI, SOcount, msg='Security Officer count is less then expected')
        self.assertGreaterEqual(fundlwtbeltCountOnUI, fundlwtbeltCount, msg='Fundamental Whitebelt count is less then expected')
        self.assertGreaterEqual(advwtbeltOnUI, advwtbelt, msg='Advanced Whitebelt count is less then expected')
        self.assertGreaterEqual(gbCountOnUI, gbCount, msg='Green Belt count is less then expected')
        self.assertGreaterEqual(blueBeltOnUI, blueBelt, msg='Blue Belt count is less then expected')
        self.assertGreaterEqual(brownBeltOnUI, brownBelt, msg='Brown Belt count is less then expected')
        self.assertGreaterEqual(blackBeltOnUI, blackBelt, msg='Black Belt count is less then expected')
        self.assertGreaterEqual(opensourcecompletedOnUI, opensourceCompleted, msg='Open source count is less then expected')
        self.assertGreaterEqual(v0OnUI, v0, msg='v0 count is less then expected')
        self.assertGreaterEqual(v1OnUI, v1, msg='v1 count is less then expected')
        '''





