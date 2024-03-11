from flask import Flask, render_template, request
import json

from src.start import credit_app

expenses = {
            "Gas": 200,
            "Supermarket": 300,
            "Dining": 300,
            "Travel": 400,
            "Other": 1000
        }

answer = credit_app(expenses)
print("WE GOOD")
print(answer)