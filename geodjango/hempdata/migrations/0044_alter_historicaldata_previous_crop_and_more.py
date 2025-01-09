# Generated by Django 5.1.3 on 2025-01-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hempdata', '0043_alter_soilpreparation_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaldata',
            name='previous_crop',
            field=models.CharField(choices=[('Mais', 'Mais'), ('Hanf', 'Hanf'), ('Flachs', 'Flachs')], help_text='Welche Vorfrucht wurde auf dem Schlag bereits angebaut?', max_length=100, verbose_name='Vorfrucht'),
        ),
        migrations.AlterField(
            model_name='historicaldata',
            name='sommerung',
            field=models.CharField(blank=True, choices=[('2024 Sommerung', '2024 Sommerung'), ('2023 Sommerung', '2023 Sommerung'), ('2022 Sommerung', '2022 Sommerung'), ('2021 Sommerung', '2021 Sommerung'), ('2020 Sommerung', '2020 Sommerung'), ('2019 Sommerung', '2019 Sommerung'), ('2018 Sommerung', '2018 Sommerung'), ('2017 Sommerung', '2017 Sommerung'), ('2016 Sommerung', '2016 Sommerung'), ('2015 Sommerung', '2015 Sommerung'), ('2014 Sommerung', '2014 Sommerung'), ('2013 Sommerung', '2013 Sommerung'), ('2012 Sommerung', '2012 Sommerung'), ('2011 Sommerung', '2011 Sommerung'), ('2010 Sommerung', '2010 Sommerung'), ('2009 Sommerung', '2009 Sommerung'), ('2008 Sommerung', '2008 Sommerung'), ('2007 Sommerung', '2007 Sommerung'), ('2006 Sommerung', '2006 Sommerung'), ('2005 Sommerung', '2005 Sommerung')], help_text='Nur Ausfüllen, wenn es sich um eine Sommerung handelt.', max_length=100, null=True, verbose_name='Jahr der Sommerung'),
        ),
        migrations.AlterField(
            model_name='historicaldata',
            name='winterung',
            field=models.CharField(blank=True, choices=[('2024/2025 Winterung', '2024/2025 Winterung'), ('2023/2024 Winterung', '2023/2024 Winterung'), ('2022/2023 Winterung', '2022/2023 Winterung'), ('2021/2022 Winterung', '2021/2022 Winterung'), ('2020/2021 Winterung', '2020/2021 Winterung'), ('2019/2020 Winterung', '2019/2020 Winterung'), ('2018/2019 Winterung', '2018/2019 Winterung'), ('2017/2018 Winterung', '2017/2018 Winterung'), ('2016/2017 Winterung', '2016/2017 Winterung'), ('2015/2016 Winterung', '2015/2016 Winterung'), ('2014/2015 Winterung', '2014/2015 Winterung'), ('2013/2014 Winterung', '2013/2014 Winterung'), ('2012/2013 Winterung', '2012/2013 Winterung'), ('2011/2012 Winterung', '2011/2012 Winterung'), ('2010/2011 Winterung', '2010/2011 Winterung'), ('2009/2010 Winterung', '2009/2010 Winterung'), ('2008/2009 Winterung', '2008/2009 Winterung'), ('2007/2008 Winterung', '2007/2008 Winterung'), ('2006/2007 Winterung', '2006/2007 Winterung'), ('2005/2006 Winterung', '2005/2006 Winterung')], help_text='Nur Ausfüllen, wenn es sich um eine Winterung handelt.', max_length=100, null=True, verbose_name='Jahr der Winterung'),
        ),
    ]
