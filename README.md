# Autoexaminator

A screen capture and autogui tool that automatically extracts exam questions and provides AI-powered explanations using Google's Gemini API.

## ⚠️ Educational Use Only

**This project is designed strictly for educational purposes to help students understand concepts and learn from their mistakes.** It should never be used to cheat on actual exams, tests, or assessments. Academic integrity is paramount, and this tool is intended to support learning, not circumvent it.

## Features

- 📸 Screen capture functionality for exam questions
- 🤖 Integration with Google Gemini API for intelligent responses
- 📝 Text extraction from captured images
- 💡 Detailed explanations and step-by-step solutions
- 📚 Educational context and learning resources

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gkesh/autoexaminator.git
cd autoexaminator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
```
Edit the `.env` file with your configuration:
```
GEMINI_API_KEY=your_actual_api_key_here
SCREENSHOT_LOC=path/to/screenshot/directory
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Use the screen capture tool to select the exam question area
3. The application will automatically:
   - Extract text from the captured image
   - Send the question to Gemini API
   - Display the educational explanation

## Configuration

Configuration is managed through environment variables in a `.env` file:

```env
GEMINI_API_KEY=your_actual_api_key_here
SCREENSHOT_LOC=path/to/screenshot/directory
```

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key for AI responses
- `SCREENSHOT_LOC`: Directory path where screenshots will be saved

Create a `.env` file in the root directory and update the values according to your setup.

## Educational Guidelines

This tool is designed to enhance learning by:

- Providing detailed explanations of concepts
- Breaking down complex problems into steps
- Offering additional resources for further study
- Helping identify knowledge gaps

### Proper Use Cases

✅ **Appropriate Uses:**
- Reviewing practice exams and homework
- Understanding concepts after completing assignments
- Self-study and concept reinforcement
- Preparing for future exams by learning from mistakes

❌ **Inappropriate Uses:**
- Cheating on live exams or tests
- Completing graded assignments dishonestly
- Violating academic integrity policies
- Bypassing learning processes

## Technical Details

### Architecture

The application consists of several key components:

- **Screen Capture Module**: Handles screenshot functionality
- **OCR Engine**: Extracts text from captured images
- **Gemini Integration**: Communicates with Google's AI API
- **Response Processor**: Formats and displays educational content

### API Integration

The tool integrates with Google's Gemini API to provide:
- Contextual explanations
- Step-by-step problem solving
- Related concept discussions
- Learning resource recommendations

## Privacy and Security

- Screenshots are processed locally when possible
- API requests are made securely over HTTPS
- No personal data is stored without explicit consent
- Images can be automatically deleted after processing

## Contributing

We welcome contributions that enhance the educational value of this tool:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please ensure all contributions maintain the educational focus and ethical use of the application.

## Disclaimer

**Academic Integrity Notice**: This software is provided for educational purposes only. Users are responsible for ensuring their use complies with their institution's academic integrity policies. The developers do not condone or support academic dishonesty in any form.

**Usage Responsibility**: By using this software, you acknowledge that you will only use it for legitimate educational purposes and in compliance with all applicable academic policies and regulations.

## Support

For questions about proper educational use or technical support:

- Open an issue on GitHub
- Review the educational guidelines above

---

**Remember**: The goal of education is to learn and grow. Use this tool to enhance your understanding, not to avoid the learning process. Academic success achieved through honest effort is far more valuable and lasting than any shortcut.