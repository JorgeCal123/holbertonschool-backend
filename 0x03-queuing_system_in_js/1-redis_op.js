import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', (err) => console.log('Redis client not connected to the server:', err));


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    const result = client.get(schoolName);
    console.log(result)
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');