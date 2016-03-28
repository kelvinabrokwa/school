
my $mystartdir = ".";

if (@ARGV > 0)  { $mystartdir = shift; }

opendir(DIR,$mystartdir) or die "Can't open the current directory: $!\n";

# read file/directory names in that directory into @names 
@names = readdir(DIR) or die "Unable to read current dir:$!\n";

closedir(DIR);

foreach $name (@names) {
   next if ($name eq ".");   # skip the current directory entry
   next if ($name eq "..");  # skip the parent  directory entry

   if (-d $name){            # is this a directory?
      print "found a directory: $name\n";
      next;                  # can skip to the next name in the for loop 
   }
   if ($name eq "core") {    # is this a file named "core"?
     print "found one!\n"; 
  }
}

