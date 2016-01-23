REM Ilia's path
REM set TestRunner="H:\Telerik\QAAcademy\Sikuli\runsikulix.cmd"

REM Ivan's path
set TestRunner="C:\Stuff\Programs\Sikulix\runsikulix.cmd"

REM Pesho's path
REM set TestRunner="C:\Sikuli\runsikulix.cmd"

set TestList="sikuli_tests\%tils_tests.sikuli"

call %TestRunner% -r %TestList%                 

