# 📅 Foldable Daybook

Generate your own foldable calendar that sits perfectly between you and your laptop! Perfect for the analog note-taker in a digital world.

## 🎯 What it does

This Python tool creates a printable PDF calendar that you can fold into a compact, portable planner. Keep track of meetings, deadlines, and random thoughts without switching screens or hunting for your phone. The clever folding design shows one week at a time, helping you stay focused on current tasks without getting overwhelmed by the entire month.

## 🚀 Quick Start

### Prerequisites
- [Docker](https://www.docker.com/) (installation required)
- Printer (yes, the one collecting dust in the corner)
- Basic folding skills (origami masters welcome!)

### 1. Docker Setup
* Navigate to the `dockerfile` folder and build the Docker image:

```bash
docker build -t foldable-daybook .
```

### 2. Generate Calendar
* Run the calendar generator:
⚠️ **Note:** Update file paths to match your local **foldable-daybook** folder.

```bash
docker run --rm \
  -v /path/to/foldable-daybook/output:/app/output \
  foldable-daybook bash make_calendar.sh
```

### 3. Print and Fold
* Navigate to the output folder
* Print the generated PDF file
* Follow the folding guidelines in the included instructions
* Place under your laptop and start planning!

## 🎨 Features

- Clean, minimalist design
- Perfectly sized for laptop-side placement
- Easy to print and fold
- Monthly calendar views
- Space for daily notes
- No batteries required! 🔋


## 🙏 Acknowledgments

This project is inspired by the [Cortex Brand Sidekick Calendar Companion](https://cottonbureau.com/p/JJGBJR/journal/sidekick-calendar-companion#/19301969/black-paper-12x7). While this is a DIY, customizable free alternative, if you're looking for a premium, professionally crafted solution, definitely check out their original product!

## 📝 Contributing

Got ideas for making this even better? PRs are welcome! Whether it's adding new features, improving the design, or fixing my terrible folding instructions.
