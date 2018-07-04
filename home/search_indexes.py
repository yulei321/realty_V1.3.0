#coding=UTF-8
from haystack import indexes
from home.models import *

#注意格式
class HomeIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #给title,content设置索引
    source_name = indexes.NgramField(model_attr='source_name')
    source_name = indexes.NgramField(model_attr='source_name')

    def get_model(self):
        return CustomerSource

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')