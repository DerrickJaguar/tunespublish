# recommendation/engine/collaborative_filtering.py

from .base import BaseRecommendationEngine
from ..models import UserInteraction, Track, Recommendation
from django.db.models import Count


class CollaborativeFilteringEngine(BaseRecommendationEngine):

    def recommend(self, user, num_recommendations=10):
        similar_users = UserInteraction.objects.filter(track__userinteraction__user=user).exclude(user=user).values(
            'user').annotate(similarity=Count('track')).order_by('-similarity')

        similar_user_ids = [u['user'] for u in similar_users]
        recommended_tracks = Track.objects.filter(userinteraction__user__in=similar_user_ids).distinct()[
                             :num_recommendations]

        recommendations = []
        for track in recommended_tracks:
            recommendations.append(Recommendation(user=user, track=track, score=1.0))
        Recommendation.objects.bulk_create(recommendations)

        return recommended_tracks

    def update_preferences(self, user):
        pass
