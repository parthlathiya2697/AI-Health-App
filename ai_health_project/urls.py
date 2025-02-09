"""
URL configuration for ai_health_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# ai_health_project/urls.py
from django.contrib import admin
from django.urls import path
from health_app.views import SleepConditionView, StepsConditionView, StepsComparisonView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sleep-condition/', SleepConditionView.as_view(), name='sleep-condition'),
    path('api/steps-condition/', StepsConditionView.as_view(), name='steps-condition'),
    path('api/steps-comparison/', StepsComparisonView.as_view(), name='steps-comparison'),
]
