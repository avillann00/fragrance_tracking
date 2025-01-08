import React, { useState, useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import AuthContext from '../components/AuthContext'

function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()
  const { loginUser } = useContext(AuthContext)

  const handleSubmit = async (event) => {
    event.preventDefault()
    await loginUser(username, password)
    navigate('/')
  }

  function goToRegister() {
    navigate('/register')
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input 
          type='text'
          placeholder='username'
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input 
          type='password'
          placeholder='password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type='submit'>Login</button>
      </form>
      <button onClick={goToRegister}>Need An Account?</button>
    </div>
  )
}

export default Login
