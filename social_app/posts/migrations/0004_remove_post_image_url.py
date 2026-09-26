from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_post_image_url_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="image_url",
        ),
    ]
