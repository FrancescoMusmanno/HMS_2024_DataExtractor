# Overview

This Python project aims to provide a way to easily read data from a JSON file generated from a simulation and show it
to the user in a more friendly way. The user can filter the data by submitting the parameters he wants to filter by.

In this file there are instructions on how to configure Python, the IDE and how to run the project.

# Environment Setup
## Python Setup

To run this project you need to have Python installed on your machine. You can download it from
the [official website](https://www.python.org/)

You can refer to this [guide](https://www.youtube.com/watch?v=P7Q4_pqj7uc&ab_channel=AmitThinks) to install Python on
your Windows machine.

## IDE Setup

You can use any IDE to run this project, but I recommend using Visual Studio Code. You can download it from
the [official website](https://code.visualstudio.com/)

You can refer to this [guide](https://www.youtube.com/watch?v=cu_ykIfBprI&ab_channel=ProgrammingKnowledge) to install
Visual Studio Code on your Windows machine.

## Clone the repository

If you have Git installed on your machine, you can clone the repository by running the following command:

```bash
git clone https://github.com/FrancescoMusmanno/HMS_2024_DataExtractor.git
```

Otherwise, you can download the repository as a ZIP file by clicking on the green "Code" button on the top right of the
page.

# Run the project
Open the terminal in Visual Studio Code by pressing `Ctrl + ~` and navigate to the project folder.
You can open the terminal by clicking on the `Terminal` tab in the top menu and then clicking on `New Terminal`.

Before running the project, you need to install the required packages. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

To run the project, you need to place yourself in the terminal in the `src` (you can do that with `cd .\src`) folder and execute the following command:

```bash
py .\__main__.py
```

Once you run the command, in the output folder will be generated a csv file with the data retrieved from the `data.json`
file.

# Filter the data
To filter the data, you need to change the `config.json` file in the config folder. You can filter the data by changing the array values:
```json
{
  "input_pallets": [
    [3,7],
    [2,9],
    [5,25],
    [4,23],
    [6,21]
  ],
  "pickup_pallets": [
    [15,22],
    [6,9],
    [9,60],
    [4,25],
    [7,32]
  ]
}
```