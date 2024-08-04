from loguru import logger
from litellm import completion
from config import get_settings
import time

class LLMService:
    def __init__(self):
        self.settings = get_settings()
        self.model = self.settings.LITELLM_MODEL
        self.max_retries = 5
        self.retry_delay = 30

    def get_response(self, prompt: str) -> str:
        original_prompt = prompt
        for attempt in range(self.max_retries):
            try:
                response = completion(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                logger.error(f"LLMからのレスポンス取得中にエラーが発生しました (試行 {attempt + 1}/{self.max_retries}): {str(e)}")
                if attempt < self.max_retries - 1:
                    # プロンプトの後ろ1割を削除
                    prompt = original_prompt[:int(len(original_prompt) * 0.9)]
                    logger.info(f"プロンプトを短縮しました。新しい長さ: {len(prompt)}")
                    time.sleep(self.retry_delay)
                else:
                    raise

    def apply_diff(self, original_content: str, diff: str) -> str:
        prompt = f"""```diff
        {diff}
        ```

        上記のdiffを適用した結果を、ファイル全体の内容として出力してください。
        ファイルの内容:
        ```
        {original_content}
        ```"""
        
        return self.get_response(prompt)

    def analyze_issue(self, issue_title: str, issue_body: str, existing_labels: list) -> str:
        prompt = f"""
        以下のGitHubイシューを分析し、適切なラベルを提案してください：

        タイトル: {issue_title}

        本文:
        {issue_body}

        既存のラベルのリスト:
        {', '.join(existing_labels)}

        上記の既存のラベルのリストから、このイシューに最も適切なラベルを最大3つ選んでください。
        選んだラベルをカンマ区切りで提案してください。既存のラベルにない新しいラベルは提案しないでください。
        
        回答は以下の形式でラベルのみを提供してください：
        label1, label2, label3
        """
        return self.get_response(prompt)
