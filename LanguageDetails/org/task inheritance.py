# QUESTION
# 1:
# ------------
# package name: org.all
# Project name: LanguageDetails
#
# Class name: Languageclass
# Methods: all_Language
#
# Class name: Tamil
# Methods: tamil_Language
#
# Class name: English
# Methods: english_Language
#
# Class name: Telgu
# Methods: telgu_Language
#
# Description: create all class methods into the Languageclass[derived class]
# using multilevel inheritance.
# class Languageclass():
#     def all_Language(self):
#         print("Tamil,English,Telgu")
# class Tamil(Languageclass):
#     def tamil_Language(self):
#         print("tamil")
# class English(Tamil):
#     def english_Language(self):
#         print("english")
# class Telgu(English):
#     def telgu_Language(self):
#         print("telgu")
#
# c=Telgu()
# c.all_Language()
# c.tamil_Language()
# c.english_Language()
# c.telgu_Language()

#

# QUESTION 5:
# -----------
#      Project   :LanguageDetails
#      Package   :org.lang
#      Class     :LanguageInfo
#      Methods   :tamil_Language(),english_Language(),hindi_Language()
#
#      Class     :StateDetails
#      Methods   :south_India(),north_India()
#
# Description:
# create above 2 class
# Assume LanguageInfo as derived class and stateDetails
# as Parent class using single inheritance.

class LanguageInfo():
    def tamil_Language(self):
        print("tamil language")
    def english_Language(self):
        print("english language")
    def hindi_Language(self):
        print("hindi language")

class StateDetails(LanguageInfo):
    def south_India(self):
        print("south india")
    def north_India(self):
        print("north india")
a=StateDetails()
a.south_India()
a.north_India()
a.hindi_Language()
a.english_Language()
a.tamil_Language()




