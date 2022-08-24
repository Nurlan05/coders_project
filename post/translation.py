from modeltranslation.translator import translator,TranslationOptions
from post.models import *

class CategoryOptions(TranslationOptions):
    fields=['title',]

translator.register(Category,CategoryOptions)

class PostOptions(TranslationOptions):
    fields=['title','content',]

translator.register(Post,PostOptions)


