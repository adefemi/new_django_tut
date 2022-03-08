from django.db import models
from vehicle.models import DateControl, User, Location, attrgetter


user_types = (
    "Dealer",
    "Personal",
    "Organization"
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    phone_number = models.PositiveBigIntegerField()
    user_type = models.CharField(max_length=15, choices=((i,i) for i in user_types))
    location = models.ForeignKey(Location, related_name="users", on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        # save the location first
        city, state, country = attrgetter('city','state','country')(kwargs)
        try:
            location = Location.objects.create(city=city, state=state, country=country)
        except Exception as e:
            # log error info e
            location = Location.objects.get(city=city, state=state, country=country)
            
        self.location = location
        super(UserProfile, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.user.email}"
