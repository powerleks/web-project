from django.contrib.auth.models import User
from django.db import models

class QuestionManager(models.Manager):
    def popular(self):
        # from django.db import connection
        # with connection.cursor() as cursor:
        #     cursor.execute("""
        #         SELECT *
        #         FROM qa_question
        #         ORDER BY rating DESC""")
        #     result_list = []
        #     for row in cursor.fetchall():
        #         q = self.model(title=row[0], text=row[1], added_at=row[2], rating=row[3], author=row[4])
        #         result_list.append(q)
        return self.order_by('-rating')

    def new(self):
        # from django.db import connection
        # with connection.cursor() as cursor:
        #     cursor.execute("""
        #         SELECT *
        #         FROM qa_question
        #         ORDER BY added_at DESC""")
        #     result_list = []
        #     for row in cursor.fetchall():
        #         q = self.model(title=row[0], text=row[1], added_at=row[2], rating=row[3], author=row[4])
        #         result_list.append(q)
        return self.order_by('-added_at')
            
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)