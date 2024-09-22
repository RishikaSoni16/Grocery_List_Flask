<h1>1. Add an Item</h1>
curl -X POST "http://localhost:5000/api/items" -H "Content-Type: application/json" -d "{\"iname\": \"New Item\", \"quantity\": 10}"
<h1>2. Update an Item</h1>
curl -X PUT "http://localhost:5000/api/items/1" -H "Content-Type: application/json" -d "{\"iname\": \"Updated Item\", \"quantity\": 20}"
<h1>3. Delete an Item</h1>
curl -X DELETE "http://localhost:5000/api/items/1"
