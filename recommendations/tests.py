from django.test import TestCase

# Create your tests here.
# recommendation/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Track, UserInteraction, UserPreference, Recommendation
from .engine.hybrid import HybridRecommendationEngine

class HybridRecommendationEngineTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.track1 = Track.objects.create(title="Song 1", artist="Artist 1", genre="Rock", tempo=120)
        self.track2 = Track.objects.create(title="Song 2", artist="Artist 2", genre="Jazz", tempo=90)

        UserInteraction.objects.create(user=self.user, track=self.track1, liked=True, play_count=5)
        UserInteraction.objects.create(user=self.user, track=self.track2, liked=False, play_count=2)

    def test_recommendations(self):
        engine = HybridRecommendationEngine()
        recommendations = engine.recommend(self.user)

        self.assertEqual(len(recommendations), 2)  # Expecting two recommendations

    def test_update_preferences(self):
        engine = HybridRecommendationEngine()
        engine.update_preferences(self.user)

        preferences = UserPreference.objects.get(user=self.user)
        self.assertIn("Rock", preferences.preferred_genres)
