# Generated by Django 2.2.13 on 2021-02-19 07:57

import DjangoUeditor.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=' 新闻标题')),
                ('description', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('newsType', models.CharField(choices=[('企业要闻', '企业要闻'), ('行业新闻', '行业新闻'), ('通知公告', '通知公告')], max_length=50, verbose_name='新闻类型')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
                'ordering': ['-publishDate'],
            },
        ),
        migrations.DeleteModel(
            name='MyNew',
        ),
    ]
