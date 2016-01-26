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
	if exists(LoginPage.button_logout):
		click(LoginPage.button_logout)
		wait(LoginPage.button_enter,10)
	
	click(LoginPage.button_enter)
	wait(LoginPage.button_login)
	click(LoginPage.input_username)
	type(username)
	click(LoginPage.input_password)
	type(password)
	click(LoginPage.button_login)
	wait(LoginPage.button_logout)

def ChangeUrl(url):
	type("l",KeyModifier.CTRL)
	type(url)
	type(Key.ENTER)
	
def CloseBrowser():
	type(Key.F4,KeyModifier.ALT )

def LoginAsAdmin(user,password):
    wait(Login.label,5)
    click(Login.label)
    wait(Login.username)
    type(Login.username,user)
    type(Login.password,password)
    click(Login.submit)
    wait(Login.verify)

def NavigateToAdminModule(module):
    wait(Admin.navigation_label,5)
    click(Admin.navigation_label)
    wait(4)
    wheel(WHEEL_DOWN, 7)
    wait(Admin.homeworkEvaluationLabel,5)
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