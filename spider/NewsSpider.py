# -*- coding: utf-8 -*-
import time
import feapder
from items import *
from feapder.utils.webdriver import WebDriver
from selenium.webdriver.common.by import By

from NetNes.items import spider_data_item


class SpiderTest(feapder.Spider):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis_key = "feapder:spider_test"

    def start_requests(self):
        yield feapder.Request("https://news.163.com/domestic/", render=True)

    def parse(self, request, response):
        """
        解析新闻首页列表
        """
        browser: WebDriver = response.browser
        time.sleep(3)
        # js = 'window.scrollTo(0,document.body.scrollHeight);'
        # browser.execute_script(js)
        # browser.execute_script("arguments[0].scrollIntoView();", target)
        target = browser.find_element(By.CLASS_NAME, 'load_more_btn')
        post_addmore = browser.find_element(By.CLASS_NAME, 'post_addmore')
        while post_addmore.is_displayed():
            target.click()
            time.sleep(3)

        # 若有滚动，可通过如下方式更新response，使其加载滚动后的内容
        response.text = browser.page_source
        article_list = response.xpath('//div[contains(@class,"data_row news_article clearfix")]') #定位新闻列表
        for article in article_list:
            img_url = article.xpath("./a/img/@src").extract_first()  #图片链接
            detail_url = article.xpath("./div/div[@class ='news_title']/h3/a/@href").extract_first()  #详情链接
            title = article.xpath("./div/div[@class ='news_title']/h3/a/text()").extract_first() #新闻标题
            yield feapder.Request(
                detail_url, callback=self.parse_detail, img_url=img_url, title=title
            )

        response.close_browser(request)
        browser.close()

    def parse_detail(self, request, response):
        """
        解析详情
        """
        # 取url
        detail_url = request.url
        # 取img_url,title
        img_url = request.img_url
        title = request.title
        # 解析正文
        selector_list = response.xpath('//*[@id="content"]/div[2]/p/text()').extract() #获取新闻内容
        content = "".join(selector_list)

        print(content)

        item = spider_data_item.SpiderDataItem()
        item.title = title
        item.img_url = img_url
        item.detail_url = detail_url
        item.content = content
        item.save_to_excel('../data.xlsx')
        yield item


if __name__ == "__main__":
    SpiderTest(redis_key="feapder:spider_test", redis_host="127.0.0.1", redis_port=6379,redis_password=None).start()
