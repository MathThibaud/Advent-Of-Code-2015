#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 23:15:53 2021

@author: mathieuthibaud

"""

fichier = open("input12", "r")

donnees = fichier.read()
donnees2 = eval(donnees)



def partie1(text):  # Version lisant seulement entiers
    nb = 0
    current = ""
    i = 0
    while i < len(text):
        if not text[i] in "-1234567890":
            i += 1
            if current != "":
                nb += int(current)
                current = ""
        else:
            current += text[i]
            i += 1
    if current != "":
        nb += int(current)
    return nb


def partie1bis(expression, val=0): # Version utilisant structure list et dict
    if type(expression) is list:
        for ele in expression:
            if type(ele) is list or type(ele) is dict:
                val = partie1bis(ele, val)
            if type(ele) is int:
                val += ele
    if type(expression) is dict:
        for ele in expression:
            if type(expression[ele]) is list or type(expression[ele]) is dict:
               val = partie1bis(expression[ele], val)
            if type(expression[ele]) is int:
                val += expression[ele]
    return val


def partie2(expression, val=0):
    if type(expression) is list:
        for ele in expression:
            if type(ele) is list or type(ele) is dict:
                val = partie2(ele, val)
            if type(ele) is int:
                val += ele
    if type(expression) is dict:
        if not("red" in expression.values()):
            for ele in expression:
                if type(expression[ele]) is list or type(expression[ele]) is dict:
                   val = partie2(expression[ele], val)
                if type(expression[ele]) is int:
                    val += expression[ele]
    return val
    
    

print("Advent Of The Code 2015")
print("Jour 12")
print(f"Réponse partie 1 : {partie1bis(donnees2)} ")
print(f"Réponse partie 2 : {partie2(donnees2)} ")
      
    