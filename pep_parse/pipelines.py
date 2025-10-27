# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import (
    BASE_DIR,
    RESULTS_DIR,
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)
        self.results_dir = RESULTS_DIR

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] += 1
        return item

    def close_spider(self, spider):
        time_format = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = self.results_dir / f'status_summary_{time_format}.csv'
        with open(file_path, 'w', encoding='utf-8') as f:
            status_summary = [('Status', 'Count')]
            status_summary.extend(self.status_count.items())
            status_summary.append(('Total', sum(self.status_count.values())))
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(status_summary)

        with open(file_root, 'w', encoding='utf-8') as f:
            status_summary = [('Status', 'Count')]
            status_summary.extend(self.status_count.items())
            status_summary.append(('Total', sum(self.status_count.values())))
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(status_summary)
