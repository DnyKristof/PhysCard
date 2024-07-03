import axios from 'axios';
const API_URL = 'http://localhost:8000';
export async function getCards() {
    try {
        const response = await axios.get(`${API_URL}/cards`);
        return response.data;
    }
    catch (error) {
        console.error(error);
    }
}