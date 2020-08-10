from django import template
from articles.models import Article, Scope, ScopeAssign

register = template.Library()


@register.filter
def is_main(scope, article):
    assigner = ScopeAssign.objects.filter(scope_id=scope.id, article_id = article.id).first()
    return assigner.is_main
