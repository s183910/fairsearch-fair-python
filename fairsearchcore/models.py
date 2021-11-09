# -*- coding: utf-8 -*-

"""
fairsearchcore.models
~~~~~~~~~~~~~~~
This module contains the primary objects that power fairsearchore.
"""
from Kat_GABS import dataframen

class FairScoreDoc(object):
    """The :class:`FairScoreDoc` object, which is a representation of the items in the rankings.
    Contains a `id`, `score` and `is_protected` attribute
    """
    # df = pd.read_csv("GUDF.csv")
    def __init__(self, id, score, is_protected):
        # self.df = dataframen
        self.id = dataframen.Idx
        self.score = dataframen.Preds
        self.is_protected = dataframen.GENDER_bins

    def __repr__(self):
        return "<FairScoreDoc [%s]>" % ("Protected" if self.is_protected else "Nonprotected")

# class Tilbage(FairScoreDoc):
#     def Tilbage_nu(self):
#         return "<FairScoreDoc [%s]>" % ("Protected" if self.is_protected else "Nonprotected")
