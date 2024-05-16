from django.http import HttpResponse
from django.template import Context, loader
from django.db import models
from BaseTables.models import Interval, Cabinet, Patient


class QueueHTMLRenderer:
    def __init__(self, queue_data):
        self.queue_data = queue_data

    def render(self):
        # Загрузка шаблона HTML F3F32F2323
        template = loader.get_template('queue_template.html')
        # Создание контекста для передачи данных в шаблон
        context = Context({'queue_data': self.queue_data})
        # Рендеринг шаблона с данными
        rendered_template = template.render(context)
        return HttpResponse(rendered_template)


class Queue(models.Model):
    id_queue = models.IntegerField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time_id = models.ForeignKey(Interval, related_name='queues', on_delete=models.CASCADE)
    cabinet_id = models.ForeignKey(Cabinet, related_name='queues', on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, related_name='queues', on_delete=models.CASCADE)
