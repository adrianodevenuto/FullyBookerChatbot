# OpenAI Assistant API with FastAPI

A FastAPI-based web service that integrates with OpenAI's Assistant API to create conversational AI applications with function calling capabilities.

## Features

- 🤖 **OpenAI Assistant Integration**: Seamless integration with OpenAI's Assistant API
- 🔧 **Function Calling**: Support for custom function execution during conversations
- 🧵 **Thread Management**: Conversation thread creation and management
- 🚀 **FastAPI Framework**: High-performance async web framework
- 📝 **Booking System**: Example booking function implementation
- ⚡ **Real-time Processing**: Asynchronous message processing

## Prerequisites

- Python 3.8+
- OpenAI API key
- OpenAI Assistant ID

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd <repository-name>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   
   Create a `.env` file in the root directory and add your credentials:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   CHATBOT_ASSISTANT_ID=your_assistant_id_here
   ```

   **Important**: Update the `main.py` file to load these environment variables:
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
   CHATBOT_ASSISTANT_ID = os.getenv("CHATBOT_ASSISTANT_ID")
   ```

## Usage

### Starting the Server

Run the FastAPI server:
```bash
python main.py
```

The server will start on `http://0.0.0.0:8001`

### API Endpoints

#### 1. Start a New Conversation
```http
GET /start
```

**Response:**
```json
{
  "thread_id": "thread_abc123"
}
```

#### 2. Send a Message
```http
POST /chat
```

**Request Body:**
```json
{
  "thread_id": "thread_abc123",
  "message": "Hello, I'd like to make a booking"
}
```

**Response:**
```json
{
  "response": "Hello! I'd be happy to help you with your booking..."
}
```

### Example Usage with curl

1. **Start a conversation:**
   ```bash
   curl -X GET http://localhost:8001/start
   ```

2. **Send a message:**
   ```bash
   curl -X POST http://localhost:8001/chat \
     -H "Content-Type: application/json" \
     -d '{
       "thread_id": "your_thread_id",
       "message": "I want to book an appointment"
     }'
   ```

## Function Calling

The application includes an example booking function that can be called by the OpenAI Assistant:

```python
def prenota(nome, numero_cel, riassunto_breve_chat):
    """
    Example booking function
    
    Args:
        nome (str): Customer name
        numero_cel (str): Phone number
        riassunto_breve_chat (str): Brief chat summary
    
    Returns:
        str: Confirmation message
    """
```

### Adding Custom Functions

To add new functions:

1. Define your function in `main.py`
2. Add it to the `available_functions` dictionary
3. Configure the function in your OpenAI Assistant settings

## Project Structure

```
.
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── .env               # Environment variables (create this)
```

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **OpenAI**: Official OpenAI Python client
- **Uvicorn**: ASGI server for FastAPI
- **Pydantic**: Data validation using Python type annotations
- **python-dotenv**: Load environment variables from .env file

## Configuration

### OpenAI Version Compatibility

The application requires OpenAI Python client version 1.1.1 or higher. The version check is performed automatically on startup.

### Server Configuration

Default server configuration:
- **Host**: `0.0.0.0` (all interfaces)
- **Port**: `8001`

To change these settings, modify the `uvicorn.run()` call in `main.py`.

## Error Handling

The application handles various scenarios:
- Missing thread ID
- OpenAI API errors
- Function execution errors
- Assistant run failures

## Security Considerations

⚠️ **Important Security Notes:**

1. **Never commit API keys** to version control
2. **Use environment variables** for sensitive data
3. **Implement proper authentication** for production use
4. **Validate and sanitize** function inputs
5. **Set up CORS** if needed for web frontend integration

## Development

### Running in Development Mode

For development with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

### Testing

Test the API endpoints using:
- FastAPI's automatic interactive documentation at `http://localhost:8001/docs`
- Postman or similar API testing tools
- curl commands as shown in the usage examples

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

1. Check the [OpenAI API documentation](https://platform.openai.com/docs)
2. Review the [FastAPI documentation](https://fastapi.tiangolo.com/)
3. Open an issue in this repository

## Changelog

### v1.0.0
- Initial release
- OpenAI Assistant API integration
- Basic function calling support
- FastAPI web service implementation
