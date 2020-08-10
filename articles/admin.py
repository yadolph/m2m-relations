from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ScopeAssign

class ScopeAssignInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    counter += 1
                    print(counter)

        if counter != 1:
            raise ValidationError('Должен быть выбран основной раздел и он должен быть всегда один')

        return super().clean()


class ScopeAssignInline(admin.TabularInline):
    model = ScopeAssign
    formset = ScopeAssignInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeAssignInline]
