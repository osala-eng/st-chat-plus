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
  padding: '10px 14px',
  margin: '5px 20px',
  maxWidth: '70%',
  whiteSpace: 'pre-line'
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
  height: 'auto',
  margin: 0,
  width: '100%',
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

  const mdFormat = allowHTML || false

  useEffect(() => {
    Streamlit.setFrameHeight()
  }, [])

  useEffect(() => {
    hljs.highlightAll()
  })

  return <ChatMessage style={chatStyle}>
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
