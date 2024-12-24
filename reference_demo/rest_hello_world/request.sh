echo "GET request on root endpoint"
curl http://localhost:8081/

echo "GET request on /chat/George end point with institution=SUSTech"
curl http://localhost:8081/chat/George?institution=SUSTech

echo "POST request on /calculator/mult endpoint with JSON data"
curl -X POST -H "Content-Type: application/json" -d '{"xin":0.10, "yin":20}' http://localhost:8081/calculator/mult