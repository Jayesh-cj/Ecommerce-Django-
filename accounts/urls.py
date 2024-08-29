from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.registeraion_page, name='register'),
    path('activate/<email_token>/', views.activate_account, name='activate_account'),
    path('add-to-cart/<uid>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove cart/<cart_item_uid>', views.remove_cart, name='remove_cart'),
    path('remove_coupon/<cart_id>/', views.remove_coupon, name='remove_coupon')
]