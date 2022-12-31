import os
from typing import List

from pydantic import BaseSettings

from .utils import queuerunner


class Settings(queuerunner.Settings):

    project_name: str = "FediMapper"

    database_url: str = "sqlite:///./test.db"
    debug: bool = False
    sql_debug: bool = False

    stop_words_directory: str = "./data/stop-words"
    crawler_user_agent = "fedimapper"

    evil_domains: List[str] = ["activitypub-troll.cf", "gab.best"]
    bootstrap_instances: List = [
        # "Official" instance of the org that manages Mastodon.
        "mastodon.social",
    ]

    api_cache_ttl: int = 120
    api_cache_while_revalidate_ttl: int = 3600
    api_cache_while_error_ttl: int = 3600

    stale_rescan_hours: float = 0.90
    unreachable_rescan_hours: float = 6

    spam_domain_threshold: int = 100
    top_lists_min_threshold: int = 5


settings = Settings()

UNREADABLE_STATUSES = ["unreachable", "unknown_service", "no_dns", "disabled"]
