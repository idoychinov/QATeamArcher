import unittest
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class TilsTests(unittest.TestCase):
    
    def test_001_HomeworkEvaluationDownloadCorrectData_Ilia(self):
       RunBrowserToUrl("chrome","http://stage.telerikacademy.com")
       LoginUser("myadmin2", "mypassword2")
       NavigateToAdminModule(Admin.homeworkEvaluationLabel)
       click(find(HomeworkEvaluation.courseInput).right().find(HomeworkEvaluation.dropDownArrow))
       click(HomeworkEvaluation.courseSelection)
       click(find(HomeworkEvaluation.lectureInput).right().find(HomeworkEvaluation.dropDownArrow))
       click(HomeworkEvaluation.lectureSelection)
       type(HomeworkEvaluation.userInput,"ivand"+Key.ENTER); sleep(2)
       click(HomeworkEvaluation.exportToExcelButton)
       click(find(HomeworkEvaluation.excelFileChrome))
       wait(HomeworkEvaluation.excelValidadion,10)
       wait(HomeworkEvaluation.excelDataValidation,10)

    def test_100_Edit_BonusPointsEditSuccessId212(self):
        RunBrowserToUrl("iexplore","http://stage.telerikacademy.com/Administration_Courses/UsersInCoursesBonuses");sleep(5)

        wait("velizar_btn_FirstEdit_Bonus.png").highlight(3)
        click("velizar_btn_FirstEdit_Bonus.png"); sleep(2)
        find("velizar_form_BonusEdit2.png").highlight(3)
        find("velizar_label_Points.png").highlight(2)
        click("velizar_label_Points.png")
        type(Key.BACKSPACE*10);sleep(2)
        type(Key.DELETE*10);sleep(2)
        type("7.77");sleep(2)
        type(Key.TAB);sleep(2)
        type(Key.BACKSPACE*100);sleep(2)
        type("EDITED!");sleep(2)
        find("velizar_btn_Update_BonusPoints.png").highlight(2)
        click("velizar_btn_Update_BonusPoints.png"); sleep(2)
        type(Key.F5); sleep(5)
        find("velizar_label_Edited.png").right(1200).highlight(3)
        find("velizar_label_777.png").highlight(3)
        reg = find("velizar_label_Edited.png").right(1200)

        assert reg.exists("velizar_label_777.png")

        #Returning back to start situation
        wait("velizar_btn_FirstEdit_Bonus.png").highlight(3)
        click("velizar_btn_FirstEdit_Bonus.png"); sleep(2)
        find("velizar_label_Points.png").highlight(2)
        click("velizar_label_Points.png")
        type(Key.BACKSPACE*10);sleep(2)
        type(Key.DELETE*10);sleep(2)
        type("6.3")
        type(Key.TAB);sleep(2)
        type(Key.BACKSPACE*100);sleep(2)
        type("Excellent presentation!");sleep(2)
        find("velizar_btn_Update_BonusPoints.png").highlight(2)
        click("velizar_btn_Update_BonusPoints.png"); sleep(2)
        type(Key.F5); sleep(5)

    def test_101_Edit_BonusPointsEditWithAllCoursesId213(self):
        RunBrowserToUrl("iexplore","http://stage.telerikacademy.com/Administration_Courses/UsersInCoursesBonuses");sleep(5)

        wait("velizar_btn_FirstEdit_Bonus.png").highlight(3)
        click("velizar_btn_FirstEdit_Bonus.png"); sleep(2)
        find("velizar_form_BonusEdit.png").highlight(3)
        find("velizar_dropDownArrow_EditingBonusPoins.png").highlight(3)
        click("velizar_dropDownArrow_EditingBonusPoins.png")
        type(Key.DOWN)
        find("velizar_btn_Update_BonusPoints.png").highlight(2)
        click("velizar_btn_Update_BonusPoints.png"); sleep(2)

        assert not exists(Pattern("velizar_form_BonusEdit2.png").similar(0.81))

    def test_101_Edit_BonusPoints(self):
        RunBrowserToUrl("iexplore","http://stage.telerikacademy.com/Administration_Courses/UsersInCoursesBonuses");sleep(5)

        wait("velizar_btn_FirstEdit_Bonus.png").highlight(3)
        click("velizar_btn_FirstEdit_Bonus.png"); sleep(2)
        find("velizar_form_BonusEdit.png").highlight(3)
        find("velizar_dropDownArrow_EditingBonusPoins.png").highlight(3)
        click("velizar_dropDownArrow_EditingBonusPoins.png")
        type(Key.DOWN)
        find("velizar_btn_Update_BonusPoints.png").highlight(2)
        click("velizar_btn_Update_BonusPoints.png"); sleep(2)

        assert not exists(Pattern("velizar_form_BonusEdit.png").similar(0.81))


    def test_301_HER_Reaction_Available(self):
         HER_helpers.navigateAndOpenGrid()
         ivand = find(HER.label_ivand).highlight(2)
         ivand.left(600).highlight(2).click(HER.button_arrow)
         assert exists (HER.button_all_evals)
         find(HER.button_all_evals).highlight(1)

    def test_302_HER_Reaction_Haters_Accepted(self):
         HER_helpers.navigateAndOpenGrid()
         ivand = find(HER.label_ivand).highlight(2)
         ivand.left(600).highlight(2).click(HER.button_arrow)
         wait(HER.button_accept_evals)
         click(HER.button_accept_evals)
         assert exists (HER.button_accept_evals)
         
    def test_303_HER_Reaction_Haters_Rejected(self):
         HER_helpers.navigateAndOpenGrid()
         ivand = find(HER.label_ivand).highlight(2)
         ivand.left(600).highlight(2).click(HER.button_arrow)
         click(HER.button_reject_evals)
         assert exists (HER.button_accept_evals)
         
    def test_304_HER_Reaction_Hated(self):
         HER_helpers.navigateAndOpenGrid()
         click(HER.label_hated)
         wait(HER.label_ivand)
         ivand = find(HER.label_ivand).highlight(2)
         ivand.left(600).highlight(2).click(HER.button_arrow)
         assert exists (HER.button_all_evals)
         find(HER.button_all_evals).highlight(1)
		
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TilsTests)

    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='TilsTests Report')
    runner.run(suite)
    outfile.close()
