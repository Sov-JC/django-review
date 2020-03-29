from django.contrib import admin

from .models import Choice
from .models import Question


'''admin.site.register(Question)'''

'''
class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text'] '''

'''
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]'''

class ChoiceInline(admin.StackedInline): #can be admin.TabularInline for more compact view
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline] 

	list_display = ('question_text', 'pub_date', 'was_published_recently') #adds columns 'question text', 'date published', and 'was published recently'"
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)