Reflection - Why each collection fits a different use
A list fits the observations because it keeps order and keeps duplicates. We have 8 observations, WELL-07 appears twice, and a list keeps both.
A dictionary fits one observation because each value has a label, like well_id, field, pressure_psi. It is clear and easy to read by key.
A set fits unique wells and fields because it removes duplicates automatically. From 8 readings we get 6 unique wells and 3 fields: east, north, south.
A tuple fits measurement units like ("psi", "m") because units should never change. A tuple protects them from accidental change.
Together, they let us keep every reading, find the mean pressure, and count per well without losing data.