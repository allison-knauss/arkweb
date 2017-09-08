from flask import render_template
from app import app
from clients import page_client

def nav(current_path):
    return {
        'pages': page_client.all().json(),
        'current_path': current_path
    }
