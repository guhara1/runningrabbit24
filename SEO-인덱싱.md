# choilove21.com 최속 색인 가이드

도메인 변경(`runningrabbit24.com` → `choilove21.com`) 후, 새 도메인을 **가장 빠르게** 색인시키는 절차입니다.
저장소에서 자동화한 부분과, 각 검색엔진 콘솔에서 한 번만 해주면 되는 부분으로 나뉩니다.

---

## 0. 배포 먼저 확인 (필수)

아래 URL들이 브라우저에서 열려야 색인 요청이 통과합니다.

- https://choilove21.com/sitemap.xml
- https://choilove21.com/rss.xml
- https://choilove21.com/robots.txt
- https://choilove21.com/c7d2a91e6b4f80351da9e3c7b0f6284a.txt  ← IndexNow 키
- https://choilove21.com/google7cb5bedbb9af927c.html  ← 구글 인증
- https://choilove21.com/naver82e7d8c96600f8ee945bb984b9f63154.html  ← 네이버 인증

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

https://searchadvisor.naver.com → 사이트 등록 `choilove21.com`

1. **사이트 소유확인**: `naver82e7d8c96600f8ee945bb984b9f63154.html` 파일 방식으로 확인.
2. **요청 → 사이트맵 제출**: `https://choilove21.com/sitemap.xml`
3. **요청 → RSS 제출**: `https://choilove21.com/rss.xml`  (네이버는 RSS를 빠른 수집 채널로 활용)
4. **웹페이지 수집**: 메인 URL을 직접 넣어 수집 요청.

## 3. 구글 서치콘솔 (한 번만) — 구글은 IndexNow 미지원

https://search.google.com/search-console → 속성 추가 `https://choilove21.com/`

1. **소유확인**: `google7cb5bedbb9af927c.html` 파일 방식으로 확인.
2. **색인 → Sitemaps**: `sitemap.xml` 제출.
3. **URL 검사**: 메인 및 주요 페이지 URL을 검사 → **색인 생성 요청**(가장 빠른 단건 색인).
4. (도메인 이전이라면) 구 도메인 속성에서 **주소 변경 도구** 사용 시 평판 이전이 빨라집니다.

---

## 저장소에서 이미 최적화된 항목

| 파일 | 최적화 내용 |
|------|-------------|
| `robots.txt` | 전 검색봇 전체 허용 + sitemap·rss 등록 (Googlebot / Yeti / Daum / bingbot 명시) |
| `sitemap.xml` | 19개 URL, `lastmod` 최신일(2026-07-08), 페이지별 `changefreq`/`priority` |
| `rss.xml` | 네이버 서치어드바이저 제출용 피드, `pubDate`/`lastBuildDate` 최신화 |
| `*.txt` (IndexNow 키) | 네이버·빙 즉시 색인 소유권 검증 파일 |
| 인증 파일 2종 | 구글·네이버 사이트 소유확인 |

> 콘텐츠 변경 시: `python3 generate.py`로 사이트맵·RSS 재생성(날짜는 `generate.py`의 `BUILD` 상수) → `python3 tools/indexnow.py`로 재제출.
