# Generated by Django 5.0.1 on 2024-02-01 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabs', '0002_alter_property_options_alter_vocabulary_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predicate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=256)),
                ('object_type', models.CharField(choices=[('URIRef', 'Uri Ref'), ('Literal', 'Literal')], max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='vocabs.term'),
        ),
        migrations.AlterField(
            model_name='term',
            name='vocabulary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terms', to='vocabs.vocabulary'),
        ),
        migrations.AlterField(
            model_name='property',
            name='predicate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vocabs.predicate'),
        ),
    ]
