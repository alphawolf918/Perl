#!/usr/local/bin/perl

print "Content-type: text/html\r\n\r\n";
print '<html>';
print '<head>';
print '</head>';
print '<body>';
print "<div style=\"font-weight: bold;\">Environment Variables:</div>";
print '<div style="width: 650px;">';
foreach(sort keys %ENV){
	print "<div><strong>".$_."</strong>: ".$ENV{$_}."<br/>";
}
print '</div>';
print '</body>';
print '</html>';