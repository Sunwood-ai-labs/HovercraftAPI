# HovercraftAPI 使用ガイド

## 目次

1. [はじめに](#はじめに)
2. [インストール](#インストール)
3. [基本的な使用方法](#基本的な使用方法)
4. [コマンドラインオプション](#コマンドラインオプション)
5. [高度な機能](#高度な機能)
6. [カスタマイズ](#カスタマイズ)
7. [トラブルシューティング](#トラブルシューティング)

## はじめに

HovercraftAPIは、Markdownファイルから印象的なHovercraftプレゼンテーションを簡単に作成するためのPythonツールです。このガイドでは、HovercraftAPIの詳細な使用方法と各機能について説明します。

## インストール

HovercraftAPIは、pip を使用して簡単にインストールできます：

```bash
pip install hovercraft-api
```

## 基本的な使用方法

HovercraftAPIの基本的な使用方法は以下の通りです：

```bash
hovercraftapi your_markdown_file.md
```

これにより、指定されたMarkdownファイルからHovercraftプレゼンテーションが生成されます。

## コマンドラインオプション

HovercraftAPIは、多くのコマンドラインオプションをサポートしています。以下に主なオプションを説明します：

### 入力ファイルと出力設定

- `markdown_file`: 入力Markdownファイル（必須）
- `-c`, `--css`: カスタムCSSファイル（デフォルト: "css/mytheme.css"）
- `--svg-css-file`: SVG用のカスタムCSSファイル（デフォルト: "css/svg_oasis.css"）
- `--js-file`: カスタムJavaScriptファイル（デフォルト: "js/impress.js"）

### モデル設定

- `--model-name`: 使用するLLMモデル名（デフォルト: "gemini/gemini-1.5-pro-latest"）

### グリッドとスライドのサイズ設定

- `--grid-width`: グリッドの幅（デフォルト: 6000）
- `--grid-height`: グリッドの高さ（デフォルト: 6000）
- `--grid-depth`: グリッドの奥行き（デフォルト: 6000）
- `--slide-width`: スライドの幅（デフォルト: 1000）
- `--slide-height`: スライドの高さ（デフォルト: 750）
- `--slide-depth`: スライドの奥行き（デフォルト: 1000）

### 3Dダイナミックトランジションのオプション

- `--enable-dynamic-position`: 動的なスライド位置を有効にする
- `--use-rotate-x`: X軸回転を有効にする
- `--use-rotate-y`: Y軸回転を有効にする
- `--use-rotate-z`: Z軸回転を有効にする

### スライドキャプチャのオプション

- `--capture-images`: スライドを画像としてキャプチャする
- `--capture-video`: スライドを動画としてキャプチャする
- `--capture-fps`: 動画キャプチャ時のフレームレート（デフォルト: 30）
- `--capture-duration`: 動画キャプチャ時の各スライドのキャプチャ時間（秒）（デフォルト: 5）
- `--html-file`: キャプチャするHTMLファイル名（デフォルト: "index_with_svg.html"）

### 実行ステージの選択

- `--stages`: 実行するステージを選択（複数選択可能）
  - 選択肢: 'all', 'md_to_slides', 'md_to_rst', 'rst_to_hovercraft', 'hovercraft_to_html', 'mermaid_fusion', 'codeblock_transmute', 'mermaid_to_svg', 'capture_slides'
  - デフォルト: ['all']

## 高度な機能

### 3Dダイナミックトランジション

3Dダイナミックトランジションを有効にするには、`--enable-dynamic-position` オプションを使用します：

```bash
hovercraftapi your_markdown_file.md --enable-dynamic-position
```

これにより、スライド間のトランジションが3D空間で動的に行われます。

### MermaidダイアグラムのSVG変換

MermaidダイアグラムをSVGに変換するには、`mermaid_to_svg` ステージを指定します：

```bash
hovercraftapi your_markdown_file.md --stages mermaid_to_svg
```

### スライドのキャプチャと動画生成

スライドを画像や動画としてキャプチャするには、以下のオプションを使用します：

```bash
hovercraftapi your_markdown_file.md --stages capture_slides --capture-images --capture-video
```

## カスタマイズ

### カスタムCSSの使用

プレゼンテーションのスタイルをカスタマイズするには、独自のCSSファイルを指定できます：

```bash
hovercraftapi your_markdown_file.md -c path/to/your/custom.css
```

### SVG用のカスタムCSS

SVGのスタイルをカスタマイズするには、SVG用のCSSファイルを指定できます：

```bash
hovercraftapi your_markdown_file.md --svg-css-file path/to/your/svg_custom.css
```

## トラブルシューティング

### よくある問題と解決方法

1. **Mermaidダイアグラムが表示されない**
   - Mermaid.jsが正しく読み込まれているか確認してください。
   - ブラウザのコンソールでエラーメッセージを確認してください。

2. **3Dダイナミックトランジションが機能しない**
   - `--enable-dynamic-position` オプションが指定されているか確認してください。
   - グリッドサイズとスライドサイズの設定を確認してください。

3. **スライドのキャプチャに失敗する**
   - Seleniumのドライバーが正しくインストールされているか確認してください。
   - ブラウザのバージョンとSeleniumドライバーのバージョンが一致しているか確認してください。

問題が解決しない場合は、GitHubのissueを開いてサポートを求めてください。

---

このガイドでは、HovercraftAPIの主な機能と使用方法を説明しました。さらに詳細な情報や最新の更新については、[公式ドキュメント](https://github.com/Sunwood-ai-labs/HovercraftAPI)を参照してください。
