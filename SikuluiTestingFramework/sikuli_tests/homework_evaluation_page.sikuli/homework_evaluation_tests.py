import unittest
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path:
    sys.path.append(bdLibPath)
from _lib import *

class Homework_Evaluation(unittest.TestCase):

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
       click(HomeworkEvaluation.excelFileChrome)
       wait(HomeworkEvaluation.excelValidadion,10)
       assert exists (HomeworkEvaluation.excelDataValidation)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Homework_Evaluation)
    outfile = open("HomeworkEvaluation.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Homework Evaluation page test Report')
    runner.run(suite)
    outfile.close()