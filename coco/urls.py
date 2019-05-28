from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_coco_list, name='coco_list'),
    path('basecoco/', BaseCocoView.as_view(), name='base_coco'),
    path('promlevel/', PromLevelView.as_view(), name='promlevel'),
    path('cocomo2/', Cocomo2View.as_view(), name='cocomo2')

]