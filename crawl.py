# -*- coding: utf-8 -*-

import logging
import os.path as osp
from argparse import ArgumentParser

from icrawler.builtin import (BaiduImageCrawler, BingImageCrawler,
                              FlickrImageCrawler, GoogleImageCrawler,
                              GreedyImageCrawler, UrlListCrawler)


def test_google():
    print('start testing GoogleImageCrawler')
    google_crawler = GoogleImageCrawler(
        downloader_threads=4,
        storage={'root_dir': 'images/google'},
        log_level=logging.INFO)
    search_filters = dict(
        size='large',
        color='orange',
        license='commercial,modify',
        date=(None, (2017, 11, 30)))
    google_crawler.crawl('cat', filters=search_filters, max_num=10)



def test_baidu():
    print('start testing BaiduImageCrawler')
    search_filters = dict(size='large', color='blue')
    baidu_crawler = BaiduImageCrawler(
        downloader_threads=30, storage={'root_dir': 'images/demon_slayer'})
    baidu_crawler.crawl('tanjiro', filters=search_filters, max_num=50)



def main():
    parser = ArgumentParser(description='Test built-in crawlers')
    parser.add_argument(
        '--crawler',
        nargs='+',
        default=['google', 'bing', 'baidu', 'flickr', 'greedy', 'urllist'],
        help='which crawlers to test')
    args = parser.parse_args()
    for crawler in args.crawler:
        eval('test_{}()'.format(crawler))
        print('\n')


if __name__ == '__main__':
    main()
