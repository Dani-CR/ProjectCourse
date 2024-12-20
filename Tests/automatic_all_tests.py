import os
import subprocess

#command start applications
commands_app=["", #CS03
"" #CS04
]

commands_fuzzers=["",#restler
"", #evomaster
"", #cats
""#schemathesis
]

min_run=[5,10]

commands_jacoco=["", #begin restler cs03
"", #end restler cs03
"", #begin evo cs03
"", #end evo cs03
"", #begin st cs03
"", #end st cs03
"", #begin restler cs04
"", #end restler cs04
"", #begin evo cs04
"", #end evo cs04
"", #begin st cs04
"", #end st cs04
]

for app in commands_app:
    for fuzzer in commands_fuzzers:
        for i in min_run:
            #
