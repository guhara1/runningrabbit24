# 강남 일프로 에테르 — 공식 예약 랜딩 페이지

강남 역삼동 차병원사거리에 위치한 유흥1종 정식 허가 일프로 **에테르** 의
공식 예약 안내 웹사이트입니다. 구글 SEO(검색엔진 최적화)에 맞춰 설계된 정적(static) 사이트입니다.

## 핵심 정보

| 항목 | 내용 |
| --- | --- |
| 상호 | 에테르 |
| 담당 | 서부장 |
| 예약 전화 | **010-3431-0531** |
| 도로명 주소 | 서울특별시 강남구 봉은사로 150 (차병원사거리 지하 1·2층) |
| 지번 주소 | 서울특별시 강남구 역삼동 604-11번지 차병원사거리 |
| 영업 시간 | 연중무휴 24시간 영업 |

## 파일 구조

```
.
├── index.html             # 홈 (메인 랜딩 + 전체 구조화 데이터)
├── about/
│   ├── index.html         # 에테르 소개
│   └── greeting.html      # 인사말 & 서부장 소개
├── system/
│   ├── index.html         # 시스템 & 주류 안내
│   ├── price.html         # 이용 요금 & 세트
│   ├── business.html      # 단체 & 비즈니스 미팅
│   └── party.html         # 생일파티 & 회식 이벤트
├── gallery/
│   ├── index.html         # 갤러리 & 시설
│   ├── vip-room.html      # VIP 룸 인테리어
│   └── interior.html      # 업장 전경 (지하 1·2층)
├── location/index.html    # 오시는 길 · 지역 (지역별 안내 허브)
├── area/                   # 지역 롱테일 페이지 (내부링크 강화)
│   ├── yeoksam.html        # 역삼역 일프로
│   ├── gangnam-station.html# 강남역 일프로
│   ├── sinnonhyeon.html    # 신논현역 일프로
│   ├── eonju.html          # 언주역 일프로
│   └── seolleung.html      # 선릉역 일프로
├── reviews/index.html      # 고객 후기 & 평점 (Review · AggregateRating)
├── booking/
│   ├── index.html         # 예약 & 문의
│   └── faq.html           # 자주 묻는 질문
├── css/styles.css         # 스타일시트 (드롭다운 네비 · 반응형 · 서브페이지 레이아웃)
├── js/script.js           # 모바일 메뉴 · 스크롤 애니메이션
├── assets/                # 파비콘 · OG 이미지
├── generate.py            # 서브페이지 정적 생성기 (공유 헤더/네비/푸터)
├── robots.txt, sitemap.xml, site.webmanifest
└── README.md
```

> **페이지 수정 시:** 모든 하위 페이지는 `generate.py` 로 생성됩니다. 네비게이션/푸터/콘텐츠를
> 바꾼 뒤 `python3 generate.py` 를 실행하면 12개 하위 페이지가 일괄 갱신됩니다.
> (홈 `index.html` 의 헤더/푸터도 동일한 마크업으로 맞춰져 있으니 함께 수정하세요.)

## SEO 최적화 적용 사항

- **개별 페이지 구조** — 모든 메뉴·하위메뉴가 독립 URL을 가진 별도 페이지 (앵커 링크 아님)
- **계층형 드롭다운 네비게이션** + 페이지별 **브레드크럼**(BreadcrumbList 스키마)
- **페이지별 고유 콘텐츠 2,000~2,500자** (중복·도어웨이 회피, 주제별 차별화)
- **시맨틱 HTML5** 구조 (`header`, `main`, `nav`, `article`, `footer`)
- **페이지별 메타 태그**: title, description, canonical (전부 개별 지정)
- **Open Graph / Twitter Card** + 선호 이미지(og:image, 1200×630)
- **구조화 데이터(JSON-LD) — 전 페이지 공통 + 페이지별**
  - `NightClub` / LocalBusiness — 상호·별칭(해피해피)·주소·전화·영업시간·좌표·`areaServed` (전 페이지 공통)
  - `AggregateRating` + `Review` — 평점(4.9)·후기 데이터 (전 페이지 공통, 후기 페이지에 전체 노출)
  - `BreadcrumbList` — 전 하위 페이지
  - `FAQPage` — 자주 묻는 질문 (리치 결과)
  - `Person` — 서부장 (E-E-A-T 작성자), `WebPage` — 작성·갱신 일자
- **지역 롱테일 페이지 + 상호 내부링크** — 역삼·강남역·신논현·언주·선릉 (관련 페이지 카드로 교차 연결)
- **robots.txt / sitemap.xml / site.webmanifest** 제공
- 모바일 우선 **반응형 디자인** 및 접근성(skip link, aria 속성)

## 사이트 구성 (메뉴 / 하위메뉴)

- **홈**
- **소개** → 에테르 소개 · 인사말 & 서부장 소개 · 고객 후기 & 평점
- **시스템 & 주류** → 시스템 안내 · 이용 요금 & 세트 · 단체 & 비즈니스 미팅 · 생일파티 & 회식 이벤트
- **갤러리 & 시설** → 갤러리 & 시설 · VIP 룸 인테리어 · 업장 전경 (지하 1·2층)
- **오시는 길 · 지역** → 오시는 길 · 지도 · 역삼역 · 강남역 · 신논현역 · 언주역 · 선릉역 일프로
- **예약 & 문의** → 예약 & 문의 · 자주 묻는 질문(FAQ)

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
