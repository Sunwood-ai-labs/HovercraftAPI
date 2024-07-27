<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/HovercraftAPI.png" width="100%">
<br>
<h1 align="center">HovercraftAPI</h1>
<h2 align="center">
  ～ Craft your story, let HovercraftAPI do the rest ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/HovercraftAPI">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/HovercraftAPI">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/HovercraftAPI">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/HovercraftAPI">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/HovercraftAPI">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/HovercraftAPI">
<a href="https://github.com/Sunwood-ai-labs/HovercraftAPI" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=HovercraftAPI&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/HovercraftAPI">
<a href="https://github.com/Sunwood-ai-labs/HovercraftAPI"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/HovercraftAPI/Sunwood-ai-labs?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/HovercraftAPI"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/HovercraftAPI"></a>
<a href="https://github.com/Sunwood-ai-labs/HovercraftAPI"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/HovercraftAPI"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/HovercraftAPI?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/HovercraftAPI?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/HovercraftAPI/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

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

