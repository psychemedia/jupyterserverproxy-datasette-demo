import os

def setup_datasette():
  dbpath = os.path.join(os.environ['HOME'], 'dakar_sql.sqlite')
  return {
    'command': ['datasette', 'serve', '-p', '{port}', dbpath],
    'rewrite': '',
    #The following needs a the labextension installing.
    #eg in postBuild: jupyter labextension install jupyterlab-server-proxy
    'launcher_entry': {
        'enabled': True,
        #'icon_path': '/home/jovyan/.jupyter/datasette.svg',
        'title': 'Datasette',
    },
  }
