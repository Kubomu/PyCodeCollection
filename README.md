# PyCodeCollection

A collection of small Python programs I wrote while learning to code at university.

I started this in 2024, during my first year with Python, and I keep it here as a snapshot of where I began: a mix of little games, desktop apps, and handy tools I built just to figure out how things worked. Some are polished, some are rough, and that is exactly the point. If you are also starting out, feel free to clone it, run things, and take them apart.

## What is inside

### Games and puzzles
- `GuessGame.py` - guess the secret number
- `RockPaperScissor.py` - rock, paper, scissors against the computer
- `Formula_One_Quiz.py` - a Formula One trivia quiz
- `MAZE.py` - a maze
- `RPG.py` - a small text role-playing game

### Desktop apps (Tkinter)
- `Tkinter/BMI_GUI.py` - a body mass index calculator with a window
- `Tkinter/LoanCalculator.py` - work out loan repayments
- `Tkinter/PyCalender.py` - a simple calendar
- `Tkinter/FidgetSpinner.py` - an animated fidget spinner
- `Tkinter/OlympicSymbol.py` - draws the Olympic rings
- `Tkinter/Happy Independence Day Uganda/Uganda.py` - an Independence Day tribute with artwork

### Graphics and animation
- `Pygame/BouncingBall.py` - a ball bouncing around the screen with Pygame

### Handy tools
- `YoutubeDownloader.py` - download a video with yt-dlp
- `QRcodegeneration.py` - turn text or a link into a QR code
- `RemoveImageBG.py` - strip the background out of an image
- `Image_captcha.py` - generate a captcha image
- `Password.py` - generate and check passwords
- `ListingRunningProcesses.py` - list the processes running on your machine
- `ValidateVoters.py` - a small voter validation exercise
- `conversion.py` - convert between common units

### Learning exercises
- `Day_of_the_week.py` - find the weekday for any date
- `DeterminingLeapYear.py` - check whether a year is a leap year
- `periodic_table_elements.py` - look up elements in the periodic table
- `PieChart.py` - draw a pie chart with matplotlib
- `Printing_Coloured_Output.py` - print coloured text in the terminal

## Running the scripts

1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Clone the repository:
   ```bash
   git clone https://github.com/Kubomu/PyCodeCollection.git
   cd PyCodeCollection
   ```

3. Install the libraries the scripts use:
   ```bash
   pip install -r requirements.txt
   ```
   The plain exercises and games need nothing extra, so you can also install a single library only when a script asks for it.

4. Run any script by name:
   ```bash
   python GuessGame.py
   ```
   Scripts inside a folder are run with their path, for example:
   ```bash
   python "Tkinter/BMI_GUI.py"
   ```

A few notes:
- The Tkinter and Pygame scripts open their own window, so run them on a computer with a screen rather than a headless server.
- `tkinter` and `turtle` are part of Python already and do not need installing.
- A couple of the tools depend on the outside world and may need a refresh over time. The YouTube downloader in particular can break when the site changes, and the background remover downloads a model the first time you run it.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Questions or suggestions are welcome at [kubomuedwin@gmail.com](mailto:kubomuedwin@gmail.com).

---

Happy coding, and here is to the next two years.
