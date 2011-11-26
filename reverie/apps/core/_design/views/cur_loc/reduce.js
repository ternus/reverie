 function(key, values, rereduce) {
    var maxdate = values[0];
    values.forEach(function(value){
        if (value.date > maxdate.date)
            maxdate = value;
     });
     return maxdate;
 }