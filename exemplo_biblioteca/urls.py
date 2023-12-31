"""
URL configuration for exemplo_biblioteca project.

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as rf_views

from rest_framework.routers import SimpleRouter
from biblioteca.api import views
from biblioteca.views import teste_view


router = SimpleRouter()

router.register(r'estoque', views.EstoqueViewSet)
router.register(r'livro', views.LivroViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'estoquemovimento', views.EstoqueMovimentoViewSet)
router.register(r'entradalivros', views.EntradaLivrosViewSet)
router.register(r'emprestimo', views.EmprestimoViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', rf_views.obtain_auth_token),
    path("api/v1/", include(router.urls)),
    path("teste/", teste_view)

]