# 도메인 · 색인 가이드

현재 저장소는 **도메인 미연결 상태**입니다. 기존 도메인 연결을 해제했고,
검색엔진에서 기존 색인이 사라진 뒤 도메인을 다시 연결할 예정입니다.

---

## 현재 상태

| 항목 | 상태 |
|------|------|
| `generate.py`의 `DOMAIN` | `""` (빈 값) |
| canonical · `og:url` · JSON-LD `url`/`@id` | 상대경로 (`/`, `/about/`, `/#business`) |
| `sitemap.xml` · `rss.xml` | **생성 안 함** (절대 URL 필요) |
| IndexNow 키 파일 | **생성 안 함** |
| `robots.txt` | `Allow: /` 유지, `Sitemap:` 라인 제거 |
| `tools/indexnow.py` | `HOST=""` — 실행 시 안내 후 종료 |
| 구글 · 네이버 인증 파일 | **유지** (아래 참고) |

---

## 색인이 사라지는 조건 — 저장소 변경으로는 안 됩니다

이 저장소에서 도메인 참조를 지운 것과 **검색엔진 색인 삭제는 별개**입니다.
구글이 URL을 색인에서 내리는 실제 조건은 다음과 같습니다.

1. 해당 URL이 더 이상 응답하지 않거나 `404`/`410`을 반환 → 재크롤 시 색인에서 제거
2. `noindex` 메타를 붙인 페이지를 크롤하게 함
3. 서치콘솔 **삭제(Removals)** 도구로 요청 (임시, 약 6개월)

도메인 연결을 끊어 두면 1번이 자연히 충족되지만, 재크롤 주기에 따라
**수 주에서 수 개월**이 걸립니다. 가장 빠른 것은 3번입니다.

### 주의 1 — `robots.txt`로 차단하면 오히려 느려집니다

`Disallow: /`로 막으면 크롤러가 페이지가 사라진 사실을 **확인하지 못해**
기존 색인이 더 오래 남습니다. 그래서 `robots.txt`는 `Allow: /`를 유지했습니다.

### 주의 2 — 인증 파일은 지우지 않았습니다

`google7cb5bedbb9af927c.html`, `naver82e7d8c96600f8ee945bb984b9f63154.html`은
도메인 문자열을 담고 있지 않은 소유확인 토큰 파일입니다. 이 파일들이 있어야

- 지금: 서치콘솔에서 **삭제 요청**을 넣을 수 있고
- 나중: 도메인 재연결 시 **재인증 없이** 바로 쓸 수 있습니다

지우면 두 가지 다 못 하게 되므로 유지했습니다.

---

## 도메인을 다시 연결할 때

1. `generate.py`의 `DOMAIN`에 새 도메인을 넣습니다.

   ```python
   DOMAIN = "https://예시.com"
   ```

2. 재생성하면 `sitemap.xml` · `rss.xml` · IndexNow 키 파일이 다시 만들어지고,
   canonical · `og:url` · JSON-LD도 절대 URL로 돌아옵니다.

   ```bash
   python3 generate.py
   ```

3. `index.html`은 수동 관리 파일이라 canonical · `og:url` · `og:image` ·
   JSON-LD `url`/`@id`를 직접 절대 URL로 되돌려야 합니다.

4. `robots.txt` 하단에 `Sitemap:` 두 줄을 다시 추가합니다.

   ```
   Sitemap: https://예시.com/sitemap.xml
   Sitemap: https://예시.com/rss.xml
   ```

5. `tools/indexnow.py`의 `HOST`를 새 도메인으로 설정합니다.

6. 배포 후 색인 요청

   ```bash
   python3 tools/indexnow.py    # 네이버 · 빙 · 얀덱스 즉시 통보
   ```

   구글은 IndexNow 미지원 → 서치콘솔에서 사이트맵 제출 + URL 검사로 색인 요청.

---

## 참고 — 배포 후 열려야 하는 URL (도메인 재연결 시)

- `/sitemap.xml`
- `/rss.xml`
- `/robots.txt`
- `/c7d2a91e6b4f80351da9e3c7b0f6284a.txt` ← IndexNow 키
- `/google7cb5bedbb9af927c.html` ← 구글 인증
- `/naver82e7d8c96600f8ee945bb984b9f63154.html` ← 네이버 인증
