# Generated by Django 4.2.11 on 2024-12-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_location_neighboring_locations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='clazz',
            new_name='class_field',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='from_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='organizations',
            new_name='related_organizations',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='clazz',
            new_name='class_field',
        ),
        migrations.AddField(
            model_name='character',
            name='hostility',
            field=models.TextField(blank=True, choices=[('F', 'Friendly'), ('N', 'Neutral'), ('H', 'Hostile'), ('?', 'Unknown')], default='N'),
        ),
        migrations.AlterField(
            model_name='character',
            name='related_characters',
            field=models.ManyToManyField(blank=True, related_name='related_characters', to='core.character'),
        ),
        migrations.AlterField(
            model_name='location',
            name='hostility',
            field=models.TextField(choices=[('F', 'Friendly'), ('N', 'Neutral'), ('H', 'Hostile'), ('?', 'Unknown')], default='N'),
        ),
        migrations.AlterField(
            model_name='note',
            name='hostility',
            field=models.TextField(blank=True, choices=[('F', 'Friendly'), ('N', 'Neutral'), ('H', 'Hostile'), ('?', 'Unknown')], default='N', null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='hostility',
            field=models.TextField(choices=[('F', 'Friendly'), ('N', 'Neutral'), ('H', 'Hostile'), ('?', 'Unknown')], default='N'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='related_organizations',
            field=models.ManyToManyField(blank=True, related_name='related_organizations', to='core.organization'),
        ),
        migrations.DeleteModel(
            name='NonPlayerCharacter',
        ),
    ]
