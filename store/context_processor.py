from .models import Category


def processor(request):
    category_objs = Category.objects.all()
    return {'categories': category_objs}
