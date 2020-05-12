# Generated by Django 3.0.3 on 2020-05-11 23:22

import apps.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sspanel", "0042_auto_20200506_0744"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rebaterecord",
            options={"ordering": ("-created_at",), "verbose_name_plural": "返利记录"},
        ),
        migrations.AlterField(
            model_name="ssnode",
            name="method",
            field=models.CharField(
                choices=[
                    ("aes-256-cfb", "aes-256-cfb"),
                    ("aes-128-ctr", "aes-128-ctr"),
                    ("rc4-md5", "rc4-md5"),
                    ("salsa20", "salsa20"),
                    ("chacha20", "chacha20"),
                    ("none", "none"),
                    ("chacha20-ietf-poly1305", "chacha20-ietf-poly1305"),
                    ("aes-128-gcm", "aes-128-gcm"),
                    ("aes-256-gcm", "aes-256-gcm"),
                ],
                default="aes-256-cfb",
                max_length=32,
                verbose_name="加密类型",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="ss_method",
            field=models.CharField(
                choices=[
                    ("aes-256-cfb", "aes-256-cfb"),
                    ("aes-128-ctr", "aes-128-ctr"),
                    ("rc4-md5", "rc4-md5"),
                    ("salsa20", "salsa20"),
                    ("chacha20", "chacha20"),
                    ("none", "none"),
                    ("chacha20-ietf-poly1305", "chacha20-ietf-poly1305"),
                    ("aes-128-gcm", "aes-128-gcm"),
                    ("aes-256-gcm", "aes-256-gcm"),
                ],
                default="aes-256-cfb",
                max_length=32,
                verbose_name="加密",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="ss_password",
            field=models.CharField(
                default=apps.utils.get_short_random_string,
                max_length=32,
                unique=True,
                verbose_name="密码",
            ),
        ),
    ]