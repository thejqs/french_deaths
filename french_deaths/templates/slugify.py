
class Slugify(name):

    def __init__(self, name):
        self.name = name

    def totally_like_slugify(self):

        slug = ''

        for char in self.name:
            if not char.isalnum():
                return ''
            elif char == ' ':
                slug += '-'
            else slug += char

        return slug

a = Slugify(@two2for zeo0whywhywhy)

print a.totally_like_slugify()