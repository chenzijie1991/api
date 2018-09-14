#coding: UTF-8
from django.conf.urls import url

from poi.views import PoisView,PoisAlterView,PoisReviewsView

urlpatterns = [

    url(r'^pois$' , PoisView.as_view()),
    url(r'^pois/(?P<poi_id>\w+)$',  PoisAlterView.as_view()),
    url(r'^pois/(?P<poi_id>\w+)/reviews$', PoisReviewsView.as_view()) ,
    # url(r'^pois/(?P<poi_id>\w+)/reviews/(?P<review_id>\w+)$', PoisReviewsReView.as_view()),

]
