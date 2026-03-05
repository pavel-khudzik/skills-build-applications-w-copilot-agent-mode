from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Очистка данных
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Создание команд
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Создание пользователей
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        hulk = User.objects.create_user(username='hulk', email='hulk@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Создание активностей
        Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        Activity.objects.create(user=hulk, type='swim', duration=45, distance=2)
        Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=superman, type='run', duration=50, distance=10)

        # Создание тренировок
        Workout.objects.create(user=ironman, description='Chest day', duration=60)
        Workout.objects.create(user=batman, description='Leg day', duration=45)

        # Создание лидерборда
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=superman, score=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
