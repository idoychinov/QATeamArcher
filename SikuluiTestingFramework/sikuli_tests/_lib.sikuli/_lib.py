from sikuli import *
import HTMLTestRunner
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _uimap import *

def RunBrowserToUrl(browser,toUrl):
    #TestAction("Start " +browser +" "+toUrl)
    sleep(0.5)
    type("d",KEY_WIN); sleep(1)
    type("r", KEY_WIN); sleep(1)
    type(browser+" "); sleep(1)
    type(toUrl); sleep(1)
    type(Key.ENTER)


def LoginUser(username,password):
	click(LoginPage.button_enter)
	wait(LoginPage.wait_label, 15)
	click(LoginPage.input_username)
	type(username)
	type(Key.TAB)
	type(password)
	click(LoginPage.button_login)
	wait(LoginPage.button_logout)

def ChangeUrl(url, element):
	type("l",KeyModifier.CTRL)
	type(url)
	type(Key.ENTER)
	wait(element, 10)
	
def CloseBrowser():
	type(Key.F4,KeyModifier.ALT )

def NavigateToAdminModule(module):
    wait(Admin.navigation_label,5)
    click(Admin.navigation_label)
    wait(4)
    wheel(WHEEL_DOWN, 7)
    wait(module,5)
    click(module); sleep(3)

class HER_helpers(object):
	@staticmethod
	def navigateAndOpenGrid():
		RunBrowserToUrl("firefox", "http://stage.telerikacademy.com")
		wait(Tils.academy_logo, 15)
		LoginUser("TeamArcher","teamarcher")
		ChangeUrl("http://stage.telerikacademy.com/Administration_Courses/HomeworkEvaluationReactions")
		wait(HER.label_haters)
		type(Key.PAGE_DOWN)
		sleep(1)