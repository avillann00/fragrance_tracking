import React, { useEffect, useState, useContext } from 'react'
import AuthContext from '../components/AuthContext'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

function Home() {
  const [fragrances, setFragrances] = useState([])
  const navigate = useNavigate()
  const { authTokens, logoutUser } = useContext(AuthContext)

  useEffect(() => {
    if (!authTokens) {
      navigate('/login')
      return
    }
    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000'
    axios.get(`${apiUrl}/api/fragrances`, {
      headers: {
        'Authorization': `Bearer ${authTokens.access}`
      }
    })
      .then(response => setFragrances(response.data))
      .catch(error => console.error('there was an error getting the fragrances: ', error))
  }, [authTokens, navigate])

  const handleLogout = () => {
    logoutUser()
    navigate('/login')
  }

  const handleDelete = (id) => {
    if (!authTokens){
      navigate('/login')
      return
    }

    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000'
    axios.delete(`${apiUrl}/api/fragrances/${id}/`, {
      headers: {
        'Authorization': `Bearer ${authTokens.access}`
      }
    })
      .then(() => {
        alert('Fragrance Successfully Deleted')
        setFragrances(fragrances.filter(fragrance => fragrance.id !== id))
      })
      .catch(error => console.error('there was an error deleting this fragrance: ', error))
  }
  const getLatestPrice = (prices) => {
    if (!prices || prices.length === 0) { 
      return 'N/A'
    } 
    const latestPrice = prices.sort((a, b) => new Date(b.date) - new Date(a.date))[0]
    return latestPrice.price
  }
  const mappedFragrances = fragrances.map((fragrance) => (
    <li key={fragrance.id}>
      {console.log(fragrance)}
      <button onClick={() => navigate(`/details/${fragrance.id}`)}>View Details</button>
      {`Name: ${fragrance.name} | Website: ${fragrance.website} | Latest Price: ${getLatestPrice(fragrance.prices)}`}
      <button onClick={() => handleDelete(fragrance.id)}>Delete Fragrance</button>
    </li>
  ))

  return (
    <div>
      <p>Hi, Welcome to the Fragrance Tracking app. Add a fragrance to get started</p>
      <button onClick={() => navigate('/add')}>Add Fragrance</button>
      <div>Your Watch List:</div>
      <ul>
        {mappedFragrances}
      </ul>
      <button onClick={handleLogout}>Logout</button>
    </div>
  )
}

export default Home
