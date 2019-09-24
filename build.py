import os
from jinja2 import Environment, FileSystemLoader
import codecs

PATH = os.path.dirname(os.path.abspath(__file__))
ENV = Environment(autoescape=False,
                  loader=FileSystemLoader(os.path.join(PATH, 'templates')),
                  trim_blocks=False)

# Pages with content that doesn't change frequently
static_pages = ['index.html', 'contact.html', 'workshop.html', 'ds_forum.html']

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
print_future = True
if 'future' not in set([event['tag'] for event in events]):
    print_future = False
# Add events to page
with open(os.path.join(PATH, 'events.html'), 'w') as out_f:
    out_f.write(ENV.get_template('event_list.html').render(events=events, print_future=print_future))

# Build partners page
partners = []
partner_keys = ['imgpath', 'link', 'name', 'text']
# Parse partners.txt
with open(os.path.join(PATH, 'files/partners.txt'), 'r') as partner_f:
    for partner in partner_f.read().split('\n\n'):
        info_dict = dict(zip(partner_keys, partner.split('\n')))
        partners.append(info_dict)
# Add partners to page
with open(os.path.join(PATH, 'partners.html'), 'w') as out_f:
    out_f.write(ENV.get_template('partner_list.html').render(partners=partners))

# Build projects page
projects = []
project_keys = ['name', 'mentor', 'participants', 'slide_embed']
# Parse projects.txt
with open(os.path.join(PATH, 'files/projects.txt'), 'r') as project_f:
    for project in project_f.read().split('\n\n'):
        info_dict = dict(zip(project_keys, project.split('\n')))
        projects.append(info_dict)
# Add to projects page
with open(os.path.join(PATH, 'projects_2018.html'), 'w') as out_f:
    out_f.write(ENV.get_template('project_cards_2018.html').render(projects=projects))

# Build projects 2019 page
projects = []
project_keys = ['name', 'link', 'mentor', 'participants', 'blurb', 'slide_embed']
# Parse projects.txt
with open(os.path.join(PATH, 'files/projects_2019.txt'), 'r') as project_f:
    for project in project_f.read().split('\n\n'):
        info_dict = dict(zip(project_keys, project.split('\n')))
        projects.append(info_dict)
# Add to projects page
with open(os.path.join(PATH, 'projects_2019.html'), 'w') as out_f:
    out_f.write(ENV.get_template('project_cards_2019.html').render(projects=projects))
