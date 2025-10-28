import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import (
    RESULTS_DIR,
)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] += 1
        if 'name' in item:
            item['name'] = f" {item['name']}"
        if 'status' in item:
            item['status'] = f" {item['status']}"
        return item

    def close_spider(self, spider):
        time_format = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = self.results_dir / f'status_summary_{time_format}.csv'
        with open(file_path, 'w', encoding='utf-8') as f:
            status_summary = (
                ('Status', 'Count'),
                *self.status_count.items(),
                ('Total', sum(self.status_count.values()))
            )
            # status_summary = [('Status', 'Count')]
            # status_summary.extend(self.status_count.items())
            # status_summary.append(('Total', sum(self.status_count.values())))
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(status_summary)
