from app import app
from flask import Flask,send_file, render_template, flash, redirect, session, url_for, g, request, jsonify

@app.route("/")
def index():
    return send_file("templates/index.html")