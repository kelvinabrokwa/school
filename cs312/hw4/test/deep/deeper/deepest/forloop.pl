@one_to_ten = (1 .. 10); 
$top_limit = 25; 

for $i (@one_to_ten, 15, 20 .. $top_limit) { 

   print "$i\n"; 
}

