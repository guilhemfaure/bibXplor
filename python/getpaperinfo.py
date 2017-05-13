import urllib.parse

#https://eutils.ncbi.nlm.nih.gov/entrez/eutils/ecitmatch.cgi?
# db=pubmed&retmode=xml&bdata=proc+natl+acad+sci+u+s+a|1991|88|3248|mann+bj|Art1|%0Dscience|1987|235|182|palmenberg+ac|Art2|
# 1987 Jan 9;235(4785):182-91



def extract_paper_info(query, id='a1', authors=''):
    """

    :param query: info about the paper as 'Nucleic Acids Res. 2016 Dec 15;44(22):10898-10911. Epub 2016 Jul 27.'
    :param id: identification to retrieve the paper
    :param authors: authors name, only if several paper on one page (science like paper)
    :return: dict containing journal year volume and first_page
    """

    # TODO update with url encode!
    journal = query.split('.')[0].replace(' ', '+')
    year = query.split('.')[1].strip().split()[0]
    volume = query.split('.')[1].strip().split(';')[1].split('(')[0]
    first_page = query.split('.')[1].strip().split(':')[1].split('-')[0]
    id = id.replace(' ', '+')
    authors = authors.replace(' ', '+')


    return {'journal':journal,
            'year':year,
            'volume':volume,
            'first_page':first_page,
            'id':id,
            'authors':authors}

def get_query_paper(paper):
    """

    :param paper:
    :return:
    """

    return '{journal}|{year}|{volume}|{first_page}|{authors}|{id}|'.format(**paper)


def get_pmid(query_paper):
    """
    format of eutils query: journal_title|year|volume|first_page|author_name|your_key|
    :param query_paper: url encoded line with information for the eutils query
    :return:
    """

    # for several request at the same time separate query_paper by %0D
    web_query = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/ecitmatch.cgi?db=pubmed&retmode=xml&bdata='+query_paper

    print (web_query)



    # pmid is the last field of each line!


if __name__ == '__main__':



    # 2016 Dec 15;44(22):10898-10911



    query = 'Nucleic Acids Res. 2016 Dec 15;44(22):10898-10911. Epub 2016 Jul 27.'

    paper = extract_paper_info(query, id='paper1')

    query_paper = get_query_paper(paper)

    get_pmid(query_paper)





    # title = 'Role of mRNA structure in the control of protein folding'
    # #volume = '15;44(22)'#:10898-10911'
    #
    # query = '({title}[Title])'.format(title=title)
    # #query = '({title}[Title])AND({volume}[Volume])'.format(title=title, volume=volume)
    #
    #
    # query_encode = urllib.parse.quote_plus(query).replace('+', '%20')
    #
    # web_query = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=1000&term={term}'.format(term=query_encode)
    #
    # print (web_query)
    # pass