# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='file',
            field=models.FileField(default=b'http://www.hooyou.com/services/contracts/I539B1.pdf', upload_to=b''),
        ),
    ]
