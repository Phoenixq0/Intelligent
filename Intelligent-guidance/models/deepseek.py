import os
import requests
from dotenv import load_dotenv

# set DEEPSEEK_API_KEY=sk-5acc66c0cfa74293a3af73e0636d2cb5

load_dotenv()


class DeepSeekAPI:
    def __init__(self):
        self.api_key = 'sk-5acc66c0cfa74293a3af73e0636d2cb5'
        self.base_url = "https://api.deepseek.com/v1"

    def get_advice(self, symptom):
        """
        获取DeepSeek的补充建议
        :param symptom: 用户症状描述
        :return: DeepSeek生成的建议文本
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": f"作为眼科专家，请给出针对以下症状的初步建议：{symptom}"}
            ],
            "temperature": 0.7
        }

        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"DeepSeek API Error: {str(e)}")
            return "当前无法获取专家建议，请稍后再试"
