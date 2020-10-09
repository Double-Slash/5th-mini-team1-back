import datetime
from haystack import indexes
from postings.models import Posting

class PostingIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(document=True, use_template=True)

    # author = indexes.CharField(model_attr='user')
    # pub_date = indexes.DateTimeField(model_attr='pub_date')
    def get_model(self):
        return Posting
    # def prepare_text(self, obj):
    #     return [posting.title for _ in obj.postings.all()]
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()