import unittest
import os
from jsonschemainfotable.renderhtml import render_html_from_filename


class TestJsonSchema(unittest.TestCase):
    def test_render1(self):
        filename_in = os.path.dirname(os.path.realpath(__file__)) + '/examples/htmlrender/test1.json'
        filename_out = os.path.dirname(os.path.realpath(__file__)) + '/examples/htmlrender/test1_out.html'
        html = render_html_from_filename(filename_in)
        with open(filename_out) as fp:
            expected = fp.read()
        assert expected == html
