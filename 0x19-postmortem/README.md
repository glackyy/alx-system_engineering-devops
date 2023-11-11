# Postmortem: Unexpected Outage of Ubuntu 14.04 Container Running Apache Web Server

On November 10, 2023, at approximately 20:00 Greenwich Mean Time (GMT) in Morocco (Casablanca), an unexpected outage struck an isolated Ubuntu 14.04 container running an Apache web server. Instead of the anticipated HTML file showcasing a simple Holberton WordPress site, GET requests to the server were met with an unwelcome 500 Internal Server Error.

## Troubleshooting Journey:

The task of resolving this issue fell to WhizWarden, a dedicated bug debugger known for their enigmatic coding skills. WhizWarden was alerted to the problem at approximately 19:20 PST and immediately jumped into action.

## Initial Assessment:

WhizWarden began the debugging process by examining the system. A quick "ps aux" command revealed that two Apache processes were running normally: one as root and the other as www-data.

## Configuration Exploration:

Next, WhizWarden ventured into the "sites-available" folder within the "/etc/apache2/" directory to ensure that the web server was set up to serve content from the "/var/www/html/" directory.

## Strace Investigation:

To gain deeper insights, WhizWarden executed the "strace" command on the PID of the root Apache process in one terminal while curling the server in another. This initial attempt yielded no valuable information.

## www-data Breakthrough:

Undeterred, WhizWarden decided to try a similar approach with the PID of the "www-data" process. Expectations were subdued, but the effort bore fruit. The "strace" output indicated an "-1 ENOENT" (No such file or directory) error while attempting to access the file "/var/www/html/wp-includes/class-wp-locale.phpp."

## Identifying the Culprit:

With a newfound clue in hand, WhizWarden delved into the "/var/www/html/" directory, meticulously examining each file using Vim's pattern-matching capabilities. Success was achieved when the erroneous ".phpp" file extension was spotted within the "wp-settings.php" file, specifically on Line 137, where "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );" was causing the trouble.

## Corrective Action:

WhizWarden swiftly rectified the issue by removing the erroneous trailing 'p' from the line in "wp-settings.php."

## Test and Automation:

A final curl test on the server resulted in a satisfying 200 OK response. Not content with a simple fix, WhizWarden decided to create a Puppet manifest to automate the resolution of similar errors in the future.

## In Summary:

In a nutshell, this incident boiled down to a typo—a common and age-old nemesis of programmers. Specifically, the WordPress application encountered a critical error due to the mistaken inclusion of "class-wp-locale.phpp" in "wp-settings.php," when the correct filename, residing in the "wp-content" directory, should have been "class-wp-locale.php." The fix was straightforward: removing the extra 'p.'

## Preventative Measures:

To ensure such outages do not recur, let's take these precautions:

Rigorous Testing: Thoroughly test applications before deployment to catch potential issues early.
Uptime Monitoring: Implement a reliable uptime monitoring service to instantly alert you to website outages.
Automation: In response to this incident, a Puppet manifest was developed to automatically correct similar errors. However, we're all human, so let's embrace the philosophy that errors can and do happen, and plan accordingly.

## Conclusion

In the world of coding, it's not a matter of "if" but "when" we'll encounter those elusive bugs. However, by following the preventative measures outlined above, we can minimize the frequency and impact of these outages.