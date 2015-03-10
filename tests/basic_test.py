# coding=utf-8
from magneto.base import BaseTestCase
from magneto.utils.assertion import Assert


class TestBasic(BaseTestCase):
    """
    Test basic app features
    """

    def setup_method(self, method):
        delete = self.magneto(textMatches='del|clr')
        delete.long_click()

    def test_result(self):
        """
        Test calculation and assert result
        """

        formula = self.magneto(resourceId='me.everything.magnetodemo:id/formula')\
            .child(className='android.widget.EditText')
        result = self.magneto(resourceId='me.everything.magnetodemo:id/result')\
            .child(className='android.widget.EditText')

        self.magneto(text='2').click()
        self.magneto(text='×').click()
        self.magneto(text='3').click()
        Assert.true(result.info['text'] == '6')

        self.magneto(text='=').click()
        Assert.true(formula.info['text'] == '6')

    def test_result_comma(self):
        """
        Test that a comma is added to formula number
        """

        formula = self.magneto(resourceId='me.everything.magnetodemo:id/formula')\
            .child(className='android.widget.EditText')

        for i in range(1,5):
            self.magneto(text=i).click()

        Assert.true(formula.info['text'] == '1,234')

    def test_font_size(self):
        """
        Test that formula font decreases as content increases
        """
        formula = self.magneto(resourceId='me.everything.magnetodemo:id/formula')\
            .child(className='android.widget.EditText')
        digit_9 = self.magneto(resourceId='me.everything.magnetodemo:id/digit_9')

        # get initial bounds
        digit_9.click()
        initial_bottom = formula.info['bounds']['bottom']

        # add content
        for i in xrange(10):
            digit_9.click()
        Assert.true(formula.info['bounds']['bottom'] < initial_bottom)

        # delete content
        delete = self.magneto(text='del')
        for i in xrange(5):
            delete.click()
        Assert.true(formula.info['bounds']['bottom'] == initial_bottom)