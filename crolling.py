# # crolling (DB UPDATE 없이 GET만 진행/ 현재 DB 업로드완료 상태로 전체 주석처리)_
# # DB Update 방식으로 전환시 코드 변경 & 주석 해제 필요
#
# # ------------- BASEBALL-------------#
#
# Baseball_SSG = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=SSG+%EB%9E%9C%EB%8D%94%EC%8A%A4+%EA%B8%B0%EB%B3%B8%EC%A0%95%EB%B3%B4', headers=headers)
# Baseball_SSG_soup = BeautifulSoup(Baseball_SSG.text, 'html.parser')
# Baseball_SSGs = Baseball_SSG_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_SSG in Baseball_SSGs:
#     name = Baseball_SSG.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_SSG.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_SSG.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_SSG.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# Baseball_DOOSAN = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%91%90%EC%82%B0+%EB%B2%A0%EC%96%B4%EC%8A%A4+%EA%B8%B0%EB%B3%B8+%EC%A0%95%EB%B3%B4', headers=headers)
# Baseball_DOOSAN_soup = BeautifulSoup(Baseball_DOOSAN.text, 'html.parser')
# Baseball_DOOSANs = Baseball_DOOSAN_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_DOOSAN in Baseball_DOOSANs:
#     name = Baseball_DOOSAN.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_DOOSAN.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_DOOSAN.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_DOOSAN.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# Baseball_LG = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=LG+%ED%8A%B8%EC%9C%88%EC%8A%A4+%EA%B8%B0%EB%B3%B8%EC%A0%95%EB%B3%B4', headers=headers)
# baseball_LG_soup = BeautifulSoup(Baseball_LG.text, 'html.parser')
# Baseball_LGs = baseball_LG_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_LG in Baseball_LGs:
#     name = Baseball_LG.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_LG.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_LG.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_LG.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# Baseball_LOTTE = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%A1%AF%EB%8D%B0+%EC%9E%90%EC%9D%B4%EC%96%B8%EC%B8%A0+%EA%B8%B0%EB%B3%B8%EC%A0%95%EB%B3%B4', headers=headers)
# Baseball_LOTTE_soup = BeautifulSoup(Baseball_LOTTE.text, 'html.parser')
# Baseball_LOTTEs = Baseball_LOTTE_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_LOTTE in Baseball_LOTTEs:
#     name = Baseball_LOTTE.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_LOTTE.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_LOTTE.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_LOTTE.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# Baseball_KIWOOM = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%ED%82%A4%EC%9B%80+%ED%9E%88%EC%96%B4%EB%A1%9C%EC%A6%88+%EA%B8%B0%EB%B3%B8%EC%A0%95%EB%B3%B4', headers=headers)
# Baseball_KIWOOM_soup = BeautifulSoup(Baseball_KIWOOM.text, 'html.parser')
# Baseball_KIWOOMs = Baseball_KIWOOM_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_KIWOOM in Baseball_KIWOOMs:
#     name = Baseball_KIWOOM.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_KIWOOM.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_KIWOOM.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_KIWOOM.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# Baseball_KIA = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EA%B8%B0%EC%95%84+%ED%83%80%EC%9D%B4%EA%B1%B0%EC%A6%88+%EA%B8%B0%EB%B3%B8%EC%A0%95%EB%B3%B4', headers=headers)
# Baseball_KIA_soup = BeautifulSoup(Baseball_KIA.text, 'html.parser')
# Baseball_KIAs = Baseball_KIA_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_KIA in Baseball_KIAs:
#     name = Baseball_KIA.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_KIA.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_KIA.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_KIA.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# Baseball_SAMSUNG = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%82%BC%EC%84%B1+%EB%9D%BC%EC%9D%B4%EC%98%A8%EC%A6%88+%EA%B8%B0%EB%B3%B8%EC%A0%95%EB%B3%B4', headers=headers)
# Baseball_SAMSUNG_soup = BeautifulSoup(Baseball_SAMSUNG.text, 'html.parser')
# Baseball_SAMSUNGs = Baseball_SAMSUNG_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_SAMSUNG in Baseball_SAMSUNGs:
#     name = Baseball_SAMSUNG.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_SAMSUNG.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_SAMSUNG.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_SAMSUNG.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# Baseball_KT = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%BC%80%EC%9D%B4%ED%8B%B0+%EC%9C%84%EC%A6%88+%EA%B8%B0%EB%B3%B8%EC%A0%95%EB%B3%B4', headers=headers)
# Baseball_KT_soup = BeautifulSoup(Baseball_KT.text, 'html.parser')
# Baseball_KTs = Baseball_KT_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_KT in Baseball_KTs:
#     name = Baseball_KT.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_KT.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_KT.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_KT.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# Baseball_HANHWA = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%ED%95%9C%ED%99%94+%EC%9D%B4%EA%B8%80%EC%8A%A4+%EA%B8%B0%EB%B3%B8%EC%A0%95%EB%B3%B4', headers=headers)
# Baseball_HANHWA_soup = BeautifulSoup(Baseball_HANHWA.text, 'html.parser')
# Baseball_HANHWAs = Baseball_HANHWA_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_HANHWA in Baseball_HANHWAs:
#     name = Baseball_HANHWA.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_HANHWA.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_HANHWA.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_HANHWA.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# Baseball_NC = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=nc+%EB%8B%A4%EC%9D%B4%EB%85%B8%EC%8A%A4+%EA%B8%B0%EB%B3%B8%EC%A0%95%EB%B3%B4', headers=headers)
# Baseball_NC_soup = BeautifulSoup(Baseball_NC.text, 'html.parser')
# Baseball_NCs = Baseball_NC_soup.select('#sgrColl > div.coll_cont > div')
# for Baseball_NC in Baseball_NCs:
#     name = Baseball_NC.select_one('div.wrap_team > div > div.tit_team > a').text
#     logo = Baseball_NC.select_one('div.wrap_team > div > div.tit_team > span > img')['src']
#     rank = Baseball_NC.select_one('div.wrap_cont > dl:nth-child(5)').text[8:30]
#     home = Baseball_NC.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASEBALL.insert_one(doc)
#
# # ------------- SOCCER -------------#
#
# SOCCER_SEOUL = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%84%9C%EC%9A%B8+FC+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_SEOUL_soup = BeautifulSoup(SOCCER_SEOUL.text, 'html.parser')
# SOCCER_SEOULs = SOCCER_SEOUL_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_SEOUL in SOCCER_SEOULs:
#     name = SOCCER_SEOUL.select_one('div.wrap_league > a').text
#     logo = SOCCER_SEOUL.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_SEOUL.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_SEOUL.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_ULSAN = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%9A%B8%EC%82%B0+%ED%98%84%EB%8C%80+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_ULSAN_soup = BeautifulSoup(SOCCER_ULSAN.text, 'html.parser')
# SOCCER_ULSANs = SOCCER_ULSAN_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_ULSAN in SOCCER_ULSANs:
#     name = SOCCER_ULSAN.select_one('div.wrap_league > a').text
#     logo = SOCCER_ULSAN.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_ULSAN.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_ULSAN.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_POHANG = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%ED%8F%AC%ED%95%AD+%EC%8A%A4%ED%8B%B8%EB%9F%AC%EC%8A%A4+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_POHANG_soup = BeautifulSoup(SOCCER_POHANG.text, 'html.parser')
# SOCCER_POHANGs = SOCCER_POHANG_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_POHANG in SOCCER_POHANGs:
#     name = SOCCER_POHANG.select_one('div.wrap_league > a').text
#     logo = SOCCER_POHANG.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_POHANG.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_POHANG.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_JEJU = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%A0%9C%EC%A3%BC+Utd+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_JEJU_soup = BeautifulSoup(SOCCER_JEJU.text, 'html.parser')
# SOCCER_JEJUs = SOCCER_JEJU_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_JEJU in SOCCER_JEJUs:
#     name = SOCCER_JEJU.select_one('div.wrap_league > a').text
#     logo = SOCCER_JEJU.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_JEJU.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_JEJU.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_INCHEON = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%9D%B8%EC%B2%9C+Utd+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_INCHEON_soup = BeautifulSoup(SOCCER_INCHEON.text, 'html.parser')
# SOCCER_INCHEONs = SOCCER_INCHEON_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_INCHEON in SOCCER_INCHEONs:
#     name = SOCCER_INCHEON.select_one('div.wrap_league > a').text
#     logo = SOCCER_INCHEON.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_INCHEON.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_INCHEON.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_JEONBUK = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%A0%84%EB%B6%81+%ED%98%84%EB%8C%80+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_JEONBUK_soup = BeautifulSoup(SOCCER_JEONBUK.text, 'html.parser')
# SOCCER_JEONBUKs = SOCCER_JEONBUK_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_JEONBUK in SOCCER_JEONBUKs:
#     name = SOCCER_JEONBUK.select_one('div.wrap_league > a').text
#     logo = SOCCER_JEONBUK.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_JEONBUK.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_JEONBUK.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_KIMCHEON = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EA%B9%80%EC%B2%9C+%EC%83%81%EB%AC%B4+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_KIMCHEON_soup = BeautifulSoup(SOCCER_KIMCHEON.text, 'html.parser')
# SOCCER_KIMCHEONs = SOCCER_KIMCHEON_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_KIMCHEON in SOCCER_KIMCHEONs:
#     name = SOCCER_KIMCHEON.select_one('div.wrap_league > a').text
#     logo = SOCCER_KIMCHEON.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_KIMCHEON.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = SOCCER_KIMCHEON.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
#
# SOCCER_DAEGU = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%8C%80%EA%B5%ACFC+%EC%A0%95', headers=headers)
# SOCCER_DAEGU_soup = BeautifulSoup(SOCCER_DAEGU.text, 'html.parser')
# SOCCER_DAEGUs = SOCCER_DAEGU_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_DAEGU in SOCCER_DAEGUs:
#     name = SOCCER_DAEGU.select_one('div.wrap_league > a').text
#     logo = SOCCER_DAEGU.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_DAEGU.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_DAEGU.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_SUWON = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%88%98%EC%9B%90FC+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_SUWON_soup = BeautifulSoup(SOCCER_SUWON.text, 'html.parser')
# SOCCER_SUWONs = SOCCER_SUWON_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_SUWON in SOCCER_SUWONs:
#     name = SOCCER_SUWON.select_one('div.wrap_league > a').text
#     logo = SOCCER_SUWON.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_SUWON.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_SUWON.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_KANGWON = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EA%B0%95%EC%9B%90FC+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_KANGWON_soup = BeautifulSoup(SOCCER_KANGWON.text, 'html.parser')
# SOCCER_KANGWONs = SOCCER_KANGWON_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_KANGWON in SOCCER_KANGWONs:
#     name = SOCCER_KANGWON.select_one('div.wrap_league > a').text
#     logo = SOCCER_KANGWON.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_KANGWON.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_KANGWON.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_SUWON_SAMSUNG = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%88%98%EC%9B%90+%EC%82%BC%EC%84%B1+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_SUWON_SAMSUNG_soup = BeautifulSoup(SOCCER_SUWON_SAMSUNG.text, 'html.parser')
# SOCCER_SUWON_SAMSUNGs = SOCCER_SUWON_SAMSUNG_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_SUWON_SAMSUNG in SOCCER_SUWON_SAMSUNGs:
#     name = SOCCER_SUWON_SAMSUNG.select_one('div.wrap_league > a').text
#     logo = SOCCER_SUWON_SAMSUNG.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_SUWON_SAMSUNG.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_SUWON_SAMSUNG.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# SOCCER_SEONGNAM = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%84%B1%EB%82%A8FC+%EC%A0%95%EB%B3%B4', headers=headers)
# SOCCER_SEONGNAM_soup = BeautifulSoup(SOCCER_SEONGNAM.text, 'html.parser')
# SOCCER_SEONGNAMs = SOCCER_SEONGNAM_soup.select('#sgrColl > div.coll_cont > div')
# for SOCCER_SEONGNAM in SOCCER_SEONGNAMs:
#     name = SOCCER_SEONGNAM.select_one('div.wrap_league > a').text
#     logo = SOCCER_SEONGNAM.select_one('div.wrap_thumb > a > img')['src']
#     rank = SOCCER_SEONGNAM.select_one('div.wrap_cont > dl:nth-child(5) > dd').text
#     home = SOCCER_SEONGNAM.select_one('div.wrap_cont > dl:nth-child(3) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.SOCCER.insert_one(doc)
#
# # ------------- BASKETBALL -------------#
#
# BASKETBALL_DB = requests.get('https://search.daum.net/search?w=tot&q=%EC%84%9C%EC%9A%B8%20%EC%82%BC%EC%84%B1%20%EC%8D%AC%EB%8D%94%EC%8A%A4&rtmaxcoll=SGR&DA=SGR&irt=sports-team&irk=KBL-356', headers=headers)
# BASKETBALL_DB_soup = BeautifulSoup(BASKETBALL_DB.text, 'html.parser')
# BASKETBALL_DBs = BASKETBALL_DB_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_DB in BASKETBALL_DBs:
#     name = BASKETBALL_DB.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_DB.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_DB.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_DB.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASKETBALL.insert_one(doc)
#
# BASKETBALL_SK = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%84%9C%EC%9A%B8+SK+%EB%82%98%EC%9D%B4%EC%B8%A0+%EC%A0%95%EB%B3%B4', headers=headers)
# BASKETBALL_SK_soup = BeautifulSoup(BASKETBALL_SK.text, 'html.parser')
# BASKETBALL_SKs = BASKETBALL_SK_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_SK in BASKETBALL_SKs:
#     name = BASKETBALL_SK.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_SK.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_SK.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_SK.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASKETBALL.insert_one(doc)
#
# BASKETBALL_KT = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%88%98%EC%9B%90+KT+%EC%86%8C%EB%8B%89%EB%B6%90+%EC%A0%95%EB%B3%B4', headers=headers)
# BASKETBALL_KT_soup = BeautifulSoup(BASKETBALL_KT.text, 'html.parser')
# BASKETBALL_KTs = BASKETBALL_KT_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_KT in BASKETBALL_KTs:
#     name = BASKETBALL_KT.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_KT.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_KT.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_KT.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASKETBALL.insert_one(doc)
#
# BASKETBALL_KGC = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%95%88%EC%96%91+KGC+%EC%9D%B8%EC%82%BC%EA%B3%B5%EC%82%AC+%EC%A0%95%EB%B3%B4', headers=headers)
# BASKETBALL_KGC_soup = BeautifulSoup(BASKETBALL_KGC.text, 'html.parser')
# BASKETBALL_KGCs = BASKETBALL_KGC_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_KGC in BASKETBALL_KGCs:
#     name = BASKETBALL_KGC.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_KGC.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_KGC.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_KGC.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name, 'logo': logo, 'rank': rank, 'home': home}
#     db.BASKETBALL.insert_one(doc)
#
# BASKETBALL_MOBIS = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%9A%B8%EC%82%B0+%ED%98%84%EB%8C%80%EB%AA%A8%EB%B9%84%EC%8A%A4+%ED%94%BC%EB%B2%84%EC%8A%A4+%EC%A0%95%EB%B3%B4', headers=headers)
# BASKETBALL_MOBIS_soup = BeautifulSoup(BASKETBALL_MOBIS.text, 'html.parser')
# BASKETBALL_MOBISs = BASKETBALL_MOBIS_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_MOBIS in BASKETBALL_MOBISs:
#     name = BASKETBALL_MOBIS.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_MOBIS.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_MOBIS.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_MOBIS.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASKETBALL.insert_one(doc)
#
# BASKETBALL_ORION = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EA%B3%A0%EC%96%91+%EC%98%A4%EB%A6%AC%EC%98%A8+%EC%98%A4%EB%A6%AC%EC%98%A8%EC%8A%A4+%EC%A0%95%EB%B3%B4', headers=headers)
# BASKETBALL_ORION_soup = BeautifulSoup(BASKETBALL_ORION.text, 'html.parser')
# BASKETBALL_ORIONs = BASKETBALL_ORION_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_ORION in BASKETBALL_ORIONs:
#     name = BASKETBALL_ORION.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_ORION.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_ORION.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_ORION.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASKETBALL.insert_one(doc)
#
# BASKETBALL_GAS = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%8C%80%EA%B5%AC+%ED%95%9C%EA%B5%AD%EA%B0%80%EC%8A%A4%EA%B3%B5%EC%82%AC+%ED%8E%98%EA%B0%80%EC%88%98%EC%8A%A4+%EC%A0%95%EB%B3%B4', headers=headers)
# BASKETBALL_GAS_soup = BeautifulSoup(BASKETBALL_GAS.text, 'html.parser')
# BASKETBALL_GASs = BASKETBALL_GAS_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_GAS in BASKETBALL_GASs:
#     name = BASKETBALL_GAS.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_GAS.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_GAS.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_GAS.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASKETBALL.insert_one(doc)
#
# BASKETBALL_LG = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%B0%BD%EC%9B%90+LG+%EC%84%B8%EC%9D%B4%EC%BB%A4%EC%8A%A4+%EC%A0%95%EB%B3%B4', headers=headers)
# BASKETBALL_LG_soup = BeautifulSoup(BASKETBALL_LG.text, 'html.parser')
# BASKETBALL_LGs = BASKETBALL_LG_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_LG  in BASKETBALL_LGs:
#     name = BASKETBALL_LG.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_LG.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_LG.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_LG.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASKETBALL.insert_one(doc)
#
# BASKETBALL_KCC = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%A0%84%EC%A3%BC+KCC+%EC%9D%B4%EC%A7%80%EC%8A%A4+%EC%A0%95%EB%B3%B4', headers=headers)
# BASKETBALL_KCC_soup = BeautifulSoup(BASKETBALL_KCC.text, 'html.parser')
# BASKETBALL_KCCs = BASKETBALL_KCC_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_KCC in BASKETBALL_KCCs:
#     name = BASKETBALL_KCC.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_KCC.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_KCC.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_KCC.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASKETBALL.insert_one(doc)
#
# BASKETBALL_SAMSUNG = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%84%9C%EC%9A%B8+%EC%82%BC%EC%84%B1+%EC%8D%AC%EB%8D%94%EC%8A%A4+%EC%A0%95%EB%B3%B4', headers=headers)
# BASKETBALL_SAMSUNG_soup = BeautifulSoup(BASKETBALL_KT.text, 'html.parser')
# BASKETBALL_SAMSUNGs = BASKETBALL_SAMSUNG_soup.select('#sgrColl > div.coll_cont > div')
# for BASKETBALL_SAMSUNG in BASKETBALL_SAMSUNGs:
#     name = BASKETBALL_SAMSUNG.select_one('div.wrap_league > a').text
#     logo = BASKETBALL_SAMSUNG.select_one('div.wrap_thumb > a > img')['src']
#     rank = BASKETBALL_SAMSUNG.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = BASKETBALL_SAMSUNG.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.BASKETBALL.insert_one(doc)
#
#
# # ------------- VOLLEYBALL -------------#
#
# VOLLEYBALL_DAEHAN = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%8C%80%ED%95%9C%ED%95%AD%EA%B3%B5+%EB%B0%B0%EA%B5%AC%EB%8B%A8+%EC%A0%95%EB%B3%B4', headers=headers)
# VOLLEYBALL_DAEHAN_soup = BeautifulSoup(VOLLEYBALL_DAEHAN.text, 'html.parser')
# VOLLEYBALL_DAEHANs = VOLLEYBALL_DAEHAN_soup.select('#sgrColl > div.coll_cont > div')
# for VOLLEYBALL_DAEHAN in VOLLEYBALL_DAEHANs:
#     name = VOLLEYBALL_DAEHAN.select_one('div.wrap_league > a').text
#     logo = VOLLEYBALL_DAEHAN.select_one('div.wrap_thumb > a > img')['src']
#     rank = VOLLEYBALL_DAEHAN.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = VOLLEYBALL_DAEHAN.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.VOLLEYBALL.insert_one(doc)
#
# VOLLEYBALL_KB = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%9D%98%EC%A0%95%EB%B6%80+KB%EC%86%90%ED%95%B4%EB%B3%B4%ED%97%98+%EC%8A%A4%ED%83%80%EC%A6%88+%EB%B0%B0%EA%B5%AC%EB%8B%A8+%EC%A0%95%EB%B3%B4', headers=headers)
# VOLLEYBALL_KB_soup = BeautifulSoup(VOLLEYBALL_KB.text, 'html.parser')
# VOLLEYBALL_KBs = VOLLEYBALL_KB_soup.select('#sgrColl > div.coll_cont > div')
# for VOLLEYBALL_KB in VOLLEYBALL_KBs:
#     name = VOLLEYBALL_KB.select_one('div.wrap_league > a').text
#     logo = VOLLEYBALL_KB.select_one('div.wrap_thumb > a > img')['src']
#     rank = VOLLEYBALL_KB.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = VOLLEYBALL_KB.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.VOLLEYBALL.insert_one(doc)
#
# VOLLEYBALL_WOORI = requests.get('https://search.daum.net/search?w=tot&q=%EC%84%9C%EC%9A%B8%20%EC%9A%B0%EB%A6%AC%EC%B9%B4%EB%93%9C%20%EC%9A%B0%EB%A6%ACWON%20%ED%94%84%EB%A1%9C%EB%B0%B0%EA%B5%AC%EB%8B%A8&rtmaxcoll=SGR&DA=SGR&irt=sports-team&irk=VL-358425', headers=headers)
# VOLLEYBALL_WOORI_soup = BeautifulSoup(VOLLEYBALL_WOORI.text, 'html.parser')
# VOLLEYBALL_WOORIs = VOLLEYBALL_WOORI_soup.select('#sgrColl > div.coll_cont > div')
# for VOLLEYBALL_WOORI in VOLLEYBALL_WOORIs:
#     name = VOLLEYBALL_WOORI.select_one('div.wrap_league > a').text
#     logo = VOLLEYBALL_WOORI.select_one('div.wrap_thumb > a > img')['src']
#     rank = VOLLEYBALL_WOORI.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = VOLLEYBALL_WOORI.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.VOLLEYBALL.insert_one(doc)
#
# VOLLEYBALL_KEPKO = requests.get('https://search.daum.net/search?w=tot&q=%EC%88%98%EC%9B%90%20%ED%95%9C%EA%B5%AD%EC%A0%84%EB%A0%A5%20VIXTORM%20%ED%94%84%EB%A1%9C%EB%B0%B0%EA%B5%AC%EB%8B%A8&rtmaxcoll=SGR&DA=SGR&irt=sports-team&irk=VL-358422', headers=headers)
# VOLLEYBALL_KEPKO_soup = BeautifulSoup(VOLLEYBALL_KEPKO.text, 'html.parser')
# VOLLEYBALL_KEPKOs = VOLLEYBALL_KEPKO_soup.select('#sgrColl > div.coll_cont > div')
# for VOLLEYBALL_KEPKO in VOLLEYBALL_KEPKOs:
#     name = VOLLEYBALL_KEPKO.select_one('div.wrap_league > a').text
#     logo = VOLLEYBALL_KEPKO.select_one('div.wrap_thumb > a > img')['src']
#     rank = VOLLEYBALL_KEPKO.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = VOLLEYBALL_KEPKO.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.VOLLEYBALL.insert_one(doc)
#
# VOLLEYBALL_OK = requests.get('https://search.daum.net/search?w=tot&q=%EC%95%88%EC%82%B0%20OK%EA%B8%88%EC%9C%B5%EA%B7%B8%EB%A3%B9%20%EC%9D%8F%EB%A7%A8%20%ED%94%84%EB%A1%9C%EB%B0%B0%EA%B5%AC%EB%8B%A8&rtmaxcoll=SGR&DA=SGR&irt=sports-team&irk=VL-358424', headers=headers)
# VOLLEYBALL_OK_soup = BeautifulSoup(VOLLEYBALL_OK.text, 'html.parser')
# VOLLEYBALL_OKs = VOLLEYBALL_OK_soup.select('#sgrColl > div.coll_cont > div')
# for VOLLEYBALL_OK in VOLLEYBALL_OKs:
#     name = VOLLEYBALL_OK.select_one('div.wrap_league > a').text
#     logo = VOLLEYBALL_OK.select_one('div.wrap_thumb > a > img')['src']
#     rank = VOLLEYBALL_OK.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = VOLLEYBALL_OK.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.VOLLEYBALL.insert_one(doc)
#
#
# VOLLEYBALL_SAMSUNG = requests.get('https://search.daum.net/search?w=tot&q=%EB%8C%80%EC%A0%84%20%EC%82%BC%EC%84%B1%ED%99%94%EC%9E%AC%20%EB%B8%94%EB%A3%A8%ED%8C%A1%EC%8A%A4%20%EB%B0%B0%EA%B5%AC%EB%8B%A8&rtmaxcoll=SGR&DA=SGR&irt=sports-team&irk=VL-358419', headers=headers)
# VOLLEYBALL_SAMSUNG_soup = BeautifulSoup(VOLLEYBALL_SAMSUNG.text, 'html.parser')
# VOLLEYBALL_SAMSUNGs = VOLLEYBALL_SAMSUNG_soup.select('#sgrColl > div.coll_cont > div')
# for VOLLEYBALL_SAMSUNG in VOLLEYBALL_SAMSUNGs:
#     name = VOLLEYBALL_SAMSUNG.select_one('div.wrap_league > a').text
#     logo = VOLLEYBALL_SAMSUNG.select_one('div.wrap_thumb > a > img')['src']
#     rank = VOLLEYBALL_SAMSUNG.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = VOLLEYBALL_SAMSUNG.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.VOLLEYBALL.insert_one(doc)
#
#
# VOLLEYBALL_HYEONDAE = requests.get('https://search.daum.net/search?w=tot&q=%EC%B2%9C%EC%95%88%20%ED%98%84%EB%8C%80%EC%BA%90%ED%94%BC%ED%83%88%20%EC%8A%A4%EC%B9%B4%EC%9D%B4%EC%9B%8C%EC%BB%A4%EC%8A%A4&rtmaxcoll=SGR&DA=SGR&irt=sports-team&irk=VL-358421', headers=headers)
# VOLLEYBALL_HYEONDAE_soup = BeautifulSoup(VOLLEYBALL_HYEONDAE.text, 'html.parser')
# VOLLEYBALL_HYEONDAEs = VOLLEYBALL_HYEONDAE_soup.select('#sgrColl > div.coll_cont > div')
# for VOLLEYBALL_HYEONDAE in VOLLEYBALL_HYEONDAEs:
#     name = VOLLEYBALL_HYEONDAE.select_one('div.wrap_league > a').text
#     logo = VOLLEYBALL_HYEONDAE.select_one('div.wrap_thumb > a > img')['src']
#     rank = VOLLEYBALL_HYEONDAE.select_one('div.wrap_cont > dl:nth-child(6) > dd').text
#     home = VOLLEYBALL_HYEONDAE.select_one('div.wrap_cont > dl:nth-child(4) > dd > a:nth-child(2)').text
#
#     doc = {'name': name,'logo': logo, 'rank':rank, 'home' : home}
#     db.VOLLEYBALL.insert_one(doc)
#
