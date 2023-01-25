import scrapy


class PilmSpider(scrapy.Spider):
    name = 'pilm'
    allowed_domains = ['rottentomatoes.com']
    start_urls = ['https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest?page=' + str(i) for i in range(1,300)]

    def parse(self, response):
        # print(response.url)
        urls = response.css('div.discovery-tiles__wrap a.js-tile-link ::attr(href)').getall()
        for url in urls:
            if "rottentomatoes.com" not in url:
                url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.find_details)

    def find_details(self, response):
        film = {
            'Source': response.url,
            'Title': response.css('h1.scoreboard__title ::text').extract(),
            'Rating': response.css('div.meta-value ::text').extract(),
            'Genre':response.css('div.meta-value.genre ::text').extract(),
            'Original Lenguage':response.css('div.panel-body.content_body > ul > li:nth-child(3) > div.meta-value ::text').extract(),
            'Director':response.css('div.panel-body.content_body > ul > li:nth-child(4) > div.meta-value > a::text').extract(),
            'Producer':response.css('div.panel-body.content_body > ul > li:nth-child(5) > div.meta-value ::text').extract(),
            'Writer':response.css('div.panel-body.content_body > ul > li:nth-child(6) > div.meta-value > a::text').extract(),
            'Release Date(Theaters)':response.css('div.panel-body.content_body > ul > li:nth-child(7) > div.meta-value > ::text').extract(),
            'Release Date(Stremming)':response.css('div.panel-body.content_body > ul > li:nth-child(8) > div.meta-value ::text').extract(),
            'Box Office(Gros USA)':response.css('div.panel-body.content_body > ul > li:nth-child(9) > div.meta-value ::text').extract(),
            'Runtime':response.css('div.panel-body.content_body > ul > li:nth-child(10) > div.meta-value ::text').extract(),
            'Distributor':response.css('div.panel-body.content_body > ul > li:nth-child(11) > div.meta-value ::text').extract(),
            'Sound Mix':response.css('div.panel-body.content_body > ul > li:nth-child(12) > div.meta-value ::text').extract(),
            'Description':response.css('div.movie_synopsis::text').extract(),
        }
        yield film

#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(1) > div.meta-value
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(2) > div.meta-value.genre
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(3) > div.meta-value
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(4) > div.meta-value > a
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(5) > div.meta-value
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(6) > div.meta-value > a
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(7) > div.meta-value
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(8) > div.meta-value
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(9) > div.meta-value
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(10) > div.meta-value
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(11) > div.meta-value
#mainColumn > section.panel.panel-rt.panel-box.movie_info.media > div > div > ul > li:nth-child(12) > div.meta-value
#movieSynopsis

