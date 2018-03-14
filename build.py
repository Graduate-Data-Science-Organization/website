import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
ENV = Environment(autoescape=False,
                  loader=FileSystemLoader(os.path.join(PATH, 'templates')),
                  trim_blocks=False)

# Pages with content that doesn't change frequently
static_pages = ['index.html', 'contact.html', 'workshop.html']

# Build static pages
for temp_fname in static_pages:
    with open(os.path.join(PATH, temp_fname), 'w') as out_f:
        out_f.write(ENV.get_template(temp_fname).render())

# Build team page
team = []
formerteam = []
team_keys = ['name',
             'title',
             'imgpath',
             'email',
             'github',
             'linkedin',
             'bio']
# Parse bios.txt
with open(os.path.join(PATH, 'files/bios.txt'), 'r') as bio_f:
    for person in bio_f.read().split('\n\n'):
        info_dict = dict(zip(team_keys, person.split('\n')))
        if info_dict['imgpath'] == '---':
            formerteam.append(info_dict)
        else:
            team.append(info_dict)
# Add bios to team page
with open(os.path.join(PATH, 'about.html'), 'w') as out_f:
    out_f.write(ENV.get_template('about_cards.html').render(team=team, formerteam=formerteam))

# Build event page
events = []
event_keys = ['title', 'tag', 'text', 'flyerpath']
# Parse events.txt
with open(os.path.join(PATH, 'files/events.txt'), 'r') as event_f:
    for event in event_f.read().split('\n\n'):
        info_dict = dict(zip(event_keys, event.split('\n')))
        events.append(info_dict)
# Add events to page
with open(os.path.join(PATH, 'events.html'), 'w') as out_f:
    out_f.write(ENV.get_template('event_list.html').render(events=events))
