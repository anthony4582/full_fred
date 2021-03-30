
import pytest
from new_fred.fred import Fred

# I can use the returned METAdata to test success of a method
# ensure method coverage
# test different realtime dates

@pytest.fixture
def fred():
    return Fred()

@pytest.fixture
def expected_get_series_id():
    # fred/series
    """
    The expected value associated with key 'id' in the map returned
    by fred.get_series('GNPCA')
    """
    return "GNPCA"

@pytest.fixture
def expected_get_series_title():
    """
    The expected value associated with key 'title' in the map returned
    by fred.get_series('GNPCA')
    """
    return "Real Gross National Product"

@pytest.mark.skip("passed v1")
def test_get_series(
        fred: Fred,
        expected_get_series_id: str,
        expected_get_series_title: str,
        ):
    # fred/series
    returned_correctly = False
    observed = fred.get_series("GNPCA")
    if "id" in observed.keys():
        if not observed["id"] == expected_get_series_id:
            assert returned_correctly == True
    if "title" in observed.keys():
        if not observed["title"] == expected_get_series_title: 
            assert returned_correctly == True
    returned_correctly = True
    assert returned_correctly == True

@pytest.fixture
def expected_names_get_categories_of_series():
    # fred/series/categories
    return ("Japan", "Monthly Rates",)

@pytest.mark.skip("passed v1")
def test_get_categories_of_series(
        fred: Fred,
        expected_names_get_categories_of_series: tuple,
        ):
    # fred/series/categories
    returned_correctly = False
    observed = fred.get_categories_of_series("EXJPUS")
    if not isinstance(observed, dict):
        assert returned_correctly == True
    if not "categories" in observed.keys():
        assert returned_correctly == True
    categories = observed["categories"] # categories is a list
    expected_keys = ("id", "name", "parent_id")
    for key in categories[0].keys():
        if key not in expected_keys:
            assert returned_correctly == True
    expected_names = expected_names_get_categories_of_series
    for a_category in categories:
        if expected_names[0] in a_category.values():
            returned_correctly = True
        if expected_names[1] in a_category.values():
            returned_correctly = True
    assert returned_correctly == True

@pytest.fixture
def get_release_for_a_series_method_works() -> bool:
    # fred/series/release
    params = {
            'series_id': 'IRA',
            }
    observed = Fred().get_release_for_a_series(**params)
    if not isinstance(observed, dict):
        return False
    if not "releases" in observed.keys():
        return False
    return True

@pytest.mark.skip("passed v1")
def test_get_release_for_a_series(
        get_release_for_a_series_method_works: bool,
        ):
    # fred/series/release
    assert get_release_for_a_series_method_works == True

@pytest.fixture
def search_for_a_series_method_works() -> bool:
    # fred/series/search
    params = {
            'search_text': ('monetary', 'service', 'index',),
            'limit': 3,
            }
    observed = Fred().search_for_a_series(**params)
    if not isinstance(observed, dict):
        return False
    if not "limit" in observed.keys():
        return False
    if not "series" in observed.keys():
        if not "seriess" in observed.keys():
            return False
    # for v2 can look at each title to see if search text words are
    # present
    return True

@pytest.mark.skip("passed v1")
def test_search_for_a_series(
        search_for_a_series_method_works: bool,
        ):
    # fred/series/search
    assert search_for_a_series_method_works == True





@pytest.fixture
def get_tags_for_a_series_search_method_works() -> bool:
    # fred/series/search/tags
    params = {
            'series_search_text': ('monetary', 'service', 'index',),
            'limit': 3,
            }
    observed = Fred().get_tags_for_a_series_search(**params)
    if not isinstance(observed, dict):
        return False
    if not "tags" in observed.keys():
        return False
    return True

@pytest.mark.skip("passed v1")
def test_get_tags_for_a_series_search(
        get_tags_for_a_series_search_method_works: bool,
        ):
    # fred/series/search/tags
    assert get_tags_for_a_series_search_method_works == True

@pytest.fixture
def get_related_tags_for_a_series_search_method_works() -> bool:
    # fred/series/search/related_tags
    params = {
            'series_search_text': ('mortgage', 'rate', 'index',),
            'tag_names': ('30-year', 'frb',),
            'limit': 3,
            }
    observed = Fred().get_related_tags_for_a_series_search(**params)
#    breakpoint()
    if not isinstance(observed, dict):
        return False
    if not "limit" in observed.keys():
        return False
    if params["limit"] != observed["limit"]:
        return False
    if not "tags" in observed.keys():
        return False
    return True

@pytest.mark.skip("passed v1")
def test_get_related_tags_for_a_series_search(
        get_related_tags_for_a_series_search_method_works: bool,
        ):
    # fred/series/search/related_tags
    assert get_related_tags_for_a_series_search_method_works == True

@pytest.fixture
def get_tags_for_a_series_method_works() -> bool:
    # fred/series/tags
    params = {
            'series_id': 'STLFSI',
            }
    observed = Fred().get_tags_for_a_series(**params)
    if not isinstance(observed, dict):
        return False
    if not "tags" in observed.keys():
        return False
    return True

@pytest.mark.skip("passed v1")
def test_get_tags_for_a_series(
        get_tags_for_a_series_method_works: bool,
        ):
    # fred/series/tags
    assert get_tags_for_a_series_method_works == True

@pytest.fixture
def get_series_vintage_dates_method_works() -> bool:
    # fred/series/vintagedates
    params = {
            'series_id': 'GNPCA',
            'limit': 3,
            }
    observed = Fred().get_series_vintage_dates(**params)
    if not isinstance(observed, dict):
        return False
    if not "limit" in observed.keys():
        return False
    if observed["limit"] != params["limit"]:
        return False
    if not "vintage_dates" in observed.keys():
        return False
    return True

@pytest.mark.skip("passed v1")
def test_get_series_vintage_dates(
        get_series_vintage_dates_method_works: bool,
        ):
    # fred/series/vintagedates
    assert get_series_vintage_dates_method_works == True
