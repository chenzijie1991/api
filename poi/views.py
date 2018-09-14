# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .models import Poi ,Review
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import View
from poi.form import PoisListForm,PoisAddForm,ReviewsAddForm
from utils.helper import HttpJsonResponse, validate_form, get_local_host,datetime_to_timestamp
import uuid
from auth.decorators import login_required

class  PoisView(View):
    @login_required()
    def get(self, request):
        """poi列表"""
        flag, data = validate_form(PoisListForm, request.GET)
        if not flag:
            return HttpJsonResponse(
                {
                    'message': 'Validate Failed',
                    'errors': data,
                }, status=422)

        q = Q(del_sign='N')
        if data['title']:
            q &= Q(title__icontains=data['title'])
        if data['ucode']:
            q &= Q(ucode=data['ucode'])
        poilist = Poi.objects.filter(q).order_by('-create_time')
        count = poilist.count()
        poilist_set = Paginator(poilist, data['pagesize'])
        one_poilist_set = poilist_set.page(data['page'])
        datas = [poi.poi_info() for poi in one_poilist_set]
        response = HttpJsonResponse(datas, status=200)
        if count >  data['page'] * data['pagesize']:
            params = 'page=%d&pagesize=%d' % (data['page'] + 1, data['pagesize'])
            if data['title']:
                params = params + '&title=%s' % data["title"]
            if data['ucode']:
                params = params + '&ucode=%s' % data["ucode"]
            response['Link'] = r'<%s%s?%s>; rel="next"' % (
                get_local_host(request), request.path, params)
        return response

    @login_required()
    def post(self, request):
        """添加poi"""
        flag, data = validate_form(PoisAddForm, request.GET)
        if not flag:
            return HttpJsonResponse(
                {
                    'message': 'Validate Failed',
                    'errors': data,
                }, status=422)

        data['poi_id'] = uuid.uuid1().hex
        data['ucode']=request.user.username
        print(request.user.username)
        poi = Poi.objects.create(**data)
        return HttpJsonResponse({'poi_id': poi.poi_id}, status=201)


class  PoisAlterView(View):
    @login_required()
    def delete(self, request, poi_id):
        """删除poi"""
        try:
            poi = Poi.objects.get(poi_id=poi_id)
        except Poi.DoesNotExist:
            return HttpJsonResponse(status=404)
        poi.del_sign = 'Y'
        poi.save()
        return HttpJsonResponse(status=204)

    @login_required()
    def get(self, request, poi_id):
        """获取单个poi"""
        try:
            poi = Poi.objects.get(poi_id=poi_id)
        except Poi.DoesNotExist:
            return HttpJsonResponse(status=404)
        data = [poi.poi_info()]
        return HttpJsonResponse(data, status=200)

    @login_required()
    def put(self, request, poi_id):
        """修改单个poi"""
        status, data = validate_form(PoisAddForm, request.GET)
        if not status:
            return HttpJsonResponse(data, status=422)
        try:
            poi = Poi.objects.get(poi_id=poi_id)
        except Poi.DoesNotExist:
            return HttpJsonResponse(status=404)
        poi.title = data['title']
        poi.poigenre = data['poigenre']
        poi.content = data['content']
        poi.ucode  = request.user.username
        poi.save()
        return HttpJsonResponse(status=204)


class PoisReviewsView(View):
    @login_required()
    def get(self, request, poi_id):
        """获取单个poi下评论列表"""
        try:
            poi = Poi.objects.get(poi_id=poi_id)
        except Poi.DoesNotExist:
            return HttpJsonResponse(status=404)
        reviews_set= poi.review_set.all()
        if reviews_set:
            data = [review.review_info() for review in reviews_set]
        else:
            return HttpJsonResponse(status=404)
        return HttpJsonResponse(data, status=200)

    @login_required()
    def post(self, request, poi_id):
        """对poi评论操作"""
        flag, data = validate_form(ReviewsAddForm, request.GET)
        if not flag:
            return HttpJsonResponse(
                {
                    'message': 'Validate Failed',
                    'errors': data,
                }, status=422)
        try:
            poi = Poi.objects.get(poi_id=poi_id)
        except Poi.DoesNotExist:
            return HttpJsonResponse(status=404)
        try:
            review = None
            if data['review_id']:
                review = Review.objects.get(review_id=data['review_id'])
        except Review.DoesNotExist:
                return HttpJsonResponse(status=404)
        u1 = Review(review_id=uuid.uuid1().hex,ucode=request.user.username, content=data["content"], poi=poi,sur_re=review)
        u1.save()
        return HttpJsonResponse({'review_id': u1.review_id}, status=201)