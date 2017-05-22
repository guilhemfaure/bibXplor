__description__ = ''
__author__ = 'Guilhem Faure, PhD'

import urllib.request
from xml.dom import minidom
import xml.dom.minidom


class Paper:
    def __init__(self, pmid=None):
        """

        :param pmid:
        :return:
        """
        self.pmid = None
        self.title = None
        self.l_author = []
        self.abstract = None
        self.l_ref = []


        

        self.xdoc = minidom.parse('test.xml') # will be load from _fetch_xml

        # to access data
        self._get_paperinfo() # ==> encompass get_year get_page get_volume
        self._get_abstract()
        self._get_authors()
        self._get_title()
        print (self._get_reference())


        return


    def _get_info(self, tag, xdoc = None):
        """

        :return:
        """

        if xdoc is None:
            xdoc = self.xdoc

        xtag = xdoc.getElementsByTagName(tag)

        if len(xtag) == 0:
            return None

        result = xtag[0].firstChild.data

        return result



    def _fetch_xml(self):
        """

        :return:
        """

        # TODO manage online fetch
        #w_root = 'https://www.ncbi.nlm.nih.gov/pubmed/{pmid}?report=xml'

        #webpage = urllib.request.urlopen(w_root.format(pmid=pmid))
        #f_webpage = webpage.read()
        #print (f_webpage)



    def _get_abstract(self):
        """
        Abstract tag <AbstractText>
        :return: None if no abstract
        """

        return self._get_info('AbstractText')




    def _get_title(self):
        """
        Title tag <ArticleTitle>
        :return: None if no abstract
        """

        return self._get_info('ArticleTitle')



    def _get_journal(self):
        """
        Title tag <ArticleTitle>
        :return: None if no abstract
        """

        return self._get_info('ISOAbbreviation')


    def _get_volume(self):
        """

        :return:
        """

        return self._get_info('Volume')

    def _get_page(self):
        """

        :return:
        """

        return self._get_info('MedlinePgn')

    def _get_year(self):
        """

        :return:
        """

        return self._get_info('Year')


    def _get_paperinfo(self):
        """

        :return:
        """

        return self._get_volume(), self._get_page(), self._get_year()




    def _get_authors(self):
        """

        :return:
        """

        xlauthors = self.xdoc.getElementsByTagName('Author')

        l_author = []
        for xauthors in xlauthors:


            lastname = self._get_info('LastName', xauthors)
            forename = self._get_info('ForeName', xauthors)
            initial = self._get_info('Initials', xauthors)

            # possibility to get the affiliation

            l_author.append([lastname, forename, initial])


        return l_author


    def _get_reference(self):
        """

        :return:
        """


        xlref = self.xdoc.getElementsByTagName('CommentsCorrections')
        if len(xlref) == 0:
            return [] # no ref

        l_ref = []
        for xref in xlref:


            ref = self._get_info('RefSource', xref)
            pmid = self._get_info('PMID', xref)

            l_ref.append ([ref, pmid])

        return l_ref






if __name__ == '__main__':

    a = Paper('28472712')
    #a._get_reference('28472712')
    pass