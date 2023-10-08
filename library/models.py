from django.db import models

class Department(models.Model):
    department = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.abbreviation

class Group(models.Model):
    uid = models.CharField(max_length=6)

    def __str__(self) -> str:
        return self.uid

class Course(models.Model):
    course = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=16)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=-1)

    def __str__(self) -> str:
        return self.abbreviation

class Document(models.Model):
    title = models.CharField(max_length=128)
    school_year = models.CharField(max_length=9)
    abstract = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=-1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=-1)
    file = models.FileField(upload_to='documents/')

    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=-1)

    def __str__(self) -> str:
        return self.name

class Adviser(models.Model):
    name = models.CharField(max_length=64)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=-1)

    def __str__(self) -> str:
        return self.name