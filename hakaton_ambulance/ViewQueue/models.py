from django.http import HttpResponse
from django.template import Context, loader

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

