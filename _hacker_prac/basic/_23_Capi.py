"""
You are asked to ensure that the first and last names of people begin with a capital letter
in their passports. For example, alison heck should be capitalized correctly as Alison Heck.

alison heck  – Alison Heck

Given a full name, your task is to capitalize the name appropriately.
"""

'''
fn =  input("Enter first name : ")
ln = input("Enter second name : ")
name = fn.capitalize()+ " " + ln.capitalize()
print(name)
'''
n =  input("Enter first name : ")

rs1=""
for i in n[:].split():
  rs=i.capitalize()
  rs1 = rs1 + " " +rs
print(rs1)





