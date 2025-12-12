// read.js
// This script functions to read, process, and present the data

// variables

var unpacked_data = vbuck_csv_data;  // csv data in text format
var new_array = [];

var current_vbuck_count = 0;

var positive_color = "#19ff4b";
var negative_color = "#ff5c5c";
var neutral_color = "#00a8ff";

// functions

function convert_data() {
    // converts the long string into a array
    // split data by new line

    new_array = unpacked_data.split("\n");

    // pack into more arrays
    for (var i = 0; i < new_array.length; i++) {
        new_array[i] = new_array[i].split(",");
    };

    console.log(new_array);

    // it should now be in the format of
    // DATE, SEASON, AMOUNT, VALUE, CHANGE, VALUE CHANGE, REASON
};

function read_last_entry() {
    // reads the last entry in csv file
    return new_array[new_array.length - 1];
};

function on_page_load() {
    //console.log(unpacked_data);
    // runs on page load
    convert_data();

    var current_vbuck_count = read_last_entry()[2];
    document.getElementById("vbuck_count").innerHTML = current_vbuck_count;
    //console.log(current_vbuck_count);
};

// main

on_page_load();
