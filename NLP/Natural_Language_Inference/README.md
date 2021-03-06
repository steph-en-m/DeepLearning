# Natural Language Inference (NLI):

## Overview:

Natural Language Inference is a task of determining whether a `hypothesis` is true `(entailment)`, False `(contradiction)`, or undertermined `(neutral)` given a `premise`.

**[Example:](http://nlpprogress.com/english/natural_language_inference.html#:~:text=Natural%20language%20inference%20is%20the,Premise)**

| Premise | Label | Hypothesis |
| :- | :-: | :- |
| A soccer game with multiple males playing. | entailement | Some men are playing a sport|
| A man inspects the uniform of a figure in some East Asian country. | contradiction | The man is sleeping. |
| An older and younger man smiling. | neutral | An older and younger man smiling. |

In summary, **`NLI` determines whether a given text `(hypothesis)` implies something similar to what is implied in the reference text `(premise)`**

The `Roberta_model.py` file contains a Roberta Language Model trained for NLI.<br/>
The related Kaggle Kernel can be accessed [HERE](https://www.kaggle.com/stephenmugisha/roberta-vs-watson)
