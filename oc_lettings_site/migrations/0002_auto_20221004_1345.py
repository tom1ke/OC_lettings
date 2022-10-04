# Generated by Django 3.0 on 2022-10-04 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name='letting',
                    name='address',
                ),
            ],
            database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name='profile',
                    name='user',
                ),
            ],
            database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Address',
                ),
            ],
            database_operations=[
                    migrations.AlterModelTable(
                        name='Address',
                        table='lettings_address',
                    )
                ],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Letting',
                ),
            ],
            database_operations=[
                    migrations.AlterModelTable(
                        name='Letting',
                        table='lettings_letting',
                    )
                ],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Profile',
                ),
            ],
            database_operations=[
                    migrations.AlterModelTable(
                        name='Profile',
                        table='profiles_profile',
                    )
                ],
        ),
    ]
