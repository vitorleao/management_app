from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                (
                    'id', models.BigAutoField(
                                            auto_created=True,
                                            primary_key=True,
                                            serialize=False,
                                            verbose_name='ID'
                                        )
                ),
                (
                    'name', models.CharField(
                                            max_length=255,
                                            verbose_name='name'
                                        )
                ),
                (
                    'email', models.EmailField(
                                            max_length=255,
                                            verbose_name='email'
                                            )
                ),
                (
                    'department', models.CharField(
                                                    max_length=255,
                                                    verbose_name='department'
                                                )
                ),
            ],
        ),
    ]
