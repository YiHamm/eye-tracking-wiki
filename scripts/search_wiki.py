"""Eye Tracking Wiki: search the five ingested source records (stdlib only)."""
import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / 'sources.json'


def load_sources():
    with DATA_FILE.open(encoding='utf-8') as f:
        sources = json.load(f)
    if not isinstance(sources, list):
        raise ValueError('sources.json 必須是文獻清單（JSON array）')
    return sources


def search(sources, keyword):
    keyword = keyword.strip().casefold()
    if not keyword:
        return []
    return [s for s in sources if any(keyword in str(s.get(field, '')).casefold()
            for field in ('id', 'title', 'authors', 'year', 'venue', 'topic', 'summary', 'claim'))]


def show_results(results):
    print(f'找到 {len(results)} 篇相關文獻')
    for s in results:
        print(f"\n[{s.get('id', '?')}] {s.get('title', '未命名')} ({s.get('year', '?')})")
        print('主題：', s.get('topic', ''))
        print('摘要：', s.get('summary', ''))
        print('重點：', s.get('claim', ''))
        print('來源：', s.get('url', ''))
        print('核對狀態：', s.get('status', '未標記'))


def main():
    parser = argparse.ArgumentParser(description='查詢 Eye Tracking Wiki 文獻資料')
    parser.add_argument('--query', '-q', help='單次查詢關鍵字；省略時進入互動模式')
    args = parser.parse_args()
    sources = load_sources()
    print(f'===== Eye Tracking Wiki：已載入 {len(sources)} 篇文獻 =====')
    if args.query is not None:
        show_results(search(sources, args.query))
        return
    while True:
        try:
            keyword = input('\n請輸入關鍵字（exit 結束）：').strip()
        except (EOFError, KeyboardInterrupt):
            print('\n結束查詢')
            break
        if keyword.lower() == 'exit':
            break
        show_results(search(sources, keyword))


if __name__ == '__main__':
    main()
