"""
    A multi-clipboard program
"""
text = {'agree': "Yes,I agree",
        'busy': "Sorry, can we do this later",
        'upsell': "Would you consider making this a monthly donation?"
        }

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python 6.6mclip.py[keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('text for' + keyphrase + 'copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
