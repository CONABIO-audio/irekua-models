# Generated by Django 3.0.5 on 2020-04-26 19:14

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import irekua_database.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('irekua_database', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on', help_text='Date of creation', verbose_name='created on')),
                ('modified_on', models.DateTimeField(auto_now=True, db_column='modified_on', help_text='Date of last modification', verbose_name='modified on')),
                ('name', models.CharField(db_column='name', help_text='Name of the model.', max_length=64, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, db_column='description', help_text='Description of the model.', null=True, verbose_name='description')),
                ('repository', models.URLField(db_column='repository', help_text='URL for repository of model code.', verbose_name='repository')),
                ('annotation_type', models.ForeignKey(db_column='annotation_type_id', help_text='Type of annotation produced by the model.', on_delete=django.db.models.deletion.CASCADE, to='irekua_database.AnnotationType', verbose_name='annotation type')),
                ('created_by', models.ForeignKey(blank=True, db_column='creator_id', help_text='Creator of object', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='model_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('event_types', models.ManyToManyField(blank=True, help_text='Event types that can be detected by the model.', to='irekua_database.EventType')),
                ('item_types', models.ManyToManyField(blank=True, help_text='Item Types that can be processed by the model', to='irekua_database.ItemType')),
                ('modified_by', models.ForeignKey(blank=True, db_column='modified_by', editable=False, help_text='User who made modifications last', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
                ('terms', models.ManyToManyField(blank=True, help_text='Terms that the model uses for its predictions.', to='irekua_database.Term')),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
                'ordering': ['-modified_on'],
            },
        ),
        migrations.CreateModel(
            name='ModelVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on', help_text='Date of creation', verbose_name='created on')),
                ('modified_on', models.DateTimeField(auto_now=True, db_column='modified_on', help_text='Date of last modification', verbose_name='modified on')),
                ('version', models.CharField(db_column='version', help_text='Version of the model', max_length=32, verbose_name='version')),
                ('created_by', models.ForeignKey(blank=True, db_column='creator_id', help_text='Creator of object', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modelversion_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('model', models.ForeignKey(db_column='model_id', help_text='Model being versioned.', on_delete=django.db.models.deletion.CASCADE, to='irekua_models.Model', verbose_name='model')),
                ('modified_by', models.ForeignKey(blank=True, db_column='modified_by', editable=False, help_text='User who made modifications last', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modelversion_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'verbose_name': 'Model Version',
                'verbose_name_plural': 'Model Versions',
                'ordering': ['created_on', '-version'],
                'unique_together': {('model', 'version')},
            },
        ),
        migrations.CreateModel(
            name='ModelPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on', help_text='Date of creation', verbose_name='created on')),
                ('modified_on', models.DateTimeField(auto_now=True, db_column='modified_on', help_text='Date of last modification', verbose_name='modified on')),
                ('certainty', models.FloatField(db_column='certainty', help_text='Model certainty of prediction. A number from 0 to 1.', verbose_name='certainty')),
                ('annotation', django.contrib.postgres.fields.jsonb.JSONField(db_column='annotation', default=irekua_database.utils.empty_JSON, help_text='Information of annotation location within item', verbose_name='annotation')),
                ('created_by', models.ForeignKey(blank=True, db_column='creator_id', help_text='Creator of object', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modelprediction_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('event_type', models.ForeignKey(db_column='event_type_id', help_text='Event predicted by the model.', on_delete=django.db.models.deletion.PROTECT, to='irekua_database.EventType', verbose_name='event type')),
                ('item', models.ForeignKey(db_column='item_id', help_text='Item on which the prediction was made.', on_delete=django.db.models.deletion.CASCADE, to='irekua_database.Item', verbose_name='item')),
                ('labels', models.ManyToManyField(help_text='Terms used as labels to describe the predicted event.', to='irekua_database.Term', verbose_name='labels')),
                ('model_version', models.ForeignKey(db_column='model_version_id', help_text='Model and version used for this prediction', on_delete=django.db.models.deletion.PROTECT, to='irekua_models.ModelVersion', verbose_name='model version')),
                ('modified_by', models.ForeignKey(blank=True, db_column='modified_by', editable=False, help_text='User who made modifications last', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modelprediction_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'verbose_name': 'Model Prediction',
                'verbose_name_plural': 'Model Predictions',
                'ordering': ['-modified_on'],
            },
        ),
    ]
