# Contributing to NeuroPolis

Thank you for your interest in helping improve NeuroPolis! We welcome all contributions—bug fixes, enhancements, documentation updates, and feature ideas.

## How You Can Contribute

1. **Fork the repository**  
   Clone the main repo and create your own fork:
   ```bash
   git clone https://github.com/Avikalp-Karrahe/NeuroPolis.git
   cd NeuroPolis
   git remote add fork https://github.com/<your-username>/NeuroPolis.git
   ```

2. **Create a feature branch**  
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Develop & Test**  
   - Follow the existing code style and project structure.  
   - Write clear, descriptive commit messages.  
   - Add or update tests under the `tests/` directory.  
   - Ensure all tests pass:
     ```bash
     pytest
     ```

4. **Ensure Continuous Integration (CI) Passes**  
   NeuroPolis uses GitHub Actions to run linting and tests. Make sure your branch builds successfully.

5. **Submit a Pull Request (PR)**  
   - Push your branch to your fork:
     ```bash
     git push fork feature/your-feature-name
     ```
   - Open a pull request against the `main` branch of the upstream repository.  
   - Reference any relevant issue numbers in your PR description.  
   - Provide a clear summary of your changes and why they’re needed.

## Reporting Bugs & Requesting Features

- **Bugs**: Please open an issue in this repository with a descriptive title, steps to reproduce, and any relevant logs or screenshots.  
- **Feature Requests**: If you have a new feature idea, open an issue describing the motivation and proposed approach.

## Code of Conduct

All contributors are expected to adhere to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Please be respectful and collaborative.

---

Thank you for helping make NeuroPolis better!
