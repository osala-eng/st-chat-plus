from streamlit_chat_plus import message
import streamlit as st


st.title("Streamlit Chat Plus - Demo")


md = links = """

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

message(md, allow_html=True)