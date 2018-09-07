# bookAnalysis My attention drew to this project while I was reading
`The protrait of an artist as a young man` by James Joyes. Beside the
style of the text, the number of new words and expressions are an
important factor that makes a text harder or easier to understand. So
I encouraged to do some basic analysis and compare the result for  few
well-known authors such as Jame Joyce, Jane Austin, Bram Stoker and
english translation of works by Friedrich Nietzche.

Fortunately, works of very well-known authors are collected into
Gutenberg project and the texts can be downloaded in ebook or simple
txt format. So after collecting texts, I performed a simple analysis
and build a dictionary of new words and number of occurance of each
words in the text. Here are some results for each author and
text.

| Jane Austin    |  New Words  | Total Words
|----------------|-------------|------------
| Emma           | 8905        | 164120
| Persuasion     | 6190        |  86755
|MansfieldPark   | 9376        | 163560

| James Joyce    |  New Words  | Total Words
|----------------|-------------|------------
| Emma           | 8905        | 164120
| Persuasion     | 6190        |  86755
|MansfieldPark   | 9376        | 163560


According to this simple analysis, we can see the ratio of number
of new words to the total number of words for each author is constant
if the length of book is bigger than some threshold. And it does make
sense because each author use certain number of words to convey an idea.
If the text is too short then the ratio would be high as for example
book .... of James Joyce or .... of Jane Austin. One other import point
is ... of Jane Austin that our analysis shows higher ratio, but looking
at the title we see it is her letter and it is different from books. It can
be included the correspondence reply or the style of letter that make it
different from the style of the book.

What is the saturation length, after some length of a book, the chance
of apearance of new words will decrease. So do the same analysis
at different length of a same book. For example to the analysis at 1/4
of the book till whole book.


The other thing that we can do is to check the Zipf's law. According to
Zipf's law the frequency of a word is predicted by
$$ f = cr^{-s} $$
where $r$ is the rank of the word in text. If $s$ is different for different author? 

The next goal would be recognition of an author form the feeded
text. possible way is to follow the same step for spam filtering with the difference
that the decision is not binary (number of authors). Maybe better to remove
high frequency words such as 'a' 'the' word between all authors.


