import json
import unittest
from pycognaize.document.html_info import HTML
from unittest.mock import patch

from pycognaize.common.enums import IqFieldKeyEnum, ID
from pycognaize.document.page import create_dummy_page, Page
from pycognaize.tests.resources import RESOURCE_FOLDER
from pycognaize.document.tag.section_tag import SectionTag
from pycognaize.document.field.section_field import SectionField

class TestSectionField(unittest.TestCase):

    def setUp(self):
        with open(RESOURCE_FOLDER + '/snapshots/632c61fc86d52800197d03f3/document.json') as document_json:
            self.data = json.load(document_json)

        self.html = HTML(path=(
            RESOURCE_FOLDER + '/snapshots/632c61fc86d52800197d03f3'),
                         document_id='632c61fc86d52800197d03f3')
        self.section_tag_1 = SectionTag(left=5, top=10, height=20, width=7,
                                      tag_type="Section", page=create_dummy_page())
        self.section_tag_2 = SectionTag(left=7, top=11, height=20, width=7,
                                      tag_type="Section", page=create_dummy_page())
        self.section_field_without_tags = SectionField(name="field")
        self.section_field_with_tags = SectionField(name="field_2", tags=[self.section_tag_1, self.section_tag_2])
        self.raw_section = self.data['input_fields']['section'][0]
        self.pages_1 = {1: create_dummy_page(page_n=1)}

    def test_start(self):
        self.assertEqual(self.section_field_with_tags.start.top, 10)    #if case
        self.assertEqual(self.section_field_without_tags.start, None)   #else case

    def test_end(self):
        self.assertEqual(self.section_field_with_tags.end.top, 11)      #if case
        self.assertEqual(self.section_field_without_tags.end, None)     #else case

    def test_construct_from_raw(self):
        self.section_field=SectionField.construct_from_raw(raw=self.raw_section, pages=self.pages_1)
        self.assertEqual(self.section_field.name, "Section")
