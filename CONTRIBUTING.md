# Contributing to ScayForce

Thank you for your interest in contributing to ScayForce! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)

## Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Report any violations to the maintainer

## How Can I Contribute?

### Reporting Bugs

1. Check if the bug has already been reported in the Issues section
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Error messages or logs

### Suggesting Features

1. Check if the feature has already been suggested
2. Create a feature request issue with:
   - Clear description of the feature
   - Use cases and benefits
   - Potential implementation approach (if you have ideas)

### Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit with clear messages
5. Push to your fork
6. Create a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/ScayForce.git
cd ScayForce

# Install dependencies
pip install -r requirements.txt

# Create a test environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
```

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the CHANGELOG.md (if it exists)
3. Ensure all tests pass (if tests exist)
4. Follow the coding standards
5. Get approval from maintainers before merging

## Coding Standards

### Python Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Add comments for complex logic

### Code Formatting

- Maximum line length: 100 characters
- Use 4 spaces for indentation
- Use descriptive variable names
- Add type hints where appropriate

### Commit Messages

- Use clear, descriptive commit messages
- Use present tense ("Add feature" not "Added feature")
- Reference issue numbers when applicable

Example:
```
Add support for 7z archives
Fix resume functionality for large wordlists
Update documentation with new features
```

## Questions?

If you have questions, feel free to:

- Open an issue with the "question" label
- Contact the maintainer:
  - Email: Scayar.exe@gmail.com
  - Telegram: @im_scayar
  - Website: https://scayar.com

---

**Thank you for contributing to ScayForce!** 🚀

