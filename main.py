import os
from backend import create_db

if not os.path.isdir('participant.db'):
    print('creating..')
    create_db.create_database('participant.db')