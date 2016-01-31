import unittest
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path:
    sys.path.append(bdLibPath)
from _lib import *


class BonusPoints(unittest.TestCase):

    def test_100_Edit_BonusPointsEditSuccessId212(self):
        RunBrowserToUrl("iexplore","http://stage.telerikacademy.com")
        wait(Tils.academy_logo, 15)
        if exists(LoginPage.button_enter):
            LoginUser("myadmin2", "mypassword2")

        ChangeUrl("http://stage.telerikacademy.com/Administration_Courses/UsersInCoursesBonuses", BonusPointsPage.btn_FirstEditBonus);sleep(5)

        wait(BonusPointsPage.btn_FirstEditBonus).highlight(3)
        click(BonusPointsPage.btn_FirstEditBonus); sleep(2)
        find(BonusPointsPage.form_BonusEdit2).highlight(3)
        find(BonusPointsPage.label_Points).highlight(2)
        click(BonusPointsPage.label_Points)
        type(Key.BACKSPACE*10);sleep(2)
        type(Key.DELETE*10);sleep(2)
        type("7.77");sleep(2)
        type(Key.TAB);sleep(2)
        type(Key.BACKSPACE*100);sleep(2)
        type("EDITED!");sleep(2)
        find(BonusPointsPage.btn_Update_BonusPoints).highlight(2)
        click(BonusPointsPage.btn_Update_BonusPoints); sleep(2)
        type(Key.F5); sleep(5)
        find(BonusPointsPage.label_Edited).right(1200).highlight(3)
        find(BonusPointsPage.label_777).highlight(3)
        reg = find(BonusPointsPage.label_Edited).right(1200)

        assert reg.exists(BonusPointsPage.label_777)

        #Returning back to start situation
        wait(BonusPointsPage.btn_FirstEditBonus).highlight(3)
        click(BonusPointsPage.btn_FirstEditBonus); sleep(2)
        find(BonusPointsPage.label_Points).highlight(2)
        click(BonusPointsPage.label_Points)
        type(Key.BACKSPACE*10);sleep(2)
        type(Key.DELETE*10);sleep(2)
        type("6.3")
        type(Key.TAB);sleep(2)
        type(Key.BACKSPACE*100);sleep(2)
        type("Excellent presentation!");sleep(2)
        find(BonusPointsPage.btn_Update_BonusPoints).highlight(2)
        click(BonusPointsPage.btn_Update_BonusPoints); sleep(2)
        type(Key.F5); sleep(5)

        assert not exists(BonusPointsPage.label_Edited)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BonusPoints)
    outfile = open("bonus_points_tests.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Bonus Points Tests Report')
    runner.run(suite)
    outfile.close()