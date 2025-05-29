import os
import django
import pydoc

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

# Genera HTML de cada mòdul
pydoc.writedoc("blog.models")
pydoc.writedoc("blog.views")
