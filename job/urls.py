from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers 
from . import views

router = routers.SimpleRouter()
router.register(r'jobs',views.JobViewSet)
router.register(r'users',views.JobUserViewSet)
router.register(r'applications',views.ApplicationsViewSet)
router.register(r'skills',views.SkillViewViewSet)
router.register(r'userskills',views.UserSkillViewSet)
router.register(r'experiences',views.ExperienceViewSet)
router.register(r'userprofiles',views.UserProfileViewSet)
router.register(r'companies',views.CompanyViewSet)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/',views.DecoratedTokenObtainPairView.as_view(),name="token"),
    path('api/token/refresh/',views.DecoratedTokenRefreshView.as_view(),name="refresh_token"),
]
urlpatterns += router.urls
