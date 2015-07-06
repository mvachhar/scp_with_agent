# scp_with_agent
Python script that acts as scp, except allows agent forwarding

Use this program as if it were scp.  In other words, if you would do `scp <args>` do `scp_with_agent.py <args>` instead.  If agent forwarding is enabled via `ssh_config` or `~/.ssh/config`, this program will not disable it like standard `scp`.  You can also explicitly enable agent forwarding with `scp_with_agent.py -oForwardAgent=yes`.

The program works by acting as scp when invoked from the command line, but adds the `-S` option which allows specifying the ssh program to use for scp.  The script passes itself as the ssh script to use to the system `scp`.  When used by `scp` by as `ssh` the script will remove the -oForwardAgent=no argument `scp` passes to `ssh` allowing agent forwarding if configured elsewhere, either in a configuration file or on the command line.

The script expects `ssh` and `scp` to be in `/usr/bin`, edit the `ssh_prog` and `scp_prog` variables if your system has these programs in a different location.


