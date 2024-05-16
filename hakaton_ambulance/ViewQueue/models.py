from django.http import HttpResponse
from django.template import Context, loader
from django.db import models

class QueueHTMLRenderer:
    def __init__(self, queue_data):
        self.queue_data = queue_data

    def render(self):
        # Загрузка шаблона HTML
        template = loader.get_template('queue_template.html')
        # Создание контекста для передачи данных в шаблон
        context = Context({'queue_data': self.queue_data})
        # Рендеринг шаблона с данными
        rendered_template = template.render(context)
        return HttpResponse(rendered_template)

class Specialist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name