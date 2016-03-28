#!/usr/local/bin/perl

# Kelvin Abrokwa-Johnson
# Homework 4
# myfind.pl
# This program implements *nix `find` with options ls grep name pwd.
# ls cannot be combined with grep or pwd

use Cwd;
use strict;

my $ls = 0;
my $pwd = 0;
my $nameArg;
my $grep = 0;
my $dirArg = ".";
my $dirArgSet = 0;
my $noFlags = 0;

sub glob2pat {
    my $globstr = shift;
    my %patmap = (
        '*' => '.*',
        '?' => '.',
        '[' => '[',
        ']' => ']',
    );
    $globstr =~ s{(.)} { $patmap{$1} || "\Q$1" }ge;
    return '^' . $globstr . '$';
}

# parse arguments
while (@ARGV) {
    my $arg = shift;
    if ($dirArgSet == 0) {
        $dirArg = $arg;
        $dirArgSet = 1;
    } elsif ($arg eq '-name') {
        $nameArg = glob2pat(shift);
    } elsif ($arg eq '-ls') {
        $ls = 1;
    } elsif ($arg eq '-pwd') {
        $pwd = 1;
    } elsif ($arg eq '-grep') {
        $grep = shift;
    }
}

sub ScanDirectory {
    my ($workdir) = shift;

    my ($startdir) = &cwd; # keep track of where we began

    chdir($workdir) or die "Unable to enter dir $workdir:$!\n";
    opendir(DIR, ".") or die "Unable to open $workdir:$!\n";
    my @names = readdir(DIR) or die "Unable to read $workdir:$!\n";
    closedir(DIR);

    foreach my $name (@names){
        next if ($name eq ".");
        next if ($name eq "..");

        if (-d $name) {
            &ScanDirectory($name);
            next;
        }
        my $out = 1;
        if ($nameArg) {
            if ($name !~ m/$nameArg/) { # move on if name doesn't match
                next;
            }
        }
        if ($pwd) {
            $name = &cwd . "/" . $name;
        }
        if ($ls) {
            system("ls -l $name");
            $out = 0;
        }
        if ($grep) {
            my $lineNum = 0;
            open my $content, $name or die "Could not open file: $name\n";
            while (my $line = <$content>) {
                $lineNum++;
                if ($line =~ m/$grep/) {
                    print "$name: $lineNum: $line";
                }
            }
            $out = 0;
        }
        if ($out == 1) {
            print "$name\n";
        }
    }
    chdir($startdir) or die "Unable to change to dir $startdir:$!\n";
}

&ScanDirectory($dirArg);
