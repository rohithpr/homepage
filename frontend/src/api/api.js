import axios from 'axios'

const v0Client = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/v0/',
  headers: {
    'Content-Type': 'application/vnd.api+json',
  }
})

export default v0Client;
