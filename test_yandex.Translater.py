import googletrans
from googletrans import Translator
from langdetect import detect

translator = googletrans.Translator()
# print(translator.translate("The only aim in Rust is to survive. Everything wants you to die - the island’s wildlife and other inhabitants, the environment, other survivors. Do whatever it takes to last another night.", dest="ru").text)

text = "The only aim in Rust is to survive. Everything wants you to die - the island’s wildlife and other inhabitants, the environment, other survivors. Do whatever it takes to last another night."
print(detect(text))

if detect(text) == 'en':
    print(translator.translate(
        "The only aim in Rust is to survive. Everything wants you to die - the island’s wildlife and other inhabitants, the environment, other survivors. Do whatever it takes to last another night.",
        dest="ru").text)
