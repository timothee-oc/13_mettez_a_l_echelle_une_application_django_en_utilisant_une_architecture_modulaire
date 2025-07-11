from django.db import migrations

def copy_lettings_data(apps, schema_editor):
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')

    old_to_new_address = {}
    for old_addr in OldAddress.objects.all():
        new_addr = NewAddress.objects.create(
            number=old_addr.number,
            street=old_addr.street,
            city=old_addr.city,
            state=old_addr.state,
            zip_code=old_addr.zip_code,
            country_iso_code=old_addr.country_iso_code
        )
        old_to_new_address[old_addr.pk] = new_addr

    for old_letting in OldLetting.objects.all():
        NewLetting.objects.create(
            title=old_letting.title,
            address=old_to_new_address[old_letting.address_id]
        )

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_lettings_data),
    ]
