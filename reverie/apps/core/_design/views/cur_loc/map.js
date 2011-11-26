 function(doc) {
   if (doc.doc_type == "CharLog")
    emit([doc.char_id, doc.type], {"date": doc.date, "lat": doc.lat, "long": doc.long});
 }