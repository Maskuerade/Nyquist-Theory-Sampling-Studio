# Sampling-Theory Studio

## Introduction
Sampling an analog signal is a critical process in digital signal processing. The Nyquist–Shannon sampling theorem ensures the full recovery of a signal when sampled at a frequency that meets or exceeds its bandwidth (or double the maximum frequency for real signals). This project, **Sampling-Theory Studio**, provides a visual and interactive way to understand and demonstrate these concepts.

## Features
- **Sample & Recover**: Load a mid-length signal (~1000 points), visualize it, and sample it at various frequencies. The application will:
  - Display the original signal with markers for sampled points.
  - Reconstruct the signal using the Whittaker–Shannon interpolation formula.
  - Show the difference between the original and reconstructed signals across three graphs.

- **Load & Compose**: Users can load signals from files or create composite signals using:
  - A signal mixer to add multiple sinusoidal signals of varying frequencies and magnitudes.
  - The option to remove components from the mixed signal.

- **Additive Noise**: Introduce controllable noise to the loaded signal, allowing users to adjust the Signal-to-Noise Ratio (SNR) and visualize the impact of noise on different frequencies.

- **Real-Time Processing**: All sampling and recovery operations are performed in real time, reflecting user changes immediately.

- **Resizable Interface**: The application UI can be resized without compromising usability or layout.

- **Testing Scenarios**: Includes at least three synthetic signal examples to illustrate various sampling scenarios:
  1. A mix of 2Hz and 6Hz sinusoidal signals. Sampling at 12Hz or above results in proper recovery, while sampling at 4Hz leads to aliasing. The effect of sampling at 8Hz is also explored.
  2. [Example 2: Add your unique test case here.]
  3. [Example 3: Add your unique test case here.]

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sampling-theory-studio.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sampling-theory-studio
   ```
3. Install the required dependencies:
   ```bash
   # For Python projects, use:
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Use the interface to load signals, compose new ones, adjust sampling frequencies, and visualize results in real time.

## Contributing
Contributions are welcome! If you'd like to improve the project, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Special thanks to the authors of the Nyquist–Shannon sampling theorem for their foundational work in signal processing.


## Contributors

<table>
  <tr>
    <td align="center">
    <a href="https://github.com/Youssef-Ashraf71" target="_black">
    <img src="https://avatars.githubusercontent.com/u/83988379?v=4" width="150px;" alt="Youssef Ashraf"/>
    <br />
    <sub><b>Youssef Ashraf</b></sub></a>
    </td>
    <td align="center">
    <a href="https://github.com/mouradmagdy" target="_black">
    <img src="https://avatars.githubusercontent.com/u/89527761?v=4" width="150px;" alt="Mourad Magdy"/>
    <br />
    <sub><b>Mourad Magdy</b></sub></a>
    <td align="center">
    <a href="https://github.com/ZiadMeligy" target="_black">
    <img src="https://avatars.githubusercontent.com/u/89343979?v=4" width="150px;" alt="Ziad Meligy"/>
    <br />
    <sub><b>Ziad Meligy</b></sub></a>
    </td>
    </td>
    <td align="center">
    <a href="https://github.com/Maskuerade" target="_black">
    <img src="https://avatars.githubusercontent.com/u/106713214?v=4" width="150px;" alt="Mariam Ahmed"/>
    <br />
    <sub><b>Mariam Ahmed</b></sub></a>
    </td>
      </tr>
 </table>

