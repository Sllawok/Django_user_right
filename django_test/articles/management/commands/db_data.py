from django.core.management.base import BaseCommand
from articles.models import Article, Tag


class Command(BaseCommand):

    def handle(self, *args, **options):



# Запрос в базу без условия!
        print('DB command!')
        articles = Article.objects.all()
        print(type(articles), articles)
        for art in articles:
            print(art.article_text)

#Запрос в базу c условием!

    #   get
        art_ = Article.objects.get(article_name = 'Happy lion')
        print(art_)
    #  filter
        tags = Tag.objects.filter(tag_name = 'nature')
        print(tags)

# Связанные поля
        print(art_.article_tag.all())
        print(art_.article_tag.first())


# Добавление в БД
        Tag.objects.create(tag_name = 'Travelling')
        tags = Tag.objects.all()
        print(tags)

# Удаление
        tag = Tag.objects.filter(tag_name='Travelling')
        tag.delete()


        tags = Tag.objects.all()
        print(tags)