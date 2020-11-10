from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': './naruto'})
google_crawler.crawl(keyword='naruto', max_num=100)
