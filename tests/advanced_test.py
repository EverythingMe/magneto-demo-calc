# coding=utf-8
from magneto.base import BaseTestCase
from magneto.utils.assertion import Assert


class TestAdvanced(BaseTestCase):
    """
    Test advanced app features on drawer
    """

    def setup_method(self, method):
        delete = self.magneto(textMatches='del|clr')
        delete.long_click()

    def test_drawer_by_gesture(self):
        """
        Test drawer in/out by swipe
        """

        content = self.magneto(resourceId='android:id/content')
        sin_button = self.magneto(resourceId='me.everything.magnetodemo:id/fun_sin')

        # check that drawer has no inner elements
        Assert.false(sin_button.exists)

        # swipe it in
        content.swipe.left()

        # check that drawer is populated
        Assert.true(sin_button.exists)

        # swipe drawer back
        self.magneto.press.back()

    def test_drawer_by_orientation(self):
        """
        Test drawer in/out by orientation change
        """

        # check that the sin button is hidden
        sin_button = self.magneto(resourceId='me.everything.magnetodemo:id/fun_sin')
        Assert.false(sin_button.exists)

        # change to landscape
        self.magneto.orientation = 'r'
        self.magneto.wait.idle()

        # check that the sin button is visible
        Assert.true(sin_button.exists)

        # change back
        self.magneto.orientation = 'n'
        self.magneto.wait.idle()

    def test_power(self):
        self.magneto(text='2').click()

        # swipe in drawer, click power button and dismiss
        content = self.magneto(resourceId='android:id/content')
        content.swipe.left()
        self.magneto(text='^').click()
        self.magneto.press.back()

        self.magneto(text='3').click()
        self.magneto(text='=').click()

        formula = self.magneto(className='android.widget.EditText')
        Assert.true(formula.info['text'] == '8')
