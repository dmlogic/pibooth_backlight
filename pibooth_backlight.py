# -*- coding: utf-8 -*-

"""Pibooth plugin for backlight during capture."""

import pibooth
import RPi.GPIO as GPIO
from pibooth.utils import LOGGER

controlPin = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(controlPin,GPIO.OUT)

__version__ = "0.0.1"

@pibooth.hookimpl
def pibooth_startup(app):
    LOGGER.info("Backlight turning off at startup")
    GPIO.output(controlPin,GPIO.HIGH)

@pibooth.hookimpl
def state_preview_enter(app):
    LOGGER.info("Backlight turning on")
    GPIO.output(controlPin,GPIO.LOW)

@pibooth.hookimpl
def state_processing_enter(app):
    LOGGER.info("Backlight turning off")
    GPIO.output(controlPin,GPIO.HIGH)
