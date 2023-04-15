from django.db import models
from django.contrib.auth.models import User
import uuid


class HSKVocab(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.IntegerField()
    unicode = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=50)
    pinyin2 = models.CharField(max_length=50)
    english = models.CharField(max_length=300)
    partofspeech = models.CharField(max_length=30)

    def __str__(self):
        return self.pinyin


class Vocab(models.Model):
    id = models.IntegerField(primary_key=True)
    hsk_level = models.IntegerField()
    difficulty = models.IntegerField()
    simplified = models.CharField(max_length=50)
    traditional = models.CharField(max_length=50)
    unicode = models.CharField(max_length=50)
    pinyin1 = models.CharField(max_length=50)
    pinyin2 = models.CharField(max_length=50)
    pinyin3 = models.CharField(max_length=50)
    english1 = models.CharField(max_length=200)
    english2 = models.CharField(max_length=200)
    english3 = models.CharField(max_length=200)
    partofspeech = models.CharField(max_length=50)
    s1_char = models.CharField(max_length=50)
    s2_char = models.CharField(max_length=50)
    s3_char = models.CharField(max_length=50)
    s1_pinyin = models.CharField(max_length=200)
    s2_pinyin = models.CharField(max_length=200)
    s3_pinyin = models.CharField(max_length=200)
    s1_english = models.CharField(max_length=200)
    s2_english = models.CharField(max_length=200)
    s3_english = models.CharField(max_length=200)
    is_vocab = models.IntegerField()
    word_freq_rank = models.IntegerField()

    def __str__(self):
        return self.pinyin1


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    traditional = models.CharField(max_length=50)
    simplified = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=50)
    pinyin2 = models.CharField(max_length=50)
    pinyin3 = models.CharField(max_length=50)
    english = models.CharField(max_length=300)
    unicode = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    hsk = models.CharField(max_length=50)
    ranking = models.IntegerField()
    pos = models.CharField(max_length=50)

    def __str__(self):
        return self.simplified

