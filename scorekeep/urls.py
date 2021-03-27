from django.urls import path
from .views import (
    SportsSelectView,
    BBScoreCreateFormView,
    VBScoreCreateFormView,
    ScoreDisplayUpdateView,
    ScoreDeleteView,
    ScoreListView,
)

urlpatterns = [
    path('', ScoreListView),
    path('select/', SportsSelectView),
    path('bbscore/', BBScoreCreateFormView),
    path('vbscore/', VBScoreCreateFormView),
    path('<str:sport>/<str:slug>/', ScoreDisplayUpdateView),
    path('<str:sport>/<str:slug>/delete', ScoreDeleteView),
]

