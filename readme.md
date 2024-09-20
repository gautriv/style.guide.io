## MSTP Style Checker

**A Python-based tool for analyzing text content and providing suggestions based on the Microsoft Style Guide (MSTP).**

### Table of Contents

* [Description](#description)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
    * [Running the Application](#running-the-application)
    * [Analyzing Content](#analyzing-content)
* [Examples](#examples)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

### Description

The MSTP Style Checker is a Flask-based web application designed to help writers and editors ensure that their content adheres to the Microsoft Style Guide. The application analyzes input text and provides suggestions to improve consistency, clarity, and professionalism in line with MSTP guidelines.

### Features

* Terminology Checks: Validates the usage of specific terms and suggests corrections.
* Stylistic Guidelines: Enforces style rules related to grammar, punctuation, and formatting.
* Inclusivity: Identifies non-inclusive language and suggests alternatives.
* Extensibility: Modular rule-based system allows for easy addition of new rules.
* User-Friendly Interface: Simple web interface for easy content analysis.

### Installation

#### Prerequisites

* Python 3.6 or higher
* Git (optional, for cloning the repository)

#### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/gautriv/style.guide.io.git
   cd style.guide.io.git
   ```

   Alternatively, download the repository as a ZIP file and extract it.

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

### Usage

#### Running the Application

Start the Flask web server by running:

```bash
python app.py
```

The application will start on http://localhost:5000.

#### Analyzing Content

1. Open your web browser and navigate to http://localhost:5000.
2. Paste or type your text content into the input field provided.
3. Click the Analyze button.
4. Review the suggestions displayed below the input field.

### Examples

#### Sample Input

```
plaintext
Please backup your files regularly to prevent data loss.

Ensure Bluetooth is enabled on your device.

He requested access to the administrator panel.

Avoid using and/or in official documents.

Afterwards, we can review the results.
```

#### Expected Suggestions

* Line 1: Use 'back up' as a verb: 'back up your files' instead of 'backup your files'.
* Line 2: Capitalize 'Bluetooth' as it's a proper noun.
* Line 3: Use 'administrator' instead of 'admin' in content.
* Line 4: Avoid using 'and/or'; consider rephrasing for clarity.
* Line 5: Use 'afterward' instead of 'afterwards'.

### Project Structure

```
mstp-style-checker/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   └── css
│       ├── styles.css
│   └── js
├── templates/
│   └── index.html
├── app/
│   ├── __init__.py
│   ├── mstp_rules.py
│   ├── utils.py
│   └── rules/
│       ├── __init__.py
│       ├── accessibility_terms.py
│       # ... (other rule files) ...
│       └── units_of_measure_terms.py
readme.md
requirements.txt
run.py
```

### Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**
   Click the Fork button on the repository's GitHub page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/yourusername/mstp-style-checker.git
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/new-rule
   ```

4. **Make Your Changes**
   Add new rules or improve existing ones.
   Ensure that your code follows the project's style guidelines.

5. **Commit Your Changes**

   ```bash
   git commit -am "Add new rule for XYZ"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/new-rule
   ```

7. **Submit a Pull Request** - Go to the original repository and create a pull request from your forked repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue in the repository or contact:
* Email: trivedi.gaurav30@gmail.com
  

> [!IMPORTANT]  
This tool is intended to assist with writing content in compliance with the Microsoft Style Guide. It is not affiliated with or endorsed by Microsoft. Always refer to the official [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) for authoritative guidelines.

