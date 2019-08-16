from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestEntriesFeed(Feed):
    title = "Rachel's Django Blog"
    link = "/sitenews/"
    description = "Latest posts from Rachel's Django Blog"

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

#    def item_link(self, item):
#        return reverse('Post', args=[item.pk])
