import feedparser
import justext
import pickle
import requests
import sys

__all__ = ["get_text", "collect"]

def get_text(link):
    response = requests.get(link)
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    text = "\n\n".join([p.text for p in paragraphs if not p.is_boilerplate])
    return text

def collect(url, filename="rssdata.txt", mode='write'):
    # read RSS feed
    d = feedparser.parse(url)

    # grab each article
    texts = {}
    for entry in d["entries"]:
        link = entry["link"]
        print("downloading: " + link)
        text = get_text(link)
        texts[link] = text

    if mode == 'write':
        # pickle
        pickle.dump(texts, open(filename, "wb"))

    elif mode == 'return':
        return texts

    else:
        raise Exception("Mode not implemented.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python collect_rss.py <url> <filename>")
        sys.exit(1)

    # https://www.reuters.com/tools/rss
    # http://feeds.reuters.com/Reuters/domesticNews
    url = sys.argv[1]
    filename = sys.argv[2]
    collect(url, filename)
