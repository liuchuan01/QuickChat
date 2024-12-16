import aiohttp
import json
import requests

def stream_response(question, key, model):
    url = "https://yunwu.ai/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": True
    }
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload),stream=True)

    for chunk in response.iter_lines():
        # 解码为字符串，明确指定 UTF-8
        chunk_str = chunk.decode('utf-8', errors='replace')  # 将无法解码的字符替换为特殊字符
        if chunk_str.strip():
            if chunk_str == '[DONE]':
                break
            if chunk_str.startswith("data: "):
                chunk_str = chunk_str[len("data: "):]  # 去掉前缀
            try:
                data = json.loads(chunk_str)
                if data['choices'][0].get('delta') and data['choices'][0]['delta'].get('content'):
                    yield data['choices'][0]['delta']['content']
            except json.JSONDecodeError:
                continue


async def async_stream_response(question,key,model):

    url = "https://yunwu.ai/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": True
    }
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            async for chunk in response.content.iter_any():
                # 解码为字符串，明确指定 UTF-8
                chunk_str = chunk.decode('utf-8', errors='replace')  # 将无法解码的字符替换为特殊字符
                if chunk_str.strip():
                    if chunk_str == '[DONE]':
                        break
                    if chunk_str.startswith("data: "):
                        chunk_str = chunk_str[len("data: "):]  # 去掉前缀
                    try:
                        data = json.loads(chunk_str)
                        if data['choices'][0].get('delta') and data['choices'][0]['delta'].get('content'):
                            yield data['choices'][0]['delta']['content']
                    except json.JSONDecodeError:
                        continue

# 使用示例
if __name__ == "__main__":
    key = "key"
    question = "介绍自己"
    for chunk in stream_response(question, key, "claude-3-haiku-20240307"):
        print(chunk, flush=True)



