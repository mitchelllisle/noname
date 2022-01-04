from noname import Email, AusPassport, AusDriversLicence, AusTaxFileNumber, AusPostCode, AusLicensePlate, AusInfoTypes
from hypothesis import given, strategies as st


@given(st.from_regex(Email.expr))
def test_email(email):
    found = Email.compiled().search(email)
    assert found is not None


@given(st.from_regex(AusPassport.expr))
def test_passport(passport):
    found = AusPassport.compiled().search(passport)
    assert found is not None


@given(st.from_regex(AusDriversLicence.expr))
def test_drivers_license(licence):
    found = AusDriversLicence.compiled().search(licence)
    assert found is not None


@given(st.from_regex(AusTaxFileNumber.expr))
def test_tfn(tfn):
    found = AusTaxFileNumber.compiled().search(tfn)
    assert found is not None


@given(st.from_regex(AusPostCode.expr))
def test_postcode(postcode):
    found = AusPostCode.compiled().search(postcode)
    assert found is not None


@given(st.from_regex(AusLicensePlate.expr))
def test_license_plate(license_plate):
    found = AusLicensePlate.compiled().search(license_plate)
    assert found is not None


def test_aus_info_types():
    assert isinstance(AusInfoTypes, list)
