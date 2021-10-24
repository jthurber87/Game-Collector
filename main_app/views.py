# Add the following import
# from django.http import HttpResponse
import os
import uuid
import boto3
from .forms import PlayForm
from .models import Game, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Define the home view


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
            form = UserCreationForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'registration/signup.html', context)


@login_required
def add_photo(request, game_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, game_id=game_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', game_id=game_id)


@login_required
def games_index(request):
    games = Game.objects.filter(user=request.user)
    return render(request, 'games/index.html', {'games': games})


@login_required
def game_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    play_form = PlayForm()
    return render(request, 'games/detail.html', {'game': game, 'play_form': play_form})


@login_required
def add_play(request, game_id):
    form = PlayForm(request.POST)
    if form.is_valid():
        new_play = form.save(commit=False)
        new_play.game_id = game_id
        new_play.save()

    return redirect('detail', game_id=game_id)


class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = '__all__'
    success_url = '/games'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    fields = ['name', 'photos', 'players', 'description']


class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/games/'
