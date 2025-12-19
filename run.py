from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run the Flask development server, ajusting the port accordingly
    app.run(host="127.0.0.1", port=5005, debug=True)