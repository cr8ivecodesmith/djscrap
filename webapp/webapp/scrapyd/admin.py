from django.contrib import admin

from .models import Server, Project, Spider, Job


class ServerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'url',
        'active',
    ]
    list_editable = [
        'active',
    ]
    filter_fields = [
        'active',
    ]


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'server',
        'active',
    ]
    list_editable = [
        'active',
    ]
    filter_fields = [
        'server',
        'active',
    ]


class SpiderAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'project',
        'server',
        'active',
    ]
    list_editable = [
        'active',
    ]
    filter_fields = [
        'project',
        'server',
        'active',
    ]
    search_fields = [
        'name'
    ]

    def server(self, obj):
        return obj.project.server


class JobAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'status',
        'item_count',
        'log_file',
        'output_file',
        'job_created',
        'job_modified',
    ]
    filter_fields = [
        'job_created',
        'job_modified',
        'finish_reason',
        'server',
        'project',
        'spider',
    ]

    def server(self, obj):
        return obj.spider.project.server

    def project(self, obj):
        return obj.spider.project


admin.site.register(Server, ServerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Spider, SpiderAdmin)
admin.site.register(Job, JobAdmin)
