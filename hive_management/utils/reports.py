from hive_management.models import Hive, Treatment
import datetime

def check_treatment():
    hives = Hive.objects.all()
    hdays = (datetime.datetime.today() - datetime.timedelta(days=100)).strftime('%Y-%m-%d')
    treatments = []
    for hive in hives:
        try:
            check_treatment = Treatment.objects.filter(hive=hive).latest('created_on')
            if check_treatment and str(check_treatment.created_on) >= hdays:
                pass
            else: 
                treatments.append(hive)
        except:
            treatments.append(hive)
    return treatments
