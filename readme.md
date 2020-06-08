Calculator
------

A simple in game calculator plugin for [MCDaemon](https://github.com/kafuuchino-desu/MCDaemon) or [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)

For MCDR it needs MCDR version >= `0.9.1-alpha`

## Usage

It will calculate the expression with an extra prefix `==` such as `==1+1`. All unrelated chars will be ignored

Try input `==3*4-(1+3.0)` in game chat and that's it

If module [simpleeval](https://pypi.org/project/simpleeval/) is installed it will use `simpleeval.simple_eval` with names and functions in `math` module for advanced calculation
