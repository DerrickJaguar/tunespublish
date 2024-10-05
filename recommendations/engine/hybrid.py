# recommendation/engine/hybrid.py

from .collaborative_filtering import CollaborativeFilteringEngine
from .content_based import ContentBasedFilteringEngine

class HybridRecommendationEngine(CollaborativeFilteringEngine, ContentBasedFilteringEngine):

    def recommend(self, user, num_recommendations=10):
        collaborative_recommendations = super(CollaborativeFilteringEngine, self).recommend(user, num_recommendations=num_recommendations // 2)
        content_based_recommendations = super(ContentBasedFilteringEngine, self).recommend(user, num_recommendations=num_recommendations // 2)

        return collaborative_recommendations | content_based_recommendations

    def update_preferences(self, user):
        super(ContentBasedFilteringEngine, self).update_preferences(user)
