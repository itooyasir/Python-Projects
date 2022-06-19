# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 10:57:27 2022

@author: HP
"""

#GPT-2 stands for Generative Pre-trained Transformer 2.
#It is an open-source Natural Language Processing model created by OpenAI. 
#It can generate paragraphs of text with state of the art performance on many language benchmarks. 
#It is also used for machine translation, question answering, and text summarization.

from transformers import pipeline
model = pipeline("text-generation", model = "gpt2")

sentence = model("Hi, My name is Yasir Itoo, I am here", 
                 do_sample=True, top_k=50, 
                 temperature=0.9, max_length=200, 
                 num_return_sentences=2)

for i in sentence:
  print(i["generated_text"])