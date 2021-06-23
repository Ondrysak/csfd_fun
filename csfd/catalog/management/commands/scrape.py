from django.core.management.base import BaseCommand, CommandError
from catalog.models import Actor, Movie

import requests

from bs4 import BeautifulSoup
from time import sleep

top300_url = 'https://www.csfd.cz/zebricky/filmy/nejlepsi/?showMore=1'
# todo this should probably be rotated 
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
# todo use proxies?


def get_top_300_urls():
    page = requests.get(top300_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    urls = ['https://www.csfd.cz' + film['href'] for film in soup.findAll("a", {"class" : "film-title-name"})]
    return urls



def parse_movie(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find('h1', {"itemprop" : "name"}).text.strip()
    hraji = soup.find("h4", string="Hrají: ")
    actors = [herec.text for herec in hraji.parent.findAll("a")]
    if actors[-1] == 'více':
        actors = actors[:-1]
    return name, actors


class Command(BaseCommand):
    help = "Scrapes csfd top 300"


        


    def add_arguments(self, parser):
        parser.add_argument('sleep', type=int)

    def handle(self, *args, **options):
        Actor.objects.all().delete()
        Movie.objects.all().delete()

        urls = get_top_300_urls()

        for url in urls:
            title, actors = parse_movie(url)
            m = Movie(title=title)
            m.save()
            for actor_name in actors:
                actor, created = Actor.objects.get_or_create(name=actor_name)
                m.actor_set.add(actor)


            self.stdout.write(self.style.SUCCESS(f'Successfully scraped {title} with {len(actors)} actors!'))

            sleep(options['sleep']) # dont be that guy :)

        self.stdout.write(self.style.SUCCESS('Successfully scraped!'))