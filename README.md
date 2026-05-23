<img width="300" alt="ポータルトップ画像" src="https://github.com/user-attachments/assets/faa8f338-b186-44e9-910c-43a8a3b4b40e" />


# ゆるっとマイペースに推しごとチュウ ポータルサイト

ブログ「ゆるっとマイペースに推しごとチュウ」の記事を、カテゴリ別に見やすく整理するために制作したポータルサイトです。  
はてなブログのRSSを取得し、最新記事をカード形式で一覧表示できるようにしています。

公開URL  
[https://naru08-creator.github.io/narunikki_portal/](https://naru08-creator.github.io/narunikki_portal/)

## 概要

このサイトは、ブログ本体の記事導線を分かりやすくし、旅行・推し活・ゲームなどのテーマごとに記事へアクセスしやすくすることを目的に作成しました。  
シンプルな静的構成で、GitHub Pages 上で公開しています。

## 主な機能

- はてなブログのRSSを取得して最新記事を自動表示
- 「最新記事」「旅行」「推し活」「ゲーム」のカテゴリ切り替え
- 人気記事や固定記事、PRカードの差し込み表示
- 画像未設定記事で `NoImage.png` を表示するフォールバック処理
- スマホ・PCの両方を意識したレスポンシブレイアウト

## 使用技術

- HTML
- CSS
- JavaScript
- GitHub Pages
- RSS2JSON API

## 工夫したポイント

- ブログ記事をそのまま並べるのではなく、カードUIで視認性を上げたこと
- カテゴリごとに雰囲気が伝わる配色を分けたこと
- RSS側の画像データの揺れに対応し、画像未設定時でも見た目が崩れないようにしたこと
- 外部サービスを使いながらも、フロントエンドのみで完結する構成にしたこと

## 今後の改善案

- 表示対象記事の絞り込み精度向上
- デザインの微調整とアクセシビリティ改善
- 記事カードの並び順や差し込みロジックの最適化
- 運用しやすい更新フローの整理

## 制作背景

自分のブログ記事が増える中で、読者がカテゴリ別に記事を探しやすい入口を作りたいと考え、このポータルサイトを制作しました。  
見た目の親しみやすさと、個人運用でも更新しやすい仕組みの両立を意識しています。

---

# Yurutto My Pace Oshi-goto Chu Portal Site

This is a portal site created to organize and showcase articles from the blog "Yurutto My Pace Oshi-goto Chu" in a more accessible way.  
It fetches the blog RSS feed and displays the latest posts in a card-based layout.

Live URL  
[https://naru08-creator.github.io/narunikki_portal/](https://naru08-creator.github.io/narunikki_portal/)

## Overview

This site was built to make blog content easier to browse by category, helping readers quickly find posts related to travel, fandom activities, and games.  
It is a lightweight static site published on GitHub Pages.

## Key Features

- Automatically fetches and displays the latest posts from a Hatena Blog RSS feed
- Category switching for Latest Posts, Travel, Fandom, and Games
- Inserts featured articles, fixed articles, and promotional cards into the feed
- Fallback image handling with `NoImage.png` for posts without a proper thumbnail
- Responsive layout for both mobile and desktop users

## Tech Stack

- HTML
- CSS
- JavaScript
- GitHub Pages
- RSS2JSON API

## Highlights

- Improved readability by converting blog entries into a card-based UI
- Used category-based color design to create a more intuitive browsing experience
- Added image fallback logic to handle inconsistent RSS image data gracefully
- Built a front-end-only structure that is easy to maintain for personal use

## Future Improvements

- Improve filtering accuracy for displayed articles
- Refine the design and accessibility
- Optimize article ordering and insertion logic
- Streamline the update and publishing workflow

## Background

As the number of blog posts increased, I wanted to create a clearer entry point where readers could find content by category more easily.  
This project was designed with both friendliness and maintainability in mind for ongoing personal operation.
