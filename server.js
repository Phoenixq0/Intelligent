const express = require('express')
const cors = require('cors')
const app = express()

// 允许跨域（前端开发时使用）
app.use(cors())
// 解析JSON请求体
app.use(express.json())

// 模拟AI聊天接口
app.post('/api/chat', (req, res) => {
  const { message } = req.body
  console.log('收到用户消息:', message)
  
  // 模拟延迟（1秒）
  setTimeout(() => {
    res.json({ 
      reply: `AI回复：${message}` 
    })
  }, 1000)
})

// 启动服务器
const PORT = 3000
app.listen(PORT, () => {
  console.log(`后端API运行在 http://localhost:${PORT}`)
})