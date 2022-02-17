from api import app
import os

if __name__ == '__main__':
    port= int(os.environ.get("PORT", 8000))
    app.debug = True
    # print("Starting server at port 5000...")
    app.run(host="0.0.0.0", port=port)