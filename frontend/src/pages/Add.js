import React, { useState, useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import AuthContext from '../components/AuthContext'
import axios from 'axios'

function Add() {
  const [name, setName] = useState('')
  const [house, setHouse] = useState('')
  const [website, setWebsite] = useState('')
  const [url, setUrl] = useState('')
  const [notes, setNotes] = useState('')
  const navigate = useNavigate()
  const { authTokens } = useContext(AuthContext)

  const handleSubmit = (event) => {
    event.preventDefault()
    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000'
    axios.post(`${apiUrl}/api/fragrances/`,
      {
        name: name,
        house: house,
        website: website,
        url: url,
        notes: notes
      },
      {
        headers: {
          'Authorization': `Bearer ${authTokens.access}`
        }
      }
    )
      .then(response => {
        console.log('added fragrance: ', response.data)
        setName('')
        setHouse('')
        setUrl('')
        setWebsite('')
        setNotes('')
        navigate('/')
      })
      .catch(error => console.error('error adding note: ', error))
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input 
          type='text'
          placeholder='Enter the Fragrance Name'
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <input 
          type='text'
          placeholder='Enter the Fragrance House'
          value={house}
          onChange={e => setHouse(e.target.value)}
        />
        <input 
          type='text'
          placeholder='Enter the Website Name'
          value={website}
          onChange={e => setWebsite(e.target.value)}
        />
        <input 
          type='text'
          placeholder='Enter Website Url'
          value={url}
          onChange={e => setUrl(e.target.value)}
        />
        <input 
          type='text'
          placeholder='Enter the Fragrance Notes Or Your Thoughts'
          value={notes}
          onChange={e => setNotes(e.target.value)}
        />
        <button type='submit'>Add</button>
      </form>
    </div>
  )
}

export default Add
