from rest_framework import routers

from .views import *

routerAulas = routers.DefaultRouter()
routerAulas.register(r"alunos", AlunosViewSet)
routerAulas.register(r"professores", ProfessoresViewSet)
routerAulas.register(r"disciplinas", DisciplinasViewSet)
routerAulas.register(r"disciplinaaluno", DisciplinaAlunoViewSet)
routerAulas.register(r"frequencia", FrequenciaViewSet)
routerAulas.register(r"frequenciaaluno", FrequenciaAlunoViewSet)
routerAulas.register(r"planoaula", PlanoAulaViewSet)
routerAulas.register(r"atividades", AtividadesViewSet)
