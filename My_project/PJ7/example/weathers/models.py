from django.db import models

# Create your models here.

class Weather(models.Model):
    # 1. 이름을 맞춰줌                   # 2. 주석은 자세하게
    dt_txt = models.DateTimeField()     # 관측 시간
    temp = models.FloatField()          # 온도(기본값 : 켈빈 온도)
    feels_like = models.FloatField()    # 체감 온도(기본값 : 켈빈 온도)
    
