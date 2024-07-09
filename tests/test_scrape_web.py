# tests/test_scrape_web.py
import unittest
from ScrapySub.scrape_web import ScrapWeb

class TestScrapeWeb(unittest.TestCase):
    def test_scrape(self):
        scraper = ScrapWeb()
        scraper.scrape("https://myportfolio-five-tau.vercel.app/")
        documents = scraper.get_all_documents()

if __name__ == "__main__":
    unittest.main()
