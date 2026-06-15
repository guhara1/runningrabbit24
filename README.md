# 강남 런닝래빗 가라오케 (달리는토끼) — 공식 예약 랜딩 페이지

강남 역삼동 삼정호텔에 위치한 유흥1종 정식 허가 가라오케 **런닝래빗(달리는토끼)** 의
공식 예약 안내 웹사이트입니다. 구글 SEO(검색엔진 최적화)에 맞춰 설계된 정적(static) 사이트입니다.

## 핵심 정보

| 항목 | 내용 |
| --- | --- |
| 상호 | 런닝래빗 (달리는토끼) |
| 담당 | 서부장 |
| 예약 전화 | **010-3431-0531** |
| 도로명 주소 | 서울특별시 강남구 봉은사로 150 (삼정호텔 지하 1·2층) |
| 지번 주소 | 서울특별시 강남구 역삼동 604-11번지 삼정호텔 |
| 영업 시간 | 연중무휴 18:00 ~ 익일 06:00 |

## 파일 구조

```
.
├── index.html        # 메인 랜딩 페이지 (전체 콘텐츠 + 구조화 데이터)
├── css/styles.css    # 스타일시트 (반응형 · 다크 프리미엄 테마)
├── js/script.js      # 모바일 메뉴 · 스크롤 애니메이션
├── robots.txt        # 크롤러 허용 설정
├── sitemap.xml       # 사이트맵
└── README.md
```

## SEO 최적화 적용 사항

- **시맨틱 HTML5** 구조 (`header`, `main`, `section`, `footer`)
- **메타 태그**: title, description, keywords, canonical
- **Open Graph / Twitter Card** 소셜 공유 메타데이터
- **구조화 데이터(JSON-LD)**
  - `NightClub` / LocalBusiness 스키마 — 상호·주소·전화·영업시간·좌표
  - `FAQPage` 스키마 — 자주 묻는 질문 리치 결과 노출
- **robots.txt / sitemap.xml** 제공
- 모바일 우선 **반응형 디자인** 및 접근성(skip link, aria 속성) 적용

## 사이트 구성 (메뉴)

1. 홈 (Home)
2. 런닝래빗 소개 (About) — 인사말 & 서부장 소개
3. 시스템 & 주류 안내 (System) — 이용 요금, 단체 예약, 이벤트
4. 갤러리 & 시설 (Gallery) — VIP 룸 인테리어, 업장 전경
5. 오시는 길 (Location) — 위치/지도/교통
6. 자주 묻는 질문 (FAQ)
7. 예약 및 문의 (Booking) — 서부장 직통 전화

## 로컬 미리보기

별도 빌드 과정 없이 정적 파일로 동작합니다.

```bash
# 예: 파이썬 내장 서버
python3 -m http.server 8000
# 브라우저에서 http://localhost:8000 접속
```

## 배포 안내

GitHub Pages, Netlify, Vercel, Cloudflare Pages 등 정적 호스팅에 그대로 배포 가능합니다.
배포 도메인이 확정되면 아래 항목의 URL을 실제 주소로 교체하세요.

- `index.html` 의 `<link rel="canonical">`, Open Graph `og:url`, JSON-LD `url`
- `robots.txt` 및 `sitemap.xml` 의 도메인

> 본 사이트는 만 19세 이상 성인을 위한 정식 유흥1종 허가 업소 안내 페이지입니다.
