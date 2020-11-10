from icrawler.builtin import GoogleImageCrawler
google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': 'dog'})
google_crawler.session.verify = False
google_crawler.crawl(keyword='dog', max_num=1000,
                     date_min=None, date_max=None,
                     min_size=(10,10), max_size=None)
