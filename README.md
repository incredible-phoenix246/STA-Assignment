# Statics Assignment Solution

## Description
A detailed solution for EGR4201 Assignment.

This project performs data analysis, including data summarization, data cleaning, basic descriptive statistics, and graphical summaries. It is designed to work with a CSV dataset containing information related to storm events, including 'Event_Type' and 'Property_Cost' columns.

It aslo contains a regression model.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Data](#data)

## Introduction

This Python project aims to analyze storm event data stored in a CSV file. It provides tools for data summarization, data cleaning, basic descriptive statistics, and graphical summaries. The project uses libraries like pandas, matplotlib, numpy, and scipy to perform these tasks.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following dependencies installed:

- Python 3
- pip (Python package manager)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/data-analysis-project.git
   cd STA-Assignment
   ```

2. Create a virtual environment (optional but recommended):

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

## Usage 

- Run the Python script to perform data analysis:

    ```
    python data_analysis.py
    ```

    The script will load the CSV data, perform data cleaning, calculate descriptive statistics, and create graphical summaries.


## Data

The project assumes a CSV dataset with columns including:

'Event_Type': Represents the type or category of storm events.
'Property_Cost': Represents the cost associated with the property related to each storm event.
Ensure your data is in the correct format and provide the path to your CSV file in the script.

Also the script also gives room for you to edit and make changes ti the category you want 


