from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")


def translate(text):
    batch = tokenizer([text], return_tensors="pt")
    gen = model.generate(**batch)
    translated_text = tokenizer.batch_decode(gen, skip_special_tokens=True)
    return translated_text
