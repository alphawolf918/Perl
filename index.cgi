#!/usr/local/bin/perl

print "Content-type: text/html\r\n\r\n";
print '<html>';
print '<head>';
print '<title>Perl Env</title>';
print '</head>';
print '<body>';
print "<div style=\"font-weight: bold;\">Environment Variables:</div>";
print '<div style="width: 650px; overflow: hidden;">';
foreach(sort keys %ENV){
	print "<div style='width: 85%;'> &nbsp; &nbsp; <strong>".$_."</strong>: ".$ENV{$_}."</div>";
}
print '</div>';
print '</body>';
print '</html>';