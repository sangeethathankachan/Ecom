from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('adminindex',views.adminindex,name='adminindex'),
    path('estore',views.estore,name='estore'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addpro',views.addpro,name='addpro'),
    path('showpro',views.showpro,name='showpro'),
    path('editdetails/<int:pk>',views.editdetails,name='editdetails'),
    path('deletedetails/<int:pk>',views.deletedetails,name='deletedetails'),
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('signup',views.signup,name='signup'),
    path('login_user',views.login_user,name='login_user'),
    path('cartitem/<int:pk>/<int:k>/',views.cartitem,name='cartitem'),
    path('details/<int:pk>/<int:k>/',views.details,name='details'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('showuser',views.showuser,name='showuser'),
    path('items',views.items,name='items'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('loadcartitems/<int:pk>',views.loadcartitems,name='loadcartitems'),
    path('deleteitem/<int:pk>',views.deleteitem,name='deleteitem'),
    
]