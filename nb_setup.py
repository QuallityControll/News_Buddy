from setuptools import setup, find_packages

def do_setup():
    setup(name='news_buddy',
          version="1.0",
          authors='Quallitycontroll',
          description='Returns most recent news from https://www.reddit.com/r/news/',
          license='MIT Beaverworks',
          platforms=['Windows', 'Linux', 'Mac OS-X', 'Unix'],
          packages=find_packages())

if __name__ == "__main__":
    do_setup()