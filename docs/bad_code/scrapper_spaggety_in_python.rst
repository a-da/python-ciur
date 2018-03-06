WRONG
=====

.. code-block:: python


       def parseItem(self, response):
        """
        Parsers product page
        @param response: Response
        """
        hxs = HtmlXPathSelector(response)
        item = UItem()
        item["url"] = response.url

        #====================== from page
        title = self.getFirst(".//span[@id='titreDetail']/text()", hxs, expected_only_one=True)
        item["title"] = title

        price = self.getFirst("//div[@id='infosVehicule']//ul[last()]/li[1]/span[1]/text()", hxs, expected_only_one=True)
        price = self._price_regex.sub("", price)
        if price.isdigit():
            item["price"] = price

        item["description"] = self.extractText("//div[@id='DetailCommentaires']//p[@class='contenuDetail']", hxs)

        item["specification"] = self.extractText("//div[@id='DetailEquipement']//ul/li", hxs)


        year = self.getFirst(".//div[@id='infosVehicule']/ul[1]/li[1]/text()", hxs, expected_only_one=True)
        m = self._year_regex.search(year)
        if m:
            item["year"] = m.group(1)

        mileage = self.getFirst("//div[@id='infosVehicule']/ul[1]/li[contains(text(), ' km')]/text()", hxs, expected_only_one=True)
        mileage = self._mileage_regex.sub("", mileage)
        if mileage.isdigit():
            item["mileage"] = mileage

        thumb = self.getFirst("//a[@id='detail-photo1']/img/@src", hxs, expected_only_one=True)
        # http://occasion.321auto.com/photos/detail/46770410_634822208340068000.jpg
        # http://occasion.321auto.com/photos/big/46770410_634822208340068000.jpg
        # place holder has another xpath !
        item["thumb"] = urlparse.urljoin(response.url, thumb.replace("/photos/detail/", "/photos/big/"))

        title_string = self.extractText("//head/title", hxs)

        m = self._postal_code_regex.search(title_string)
        if m:
            item["postal_code"] = m.group(1) or m.group(2)

        m  = self._city_regex.search(title_string)
        if m:
            item["city"] = m.group(1)

        m  = self._region_regex.search(title_string)
        if m:
            item["region"] = m.group(1)

        item["objectId"] = self._object_id_regex.search(response.url).group(1)


        def _get_doors(text_chunk_keys):
            for key in text_chunk_keys:
                m = self._doors_regex.search(item[key])
                if m:
                    return m.group(1)
            else:
                return 0

        item["doors"] = _get_doors(["description", "specification"])

        #====================== from api
        item["make"]     = self._vehicles.searchMake(item["title"])
        item["model"]    = self._vehicles.searchModel(item["make"], item["title"])
        item["model_id"] = self._vehicles.findModelId(item["make"], item["model"], Vehicles.CARS)
        item["type"]     = Vehicles.CAR # there are only cars

        item["bodytype"] = self._filters.searchBodyTypeId(item["description"])
        item["colour"]   = self._filters.searchColourId(item["description"])

        item["colour"] = self._filters.searchColourId(item["description"]) or\
                         self._filters.searchColourId(item["specification"])

        item["transmission"] = self._filters.searchTransmissionId(item["description"]) or\
                               self._filters.searchTransmissionId(item["specification"])


CORRECT
=======

    file: scrapper_spaggety.ciur

    .. code-block::

        root `//body` +1
            title `.//span[@id='titreDetail']/text()` +1
            price `.//div[@id='infosVehicule']//ul[last()]/li[1]/span[1]/text()` float +1
            ...

    execute

    .. code-block::

        >>> ciur.parse("scrapper_spaggety.ciur" , "http://some_site.org")
        {
            "root": {
                "title": "some title",
                "price":  99.98
            }
        }


