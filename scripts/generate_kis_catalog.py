import json
import re

with open('/Users/jodongik/workspace/trade-pluse/docs/profiles/kis_apis_extracted.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def clean_title(t):
    if not t:
        return ''
    t = re.sub(r'\[v\d+_[^\]]+\]', '', t)
    t = re.sub(r'\[국내주식-[^\]]+\]', '', t)
    t = re.sub(r'\[해외주식-[^\]]+\]', '', t)
    t = re.sub(r'\[실시간-[^\]]+\]', '', t)
    t = re.sub(r'\[국내선물옵션-[^\]]+\]', '', t)
    t = re.sub(r'\[해외선물옵션-[^\]]+\]', '', t)
    t = re.sub(r'\[장내채권-[^\]]+\]', '', t)
    t = re.sub(r'\[ELW-[^\]]+\]', '', t)
    t = re.sub(r'\[ETF/ETN-[^\]]+\]', '', t)
    t = re.sub(r'#', '', t)
    return t.strip()

cat_names = {
    'auth': '1. 인증 (OAuth / WebSocket Key)',
    'domestic_stock': '2. 국내주식 (Domestic Stock)',
    'overseas_stock': '3. 해외주식 (Overseas Stock)',
    'domestic_futureoption': '4. 국내선물옵션 (Domestic Futures & Options)',
    'overseas_futureoption': '5. 해외선물옵션 (Overseas Futures & Options)',
    'domestic_bond': '6. 국내채권 (Domestic Bond)',
    'etfetn': '7. ETF / ETN',
    'elw': '8. ELW (주식워런트증권)'
}

grouped = {}
for itm in items:
    cat = itm['category']
    grouped.setdefault(cat, []).append(itm)

md_lines = []
md_lines.append('# 한국투자증권 (KIS) Open API 전체 카탈로그 (docs/profiles/kis-api-catalog.md)\n')
md_lines.append('> ℹ️ **안내**: 한국투자증권 공식 샘플 코드 저장소([koreainvestment/open-trading-api](https://github.com/koreainvestment/open-trading-api))를 전수 분석하여 정제한 **333개 API 인벤토리**입니다. 각 기능별 REST 엔드포인트, 실시간 웹소켓 TR ID 및 공식 파이썬 샘플 함수명이 매핑되어 있습니다.\n')

# Table of contents
md_lines.append('## 📋 카테고리 요약\n')
md_lines.append('| 카테고리 | REST API | WebSocket | 합계 |')
md_lines.append('| :--- | :---: | :---: | :---: |')
order_cats = ['auth', 'domestic_stock', 'overseas_stock', 'domestic_futureoption', 'overseas_futureoption', 'domestic_bond', 'etfetn', 'elw']
for c in order_cats:
    itms = grouped.get(c, [])
    r_cnt = sum(1 for x in itms if x.get('type') == 'REST')
    w_cnt = sum(1 for x in itms if x.get('type') == 'WebSocket')
    md_lines.append(f'| {cat_names[c]} | {r_cnt} | {w_cnt} | {len(itms)} |')
md_lines.append(f'| **합계** | **273** | **60** | **333** |\n')
md_lines.append('---\n')

for c in order_cats:
    itms = grouped.get(c, [])
    itms.sort(key=lambda x: (0 if x.get('type') == 'REST' else 1, x['func']))
    md_lines.append(f'## {cat_names[c]}\n')
    md_lines.append('| 함수명 (`examples_llm`) | 구분 | 한글 기능명 | 엔드포인트 / 실시간 TR ID | TR ID |')
    md_lines.append('| :--- | :---: | :--- | :--- | :--- |')
    for itm in itms:
        f_name = f"`{itm['func']}`"
        proto = f"`{itm.get('type', 'REST')}`"
        title = clean_title(itm.get('title', ''))
        ep = f"`{itm['api_url']}`" if itm.get('api_url') else '-'
        trs = ', '.join([f"`{t}`" for t in itm.get('tr_ids', [])]) if itm.get('tr_ids') else '-'
        md_lines.append(f'| {f_name} | {proto} | {title} | {ep} | {trs} |')
    md_lines.append('\n---\n')

with open('/Users/jodongik/workspace/trade-pluse/docs/profiles/kis-api-catalog.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print('Successfully generated docs/profiles/kis-api-catalog.md!')
