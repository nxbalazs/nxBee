from hive_management.models import Hive


class Divide:
    def __init__(self):
        self.good_queens = Hive.objects.filter(purpose='Queen').filter(frames__gt=6).order_by('-strength')
        self.hives_for_bee_production = Hive.objects.filter(purpose='Bee').filter(frames__gt=6).order_by('-strength')
        self.queen_hive = False
        self.hives_to_divide = []

    def make_divided_hive_queen(self):
        if self.good_queens.count() != 0 and self.good_queens[0].strength > 65:
            self.queen_hive = self.good_queens[0]
        else:
            self.queen_hive = False

        return self.queen_hive

    def make_divided_hive(self):
        if self.hives_for_bee_production.count() >= 2 and self.hives_for_bee_production[1].strength > 65 and self.queen_hive != False:
            self.hives_to_divide.append(self.hives_for_bee_production[0])
            self.hives_to_divide.append(self.hives_for_bee_production[1])
        elif self.hives_for_bee_production.count() >= 3 and self.hives_for_bee_production[2].strength > 65 and self.queen_hive == False:
            self.hives_to_divide.append(self.hives_for_bee_production[0])
            self.hives_to_divide.append(self.hives_for_bee_production[1])
            self.hives_to_divide.append(self.hives_for_bee_production[2])
        else:
            self.hives_to_divide.append(False)

        return self.hives_to_divide

