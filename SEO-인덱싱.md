# aetherbest118.com 최속 색인 가이드

신규 도메인 `aetherbest118.com` 연결 후, 가장 빠르게 색인시키는 절차입니다.
저장소에서 자동화한 부분과, 각 검색엔진 콘솔에서 한 번만 해주면 되는 부분으로 나뉩니다.

---

## 소유확인 현황

| 검색엔진 | 방식 | 상태 |
|---|---|---|
| 구글 | `index.html`의 `google-site-verification` 메타 태그 | ✅ **신규 도메인용으로 등록 완료** |
| 네이버 | 루트의 `naver82e7d8c96600f8ee945bb984b9f63154.html` | ⚠️ **재발급 필요** |

### 구글 — 완료

메인페이지 `<head>`에 메타 태그가 들어 있습니다. 구글은 **메인페이지에만** 있으면
인증되므로 하위 페이지에는 넣지 않습니다.

```html
<meta name="google-site-verification" content="-u4-g1WyWAhQskpsajJ8JDJO8gvEAhjusGq59XqOfhs" />
```

> 인증 후에도 **절대 지우지 마십시오.** 태그가 사라지면 소유확인이 해제되어
> 서치콘솔 데이터 접근이 끊깁니다.

구 도메인용 파일 `google7cb5bedbb9af927c.html`은 이제 쓰이지 않습니다. 남겨 둬도
무해하지만 정리하셔도 됩니다.

### 네이버 — 재발급 필요

`naver82e7d8c96600f8ee945bb984b9f63154.html`은 **이전 도메인(choilove21.com)
속성에서 발급된 토큰**이라 신규 도메인에서는 인증되지 않습니다. 서치어드바이저에서
`aetherbest118.com`을 새 속성으로 추가하고, 새로 받은 파일을 루트에 올린 뒤
구 파일을 지우십시오.

`IndexNow` 키(`c7d2a91e6b4f80351da9e3c7b0f6284a.txt`)는 도메인에 종속되지 않으므로
그대로 재사용 가능합니다. 새 도메인 루트에서 서빙되기만 하면 됩니다.

---

## 0. 배포 먼저 확인 (필수)

아래 URL들이 브라우저에서 열려야 색인 요청이 통과합니다.

- https://aetherbest118.com/sitemap.xml
- https://aetherbest118.com/rss.xml
- https://aetherbest118.com/robots.txt
- https://aetherbest118.com/c7d2a91e6b4f80351da9e3c7b0f6284a.txt ← IndexNow 키
- 신규 발급받은 네이버 인증 파일

구글은 파일이 아니라 메인페이지 메타 태그로 인증하므로 별도 URL 확인이 필요 없습니다.

---

## 1. 네이버 · 빙 — IndexNow 즉시 제출 (자동)

배포가 끝나면 저장소 루트에서 한 줄이면 끝납니다.

```bash
python3 tools/indexnow.py
```

- `sitemap.xml`의 **19개 URL 전체**를 IndexNow로 한 번에 통보 → 네이버·빙·얀덱스에 즉시 전파.
- 콘텐츠를 수정할 때마다 재실행하면 그때그때 재색인 요청됩니다.
- 응답 200/202 = 접수 완료. 403 = 키 파일 미배포, 422 = 호스트/URL 불일치.

## 2. 네이버 서치어드바이저 (한 번만)

https://searchadvisor.naver.com → 사이트 등록 `aetherbest118.com`

1. **사이트 소유확인**: 신규 발급 HTML 파일 방식으로 확인.
2. **요청 → 사이트맵 제출**: `https://aetherbest118.com/sitemap.xml`
3. **요청 → RSS 제출**: `https://aetherbest118.com/rss.xml` (네이버는 RSS를 빠른 수집 채널로 활용)
4. **웹페이지 수집**: 메인 URL을 직접 넣어 수집 요청.

## 3. 구글 서치콘솔 (한 번만) — 구글은 IndexNow 미지원

https://search.google.com/search-console → 속성 추가 `https://aetherbest118.com/`

1. **소유확인**: 이미 메인페이지 메타 태그로 등록 완료 — 서치콘솔에서 `HTML 태그` 방식 선택 후 확인 누르면 됩니다.
2. **색인 → Sitemaps**: `sitemap.xml` 제출.
3. **URL 검사**: 메인 및 주요 페이지 URL을 검사 → **색인 생성 요청**(가장 빠른 단건 색인).

---

## 저장소에서 이미 최적화된 항목

| 파일 | 최적화 내용 |
|------|-------------|
| `robots.txt` | 전 검색봇 전체 허용 + sitemap·rss 등록 (Googlebot / Yeti / Daum / bingbot 명시) |
| `sitemap.xml` | 19개 URL, `lastmod` 최신일(2026-08-06), 페이지별 `changefreq`/`priority` |
| `rss.xml` | 네이버 서치어드바이저 제출용 피드, `pubDate`/`lastBuildDate` 최신화 |
| `*.txt` (IndexNow 키) | 네이버·빙 즉시 색인 소유권 검증 파일 |

> 콘텐츠 변경 시: `python3 generate.py`로 사이트맵·RSS 재생성(날짜는 `generate.py`의 `BUILD` 상수) → `python3 tools/indexnow.py`로 재제출.

---

## 도메인을 다시 바꾸거나 해제할 때

`generate.py`의 `DOMAIN` 한 줄이 기준점입니다.

```python
DOMAIN = "https://aetherbest118.com"   # 빈 값 "" 이면 도메인 미연결 모드
```

빈 값으로 두고 `python3 generate.py`를 실행하면 canonical·`og:url`·JSON-LD가
상대경로로 바뀌고, 절대 URL이 필요한 `sitemap.xml`·`rss.xml`·IndexNow 키는
생성되지 않습니다. `index.html`·`robots.txt`·`tools/indexnow.py`는 수동 관리
파일이라 별도 수정이 필요합니다.
