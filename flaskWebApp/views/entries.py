import os
import random, string
from flask import Flask
from flask import request,redirect,url_for,render_template,flash,session
from flaskWebApp import app

import json
import math


@app.route('/')
def main():
    return "hello"
