# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.URLField(default=b'http://farm4.staticflickr.com/3130/2836828090_67d4900ab3_o.jpg', blank=True),
            preserve_default=True,
        ),
    ]
