import scrapy
from fareast_scraper.items import FareastScraperItem

class FarEastSpider(scrapy.Spider):
    name = "fareast"
    start_urls = [
        "https://www.klsescreener.com/v2/stocks/view/5029"
    ]

    # def filter_tuple(self, my_tuple):
    #     self.mylist = list(my_tuple)
    #     [self.my_new_list] = self.mylist
    #     self.mystr = self.my_new_list[1]
    #     self.str_v1 = rsi_str.replace("\n", "")
    #     rsi_str_v1 = rsi_str_v1.replace(" ", "")


    def parse(self, response):
        item = FareastScraperItem()
        
        item['High'] = response.css("#priceHigh::text").extract_first()
        item['Low'] = response.css("#priceLow::text").extract_first()
        item['Volume'] = response.css('#volume::text').extract_first()
        volume_bs_list = response.css('#volumeBuySell span::text').getall()
        item['volume_bs'] = f"{volume_bs_list[0]} / {volume_bs_list[1]}"
        price_list = response.css("#priceBidAsk span::text").getall()
        item["price"] = f"{price_list[0]} / {price_list[1]}"
        item['fiftytwoW'] = response.xpath('//td[text()="52w"]/following-sibling::td[1]/text()').get()
        item['ROE'] = response.xpath('//td[text()="ROE"]/following-sibling::td[1]/text()').get()
        item['PE'] = response.xpath('//td[text()="P/E"]/following-sibling::td[1]/text()').get()
        item['EPS'] = response.xpath('//td[text()="EPS"]/following-sibling::td[1]/text()').get()
        item['DPS'] = response.xpath('//td[text()="DPS"]/following-sibling::td[1]/text()').get()
        item['DY'] = response.xpath('//td[text()="DY"]/following-sibling::td[1]/text()').get()
        item['NTA'] = response.xpath('//td[text()="NTA"]/following-sibling::td[1]/text()').get()
        item['PB'] = response.xpath('//td[text()="P/B"]/following-sibling::td[1]/text()').get()
        item['RPS'] = response.xpath('//td[text()="RPS"]/following-sibling::td[1]/text()').get()
        item['PSR'] = response.xpath('//td[text()="PSR"]/following-sibling::td[1]/text()').get()
        item['Market_cap'] = response.xpath('//td[text()="Market Cap"]/following-sibling::td[1]/text()').get()
        item['Shares'] = response.xpath('//td[text()="Shares (mil)"]/following-sibling::td[1]/text()').get()

        rsi_tuple  = response.xpath('//td[text()="RSI(14)"]/following-sibling::td[1]/text()').extract(),
        rsi_list = list(rsi_tuple)
        [new_rsi_list] = rsi_list
        rsi_str = new_rsi_list[1]
        rsi_str_v1 = rsi_str.replace("\n", "")
        rsi_str_v1 = rsi_str_v1.replace(" ", "")
        item['RSI'] = rsi_str_v1

        stochastic_tuple = response.xpath('//td[text()="Stochastic(14)"]/following-sibling::td[1]/text()').extract(),
        stochastic_list = list(stochastic_tuple)
        [new_stochastis_list] = stochastic_list
        stochastic_str_p1 = new_stochastis_list[1]
        stochastic_str_p1_v1 = stochastic_str_p1.replace("\n", "")
        stochastic_str_p1_v1 = stochastic_str_p1_v1.replace(" ", "")
        item['Stochastic14'] = stochastic_str_p1_v1

        average3m_tuple = response.xpath('//span[text()="Average Volume (3M)"]/parent::td/following-sibling::td[1]/text()').extract_first(),
        average3m_list = list(average3m_tuple)
        average3m_str = average3m_list[0]
        average3m_str = average3m_str.replace("\n", "")
        average3m_str = average3m_str.replace(" ", "")
        item['Average3M'] = average3m_str

        relative_volume_liste= response.xpath('//td[text()="Relative Volume"]/following-sibling::td[1]/text()').extract()
        Relative_Volume_str_p1 = relative_volume_liste[0]
        Relative_Volume_str_p1_v1 = Relative_Volume_str_p1.replace("\n", "")
        Relative_Volume_str_p1_v1 = Relative_Volume_str_p1_v1.replace(" ", "")
        item['Relative_Volume'] = Relative_Volume_str_p1_v1

        price_c = response.css("#priceDiff::text").get()
        price_c = price_c.split(" ")
        item['last_done'] = response.css("#price::text").get()
        item['change'] = price_c[0]
        item['percent_change'] = price_c[1]
            # 'Volume': response.xpath('#volume::text').get(),
        yield item