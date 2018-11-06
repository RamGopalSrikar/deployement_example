import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","database_exp.settings")

import django

django.setup()

from faker import Faker
from user_details.models import userdetails

fakegen=Faker()

def populate(N=5):

    nameslist=fakegen.name().split(' ')
    last=nameslist[-1]
    first=""
    for name in nameslist[0:-1]:
        first=first+name+" "
        fake_email=fakegen.email()

        userdetail=userdetails.objects.get_or_create(first_name=first, last_name=last, email=fake_email)

if __name__=='__main__':
    print('pouplating data')
    populate(20)
    print('populating data completed!')
