 function(doc) {
   if (doc.doc_type == "CharLog")
    emit([doc.char_id], null);
 }