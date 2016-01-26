import unittest
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path:
    sys.path.append(bdLibPath)
from _lib import *


class TeamworkPage(unittest.TestCase):

    def test_001_VerifyTeamwork(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com")
        wait(Tils.academy_logo, 15)
        if exists(LoginPage.button_enter):
            LoginUser("myadmin2", "mypassword2")

        ChangeUrl("http://stage.telerikacademy.com/Administration_Teamwork/Teamworks", TeamworkPageClass.teamwork_wait_element)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TeamworkPage)
    outfile = open("teamwork_page_teams.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Teamwork Page test Report')
    runner.run(suite)
    outfile.close()