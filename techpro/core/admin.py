from django.contrib import admin
from .models import Slider, About, Service, Why_choose_us, Blog, Contact

# Registering each model

admin.site.register(Slider)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Why_choose_us)
admin.site.register(Contact)
admin.site.register(Blog)