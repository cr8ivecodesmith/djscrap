from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True

    def __repr__(self):
        return '<{self.__class__.__name__}:[{self.id}] {self.name}>'.format(
            self=self
        )

    def __str__(self):
        return self.name


class Server(Base):
    url = models.URLField(unique=True)


class Project(Base):
    server = models.ForeignKey(Server)

    class Meta:
        unique_together = ('name', 'server',)


class Spider(Base):
    project = models.ForeignKey(Project)

    class Meta:
        unique_together = ('name', 'project',)


class Job(Base):
    PENDING = 'pending'
    RUNNING = 'running'
    FINISHED = 'finished'
    STATUS = (
        (PENDING, PENDING,),
        (RUNNING, RUNNING,),
        (FINISHED, FINISHED,),
    )

    spider = models.ForeignKey(Spider)
    status = models.CharField(max_length=12, choices=STATUS, default=PENDING)
    output_file = models.URLField(max_length=512, blank=True)
    log_file = models.URLField(max_length=512, blank=True)
    item_count = models.PositiveIntegerField(default=0)
    job_created = models.DateTimeField(null=True, blank=True)
    job_modified = models.DateTimeField(null=True, blank=True)
    finish_reason = models.CharField(max_length=24, blank=True)
    stats = models.TextField(blank=True)

    class Meta:
        unique_together = ('name', 'spider',)
