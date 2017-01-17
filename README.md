# urbex_bot
data mining project on urban exploration discourse.

borrows python code heavily from [Mastering Social Media Mining with Python](https://www.amazon.com/Mastering-Social-Media-Mining-Python-ebook/dp/B01BFD2Z2Q).

## usage

run the bot, searching for terms or hashtags:
```python
python urbex_bot.py "term1" "term2" "#hashtag1"
```
output will appear in a jsonl file.

perform frequency analysis on hashtags:
```python
python hastag_freq.py stream_term1_term2.jsonl
```

perform frequency analysis on terms, using natural language toolkit:
```python
python term_freq.py stream_term1_term2.jsonl
```
