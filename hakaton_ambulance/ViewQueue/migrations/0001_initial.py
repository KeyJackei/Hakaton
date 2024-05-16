from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id_queue', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('cabinet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queues',
                                                 to='BaseTables.cabinet')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queues',
                                                 to='BaseTables.patient')),
                ('time_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queues',
                                              to='BaseTables.interval')),
            ],
        ),
    ]
