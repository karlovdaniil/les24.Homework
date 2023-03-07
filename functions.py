from typing import Any, Iterable, List, Iterator
import re


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> set[str]:
    return set(data)


def limit_query(value: str, data: Iterable[str]) -> List[str]:
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]) -> Iterator[str]:
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> List[str]:
    revers: bool = value == 'desc'
    return sorted(data, reverse=revers)


def regex_query(value: str, data: Iterable[str]) -> Iterator[str]:
    regex: re.Pattern = re.compile(value)
    return filter(lambda x: re.search(regex, x), data)
