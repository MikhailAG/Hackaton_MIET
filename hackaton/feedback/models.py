from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    role = models.ForeignKey('Roles', on_delete=models.CASCADE)
    lead_user = models.ForeignKey('Users', on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=256)

class Roles(models.Model):
    name = models.CharField(max_length=100)

class Feedbacks(models.Model):
    body = models.TextField()
    stars = models.IntegerField(max_length=1)
    subjectivity = models.IntegerField(max_length=1)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='received_feedbacks')
    from_user = models.ForeignKey(Users, on_delete=models.CASCADE,  related_name='given_feedbacks')
    body_english = models.TextField(blank=True, null=True)

class Notifications(models.Model):
    comment = models.TextField()
    lead = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='received_notifications')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sent_notifications')
    is_read = models.BooleanField(default=False)

