# 한국투자증권 (KIS) Open API 전체 카탈로그 (docs/profiles/kis-api-catalog.md)

> ℹ️ **안내**: 한국투자증권 공식 샘플 코드 저장소([koreainvestment/open-trading-api](https://github.com/koreainvestment/open-trading-api))를 전수 분석하여 정제한 **333개 API 인벤토리**입니다. 각 기능별 REST 엔드포인트, 실시간 웹소켓 TR ID 및 공식 파이썬 샘플 함수명이 매핑되어 있습니다.

## 📋 카테고리 요약

| 카테고리 | REST API | WebSocket | 합계 |
| :--- | :---: | :---: | :---: |
| 1. 인증 (OAuth / WebSocket Key) | 2 | 0 | 2 |
| 2. 국내주식 (Domestic Stock) | 130 | 25 | 155 |
| 3. 해외주식 (Overseas Stock) | 46 | 4 | 50 |
| 4. 국내선물옵션 (Domestic Futures & Options) | 23 | 20 | 43 |
| 5. 해외선물옵션 (Overseas Futures & Options) | 31 | 4 | 35 |
| 6. 국내채권 (Domestic Bond) | 15 | 3 | 18 |
| 7. ETF / ETN | 5 | 1 | 6 |
| 8. ELW (주식워런트증권) | 21 | 3 | 24 |
| **합계** | **273** | **60** | **333** |

---

## 1. 인증 (OAuth / WebSocket Key)

| 함수명 (`examples_llm`) | 구분 | 한글 기능명 | 엔드포인트 / 실시간 TR ID | TR ID |
| :--- | :---: | :--- | :--- | :--- |
| `auth_token` | `REST` | [인증] OAuth 접근토큰 발급 | `/oauth2/tokenP` | - |
| `auth_ws_token` | `REST` | [인증] WebSocket 웹소켓 접속키 발급 | `/oauth2/Approval` | - |

---

## 2. 국내주식 (Domestic Stock)

| 함수명 (`examples_llm`) | 구분 | 한글 기능명 | 엔드포인트 / 실시간 TR ID | TR ID |
| :--- | :---: | :--- | :--- | :--- |
| `after_hour_balance` | `REST` | [국내주식] 기본시세 > 국내주식 시간외잔량 순위 | `/uapi/domestic-stock/v1/ranking/after-hour-balance` | `FHPST01760000` |
| `bulk_trans_num` | `REST` | [국내주식] 순위분석 > 국내주식 대량체결건수 상위 | `/uapi/domestic-stock/v1/ranking/bulk-trans-num` | `FHKST190900C0` |
| `capture_uplowprice` | `REST` | [국내주식] 시세분석 > 국내주식 상하한가 포착 | `/uapi/domestic-stock/v1/quotations/capture-uplowprice` | `FHKST130000C0` |
| `comp_interest` | `REST` | [국내주식] 업종/기타 > 금리 종합(국내채권_금리) | `/uapi/domestic-stock/v1/quotations/comp-interest` | `FHPST07020000` |
| `comp_program_trade_daily` | `REST` | [국내주식] 시세분석 > 프로그램매매 종합현황(일별) | `/uapi/domestic-stock/v1/quotations/comp-program-trade-daily` | `FHPPG04600001` |
| `comp_program_trade_today` | `REST` | [국내주식] 시세분석 > 프로그램매매 종합현황(시간) | `/uapi/domestic-stock/v1/quotations/comp-program-trade-today` | `FHPPG04600101` |
| `credit_balance` | `REST` | [국내주식] 순위분석 > 국내주식 신용잔고 상위 | `/uapi/domestic-stock/v1/ranking/credit-balance` | `FHKST17010000` |
| `credit_by_company` | `REST` | [국내주식] 종목정보 > 국내주식 당사 신용가능종목 | `/uapi/domestic-stock/v1/quotations/credit-by-company` | `FHPST04770000` |
| `daily_credit_balance` | `REST` | [국내주식] 시세분석 > 국내주식 신용잔고 일별추이 | `/uapi/domestic-stock/v1/quotations/daily-credit-balance` | `FHPST04760000` |
| `daily_loan_trans` | `REST` | [국내주식] 시세분석 > 종목별 일별 대차거래추이 | `/uapi/domestic-stock/v1/quotations/daily-loan-trans` | `HHPST074500C0` |
| `daily_short_sale` | `REST` | [국내주식] 시세분석 > 국내주식 공매도 일별추이 | `/uapi/domestic-stock/v1/quotations/daily-short-sale` | `FHPST04830000` |
| `disparity` | `REST` | [국내주식] 순위분석 > 국내주식 이격도 순위 | `/uapi/domestic-stock/v1/ranking/disparity` | `FHPST01780000` |
| `dividend_rate` | `REST` | [국내주식] 순위분석 > 국내주식 배당률 상위 | `/uapi/domestic-stock/v1/ranking/dividend-rate` | `HHKDB13470100` |
| `estimate_perform` | `REST` | [국내주식] 종목정보 > 국내주식 종목추정실적 | `/uapi/domestic-stock/v1/quotations/estimate-perform` | `HHKST668300C0` |
| `exp_closing_price` | `REST` | [국내주식] 기본시세 > 국내주식 장마감 예상체결가 | `/uapi/domestic-stock/v1/quotations/exp-closing-price` | `FHKST117300C0` |
| `exp_index_trend` | `REST` | [국내주식] 업종/기타 > 국내주식 예상체결지수 추이 | `/uapi/domestic-stock/v1/quotations/exp-index-trend` | `FHPST01840000` |
| `exp_price_trend` | `REST` | [국내주식] 시세분석 > 국내주식 예상체결가 추이 | `/uapi/domestic-stock/v1/quotations/exp-price-trend` | `FHPST01810000` |
| `exp_total_index` | `REST` | [국내주식] 업종/기타 > 국내주식 예상체결 전체지수 | `/uapi/domestic-stock/v1/quotations/exp-total-index` | `FHKUP11750000` |
| `exp_trans_updown` | `REST` | [국내주식] 순위분석 > 국내주식 예상체결 상승_하락상위 | `/uapi/domestic-stock/v1/ranking/exp-trans-updown` | `FHPST01820000` |
| `finance_balance_sheet` | `REST` | [국내주식] 종목정보 > 국내주식 대차대조표 | `/uapi/domestic-stock/v1/finance/balance-sheet` | `FHKST66430100` |
| `finance_financial_ratio` | `REST` | [국내주식] 종목정보 > 국내주식 재무비율 | `/uapi/domestic-stock/v1/finance/financial-ratio` | `FHKST66430300` |
| `finance_growth_ratio` | `REST` | [국내주식] 종목정보 > 국내주식 성장성비율 | `/uapi/domestic-stock/v1/finance/growth-ratio` | `FHKST66430800` |
| `finance_income_statement` | `REST` | [국내주식] 종목정보 > 국내주식 손익계산서 | `/uapi/domestic-stock/v1/finance/income-statement` | `FHKST66430200` |
| `finance_other_major_ratios` | `REST` | [국내주식] 종목정보 > 국내주식 기타주요비율 | `/uapi/domestic-stock/v1/finance/other-major-ratios` | `FHKST66430500` |
| `finance_profit_ratio` | `REST` | [국내주식] 종목정보 - 국내주식 수익성비율 | `/uapi/domestic-stock/v1/finance/profit-ratio` | `FHKST66430400` |
| `finance_ratio` | `REST` | [국내주식] 순위분석 > 국내주식 재무비율 순위 | `/uapi/domestic-stock/v1/ranking/finance-ratio` | `FHPST01750000` |
| `finance_stability_ratio` | `REST` | [국내주식] 종목정보 > 국내주식 안정성비율 | `/uapi/domestic-stock/v1/finance/stability-ratio` | `FHKST66430600` |
| `fluctuation` | `REST` | [국내주식] 순위분석 > 등락률 순위 | `/uapi/domestic-stock/v1/ranking/fluctuation` | `FHPST01700000` |
| `foreign_institution_total` | `REST` | [국내주식] 시세분석 > 국내기관_외국인 매매종목가집계 | `/uapi/domestic-stock/v1/quotations/foreign-institution-total` | `FHPTJ04400000` |
| `frgnmem_pchs_trend` | `REST` | [국내주식] 시세분석 > 종목별 외국계 순매수추이 | `/uapi/domestic-stock/v1/quotations/frgnmem-pchs-trend` | `FHKST644400C0` |
| `frgnmem_trade_estimate` | `REST` | [국내주식] 시세분석 > 외국계 매매종목 가집계 | `/uapi/domestic-stock/v1/quotations/frgnmem-trade-estimate` | `FHKST644100C0` |
| `frgnmem_trade_trend` | `REST` | [국내주식] 기본시세 > 회원사 실 시간 매매동향(틱) | `/uapi/domestic-stock/v1/quotations/frgnmem-trade-trend` | `FHPST04320000` |
| `hts_top_view` | `REST` | [국내주식] 순위분석 > HTS조회상위20종목 | `/uapi/domestic-stock/v1/ranking/hts-top-view` | `HHMCM000100C0` |
| `inquire_account_balance` | `REST` | [국내주식] 주문/계좌 > 투자계좌자산현황조회 | `/uapi/domestic-stock/v1/trading/inquire-account-balance` | `CTRP6548R` |
| `inquire_asking_price_exp_ccn` | `REST` | [국내주식] 기본시세 > 주식현재가 호가/예상체결 | `/uapi/domestic-stock/v1/quotations/inquire-asking-price-exp-ccn` | `FHKST01010200` |
| `inquire_balance` | `REST` | [국내주식] 주문/계좌 > 주식잔고조회 | `/uapi/domestic-stock/v1/trading/inquire-balance` | `TTTC8434R`, `VTTC8434R` |
| `inquire_balance_rlz_pl` | `REST` | [국내주식] 주문/계좌 > 주식잔고조회_실현손익 | `/uapi/domestic-stock/v1/trading/inquire-balance-rlz-pl` | `TTTC8494R` |
| `inquire_ccnl` | `REST` | [국내주식] 기본시세 > 주식현재가 체결 | `/uapi/domestic-stock/v1/quotations/inquire-ccnl` | `FHKST01010300` |
| `inquire_credit_psamount` | `REST` | [국내주식] 주문/계좌 > 신용매수가능조회 | `/uapi/domestic-stock/v1/trading/inquire-credit-psamount` | `TTTC8909R` |
| `inquire_daily_ccld` | `REST` | [국내주식] 주문/계좌 > 주식일별주문체결조회 | `/uapi/domestic-stock/v1/trading/inquire-daily-ccld` | `CTSC9215R`, `TTTC0081R`, `VTSC9215R`, `VTTC0081R` |
| `inquire_daily_indexchartprice` | `REST` | [국내주식] 업종/기타 - 국내주식업종기간별시세(일/주/월/년) | `/uapi/domestic-stock/v1/quotations/inquire-daily-indexchartprice` | `FHKUP03500100` |
| `inquire_daily_itemchartprice` | `REST` | [국내주식] 기본시세 > 국내주식기간별시세(일/주/월/년) | `/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice` | `FHKST03010100` |
| `inquire_daily_overtimeprice` | `REST` | [국내주식] 기본시세 > 주식현재가 시간외일자별주가 | `/uapi/domestic-stock/v1/quotations/inquire-daily-overtimeprice` | `FHPST02320000` |
| `inquire_daily_price` | `REST` | [국내주식] 기본시세 > 주식현재가 일자별 | `/uapi/domestic-stock/v1/quotations/inquire-daily-price` | `FHKST01010400` |
| `inquire_daily_trade_volume` | `REST` | [국내주식] 시세분석 > 종목별일별매수매도체결량 | `/uapi/domestic-stock/v1/quotations/inquire-daily-trade-volume` | `FHKST03010800` |
| `inquire_elw_price` | `REST` | [국내주식] ELW시세 > ELW 현재가 시세 | `/uapi/domestic-stock/v1/quotations/inquire-elw-price` | `FHKEW15010000` |
| `inquire_index_category_price` | `REST` | [국내주식] 업종/기타 > 국내업종 구분별전체시세 | `/uapi/domestic-stock/v1/quotations/inquire-index-category-price` | `FHPUP02140000` |
| `inquire_index_daily_price` | `REST` | [국내주식] 업종/기타 > 국내업종 일자별지수 | `/uapi/domestic-stock/v1/quotations/inquire-index-daily-price` | `FHPUP02120000` |
| `inquire_index_price` | `REST` | [국내주식] 업종/기타 > 국내업종 현재지수 | `/uapi/domestic-stock/v1/quotations/inquire-index-price` | `FHPUP02100000` |
| `inquire_index_tickprice` | `REST` | [국내주식] 업종/기타 > 국내업종 시간별지수(초) | `/uapi/domestic-stock/v1/quotations/inquire-index-tickprice` | `FHPUP02110100` |
| `inquire_index_timeprice` | `REST` | [국내주식] 업종/기타 > 국내업종 시간별지수(분) | `/uapi/domestic-stock/v1/quotations/inquire-index-timeprice` | `FHPUP02110200` |
| `inquire_investor` | `REST` | [국내주식] 기본시세 > 주식현재가 투자자 | `/uapi/domestic-stock/v1/quotations/inquire-investor` | `FHKST01010900` |
| `inquire_investor_daily_by_market` | `REST` | [국내주식] 시세분석 > 시장별 투자자매매동향(일별) | `/uapi/domestic-stock/v1/quotations/inquire-investor-daily-by-market` | `FHPTJ04040000` |
| `inquire_investor_time_by_market` | `REST` | [국내주식] 시세분석 > 시장별 투자자매매동향(시세) | `/uapi/domestic-stock/v1/quotations/inquire-investor-time-by-market` | `FHPTJ04030000` |
| `inquire_member` | `REST` | [국내주식] 기본시세 > 주식현재가 회원사 | `/uapi/domestic-stock/v1/quotations/inquire-member` | `FHKST01010600` |
| `inquire_member_daily` | `REST` | [국내주식] 시세분석 > 주식현재가 회원사 종목매매동향 | `/uapi/domestic-stock/v1/quotations/inquire-member-daily` | `FHPST04540000` |
| `inquire_overtime_asking_price` | `REST` | [국내주식] 기본시세 > 국내주식 시간외호가 | `/uapi/domestic-stock/v1/quotations/inquire-overtime-asking-price` | `FHPST02300400` |
| `inquire_overtime_price` | `REST` | [국내주식] 기본시세 > 국내주식 시간외현재가 | `/uapi/domestic-stock/v1/quotations/inquire-overtime-price` | `FHPST02300000` |
| `inquire_period_profit` | `REST` | [국내주식] 주문/계좌 > 기간별손익일별합산조회 | `/uapi/domestic-stock/v1/trading/inquire-period-profit` | `TTTC8708R` |
| `inquire_period_trade_profit` | `REST` | [국내주식] 주문/계좌 > 기간별매매손익현황조회 | `/uapi/domestic-stock/v1/trading/inquire-period-trade-profit` | `TTTC8715R` |
| `inquire_price` | `REST` | [국내주식] 기본시세 > 주식현재가 시세 | `/uapi/domestic-stock/v1/quotations/inquire-price` | `FHKST01010100` |
| `inquire_price_2` | `REST` | [국내주식] 기본시세 > 주식현재가 시세2 | `/uapi/domestic-stock/v1/quotations/inquire-price-2` | `FHPST01010000` |
| `inquire_psbl_order` | `REST` | [국내주식] 주문/계좌 > 매수가능조회 | `/uapi/domestic-stock/v1/trading/inquire-psbl-order` | `TTTC8908R`, `VTTC8908R` |
| `inquire_psbl_rvsecncl` | `REST` | [국내주식] 주문/계좌 > 주식정정취소가능주문조회 | `/uapi/domestic-stock/v1/trading/inquire-psbl-rvsecncl` | `TTTC0084R` |
| `inquire_psbl_sell` | `REST` | [국내주식] 주문/계좌 - 매도가능수량조회 | `/uapi/domestic-stock/v1/trading/inquire-psbl-sell` | `TTTC8408R` |
| `inquire_time_dailychartprice` | `REST` | [국내주식] 기본시세 > 주식일별분봉조회 | `/uapi/domestic-stock/v1/quotations/inquire-time-dailychartprice` | `FHKST03010230` |
| `inquire_time_indexchartprice` | `REST` | [국내주식] 업종/기타 - 업종 분봉조회 | `/uapi/domestic-stock/v1/quotations/inquire-time-indexchartprice` | `FHKUP03500200` |
| `inquire_time_itemchartprice` | `REST` | [국내주식] 기본시세 > 주식당일분봉조회 | `/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice` | `FHKST03010200` |
| `inquire_time_itemconclusion` | `REST` | [국내주식] 기본시세 > 주식현재가 당일시간대별체결 | `/uapi/domestic-stock/v1/quotations/inquire-time-itemconclusion` | `FHPST01060000` |
| `inquire_time_overtimeconclusion` | `REST` | [국내주식] 기본시세 > 주식현재가 시간외시간별체결 | `/uapi/domestic-stock/v1/quotations/inquire-time-overtimeconclusion` | `FHPST02310000` |
| `inquire_vi_status` | `REST` | [국내주식] 기본시세 > 변동성완화장치(VI) 현황 | `/uapi/domestic-stock/v1/quotations/inquire-vi-status` | `FHPST01390000` |
| `intgr_margin` | `REST` | [국내주식] 주문/계좌 > 주식통합증거금 현황 | `/uapi/domestic-stock/v1/trading/intgr-margin` | `TTTC0869R` |
| `intstock_grouplist` | `REST` | [국내주식] 시세분석 > 관심종목 그룹조회 | `/uapi/domestic-stock/v1/quotations/intstock-grouplist` | `HHKCM113004C7` |
| `intstock_multprice` | `REST` | [국내주식] 시세분석 > 관심종목(멀티종목) 시세조회 | `/uapi/domestic-stock/v1/quotations/intstock-multprice` | `FHKST11300006` |
| `intstock_stocklist_by_group` | `REST` | [국내주식] 시세분석 > 관심종목 그룹별 종목조회 | `/uapi/domestic-stock/v1/quotations/intstock-stocklist-by-group` | `HHKCM113004C6` |
| `invest_opbysec` | `REST` | [국내주식] 종목정보 - 국내주식 증권사별 투자의견 | `/uapi/domestic-stock/v1/quotations/invest-opbysec` | `FHKST663400C0` |
| `invest_opinion` | `REST` | [국내주식] 종목정보 - 국내주식 종목투자의견 | `/uapi/domestic-stock/v1/quotations/invest-opinion` | `FHKST663300C0` |
| `investor_program_trade_today` | `REST` | [국내주식] 시세분석 > 프로그램매매 투자자매매동향(당일) | `/uapi/domestic-stock/v1/quotations/investor-program-trade-today` | `HHPPG046600C1` |
| `investor_trade_by_stock_daily` | `REST` | [국내주식] 시세분석  > 종목별 투자자매매동향(일별)[종목별 투자자매매동향(일별)] | `/uapi/domestic-stock/v1/quotations/investor-trade-by-stock-daily` | `FHPTJ04160001` |
| `investor_trend_estimate` | `REST` | [국내주식] 시세분석 > 종목별 외인기관 추정가집계 | `/uapi/domestic-stock/v1/quotations/investor-trend-estimate` | `HHPTJ04160200` |
| `ksdinfo_bonus_issue` | `REST` | [국내주식] 종목정보 - 예탁원정보(무상증자일정) | `/uapi/domestic-stock/v1/ksdinfo/bonus-issue` | `HHKDB669101C0` |
| `ksdinfo_cap_dcrs` | `REST` | [국내주식] 종목정보 > 예탁원정보(자본감소일정) | `/uapi/domestic-stock/v1/ksdinfo/cap-dcrs` | `HHKDB669106C0` |
| `ksdinfo_dividend` | `REST` | [국내주식] 종목정보 - 예탁원정보(배당일정) | `/uapi/domestic-stock/v1/ksdinfo/dividend` | `HHKDB669102C0` |
| `ksdinfo_forfeit` | `REST` | [국내주식] 종목정보 > 예탁원정보(실권주일정) | `/uapi/domestic-stock/v1/ksdinfo/forfeit` | `HHKDB669109C0` |
| `ksdinfo_list_info` | `REST` | [국내주식] 종목정보 > 예탁원정보(상장정보일정) | `/uapi/domestic-stock/v1/ksdinfo/list-info` | `HHKDB669107C0` |
| `ksdinfo_mand_deposit` | `REST` | [국내주식] 종목정보 > 예탁원정보(의무예치일정) | `/uapi/domestic-stock/v1/ksdinfo/mand-deposit` | `HHKDB669110C0` |
| `ksdinfo_merger_split` | `REST` | [국내주식] 종목정보 > 예탁원정보(합병_분할일정) | `/uapi/domestic-stock/v1/ksdinfo/merger-split` | `HHKDB669104C0` |
| `ksdinfo_paidin_capin` | `REST` | [국내주식] 종목정보 > 예탁원정보(유상증자일정) | `/uapi/domestic-stock/v1/ksdinfo/paidin-capin` | `HHKDB669100C0` |
| `ksdinfo_pub_offer` | `REST` | [국내주식] 종목정보 - 예탁원정보(공모주청약일정) | `/uapi/domestic-stock/v1/ksdinfo/pub-offer` | `HHKDB669108C0` |
| `ksdinfo_purreq` | `REST` | [국내주식] 종목정보 - 예탁원정보(주식매수청구일정) | `/uapi/domestic-stock/v1/ksdinfo/purreq` | `HHKDB669103C0` |
| `ksdinfo_rev_split` | `REST` | [국내주식] 종목정보 - 예탁원정보(액면교체일정) | `/uapi/domestic-stock/v1/ksdinfo/rev-split` | `HHKDB669105C0` |
| `ksdinfo_sharehld_meet` | `REST` | [국내주식] 종목정보 - 예탁원정보(주주총회일정) | `/uapi/domestic-stock/v1/ksdinfo/sharehld-meet` | `HHKDB669111C0` |
| `lendable_by_company` | `REST` | [국내주식] 종목정보 - 당사 대주가능 종목 | `/uapi/domestic-stock/v1/quotations/lendable-by-company` | `CTSC2702R` |
| `market_cap` | `REST` | [국내주식] 순위분석 > 국내주식 시가총액 상위 | `/uapi/domestic-stock/v1/ranking/market-cap` | `FHPST01740000` |
| `market_time` | `REST` | [국내주식] 업종/기타 > 국내선물 영업일조회 | `/uapi/domestic-stock/v1/quotations/market-time` | `HHMCM000002C0` |
| `market_value` | `REST` | [국내주식] 순위분석 > 국내주식 시장가치 순위 | `/uapi/domestic-stock/v1/ranking/market-value` | `FHPST01790000` |
| `mktfunds` | `REST` | [국내주식] 시세분석 > 국내 증시자금 종합 | `/uapi/domestic-stock/v1/quotations/mktfunds` | `FHKST649100C0` |
| `near_new_highlow` | `REST` | [국내주식] 순위분석 > 국내주식 신고_신저근접종목 상위 | `/uapi/domestic-stock/v1/ranking/near-new-highlow` | `FHPST01870000` |
| `news_title` | `REST` | [국내주식] 업종/기타 - 종합 시황/공시(제목) | `/uapi/domestic-stock/v1/quotations/news-title` | `FHKST01011800` |
| `order_cash` | `REST` | [국내주식] 주문/계좌 > 주식주문(현금) | `/uapi/domestic-stock/v1/trading/order-cash` | `TTTC0011U`, `TTTC0012U`, `VTTC0011U`, `VTTC0012U` |
| `order_credit` | `REST` | [국내주식] 주문/계좌 > 주식주문(신용) | `/uapi/domestic-stock/v1/trading/order-credit` | `TTTC0052U`, `TTTC0051U` |
| `order_resv` | `REST` | [국내주식] 주문/계좌 > 주식예약주문 | `/uapi/domestic-stock/v1/trading/order-resv` | `CTSC0008U` |
| `order_resv_ccnl` | `REST` | [국내주식] 주문/계좌 > 주식예약주문조회 | `/uapi/domestic-stock/v1/trading/order-resv-ccnl` | `CTSC0004R` |
| `order_resv_rvsecncl` | `REST` | [국내주식] 주문/계좌 > 주식예약주문정정취소 | `/uapi/domestic-stock/v1/trading/order-resv-rvsecncl` | `CTSC0009U`, `CTSC0013U` |
| `order_rvsecncl` | `REST` | [국내주식] 주문/계좌 > 주식주문(정정취소) | `/uapi/domestic-stock/v1/trading/order-rvsecncl` | `TTTC0013U`, `VTTC0013U` |
| `overtime_exp_trans_fluct` | `REST` | [국내주식] 시세분석 > 국내주식 시간외예상체결등락률 | `/uapi/domestic-stock/v1/ranking/overtime-exp-trans-fluct` | `FHKST11860000` |
| `overtime_fluctuation` | `REST` | [국내주식] 순위분석 > 국내주식 시간외등락율순위 | `/uapi/domestic-stock/v1/ranking/overtime-fluctuation` | `FHPST02340000` |
| `overtime_volume` | `REST` | [국내주식] 순위분석 - 국내주식 시간외거래량순위 | `/uapi/domestic-stock/v1/ranking/overtime-volume` | `FHPST02350000` |
| `pbar_tratio` | `REST` | [국내주식] 시세분석 > 국내주식 매물대/거래비중 | `/uapi/domestic-stock/v1/quotations/pbar-tratio` | `FHPST01130000` |
| `pension_inquire_balance` | `REST` | [국내주식] 주문/계좌 > 퇴직연금 잔고조회 | `/uapi/domestic-stock/v1/trading/pension/inquire-balance` | `TTTC2208R` |
| `pension_inquire_daily_ccld` | `REST` | [국내주식] 주문/계좌 > 퇴직연금 미체결내역 | `/uapi/domestic-stock/v1/trading/pension/inquire-daily-ccld` | `TTTC2201R` |
| `pension_inquire_deposit` | `REST` | [국내주식] 주문/계좌 > 퇴직연금 예수금조회 | `/uapi/domestic-stock/v1/trading/pension/inquire-deposit` | `TTTC0506R` |
| `pension_inquire_present_balance` | `REST` | [국내주식] 주문/계좌 > 퇴직연금 체결기준잔고 | `/uapi/domestic-stock/v1/trading/pension/inquire-present-balance` | `TTTC2202R` |
| `pension_inquire_psbl_order` | `REST` | [국내주식] 주문/계좌 > 퇴직연금 매수가능조회 | `/uapi/domestic-stock/v1/trading/pension/inquire-psbl-order` | `TTTC0503R` |
| `period_rights` | `REST` | [국내주식] 주문/계좌 > 기간별계좌권리현황조회 | `/uapi/domestic-stock/v1/trading/period-rights` | `CTRGA011R` |
| `prefer_disparate_ratio` | `REST` | [국내주식] 순위분석 > 국내주식 우선주_괴리율 상위 | `/uapi/domestic-stock/v1/ranking/prefer-disparate-ratio` | `FHPST01770000` |
| `profit_asset_index` | `REST` | [국내주식] 순위분석 > 국내주식 수익자산지표 순위 | `/uapi/domestic-stock/v1/ranking/profit-asset-index` | `FHPST01730000` |
| `program_trade_by_stock` | `REST` | [국내주식] 시세분석 > 종목별 프로그램매매추이(체결) | `/uapi/domestic-stock/v1/quotations/program-trade-by-stock` | `FHPPG04650101` |
| `program_trade_by_stock_daily` | `REST` | [국내주식] 시세분석 > 종목별 프로그램매매추이(일별) | `/uapi/domestic-stock/v1/quotations/program-trade-by-stock-daily` | `FHPPG04650201` |
| `psearch_result` | `REST` | [국내주식] 시세분석 > 종목조건검색조회 | `/uapi/domestic-stock/v1/quotations/psearch-result` | `HHKST03900400` |
| `psearch_title` | `REST` | [국내주식] 시세분석 > 종목조건검색 목록조회 | `/uapi/domestic-stock/v1/quotations/psearch-title` | `HHKST03900300` |
| `quote_balance` | `REST` | [국내주식] 기본시세 > 국내주식 호가잔량 순위 | `/uapi/domestic-stock/v1/ranking/quote-balance` | `FHPST01720000` |
| `search_info` | `REST` | [국내주식] 종목정보 - 상품기본조회 | `/uapi/domestic-stock/v1/quotations/search-info` | `CTPF1604R` |
| `search_stock_info` | `REST` | [국내주식] 종목정보 - 주식기본조회 | `/uapi/domestic-stock/v1/quotations/search-stock-info` | `CTPF1002R` |
| `short_sale` | `REST` | [국내주식] 순위분석 > 국내주식 공매도 상위종목 | `/uapi/domestic-stock/v1/ranking/short-sale` | `FHPST04820000` |
| `top_interest_stock` | `REST` | [국내주식] 순위분석 > 국내주식 관심종목등록 상위 | `/uapi/domestic-stock/v1/ranking/top-interest-stock` | `FHPST01800000` |
| `traded_by_company` | `REST` | [국내주식] 순위분석 > 국내주식 당사매매종목 상위 | `/uapi/domestic-stock/v1/ranking/traded-by-company` | `FHPST01860000` |
| `tradprt_byamt` | `REST` | [국내주식] 시세분석 > 국내주식 체결금액별 매매비중 | `/uapi/domestic-stock/v1/quotations/tradprt-byamt` | `FHKST111900C0` |
| `volume_power` | `REST` | [국내주식] 순위분석 > 국내주식 체결강도 상위 | `/uapi/domestic-stock/v1/ranking/volume-power` | `FHPST01680000` |
| `volume_rank` | `REST` | [국내주식] 순위분석 > 거래량순위 | `/uapi/domestic-stock/v1/quotations/volume-rank` | `FHPST01710000` |
| `asking_price_krx` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간호가 (KRX) | - | `H0STASP0` |
| `asking_price_nxt` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간호가 (NXT) | - | `H0NXASP0` |
| `asking_price_total` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간호가 (통합) | - | `H0UNASP0` |
| `ccnl_krx` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간체결가(KRX) | - | `H0STCNT0` |
| `ccnl_notice` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 주식체결통보 | - | `H0STCNI0`, `H0STCNI9` |
| `ccnl_nxt` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간체결가 (NXT) | - | `H0NXCNT0` |
| `ccnl_total` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간체결가 (통합) | - | `H0UNCNT0` |
| `exp_ccnl_krx` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간예상체결 (KRX) | - | `H0STANC0` |
| `exp_ccnl_nxt` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간예상체결 (NXT) | - | `H0NXANC0` |
| `exp_ccnl_total` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간예상체결(통합) | - | `H0UNANC0` |
| `index_ccnl` | `WebSocket` | [국내주식] 실시간시세 > 국내지수 실시간체결 | - | `H0UPCNT0` |
| `index_exp_ccnl` | `WebSocket` | [국내주식] 실시간시세 > 국내지수 실시간예상체결 | - | `H0UPANC0` |
| `index_program_trade` | `WebSocket` | [국내주식] 실시간시세 > 국내지수 실시간프로그램매매 | - | `H0UPPGM0` |
| `market_status_krx` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 장운영정보 (KRX) | - | `H0STMKO0` |
| `market_status_nxt` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 장운영정보(NXT) | - | `H0NXMKO0` |
| `market_status_total` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 장운영정보(통합) | - | `H0UNMKO0` |
| `member_krx` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간회원사 (KRX) | - | `H0STMBC0` |
| `member_nxt` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간회원사 (NXT) | - | `H0NXMBC0` |
| `member_total` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간회원사 (통합) | - | `H0UNMBC0` |
| `overtime_asking_price_krx` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 시간외 실시간호가 (KRX) | - | `H0STOAA0` |
| `overtime_ccnl_krx` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 시간외 실시간체결가 (KRX) | - | `H0STOUP0` |
| `overtime_exp_ccnl_krx` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 시간외 실시간예상체결 (KRX) | - | `H0STOAC0` |
| `program_trade_krx` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간프로그램매매 (KRX) | - | `H0STPGM0` |
| `program_trade_nxt` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간프로그램매매 (NXT) | - | `H0NXPGM0` |
| `program_trade_total` | `WebSocket` | [국내주식] 실시간시세 > 국내주식 실시간프로그램매매 (통합) | - | `H0UNPGM0` |

---

## 3. 해외주식 (Overseas Stock)

| 함수명 (`examples_llm`) | 구분 | 한글 기능명 | 엔드포인트 / 실시간 TR ID | TR ID |
| :--- | :---: | :--- | :--- | :--- |
| `algo_ordno` | `REST` | [해외주식] 주문/계좌 > 해외주식 지정가주문번호조회 | `/uapi/overseas-stock/v1/trading/algo-ordno` | `TTTS6058R` |
| `brknews_title` | `REST` | [해외주식] 시세분석 > 해외속보(제목) | `/uapi/overseas-price/v1/quotations/brknews-title` | `FHKST01011801` |
| `colable_by_company` | `REST` | [해외주식] 시세분석 > 당사 해외주식담보대출 가능 종목 | `/uapi/overseas-price/v1/quotations/colable-by-company` | `CTLN4050R` |
| `countries_holiday` | `REST` | [해외주식] 기본시세 > 해외결제일자조회 | `/uapi/overseas-stock/v1/quotations/countries-holiday` | `CTOS5011R` |
| `dailyprice` | `REST` | [해외주식] 기본시세 > 해외주식 기간별시세 | `/uapi/overseas-price/v1/quotations/dailyprice` | `HHDFS76240000` |
| `daytime_order` | `REST` | [해외주식] 주문/계좌 > 해외주식 미국주간주문 | `/uapi/overseas-stock/v1/trading/daytime-order` | `TTTS6036U`, `TTTS6037U` |
| `daytime_order_rvsecncl` | `REST` | [해외주식] 주문/계좌 > 해외주식 미국주간정정취소 | `/uapi/overseas-stock/v1/trading/daytime-order-rvsecncl` | `TTTS6038U` |
| `foreign_margin` | `REST` | [해외주식] 주문/계좌 - 해외증거금 통화별조회 | `/uapi/overseas-stock/v1/trading/foreign-margin` | `TTTC2101R` |
| `industry_price` | `REST` | [해외주식] 기본시세 > 해외주식 업종별코드조회 | `/uapi/overseas-price/v1/quotations/industry-price` | `HHDFS76370100` |
| `industry_theme` | `REST` | [해외주식] 기본시세 > 해외주식 업종별시세 | `/uapi/overseas-price/v1/quotations/industry-theme` | `HHDFS76370000` |
| `inquire_algo_ccnl` | `REST` | [해외주식] 주문/계좌 > 해외주식 지정가체결내역조회 | `/uapi/overseas-stock/v1/trading/inquire-algo-ccnl` | `TTTS6059R` |
| `inquire_asking_price` | `REST` | [해외주식] 기본시세 > 해외주식 현재가 1호가 | `/uapi/overseas-price/v1/quotations/inquire-asking-price` | `HHDFS76200100` |
| `inquire_balance` | `REST` | [해외주식] 주문/계좌 > 해외주식 잔고 | `/uapi/overseas-stock/v1/trading/inquire-balance` | `TTTS3012R`, `VTTS3012R` |
| `inquire_ccnl` | `REST` | [해외주식] 주문/계좌 > 해외주식 주문체결내역 | `/uapi/overseas-stock/v1/trading/inquire-ccnl` | `TTTS3035R`, `VTTS3035R` |
| `inquire_daily_chartprice` | `REST` | [해외주식] 기본시세 > 해외주식 종목_지수_환율기간별시세(일_주_월_년) | `/uapi/overseas-price/v1/quotations/inquire-daily-chartprice` | `FHKST03030100` |
| `inquire_nccs` | `REST` | [해외주식] 주문/계좌 > 해외주식 미체결내역 | `/uapi/overseas-stock/v1/trading/inquire-nccs` | `TTTS3018R` |
| `inquire_paymt_stdr_balance` | `REST` | [해외주식] 주문/계좌 > 해외주식 결제기준잔고 | `/uapi/overseas-stock/v1/trading/inquire-paymt-stdr-balance` | `CTRP6010R` |
| `inquire_period_profit` | `REST` | [해외주식] 주문/계좌 > 해외주식 기간손익 | `/uapi/overseas-stock/v1/trading/inquire-period-profit` | `TTTS3039R` |
| `inquire_period_trans` | `REST` | [해외주식] 주문/계좌 > 해외주식 일별거래내역 | `/uapi/overseas-stock/v1/trading/inquire-period-trans` | `CTOS4001R` |
| `inquire_present_balance` | `REST` | [해외주식] 주문/계좌 > 해외주식 체결기준현재잔고 | `/uapi/overseas-stock/v1/trading/inquire-present-balance` | `CTRP6504R`, `VTRP6504R` |
| `inquire_psamount` | `REST` | [해외주식] 주문/계좌 > 해외주식 매수가능금액조회 | `/uapi/overseas-stock/v1/trading/inquire-psamount` | `TTTS3007R`, `VTTS3007R` |
| `inquire_search` | `REST` | [해외주식] 시세분석 > 해외주식조건검색 | `/uapi/overseas-price/v1/quotations/inquire-search` | `HHDFS76410000` |
| `inquire_time_indexchartprice` | `REST` | [해외주식] 기본시세 > 해외지수분봉조회 | `/uapi/overseas-price/v1/quotations/inquire-time-indexchartprice` | `FHKST03030200` |
| `inquire_time_itemchartprice` | `REST` | [해외주식] 기본시세 > 해외주식분봉조회 | `/uapi/overseas-price/v1/quotations/inquire-time-itemchartprice` | `HHDFS76950200` |
| `market_cap` | `REST` | [해외주식] 시세분석 > 해외주식 시가총액순위 | `/uapi/overseas-stock/v1/ranking/market-cap` | `HHDFS76350100` |
| `new_highlow` | `REST` | [해외주식] 시세분석 > 해외주식 신고/신저가 | `/uapi/overseas-stock/v1/ranking/new-highlow` | `HHDFS76300000` |
| `news_title` | `REST` | [해외주식] 시세분석 > 해외뉴스종합(제목) | `/uapi/overseas-price/v1/quotations/news-title` | `HHPSTH60100C1` |
| `order` | `REST` | [해외주식] 주문/계좌 > 해외주식 주문 | `/uapi/overseas-stock/v1/trading/order` | `TTTT1002U`, `TTTS1002U`, `TTTS0202U`, `TTTS0305U`, `TTTS0308U`, `TTTS0311U`, `TTTT1006U`, `TTTS1001U`, `TTTS1005U`, `TTTS0304U`, `TTTS0307U`, `TTTS0310U`, `V` |
| `order_resv` | `REST` | [해외주식] 주문/계좌 > 해외주식 예약주문접수 | `/uapi/overseas-stock/v1/trading/order-resv` | `TTTT3014U`, `TTTT3016U`, `TTTS3013U`, `VTTT3014U`, `VTTT3016U`, `VTTS3013U` |
| `order_resv_ccnl` | `REST` | [해외주식] 주문/계좌 > 해외주식 예약주문접수취소 | `/uapi/overseas-stock/v1/trading/order-resv-ccnl` | `TTTT3017U`, `VTTT3017U` |
| `order_resv_list` | `REST` | [해외주식] 주문/계좌 > 해외주식 예약주문조회 | `/uapi/overseas-stock/v1/trading/order-resv-list` | `TTTT3039R`, `TTTS3014R` |
| `order_rvsecncl` | `REST` | [해외주식] 주문/계좌 > 해외주식 정정취소주문 | `/uapi/overseas-stock/v1/trading/order-rvsecncl` | `TTTT1004U`, `VTTT1004U` |
| `period_rights` | `REST` | [해외주식] 시세분석 > 해외주식 기간별권리조회 | `/uapi/overseas-price/v1/quotations/period-rights` | `CTRGT011R` |
| `price` | `REST` | [해외주식] 기본시세 - 해외주식 현재체결가 | `/uapi/overseas-price/v1/quotations/price` | `HHDFS00000300` |
| `price_detail` | `REST` | [해외주식] 기본시세 > 해외주식 현재가상세 | `/uapi/overseas-price/v1/quotations/price-detail` | `HHDFS76200200` |
| `price_fluct` | `REST` | [해외주식] 시세분석 > 해외주식 가격급등락 | `/uapi/overseas-stock/v1/ranking/price-fluct` | `HHDFS76260000` |
| `quot_inquire_ccnl` | `REST` | [해외주식] 기본시세 > 해외주식 체결추이 | `/uapi/overseas-price/v1/quotations/inquire-ccnl` | `HHDFS76200300` |
| `rights_by_ice` | `REST` | [해외주식] 시세분석 > 해외주식 권리종합 | `/uapi/overseas-price/v1/quotations/rights-by-ice` | `HHDFS78330900` |
| `search_info` | `REST` | [해외주식] 시세분석 > 해외주식 상품기본정보 | `/uapi/overseas-price/v1/quotations/search-info` | `CTPF1702R` |
| `trade_growth` | `REST` | [해외주식] 시세분석 > 해외주식 거래증가율순위 | `/uapi/overseas-stock/v1/ranking/trade-growth` | `HHDFS76330000` |
| `trade_pbmn` | `REST` | [해외주식] 시세분석 > 해외주식 거래대금순위 | `/uapi/overseas-stock/v1/ranking/trade-pbmn` | `HHDFS76320010` |
| `trade_turnover` | `REST` | [해외주식] 시세분석 > 해외주식 거래회전율순위 | `/uapi/overseas-stock/v1/ranking/trade-turnover` | `HHDFS76340000` |
| `trade_vol` | `REST` | [해외주식] 시세분석 > 해외주식 거래량순위 | `/uapi/overseas-stock/v1/ranking/trade-vol` | `HHDFS76310010` |
| `updown_rate` | `REST` | [해외주식] 시세분석 > 해외주식 상승률/하락률 | `/uapi/overseas-stock/v1/ranking/updown-rate` | `HHDFS76290000` |
| `volume_power` | `REST` | [해외주식] 시세분석 > 해외주식 매수체결강도상위 | `/uapi/overseas-stock/v1/ranking/volume-power` | `HHDFS76280000` |
| `volume_surge` | `REST` | [해외주식] 시세분석 > 해외주식 거래량급증 | `/uapi/overseas-stock/v1/ranking/volume-surge` | `HHDFS76270000` |
| `asking_price` | `WebSocket` | [해외주식] 실시간시세 > 해외주식 실시간호가 | - | `HDFSASP0` |
| `ccnl_notice` | `WebSocket` | [해외주식] 실시간시세 > 해외주식 실시간체결통보 | - | `H0GSCNI0`, `H0GSCNI9` |
| `delayed_asking_price_asia` | `WebSocket` | [해외주식] 실시간시세 > 해외주식 지연호가(아시아) | - | `HDFSASP1` |
| `delayed_ccnl` | `WebSocket` | [해외주식] 실시간시세 > 해외주식 실시간지연체결가 | - | `HDFSCNT0` |

---

## 4. 국내선물옵션 (Domestic Futures & Options)

| 함수명 (`examples_llm`) | 구분 | 한글 기능명 | 엔드포인트 / 실시간 TR ID | TR ID |
| :--- | :---: | :--- | :--- | :--- |
| `display_board_callput` | `REST` | [국내선물옵션] 기본시세 > 국내옵션전광판_콜풋[국내선물-022] | `/uapi/domestic-futureoption/v1/quotations/display-board-callput` | `FHPIF05030100` |
| `display_board_futures` | `REST` | [국내선물옵션] 기본시세 > 국내옵션전광판_선물[국내선물-023] | `/uapi/domestic-futureoption/v1/quotations/display-board-futures` | `FHPIF05030200` |
| `display_board_option_list` | `REST` | [국내선물옵션] 기본시세 > 국내옵션전광판_옵션월물리스트[국내선물-020] | `/uapi/domestic-futureoption/v1/quotations/display-board-option-list` | `FHPIO056104C0` |
| `display_board_top` | `REST` | [국내선물옵션] 기본시세 > 국내선물 기초자산 시세[국내선물-021] | `/uapi/domestic-futureoption/v1/quotations/display-board-top` | `FHPIF05030000` |
| `exp_price_trend` | `REST` | [국내선물옵션] 기본시세 > 선물옵션 일중예상체결추이[국내선물-018] | `/uapi/domestic-futureoption/v1/quotations/exp-price-trend` | `FHPIF05110100` |
| `inquire_asking_price` | `REST` | [국내선물옵션] 기본시세 > 선물옵션 시세호가 | `/uapi/domestic-futureoption/v1/quotations/inquire-asking-price` | `FHMIF10010000` |
| `inquire_balance` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션 잔고현황 | `/uapi/domestic-futureoption/v1/trading/inquire-balance` | `CTFO6118R`, `VTFO6118R` |
| `inquire_balance_settlement_pl` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션 잔고정산손익내역 | `/uapi/domestic-futureoption/v1/trading/inquire-balance-settlement-pl` | `CTFO6117R` |
| `inquire_balance_valuation_pl` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션 잔고평가손익내역 | `/uapi/domestic-futureoption/v1/trading/inquire-balance-valuation-pl` | `CTFO6159R` |
| `inquire_ccnl` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션 주문체결내역조회 | `/uapi/domestic-futureoption/v1/trading/inquire-ccnl` | `TTTO5201R`, `VTTO5201R` |
| `inquire_ccnl_bstime` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션 기준일체결내역 | `/uapi/domestic-futureoption/v1/trading/inquire-ccnl-bstime` | `CTFO5139R` |
| `inquire_daily_amount_fee` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션기간약정수수료일별 | `/uapi/domestic-futureoption/v1/trading/inquire-daily-amount-fee` | `CTFO6119R` |
| `inquire_daily_fuopchartprice` | `REST` | [국내선물옵션] 기본시세 > 선물옵션기간별시세(일/주/월/년) | `/uapi/domestic-futureoption/v1/quotations/inquire-daily-fuopchartprice` | `FHKIF03020100` |
| `inquire_deposit` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션 총자산현황 | `/uapi/domestic-futureoption/v1/trading/inquire-deposit` | `CTRP6550R` |
| `inquire_ngt_balance` | `REST` | [국내선물옵션] 주문/계좌 > (야간)선물옵션 잔고현황 [국내선물-010] | `/uapi/domestic-futureoption/v1/trading/inquire-ngt-balance` | `CTFN6118R` |
| `inquire_ngt_ccnl` | `REST` | [국내선물옵션] 주문/계좌 > (야간)선물옵션 주문체결 내역조회 [국내선물-009] | `/uapi/domestic-futureoption/v1/trading/inquire-ngt-ccnl` | `STTN5201R` |
| `inquire_price` | `REST` | [국내선물옵션] 기본시세 > 선물옵션 시세 | `/uapi/domestic-futureoption/v1/quotations/inquire-price` | `FHMIF10000000` |
| `inquire_psbl_ngt_order` | `REST` | [국내선물옵션] 주문/계좌 > (야간)선물옵션 주문가능 조회 [국내선물-011] | `/uapi/domestic-futureoption/v1/trading/inquire-psbl-ngt-order` | `STTN5105R` |
| `inquire_psbl_order` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션 주문가능 | `/uapi/domestic-futureoption/v1/trading/inquire-psbl-order` | `TTTO5105R`, `VTTO5105R` |
| `inquire_time_fuopchartprice` | `REST` | [국내선물옵션] 기본시세 > 선물옵션 분봉조회 | `/uapi/domestic-futureoption/v1/quotations/inquire-time-fuopchartprice` | `FHKIF03020200` |
| `ngt_margin_detail` | `REST` | [국내선물옵션] 주문/계좌 > (야간)선물옵션 증거금 상세 [국내선물-024] | `/uapi/domestic-futureoption/v1/trading/ngt-margin-detail` | `CTFN7107R` |
| `order` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션 주문 | `/uapi/domestic-futureoption/v1/trading/order` | `TTTO1101U`, `STTN1101U`, `VTTO1101U` |
| `order_rvsecncl` | `REST` | [국내선물옵션] 주문/계좌 > 선물옵션 정정취소주문 | `/uapi/domestic-futureoption/v1/trading/order-rvsecncl` | `TTTO1103U`, `TTTN1103U`, `VTTO1103U` |
| `commodity_futures_realtime_conclusion` | `WebSocket` | [국내선물옵션] 실시간시세 > 상품선물 실시간체결가 | - | `H0CFCNT0` |
| `commodity_futures_realtime_quote` | `WebSocket` | [국내선물옵션] 실시간시세 > 상품선물 실시간호가 | - | `H0CFASP0` |
| `fuopt_ccnl_notice` | `WebSocket` | [국내선물옵션] 실시간시세 > 선물옵션 실시간체결통보 | - | `H0IFCNI0` |
| `futures_exp_ccnl` | `WebSocket` | [국내선물옵션] 실시간시세 > 주식선물 실시간예상체결 | - | `H0ZFANC0` |
| `index_futures_realtime_conclusion` | `WebSocket` | [국내선물옵션] 실시간시세 > 지수선물 실시간체결가 | - | `H0IFCNT0` |
| `index_futures_realtime_quote` | `WebSocket` | [국내선물옵션] 실시간시세 > 지수선물 실시간호가 | - | `H0IFASP0` |
| `index_option_realtime_conclusion` | `WebSocket` | [국내선물옵션] 실시간시세 > 지수옵션 실시간체결가 | - | `H0IOCNT0` |
| `index_option_realtime_quote` | `WebSocket` | [국내선물옵션] 실시간시세 > 지수옵션 실시간호가 | - | `H0IOASP0` |
| `krx_ngt_futures_asking_price` | `WebSocket` | [국내선물옵션] 실시간시세 > KRX야간선물 실시간호가 | - | `H0MFASP0` |
| `krx_ngt_futures_ccnl` | `WebSocket` | [국내선물옵션] 실시간시세 > KRX야간선물 실시간종목체결 | - | `H0MFCNT0` |
| `krx_ngt_futures_ccnl_notice` | `WebSocket` | [국내선물옵션] 실시간시세 > KRX야간선물 실시간체결통보 | - | `H0MFCNI0` |
| `krx_ngt_option_asking_price` | `WebSocket` | [국내선물옵션] 실시간시세 > KRX야간옵션 실시간호가 | - | `H0EUASP0` |
| `krx_ngt_option_ccnl` | `WebSocket` | [국내선물옵션] 실시간시세 > KRX야간옵션 실시간체결가 | - | `H0EUCNT0` |
| `krx_ngt_option_exp_ccnl` | `WebSocket` | [국내선물옵션] 실시간시세 > KRX야간옵션실시간예상체결 | - | `H0EUANC0` |
| `krx_ngt_option_notice` | `WebSocket` | [국내선물옵션] 실시간시세 > KRX야간옵션실시간체결통보 | - | `H0EUCNI0` |
| `option_exp_ccnl` | `WebSocket` | [국내선물옵션] 실시간시세 > 주식옵션 실시간예상체결 | - | `H0ZOANC0` |
| `stock_futures_realtime_conclusion` | `WebSocket` | [국내선물옵션] 실시간시세 > 주식선물 실시간체결가 | - | `H0ZFCNT0` |
| `stock_futures_realtime_quote` | `WebSocket` | [국내선물옵션] 실시간시세 > 주식선물 실시간호가 | - | `H0ZFASP0` |
| `stock_option_asking_price` | `WebSocket` | [국내선물옵션] 실시간시세 > 주식옵션 실시간호가 | - | `H0ZOASP0` |
| `stock_option_ccnl` | `WebSocket` | [국내선물옵션] 실시간시세 > 주식옵션 실시간체결가 | - | `H0ZOCNT0` |

---

## 5. 해외선물옵션 (Overseas Futures & Options)

| 함수명 (`examples_llm`) | 구분 | 한글 기능명 | 엔드포인트 / 실시간 TR ID | TR ID |
| :--- | :---: | :--- | :--- | :--- |
| `daily_ccnl` | `REST` | [해외선물옵션] 기본시세 > 해외선물 체결추이(일간) [해외선물-018] | `/uapi/overseas-futureoption/v1/quotations/daily-ccnl` | `HHDFC55020100` |
| `inquire_asking_price` | `REST` | [해외선물옵션] 기본시세 > 해외선물 호가 [해외선물-031] | `/uapi/overseas-futureoption/v1/quotations/inquire-asking-price` | `HHDFC86000000` |
| `inquire_ccld` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 당일주문내역조회 | `/uapi/overseas-futureoption/v1/trading/inquire-ccld` | `OTFM3116R` |
| `inquire_daily_ccld` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 일별체결내역[해외선물-011] | `/uapi/overseas-futureoption/v1/trading/inquire-daily-ccld` | `OTFM3122R` |
| `inquire_daily_order` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 일별 주문내역 [해외선물-013] | `/uapi/overseas-futureoption/v1/trading/inquire-daily-order` | `OTFM3120R` |
| `inquire_deposit` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 예수금현황 [해외선물-012] | `/uapi/overseas-futureoption/v1/trading/inquire-deposit` | `OTFM1411R` |
| `inquire_period_ccld` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 기간계좌손익 일별 [해외선물-010] | `/uapi/overseas-futureoption/v1/trading/inquire-period-ccld` | `OTFM3118R` |
| `inquire_period_trans` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 기간계좌거래내역 [해외선물-014] | `/uapi/overseas-futureoption/v1/trading/inquire-period-trans` | `OTFM3114R` |
| `inquire_price` | `REST` | [해외선물옵션] 기본시세 > 해외선물종목현재가 | `/uapi/overseas-futureoption/v1/quotations/inquire-price` | `HHDFC55010000` |
| `inquire_psamount` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 주문가능조회 | `/uapi/overseas-futureoption/v1/trading/inquire-psamount` | `OTFM3304R` |
| `inquire_time_futurechartprice` | `REST` | [해외선물옵션] 기본시세 > 해외선물 분봉조회[해외선물-016] | `/uapi/overseas-futureoption/v1/quotations/inquire-time-futurechartprice` | `HHDFC55020400` |
| `inquire_time_optchartprice` | `REST` | [해외선물옵션] 기본시세 > 해외옵션 분봉조회 [해외선물-040] | `/uapi/overseas-futureoption/v1/quotations/inquire-time-optchartprice` | `HHDFO55020100` |
| `inquire_unpd` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 미결제내역조회(잔고) | `/uapi/overseas-futureoption/v1/trading/inquire-unpd` | `OTFM1412R` |
| `investor_unpd_trend` | `REST` | [해외선물옵션] 기본시세 > 해외선물 미결제추이 [해외선물-029] | `/uapi/overseas-futureoption/v1/quotations/investor-unpd-trend` | `HHDDB95030000` |
| `margin_detail` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 증거금상세 [해외선물-032] | `/uapi/overseas-futureoption/v1/trading/margin-detail` | `OTFM3115R` |
| `market_time` | `REST` | [해외선물옵션] 기본시세 > 해외선물옵션 장운영시간 [해외선물-030] | `/uapi/overseas-futureoption/v1/quotations/market-time` | `OTFM2229R` |
| `monthly_ccnl` | `REST` | [해외선물옵션] 기본시세 > 해외선물 체결추이(월간)[해외선물-020] | `/uapi/overseas-futureoption/v1/quotations/monthly-ccnl` | `HHDFC55020300` |
| `opt_asking_price` | `REST` | [해외선물옵션] 기본시세 > 해외옵션 호가 [해외선물-033] | `/uapi/overseas-futureoption/v1/quotations/opt-asking-price` | `HHDFO86000000` |
| `opt_daily_ccnl` | `REST` | [해외선물옵션] 기본시세 > 해외옵션 체결추이(일간) [해외선물-037] | `/uapi/overseas-futureoption/v1/quotations/opt-daily-ccnl` | `HHDFO55020100` |
| `opt_detail` | `REST` | [해외선물옵션] 기본시세 > 해외옵션종목상세 [해외선물-034] | `/uapi/overseas-futureoption/v1/quotations/opt-detail` | `HHDFO55010100` |
| `opt_monthly_ccnl` | `REST` | [해외선물옵션] 기본시세 > 해외옵션 체결추이(월간) [해외선물-039] | `/uapi/overseas-futureoption/v1/quotations/opt-monthly-ccnl` | `HHDFO55020300` |
| `opt_price` | `REST` | [해외선물옵션] 기본시세 > 해외옵션종목현재가 [해외선물-035] | `/uapi/overseas-futureoption/v1/quotations/opt-price` | `HHDFO55010000` |
| `opt_tick_ccnl` | `REST` | [해외선물옵션] 기본시세 > 해외옵션 체결추이(틱) [해외선물-038] | `/uapi/overseas-futureoption/v1/quotations/opt-tick-ccnl` | `HHDFO55020200` |
| `opt_weekly_ccnl` | `REST` | [해외선물옵션] 기본시세 > 해외옵션 체결추이(주간) [해외선물-036] | `/uapi/overseas-futureoption/v1/quotations/opt-weekly-ccnl` | `HHDFO55020000` |
| `order` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 주문 | `/uapi/overseas-futureoption/v1/trading/order` | `OTFM3001U` |
| `order_rvsecncl` | `REST` | [해외선물옵션] 주문/계좌 > 해외선물옵션 정정취소주문 | `/uapi/overseas-futureoption/v1/trading/order-rvsecncl` | `OTFM3002U`, `OTFM3003U` |
| `search_contract_detail` | `REST` | [해외선물옵션] 기본시세 > 해외선물 상품기본정보[해외선물-023] | `/uapi/overseas-futureoption/v1/quotations/search-contract-detail` | `HHDFC55200000` |
| `search_opt_detail` | `REST` | [해외선물옵션] 기본시세 > 해외옵션 상품기본정보 [해외선물-041] | `/uapi/overseas-futureoption/v1/quotations/search-opt-detail` | `HHDFO55200000` |
| `stock_detail` | `REST` | [해외선물옵션] 기본시세 > 해외선물종목상세 | `/uapi/overseas-futureoption/v1/quotations/stock-detail` | `HHDFC55010100` |
| `tick_ccnl` | `REST` | [해외선물옵션] 기본시세 > 해외선물 체결추이(틱)[해외선물-019] | `/uapi/overseas-futureoption/v1/quotations/tick-ccnl` | `HHDFC55020200` |
| `weekly_ccnl` | `REST` | [해외선물옵션] 기본시세 > 해외선물 체결추이(주간)[해외선물-017] | `/uapi/overseas-futureoption/v1/quotations/weekly-ccnl` | `HHDFC55020000` |
| `asking_price` | `WebSocket` | [해외선물옵션] 실시간시세 > 해외선물옵션 실시간호가 | - | `HDFFF010` |
| `ccnl` | `WebSocket` | [해외선물옵션] 실시간시세 > 해외선물옵션 실시간체결가 | - | `HDFFF020` |
| `ccnl_notice` | `WebSocket` | [해외선물옵션] 실시간시세 > 해외선물옵션 실시간체결내역통보 | - | `HDFFF2C0` |
| `order_notice` | `WebSocket` | [해외선물옵션] 실시간시세 > 해외선물옵션 실시간주문내역통보 | - | `HDFFF1C0` |

---

## 6. 국내채권 (Domestic Bond)

| 함수명 (`examples_llm`) | 구분 | 한글 기능명 | 엔드포인트 / 실시간 TR ID | TR ID |
| :--- | :---: | :--- | :--- | :--- |
| `avg_unit` | `REST` | [장내채권] 기본시세 - 장내채권 평균단가조회 | `/uapi/domestic-bond/v1/quotations/avg-unit` | `CTPF2005R` |
| `buy` | `REST` | [장내채권] 주문/계좌 - 장내채권 매수주문 | `/uapi/domestic-bond/v1/trading/buy` | `TTTC0952U` |
| `inquire_asking_price` | `REST` | [장내채권] 기본시세 - 장내채권현재가(호가) | `/uapi/domestic-bond/v1/quotations/inquire-asking-price` | `FHKBJ773401C0` |
| `inquire_balance` | `REST` | [장내채권] 주문/계좌 - 장내채권 잔고조회 | `/uapi/domestic-bond/v1/trading/inquire-balance` | `CTSC8407R` |
| `inquire_ccnl` | `REST` | [장내채권] 기본시세 - 장내채권현재가(체결) | `/uapi/domestic-bond/v1/quotations/inquire-ccnl` | `FHKBJ773403C0` |
| `inquire_daily_ccld` | `REST` | [장내채권] 주문/계좌 - 장내채권 주문체결내역 | `/uapi/domestic-bond/v1/trading/inquire-daily-ccld` | `CTSC8013R` |
| `inquire_daily_itemchartprice` | `REST` | [장내채권] 기본시세 - 장내채권 기간별시세(일) | `/uapi/domestic-bond/v1/quotations/inquire-daily-itemchartprice` | `FHKBJ773701C0` |
| `inquire_daily_price` | `REST` | [장내채권] 기본시세 - 장내채권현재가(일별) | `/uapi/domestic-bond/v1/quotations/inquire-daily-price` | `FHKBJ773404C0` |
| `inquire_price` | `REST` | [장내채권] 기본시세 - 장내채권현재가(시세) | `/uapi/domestic-bond/v1/quotations/inquire-price` | `FHKBJ773400C0` |
| `inquire_psbl_order` | `REST` | [장내채권] 주문/계좌 - 장내채권 매수가능조회 | `/uapi/domestic-bond/v1/trading/inquire-psbl-order` | `TTTC8910R` |
| `inquire_psbl_rvsecncl` | `REST` | [장내채권] 주문/계좌 - 채권정정취소가능주문조회 | `/uapi/domestic-bond/v1/trading/inquire-psbl-rvsecncl` | `CTSC8035R` |
| `issue_info` | `REST` | [장내채권] 기본시세 - 장내채권 발행정보 | `/uapi/domestic-bond/v1/quotations/issue-info` | `CTPF1101R` |
| `order_rvsecncl` | `REST` | [장내채권] 주문/계좌 - 장내채권 정정취소주문 | `/uapi/domestic-bond/v1/trading/order-rvsecncl` | `TTTC0953U` |
| `search_bond_info` | `REST` | [장내채권] 기본시세 - 장내채권 기본조회 | `/uapi/domestic-bond/v1/quotations/search-bond-info` | `CTPF1114R` |
| `sell` | `REST` | [장내채권] 주문/계좌 - 장내채권 매도주문 | `/uapi/domestic-bond/v1/trading/sell` | `TTTC0958U` |
| `bond_asking_price` | `WebSocket` | [장내채권] 실시간시세 > 일반채권 실시간호가 | - | `H0BJASP0` |
| `bond_ccnl` | `WebSocket` | [장내채권] 실시간시세 > 일반채권 실시간체결가 | - | `H0BJCNT0` |
| `bond_index_ccnl` | `WebSocket` | [장내채권] 실시간시세 > 채권지수 실시간체결가 | - | `H0BICNT0` |

---

## 7. ETF / ETN

| 함수명 (`examples_llm`) | 구분 | 한글 기능명 | 엔드포인트 / 실시간 TR ID | TR ID |
| :--- | :---: | :--- | :--- | :--- |
| `inquire_component_stock_price` | `REST` | [국내주식] 기본시세 > ETF 구성종목시세 | `/uapi/etfetn/v1/quotations/inquire-component-stock-price` | `FHKST121600C0` |
| `inquire_price` | `REST` | [국내주식] 기본시세 > ETF/ETN 현재가 | `/uapi/etfetn/v1/quotations/inquire-price` | `FHPST02400000` |
| `nav_comparison_daily_trend` | `REST` | [국내주식] 기본시세 > NAV 비교추이(일) | `/uapi/etfetn/v1/quotations/nav-comparison-daily-trend` | `FHPST02440200` |
| `nav_comparison_time_trend` | `REST` | [국내주식] 기본시세 > NAV 비교추이(분) | `/uapi/etfetn/v1/quotations/nav-comparison-time-trend` | `FHPST02440100` |
| `nav_comparison_trend` | `REST` | [국내주식] 기본시세 > NAV 비교추이(종목) | `/uapi/etfetn/v1/quotations/nav-comparison-trend` | `FHPST02440000` |
| `etf_nav_trend` | `WebSocket` | [국내주식] 실시간시세 > 국내ETF NAV추이 | - | `H0STNAV0` |

---

## 8. ELW (주식워런트증권)

| 함수명 (`examples_llm`) | 구분 | 한글 기능명 | 엔드포인트 / 실시간 TR ID | TR ID |
| :--- | :---: | :--- | :--- | :--- |
| `compare_stocks` | `REST` | [국내주식] ELW시세 - ELW 비교대상종목조회 | `/uapi/elw/v1/quotations/compare-stocks` | `FHKEW151701C0` |
| `cond_search` | `REST` | [국내주식] ELW시세 - ELW 종목검색 | `/uapi/elw/v1/quotations/cond-search` | `FHKEW15100000` |
| `expiration_stocks` | `REST` | [국내주식] ELW시세 - ELW 만기예정/만기종목 | `/uapi/elw/v1/quotations/expiration-stocks` | `FHKEW154700C0` |
| `indicator` | `REST` | [국내주식] ELW시세 - ELW 지표순위 | `/uapi/elw/v1/ranking/indicator` | `FHPEW02790000` |
| `indicator_trend_ccnl` | `REST` | [국내주식] ELW시세 - ELW 투자지표추이(체결) | `/uapi/elw/v1/quotations/indicator-trend-ccnl` | `FHPEW02740100` |
| `indicator_trend_daily` | `REST` | [국내주식] ELW시세 - ELW 투자지표추이(일별) | `/uapi/elw/v1/quotations/indicator-trend-daily` | `FHPEW02740200` |
| `indicator_trend_minute` | `REST` | [국내주식] ELW시세 - ELW 투자지표추이(분별) | `/uapi/elw/v1/quotations/indicator-trend-minute` | `FHPEW02740300` |
| `lp_trade_trend` | `REST` | [국내주식] ELW시세 - ELW LP매매추이 | `/uapi/elw/v1/quotations/lp-trade-trend` | `FHPEW03760000` |
| `newly_listed` | `REST` | [국내주식] ELW시세 - ELW 신규상장종목 | `/uapi/elw/v1/quotations/newly-listed` | `FHKEW154800C0` |
| `quick_change` | `REST` | [국내주식] ELW시세 - ELW 당일급변종목 | `/uapi/elw/v1/ranking/quick-change` | `FHPEW02870000` |
| `sensitivity` | `REST` | [국내주식] ELW시세 - ELW 민감도 순위 | `/uapi/elw/v1/ranking/sensitivity` | `FHPEW02850000` |
| `sensitivity_trend_ccnl` | `REST` | [국내주식] ELW시세 - ELW 민감도 추이(체결) | `/uapi/elw/v1/quotations/sensitivity-trend-ccnl` | `FHPEW02830100` |
| `sensitivity_trend_daily` | `REST` | [국내주식] ELW시세 - ELW 민감도 추이(일별) | `/uapi/elw/v1/quotations/sensitivity-trend-daily` | `FHPEW02830200` |
| `udrl_asset_list` | `REST` | [국내주식] ELW시세 - ELW 기초자산 목록조회 | `/uapi/elw/v1/quotations/udrl-asset-list` | `FHKEW154100C0` |
| `udrl_asset_price` | `REST` | [국내주식] ELW시세 - ELW 기초자산별 종목시세 | `/uapi/elw/v1/quotations/udrl-asset-price` | `FHKEW154101C0` |
| `updown_rate` | `REST` | [국내주식] ELW시세 - ELW 상승률순위 | `/uapi/elw/v1/ranking/updown-rate` | `FHPEW02770000` |
| `volatility_trend_ccnl` | `REST` | [국내주식] ELW시세 - ELW 변동성추이(체결) | `/uapi/elw/v1/quotations/volatility-trend-ccnl` | `FHPEW02840100` |
| `volatility_trend_daily` | `REST` | [국내주식] ELW시세 - ELW 변동성추이(일별) | `/uapi/elw/v1/quotations/volatility-trend-daily` | `FHPEW02840200` |
| `volatility_trend_minute` | `REST` | [국내주식] ELW시세 - ELW 변동성 추이(분별) | `/uapi/elw/v1/quotations/volatility-trend-minute` | `FHPEW02840300` |
| `volatility_trend_tick` | `REST` | [국내주식] ELW시세 - ELW 변동성추이(틱) | `/uapi/elw/v1/quotations/volatility-trend-tick` | `FHPEW02840400` |
| `volume_rank` | `REST` | [국내주식] ELW시세 - ELW 거래량순위 | `/uapi/elw/v1/ranking/volume-rank` | `FHPEW02780000` |
| `elw_asking_price` | `WebSocket` | [국내주식] 실시간시세 - ELW 실시간호가 | - | `H0EWASP0` |
| `elw_ccnl` | `WebSocket` | [국내주식] 실시간시세 - ELW 실시간체결가 | - | `H0EWCNT0` |
| `elw_exp_ccnl` | `WebSocket` | [국내주식] 실시간시세 - ELW 실시간예상체결 | - | `H0EWANC0` |

---
