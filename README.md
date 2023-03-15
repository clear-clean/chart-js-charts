# chart-js-charts

This project provides the data sheets as well as the code for the interactive diagrams on [https://www.cleanboss.de/](https://www.cleanboss.de/).

## How to create CSV files

1. Change to the scripts directory of this project.
2. Edit the `YEAR` variable in the `create_base_csv.py` script according to your needs - and do not forget to save your changes.
3. Run the script like this:
    ```bash
    python create_base_csv.py
    ```
4. Add the created csv file to the data directory of this Github project. For doing so, you can use the webinterface via browser.

## How to include the diagram of an additional year

To obtain this, you have to make the following changes to [charts/sonit-mdm-particles.html](charts/sonit-mdm-particles.html):

1. Add the new year to the options of the select object and set the default value accordingly, e.g. for the year 2023 like this:
    ```html
    <select id="selectYear" onchange="reloadChart(this)">
        <option value="2023">Select Year</option> <!-- default value -->
        <option value="2019">2019</option>
        <option value="2020">2020</option>
        <option value="2021">2021</option>
        <option value="2022">2022</option>
        <option value="2023">2023</option> <!-- new option -->
    </select>
    ```
2. Change the inital value, e.g. for the year 2023 like this:
    ```javascript
        var chart;
        var timeFormat = 'MM/DD/YYYY HH:mm';
        var factor = 191422.8/1000000.0;
        var value = '2023'; // initial value
    ```
3. Copy the whole html code into your WIX object.
