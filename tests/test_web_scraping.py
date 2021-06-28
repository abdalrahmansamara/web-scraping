from web_scraping import __version__
from web_scraping.scraper import get_citations_needed_count as counts, get_citations_needed_report as report


def test_version():
    assert __version__ == '0.1.0'

def test_count():
    assert counts("https://en.wikipedia.org/wiki/History_of_Mexico") == 5

def test_report():
    actual = report("https://en.wikipedia.org/wiki/History_of_Mexico")[:20]
    expected = 'The first people to '
    assert actual == expected