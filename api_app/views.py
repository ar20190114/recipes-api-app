from rest_framework import viewsets
from .models import RecipesInfo
from .serializer import RecipesInfoSerializer


class RecipesInfoViewSet(viewsets.ModelViewSet):

    queryset = RecipesInfo.objects.all()
    # シリアライザーを取得
    serializer_class = RecipesInfoSerializer
