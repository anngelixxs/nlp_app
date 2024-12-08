import streamlit as st
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

# Завантаження моделі
@st.cache_resource
def load_model():
    model_name = "Helsinki-NLP/opus-mt-en-uk"  # Модель для перекладу з англійської на українську
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    translator = pipeline("translation_en_to_uk", model=model, tokenizer=tokenizer)
    return translator

# Ініціалізація Streamlit
st.title("Перекладач тексту з англійської на українську")


translator = load_model()

# Поле вводу тексту
input_text = st.text_area("Введіть текст англійською:", "")

# Кнопка для виконання перекладу
if st.button("Перекласти"):
    if input_text.strip():
        with st.spinner("Переклад виконується..."):
            result = translator(input_text)
            translated_text = result[0]['translation_text']
            st.success("Переклад виконано!")
            st.write("### Результат перекладу:")
            st.write(translated_text)
    else:
        st.error("Будь ласка, введіть текст для перекладу.")
