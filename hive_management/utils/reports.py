from hive_management.models import Hive, Treatment

def check_treatment():
    hives = Hive.objects.all()
    treatments = []
    for hive in hives:
        check_treatment = Treatment.objects.filter(hive=hive)
        if check_treatment:
            pass
        else: 
            treatments.append(hive)
    return treatments
