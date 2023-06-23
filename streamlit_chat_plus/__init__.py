import streamlit.components.v1 as components
import os
from typing import Optional, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


_RELEASE = True
COMPONENT_NAME = "streamlit_chat_plus"

# use the build instead of development if release is true
if _RELEASE:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/build")

    _streamlit_chat = components.declare_component(COMPONENT_NAME, path=build_dir)
else:
    _streamlit_chat = components.declare_component(
        COMPONENT_NAME, url="http://localhost:3000"
    )

# data type for avatar style
AvatarStyle = Literal[
    "adventurer",
    "adventurer-neutral",
    "avataaars",
    "avataaars-neutral",
    "big-ears",
    "big-ears-neutral",
    "big-smile",
    "bottts",
    "bottts-neutral",
    "croodles",
    "croodles-neutral",
    "fun-emoji",
    "icons",
    "identicon",
    "initials",
    "lorelei",
    "lorelei-neutral",
    "micah",
    "miniavs",
    "open-peeps",
    "personas",
    "pixel-art",
    "pixel-art-neutral",
    "shapes",
    "thumbs",
]


def message( message: str,
            is_user: Optional[bool] = False,
            avatar_style: Optional[AvatarStyle] = None,
            logo: Optional[str]=None,
            seed: Optional[Union[int, str]] = 88,
            key: Optional[str] = None,
            allow_html: Optional[bool] = False,
            open_links_externally: Optional[bool] = True):
    """
    _summary_: A message to be displayed in the chatbot

    """
    if logo:
        _streamlit_chat(
            message=message,
            seed=seed,
            isUser=is_user,
            logo=logo,
            key=key,
            allowHTML=allow_html,
            extLinks = open_links_externally
        )
    else:
        if not avatar_style:
            avatar_style = "fun-emoji" if is_user else "bottts"
        _streamlit_chat(
            message=message,
            seed=seed,
            isUser=is_user,
            avatarStyle=avatar_style,
            key=key,
            allowHTML = allow_html,
            extLinks = open_links_externally
        )
markdown = """
#### Sample md
- list 1
- list 2

> Data
> Done

"""

links = """


# Header 1
## Header 2
### Header 3
#### Header 4

<br>

#### Links
- [Click Me](https:/google.com)
- https://google.com


#### code sample

```python
import streamlit as st

with st.container():
    st.write("Hello world!")
    st.markdown('*Data*')
```

#### Table
| A | B | C | D | E | F | G | H | I | J |
| - | - | - | - | - | - | - | - | - | - |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|
| 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13|
| 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16|

#### Task List
- [x] Task 1
- [ ] Task 2
- [ ] Task 3
- [ ] Task 4

#### Video
<iframe width="500" height="340" src="https://www.youtube.com/embed/9Q6sLbz37gk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Image
![alt text](https://picsum.photos/320/240)

#### Audio
<audio controls>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
</audio>



### Typescript code
Here's a sample Typescript code to create a server using the Express framework:

```ts
import express from 'express';

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
```
In this code, we import the `express` module and create an instance of it using `const app = express()`. We then define a route for the root URL (/) using `app.get('/', ...)`, and send a response with the text `"Hello World!"` using `res.send('Hello World!')`.

Finally, we start the server listening on port 3000 using `app.listen(port, ...)`, and log a message to the console to confirm that the server is running.

Visit [Streamlit](https://streamlit.io) for more info.
<br>
"""


if not _RELEASE:
    import streamlit as st

    long_message = """A chatbot or chatterbot is a software application used to conduct an on-line chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent. 
    Designed to convincingly simulate the way a human would behave as a conversational partner, chatbot systems typically require continuous tuning and testing, and many in production remain unable to adequately converse, while none of them can pass the standard Turing test. 
    The term "ChatterBot" was originally coined by Michael Mauldin (creator of the first Verbot) in 1994 to describe these conversational programs.
    """
    
    message("Hello world", True)
    message(long_message)
    message(markdown, allow_html=True)
    message(links, allow_html=True)
 
    st.text_input("Message:")
