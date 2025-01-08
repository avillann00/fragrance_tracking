import axios from 'axios'
import React, { useContext, useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import AuthContext from '../components/AuthContext'

function Details() {
  const { id } = useParams()
  const [fragrance, setFragrance] = useState(null)
  const navigate = useNavigate()
  const { authTokens } = useContext(AuthContext)

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000'
    axios.get(`${apiUrl}/api/details/${id}`, {
      headers: {
        'Authorization': `Bearer ${authTokens.access}`
      }
    })
      .then(response => setFragrance(response.data))
      .catch(error => console.error('error fetching details: ', error))
  }, [authTokens, id])

  const priceHistory = fragrance?.prices?.map(price => (
    <li>
      <h3>Price From Website: {price.price}</h3>
      <h3>Date Collected: {price.date}</h3>
    </li>
  ))

  function goHome() {
    navigate('/')
  }

  if (!fragrance){
    return (
      <h1>Loading...</h1>
    )
  }

  return (
    <div>
      <h1>Fragrance Name: {fragrance.name}</h1>
      <h1>Fragrance House: {fragrance.house}</h1>
      <h1>Website Name: {fragrance.website}</h1>
      <a href={fragrance.url}>{fragrance.url}</a>
      <h1>Your Notes: {fragrance.notes}</h1>
      <h1>Price History:</h1>
      {priceHistory}
      <button onClick={goHome}>Back</button>
    </div>
  )
}

export default Details
