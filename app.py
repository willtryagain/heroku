import io
import json

from PIL import Image
from flask import Flask, jsonify, request


app = Flask(__name__)