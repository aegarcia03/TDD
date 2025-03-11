from point_of_sale import PointOfSale

def test_barcode_12345():
    pos = PointOfSale()
    assert pos.scan("12345") == "$7.25"

def test_barcode_23456():
    pos = PointOfSale()
    assert pos.scan("23456") == "$12.50"

def test_barcode_99999():
    pos = PointOfSale()
    assert pos.scan("99999") == "Not found"

def test_empty_barcode():
    pos = PointOfSale()
    assert pos.scan("") == "Error: empty barcode"

def test_total():
    pos = PointOfSale()
    pos.scan("12345")
    pos.scan("23456")
    assert pos.scan("total") == "$19.75"
    