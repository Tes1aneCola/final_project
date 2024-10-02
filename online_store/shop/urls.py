from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('', ProductListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),
    path('Category', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('Category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                               'put': 'update',
                                               'delete': 'destroy'}), name='category_detail'),
    path('UserProfile', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('UserProfile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='user_detail'),
    path('Review', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('Review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='review_detail'),
    path('ProductPhotos', ProductPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='productphotos_list'),
    path('ProductPhotos/<int:pk>/', ProductPhotosViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='productphotos_detail'),
    path('Rating', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('Rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='rating_detail'),
]
