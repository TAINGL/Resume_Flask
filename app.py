from flask import Flask, render_template
app = Flask(__name__)

person = {
        'first_name': 'Laura',
        'last_name': 'TAING',
        'title': 'Data Scientist',
        'address': 'FRANCE',
        'phone_number': 'yournumber',
        'email': 'youremail',
        'description': 'Curieuse, j’ai un parcours polyvalent axé dans différent secteur en science: santé, industrie biochimique et agroalimentaire en plus de mes connaissances dans le secteur de la data.',
        'github': 'https://github.com/TAINGL',
        'linkedin': 'https://www.linkedin.com/in/tlaura/',
        'img': 'img/avatar.jpg',
         'programming_languages': {
            'HTML': 'fa-html5',
            'CSS': 'fa-css3-alt',
            'Python': 'fab fa-python',
            'SQL': 'fas fa-database',
            'R': 'fab fa-r-project'
        },
        'languages': ['French', 'English'],
        'interests': [' Yoga Vinyasa', 
                    'Running : 20K , 16K, 10K, 5K',
                    'Développement durable',
                    'voyages',
                    'culture coréenne',
                    'jeux de stratégie']
        }

experiences = {
        '1':
            {
                'title': 'Data Analyst Junior',
                'company': '50intech',
                'description': "Start-up qui élabore une plateforme basée sur de la data pour mettre en relation les femmes de la tech.\n Mise en place d'une base de donnée client (SQL).\n Élaboration d'un dashboard : visualisation sous Tableau et Dataiku, et documentation sur Dash by Plotly",
                'timeframe': 'Sept - Oct 2019'
            },
        '2':
            {
                'title': 'Commis pâtissière',
                'company': 'Le Train Bleu, Le Dali Le Meurice',
                'description': "Service et envoi\n Préparation du poste de travail\nCuissons des crèmes, des biscuits\nFinitions des desserts\n",
                'timeframe': 'Avril 2017 - Août 2018'
            },
        '3':
            {
                'title': 'Technicienne industrialisation méthodes',
                'company': 'Bio-Rad',
                'description': "Contribution au scale up d’un multi-test rapide\nParticiper à la réalisation des essais industriels\nFabrication des réactifs nécessaire au essais\nContrôler les préparations\nÉlaborer les données techniques de production (modes opératoires, niveau de qualité)",
                'timeframe': 'Sept 2014 - Sept 2015'
            },
        '4':
            {
                'title': 'Technicienne assurance qualité',
                'company': 'ZTP',
                'description': 'Evaluation des points critiques de l’ECBU (examen cytobactériologique)',
                'timeframe': 'Sept 2014 - Sept 2015'
            }
}

educations = {
    '1':
            {
                'university': 'MICROSOFT powered by SIMPLON.CO',
                'degree': 'Développeur Data IA',
                'description': "Certification « Exploiter les méthodes d'intelligence artificielle dans le développement d'applications »",
                'timeframe': 'Mars - Octobre 2020)'
            },
    '2':
            {
                'university': 'SIMPLON.CO',
                'degree': 'Développeur Data',
                'description': 'Certification « Développer une base de données »\n« Exploiter une base de données »',
                'timeframe': 'Juin 2019 – Dec 2019)'
            },
    '3':
              {
                'university': 'ISSBA',
                'degree': 'Master 1 en Sciences, ingénierie et management de la santé',
                'description': '',
                'timeframe': '2016'
            },
    '4':
            {
                'university': 'UMPC Paris VI',
                'degree': 'Licence professionnelle spécialité métiers de la biotechnologie',
                'description': '',
                'timeframe': '2015'
            },
    '5':
            {
                'university': 'IUT La Rochelle',
                'degree': 'Licence professionnelle spécialité analyses, traçabilité au laboratoire',
                'description': '',
                'timeframe': '2014'
            },
    '6':
            {
                'university': 'IUT Brest',
                'degree': 'DUT Génie biologique',
                'description': '',
                'timeframe': '2013'
            }
}


@app.route('/')
def cv(person=person, experiences=experiences, educations=educations): 
    return render_template('index.html', person=person, experiences=experiences, educations=educations)

if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)