#!/usr/bin/env python3
"""Fetch Hatena and note RSS feeds and write a browser-friendly JSON file."""
import json
import os
import re
import html
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

FEEDS = {
    "hatena": "https://narunikki.hatenablog.com/rss",
    "note": "https://note.com/naru08_creator/rss",
}
OUT = Path("articles.json")
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "media": "http://search.yahoo.com/mrss/",
    "atom": "http://www.w3.org/2005/Atom",
}

def text_of(el, paths):
    for path in paths:
        found = el.find(path, NS)
        if found is not None and found.text:
            return found.text.strip()
    return ""

def parse_feed(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; GitHubActionsRSS/1.0)"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)
    entries = root.findall(".//item") or root.findall(".//atom:entry", NS)
    items = []
    for entry in entries:
        title = text_of(entry, ["title", "atom:title"])
        link = text_of(entry, ["link", "atom:link"])
        if not link:
            link_el = entry.find("atom:link", NS)
            if link_el is not None:
                link = link_el.attrib.get("href", "")
        categories = []
        for category in entry.findall("category") + entry.findall("atom:category", NS):
            value = (category.text or category.attrib.get("term", "")).strip()
            if value and value not in categories:
                categories.append(value)

        enclosure = entry.find("enclosure")
        enclosure_url = enclosure.attrib.get("url", "") if enclosure is not None else ""
        thumbnail = text_of(entry, ["media:thumbnail", "media:content"])
        if not thumbnail:
            media = entry.find("media:thumbnail", NS) or entry.find("media:content", NS)
            if media is not None:
                thumbnail = media.attrib.get("url", "")
        description = text_of(entry, ["description", "summary", "atom:summary"])
        content = text_of(entry, ["content:encoded", "content", "atom:content"])
        if not thumbnail:
            image_source = description or content
            match = re.search(r'<img[^>]+src=[\"\\\']([^\"\\\']+)', html.unescape(image_source), re.IGNORECASE)
            if match:
                thumbnail = match.group(1)
        items.append({
            "title": title,
            "link": link,
            "categories": categories,
            "thumbnail": thumbnail,
            "enclosure": {"link": enclosure_url} if enclosure_url else {},
            "description": description,
            "content": content,
        })
    return items

def main():
    data = {}
    for name, url in FEEDS.items():
        print(f"Fetching {name}: {url}")
        data[name] = parse_feed(url)
        print(f"  got {len(data[name])} items")
        if not data[name]:
            raise RuntimeError(f"{name} feed returned zero items; refusing to overwrite JSON")
    data["updated_at"] = datetime.now(timezone.utc).isoformat()
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
