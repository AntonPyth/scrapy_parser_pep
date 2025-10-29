from pathlib import Path
import sys
import asyncio


if sys.platform == "win32":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except AttributeError:
        pass


BOT_NAME = 'pep_parse'
SPIDERS_MODULE_PATH = f'{BOT_NAME}.spiders'

SPIDER_MODULES = [SPIDERS_MODULE_PATH]
NEWSPIDER_MODULE = SPIDERS_MODULE_PATH

ALLOWED_DOMAINS = ['peps.python.org']
SPIDER_NAME = 'pep'
START_URLS = [f'https://{domain}/' for domain in ALLOWED_DOMAINS]
ROBOTSTXT_OBEY = True


REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR_NAME = 'results'
RESULTS_DIR = BASE_DIR / RESULTS_DIR_NAME

FEEDS = {
    f'{RESULTS_DIR_NAME}/pep_%(time)s.csv':
    {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}
