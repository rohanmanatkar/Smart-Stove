from django.db import models

# Create your models here.
from django.db import models


class State(models.Model):
    temp = models.FloatField()
    proximity1 = models.FloatField()
    proximity2 = models.FloatField()

    @staticmethod
    def get_state():
        data = None
        try:
            state = State.objects.all()[0]
            print(state)

            data = {'temp': state.temp,
                    'proximity1': state.proximity1,
                    'proximity2': state.proximity2}
            print(data) 

        except Exception as e:
            print(str(e))
            return {}
        return data
 
    @staticmethod
    def mobileApp():
        data = None
        try:
            state = State.objects.all()[0]
            print(state)

            data = {'temp': state.temp,
                    'proximity1': state.proximity1,
                    'proximity2': state.proximity2}
            print(data)

        except Exception as e:
            print(str(e))
            return {}
        return data

    @staticmethod
    def saveState(temp, p1, p2):
        try:
            State.objects.all().delete()
            new = State()
            new.temp = temp
            new.proximity1 = p1
            new.proximity2 = p2
            new.save()
           # print(State.objects.all()[0])
        except Exception as e:
            print(str(e))
            return False
        return True
