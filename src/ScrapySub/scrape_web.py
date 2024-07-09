from typing import Any, List, Literal
from langchain_core.load.serializable import Serializable
from langchain_core.pydantic_v1 import Field
import requests
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin, urlparse
import time


class Document(Serializable):
    """Class for storing a piece of text and associated metadata."""

    page_content: str
    """String text."""
    metadata: dict = Field(default_factory=dict)
    """Arbitrary metadata about the page content (e.g., source, relationships to other
        documents, etc.).
    """
    type: Literal["Document"] = "Document"

    def __init__(self, page_content: str, **kwargs: Any) -> None:
        """Pass page_content in as positional or named arg."""
        super().__init__(page_content=page_content, **kwargs)

    @classmethod
    def is_lc_serializable(cls) -> bool:
        """Return whether this class is serializable."""
        return True

    @classmethod
    def get_lc_namespace(cls) -> List[str]:
        """Get the namespace of the langchain object."""
        return ["langchain", "schema", "document"]


class ScrapWeb:
    def __init__(self):
        self.visited_urls = set()
        self.documents = []

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return None

    def scrape_text(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        texts = soup.find_all(string=True)
        visible_texts = filter(self.tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)

    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def get_links(self, url, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(url, href)
            if self.is_valid_url(full_url, url):
                links.add(full_url)
        return links

    def is_valid_url(self, url, base_url):
        parsed_url = urlparse(url)
        base_parsed_url = urlparse(base_url)
        return (parsed_url.scheme in ['http', 'https'] and
                parsed_url.netloc == base_parsed_url.netloc and
                url not in self.visited_urls)

    def scrape(self, url):
        if url in self.visited_urls:
            return

        self.visited_urls.add(url)
        html_content = self.fetch_page(url)
        if not html_content:
            return

        text_content = self.scrape_text(html_content)
        document = Document(page_content=text_content, metadata={"url": url})
        self.documents.append(document)

        links = self.get_links(url, html_content)
        for link in links:
            time.sleep(1)  # Be polite to the server by adding a delay between requests
            self.scrape(link)

    def get_all_documents(self):
        return self.documents