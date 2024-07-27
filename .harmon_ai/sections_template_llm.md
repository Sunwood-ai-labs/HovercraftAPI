## 🌟 HovercraftAPI

HovercraftAPIは、Markdownファイルから印象的なHovercraftプレゼンテーションを簡単に作成するためのPythonツールです。

## 🎥 デモ

(デモ動画やGIFがあればここに挿入)

## 🚀 はじめに

### インストール

```bash
pip install hovercraft-api
```

## 📝 HovercraftAPIの使い方

### コマンドラインインターフェース

```bash
hovercraftapi your_markdown_file.md -c path/to/your/custom.css
```

### Pythonスクリプト内での使用

```python
from hovercraft_api import HovercraftAPI

api = HovercraftAPI("your_markdown_file.md", css_file="path/to/your/custom.css")
api.generate_slides()
```

## 特徴

* Markdownからスライドを生成
* Mermaidダイアグラムとコードブロックをサポート
* カスタムCSSによるスタイリング
* CLIインターフェース対応

## 必要条件

* Python 3.7以上
* Hovercraft
* その他の依存関係は `requirements.txt` を参照してください。

## カスタムCSS

デフォルトのCSSファイルは `css/mytheme.css` です。カスタムCSSファイルを使用する場合は、`-c` または `--css` オプションで指定してください。

## Markdownファイルの構造

HovercraftAPIは以下の構造のMarkdownファイルをサポートしています:

(具体的なMarkdownファイルの構造についての記述は原文にないため、省略) 

## 🤝 貢献

プルリクエストは大歓迎です。大きな変更の場合は、まずissueを開いて議論してください。

## 🙏 サポート

問題が発生した場合は、GitHubのissueを開いてください。 

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。 
