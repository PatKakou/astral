# -*- coding: utf-8 -*-
from nose.tools import raises

import pytz
from astral import City

def test_Name():
    c = City()
    assert c.name == 'Greenwich'
    c.name = 'London'
    assert c.name == 'London'
    c.name = 'Köln'
    assert c.name == 'Köln'

def test_Country():
    c = City()
    assert c.country == 'England'
    c.country = 'Australia'
    assert c.country == 'Australia'

def test_TimezoneName():
    c = City()
    assert c.timezone == 'Europe/London'
    c.name = 'Asia/Riyadh'
    assert c.name == 'Asia/Riyadh'

def test_Timezone():
    c = City()
    assert c.tz == pytz.timezone('Europe/London')
    c.timezone='Europe/Stockholm'
    assert c.tz == pytz.timezone('Europe/Stockholm')

def test_Dawn():
    c = City()
    c.dawn()

def test_Sunrise():
    c = City()
    c.sunrise()

def test_SolarNoon():
    c = City()
    c.solar_noon()

def test_Dusk():
    c = City()
    c.dusk()

def test_Sunset():
    c = City()
    c.sunset()
    
def test_Elevation():
    c = City()
    c.solar_elevation()
    
def test_Azimuth():
    c = City()
    c.solar_azimuth()

@raises(AttributeError)
def test_TzError():
    c = City()
    c.tz = 1
