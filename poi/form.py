# encoding:utf-8


from django import forms


class PoisListForm(forms.Form):
    title = forms.CharField(required=False)
    ucode = forms.CharField(required=False)
    page = forms.IntegerField(required=False)
    pagesize = forms.IntegerField(required=False)

    def clean_page(self):
        field = self.cleaned_data['page']
        return field if field else 1

    def clean_pagesize(self):
        field = self.cleaned_data['pagesize']
        return field if field else 10

class PoisAddForm(forms.Form):
    title = forms.CharField(required=True)
    poigenre = forms.CharField(required=True)
    content = forms.CharField(required=True)

class ReviewsAddForm(forms.Form):
    content = forms.CharField(required=True)
    review_id = forms.CharField(required=False)