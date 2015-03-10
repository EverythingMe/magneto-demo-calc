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

        drawer = self.magneto(resourceId='me.everything.magnetodemo:id/pad_advanced')
        drawer_children = drawer.child(className='android.widget.Button')

        # check that drawer has no inner elements
        Assert.false(len(drawer_children))

        # swipe it in
        _, y = drawer.center()
        self.magneto.drag(drawer, 0, y, steps=10)

        # check that drawer is populated
        Assert.true(len(drawer_children))

        # swipe drawer back
        drawer.swipe.right()

    def test_drawer_by_orientation(self):
        """
        Test drawer in/out by orientation change
        """

        drawer = self.magneto(resourceId='me.everything.magnetodemo:id/pad_advanced')
        drawer_children = drawer.child(className='android.widget.Button')

        # check that drawer has no inner elements
        Assert.false(len(drawer_children))

        # change to landscape
        self.magneto.orientation = 'r'

        # check that drawer is populated
        Assert.true(len(drawer_children))

        # change back
        self.magneto.orientation = 'n'

    def test_power(self):
        formula = self.magneto(resourceId='me.everything.magnetodemo:id/formula')\
            .child(className='android.widget.EditText')

        self.magneto(text='2').click()

        # swipe in drawer
        drawer = self.magneto(resourceId='me.everything.magnetodemo:id/pad_advanced')
        _, y = drawer.center()
        self.magneto.drag(drawer, 0, y, steps=10)

        # power button
        self.magneto(text='^').click()

        # swipe drawer back
        drawer.swipe.right()

        self.magneto(text='3').click()
        self.magneto(text='=').click()
        Assert.true(formula.info['text'] == '8')
