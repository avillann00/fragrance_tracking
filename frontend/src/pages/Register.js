import React, { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

function Register() {
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const navigate = useNavigate()

  const handleSubmit = async (event) => {
    event.preventDefault()
    if (password !== confirmPassword) {
      alert('Passwords Do Not Match')
      return
    }
    try{
      const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000'
      await axios.post(`${apiUrl}/users/register/`, {
        username: username,
        email: email,
        password: password
      })
      goToLogin()
    }
    catch (error){
      console.error('Error Registering User: ', error)
    }
  }

  function goToLogin(){
    navigate('/login')
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input 
          type='text'
          placeholder='Username'
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input 
          type='text'
          placeholder='Email'
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input 
          type='password'
          placeholder='Password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <input 
          type='password'
          placeholder='Confirm Password'
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />
        <button type='submit'>Register</button>
      </form>
      <button onClick={goToLogin}>Already Have An Account?</button>
    </div>
  )
}

export default Register
