import axios from 'axios'

const httpClient = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    'Content-Type': 'application/vnd.api+json',
  }
})

export default httpClient;
