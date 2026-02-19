import pytest
from dash.testing.application_runners import import_app


def test_header_present(dash_duo):
    """Test 1: Check that the header is present"""
    app = import_app('appp')
    dash_duo.start_server(app)
    dash_duo.wait_for_element('h1', timeout=10)
    header = dash_duo.find_element('h1')
    assert header is not None
    assert 'Soul Foods' in header.text


def test_visualisation_present(dash_duo):
    """Test 2: Check that the line chart visualisation is present"""
    app = import_app('appp')
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#sales-chart', timeout=10)
    chart = dash_duo.find_element('#sales-chart')
    assert chart is not None


def test_region_picker_present(dash_duo):
    """Test 3: Check that the region radio button picker is present"""
    app = import_app('appp')
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#region-filter', timeout=10)
    region_picker = dash_duo.find_element('#region-filter')
    assert region_picker is not None
    options = dash_duo.find_elements('input[type="radio"]')
    assert len(options) == 5