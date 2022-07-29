from pycognaize.document.tag.tag import Tag
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pycognaize.document.page import Page

from pycognaize.common.decorators import module_not_found

class SpanTag(Tag):

    def __init__(self, left, right, top, bottom,
                 page: 'Page',
                 raw_value: str):
        super().__init__(left=left, right=right, top=top, bottom=bottom,
                         page=page)
        self.raw_value = raw_value
        self._spacy_doc = None

    @property
    def spacy_doc(self):
        if self._spacy_doc is None:
            self._spacy_doc = self.__create_spacy_doc
        return self._spacy_doc

    @module_not_found
    def __create_spacy_doc(self):
        """Creates spacy nlp object from raw value"""
        import spacy
        nlp = spacy.blank("en")
        self._spacy_doc = nlp(self.raw_value)
