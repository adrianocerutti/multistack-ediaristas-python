# Generated by Django 3.2.8 on 2021-11-14 12:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_usuario_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Diaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_atendimento', models.DateField()),
                ('tempo_atendimento', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'SEM PAGAMENTO'), (2, 'PAGO'), (3, 'CONFIRMADO'), (4, 'CONCLUIDO'), (5, 'CANCELADO'), (6, 'AVALIADO'), (7, 'TRANSFERIDO')], default=1)),
                ('preco', models.FloatField()),
                ('valor_comissao', models.FloatField()),
                ('logradouro', models.CharField(max_length=60)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=30)),
                ('complemento', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
                ('codigo_ibge', models.IntegerField(blank=True, null=True)),
                ('quantidade_quartos', models.IntegerField()),
                ('quantidade_salas', models.IntegerField()),
                ('quantidade_cozinhas', models.IntegerField()),
                ('quantidade_banheiros', models.IntegerField()),
                ('quantidade_quintais', models.IntegerField()),
                ('quantidade_outros', models.IntegerField()),
                ('observacoes', models.TextField(blank=True)),
                ('motivo_cancelamento', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('candidatos', models.ManyToManyField(blank=True, related_name='candidatos', to=settings.AUTH_USER_MODEL)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente', to=settings.AUTH_USER_MODEL)),
                ('diarista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='diarista', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]