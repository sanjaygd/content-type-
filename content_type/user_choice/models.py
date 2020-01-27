from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

# from user_choice.models import Activity

User = get_user_model()


class Activity(models.Model):
    FAVORITE = 'F'
    LIKE = 'L'
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPE = (
        (FAVORITE,'Favorite'),
        (LIKE,'Like'),
        (UP_VOTE,'Up Vote'),
        (DOWN_VOTE,'Down Vote'),

    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=1,choices=ACTIVITY_TYPE)
    created_on = models.DateTimeField(auto_now_add=True)

    #Below are the mandatory fields for generic relationship
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Activity)


class Comment(models.Model):
    comenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    modified_on=models.DateTimeField(auto_now=True)
    vote = GenericRelation(Activity)
    






