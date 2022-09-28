import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis client not connected to the server:', err));


const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

const KEY = 'HolbertonSchools';

function addhset(key, k, v) {
    client.hset(key, k, v, print);

}
addhset(KEY, "Portland", 50);
addhset(KEY, "Seattle", 80);
addhset(KEY, "New York",20);
addhset(KEY, "Bogota", 20);
addhset(KEY, "Cali", 40);
addhset(KEY, "Paris", 2);

client.hgetall(KEY, (err, value) => {
    console.log(value);
});