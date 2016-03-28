# argv.pl
#! /usr/local/bin/perl

print @ARGV, "\n";
print $ARGV[0], "\n";
print $#ARGV, "\n";

if (@ARGV < 0) {print "0\n"};
if (@ARGV < 1) {print "1\n"};
if (@ARGV < 2) {print "2\n"};

use strict;
my $string = shift;
my $ct = 0;

exit;

