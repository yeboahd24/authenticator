# Generated by Django 4.2.3 on 2023-07-27 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("otp_totp", "0002_auto_20190420_0723"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="otp_device",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="otp_totp.totpdevice",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to.",
                related_name="customuser_set",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="customuser_set",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]