########################################################
# UI map for XYZ
########################################################
from sikuli import *
########################################################

class Tils:
    academy_logo = "academy_logo.png"
class Login:
    label="1453418625552.png"
    username = "username.png"
    password = "password.png"
    submit = "submit.png"
    verify = "verify.png"
class Admin:
    navigation_label = "navigation_label.png"
    homeworkEvaluationLabel = "homeworkEvaluationLabel.png"
    
class HomeworkEvaluation:
    dropDownArrow = "dropDownArrow.png"
    courseInput = "courseInput.png"
    courseSelection = "courseSelection.png"
    lectureInput  = "1453421073065.png"
    lectureSelection =Pattern("1453450403854.png").targetOffset(-3,21)
    
    userInput = "userInput.png"
    evaluatedFrom = "evaluatedFrom.png"
    exportToExcelButton = "exportToExcelButton.png"
    backToAdminButton = "backToAdminButton.png"
    excelFileChrome = "excelFileChrome.png"
    excelValidadion = "excelValidadion.png"
    excelDataValidation = "excelValidation.png"
    
class ImportTeamsPage:
    teamwork_dropdown = "teamwork_dropdown.png"
    select_teamworkO = "select_teamworkO.png"
    select_TeamworkP = "select_TeamworkP.png"
    set_number_users = Pattern("set_number_users.png").targetOffset(90,0)
    select_teamname = Pattern("select_teamname.png").similar(0.89)
    set_teamname = Pattern("set_teamname.png").similar(0.88)
    wheel_target = Pattern("wheel_target.png").similar(0.75)
    select_files = "select_files.png"
    file_name = "file_name.png"
    open_button = "open_button.png"
    exist_importedFile = "exist_importedFile.png"
    column_toSort = Pattern("column_toSort.png").targetOffset(70,0)
    select_column_toSort = Pattern("select_column_toSort.png").similar(0.88)
    import_button = "import_button.png"
    chose_teamworkMessage = Pattern("chose_teamworkMessage.png").exact()
    chose_numberOfUSersMessage = "chose_numberOfUSersMessage.png"
    chose_teamworkNames = "chose_teamworkNames.png"
    chose_fileToImportMessage = "chose_fileToImportMessage.png"
    invalid_importFileMessage = "invalid_importFileMessage.png"
    asert_bug_message = "asert_bug_message.png"
	
class LoginPage:
	button_enter = Pattern("button_enter.png").targetOffset(-40,0)
	button_login = "button_login.png"
	button_logout=Pattern("button_logout.png").similar(0.84)
	wait_label = "wait_label.png"
	input_username = "input_username.png"
	input_password = "input_password.png"
	
	
#Homework Evaluation Responses (HER)
class HER:
	button_enter = "button_enter.png"
	label_hated = "label_hated.png"
	label_haters = "label_haters.png"
	button_arrow = "button_arrow.png"
	label_ivand="label_ivand.png"
	button_all_evals = "button_all_evals.png"
	button_accept_evals = "button_accept_evals.png"
	button_reject_evals = "button_reject_evals.png"

class TeamworkPageClass:
    teamwork_wait_element = "teamwork_wait_element.png"
	
class BonusPointsPage:
    btn_FirstEditBonus = "velizar_btn_FirstEdit_Bonus.png"
    form_BonusEdit2 = "velizar_form_BonusEdit2.png"
    label_Points = "velizar_label_Points.png"
    btn_Update_BonusPoints = "velizar_btn_Update_BonusPoints.png"
    label_Edited = "velizar_label_Edited.png"
    label_777 = "velizar_label_777.png"
    dropDownArrow = "velizar_dropDownArrow_EditingBonusPoins.png"