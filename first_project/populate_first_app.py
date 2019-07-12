import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
import random
django.setup()
#fake pop scrip

from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
topics = ['search','social','marketplace','news','games']
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        #get topic for the entry
        top =  add_topic()
        #create a fake data for the entry
        fake_url = fakegen.url()
        fake_date= fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
#       #create fake AccessRecord for the webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
if __name__ == '__main__':
    print("populate")
    populate(20)
