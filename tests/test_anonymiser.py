from random import SystemRandom

from hypothesis import given
from hypothesis import strategies as st

from redacted import Anonymiser, AusInfoTypes

anonymiser = Anonymiser(AusInfoTypes)
random = SystemRandom()


def longer_text_strategy():
    return st.builds(
        lambda *args: '{} {} {}'.format(*args),
        st.from_regex(random.choice(AusInfoTypes).expr),
        st.from_regex(random.choice(AusInfoTypes).expr),
        st.from_regex(random.choice(AusInfoTypes).expr),
    )


@given(st.from_regex(anonymiser.expr))
def test_matches_from_types(text):
    matches = list(anonymiser.get_matches(text))
    assert all(map(lambda x: x.type in AusInfoTypes, matches))


@given(longer_text_strategy())
def test_matches_in_text(text):
    matches = list(anonymiser.get_matches(text))
    assert all(map(lambda x: x.text in text, matches))
