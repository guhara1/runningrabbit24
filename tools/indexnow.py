#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IndexNow 즉시 색인 제출기 — 네이버·빙·얀덱스에 sitemap.xml의 모든 URL을 한 번에 통보.

사용법 (도메인 연결 + 배포가 끝난 뒤 실행):
    python3 tools/indexnow.py

동작:
  1. 같은 저장소의 sitemap.xml 에서 <loc> URL을 모두 읽는다.
  2. IndexNow 엔드포인트(api.indexnow.org)로 JSON POST → 참여 검색엔진(네이버·빙·얀덱스)에 즉시 전파.
  3. 키 소유권은 루트의 {KEY}.txt 파일로 검증되므로, 배포 후에만 정상 동작한다.

주의: 구글은 IndexNow 미참여. 구글은 Search Console 사이트맵 제출 + URL 검사로 색인 요청.
"""
import json
import os
import re
import sys
import urllib.request

HOST = ""  # 도메인 미연결. 재연결 시 예: "example.com"
KEY = "c7d2a91e6b4f80351da9e3c7b0f6284a"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"


def read_sitemap_urls():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(here, "sitemap.xml"), encoding="utf-8") as f:
        xml = f.read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def submit(urls):
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def main():
    if not HOST:
        print("도메인 미연결 상태입니다. HOST 를 설정한 뒤 실행하세요.", file=sys.stderr)
        sys.exit(1)
    urls = read_sitemap_urls()
    if not urls:
        print("sitemap.xml 에서 URL을 찾지 못했습니다.", file=sys.stderr)
        sys.exit(1)
    print(f"제출 대상 {len(urls)}개 URL:")
    for u in urls:
        print(f"  - {u}")
    print(f"\nIndexNow 제출 → {ENDPOINT}")
    try:
        status, body = submit(urls)
    except Exception as e:  # noqa: BLE001
        print(f"제출 실패: {e}", file=sys.stderr)
        print("배포 완료 후(키 파일이 공개 서빙된 뒤) 다시 실행하세요.", file=sys.stderr)
        sys.exit(1)
    print(f"응답 상태: {status}")
    if body.strip():
        print(f"응답 본문: {body}")
    # IndexNow 정상 접수 = 200 또는 202
    if status in (200, 202):
        print("접수 완료. 네이버·빙·얀덱스에 색인 요청이 전파됩니다.")
    else:
        print("접수 상태를 확인하세요 (403=키 검증 실패, 422=URL/호스트 불일치).")


if __name__ == "__main__":
    main()
