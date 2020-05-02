# text-styler
Convert ASCII alphanumeric text to a random style using Unicode character normalization.

This script uses the [Mathematical Alphanumeric Symbols](https://en.wikipedia.org/wiki/Mathematical_Alphanumeric_Symbols) from the Unicode database to find a stylish looking replacement for each input character.

## CLI Usage
    Usage: python text_styler.py "<text>"

    $ python text_styler.py "Hello World"
    𝖧𝖾𝔩𝖑𝕠 𝑊𝙤𝒓𝒍𝘥
    
    $ python text_styler.py "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991"
    𝖯𝑦𝓉𝙝𝗼𝗻 𝚒𝘴 𝐚𝙣 𝘪𝗻𝒕𝕖𝘳𝙥𝑟𝗲𝙩𝙚𝑑, 𝒉𝖎𝕘𝗵-𝔩𝙚𝒗𝒆𝔩, 𝓰𝔢𝙣𝕖𝔯𝙖𝘭-𝗉𝖚𝑟𝚙𝑜𝒔𝔢 𝕡𝐫𝗼𝒈𝓇𝕒𝖒𝑚𝔦𝖓𝔤 𝔩𝘢𝖓𝖌𝓊𝒂𝙜𝗲. 𝑪𝗿𝓮𝔞𝑡𝚎𝐝 𝕓𝖞 𝐺𝖚𝐢𝖉𝔬 𝗏𝖺𝔫 𝓡𝑜𝑠𝐬𝚞𝒎 𝒶𝘯𝓭 𝒇𝘪𝓇𝔰𝘵 𝕣𝗲𝐥𝙚𝙖𝙨𝙚𝔡 𝓲𝘯 𝟏𝟵𝟫𝟙

## Library Usage
    >>> from text_styler import TextStyler

    >>> styler = TextStyler()
    >>> converted = styler.convert("Hello World!")
    
    >>> print(converted)
    𝖧𝖾𝔩𝖑𝕠 𝑊𝙤𝒓𝒍𝘥

## Notes
Only supported with Python3.

