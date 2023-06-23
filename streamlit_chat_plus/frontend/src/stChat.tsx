import {
  // eslint-disable-next-line 
  Streamlit,
  ComponentProps,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { useEffect } from "react"
import styled from '@emotion/styled'

import Markdown from 'markdown-to-jsx'

import hljs from "highlight.js"
import "highlight.js/styles/base16/dracula.css"

hljs.configure({
  cssSelector: "pre code"
})

const Message = styled.div({
  display: 'inline-block',

  border: '1px solid transparent',
  borderRadius: '10px',
  padding: '10px 2rem',
  margin: '5px 20px',
  maxWidth: '80%',
})

const Avatar = styled.img({
  border: `1px solid transparent`,
  borderRadius: '50%',
  height: '3rem',
  width: '3rem',
  margin: 0
})

const ChatMessage = styled.div({
  display: 'flex',
  margin: 0,
  width: '100%',
  flex: '1',
})

const ChatUI: React.FC<ComponentProps> = (props) => {
  const { isUser, avatarStyle, seed, message, logo, allowHTML, extLinks } = props.args;
  const avatarUrl = !!logo ? logo : `https://api.dicebear.com/5.x/${avatarStyle}/svg?seed=${seed}`
  const { theme } = props

  const chatStyle: React.CSSProperties = {
    flexDirection: isUser ? 'row-reverse' : 'row',
    fontFamily: `${theme?.font}, 'Segoe UI', 'Roboto', sans-serif`,
  }

  const messageStyle = {
    background: theme?.secondaryBackgroundColor,
  }

  const messageRef = React.useRef<HTMLDivElement>(null)
  const mdFormat = allowHTML || false

  // Highlight code blocks
  useEffect(() => {
    hljs.highlightAll()
  });

  // Watch for changes in the element and auto update the frame height
  useEffect(() => {
    const resizeObserver = new ResizeObserver(() => {
      Streamlit.setFrameHeight()
    })
    if (messageRef.current) {
      resizeObserver.observe(messageRef.current)
    }
    return () => {
      resizeObserver.disconnect()
    }
  }, [messageRef])

  // Copy code to clipboard
  useEffect(() => {
    if (messageRef.current && window.isSecureContext) {
      const codes = messageRef.current.getElementsByTagName('pre')
        for(let pre = 0; pre < codes.length; pre++) {
          const button = document.createElement('div')
          button.innerHTML = '<span class="tooltiptext" id="myTooltip">Copy to clipboard</span>📋'
          button.className = 'copy-button'
          button.addEventListener('click', () => {
            try {
            console.log('copying')
            navigator.clipboard.writeText(codes[pre].innerText).then(() => {
              const tooltip = codes[pre].getElementsByClassName("tooltiptext")[0]
              tooltip.innerHTML = 'Copied!'
              setTimeout(() => {
                tooltip.innerHTML = 'Copy to clipboard'
              }, 2000)
            })
            } catch (err) {
              console.log('Failed to copy: ', err)
            }
          })
          codes[pre].style.position = 'relative'
          codes[pre].appendChild(button)
        }
    }    
  }, [messageRef])
    

  return <ChatMessage style={chatStyle} ref={messageRef}
    onLoad={() => {
      Streamlit.setFrameHeight()
      console.log('onLoad')
    }}
  >
    <Avatar src={avatarUrl} />
    <Message style={messageStyle}>
      {mdFormat ?
        <Markdown
          options={{
            overrides: extLinks ? {
              a: { component: 'a', props: { target: "_blank" } }
            } : undefined,
          }}
        >{message}</Markdown> :
         message 
      }
    </Message>
  </ChatMessage>
}

export default withStreamlitConnection(ChatUI);
