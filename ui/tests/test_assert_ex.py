import softest

import softest

from ui.pageobjects.UiUtils.CustomSoftAssert import CustomSoftAssert


class ExampleTest(softest.TestCase):

    def test_example(self):
        cs = CustomSoftAssert()
        self.soft_assert(self.assertEqual, 'Worf', 'wharf', 'Klingon is not ship receptacle')
        self.soft_assert(self.assertTrue, True)
        self.soft_assert(self.assertTrue, False, 'this is basheer......!')

        self.assert_all()
