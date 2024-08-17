# GeminiFusion

**GeminiFusion** is an innovative platform that integrates the power of Google Gemini Pro and Gemini Pro Vision models. This application allows users to interact with AI through text-based conversation and image-based captioning, providing a seamless experience across multiple modalities.

## Features

- **ChatBot:** Engage in real-time conversations with the AI, powered by the Gemini Pro model.
- **Image Captioning:** Generate descriptive captions for your images using the Gemini Pro Vision model.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Abhrankan-Chakrabarti/GeminiFusion.git
   cd GeminiFusion
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```
     api_key=YOUR_GOOGLE_API_KEY
     ```

## Usage

1. **Run the application:**
   ```bash
   streamlit run app.py
   ```

2. **Features:**
   - **ChatBot:** Navigate to the ChatBot section to start a conversation with the AI.
   - **Image Captioning:** Upload an image and enter a prompt to generate a caption.

## Technology Stack

- **Python**
- **Streamlit**
- **Google Gemini Pro**
- **Google Gemini Pro Vision**

## Contributing

We welcome contributions! Please see our [contribution guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.