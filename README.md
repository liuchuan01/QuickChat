# QUICK-CHAT

## 介绍

这是一个**Streamlit应用**，允许我们调用云雾平台的API去访问模型

>由于目前OpenAI持续不给力（4o的指令遵从能力变得好差呀）
> 
> Claude作为后期之秀，真的很棒！但是免费的次数太少啦~

链接：[云雾API](https://yunwu.ai/register?aff=ZDXj)

这个平台也就是API中转，好处就是能在国内自由的访问各类先进模型。并且其内部通过各种手段能拿到低价API
。所以用这个来帮我们简单使用Claude系列模型（倒是没有赞助哈哈哈）

大家有类似需求可以试一试的。


## 运行

你可以选择源码启动
```bash
 python -m streamlit /your_path/quick_chat/ui.py
```
也可以打镜像
```bash
docker build -t quick_chat .         

docker run -d -p 31001:31001 --name quick_chat_container quick_chat

```
> 我为了最快实现，Dockerfile里依赖是固定的哦
