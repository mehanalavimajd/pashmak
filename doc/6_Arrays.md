# Arrays
arrays are a list from variables

look at this example:

```bash
set $names;
mem ['parsa' , 'pashmak' , 'jack'];
copy $names;

out $names; # output: ['parsa' , 'pashmak' , 'jack']
mem $names[0]; out ^; # output: parsa
mem $names[1]; out ^; # output: pashmak
mem $names[2]; out ^; # output: jack
```

this is a example about array and loop:

```bash
set $names;
mem ['parsa' , 'pashmak' , 'jack'];
copy $names;

set $i; mem 0; copy $i;

section loop;
    mem $names[$i] + '\n'; out ^;
    mem $i + 1; copy $i;
mem $i < len($names); gotoif loop;
```

output:

```
parsa
pashmak
jack
```

that prints names one by one

### arraypush
you can add a item to array:

```bash
set $myarray; mem ['red' , 'green' , 'blue']; copy $myarray;
out $myarray; # output: ['red' , 'green' , 'blue']

mem 'yellow'; arraypush $myarray ^; # add mem (^) to the $myarray
out $myarray; # output: ['red' , 'green' , 'blue' , 'yellow']
```

### arraypop
you can delete a item from array:

```bash
set $myarray; mem ['red' , 'green' , 'blue']; copy $myarray;
out $myarray; # output: ['red' , 'green' , 'blue']

mem 1; arraypop $myarray ^; # remove index mem (^) from $myarray
out $myarray; # output: ['red' , 'blue']
```