from django.contrib import admin
from .models import *
from django.forms.fields import DurationField
from django import forms

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'date')
    list_display = ('name',)

class SessionAdminForm(forms.ModelForm):
    length = DurationField()

    class Meta:
        model = Session
        fields = ('name', 'event', 'length')

    def clean_length(self):
        print(self.data)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    form = SessionAdminForm
    fields = ('name', 'event', 'length')
    list_display = ('name', 'event')


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    fields = ('name','email','bio','company','title','abstract', 'session', 'accepted')
    list_display = ('name','email','title','session','accepted')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('name','email','bio','company','title','abstract', 'session')
        else:
            return self.readonly_fields + ('accepted',)

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    fields = ('user_name','email','bio','company','title','abstract', 'session', 'confirmed')
    list_display = ('user_name','email','title','session','confirmed')

@admin.register(SponsorType)
class SponsorTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name',)

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    fields = ('name', 'logo', 'email', 'contact_name', 'sponsor_type', )
    list_display = ('name' , 'email', 'sponsor_type',)



