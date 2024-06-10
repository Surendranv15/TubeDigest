from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo
import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
def f(videourl):
 youtube_video = videourl
 
 video_id = youtube_video.split("=")[1]
 YouTubeVideo(video_id)
 # transcript = YouTubeTranscriptApi.get_transcript(video_id)
 try:
 transcript = YouTubeTranscriptApi.get_transcript(video_id)
 result = ""
 for i in transcript:
 result += ' ' + i['text']
 # print(result)
 print(len(result))
 # sum(result)
 return result
 except:
 return "no"
def summ(videourl):
 text = f(videourl)
 if(len(text) > 2):
 stopwords = list(STOP_WORDS)
 nlp = spacy.load('en_core_web_sm')
 docx = nlp(text)
 mytokens = [token.text for token in docx]
 word_frequencies = {}
 for word in docx:
 if word.text not in stopwords:
 if word.text not in word_frequencies.keys():
 word_frequencies[word.text] = 1
 else:
 word_frequencies[word.text] += 1
 # print(word_frequencies)
 maximum_frequency = max(word_frequencies.values())
 for word in word_frequencies.keys(): 
 word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
 # print(word_frequencies)
 sentence_list = [ sentence for sentence in docx.sents ]
 for t in sentence_list:
 for w in t:
 w.text.lower()
 sentence_scores = {} 
 for sent in sentence_list: 
 for word in sent:
 if word.text.lower() in word_frequencies.keys():
 if len(sent.text.split(' ')) < 40:
 if sent not in sentence_scores.keys():
 sentence_scores[sent] = word_frequencies[word.text.lower()]
 else:
 sentence_scores[sent] += word_frequencies[word.text.lower()]
 summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
 final_sentences = [ w.text for w in summarized_sentences ]
 summary = ' '.join(final_sentences)
 return summary
 else:
 return "not available"
 # print(summary)
v = "https://www.youtube.com/watch?list=RDGMEMCMFH2exzjBeE_zAHHJOdxg&v=cE
WwJxEq9Lg"
result = f(v)
# print(result)
# summ(result)
