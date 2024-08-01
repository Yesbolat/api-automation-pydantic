from http import HTTPStatus
from typing import List

from utils.assertions.base.expect import expect


def assert_status_code(actual: int, expected: HTTPStatus) -> None:
    expect(expected) \
        .set_description('Response status code') \
        .to_be_equal(actual)


def assert_sorted_by_field(items: List[dict], field, reverse):
    if len(items) < 2:
        return
    sorted_items = sorted(items, key=lambda x: x[field], reverse=reverse)
    description = f"Checking that the list is sorted correctly by field '{field}'"
    expect(sorted_items).set_description(description).to_be_equal(items, isDetailed=False)
