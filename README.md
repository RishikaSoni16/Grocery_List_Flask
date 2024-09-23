<h4>1. **Clone the repository**:</h4>
   ```bash
   git clone https://github.com/RishikaSoni16/Grocery_List_flask.git
   cd Grocery_List_flask
<h4>2. Ensure you have Docker and Docker Compose installed:</h4>
   docker --version
   docker-compose --version  
<h4>3. Build the Docker images:</h4>
   docker-compose build
<h4>4. Run the application:</h4>
   docker-compose up
<h4>5. Access the application:</h4>
   http://localhost:5000
<h4>6. To stop the running containers, use:</h4>
   docker-compose down   
<h3>Use Curl to interact with the API</h3>
<h4>1. Add an Item</h4>
curl -X POST "http://localhost:5000/api/items" -H "Content-Type: application/json" -d "{\"iname\": \"New Item\", \"quantity\": 10}"
<h4>2. Update an Item</h4>
curl -X PUT "http://localhost:5000/api/items/1" -H "Content-Type: application/json" -d "{\"iname\": \"Updated Item\", \"quantity\": 20}"
<h4>3. Delete an Item</h4>
curl -X DELETE "http://localhost:5000/api/items/1"
