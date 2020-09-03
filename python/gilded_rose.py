# -*- coding: utf-8 -*-

class GildedRose:

    def __init__(self, items):
        self.orig_items = items
        self.items = [WrappedItem.factory(item) for item in items]

    def update_quality(self):
        for i, item in enumerate(self.items):
            item.update()
            self.orig_items[i] = item


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class WrappedItem(Item):

    @staticmethod
    def factory(item):
        if item.name == "Aged Brie": return AgedBrie(item.name, item.sell_in, item.quality)
        if item.name == "Sulfuras, Hand of Ragnaros": return Sulfuras(item.name, item.sell_in, item.quality)
        if item.name == "Backstage passes to a TAFKAL80ETC concert": return BackstagePass(item.name, item.sell_in, item.quality)
        if item.name == "Conjured": return Conjured(item.name, item.sell_in, item.quality)
        return WrappedItem(item.name, item.sell_in, item.quality)

    def validate(self):
        if self.quality < 0: self.quality = 0
        if self.quality > 50: self.quality = 50
    
    def update(self):
        self.sell_in -= 1
        self.quality -= 1
        if self.sell_in < 0: self.quality -= 1
        self.validate()
        
class Sulfuras(WrappedItem):
    
    def update(self):
        self.sell_in -= 1
        

class AgedBrie(WrappedItem):

    def update(self):
        self.quality += 1
        self.sell_in -= 1
        self.validate()


class BackstagePass(WrappedItem):
    
    def update(self):
        self.sell_in -= 1
        self.quality += 1
        if self.sell_in <= 10: self.quality += 1
        if self.sell_in <= 5:  self.quality += 1
        if self.sell_in <= 0:  self.quality = 0
        self.validate()


class Conjured(WrappedItem):
    
    def update(self):
        self.sell_in -= 1
        self.quality -= 2
        self.validate()