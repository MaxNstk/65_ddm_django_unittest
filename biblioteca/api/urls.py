from rest_framework.routers import SimpleRouter
from biblioteca import views


router = SimpleRouter()

router.register(r'estoque', views.EstoqueViewSet)
router.register(r'livro', views.LivroViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'estoquemovimento', views.EstoqueMovimentoViewSet)
router.register(r'entradalivros', views.EntradaLivrosViewSet)
router.register(r'emprestimo', views.EmprestimoViewSet)

urlpatterns = router.urls
