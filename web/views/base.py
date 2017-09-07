from flask import render_template
from app import app
from clients import page_client

def nav():
    return page_client.all().json()
