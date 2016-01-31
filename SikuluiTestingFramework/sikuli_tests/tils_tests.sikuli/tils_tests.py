import unittest
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class TilsTests(unittest.TestCase):
    
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
