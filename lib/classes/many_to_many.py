class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of Author class.")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of Magazine class.")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, "_title"):
            self._title = title
        else:
            raise ValueError("Title must be a string with length between 5 and 50 characters.")


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "_name"):
            self._name = name

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        magazines = self.magazines()
        if magazines:
            return list({mag.category for mag in self.magazines()})
        else:
            return None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0 < len(category):
            self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        articles = self.articles()
        if articles:
            return [article.title for article in articles]
        else:
            return None

    def contributing_authors(self):
        contributors = [article.author for article in self.articles()]
        if len(contributors) > 2:
            return contributors

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_article_count = {magazine: len(magazine.articles()) for magazine in cls.all}
        return max(magazine_article_count, key=magazine_article_count.get)