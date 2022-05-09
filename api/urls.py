from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('product', views.ProductViewSet, basename='product')
router.register('category', views.CategoryViewSet, basename='category')
router.register('image', views.ImageViewSet, basename='image')

urlpatterns = router.urls
