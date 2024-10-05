# recommendation/engine/content_based.py

from .base import BaseRecommendationEngine
from ..models import UserInteraction, Track, UserPreference, Recommendation
from django.db.models import Q, Count

class ContentBasedFilteringEngine(BaseRecommendationEngine):

    def recommend(self, user, num_recommendations=10):
        preferences = self.get_user_preferences(user)
        preferred_genres = preferences.preferred_genres.split(',')

        recommended_tracks = Track.objects.filter(
            Q(genre__in=preferred_genres) &
            ~Q(userinteraction__user=user)
        ).distinct()[:num_recommendations]

        recommendations = []
        for track in recommended_tracks:
            recommendations.append(Recommendation(user=user, track=track, score=1.0))
        Recommendation.objects.bulk_create(recommendations)

        return recommended_tracks

    def get_user_preferences(self, user):
        try:
            return UserPreference.objects.get(user=user)
        except UserPreference.DoesNotExist:
            return UserPreference.objects.create(user=user)

    def update_preferences(self, user):
        interactions = UserInteraction.objects.filter(user=user, liked=True)
        genre_count = interactions.values('track__genre').annotate(count=Count('track__genre')).order_by('-count')

        preferences = self.get_user_preferences(user)
        preferred_genres = [item['track__genre'] for item in genre_count if item['count'] > 1]
        preferences.preferred_genres = ','.join(preferred_genres)
        preferences.save()
