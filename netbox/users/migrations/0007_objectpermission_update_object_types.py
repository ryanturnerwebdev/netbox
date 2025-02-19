# Generated by Django 5.0.1 on 2024-03-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0010_gfk_indexes'),
        ('users', '0006_custom_group_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectpermission',
            name='object_types',
            field=models.ManyToManyField(
                limit_choices_to=models.Q(
                    models.Q(
                        models.Q(
                            (
                                'app_label__in',
                                ['account', 'admin', 'auth', 'contenttypes', 'sessions', 'taggit', 'users'],
                            ),
                            _negated=True,
                        ),
                        models.Q(('app_label', 'auth'), ('model__in', ['group', 'user'])),
                        models.Q(('app_label', 'users'), ('model__in', ['objectpermission', 'token'])),
                        _connector='OR',
                    )
                ),
                related_name='object_permissions',
                to='core.objecttype',
            ),
        ),
    ]
