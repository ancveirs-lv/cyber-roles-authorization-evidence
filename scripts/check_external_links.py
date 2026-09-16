#!/usr/bin/env python3
"""Check source-registry URLs without making transient blocking a PR gate."""

from __future__ import annotations

import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml


ROOT = Path(__file__).resolve().parents[1]
PERMANENT_FAILURES = {404, 410}
INCONCLUSIVE = {401, 403, 405, 408, 425, 429}


def check(url: str, attempts: int = 2) -> tuple[str, str]:
    request = Request(
        url,
        headers={"User-Agent": "cyber-roles-source-health/0.2 (+GitHub Actions)"},
        method="GET",
    )
    for attempt in range(attempts):
        try:
            with urlopen(request, timeout=12) as response:
                status = response.status
                if 200 <= status < 400:
                    return "ok", str(status)
                if status in PERMANENT_FAILURES:
                    return "failed", str(status)
                return "warning", str(status)
        except HTTPError as error:
            if error.code in PERMANENT_FAILURES:
                return "failed", str(error.code)
            if error.code in INCONCLUSIVE or error.code >= 500:
                result = ("warning", str(error.code))
            else:
                result = ("failed", str(error.code))
        except (URLError, TimeoutError) as error:
            result = ("warning", error.__class__.__name__)
        if attempt + 1 < attempts:
            time.sleep(1)
    return result


def main() -> int:
    sources = yaml.safe_load((ROOT / "data/sources.yaml").read_text(encoding="utf-8"))[
        "sources"
    ]
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(lambda source: check(source["url"]), sources))

    failures = 0
    for source, (state, detail) in zip(sources, results, strict=True):
        print(f"{state.upper():7} {detail:12} {source['id']}: {source['url']}")
        failures += state == "failed"
    if failures:
        print(f"Permanent link failures: {failures}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
