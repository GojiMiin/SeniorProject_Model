import pandas as pd
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
import itertools

Porter_Stemmer = PorterStemmer()

readIn = pd.read_csv("IMDB Dataset.csv")
sample = readIn.head()
InFilter = sample['review'].astype('string')
InFilter.drop(InFilter.head(0))
print(InFilter)
#sentence = "One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They are right, as this is exactly what happened with me.<br /><br />The first thing that struck me about Oz was its brutality and unflinching scenes of violence, which set in right from the word GO. Trust me, this is not a show for the faint hearted or timid. This show pulls no punches with regards to drugs, sex or violence. Its is hardcore, in the classic use of the word.<br /><br />It is called OZ as that is the nickname given to the Oswald Maximum Security State Penitentary. It focuses mainly on Emerald City, an experimental section of the prison where all the cells have glass fronts and face inwards, so privacy is not high on the agenda. Em City is home to many..Aryans, Muslims, gangstas, Latinos, Christians, Italians, Irish and more....so scuffles, death stares, dodgy dealings and shady agreements are never far away.<br /><br />I would say the main appeal of the show is due to the fact that it goes where other shows wouldn't dare. Forget pretty pictures painted for mainstream audiences, forget charm, forget romance...OZ doesn't mess around. The first episode I ever saw struck me as so nasty it was surreal, I couldn't say I was ready for it, but as I watched more, I developed a taste for Oz, and got accustomed to the high levels of graphic violence. Not just violence, but injustice (crooked guards who'll be sold out for a nickel, inmates who'll kill on order and get away with it, well mannered, middle class inmates being turned into prison bitches due to their lack of street skills or prison experience) Watching Oz, you may become comfortable with what is uncomfortable viewing....thats if you can get in touch with your darker side."
#sentence = "agreement agree agreed hiiiiiiiiiiiiiiiiiiiiiii waowwwwwwwwwwwwwwwwwwwwwwwww"

#lowercase & remove html tag-----------
for sentence in InFilter:
    lower_sentence = sentence.lower()
    clean = re.compile('<.*?>')
    sentence_no_tag = re.sub(clean,'',lower_sentence)

#tokenization and clean word --------
    cleaned = []
    tokenizer = RegexpTokenizer(r'\w+')
    token_sentence = tokenizer.tokenize(sentence_no_tag)
    for w in token_sentence:
    #delIter = ''.join(ch for ch, _ in itertools.groupby(w))  # delete repeat alphabet
        if not w in stopwords.words('English'):  # delete stopwords
            cleaned.append(w)

#stemmer
    print("{0:20}{1:20}".format("Word", "Stem"))

    for word in cleaned:
        print("{0:20}{1:20}".format(
            word, Porter_Stemmer.stem(word)))




